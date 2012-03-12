%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/semaphor.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/semaphor.doc.tar.xz

Name: texlive-semaphor
License: GPL+
Summary: Semaphore alphabet font
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18651%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-semaphor-fedora-fonts = %{tl_version}

%description
These fonts represent semaphore in a highly schematic, but very
clear, fashion. The fonts are provided as MetaFont source, and
in both OpenType and Adobe Type 1 formats.

date: 2008-04-15 09:54:26 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "MixedMap semaf.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^MixedMap semaf.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for semaphor
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18651%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for semaphor

%package fedora-fonts
Summary: Fonts for semaphor
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18651%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-semaphor = %{tl_version}
BuildArch: noarch

%description fedora-fonts
These fonts represent semaphore in a highly schematic, but very
clear, fashion. The fonts are provided as MetaFont source, and
in both OpenType and Adobe Type 1 formats.

date: 2008-04-15 09:54:26 +0200


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfb10.otf .
ln -s %{_fontdir}/smfb10.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfb10.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfbsl10.otf .
ln -s %{_fontdir}/smfbsl10.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfbsl10.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfeb10.otf .
ln -s %{_fontdir}/smfeb10.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfeb10.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfebsl10.otf .
ln -s %{_fontdir}/smfebsl10.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfebsl10.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfer10.otf .
ln -s %{_fontdir}/smfer10.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfer10.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfesl10.otf .
ln -s %{_fontdir}/smfesl10.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfesl10.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfett10.otf .
ln -s %{_fontdir}/smfett10.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfett10.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfpb10.otf .
ln -s %{_fontdir}/smfpb10.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfpb10.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfpbsl10.otf .
ln -s %{_fontdir}/smfpbsl10.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfpbsl10.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfpr10.otf .
ln -s %{_fontdir}/smfpr10.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfpr10.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfpsl10.otf .
ln -s %{_fontdir}/smfpsl10.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfpsl10.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfptt10.otf .
ln -s %{_fontdir}/smfptt10.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfptt10.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfr10.otf .
ln -s %{_fontdir}/smfr10.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfr10.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfsl10.otf .
ln -s %{_fontdir}/smfsl10.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfsl10.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smftt10.otf .
ln -s %{_fontdir}/smftt10.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smftt10.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfb10.pfb .
ln -s %{_fontdir}/smfb10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfb10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfbsl10.pfb .
ln -s %{_fontdir}/smfbsl10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfbsl10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfeb10.pfb .
ln -s %{_fontdir}/smfeb10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfeb10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfebsl10.pfb .
ln -s %{_fontdir}/smfebsl10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfebsl10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfer10.pfb .
ln -s %{_fontdir}/smfer10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfer10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfesl10.pfb .
ln -s %{_fontdir}/smfesl10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfesl10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfett10.pfb .
ln -s %{_fontdir}/smfett10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfett10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfpb10.pfb .
ln -s %{_fontdir}/smfpb10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfpb10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfpbsl10.pfb .
ln -s %{_fontdir}/smfpbsl10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfpbsl10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfpr10.pfb .
ln -s %{_fontdir}/smfpr10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfpr10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfpsl10.pfb .
ln -s %{_fontdir}/smfpsl10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfpsl10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfptt10.pfb .
ln -s %{_fontdir}/smfptt10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfptt10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfr10.pfb .
ln -s %{_fontdir}/smfr10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfr10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfsl10.pfb .
ln -s %{_fontdir}/smfsl10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfsl10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smftt10.pfb .
ln -s %{_fontdir}/smftt10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smftt10.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/fonts/afm/public/semaphor/smfb10.afm
%{_texdir}/texmf-dist/fonts/afm/public/semaphor/smfbsl10.afm
%{_texdir}/texmf-dist/fonts/afm/public/semaphor/smfeb10.afm
%{_texdir}/texmf-dist/fonts/afm/public/semaphor/smfebsl10.afm
%{_texdir}/texmf-dist/fonts/afm/public/semaphor/smfer10.afm
%{_texdir}/texmf-dist/fonts/afm/public/semaphor/smfesl10.afm
%{_texdir}/texmf-dist/fonts/afm/public/semaphor/smfett10.afm
%{_texdir}/texmf-dist/fonts/afm/public/semaphor/smfpb10.afm
%{_texdir}/texmf-dist/fonts/afm/public/semaphor/smfpbsl10.afm
%{_texdir}/texmf-dist/fonts/afm/public/semaphor/smfpr10.afm
%{_texdir}/texmf-dist/fonts/afm/public/semaphor/smfpsl10.afm
%{_texdir}/texmf-dist/fonts/afm/public/semaphor/smfptt10.afm
%{_texdir}/texmf-dist/fonts/afm/public/semaphor/smfr10-1.afm
%{_texdir}/texmf-dist/fonts/afm/public/semaphor/smfr10-2.afm
%{_texdir}/texmf-dist/fonts/afm/public/semaphor/smfr10.afm
%{_texdir}/texmf-dist/fonts/afm/public/semaphor/smfsl10.afm
%{_texdir}/texmf-dist/fonts/afm/public/semaphor/smftt10.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/semaphor/smfb10.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/semaphor/smfbsl10.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/semaphor/smfeb10.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/semaphor/smfebsl10.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/semaphor/smfer10.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/semaphor/smfesl10.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/semaphor/smfett10.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/semaphor/smfpb10.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/semaphor/smfpbsl10.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/semaphor/smfpr10.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/semaphor/smfpsl10.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/semaphor/smfptt10.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/semaphor/smfr10.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/semaphor/smfsl10.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/semaphor/smftt10.enc
%{_texdir}/texmf-dist/fonts/map/dvips/semaphor/semaf.map
%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfb10.otf
%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfbsl10.otf
%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfeb10.otf
%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfebsl10.otf
%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfer10.otf
%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfesl10.otf
%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfett10.otf
%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfpb10.otf
%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfpbsl10.otf
%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfpr10.otf
%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfpsl10.otf
%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfptt10.otf
%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfr10.otf
%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smfsl10.otf
%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/smftt10.otf
%{_texdir}/texmf-dist/fonts/source/public/semaphor/Makefile
%{_texdir}/texmf-dist/fonts/source/public/semaphor/README
%{_texdir}/texmf-dist/fonts/source/public/semaphor/pfb2otf.pe
%{_texdir}/texmf-dist/fonts/source/public/semaphor/semaf.mp
%{_texdir}/texmf-dist/fonts/source/public/semaphor/smfb10.mp
%{_texdir}/texmf-dist/fonts/source/public/semaphor/smfbsl10.mp
%{_texdir}/texmf-dist/fonts/source/public/semaphor/smfeb10.mp
%{_texdir}/texmf-dist/fonts/source/public/semaphor/smfebsl10.mp
%{_texdir}/texmf-dist/fonts/source/public/semaphor/smfer10.mp
%{_texdir}/texmf-dist/fonts/source/public/semaphor/smfesl10.mp
%{_texdir}/texmf-dist/fonts/source/public/semaphor/smfett10.mp
%{_texdir}/texmf-dist/fonts/source/public/semaphor/smfpb10.mp
%{_texdir}/texmf-dist/fonts/source/public/semaphor/smfpbsl10.mp
%{_texdir}/texmf-dist/fonts/source/public/semaphor/smfpr10.mp
%{_texdir}/texmf-dist/fonts/source/public/semaphor/smfpsl10.mp
%{_texdir}/texmf-dist/fonts/source/public/semaphor/smfptt10.mp
%{_texdir}/texmf-dist/fonts/source/public/semaphor/smfr10.mp
%{_texdir}/texmf-dist/fonts/source/public/semaphor/smfsl10.mp
%{_texdir}/texmf-dist/fonts/source/public/semaphor/smftt10.mp
%{_texdir}/texmf-dist/fonts/source/public/semaphor/metafont/semaf.mf
%{_texdir}/texmf-dist/fonts/source/public/semaphor/metafont/smfbf10.mf
%{_texdir}/texmf-dist/fonts/source/public/semaphor/metafont/smfebf10.mf
%{_texdir}/texmf-dist/fonts/source/public/semaphor/metafont/smfer10.mf
%{_texdir}/texmf-dist/fonts/source/public/semaphor/metafont/smfesl10.mf
%{_texdir}/texmf-dist/fonts/source/public/semaphor/metafont/smfett10.mf
%{_texdir}/texmf-dist/fonts/source/public/semaphor/metafont/smfpbf10.mf
%{_texdir}/texmf-dist/fonts/source/public/semaphor/metafont/smfpr10.mf
%{_texdir}/texmf-dist/fonts/source/public/semaphor/metafont/smfpsl10.mf
%{_texdir}/texmf-dist/fonts/source/public/semaphor/metafont/smfptt10.mf
%{_texdir}/texmf-dist/fonts/source/public/semaphor/metafont/smfr10.mf
%{_texdir}/texmf-dist/fonts/source/public/semaphor/metafont/smfsl10.mf
%{_texdir}/texmf-dist/fonts/source/public/semaphor/metafont/smftt10.mf
%{_texdir}/texmf-dist/fonts/tfm/public/semaphor/smfb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/semaphor/smfbsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/semaphor/smfeb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/semaphor/smfebsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/semaphor/smfer10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/semaphor/smfesl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/semaphor/smfett10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/semaphor/smfpb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/semaphor/smfpbsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/semaphor/smfpr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/semaphor/smfpsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/semaphor/smfptt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/semaphor/smfr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/semaphor/smfsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/semaphor/smftt10.tfm
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfb10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfb10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfbsl10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfbsl10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfeb10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfeb10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfebsl10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfebsl10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfer10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfer10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfesl10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfesl10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfett10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfett10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfpb10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfpb10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfpbsl10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfpbsl10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfpr10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfpr10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfpsl10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfpsl10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfptt10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfptt10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfr10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfr10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfsl10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smfsl10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smftt10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/smftt10.pfm
%{_texdir}/texmf-dist/tex/context/third/semaphor/t-type-semaf.tex
%{_texdir}/texmf-dist/tex/latex/semaphor/il2semaf.fd
%{_texdir}/texmf-dist/tex/latex/semaphor/semaf.fd
%{_texdir}/texmf-dist/tex/plain/semaphor/semaf.tex

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/fonts/semaphor/README
%{_texdir}/texmf-dist/doc/fonts/semaphor/example.pdf
%{_texdir}/texmf-dist/doc/fonts/semaphor/example.tex
%{_texdir}/texmf-dist/doc/fonts/semaphor/test-context.pdf
%{_texdir}/texmf-dist/doc/fonts/semaphor/test-context.tex

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/smfb10.otf
%{_fontdir}/smfbsl10.otf
%{_fontdir}/smfeb10.otf
%{_fontdir}/smfebsl10.otf
%{_fontdir}/smfer10.otf
%{_fontdir}/smfesl10.otf
%{_fontdir}/smfett10.otf
%{_fontdir}/smfpb10.otf
%{_fontdir}/smfpbsl10.otf
%{_fontdir}/smfpr10.otf
%{_fontdir}/smfpsl10.otf
%{_fontdir}/smfptt10.otf
%{_fontdir}/smfr10.otf
%{_fontdir}/smfsl10.otf
%{_fontdir}/smftt10.otf
%{_fontdir}/smfb10.pfb
%{_fontdir}/smfbsl10.pfb
%{_fontdir}/smfeb10.pfb
%{_fontdir}/smfebsl10.pfb
%{_fontdir}/smfer10.pfb
%{_fontdir}/smfesl10.pfb
%{_fontdir}/smfett10.pfb
%{_fontdir}/smfpb10.pfb
%{_fontdir}/smfpbsl10.pfb
%{_fontdir}/smfpr10.pfb
%{_fontdir}/smfpsl10.pfb
%{_fontdir}/smfptt10.pfb
%{_fontdir}/smfr10.pfb
%{_fontdir}/smfsl10.pfb
%{_fontdir}/smftt10.pfb

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
