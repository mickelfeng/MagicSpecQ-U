%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/initials.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/initials.doc.tar.xz

Name: texlive-initials
License: LPPL
Summary: Adobe Type 1 decorative initial fonts
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-initials-fedora-fonts = %{tl_version}

%description
For each font, at least an .pfb and .tfm file is provided, with
a .fd file for use with LaTeX.

date: 2008-08-19 23:32:24 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map Acorn.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map AnnSton.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map ArtNouv.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map ArtNouvc.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map Carrickc.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map Eichenla.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map Eileen.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map EileenBl.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map Elzevier.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map GotIn.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map GoudyIn.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map Kinigcap.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map Konanur.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map Kramer.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map MorrisIn.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map Nouveaud.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map Romantik.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map Rothdn.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map RoyalIn.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map Sanremo.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map Starburst.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map Typocaps.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map Zallman.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map Acorn.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map AnnSton.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map ArtNouv.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map ArtNouvc.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map Carrickc.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map Eichenla.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map Eileen.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map EileenBl.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map Elzevier.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map GotIn.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map GoudyIn.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map Kinigcap.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map Konanur.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map Kramer.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map MorrisIn.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map Nouveaud.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map Romantik.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map Rothdn.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map RoyalIn.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map Sanremo.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map Starburst.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map Typocaps.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map Zallman.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for initials
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for initials

%package fedora-fonts
Summary: Fonts for initials
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-initials = %{tl_version}
BuildArch: noarch

%description fedora-fonts
For each font, at least an .pfb and .tfm file is provided, with
a .fd file for use with LaTeX.

