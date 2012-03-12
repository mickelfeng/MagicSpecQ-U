%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/pl.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/pl.doc.tar.xz

Name: texlive-pl
License: Public Domain
Summary: Polish extension of CM fonts in Type 1 format
Version: %{tl_version}
Release: %{tl_noarch_release}.1.15.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-pl-fedora-fonts = %{tl_version}

%description
This package is the Polish extension of the Computer Modern
fonts (known as PL fonts),in Adobe Type 1 (PostScript) format.
The fonts use the same .tfm files as for the version generated
by MetaFont. This release of fonts was adapted to the (mostly
guessed) demands of the Windows environment, while keeping the
fonts usable with TeX; however, encoding files are now added,
as Windows and TeX use different encoding schemes.

date: 2009-10-07 21:35:42 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "MixedMap plother.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "MixedMap pltext.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^MixedMap plother.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^MixedMap pltext.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for pl
Version: %{tl_version}
Release: %{tl_noarch_release}.1.15.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for pl

%package fedora-fonts
Summary: Fonts for pl
Version: %{tl_version}
Release: %{tl_noarch_release}.1.15.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-pl = %{tl_version}
BuildArch: noarch

%description fedora-fonts
This package is the Polish extension of the Computer Modern
fonts (known as PL fonts),in Adobe Type 1 (PostScript) format.
The fonts use the same .tfm files as for the version generated
by MetaFont. This release of fonts was adapted to the (mostly
guessed) demands of the Windows environment, while keeping the
fonts usable with TeX; however, encoding files are now added,
as Windows and TeX use different encoding schemes.

