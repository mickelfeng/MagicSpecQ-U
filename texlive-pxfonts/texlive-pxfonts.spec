%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/pxfonts.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/pxfonts.doc.tar.xz

Name: texlive-pxfonts
License: GPL+
Summary: Palatino-like fonts in support of mathematics
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(pxfonts.sty)
Requires: texlive-pxfonts-fedora-fonts = %{tl_version}

%description
Pxfonts supplies virtual text roman fonts using Adobe Palatino
(or URWPalladioL) with some modified and additional text
symbols in the OT1, T1, and TS1 encodings; maths alphabets
using Palatino/Palladio; maths fonts providing all the symbols
of the Computer Modern and AMS fonts, including all the Greek
capital letters from CMR; and additional maths fonts of various
other symbols. The set is complemented by a sans-serif set of
text fonts, based on Helvetica/NimbusSanL, and a monospace set
derived from the parallel TX font set. All the fonts are in
Type 1 format (AFM and PFB files), and are supported by TeX
metrics (VF and TFM files) and macros for use with LaTeX.

date: 2009-01-15 09:33:18 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map pxfonts.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map pxfonts.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  %{_bindir}/texhash 2> /dev/null
  %{_bindir}/updmap-sys --nohash --quiet &> /dev/null
else
  mkdir -p /var/run/texlive
  touch /var/run/texlive/run-texhash
  touch /var/run/texlive/run-updmap
fi
:

%posttrans
[ -e /var/run/texlive/run-texhash ] && %{_bindir}/texhash 2> /dev/null && rm -f /var/run/texlive/run-texhash
[ -e /var/run/texlive/run-updmap ] && %{_bindir}/updmap-sys --nohash --quiet &> /dev/null && rm -f /var/run/texlive/run-updmap
[ -e /var/run/texlive ] && rm -rf /var/run/texlive
:

%package doc
Summary: Documentation for pxfonts
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for pxfonts

%package fedora-fonts
Summary: Fonts for pxfonts
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-pxfonts = %{tl_version}
BuildArch: noarch

%description fedora-fonts
Pxfonts supplies virtual text roman fonts using Adobe Palatino
(or URWPalladioL) with some modified and additional text
symbols in the OT1, T1, and TS1 encodings; maths alphabets
using Palatino/Palladio; maths fonts providing all the symbols
of the Computer Modern and AMS fonts, including all the Greek
capital letters from CMR; and additional maths fonts of various
other symbols. The set is complemented by a sans-serif set of
text fonts, based on Helvetica/NimbusSanL, and a monospace set
derived from the parallel TX font set. All the fonts are in
Type 1 format (AFM and PFB files), and are supported by TeX
metrics (VF and TFM files) and macros for use with LaTeX.

date: 2009-01-15 09:33:18 +0100


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/gpl.txt gpl.txt
xz -dc %{SOURCE0} | tar x -C %{buildroot}%{_texdir}/texmf-dist
xz -dc %{SOURCE1} | tar x -C %{buildroot}%{_texdir}/texmf-dist
# nuke useless tlmgr packaging stuff and doc droppings
rm -rf %{buildroot}%{_texdir}/tlpkg/tlpobj/
rm -rf %{buildroot}%{_texdir}/texmf-dist/tlpkg/tlpobj/
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/man*/*.pdf
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/Makefile
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/man*/Makefile
rm -rf %{buildroot}%{_texdir}/texmf/doc/info/dir