date: 2008-08-19 23:32:24 +0200


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Acorn.pfb .
ln -s %{_fontdir}/Acorn.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Acorn.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/AnnSton.pfb .
ln -s %{_fontdir}/AnnSton.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/AnnSton.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/ArtNouv.pfb .
ln -s %{_fontdir}/ArtNouv.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/ArtNouv.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/ArtNouvc.pfb .
ln -s %{_fontdir}/ArtNouvc.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/ArtNouvc.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Carrickc.pfb .
ln -s %{_fontdir}/Carrickc.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Carrickc.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Eichenla.pfb .
ln -s %{_fontdir}/Eichenla.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Eichenla.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Eileen.pfb .
ln -s %{_fontdir}/Eileen.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Eileen.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/EileenBl.pfb .
ln -s %{_fontdir}/EileenBl.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/EileenBl.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Elzevier.pfb .
ln -s %{_fontdir}/Elzevier.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Elzevier.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/GotIn.pfb .
ln -s %{_fontdir}/GotIn.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/GotIn.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/GoudyIn.pfb .
ln -s %{_fontdir}/GoudyIn.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/GoudyIn.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Kinigcap.pfb .
ln -s %{_fontdir}/Kinigcap.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Kinigcap.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Konanur.pfb .
ln -s %{_fontdir}/Konanur.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Konanur.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Kramer.pfb .
ln -s %{_fontdir}/Kramer.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Kramer.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/MorrisIn.pfb .
ln -s %{_fontdir}/MorrisIn.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/MorrisIn.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Nouveaud.pfb .
ln -s %{_fontdir}/Nouveaud.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Nouveaud.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Romantik.pfb .
ln -s %{_fontdir}/Romantik.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Romantik.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Rothdn.pfb .
ln -s %{_fontdir}/Rothdn.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Rothdn.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/RoyalIn.pfb .
ln -s %{_fontdir}/RoyalIn.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/RoyalIn.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Sanremo.pfb .
ln -s %{_fontdir}/Sanremo.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Sanremo.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Starburst.pfb .
ln -s %{_fontdir}/Starburst.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Starburst.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Typocaps.pfb .
ln -s %{_fontdir}/Typocaps.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Typocaps.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Zallman.pfb .
ln -s %{_fontdir}/Zallman.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials/Zallman.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/dvips/initials/config.Acorn
%{_texdir}/texmf-dist/dvips/initials/config.AnnSton
%{_texdir}/texmf-dist/dvips/initials/config.ArtNouv
%{_texdir}/texmf-dist/dvips/initials/config.ArtNouvc
%{_texdir}/texmf-dist/dvips/initials/config.Carrickc
%{_texdir}/texmf-dist/dvips/initials/config.Eichenla
%{_texdir}/texmf-dist/dvips/initials/config.Eileen
%{_texdir}/texmf-dist/dvips/initials/config.EileenBl
%{_texdir}/texmf-dist/dvips/initials/config.Elzevier
%{_texdir}/texmf-dist/dvips/initials/config.GotIn
%{_texdir}/texmf-dist/dvips/initials/config.GoudyIn
%{_texdir}/texmf-dist/dvips/initials/config.Kinigcap
%{_texdir}/texmf-dist/dvips/initials/config.Konanur
%{_texdir}/texmf-dist/dvips/initials/config.Kramer
%{_texdir}/texmf-dist/dvips/initials/config.MorrisIn
%{_texdir}/texmf-dist/dvips/initials/config.Nouveaud
%{_texdir}/texmf-dist/dvips/initials/config.Romantik
%{_texdir}/texmf-dist/dvips/initials/config.Rothdn
%{_texdir}/texmf-dist/dvips/initials/config.RoyalIn
%{_texdir}/texmf-dist/dvips/initials/config.Sanremo
%{_texdir}/texmf-dist/dvips/initials/config.Starburst
%{_texdir}/texmf-dist/dvips/initials/config.Typocaps
%{_texdir}/texmf-dist/dvips/initials/config.Zallman
%{_texdir}/texmf-dist/fonts/afm/public/initials/Acorn.afm
%{_texdir}/texmf-dist/fonts/afm/public/initials/AnnSton.afm
%{_texdir}/texmf-dist/fonts/afm/public/initials/ArtNouv.afm
%{_texdir}/texmf-dist/fonts/afm/public/initials/ArtNouvc.afm
%{_texdir}/texmf-dist/fonts/afm/public/initials/Carrickc.afm
%{_texdir}/texmf-dist/fonts/afm/public/initials/Eichenla.afm
%{_texdir}/texmf-dist/fonts/afm/public/initials/Eileen.afm
%{_texdir}/texmf-dist/fonts/afm/public/initials/EileenBl.afm
%{_texdir}/texmf-dist/fonts/afm/public/initials/Elzevier.afm
%{_texdir}/texmf-dist/fonts/afm/public/initials/GotIn.afm
%{_texdir}/texmf-dist/fonts/afm/public/initials/GoudyIn.afm
%{_texdir}/texmf-dist/fonts/afm/public/initials/Kinigcap.afm
%{_texdir}/texmf-dist/fonts/afm/public/initials/Konanur.afm
%{_texdir}/texmf-dist/fonts/afm/public/initials/Kramer.afm
%{_texdir}/texmf-dist/fonts/afm/public/initials/MorrisIn.afm
%{_texdir}/texmf-dist/fonts/afm/public/initials/Nouveaud.afm
%{_texdir}/texmf-dist/fonts/afm/public/initials/Romantik.afm
%{_texdir}/texmf-dist/fonts/afm/public/initials/Rothdn.afm
%{_texdir}/texmf-dist/fonts/afm/public/initials/RoyalIn.afm
%{_texdir}/texmf-dist/fonts/afm/public/initials/Sanremo.afm
%{_texdir}/texmf-dist/fonts/afm/public/initials/Starburst.afm
%{_texdir}/texmf-dist/fonts/afm/public/initials/Typocaps.afm
%{_texdir}/texmf-dist/fonts/afm/public/initials/Zallman.afm
%{_texdir}/texmf-dist/fonts/map/dvips/initials/Acorn.map
%{_texdir}/texmf-dist/fonts/map/dvips/initials/AnnSton.map
%{_texdir}/texmf-dist/fonts/map/dvips/initials/ArtNouv.map
%{_texdir}/texmf-dist/fonts/map/dvips/initials/ArtNouvc.map
%{_texdir}/texmf-dist/fonts/map/dvips/initials/Carrickc.map
%{_texdir}/texmf-dist/fonts/map/dvips/initials/Eichenla.map
%{_texdir}/texmf-dist/fonts/map/dvips/initials/Eileen.map
%{_texdir}/texmf-dist/fonts/map/dvips/initials/EileenBl.map
%{_texdir}/texmf-dist/fonts/map/dvips/initials/Elzevier.map
%{_texdir}/texmf-dist/fonts/map/dvips/initials/GotIn.map
%{_texdir}/texmf-dist/fonts/map/dvips/initials/GoudyIn.map
%{_texdir}/texmf-dist/fonts/map/dvips/initials/Kinigcap.map
%{_texdir}/texmf-dist/fonts/map/dvips/initials/Konanur.map
%{_texdir}/texmf-dist/fonts/map/dvips/initials/Kramer.map
%{_texdir}/texmf-dist/fonts/map/dvips/initials/MorrisIn.map
%{_texdir}/texmf-dist/fonts/map/dvips/initials/Nouveaud.map
%{_texdir}/texmf-dist/fonts/map/dvips/initials/Romantik.map
%{_texdir}/texmf-dist/fonts/map/dvips/initials/Rothdn.map
%{_texdir}/texmf-dist/fonts/map/dvips/initials/RoyalIn.map
%{_texdir}/texmf-dist/fonts/map/dvips/initials/Sanremo.map
%{_texdir}/texmf-dist/fonts/map/dvips/initials/Starburst.map
%{_texdir}/texmf-dist/fonts/map/dvips/initials/Typocaps.map
%{_texdir}/texmf-dist/fonts/map/dvips/initials/Zallman.map
%{_texdir}/texmf-dist/fonts/tfm/public/initials/Acorn.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/initials/AnnSton.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/initials/ArtNouv.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/initials/ArtNouvc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/initials/Carrickc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/initials/Eichenla.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/initials/Eileen.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/initials/EileenBl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/initials/Elzevier.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/initials/GotIn.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/initials/GoudyIn.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/initials/Kinigcap.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/initials/Konanur.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/initials/Kramer.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/initials/MorrisIn.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/initials/Nouveaud.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/initials/Romantik.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/initials/Rothdn.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/initials/RoyalIn.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/initials/Sanremo.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/initials/Starburst.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/initials/Typocaps.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/initials/Zallman.tfm
%{_texdir}/texmf-dist/fonts/type1/public/initials/Acorn.pfb
%{_texdir}/texmf-dist/fonts/type1/public/initials/AnnSton.pfb
%{_texdir}/texmf-dist/fonts/type1/public/initials/ArtNouv.pfb
%{_texdir}/texmf-dist/fonts/type1/public/initials/ArtNouvc.pfb
%{_texdir}/texmf-dist/fonts/type1/public/initials/Carrickc.pfb
%{_texdir}/texmf-dist/fonts/type1/public/initials/Eichenla.pfb
%{_texdir}/texmf-dist/fonts/type1/public/initials/Eileen.pfb
%{_texdir}/texmf-dist/fonts/type1/public/initials/EileenBl.pfb
%{_texdir}/texmf-dist/fonts/type1/public/initials/Elzevier.pfb
%{_texdir}/texmf-dist/fonts/type1/public/initials/GotIn.pfb
%{_texdir}/texmf-dist/fonts/type1/public/initials/GoudyIn.pfb
%{_texdir}/texmf-dist/fonts/type1/public/initials/Kinigcap.pfb
%{_texdir}/texmf-dist/fonts/type1/public/initials/Konanur.pfb
%{_texdir}/texmf-dist/fonts/type1/public/initials/Kramer.pfb
%{_texdir}/texmf-dist/fonts/type1/public/initials/MorrisIn.pfb
%{_texdir}/texmf-dist/fonts/type1/public/initials/Nouveaud.pfb
%{_texdir}/texmf-dist/fonts/type1/public/initials/Romantik.pfb
%{_texdir}/texmf-dist/fonts/type1/public/initials/Rothdn.pfb
%{_texdir}/texmf-dist/fonts/type1/public/initials/RoyalIn.pfb
%{_texdir}/texmf-dist/fonts/type1/public/initials/Sanremo.pfb
%{_texdir}/texmf-dist/fonts/type1/public/initials/Starburst.pfb
%{_texdir}/texmf-dist/fonts/type1/public/initials/Typocaps.pfb
%{_texdir}/texmf-dist/fonts/type1/public/initials/Zallman.pfb
%{_texdir}/texmf-dist/tex/latex/initials/Acorn.fd
%{_texdir}/texmf-dist/tex/latex/initials/AnnSton.fd
%{_texdir}/texmf-dist/tex/latex/initials/ArtNouv.fd
%{_texdir}/texmf-dist/tex/latex/initials/ArtNouvc.fd
%{_texdir}/texmf-dist/tex/latex/initials/Carrickc.fd
%{_texdir}/texmf-dist/tex/latex/initials/Eichenla.fd
%{_texdir}/texmf-dist/tex/latex/initials/Eileen.fd
%{_texdir}/texmf-dist/tex/latex/initials/EileenBl.fd
%{_texdir}/texmf-dist/tex/latex/initials/Elzevier.fd
%{_texdir}/texmf-dist/tex/latex/initials/GotIn.fd
%{_texdir}/texmf-dist/tex/latex/initials/GoudyIn.fd
%{_texdir}/texmf-dist/tex/latex/initials/Kinigcap.fd
%{_texdir}/texmf-dist/tex/latex/initials/Konanur.fd
%{_texdir}/texmf-dist/tex/latex/initials/Kramer.fd
%{_texdir}/texmf-dist/tex/latex/initials/MorrisIn.fd
%{_texdir}/texmf-dist/tex/latex/initials/Nouveaud.fd
%{_texdir}/texmf-dist/tex/latex/initials/Romantik.fd
%{_texdir}/texmf-dist/tex/latex/initials/Rothdn.fd
%{_texdir}/texmf-dist/tex/latex/initials/RoyalIn.fd
%{_texdir}/texmf-dist/tex/latex/initials/Sanremo.fd
%{_texdir}/texmf-dist/tex/latex/initials/Starburst.fd
%{_texdir}/texmf-dist/tex/latex/initials/Typocaps.fd
%{_texdir}/texmf-dist/tex/latex/initials/Zallman.fd

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/fonts/initials/Acorn.tex
%{_texdir}/texmf-dist/doc/fonts/initials/AnnSton.tex
%{_texdir}/texmf-dist/doc/fonts/initials/ArtNouv.tex
%{_texdir}/texmf-dist/doc/fonts/initials/ArtNouvc.tex
%{_texdir}/texmf-dist/doc/fonts/initials/Carrickc.tex
%{_texdir}/texmf-dist/doc/fonts/initials/Eichenla.tex
%{_texdir}/texmf-dist/doc/fonts/initials/Eileen.tex
%{_texdir}/texmf-dist/doc/fonts/initials/EileenBl.tex
%{_texdir}/texmf-dist/doc/fonts/initials/Elzevier.tex
%{_texdir}/texmf-dist/doc/fonts/initials/GotIn.tex
%{_texdir}/texmf-dist/doc/fonts/initials/GoudyIn.tex
%{_texdir}/texmf-dist/doc/fonts/initials/Kinigcap.tex
%{_texdir}/texmf-dist/doc/fonts/initials/Konanur.tex
%{_texdir}/texmf-dist/doc/fonts/initials/Kramer.tex
%{_texdir}/texmf-dist/doc/fonts/initials/MorrisIn.tex
%{_texdir}/texmf-dist/doc/fonts/initials/Nouveaud.tex
%{_texdir}/texmf-dist/doc/fonts/initials/README
%{_texdir}/texmf-dist/doc/fonts/initials/Romantik.tex
%{_texdir}/texmf-dist/doc/fonts/initials/Rothdn.tex
%{_texdir}/texmf-dist/doc/fonts/initials/RoyalIn.tex
%{_texdir}/texmf-dist/doc/fonts/initials/Sanremo.tex
%{_texdir}/texmf-dist/doc/fonts/initials/Starburst.tex
%{_texdir}/texmf-dist/doc/fonts/initials/Typocaps.tex
%{_texdir}/texmf-dist/doc/fonts/initials/Zallman.tex

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/Acorn.pfb
%{_fontdir}/AnnSton.pfb
%{_fontdir}/ArtNouv.pfb
%{_fontdir}/ArtNouvc.pfb
%{_fontdir}/Carrickc.pfb
%{_fontdir}/Eichenla.pfb
%{_fontdir}/Eileen.pfb
%{_fontdir}/EileenBl.pfb
%{_fontdir}/Elzevier.pfb
%{_fontdir}/GotIn.pfb
%{_fontdir}/GoudyIn.pfb
%{_fontdir}/Kinigcap.pfb
%{_fontdir}/Konanur.pfb
%{_fontdir}/Kramer.pfb
%{_fontdir}/MorrisIn.pfb
%{_fontdir}/Nouveaud.pfb
%{_fontdir}/Romantik.pfb
%{_fontdir}/Rothdn.pfb
%{_fontdir}/RoyalIn.pfb
%{_fontdir}/Sanremo.pfb
%{_fontdir}/Starburst.pfb
%{_fontdir}/Typocaps.pfb
%{_fontdir}/Zallman.pfb

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
