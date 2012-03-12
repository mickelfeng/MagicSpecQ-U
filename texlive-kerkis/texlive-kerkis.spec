%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/kerkis.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/kerkis.doc.tar.xz

Name: texlive-kerkis
License: LPPL
Summary: Kerkis (Greek) font family
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(kerkis.sty)
Provides: tex(kmath.sty)
Requires: tex(txfonts.sty)
Requires: texlive-kerkis-fedora-fonts = %{tl_version}

%description
Sans-serif Greek fonts to match the URW Bookman set (which are
distributed with Kerkis). The Kerkis font set has some support
for mathematics as well as other glyphs missing from the base
URW Bookman fonts (the URW fonts are duplicated in the
distribution). Macros are provided to use the fonts in OT1, T1
(only NG/ng glyphs missing) and LGR encodings, as well as in
mathematics; small caps and old-style number glyphs are also
available. The philosophy, and the design process, of the
Kerkis fonts is discussed in a paper in TUGboat 23(3/4), 2002.

date: 2009-01-15 17:16:29 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map kerkis.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map kerkis.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for kerkis
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for kerkis

%package fedora-fonts
Summary: Fonts for kerkis
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-kerkis = %{tl_version}
BuildArch: noarch

%description fedora-fonts
Sans-serif Greek fonts to match the URW Bookman set (which are
distributed with Kerkis). The Kerkis font set has some support
for mathematics as well as other glyphs missing from the base
URW Bookman fonts (the URW fonts are duplicated in the
distribution). Macros are provided to use the fonts in OT1, T1
(only NG/ng glyphs missing) and LGR encodings, as well as in
mathematics; small caps and old-style number glyphs are also
available. The philosophy, and the design process, of the
Kerkis fonts is discussed in a paper in TUGboat 23(3/4), 2002.