# link installed fonts with Fedora
install -d -m 0755 %{buildroot}%{_fontdir}
pushd %{buildroot}%{_fontdir}
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxbex.pfb .
ln -s %{_fontdir}/pxbex.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxbex.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxbexa.pfb .
ln -s %{_fontdir}/pxbexa.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxbexa.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxbmia.pfb .
ln -s %{_fontdir}/pxbmia.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxbmia.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxbsy.pfb .
ln -s %{_fontdir}/pxbsy.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxbsy.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxbsya.pfb .
ln -s %{_fontdir}/pxbsya.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxbsya.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxbsyb.pfb .
ln -s %{_fontdir}/pxbsyb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxbsyb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxbsyc.pfb .
ln -s %{_fontdir}/pxbsyc.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxbsyc.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxex.pfb .
ln -s %{_fontdir}/pxex.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxex.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxexa.pfb .
ln -s %{_fontdir}/pxexa.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxexa.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxmia.pfb .
ln -s %{_fontdir}/pxmia.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxmia.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxsy.pfb .
ln -s %{_fontdir}/pxsy.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxsy.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxsya.pfb .
ln -s %{_fontdir}/pxsya.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxsya.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxsyb.pfb .
ln -s %{_fontdir}/pxsyb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxsyb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxsyc.pfb .
ln -s %{_fontdir}/pxsyc.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxsyc.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpcxb.pfb .
ln -s %{_fontdir}/rpcxb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpcxb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpcxbi.pfb .
ln -s %{_fontdir}/rpcxbi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpcxbi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpcxi.pfb .
ln -s %{_fontdir}/rpcxi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpcxi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpcxr.pfb .
ln -s %{_fontdir}/rpcxr.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpcxr.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpxb.pfb .
ln -s %{_fontdir}/rpxb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpxb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpxbi.pfb .
ln -s %{_fontdir}/rpxbi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpxbi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpxbmi.pfb .
ln -s %{_fontdir}/rpxbmi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpxbmi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpxbsc.pfb .
ln -s %{_fontdir}/rpxbsc.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpxbsc.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpxi.pfb .
ln -s %{_fontdir}/rpxi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpxi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpxmi.pfb .
ln -s %{_fontdir}/rpxmi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpxmi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpxr.pfb .
ln -s %{_fontdir}/rpxr.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpxr.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpxsc.pfb .
ln -s %{_fontdir}/rpxsc.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpxsc.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/pxbex.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/pxbexa.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/pxbmia.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/pxbsy.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/pxbsya.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/pxbsyb.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/pxbsyc.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/pxex.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/pxexa.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/pxmia.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/pxsy.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/pxsya.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/pxsyb.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/pxsyc.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/rpcxb.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/rpcxbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/rpcxi.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/rpcxr.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/rpxb.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/rpxbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/rpxbmi.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/rpxbsc.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/rpxi.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/rpxmi.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/rpxr.afm
%{_texdir}/texmf-dist/fonts/afm/public/pxfonts/rpxsc.afm
%{_texdir}/texmf-dist/fonts/map/dvips/pxfonts/pxfonts.map
%{_texdir}/texmf-dist/fonts/map/dvips/pxfonts/pxr.map
%{_texdir}/texmf-dist/fonts/map/dvips/pxfonts/pxr1.map
%{_texdir}/texmf-dist/fonts/map/dvips/pxfonts/pxr2.map
%{_texdir}/texmf-dist/fonts/map/dvips/pxfonts/pxr3.map
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/p1xb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/p1xbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/p1xbsc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/p1xbsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/p1xi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/p1xr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/p1xsc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/p1xsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pcxb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pcxbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pcxbsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pcxi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pcxr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pcxsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxbex.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxbexa.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxbmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxbmi1.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxbmia.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxbsc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxbsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxbsy.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxbsya.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxbsyb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxbsyc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxex.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxexa.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxmi1.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxmia.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxsc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxsy.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxsya.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxsyb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/pxsyc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/rpcxb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/rpcxbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/rpcxbsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/rpcxi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/rpcxr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/rpcxsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/rpxb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/rpxbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/rpxbmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/rpxbsc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/rpxbsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/rpxi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/rpxmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/rpxpplb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/rpxpplbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/rpxpplbo.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/rpxpplr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/rpxpplri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/rpxpplro.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/rpxr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/rpxsc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts/rpxsl.tfm
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxbex.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxbexa.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxbmia.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxbsy.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxbsya.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxbsyb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxbsyc.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxex.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxexa.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxmia.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxsy.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxsya.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxsyb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/pxsyc.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpcxb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpcxbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpcxi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpcxr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpxb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpxbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpxbmi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpxbsc.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpxi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpxmi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpxr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pxfonts/rpxsc.pfb
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/p1xb.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/p1xbi.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/p1xbsc.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/p1xbsl.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/p1xi.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/p1xr.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/p1xsc.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/p1xsl.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/pcxb.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/pcxbi.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/pcxbsl.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/pcxi.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/pcxr.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/pcxsl.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/pxb.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/pxbi.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/pxbmi.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/pxbmi1.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/pxbsc.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/pxbsl.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/pxi.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/pxmi.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/pxmi1.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/pxr.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/pxsc.vf
%{_texdir}/texmf-dist/fonts/vf/public/pxfonts/pxsl.vf
%{_texdir}/texmf-dist/tex/latex/pxfonts/omlpxmi.fd
%{_texdir}/texmf-dist/tex/latex/pxfonts/omlpxr.fd
%{_texdir}/texmf-dist/tex/latex/pxfonts/omspxr.fd
%{_texdir}/texmf-dist/tex/latex/pxfonts/omspxsy.fd
%{_texdir}/texmf-dist/tex/latex/pxfonts/omxpxex.fd
%{_texdir}/texmf-dist/tex/latex/pxfonts/ot1pxr.fd
%{_texdir}/texmf-dist/tex/latex/pxfonts/ot1pxss.fd
%{_texdir}/texmf-dist/tex/latex/pxfonts/ot1pxtt.fd
%{_texdir}/texmf-dist/tex/latex/pxfonts/pxfonts.sty
%{_texdir}/texmf-dist/tex/latex/pxfonts/t1pxr.fd
%{_texdir}/texmf-dist/tex/latex/pxfonts/t1pxss.fd
%{_texdir}/texmf-dist/tex/latex/pxfonts/t1pxtt.fd
%{_texdir}/texmf-dist/tex/latex/pxfonts/ts1pxr.fd
%{_texdir}/texmf-dist/tex/latex/pxfonts/ts1pxss.fd
%{_texdir}/texmf-dist/tex/latex/pxfonts/ts1pxtt.fd
%{_texdir}/texmf-dist/tex/latex/pxfonts/upxexa.fd
%{_texdir}/texmf-dist/tex/latex/pxfonts/upxmia.fd
%{_texdir}/texmf-dist/tex/latex/pxfonts/upxr.fd
%{_texdir}/texmf-dist/tex/latex/pxfonts/upxss.fd
%{_texdir}/texmf-dist/tex/latex/pxfonts/upxsya.fd
%{_texdir}/texmf-dist/tex/latex/pxfonts/upxsyb.fd
%{_texdir}/texmf-dist/tex/latex/pxfonts/upxsyc.fd
%{_texdir}/texmf-dist/tex/latex/pxfonts/upxtt.fd

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/fonts/pxfonts/00bug_fix.txt
%{_texdir}/texmf-dist/doc/fonts/pxfonts/COPYRIGHT
%{_texdir}/texmf-dist/doc/fonts/pxfonts/pxfontsdoc.pdf
%{_texdir}/texmf-dist/doc/fonts/pxfonts/pxfontsdoc.tex
%{_texdir}/texmf-dist/doc/fonts/pxfonts/pxfontsdocA4.pdf
%{_texdir}/texmf-dist/doc/fonts/pxfonts/pxfontsdocA4.tex

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/pxbex.pfb
%{_fontdir}/pxbexa.pfb
%{_fontdir}/pxbmia.pfb
%{_fontdir}/pxbsy.pfb
%{_fontdir}/pxbsya.pfb
%{_fontdir}/pxbsyb.pfb
%{_fontdir}/pxbsyc.pfb
%{_fontdir}/pxex.pfb
%{_fontdir}/pxexa.pfb
%{_fontdir}/pxmia.pfb
%{_fontdir}/pxsy.pfb
%{_fontdir}/pxsya.pfb
%{_fontdir}/pxsyb.pfb
%{_fontdir}/pxsyc.pfb
%{_fontdir}/rpcxb.pfb
%{_fontdir}/rpcxbi.pfb
%{_fontdir}/rpcxi.pfb
%{_fontdir}/rpcxr.pfb
%{_fontdir}/rpxb.pfb
%{_fontdir}/rpxbi.pfb
%{_fontdir}/rpxbmi.pfb
%{_fontdir}/rpxbsc.pfb
%{_fontdir}/rpxi.pfb
%{_fontdir}/rpxmi.pfb
%{_fontdir}/rpxr.pfb
%{_fontdir}/rpxsc.pfb