date: 2009-10-07 21:35:42 +0200


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/pd.txt pd.txt
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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plb10.pfb .
ln -s %{_fontdir}/plb10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plb10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plbsy10.pfb .
ln -s %{_fontdir}/plbsy10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plbsy10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx10.pfb .
ln -s %{_fontdir}/plbx10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx12.pfb .
ln -s %{_fontdir}/plbx12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx5.pfb .
ln -s %{_fontdir}/plbx5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx6.pfb .
ln -s %{_fontdir}/plbx6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx7.pfb .
ln -s %{_fontdir}/plbx7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx8.pfb .
ln -s %{_fontdir}/plbx8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx9.pfb .
ln -s %{_fontdir}/plbx9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plbxsl10.pfb .
ln -s %{_fontdir}/plbxsl10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plbxsl10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plbxti10.pfb .
ln -s %{_fontdir}/plbxti10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plbxti10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plcsc10.pfb .
ln -s %{_fontdir}/plcsc10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plcsc10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/pldunh10.pfb .
ln -s %{_fontdir}/pldunh10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/pldunh10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plex10.pfb .
ln -s %{_fontdir}/plex10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plex10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plex9.pfb .
ln -s %{_fontdir}/plex9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plex9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plff10.pfb .
ln -s %{_fontdir}/plff10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plff10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plfi10.pfb .
ln -s %{_fontdir}/plfi10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plfi10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plfib8.pfb .
ln -s %{_fontdir}/plfib8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plfib8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plinch.pfb .
ln -s %{_fontdir}/plinch.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plinch.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plitt10.pfb .
ln -s %{_fontdir}/plitt10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plitt10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi10.pfb .
ln -s %{_fontdir}/plmi10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi12.pfb .
ln -s %{_fontdir}/plmi12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi5.pfb .
ln -s %{_fontdir}/plmi5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi6.pfb .
ln -s %{_fontdir}/plmi6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi7.pfb .
ln -s %{_fontdir}/plmi7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi8.pfb .
ln -s %{_fontdir}/plmi8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi9.pfb .
ln -s %{_fontdir}/plmi9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plmib10.pfb .
ln -s %{_fontdir}/plmib10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plmib10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plr10.pfb .
ln -s %{_fontdir}/plr10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plr10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plr12.pfb .
ln -s %{_fontdir}/plr12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plr12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plr17.pfb .
ln -s %{_fontdir}/plr17.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plr17.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plr5.pfb .
ln -s %{_fontdir}/plr5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plr5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plr6.pfb .
ln -s %{_fontdir}/plr6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plr6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plr7.pfb .
ln -s %{_fontdir}/plr7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plr7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plr8.pfb .
ln -s %{_fontdir}/plr8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plr8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plr9.pfb .
ln -s %{_fontdir}/plr9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plr9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plsl10.pfb .
ln -s %{_fontdir}/plsl10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plsl10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plsl12.pfb .
ln -s %{_fontdir}/plsl12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plsl12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plsl8.pfb .
ln -s %{_fontdir}/plsl8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plsl8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plsl9.pfb .
ln -s %{_fontdir}/plsl9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plsl9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plsltt10.pfb .
ln -s %{_fontdir}/plsltt10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plsltt10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plss10.pfb .
ln -s %{_fontdir}/plss10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plss10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plss12.pfb .
ln -s %{_fontdir}/plss12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plss12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plss17.pfb .
ln -s %{_fontdir}/plss17.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plss17.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plss8.pfb .
ln -s %{_fontdir}/plss8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plss8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plss9.pfb .
ln -s %{_fontdir}/plss9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plss9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plssbi10.pfb .
ln -s %{_fontdir}/plssbi10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plssbi10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plssbx10.pfb .
ln -s %{_fontdir}/plssbx10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plssbx10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plssdc10.pfb .
ln -s %{_fontdir}/plssdc10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plssdc10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plssi10.pfb .
ln -s %{_fontdir}/plssi10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plssi10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plssi12.pfb .
ln -s %{_fontdir}/plssi12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plssi12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plssi17.pfb .
ln -s %{_fontdir}/plssi17.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plssi17.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plssi8.pfb .
ln -s %{_fontdir}/plssi8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plssi8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plssi9.pfb .
ln -s %{_fontdir}/plssi9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plssi9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plssq8.pfb .
ln -s %{_fontdir}/plssq8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plssq8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plssqi8.pfb .
ln -s %{_fontdir}/plssqi8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plssqi8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plsy10.pfb .
ln -s %{_fontdir}/plsy10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plsy10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plsy5.pfb .
ln -s %{_fontdir}/plsy5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plsy5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plsy6.pfb .
ln -s %{_fontdir}/plsy6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plsy6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plsy7.pfb .
ln -s %{_fontdir}/plsy7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plsy7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plsy8.pfb .
ln -s %{_fontdir}/plsy8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plsy8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plsy9.pfb .
ln -s %{_fontdir}/plsy9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plsy9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/pltcsc10.pfb .
ln -s %{_fontdir}/pltcsc10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/pltcsc10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/pltex10.pfb .
ln -s %{_fontdir}/pltex10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/pltex10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/pltex8.pfb .
ln -s %{_fontdir}/pltex8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/pltex8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/pltex9.pfb .
ln -s %{_fontdir}/pltex9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/pltex9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plti10.pfb .
ln -s %{_fontdir}/plti10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plti10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plti12.pfb .
ln -s %{_fontdir}/plti12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plti12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plti7.pfb .
ln -s %{_fontdir}/plti7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plti7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plti8.pfb .
ln -s %{_fontdir}/plti8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plti8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plti9.pfb .
ln -s %{_fontdir}/plti9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plti9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/pltt10.pfb .
ln -s %{_fontdir}/pltt10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/pltt10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/pltt12.pfb .
ln -s %{_fontdir}/pltt12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/pltt12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/pltt8.pfb .
ln -s %{_fontdir}/pltt8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/pltt8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/pltt9.pfb .
ln -s %{_fontdir}/pltt9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/pltt9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plu10.pfb .
ln -s %{_fontdir}/plu10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plu10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plvtt10.pfb .
ln -s %{_fontdir}/plvtt10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl/plvtt10.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc pd.txt
%{_texdir}/texmf-dist/dvips/pl/config.pl
%{_texdir}/texmf-dist/fonts/afm/public/pl/plb10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plbsy10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plbx10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plbx12.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plbx5.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plbx6.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plbx7.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plbx8.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plbx9.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plbxsl10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plbxti10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plcsc10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/pldunh10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plex10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plex9.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plff10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plfi10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plfib8.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plinch.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plitt10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plmi10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plmi12.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plmi5.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plmi6.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plmi7.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plmi8.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plmi9.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plmib10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plr10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plr12.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plr17.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plr5.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plr6.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plr7.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plr8.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plr9.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plsl10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plsl12.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plsl8.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plsl9.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plsltt10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plss10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plss12.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plss17.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plss8.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plss9.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plssbi10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plssbx10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plssdc10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plssi10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plssi12.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plssi17.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plssi8.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plssi9.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plssq8.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plssqi8.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plsy10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plsy5.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plsy6.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plsy7.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plsy8.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plsy9.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/pltcsc10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/pltex10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/pltex8.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/pltex9.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plti10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plti12.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plti7.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plti8.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plti9.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/pltt10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/pltt12.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/pltt8.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/pltt9.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plu10.afm
%{_texdir}/texmf-dist/fonts/afm/public/pl/plvtt10.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/pl/plin.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/pl/plit.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/pl/plitt.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/pl/plme.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/pl/plmi.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/pl/plms.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/pl/plrm.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/pl/plsc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/pl/plte.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/pl/pltt.enc
%{_texdir}/texmf-dist/fonts/map/dvips/pl/plother.map
%{_texdir}/texmf-dist/fonts/map/dvips/pl/pltext.map
%{_texdir}/texmf-dist/fonts/source/public/pl/cmssbi10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/dlr10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/fik_mik.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/pl.mft
%{_texdir}/texmf-dist/fonts/source/public/pl/pl_cud.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/pl_dl.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/pl_dod.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/pl_ml.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/pl_mlk.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/pl_sym.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plb10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plbsy10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plbsy5.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plbsy7.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plbx10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plbx12.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plbx5.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plbx6.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plbx7.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plbx8.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plbx9.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plbxsl10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plbxti10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plcsc10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/pldunh10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plex10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plff10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plfi10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plfib8.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plinch.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plitt10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plmi10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plmi12.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plmi5.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plmi6.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plmi7.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plmi8.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plmi9.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plmib10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plmib5.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plmib7.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plr10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plr12.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plr17.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plr5.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plr6.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plr7.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plr8.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plr9.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plsl10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plsl12.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plsl8.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plsl9.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plsltt10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plss10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plss12.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plss17.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plss8.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plss9.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plssbi10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plssbx10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plssdc10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plssi10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plssi12.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plssi17.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plssi8.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plssi9.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plssq8.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plssqi8.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plsy10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plsy5.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plsy6.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plsy7.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plsy8.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plsy9.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/pltcsc10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/pltex10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/pltex8.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/pltex9.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plti10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plti12.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plti7.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plti8.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plti9.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/pltt10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/pltt12.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/pltt8.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/pltt9.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plu10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/plvtt10.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/polan.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/polkap.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/polkur.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/polmat.mf
%{_texdir}/texmf-dist/fonts/source/public/pl/poltyt.mf
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plbsy10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plbsy5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plbsy7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plbx12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plbx5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plbx6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plbx7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plbx8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plbx9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plbxsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plbxti10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plcsc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/pldunh10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plex10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plex9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plff10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plfi10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plfib8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plinch.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plitt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plmi10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plmi12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plmi5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plmi6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plmi7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plmi8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plmi9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plmib10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plmib5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plmib7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plr12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plr17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plr5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plr6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plr7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plr8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plr9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plsl12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plsl8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plsl9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plsltt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plss10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plss12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plss17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plss8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plss9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plssbi10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plssbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plssdc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plssi10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plssi12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plssi17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plssi8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plssi9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plssq8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plssqi8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plsy10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plsy5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plsy6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plsy7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plsy8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plsy9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/pltcsc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/pltex10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/pltex8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/pltex9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plti10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plti12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plti7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plti8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plti9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/pltt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/pltt12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/pltt8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/pltt9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plu10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/pl/plvtt10.tfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plb10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plb10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plbsy10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plbsy10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx12.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx5.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx6.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx7.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plbx9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plbxsl10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plbxsl10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plbxti10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plbxti10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plcsc10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plcsc10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/pldunh10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/pldunh10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plex10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plex10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plex9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plex9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plff10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plff10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plfi10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plfi10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plfib8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plfib8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plinch.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plinch.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plitt10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plitt10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi12.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi5.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi6.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi7.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plmi9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plmib10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plmib10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plr10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plr10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plr12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plr12.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plr17.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plr17.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plr5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plr5.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plr6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plr6.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plr7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plr7.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plr8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plr8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plr9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plr9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plsl10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plsl10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plsl12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plsl12.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plsl8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plsl8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plsl9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plsl9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plsltt10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plsltt10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plss10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plss10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plss12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plss12.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plss17.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plss17.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plss8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plss8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plss9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plss9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plssbi10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plssbi10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plssbx10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plssbx10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plssdc10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plssdc10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plssi10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plssi10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plssi12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plssi12.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plssi17.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plssi17.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plssi8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plssi8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plssi9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plssi9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plssq8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plssq8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plssqi8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plssqi8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plsy10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plsy10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plsy5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plsy5.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plsy6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plsy6.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plsy7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plsy7.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plsy8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plsy8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plsy9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plsy9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/pltcsc10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/pltcsc10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/pltex10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/pltex10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/pltex8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/pltex8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/pltex9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/pltex9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plti10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plti10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plti12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plti12.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plti7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plti7.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plti8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plti8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plti9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plti9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/pltt10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/pltt10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/pltt12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/pltt12.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/pltt8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/pltt8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/pltt9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/pltt9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plu10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plu10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/pl/plvtt10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/pl/plvtt10.pfm

