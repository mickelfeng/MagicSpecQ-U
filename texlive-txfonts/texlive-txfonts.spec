%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/txfonts.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/txfonts.doc.tar.xz

Name: texlive-txfonts
License: GPL+
Summary: Times-like fonts in support of mathematics
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(txfonts.sty)
Requires: texlive-txfonts-fedora-fonts = %{tl_version}

%description
Txfonts supplies virtual text roman fonts using Adobe Times (or
URW NimbusRomNo9L) with some modified and additional text
symbols in the OT1, T1, and TS1 encodings; maths alphabets
using Times/URW Nimbus; maths fonts providing all the symbols
of the Computer Modern and AMS fonts, including all the Greek
capital letters from CMR; and additional maths fonts of various
other symbols. The set is complemented by a sans-serif set of
text fonts, based on Helvetica/NimbusSanL, and a monospace set.
All the fonts are in Type 1 format (AFM and PFB files), and are
supported by TeX metrics (VF and TFM files) and macros for use
with LaTeX.

date: 2009-01-15 09:33:18 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map txfonts.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map txfonts.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for txfonts
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for txfonts

%package fedora-fonts
Summary: Fonts for txfonts
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-txfonts = %{tl_version}
BuildArch: noarch

%description fedora-fonts
Txfonts supplies virtual text roman fonts using Adobe Times (or
URW NimbusRomNo9L) with some modified and additional text
symbols in the OT1, T1, and TS1 encodings; maths alphabets
using Times/URW Nimbus; maths fonts providing all the symbols
of the Computer Modern and AMS fonts, including all the Greek
capital letters from CMR; and additional maths fonts of various
other symbols. The set is complemented by a sans-serif set of
text fonts, based on Helvetica/NimbusSanL, and a monospace set.
All the fonts are in Type 1 format (AFM and PFB files), and are
supported by TeX metrics (VF and TFM files) and macros for use
with LaTeX.

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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtcxb.pfb .
ln -s %{_fontdir}/rtcxb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtcxb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtcxbi.pfb .
ln -s %{_fontdir}/rtcxbi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtcxbi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtcxbss.pfb .
ln -s %{_fontdir}/rtcxbss.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtcxbss.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtcxi.pfb .
ln -s %{_fontdir}/rtcxi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtcxi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtcxr.pfb .
ln -s %{_fontdir}/rtcxr.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtcxr.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtcxss.pfb .
ln -s %{_fontdir}/rtcxss.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtcxss.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxb.pfb .
ln -s %{_fontdir}/rtxb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxbi.pfb .
ln -s %{_fontdir}/rtxbi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxbi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxbmi.pfb .
ln -s %{_fontdir}/rtxbmi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxbmi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxbsc.pfb .
ln -s %{_fontdir}/rtxbsc.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxbsc.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxbss.pfb .
ln -s %{_fontdir}/rtxbss.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxbss.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxbsssc.pfb .
ln -s %{_fontdir}/rtxbsssc.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxbsssc.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxi.pfb .
ln -s %{_fontdir}/rtxi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxmi.pfb .
ln -s %{_fontdir}/rtxmi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxmi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxr.pfb .
ln -s %{_fontdir}/rtxr.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxr.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxsc.pfb .
ln -s %{_fontdir}/rtxsc.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxsc.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxss.pfb .
ln -s %{_fontdir}/rtxss.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxss.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxsssc.pfb .
ln -s %{_fontdir}/rtxsssc.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxsssc.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/t1xbtt.pfb .
ln -s %{_fontdir}/t1xbtt.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/t1xbtt.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/t1xbttsc.pfb .
ln -s %{_fontdir}/t1xbttsc.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/t1xbttsc.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/t1xtt.pfb .
ln -s %{_fontdir}/t1xtt.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/t1xtt.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/t1xttsc.pfb .
ln -s %{_fontdir}/t1xttsc.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/t1xttsc.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/tcxbtt.pfb .
ln -s %{_fontdir}/tcxbtt.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/tcxbtt.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/tcxtt.pfb .
ln -s %{_fontdir}/tcxtt.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/tcxtt.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbex.pfb .
ln -s %{_fontdir}/txbex.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbex.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbexa.pfb .
ln -s %{_fontdir}/txbexa.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbexa.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbmia.pfb .
ln -s %{_fontdir}/txbmia.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbmia.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbsy.pfb .
ln -s %{_fontdir}/txbsy.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbsy.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbsya.pfb .
ln -s %{_fontdir}/txbsya.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbsya.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbsyb.pfb .
ln -s %{_fontdir}/txbsyb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbsyb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbsyc.pfb .
ln -s %{_fontdir}/txbsyc.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbsyc.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbtt.pfb .
ln -s %{_fontdir}/txbtt.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbtt.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbttsc.pfb .
ln -s %{_fontdir}/txbttsc.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbttsc.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txex.pfb .
ln -s %{_fontdir}/txex.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txex.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txexa.pfb .
ln -s %{_fontdir}/txexa.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txexa.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txmia.pfb .
ln -s %{_fontdir}/txmia.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txmia.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txsy.pfb .
ln -s %{_fontdir}/txsy.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txsy.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txsya.pfb .
ln -s %{_fontdir}/txsya.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txsya.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txsyb.pfb .
ln -s %{_fontdir}/txsyb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txsyb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txsyc.pfb .
ln -s %{_fontdir}/txsyc.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txsyc.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txtt.pfb .
ln -s %{_fontdir}/txtt.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txtt.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txttsc.pfb .
ln -s %{_fontdir}/txttsc.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txttsc.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/rtcxb.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/rtcxbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/rtcxbss.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/rtcxi.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/rtcxr.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/rtcxss.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/rtxb.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/rtxbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/rtxbmi.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/rtxbsc.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/rtxbss.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/rtxbsssc.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/rtxi.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/rtxmi.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/rtxr.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/rtxsc.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/rtxss.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/rtxsssc.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/t1xbtt.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/t1xbttsc.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/t1xtt.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/t1xttsc.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/tcxbtt.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/tcxtt.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/txbex.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/txbexa.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/txbmia.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/txbsy.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/txbsya.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/txbsyb.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/txbsyc.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/txbtt.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/txbttsc.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/txex.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/txexa.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/txmia.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/txsy.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/txsya.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/txsyb.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/txsyc.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/txtt.afm
%{_texdir}/texmf-dist/fonts/afm/public/txfonts/txttsc.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/txfonts/tx8r.enc
%{_texdir}/texmf-dist/fonts/map/dvips/txfonts/txfonts.map
%{_texdir}/texmf-dist/fonts/map/dvips/txfonts/txr.map
%{_texdir}/texmf-dist/fonts/map/dvips/txfonts/txr1.map
%{_texdir}/texmf-dist/fonts/map/dvips/txfonts/txr2.map
%{_texdir}/texmf-dist/fonts/map/dvips/txfonts/txr3.map
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtcxb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtcxbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtcxbsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtcxbss.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtcxbsso.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtcxi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtcxr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtcxsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtcxss.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtcxsssl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxbmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxbsc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxbsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxbss.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxbsssc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxbsssl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxphvb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxphvbo.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxphvr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxphvro.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxptmb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxptmbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxptmbo.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxptmr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxptmri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxptmro.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxsc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxss.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxsssc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/rtxsssl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/t1xb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/t1xbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/t1xbsc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/t1xbsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/t1xbss.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/t1xbsssc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/t1xbsssl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/t1xbtt.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/t1xbttsc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/t1xbttsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/t1xi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/t1xr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/t1xsc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/t1xsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/t1xss.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/t1xsssc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/t1xsssl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/t1xtt.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/t1xttsc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/t1xttsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tcxb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tcxbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tcxbsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tcxbss.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tcxbsssl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tcxbtt.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tcxbttsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tcxi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tcxr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tcxsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tcxss.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tcxsssl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tcxtt.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tcxttsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txbex.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txbexa.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txbmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txbmi1.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txbmia.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txbsc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txbsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txbss.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txbsssc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txbsssl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txbsy.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txbsya.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txbsyb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txbsyc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txbtt.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txbttsc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txbttsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txex.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txexa.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txmi1.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txmia.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txsc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txss.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txsssc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txsssl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txsy.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txsya.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txsyb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txsyc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txtt.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txttsc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/txttsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tyxb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tyxbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tyxbsc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tyxbsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tyxbss.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tyxbsssc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tyxbsssl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tyxbtt.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tyxbttsc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tyxbttsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tyxi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tyxr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tyxsc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tyxsl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tyxss.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tyxsssc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tyxsssl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tyxtt.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tyxttsc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/txfonts/tyxttsl.tfm
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtcxb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtcxbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtcxbss.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtcxi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtcxr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtcxss.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxbmi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxbsc.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxbss.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxbsssc.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxmi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxsc.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxss.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/rtxsssc.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/t1xbtt.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/t1xbttsc.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/t1xtt.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/t1xttsc.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/tcxbtt.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/tcxtt.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbex.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbexa.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbmia.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbsy.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbsya.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbsyb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbsyc.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbtt.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txbttsc.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txex.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txexa.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txmia.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txsy.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txsya.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txsyb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txsyc.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txtt.pfb
%{_texdir}/texmf-dist/fonts/type1/public/txfonts/txttsc.pfb
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/t1xb.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/t1xbi.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/t1xbsc.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/t1xbsl.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/t1xbss.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/t1xbsssc.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/t1xbsssl.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/t1xi.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/t1xr.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/t1xsc.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/t1xsl.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/t1xss.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/t1xsssc.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/t1xsssl.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tcxb.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tcxbi.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tcxbsl.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tcxbss.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tcxbsssl.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tcxi.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tcxr.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tcxsl.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tcxss.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tcxsssl.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/txb.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/txbi.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/txbmi.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/txbmi1.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/txbsc.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/txbsl.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/txbss.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/txbsssc.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/txbsssl.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/txi.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/txmi.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/txmi1.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/txr.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/txsc.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/txsl.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/txss.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/txsssc.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/txsssl.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tyxb.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tyxbi.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tyxbsc.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tyxbsl.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tyxbss.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tyxbsssc.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tyxbsssl.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tyxbtt.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tyxbttsc.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tyxbttsl.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tyxi.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tyxr.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tyxsc.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tyxsl.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tyxss.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tyxsssc.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tyxsssl.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tyxtt.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tyxttsc.vf
%{_texdir}/texmf-dist/fonts/vf/public/txfonts/tyxttsl.vf
%{_texdir}/texmf-dist/tex/latex/txfonts/ly1txr.fd
%{_texdir}/texmf-dist/tex/latex/txfonts/ly1txss.fd
%{_texdir}/texmf-dist/tex/latex/txfonts/ly1txtt.fd
%{_texdir}/texmf-dist/tex/latex/txfonts/omltxmi.fd
%{_texdir}/texmf-dist/tex/latex/txfonts/omltxr.fd
%{_texdir}/texmf-dist/tex/latex/txfonts/omstxr.fd
%{_texdir}/texmf-dist/tex/latex/txfonts/omstxsy.fd
%{_texdir}/texmf-dist/tex/latex/txfonts/omxtxex.fd
%{_texdir}/texmf-dist/tex/latex/txfonts/ot1txr.fd
%{_texdir}/texmf-dist/tex/latex/txfonts/ot1txss.fd
%{_texdir}/texmf-dist/tex/latex/txfonts/ot1txtt.fd
%{_texdir}/texmf-dist/tex/latex/txfonts/t1txr.fd
%{_texdir}/texmf-dist/tex/latex/txfonts/t1txss.fd
%{_texdir}/texmf-dist/tex/latex/txfonts/t1txtt.fd
%{_texdir}/texmf-dist/tex/latex/txfonts/ts1txr.fd
%{_texdir}/texmf-dist/tex/latex/txfonts/ts1txss.fd
%{_texdir}/texmf-dist/tex/latex/txfonts/ts1txtt.fd
%{_texdir}/texmf-dist/tex/latex/txfonts/txfonts.sty
%{_texdir}/texmf-dist/tex/latex/txfonts/utxexa.fd
%{_texdir}/texmf-dist/tex/latex/txfonts/utxmia.fd
%{_texdir}/texmf-dist/tex/latex/txfonts/utxr.fd
%{_texdir}/texmf-dist/tex/latex/txfonts/utxss.fd
%{_texdir}/texmf-dist/tex/latex/txfonts/utxsya.fd
%{_texdir}/texmf-dist/tex/latex/txfonts/utxsyb.fd
%{_texdir}/texmf-dist/tex/latex/txfonts/utxsyc.fd
%{_texdir}/texmf-dist/tex/latex/txfonts/utxtt.fd

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/fonts/txfonts/00bug_fix.txt
%{_texdir}/texmf-dist/doc/fonts/txfonts/COPYRIGHT
%{_texdir}/texmf-dist/doc/fonts/txfonts/README
%{_texdir}/texmf-dist/doc/fonts/txfonts/txfontsdoc.pdf
%{_texdir}/texmf-dist/doc/fonts/txfonts/txfontsdoc.tex
%{_texdir}/texmf-dist/doc/fonts/txfonts/txfontsdocA4.pdf
%{_texdir}/texmf-dist/doc/fonts/txfonts/txfontsdocA4.tex
%{_texdir}/texmf-dist/doc/fonts/txfonts/txmi.vpl

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/rtcxb.pfb
%{_fontdir}/rtcxbi.pfb
%{_fontdir}/rtcxbss.pfb
%{_fontdir}/rtcxi.pfb
%{_fontdir}/rtcxr.pfb
%{_fontdir}/rtcxss.pfb
%{_fontdir}/rtxb.pfb
%{_fontdir}/rtxbi.pfb
%{_fontdir}/rtxbmi.pfb
%{_fontdir}/rtxbsc.pfb
%{_fontdir}/rtxbss.pfb
%{_fontdir}/rtxbsssc.pfb
%{_fontdir}/rtxi.pfb
%{_fontdir}/rtxmi.pfb
%{_fontdir}/rtxr.pfb
%{_fontdir}/rtxsc.pfb
%{_fontdir}/rtxss.pfb
%{_fontdir}/rtxsssc.pfb
%{_fontdir}/t1xbtt.pfb
%{_fontdir}/t1xbttsc.pfb
%{_fontdir}/t1xtt.pfb
%{_fontdir}/t1xttsc.pfb
%{_fontdir}/tcxbtt.pfb
%{_fontdir}/tcxtt.pfb
%{_fontdir}/txbex.pfb
%{_fontdir}/txbexa.pfb
%{_fontdir}/txbmia.pfb
%{_fontdir}/txbsy.pfb
%{_fontdir}/txbsya.pfb
%{_fontdir}/txbsyb.pfb
%{_fontdir}/txbsyc.pfb
%{_fontdir}/txbtt.pfb
%{_fontdir}/txbttsc.pfb
%{_fontdir}/txex.pfb
%{_fontdir}/txexa.pfb
%{_fontdir}/txmia.pfb
%{_fontdir}/txsy.pfb
%{_fontdir}/txsya.pfb
%{_fontdir}/txsyb.pfb
%{_fontdir}/txsyc.pfb
%{_fontdir}/txtt.pfb
%{_fontdir}/txttsc.pfb

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