%changelog
* Mon Aug 23 2010 Jindrich Novy <jnovy@redhat.com> 2010-9
- rpmlint fixes

* Sat Jul 17 2010 Jindrich Novy <jnovy@redhat.com> 2010-8
- depend on the new texlive-base noarch package
- ship licenses with documentation
- sync with upstream

* Mon May 31 2010 Jindrich Novy <jnovy@redhat.com> 2010-7
- switch to "tlpretest" source tree
- add lua and ruby dependencies to packages requiring them
- generate global package database "texlive.tlpdb" directly from
tlpobj files shipped with each package

* Wed May 19 2010 Jindrich Novy <jnovy@redhat.com> 2010-6
- update to the latest frozen development TeX Live
- add svn to noarch versions according to guildelines

* Fri Apr 30 2010 Jindrich Novy <jnovy@redhat.com> 2010-5
- add dependencies resolution among biblatex files
- another %%postun scriplets fix

* Wed Apr 21 2010 Jindrich Novy <jnovy@redhat.com> 2010-4
- fix and tighten dependencies in %%post* scriptlets
- extract dependencies also from .cls and .ldf files
- speed up build by skipping some bits in __os_install_post

* Mon Apr 19 2010 Jindrich Novy <jnovy@redhat.com> 2010-3
- speed up installation/updating by running updmap/fmtutil
and texhash post-transaction once

* Sat Apr 03 2010 Jindrich Novy <jnovy@redhat.com> 2010-0.1
- bump version to 2010
- reduce total number of packages from 3580 to 3440 by removal
of dummy ones not shipping actually anything
- add style dependencies from packages reecently added
(were previously blacklisted)
- do not ship koma-script sources

* Tue Nov 10 2009 Jindrich Novy <jnovy@redhat.com> 2009-4
- info and man pages are now part of main packages, not -doc
- use fedora-compliant license codes for License in spec
- fix fedora-fonts packages generation
- add dummy description if packages misses any
- package bdf fonts

* Tue Nov 10 2009 Jindrich Novy <jnovy@redhat.com> 2009-2
- install man and info pages into proper locations visible
by man and info
- update scriptlets
- remove xindy bits

* Mon Nov 09 2009 Jindrich Novy <jnovy@redhat.com> 2009-1
- official TeX Live 2009 release

* Tue Aug 25 2009 Jindrich Novy <jnovy@redhat.com> 2009-0.3
- make TeX Live TrueType and OpenType fonts accessible by
other Fedora apps

* Thu Aug 20 2009 Jindrich Novy <jnovy@redhat.com> 2009-0.2
- don't package generated pdfs from man pages

* Wed Aug 12 2009 Jindrich Novy <jnovy@redhat.com> 2009-0.1
- initial packaging for TeX Live 2009