%files doc
%defattr(-,root,root)
%doc pd.txt
%{_texdir}/texmf-dist/doc/fonts/pl/README-T1.ENG
%{_texdir}/texmf-dist/doc/fonts/pl/README-T1.POL
%{_texdir}/texmf-dist/doc/fonts/pl/README.ENG
%{_texdir}/texmf-dist/doc/fonts/pl/README.POL
%{_texdir}/texmf-dist/doc/fonts/pl/plsample.tex

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/plb10.pfb
%{_fontdir}/plbsy10.pfb
%{_fontdir}/plbx10.pfb
%{_fontdir}/plbx12.pfb
%{_fontdir}/plbx5.pfb
%{_fontdir}/plbx6.pfb
%{_fontdir}/plbx7.pfb
%{_fontdir}/plbx8.pfb
%{_fontdir}/plbx9.pfb
%{_fontdir}/plbxsl10.pfb
%{_fontdir}/plbxti10.pfb
%{_fontdir}/plcsc10.pfb
%{_fontdir}/pldunh10.pfb
%{_fontdir}/plex10.pfb
%{_fontdir}/plex9.pfb
%{_fontdir}/plff10.pfb
%{_fontdir}/plfi10.pfb
%{_fontdir}/plfib8.pfb
%{_fontdir}/plinch.pfb
%{_fontdir}/plitt10.pfb
%{_fontdir}/plmi10.pfb
%{_fontdir}/plmi12.pfb
%{_fontdir}/plmi5.pfb
%{_fontdir}/plmi6.pfb
%{_fontdir}/plmi7.pfb
%{_fontdir}/plmi8.pfb
%{_fontdir}/plmi9.pfb
%{_fontdir}/plmib10.pfb
%{_fontdir}/plr10.pfb
%{_fontdir}/plr12.pfb
%{_fontdir}/plr17.pfb
%{_fontdir}/plr5.pfb
%{_fontdir}/plr6.pfb
%{_fontdir}/plr7.pfb
%{_fontdir}/plr8.pfb
%{_fontdir}/plr9.pfb
%{_fontdir}/plsl10.pfb
%{_fontdir}/plsl12.pfb
%{_fontdir}/plsl8.pfb
%{_fontdir}/plsl9.pfb
%{_fontdir}/plsltt10.pfb
%{_fontdir}/plss10.pfb
%{_fontdir}/plss12.pfb
%{_fontdir}/plss17.pfb
%{_fontdir}/plss8.pfb
%{_fontdir}/plss9.pfb
%{_fontdir}/plssbi10.pfb
%{_fontdir}/plssbx10.pfb
%{_fontdir}/plssdc10.pfb
%{_fontdir}/plssi10.pfb
%{_fontdir}/plssi12.pfb
%{_fontdir}/plssi17.pfb
%{_fontdir}/plssi8.pfb
%{_fontdir}/plssi9.pfb
%{_fontdir}/plssq8.pfb
%{_fontdir}/plssqi8.pfb
%{_fontdir}/plsy10.pfb
%{_fontdir}/plsy5.pfb
%{_fontdir}/plsy6.pfb
%{_fontdir}/plsy7.pfb
%{_fontdir}/plsy8.pfb
%{_fontdir}/plsy9.pfb
%{_fontdir}/pltcsc10.pfb
%{_fontdir}/pltex10.pfb
%{_fontdir}/pltex8.pfb
%{_fontdir}/pltex9.pfb
%{_fontdir}/plti10.pfb
%{_fontdir}/plti12.pfb
%{_fontdir}/plti7.pfb
%{_fontdir}/plti8.pfb
%{_fontdir}/plti9.pfb
%{_fontdir}/pltt10.pfb
%{_fontdir}/pltt12.pfb
%{_fontdir}/pltt8.pfb
%{_fontdir}/pltt9.pfb
%{_fontdir}/plu10.pfb
%{_fontdir}/plvtt10.pfb

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