date: 2009-01-15 17:16:29 +0100


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/lppl.txt lppl.txt
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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis-Bold.pfb .
ln -s %{_fontdir}/Kerkis-Bold.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis-Bold.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis-BoldItalic.pfb .
ln -s %{_fontdir}/Kerkis-BoldItalic.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis-BoldItalic.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis-BoldSmallCaps.pfb .
ln -s %{_fontdir}/Kerkis-BoldSmallCaps.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis-BoldSmallCaps.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis-Calligraphic.pfb .
ln -s %{_fontdir}/Kerkis-Calligraphic.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis-Calligraphic.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis-Italic.pfb .
ln -s %{_fontdir}/Kerkis-Italic.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis-Italic.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis-SemiBold-Italic.pfb .
ln -s %{_fontdir}/Kerkis-SemiBold-Italic.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis-SemiBold-Italic.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis-SemiBold.pfb .
ln -s %{_fontdir}/Kerkis-SemiBold.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis-SemiBold.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis-SmallCaps.pfb .
ln -s %{_fontdir}/Kerkis-SmallCaps.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis-SmallCaps.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis.pfb .
ln -s %{_fontdir}/Kerkis.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/KerkisSans-Bold.pfb .
ln -s %{_fontdir}/KerkisSans-Bold.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/KerkisSans-Bold.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/KerkisSans-BoldItalic.pfb .
ln -s %{_fontdir}/KerkisSans-BoldItalic.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/KerkisSans-BoldItalic.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/KerkisSans-Italic.pfb .
ln -s %{_fontdir}/KerkisSans-Italic.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/KerkisSans-Italic.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/KerkisSans-SmallCaps.pfb .
ln -s %{_fontdir}/KerkisSans-SmallCaps.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/KerkisSans-SmallCaps.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/KerkisSans.pfb .
ln -s %{_fontdir}/KerkisSans.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/KerkisSans.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/ktsy.pfb .
ln -s %{_fontdir}/ktsy.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis/ktsy.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/fonts/afm/public/kerkis/Kerkis-Bold.afm
%{_texdir}/texmf-dist/fonts/afm/public/kerkis/Kerkis-BoldItalic.afm
%{_texdir}/texmf-dist/fonts/afm/public/kerkis/Kerkis-BoldSmallCaps.afm
%{_texdir}/texmf-dist/fonts/afm/public/kerkis/Kerkis-Calligraphic.afm
%{_texdir}/texmf-dist/fonts/afm/public/kerkis/Kerkis-Italic.afm
%{_texdir}/texmf-dist/fonts/afm/public/kerkis/Kerkis-SemiBold-Italic.afm
%{_texdir}/texmf-dist/fonts/afm/public/kerkis/Kerkis-SemiBold.afm
%{_texdir}/texmf-dist/fonts/afm/public/kerkis/Kerkis-SmallCaps.afm
%{_texdir}/texmf-dist/fonts/afm/public/kerkis/Kerkis.afm
%{_texdir}/texmf-dist/fonts/afm/public/kerkis/KerkisSans-Bold.afm
%{_texdir}/texmf-dist/fonts/afm/public/kerkis/KerkisSans-BoldItalic.afm
%{_texdir}/texmf-dist/fonts/afm/public/kerkis/KerkisSans-Italic.afm
%{_texdir}/texmf-dist/fonts/afm/public/kerkis/KerkisSans-SmallCaps.afm
%{_texdir}/texmf-dist/fonts/afm/public/kerkis/KerkisSans.afm
%{_texdir}/texmf-dist/fonts/afm/public/kerkis/ktsy.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/kerkis/gkerkis.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/kerkis/gkerkisc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/kerkis/gpkerkis.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/kerkis/gpkerkisc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/kerkis/kerkis.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/kerkis/kerkisc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/kerkis/kerkisec.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/kerkis/kerkisecsc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/kerkis/kmath.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/kerkis/kmex.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/kerkis/kmsym.enc
%{_texdir}/texmf-dist/fonts/map/dvips/kerkis/kerkis.map
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ek8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ek8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ekb8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ekb8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ekbi8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ekbi8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ekbo8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ekbo8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ekbsc8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ekbsc8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ekbsco8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ekbsco8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ekbui8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ekbui8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ekcal8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ekcal8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eki8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eki8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eko8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eko8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eksb8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eksb8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eksbi8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eksbi8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eksbo8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eksbo8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eksbui8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eksbui8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eksc8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eksc8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eksco8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eksco8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eksf8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eksf8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eksfb8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eksfb8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eksfbi8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eksfbi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eksfi8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eksfi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eksfsc8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/eksfsc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ekui8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ekui8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gk7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gk7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gkb7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gkb7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gkbi7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gkbi7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gkbo7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gkbo7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gkbsc8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gkbsc8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gkbsco8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gkbsco8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gkbui7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gkbui7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gkcal7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gkcal7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gki7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gki7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gko7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gko7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gksb7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gksb7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gksbi7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gksbi7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gksbo7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gksbo7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gksbui7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gksbui7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gksc7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gksc7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gksco7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gksco7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gksf7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gksf7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gksfb7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gksfb7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gksfbi7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gksfbi7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gksfi7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gksfi7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gksfsc7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gksfsc7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gkui7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/gkui7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/k8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/k8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/kb8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/kb8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/kbi8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/kbi8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/kbo8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/kbo8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/kbsc8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/kbsc8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/kbsco8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/kbsco8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/kbui8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/kbui8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/kcal8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/kcal8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ki8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ki8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/kmath8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/kmath8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ko8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ko8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ksb8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ksb8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ksbi8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ksbi8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ksbo8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ksbo8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ksbui8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ksbui8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ksc8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ksc8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ksco8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ksco8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ksf8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ksf8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ksfb8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ksfb8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ksfbi8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ksfbi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ksfi8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ksfi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ksfsc8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ksfsc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ktsy8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/ktsy8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/kui8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/kerkis/kui8r.tfm
%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis-Bold.pfb
%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis-BoldItalic.pfb
%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis-BoldSmallCaps.pfb
%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis-Calligraphic.pfb
%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis-Italic.pfb
%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis-SemiBold-Italic.pfb
%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis-SemiBold.pfb
%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis-SmallCaps.pfb
%{_texdir}/texmf-dist/fonts/type1/public/kerkis/Kerkis.pfb
%{_texdir}/texmf-dist/fonts/type1/public/kerkis/KerkisSans-Bold.pfb
%{_texdir}/texmf-dist/fonts/type1/public/kerkis/KerkisSans-BoldItalic.pfb
%{_texdir}/texmf-dist/fonts/type1/public/kerkis/KerkisSans-Italic.pfb
%{_texdir}/texmf-dist/fonts/type1/public/kerkis/KerkisSans-SmallCaps.pfb
%{_texdir}/texmf-dist/fonts/type1/public/kerkis/KerkisSans.pfb
%{_texdir}/texmf-dist/fonts/type1/public/kerkis/ktsy.pfb
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/ek8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/ekb8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/ekbi8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/ekbo8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/ekbsc8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/ekbsco8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/ekbui8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/ekcal8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/eki8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/eko8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/eksb8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/eksbi8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/eksbo8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/eksbui8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/eksc8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/eksco8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/eksf8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/eksfb8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/eksfbi8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/eksfi8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/eksfsc8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/ekui8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/gk7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/gkb7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/gkbi7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/gkbo7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/gkbsc8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/gkbsco8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/gkbui7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/gkcal7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/gki7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/gko7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/gksb7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/gksbi7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/gksbo7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/gksbui7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/gksc7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/gksco7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/gksf7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/gksfb7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/gksfbi7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/gksfi7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/gksfsc7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/gkui7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/k8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/kb8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/kbi8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/kbo8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/kbsc8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/kbsco8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/kbui8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/kcal8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/ki8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/kmath8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/ko8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/ksb8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/ksbi8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/ksbo8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/ksbui8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/ksc8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/ksco8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/ksf8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/ksfb8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/ksfbi8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/ksfi8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/ksfsc8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/ktsy8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/kerkis/kui8a.vf
%{_texdir}/texmf-dist/tex/latex/kerkis/kerkis.sty
%{_texdir}/texmf-dist/tex/latex/kerkis/kmath.sty
%{_texdir}/texmf-dist/tex/latex/kerkis/lgrkfn.fd
%{_texdir}/texmf-dist/tex/latex/kerkis/lgrmak.fd
%{_texdir}/texmf-dist/tex/latex/kerkis/lgrmaksf.fd
%{_texdir}/texmf-dist/tex/latex/kerkis/omlmak.fd
%{_texdir}/texmf-dist/tex/latex/kerkis/omsmak.fd
%{_texdir}/texmf-dist/tex/latex/kerkis/ot1kfn.fd
%{_texdir}/texmf-dist/tex/latex/kerkis/ot1mak.fd
%{_texdir}/texmf-dist/tex/latex/kerkis/ot1maksf.fd
%{_texdir}/texmf-dist/tex/latex/kerkis/t1mak.fd
%{_texdir}/texmf-dist/tex/latex/kerkis/t1maksf.fd

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/kerkis/License.txt
%{_texdir}/texmf-dist/doc/latex/kerkis/README.html

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/Kerkis-Bold.pfb
%{_fontdir}/Kerkis-BoldItalic.pfb
%{_fontdir}/Kerkis-BoldSmallCaps.pfb
%{_fontdir}/Kerkis-Calligraphic.pfb
%{_fontdir}/Kerkis-Italic.pfb
%{_fontdir}/Kerkis-SemiBold-Italic.pfb
%{_fontdir}/Kerkis-SemiBold.pfb
%{_fontdir}/Kerkis-SmallCaps.pfb
%{_fontdir}/Kerkis.pfb
%{_fontdir}/KerkisSans-Bold.pfb
%{_fontdir}/KerkisSans-BoldItalic.pfb
%{_fontdir}/KerkisSans-Italic.pfb
%{_fontdir}/KerkisSans-SmallCaps.pfb
%{_fontdir}/KerkisSans.pfb
%{_fontdir}/ktsy.pfb

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
