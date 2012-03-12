%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cm-super.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cm-super.doc.tar.xz

Name: texlive-cm-super
License: GPL+
Summary: CM-Super family of fonts
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(type1ec.sty)
Requires: texlive-cm-super-fedora-fonts = %{tl_version}

%description
CM-Super family of fonts are Adobe Type 1 fonts that replace
the T1/TS1-encoded Computer Modern (EC/TC), T1/TS1-encoded
Concrete, T1/TS1-encoded CM bright and LH fonts (thus
supporting all European languages except Greek, and all
Cyrillic-based languages), and bringing many ameliorations in
typesetting quality. The fonts exhibit the same metrics as the
MetaFont-encoded originals.

date: 2008-01-16 21:31:11 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "MixedMap cm-super-t1.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "MixedMap cm-super-t2a.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "MixedMap cm-super-t2b.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "MixedMap cm-super-t2c.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "MixedMap cm-super-ts1.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "MixedMap cm-super-x2.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^MixedMap cm-super-t1.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^MixedMap cm-super-t2a.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^MixedMap cm-super-t2b.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^MixedMap cm-super-t2c.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^MixedMap cm-super-ts1.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^MixedMap cm-super-x2.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for cm-super
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for cm-super

%package fedora-fonts
Summary: Fonts for cm-super
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-cm-super = %{tl_version}
BuildArch: noarch

%description fedora-fonts
CM-Super family of fonts are Adobe Type 1 fonts that replace
the T1/TS1-encoded Computer Modern (EC/TC), T1/TS1-encoded
Concrete, T1/TS1-encoded CM bright and LH fonts (thus
supporting all European languages except Greek, and all
Cyrillic-based languages), and bringing many ameliorations in
typesetting quality. The fonts exhibit the same metrics as the
MetaFont-encoded originals.

date: 2008-01-16 21:31:11 +0100


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/isflb8.pfb .
ln -s %{_fontdir}/isflb8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/isflb8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/isfli8.pfb .
ln -s %{_fontdir}/isfli8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/isfli8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/isflo8.pfb .
ln -s %{_fontdir}/isflo8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/isflo8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/isflq8.pfb .
ln -s %{_fontdir}/isflq8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/isflq8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/isfltt8.pfb .
ln -s %{_fontdir}/isfltt8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/isfltt8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbbx10.pfb .
ln -s %{_fontdir}/sfbbx10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbbx10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi0500.pfb .
ln -s %{_fontdir}/sfbi0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi0600.pfb .
ln -s %{_fontdir}/sfbi0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi0700.pfb .
ln -s %{_fontdir}/sfbi0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi0800.pfb .
ln -s %{_fontdir}/sfbi0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi0900.pfb .
ln -s %{_fontdir}/sfbi0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi1000.pfb .
ln -s %{_fontdir}/sfbi1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi1095.pfb .
ln -s %{_fontdir}/sfbi1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi1200.pfb .
ln -s %{_fontdir}/sfbi1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi1440.pfb .
ln -s %{_fontdir}/sfbi1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi1728.pfb .
ln -s %{_fontdir}/sfbi1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi2074.pfb .
ln -s %{_fontdir}/sfbi2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi2488.pfb .
ln -s %{_fontdir}/sfbi2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi2986.pfb .
ln -s %{_fontdir}/sfbi2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi3583.pfb .
ln -s %{_fontdir}/sfbi3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl0500.pfb .
ln -s %{_fontdir}/sfbl0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl0600.pfb .
ln -s %{_fontdir}/sfbl0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl0700.pfb .
ln -s %{_fontdir}/sfbl0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl0800.pfb .
ln -s %{_fontdir}/sfbl0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl0900.pfb .
ln -s %{_fontdir}/sfbl0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl1000.pfb .
ln -s %{_fontdir}/sfbl1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl1095.pfb .
ln -s %{_fontdir}/sfbl1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl1200.pfb .
ln -s %{_fontdir}/sfbl1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl1440.pfb .
ln -s %{_fontdir}/sfbl1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl1728.pfb .
ln -s %{_fontdir}/sfbl1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl2074.pfb .
ln -s %{_fontdir}/sfbl2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl2488.pfb .
ln -s %{_fontdir}/sfbl2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl2986.pfb .
ln -s %{_fontdir}/sfbl2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl3583.pfb .
ln -s %{_fontdir}/sfbl3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm0500.pfb .
ln -s %{_fontdir}/sfbm0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm0700.pfb .
ln -s %{_fontdir}/sfbm0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm0900.pfb .
ln -s %{_fontdir}/sfbm0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm1000.pfb .
ln -s %{_fontdir}/sfbm1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm1095.pfb .
ln -s %{_fontdir}/sfbm1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm1200.pfb .
ln -s %{_fontdir}/sfbm1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm1440.pfb .
ln -s %{_fontdir}/sfbm1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm1728.pfb .
ln -s %{_fontdir}/sfbm1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm2074.pfb .
ln -s %{_fontdir}/sfbm2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm2488.pfb .
ln -s %{_fontdir}/sfbm2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm2986.pfb .
ln -s %{_fontdir}/sfbm2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm3583.pfb .
ln -s %{_fontdir}/sfbm3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbmo10.pfb .
ln -s %{_fontdir}/sfbmo10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbmo10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbmo17.pfb .
ln -s %{_fontdir}/sfbmo17.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbmo17.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbmo8.pfb .
ln -s %{_fontdir}/sfbmo8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbmo8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbmo9.pfb .
ln -s %{_fontdir}/sfbmo9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbmo9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbmr10.pfb .
ln -s %{_fontdir}/sfbmr10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbmr10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbmr17.pfb .
ln -s %{_fontdir}/sfbmr17.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbmr17.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbmr8.pfb .
ln -s %{_fontdir}/sfbmr8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbmr8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbmr9.pfb .
ln -s %{_fontdir}/sfbmr9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbmr9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbso10.pfb .
ln -s %{_fontdir}/sfbso10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbso10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbso17.pfb .
ln -s %{_fontdir}/sfbso17.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbso17.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbso8.pfb .
ln -s %{_fontdir}/sfbso8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbso8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbso9.pfb .
ln -s %{_fontdir}/sfbso9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbso9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbsr10.pfb .
ln -s %{_fontdir}/sfbsr10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbsr10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbsr17.pfb .
ln -s %{_fontdir}/sfbsr17.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbsr17.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbsr8.pfb .
ln -s %{_fontdir}/sfbsr8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbsr8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbsr9.pfb .
ln -s %{_fontdir}/sfbsr9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbsr9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbtl10.pfb .
ln -s %{_fontdir}/sfbtl10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbtl10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbto10.pfb .
ln -s %{_fontdir}/sfbto10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbto10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx0500.pfb .
ln -s %{_fontdir}/sfbx0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx0600.pfb .
ln -s %{_fontdir}/sfbx0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx0700.pfb .
ln -s %{_fontdir}/sfbx0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx0800.pfb .
ln -s %{_fontdir}/sfbx0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx0900.pfb .
ln -s %{_fontdir}/sfbx0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx1000.pfb .
ln -s %{_fontdir}/sfbx1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx1095.pfb .
ln -s %{_fontdir}/sfbx1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx1200.pfb .
ln -s %{_fontdir}/sfbx1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx1440.pfb .
ln -s %{_fontdir}/sfbx1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx1728.pfb .
ln -s %{_fontdir}/sfbx1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx2074.pfb .
ln -s %{_fontdir}/sfbx2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx2488.pfb .
ln -s %{_fontdir}/sfbx2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx2986.pfb .
ln -s %{_fontdir}/sfbx2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx3583.pfb .
ln -s %{_fontdir}/sfbx3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc0500.pfb .
ln -s %{_fontdir}/sfcc0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc0600.pfb .
ln -s %{_fontdir}/sfcc0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc0700.pfb .
ln -s %{_fontdir}/sfcc0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc0800.pfb .
ln -s %{_fontdir}/sfcc0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc0900.pfb .
ln -s %{_fontdir}/sfcc0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc1000.pfb .
ln -s %{_fontdir}/sfcc1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc1095.pfb .
ln -s %{_fontdir}/sfcc1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc1200.pfb .
ln -s %{_fontdir}/sfcc1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc1440.pfb .
ln -s %{_fontdir}/sfcc1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc1728.pfb .
ln -s %{_fontdir}/sfcc1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc2074.pfb .
ln -s %{_fontdir}/sfcc2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc2488.pfb .
ln -s %{_fontdir}/sfcc2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc2986.pfb .
ln -s %{_fontdir}/sfcc2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc3583.pfb .
ln -s %{_fontdir}/sfcc3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci0500.pfb .
ln -s %{_fontdir}/sfci0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci0600.pfb .
ln -s %{_fontdir}/sfci0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci0700.pfb .
ln -s %{_fontdir}/sfci0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci0800.pfb .
ln -s %{_fontdir}/sfci0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci0900.pfb .
ln -s %{_fontdir}/sfci0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci1000.pfb .
ln -s %{_fontdir}/sfci1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci1095.pfb .
ln -s %{_fontdir}/sfci1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci1200.pfb .
ln -s %{_fontdir}/sfci1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci1440.pfb .
ln -s %{_fontdir}/sfci1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci1728.pfb .
ln -s %{_fontdir}/sfci1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci2074.pfb .
ln -s %{_fontdir}/sfci2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci2488.pfb .
ln -s %{_fontdir}/sfci2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci2986.pfb .
ln -s %{_fontdir}/sfci2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci3583.pfb .
ln -s %{_fontdir}/sfci3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh0500.pfb .
ln -s %{_fontdir}/sfdh0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh0600.pfb .
ln -s %{_fontdir}/sfdh0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh0700.pfb .
ln -s %{_fontdir}/sfdh0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh0800.pfb .
ln -s %{_fontdir}/sfdh0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh0900.pfb .
ln -s %{_fontdir}/sfdh0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh1000.pfb .
ln -s %{_fontdir}/sfdh1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh1095.pfb .
ln -s %{_fontdir}/sfdh1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh1200.pfb .
ln -s %{_fontdir}/sfdh1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh1440.pfb .
ln -s %{_fontdir}/sfdh1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh1728.pfb .
ln -s %{_fontdir}/sfdh1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh2074.pfb .
ln -s %{_fontdir}/sfdh2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh2488.pfb .
ln -s %{_fontdir}/sfdh2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh2986.pfb .
ln -s %{_fontdir}/sfdh2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh3583.pfb .
ln -s %{_fontdir}/sfdh3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb0500.pfb .
ln -s %{_fontdir}/sffb0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb0600.pfb .
ln -s %{_fontdir}/sffb0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb0700.pfb .
ln -s %{_fontdir}/sffb0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb0800.pfb .
ln -s %{_fontdir}/sffb0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb0900.pfb .
ln -s %{_fontdir}/sffb0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb1000.pfb .
ln -s %{_fontdir}/sffb1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb1095.pfb .
ln -s %{_fontdir}/sffb1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb1200.pfb .
ln -s %{_fontdir}/sffb1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb1440.pfb .
ln -s %{_fontdir}/sffb1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb1728.pfb .
ln -s %{_fontdir}/sffb1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb2074.pfb .
ln -s %{_fontdir}/sffb2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfff0900.pfb .
ln -s %{_fontdir}/sfff0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfff0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfff1000.pfb .
ln -s %{_fontdir}/sfff1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfff1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfff1095.pfb .
ln -s %{_fontdir}/sfff1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfff1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfff1200.pfb .
ln -s %{_fontdir}/sfff1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfff1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfff1440.pfb .
ln -s %{_fontdir}/sfff1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfff1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfff2488.pfb .
ln -s %{_fontdir}/sfff2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfff2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffi0900.pfb .
ln -s %{_fontdir}/sffi0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffi0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffi1000.pfb .
ln -s %{_fontdir}/sffi1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffi1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffi1095.pfb .
ln -s %{_fontdir}/sffi1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffi1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffi1200.pfb .
ln -s %{_fontdir}/sffi1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffi1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffi1440.pfb .
ln -s %{_fontdir}/sffi1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffi1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffi1728.pfb .
ln -s %{_fontdir}/sffi1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffi1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffi2074.pfb .
ln -s %{_fontdir}/sffi2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffi2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs0500.pfb .
ln -s %{_fontdir}/sffs0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs0600.pfb .
ln -s %{_fontdir}/sffs0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs0700.pfb .
ln -s %{_fontdir}/sffs0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs0800.pfb .
ln -s %{_fontdir}/sffs0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs0900.pfb .
ln -s %{_fontdir}/sffs0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs1000.pfb .
ln -s %{_fontdir}/sffs1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs1095.pfb .
ln -s %{_fontdir}/sffs1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs1200.pfb .
ln -s %{_fontdir}/sffs1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs1440.pfb .
ln -s %{_fontdir}/sffs1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs1728.pfb .
ln -s %{_fontdir}/sffs1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs2074.pfb .
ln -s %{_fontdir}/sffs2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit0800.pfb .
ln -s %{_fontdir}/sfit0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit0900.pfb .
ln -s %{_fontdir}/sfit0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit1000.pfb .
ln -s %{_fontdir}/sfit1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit1095.pfb .
ln -s %{_fontdir}/sfit1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit1200.pfb .
ln -s %{_fontdir}/sfit1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit1440.pfb .
ln -s %{_fontdir}/sfit1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit1728.pfb .
ln -s %{_fontdir}/sfit1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit2074.pfb .
ln -s %{_fontdir}/sfit2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit2488.pfb .
ln -s %{_fontdir}/sfit2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sflb8.pfb .
ln -s %{_fontdir}/sflb8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sflb8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfli8.pfb .
ln -s %{_fontdir}/sfli8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfli8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sflo8.pfb .
ln -s %{_fontdir}/sflo8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sflo8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sflq8.pfb .
ln -s %{_fontdir}/sflq8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sflq8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfltt8.pfb .
ln -s %{_fontdir}/sfltt8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfltt8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc0500.pfb .
ln -s %{_fontdir}/sfoc0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc0600.pfb .
ln -s %{_fontdir}/sfoc0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc0700.pfb .
ln -s %{_fontdir}/sfoc0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc0800.pfb .
ln -s %{_fontdir}/sfoc0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc0900.pfb .
ln -s %{_fontdir}/sfoc0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc1000.pfb .
ln -s %{_fontdir}/sfoc1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc1095.pfb .
ln -s %{_fontdir}/sfoc1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc1200.pfb .
ln -s %{_fontdir}/sfoc1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc1440.pfb .
ln -s %{_fontdir}/sfoc1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc1728.pfb .
ln -s %{_fontdir}/sfoc1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc2074.pfb .
ln -s %{_fontdir}/sfoc2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc2488.pfb .
ln -s %{_fontdir}/sfoc2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc2986.pfb .
ln -s %{_fontdir}/sfoc2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc3583.pfb .
ln -s %{_fontdir}/sfoc3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfocc10.pfb .
ln -s %{_fontdir}/sfocc10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfocc10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sform10.pfb .
ln -s %{_fontdir}/sform10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sform10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sform5.pfb .
ln -s %{_fontdir}/sform5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sform5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sform6.pfb .
ln -s %{_fontdir}/sform6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sform6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sform7.pfb .
ln -s %{_fontdir}/sform7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sform7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sform8.pfb .
ln -s %{_fontdir}/sform8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sform8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sform9.pfb .
ln -s %{_fontdir}/sform9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sform9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfosl10.pfb .
ln -s %{_fontdir}/sfosl10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfosl10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfosl5.pfb .
ln -s %{_fontdir}/sfosl5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfosl5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfosl6.pfb .
ln -s %{_fontdir}/sfosl6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfosl6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfosl7.pfb .
ln -s %{_fontdir}/sfosl7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfosl7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfosl8.pfb .
ln -s %{_fontdir}/sfosl8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfosl8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfosl9.pfb .
ln -s %{_fontdir}/sfosl9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfosl9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoti10.pfb .
ln -s %{_fontdir}/sfoti10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoti10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfqi8.pfb .
ln -s %{_fontdir}/sfqi8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfqi8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb0500.pfb .
ln -s %{_fontdir}/sfrb0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb0600.pfb .
ln -s %{_fontdir}/sfrb0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb0700.pfb .
ln -s %{_fontdir}/sfrb0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb0800.pfb .
ln -s %{_fontdir}/sfrb0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb0900.pfb .
ln -s %{_fontdir}/sfrb0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb1000.pfb .
ln -s %{_fontdir}/sfrb1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb1095.pfb .
ln -s %{_fontdir}/sfrb1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb1200.pfb .
ln -s %{_fontdir}/sfrb1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb1440.pfb .
ln -s %{_fontdir}/sfrb1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb1728.pfb .
ln -s %{_fontdir}/sfrb1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb2074.pfb .
ln -s %{_fontdir}/sfrb2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb2488.pfb .
ln -s %{_fontdir}/sfrb2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb2986.pfb .
ln -s %{_fontdir}/sfrb2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb3583.pfb .
ln -s %{_fontdir}/sfrb3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm0500.pfb .
ln -s %{_fontdir}/sfrm0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm0600.pfb .
ln -s %{_fontdir}/sfrm0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm0700.pfb .
ln -s %{_fontdir}/sfrm0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm0800.pfb .
ln -s %{_fontdir}/sfrm0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm0900.pfb .
ln -s %{_fontdir}/sfrm0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm1000.pfb .
ln -s %{_fontdir}/sfrm1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm1095.pfb .
ln -s %{_fontdir}/sfrm1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm1200.pfb .
ln -s %{_fontdir}/sfrm1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm1440.pfb .
ln -s %{_fontdir}/sfrm1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm1728.pfb .
ln -s %{_fontdir}/sfrm1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm2074.pfb .
ln -s %{_fontdir}/sfrm2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm2488.pfb .
ln -s %{_fontdir}/sfrm2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm2986.pfb .
ln -s %{_fontdir}/sfrm2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm3583.pfb .
ln -s %{_fontdir}/sfrm3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc0500.pfb .
ln -s %{_fontdir}/sfsc0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc0600.pfb .
ln -s %{_fontdir}/sfsc0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc0700.pfb .
ln -s %{_fontdir}/sfsc0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc0800.pfb .
ln -s %{_fontdir}/sfsc0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc0900.pfb .
ln -s %{_fontdir}/sfsc0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc1000.pfb .
ln -s %{_fontdir}/sfsc1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc1095.pfb .
ln -s %{_fontdir}/sfsc1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc1200.pfb .
ln -s %{_fontdir}/sfsc1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc1440.pfb .
ln -s %{_fontdir}/sfsc1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc1728.pfb .
ln -s %{_fontdir}/sfsc1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc2074.pfb .
ln -s %{_fontdir}/sfsc2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc2488.pfb .
ln -s %{_fontdir}/sfsc2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc2986.pfb .
ln -s %{_fontdir}/sfsc2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc3583.pfb .
ln -s %{_fontdir}/sfsc3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi0500.pfb .
ln -s %{_fontdir}/sfsi0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi0600.pfb .
ln -s %{_fontdir}/sfsi0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi0700.pfb .
ln -s %{_fontdir}/sfsi0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi0800.pfb .
ln -s %{_fontdir}/sfsi0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi0900.pfb .
ln -s %{_fontdir}/sfsi0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi1000.pfb .
ln -s %{_fontdir}/sfsi1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi1095.pfb .
ln -s %{_fontdir}/sfsi1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi1200.pfb .
ln -s %{_fontdir}/sfsi1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi1440.pfb .
ln -s %{_fontdir}/sfsi1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi1728.pfb .
ln -s %{_fontdir}/sfsi1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi2074.pfb .
ln -s %{_fontdir}/sfsi2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi2488.pfb .
ln -s %{_fontdir}/sfsi2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi2986.pfb .
ln -s %{_fontdir}/sfsi2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi3583.pfb .
ln -s %{_fontdir}/sfsi3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl0500.pfb .
ln -s %{_fontdir}/sfsl0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl0600.pfb .
ln -s %{_fontdir}/sfsl0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl0700.pfb .
ln -s %{_fontdir}/sfsl0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl0800.pfb .
ln -s %{_fontdir}/sfsl0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl0900.pfb .
ln -s %{_fontdir}/sfsl0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl1000.pfb .
ln -s %{_fontdir}/sfsl1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl1095.pfb .
ln -s %{_fontdir}/sfsl1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl1200.pfb .
ln -s %{_fontdir}/sfsl1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl1440.pfb .
ln -s %{_fontdir}/sfsl1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl1728.pfb .
ln -s %{_fontdir}/sfsl1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl2074.pfb .
ln -s %{_fontdir}/sfsl2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl2488.pfb .
ln -s %{_fontdir}/sfsl2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl2986.pfb .
ln -s %{_fontdir}/sfsl2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl3583.pfb .
ln -s %{_fontdir}/sfsl3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso0500.pfb .
ln -s %{_fontdir}/sfso0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso0600.pfb .
ln -s %{_fontdir}/sfso0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso0700.pfb .
ln -s %{_fontdir}/sfso0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso0800.pfb .
ln -s %{_fontdir}/sfso0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso0900.pfb .
ln -s %{_fontdir}/sfso0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso1000.pfb .
ln -s %{_fontdir}/sfso1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso1095.pfb .
ln -s %{_fontdir}/sfso1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso1200.pfb .
ln -s %{_fontdir}/sfso1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso1440.pfb .
ln -s %{_fontdir}/sfso1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso1728.pfb .
ln -s %{_fontdir}/sfso1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso2074.pfb .
ln -s %{_fontdir}/sfso2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso2488.pfb .
ln -s %{_fontdir}/sfso2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso2986.pfb .
ln -s %{_fontdir}/sfso2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso3583.pfb .
ln -s %{_fontdir}/sfso3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsq8.pfb .
ln -s %{_fontdir}/sfsq8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsq8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss0500.pfb .
ln -s %{_fontdir}/sfss0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss0600.pfb .
ln -s %{_fontdir}/sfss0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss0700.pfb .
ln -s %{_fontdir}/sfss0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss0800.pfb .
ln -s %{_fontdir}/sfss0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss0900.pfb .
ln -s %{_fontdir}/sfss0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss1000.pfb .
ln -s %{_fontdir}/sfss1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss1095.pfb .
ln -s %{_fontdir}/sfss1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss1200.pfb .
ln -s %{_fontdir}/sfss1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss1440.pfb .
ln -s %{_fontdir}/sfss1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss1728.pfb .
ln -s %{_fontdir}/sfss1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss2074.pfb .
ln -s %{_fontdir}/sfss2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss2488.pfb .
ln -s %{_fontdir}/sfss2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss2986.pfb .
ln -s %{_fontdir}/sfss2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss3583.pfb .
ln -s %{_fontdir}/sfss3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfssdc10.pfb .
ln -s %{_fontdir}/sfssdc10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfssdc10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst0800.pfb .
ln -s %{_fontdir}/sfst0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst0900.pfb .
ln -s %{_fontdir}/sfst0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst1000.pfb .
ln -s %{_fontdir}/sfst1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst1095.pfb .
ln -s %{_fontdir}/sfst1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst1200.pfb .
ln -s %{_fontdir}/sfst1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst1440.pfb .
ln -s %{_fontdir}/sfst1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst1728.pfb .
ln -s %{_fontdir}/sfst1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst2074.pfb .
ln -s %{_fontdir}/sfst2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst2488.pfb .
ln -s %{_fontdir}/sfst2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst2986.pfb .
ln -s %{_fontdir}/sfst2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst3583.pfb .
ln -s %{_fontdir}/sfst3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx0500.pfb .
ln -s %{_fontdir}/sfsx0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx0600.pfb .
ln -s %{_fontdir}/sfsx0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx0700.pfb .
ln -s %{_fontdir}/sfsx0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx0800.pfb .
ln -s %{_fontdir}/sfsx0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx0900.pfb .
ln -s %{_fontdir}/sfsx0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx1000.pfb .
ln -s %{_fontdir}/sfsx1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx1095.pfb .
ln -s %{_fontdir}/sfsx1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx1200.pfb .
ln -s %{_fontdir}/sfsx1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx1440.pfb .
ln -s %{_fontdir}/sfsx1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx1728.pfb .
ln -s %{_fontdir}/sfsx1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx2074.pfb .
ln -s %{_fontdir}/sfsx2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx2488.pfb .
ln -s %{_fontdir}/sfsx2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx2986.pfb .
ln -s %{_fontdir}/sfsx2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx3583.pfb .
ln -s %{_fontdir}/sfsx3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc0800.pfb .
ln -s %{_fontdir}/sftc0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc0900.pfb .
ln -s %{_fontdir}/sftc0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc1000.pfb .
ln -s %{_fontdir}/sftc1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc1095.pfb .
ln -s %{_fontdir}/sftc1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc1200.pfb .
ln -s %{_fontdir}/sftc1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc1440.pfb .
ln -s %{_fontdir}/sftc1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc1728.pfb .
ln -s %{_fontdir}/sftc1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc2074.pfb .
ln -s %{_fontdir}/sftc2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc2488.pfb .
ln -s %{_fontdir}/sftc2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc2986.pfb .
ln -s %{_fontdir}/sftc2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc3583.pfb .
ln -s %{_fontdir}/sftc3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti0500.pfb .
ln -s %{_fontdir}/sfti0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti0600.pfb .
ln -s %{_fontdir}/sfti0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti0700.pfb .
ln -s %{_fontdir}/sfti0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti0800.pfb .
ln -s %{_fontdir}/sfti0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti0900.pfb .
ln -s %{_fontdir}/sfti0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti1000.pfb .
ln -s %{_fontdir}/sfti1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti1095.pfb .
ln -s %{_fontdir}/sfti1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti1200.pfb .
ln -s %{_fontdir}/sfti1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti1440.pfb .
ln -s %{_fontdir}/sfti1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti1728.pfb .
ln -s %{_fontdir}/sfti1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti2074.pfb .
ln -s %{_fontdir}/sfti2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti2488.pfb .
ln -s %{_fontdir}/sfti2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti2986.pfb .
ln -s %{_fontdir}/sfti2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti3583.pfb .
ln -s %{_fontdir}/sfti3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt0800.pfb .
ln -s %{_fontdir}/sftt0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt0900.pfb .
ln -s %{_fontdir}/sftt0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt1000.pfb .
ln -s %{_fontdir}/sftt1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt1095.pfb .
ln -s %{_fontdir}/sftt1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt1200.pfb .
ln -s %{_fontdir}/sftt1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt1440.pfb .
ln -s %{_fontdir}/sftt1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt1728.pfb .
ln -s %{_fontdir}/sftt1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt2074.pfb .
ln -s %{_fontdir}/sftt2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt2488.pfb .
ln -s %{_fontdir}/sftt2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt2986.pfb .
ln -s %{_fontdir}/sftt2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt3583.pfb .
ln -s %{_fontdir}/sftt3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui0500.pfb .
ln -s %{_fontdir}/sfui0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui0600.pfb .
ln -s %{_fontdir}/sfui0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui0700.pfb .
ln -s %{_fontdir}/sfui0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui0800.pfb .
ln -s %{_fontdir}/sfui0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui0900.pfb .
ln -s %{_fontdir}/sfui0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui1000.pfb .
ln -s %{_fontdir}/sfui1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui1095.pfb .
ln -s %{_fontdir}/sfui1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui1200.pfb .
ln -s %{_fontdir}/sfui1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui1440.pfb .
ln -s %{_fontdir}/sfui1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui1728.pfb .
ln -s %{_fontdir}/sfui1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui2074.pfb .
ln -s %{_fontdir}/sfui2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui2488.pfb .
ln -s %{_fontdir}/sfui2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui2986.pfb .
ln -s %{_fontdir}/sfui2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui3583.pfb .
ln -s %{_fontdir}/sfui3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi0800.pfb .
ln -s %{_fontdir}/sfvi0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi0900.pfb .
ln -s %{_fontdir}/sfvi0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi1000.pfb .
ln -s %{_fontdir}/sfvi1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi1095.pfb .
ln -s %{_fontdir}/sfvi1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi1200.pfb .
ln -s %{_fontdir}/sfvi1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi1440.pfb .
ln -s %{_fontdir}/sfvi1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi1728.pfb .
ln -s %{_fontdir}/sfvi1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi2074.pfb .
ln -s %{_fontdir}/sfvi2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi2488.pfb .
ln -s %{_fontdir}/sfvi2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi2986.pfb .
ln -s %{_fontdir}/sfvi2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi3583.pfb .
ln -s %{_fontdir}/sfvi3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt0800.pfb .
ln -s %{_fontdir}/sfvt0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt0900.pfb .
ln -s %{_fontdir}/sfvt0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt1000.pfb .
ln -s %{_fontdir}/sfvt1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt1095.pfb .
ln -s %{_fontdir}/sfvt1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt1200.pfb .
ln -s %{_fontdir}/sfvt1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt1440.pfb .
ln -s %{_fontdir}/sfvt1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt1728.pfb .
ln -s %{_fontdir}/sfvt1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt2074.pfb .
ln -s %{_fontdir}/sfvt2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt2488.pfb .
ln -s %{_fontdir}/sfvt2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt2986.pfb .
ln -s %{_fontdir}/sfvt2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt3583.pfb .
ln -s %{_fontdir}/sfvt3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc0500.pfb .
ln -s %{_fontdir}/sfxc0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc0600.pfb .
ln -s %{_fontdir}/sfxc0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc0700.pfb .
ln -s %{_fontdir}/sfxc0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc0800.pfb .
ln -s %{_fontdir}/sfxc0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc0900.pfb .
ln -s %{_fontdir}/sfxc0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc1000.pfb .
ln -s %{_fontdir}/sfxc1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc1095.pfb .
ln -s %{_fontdir}/sfxc1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc1200.pfb .
ln -s %{_fontdir}/sfxc1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc1440.pfb .
ln -s %{_fontdir}/sfxc1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc1728.pfb .
ln -s %{_fontdir}/sfxc1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc2074.pfb .
ln -s %{_fontdir}/sfxc2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc2488.pfb .
ln -s %{_fontdir}/sfxc2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc2986.pfb .
ln -s %{_fontdir}/sfxc2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc3583.pfb .
ln -s %{_fontdir}/sfxc3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc3583.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/dvips/cm-super/cm-super.GS
%{_texdir}/texmf-dist/dvips/cm-super/config.cm-super
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/isflb8.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/isfli8.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/isflo8.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/isflq8.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/isfltt8.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbbx10.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbi0500.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbi0600.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbi0700.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbi0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbi0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbi1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbi1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbi1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbi1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbi1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbi2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbi2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbi2986.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbi3583.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbl0500.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbl0600.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbl0700.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbl0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbl0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbl1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbl1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbl1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbl1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbl1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbl2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbl2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbl2986.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbl3583.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbm0500.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbm0700.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbm0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbm1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbm1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbm1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbm1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbm1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbm2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbm2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbm2986.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbm3583.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbmo10.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbmo17.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbmo8.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbmo9.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbmr10.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbmr17.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbmr8.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbmr9.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbso10.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbso17.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbso8.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbso9.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbsr10.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbsr17.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbsr8.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbsr9.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbtl10.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbto10.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbx0500.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbx0600.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbx0700.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbx0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbx0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbx1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbx1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbx1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbx1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbx1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbx2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbx2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbx2986.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfbx3583.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfcc0500.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfcc0600.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfcc0700.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfcc0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfcc0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfcc1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfcc1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfcc1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfcc1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfcc1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfcc2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfcc2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfcc2986.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfcc3583.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfci0500.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfci0600.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfci0700.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfci0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfci0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfci1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfci1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfci1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfci1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfci1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfci2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfci2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfci2986.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfci3583.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfdh0500.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfdh0600.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfdh0700.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfdh0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfdh0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfdh1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfdh1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfdh1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfdh1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfdh1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfdh2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfdh2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfdh2986.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfdh3583.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffb0500.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffb0600.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffb0700.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffb0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffb0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffb1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffb1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffb1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffb1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffb1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffb2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfff0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfff1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfff1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfff1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfff1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfff2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffi0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffi1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffi1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffi1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffi1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffi1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffi2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffs0500.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffs0600.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffs0700.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffs0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffs0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffs1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffs1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffs1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffs1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffs1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sffs2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfit0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfit0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfit1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfit1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfit1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfit1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfit1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfit2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfit2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sflb8.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfli8.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sflo8.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sflq8.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfltt8.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfoc0500.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfoc0600.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfoc0700.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfoc0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfoc0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfoc1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfoc1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfoc1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfoc1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfoc1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfoc2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfoc2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfoc2986.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfoc3583.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfocc10.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sform10.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sform5.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sform6.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sform7.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sform8.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sform9.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfosl10.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfosl5.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfosl6.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfosl7.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfosl8.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfosl9.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfoti10.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfqi8.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrb0500.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrb0600.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrb0700.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrb0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrb0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrb1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrb1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrb1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrb1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrb1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrb2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrb2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrb2986.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrb3583.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrm0500.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrm0600.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrm0700.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrm0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrm0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrm1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrm1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrm1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrm1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrm1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrm2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrm2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrm2986.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfrm3583.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsc0500.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsc0600.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsc0700.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsc0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsc0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsc1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsc1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsc1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsc1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsc1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsc2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsc2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsc2986.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsc3583.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsi0500.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsi0600.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsi0700.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsi0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsi0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsi1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsi1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsi1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsi1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsi1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsi2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsi2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsi2986.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsi3583.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsl0500.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsl0600.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsl0700.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsl0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsl0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsl1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsl1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsl1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsl1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsl1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsl2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsl2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsl2986.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsl3583.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfso0500.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfso0600.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfso0700.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfso0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfso0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfso1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfso1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfso1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfso1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfso1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfso2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfso2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfso2986.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfso3583.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsq8.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfss0500.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfss0600.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfss0700.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfss0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfss0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfss1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfss1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfss1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfss1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfss1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfss2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfss2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfss2986.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfss3583.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfssdc10.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfst0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfst0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfst1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfst1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfst1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfst1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfst1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfst2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfst2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfst2986.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfst3583.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsx0500.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsx0600.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsx0700.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsx0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsx0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsx1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsx1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsx1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsx1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsx1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsx2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsx2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsx2986.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfsx3583.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sftc0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sftc0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sftc1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sftc1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sftc1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sftc1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sftc1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sftc2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sftc2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sftc2986.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sftc3583.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfti0500.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfti0600.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfti0700.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfti0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfti0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfti1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfti1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfti1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfti1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfti1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfti2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfti2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfti2986.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfti3583.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sftt0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sftt0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sftt1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sftt1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sftt1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sftt1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sftt1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sftt2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sftt2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sftt2986.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sftt3583.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfui0500.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfui0600.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfui0700.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfui0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfui0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfui1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfui1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfui1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfui1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfui1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfui2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfui2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfui2986.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfui3583.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfvi0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfvi0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfvi1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfvi1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfvi1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfvi1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfvi1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfvi2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfvi2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfvi2986.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfvi3583.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfvt0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfvt0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfvt1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfvt1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfvt1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfvt1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfvt1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfvt2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfvt2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfvt2986.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfvt3583.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfxc0500.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfxc0600.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfxc0700.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfxc0800.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfxc0900.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfxc1000.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfxc1095.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfxc1200.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfxc1440.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfxc1728.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfxc2074.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfxc2488.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfxc2986.afm.gz
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/sfxc3583.afm.gz
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-super/cm-super-t1.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-super/cm-super-t2a.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-super/cm-super-t2b.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-super/cm-super-t2c.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-super/cm-super-ts1.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-super/cm-super-x2.enc
%{_texdir}/texmf-dist/fonts/map/dvips/cm-super/cm-super-t1.map
%{_texdir}/texmf-dist/fonts/map/dvips/cm-super/cm-super-t2a.map
%{_texdir}/texmf-dist/fonts/map/dvips/cm-super/cm-super-t2b.map
%{_texdir}/texmf-dist/fonts/map/dvips/cm-super/cm-super-t2c.map
%{_texdir}/texmf-dist/fonts/map/dvips/cm-super/cm-super-ts1.map
%{_texdir}/texmf-dist/fonts/map/dvips/cm-super/cm-super-x2.map
%{_texdir}/texmf-dist/fonts/map/vtex/cm-super/cm-super-t1.ali
%{_texdir}/texmf-dist/fonts/map/vtex/cm-super/cm-super-t2a.ali
%{_texdir}/texmf-dist/fonts/map/vtex/cm-super/cm-super-t2b.ali
%{_texdir}/texmf-dist/fonts/map/vtex/cm-super/cm-super-t2c.ali
%{_texdir}/texmf-dist/fonts/map/vtex/cm-super/cm-super-ts1.ali
%{_texdir}/texmf-dist/fonts/map/vtex/cm-super/cm-super-x2.ali
%{_texdir}/texmf-dist/fonts/map/vtex/cm-super/cm-super.ali
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/isflb8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/isfli8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/isflo8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/isflq8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/isfltt8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbbx10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbi3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbl3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbm3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbmo10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbmo17.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbmo8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbmo9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbmr10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbmr17.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbmr8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbmr9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbso10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbso17.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbso8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbso9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbsr10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbsr17.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbsr8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbsr9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbtl10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbto10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfbx3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfcc3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfci3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfdh3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffb2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfff0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfff1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfff1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfff1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfff1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfff2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffi0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffi1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffi1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffi1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffi1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffi1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffi2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sffs2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfit2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sflb8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfli8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sflo8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sflq8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfltt8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoc3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfocc10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sform10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sform5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sform6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sform7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sform8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sform9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfosl10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfosl5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfosl6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfosl7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfosl8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfosl9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfoti10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfqi8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrb3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfrm3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsc3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsi3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsl3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfso3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsq8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfss3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfssdc10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfst3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfsx3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftc3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfti3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sftt3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfui3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvi3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfvt3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/sfxc3583.pfb
%{_texdir}/texmf-dist/tex/latex/cm-super/type1ec.sty

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/fonts/cm-super/COPYING
%{_texdir}/texmf-dist/doc/fonts/cm-super/ChangeLog
%{_texdir}/texmf-dist/doc/fonts/cm-super/FAQ
%{_texdir}/texmf-dist/doc/fonts/cm-super/INSTALL
%{_texdir}/texmf-dist/doc/fonts/cm-super/README
%{_texdir}/texmf-dist/doc/fonts/cm-super/TODO
%{_texdir}/texmf-dist/doc/fonts/cm-super/cm-super-inf.tar.bz2

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/isflb8.pfb
%{_fontdir}/isfli8.pfb
%{_fontdir}/isflo8.pfb
%{_fontdir}/isflq8.pfb
%{_fontdir}/isfltt8.pfb
%{_fontdir}/sfbbx10.pfb
%{_fontdir}/sfbi0500.pfb
%{_fontdir}/sfbi0600.pfb
%{_fontdir}/sfbi0700.pfb
%{_fontdir}/sfbi0800.pfb
%{_fontdir}/sfbi0900.pfb
%{_fontdir}/sfbi1000.pfb
%{_fontdir}/sfbi1095.pfb
%{_fontdir}/sfbi1200.pfb
%{_fontdir}/sfbi1440.pfb
%{_fontdir}/sfbi1728.pfb
%{_fontdir}/sfbi2074.pfb
%{_fontdir}/sfbi2488.pfb
%{_fontdir}/sfbi2986.pfb
%{_fontdir}/sfbi3583.pfb
%{_fontdir}/sfbl0500.pfb
%{_fontdir}/sfbl0600.pfb
%{_fontdir}/sfbl0700.pfb
%{_fontdir}/sfbl0800.pfb
%{_fontdir}/sfbl0900.pfb
%{_fontdir}/sfbl1000.pfb
%{_fontdir}/sfbl1095.pfb
%{_fontdir}/sfbl1200.pfb
%{_fontdir}/sfbl1440.pfb
%{_fontdir}/sfbl1728.pfb
%{_fontdir}/sfbl2074.pfb
%{_fontdir}/sfbl2488.pfb
%{_fontdir}/sfbl2986.pfb
%{_fontdir}/sfbl3583.pfb
%{_fontdir}/sfbm0500.pfb
%{_fontdir}/sfbm0700.pfb
%{_fontdir}/sfbm0900.pfb
%{_fontdir}/sfbm1000.pfb
%{_fontdir}/sfbm1095.pfb
%{_fontdir}/sfbm1200.pfb
%{_fontdir}/sfbm1440.pfb
%{_fontdir}/sfbm1728.pfb
%{_fontdir}/sfbm2074.pfb
%{_fontdir}/sfbm2488.pfb
%{_fontdir}/sfbm2986.pfb
%{_fontdir}/sfbm3583.pfb
%{_fontdir}/sfbmo10.pfb
%{_fontdir}/sfbmo17.pfb
%{_fontdir}/sfbmo8.pfb
%{_fontdir}/sfbmo9.pfb
%{_fontdir}/sfbmr10.pfb
%{_fontdir}/sfbmr17.pfb
%{_fontdir}/sfbmr8.pfb
%{_fontdir}/sfbmr9.pfb
%{_fontdir}/sfbso10.pfb
%{_fontdir}/sfbso17.pfb
%{_fontdir}/sfbso8.pfb
%{_fontdir}/sfbso9.pfb
%{_fontdir}/sfbsr10.pfb
%{_fontdir}/sfbsr17.pfb
%{_fontdir}/sfbsr8.pfb
%{_fontdir}/sfbsr9.pfb
%{_fontdir}/sfbtl10.pfb
%{_fontdir}/sfbto10.pfb
%{_fontdir}/sfbx0500.pfb
%{_fontdir}/sfbx0600.pfb
%{_fontdir}/sfbx0700.pfb
%{_fontdir}/sfbx0800.pfb
%{_fontdir}/sfbx0900.pfb
%{_fontdir}/sfbx1000.pfb
%{_fontdir}/sfbx1095.pfb
%{_fontdir}/sfbx1200.pfb
%{_fontdir}/sfbx1440.pfb
%{_fontdir}/sfbx1728.pfb
%{_fontdir}/sfbx2074.pfb
%{_fontdir}/sfbx2488.pfb
%{_fontdir}/sfbx2986.pfb
%{_fontdir}/sfbx3583.pfb
%{_fontdir}/sfcc0500.pfb
%{_fontdir}/sfcc0600.pfb
%{_fontdir}/sfcc0700.pfb
%{_fontdir}/sfcc0800.pfb
%{_fontdir}/sfcc0900.pfb
%{_fontdir}/sfcc1000.pfb
%{_fontdir}/sfcc1095.pfb
%{_fontdir}/sfcc1200.pfb
%{_fontdir}/sfcc1440.pfb
%{_fontdir}/sfcc1728.pfb
%{_fontdir}/sfcc2074.pfb
%{_fontdir}/sfcc2488.pfb
%{_fontdir}/sfcc2986.pfb
%{_fontdir}/sfcc3583.pfb
%{_fontdir}/sfci0500.pfb
%{_fontdir}/sfci0600.pfb
%{_fontdir}/sfci0700.pfb
%{_fontdir}/sfci0800.pfb
%{_fontdir}/sfci0900.pfb
%{_fontdir}/sfci1000.pfb
%{_fontdir}/sfci1095.pfb
%{_fontdir}/sfci1200.pfb
%{_fontdir}/sfci1440.pfb
%{_fontdir}/sfci1728.pfb
%{_fontdir}/sfci2074.pfb
%{_fontdir}/sfci2488.pfb
%{_fontdir}/sfci2986.pfb
%{_fontdir}/sfci3583.pfb
%{_fontdir}/sfdh0500.pfb
%{_fontdir}/sfdh0600.pfb
%{_fontdir}/sfdh0700.pfb
%{_fontdir}/sfdh0800.pfb
%{_fontdir}/sfdh0900.pfb
%{_fontdir}/sfdh1000.pfb
%{_fontdir}/sfdh1095.pfb
%{_fontdir}/sfdh1200.pfb
%{_fontdir}/sfdh1440.pfb
%{_fontdir}/sfdh1728.pfb
%{_fontdir}/sfdh2074.pfb
%{_fontdir}/sfdh2488.pfb
%{_fontdir}/sfdh2986.pfb
%{_fontdir}/sfdh3583.pfb
%{_fontdir}/sffb0500.pfb
%{_fontdir}/sffb0600.pfb
%{_fontdir}/sffb0700.pfb
%{_fontdir}/sffb0800.pfb
%{_fontdir}/sffb0900.pfb
%{_fontdir}/sffb1000.pfb
%{_fontdir}/sffb1095.pfb
%{_fontdir}/sffb1200.pfb
%{_fontdir}/sffb1440.pfb
%{_fontdir}/sffb1728.pfb
%{_fontdir}/sffb2074.pfb
%{_fontdir}/sfff0900.pfb
%{_fontdir}/sfff1000.pfb
%{_fontdir}/sfff1095.pfb
%{_fontdir}/sfff1200.pfb
%{_fontdir}/sfff1440.pfb
%{_fontdir}/sfff2488.pfb
%{_fontdir}/sffi0900.pfb
%{_fontdir}/sffi1000.pfb
%{_fontdir}/sffi1095.pfb
%{_fontdir}/sffi1200.pfb
%{_fontdir}/sffi1440.pfb
%{_fontdir}/sffi1728.pfb
%{_fontdir}/sffi2074.pfb
%{_fontdir}/sffs0500.pfb
%{_fontdir}/sffs0600.pfb
%{_fontdir}/sffs0700.pfb
%{_fontdir}/sffs0800.pfb
%{_fontdir}/sffs0900.pfb
%{_fontdir}/sffs1000.pfb
%{_fontdir}/sffs1095.pfb
%{_fontdir}/sffs1200.pfb
%{_fontdir}/sffs1440.pfb
%{_fontdir}/sffs1728.pfb
%{_fontdir}/sffs2074.pfb
%{_fontdir}/sfit0800.pfb
%{_fontdir}/sfit0900.pfb
%{_fontdir}/sfit1000.pfb
%{_fontdir}/sfit1095.pfb
%{_fontdir}/sfit1200.pfb
%{_fontdir}/sfit1440.pfb
%{_fontdir}/sfit1728.pfb
%{_fontdir}/sfit2074.pfb
%{_fontdir}/sfit2488.pfb
%{_fontdir}/sflb8.pfb
%{_fontdir}/sfli8.pfb
%{_fontdir}/sflo8.pfb
%{_fontdir}/sflq8.pfb
%{_fontdir}/sfltt8.pfb
%{_fontdir}/sfoc0500.pfb
%{_fontdir}/sfoc0600.pfb
%{_fontdir}/sfoc0700.pfb
%{_fontdir}/sfoc0800.pfb
%{_fontdir}/sfoc0900.pfb
%{_fontdir}/sfoc1000.pfb
%{_fontdir}/sfoc1095.pfb
%{_fontdir}/sfoc1200.pfb
%{_fontdir}/sfoc1440.pfb
%{_fontdir}/sfoc1728.pfb
%{_fontdir}/sfoc2074.pfb
%{_fontdir}/sfoc2488.pfb
%{_fontdir}/sfoc2986.pfb
%{_fontdir}/sfoc3583.pfb
%{_fontdir}/sfocc10.pfb
%{_fontdir}/sform10.pfb
%{_fontdir}/sform5.pfb
%{_fontdir}/sform6.pfb
%{_fontdir}/sform7.pfb
%{_fontdir}/sform8.pfb
%{_fontdir}/sform9.pfb
%{_fontdir}/sfosl10.pfb
%{_fontdir}/sfosl5.pfb
%{_fontdir}/sfosl6.pfb
%{_fontdir}/sfosl7.pfb
%{_fontdir}/sfosl8.pfb
%{_fontdir}/sfosl9.pfb
%{_fontdir}/sfoti10.pfb
%{_fontdir}/sfqi8.pfb
%{_fontdir}/sfrb0500.pfb
%{_fontdir}/sfrb0600.pfb
%{_fontdir}/sfrb0700.pfb
%{_fontdir}/sfrb0800.pfb
%{_fontdir}/sfrb0900.pfb
%{_fontdir}/sfrb1000.pfb
%{_fontdir}/sfrb1095.pfb
%{_fontdir}/sfrb1200.pfb
%{_fontdir}/sfrb1440.pfb
%{_fontdir}/sfrb1728.pfb
%{_fontdir}/sfrb2074.pfb
%{_fontdir}/sfrb2488.pfb
%{_fontdir}/sfrb2986.pfb
%{_fontdir}/sfrb3583.pfb
%{_fontdir}/sfrm0500.pfb
%{_fontdir}/sfrm0600.pfb
%{_fontdir}/sfrm0700.pfb
%{_fontdir}/sfrm0800.pfb
%{_fontdir}/sfrm0900.pfb
%{_fontdir}/sfrm1000.pfb
%{_fontdir}/sfrm1095.pfb
%{_fontdir}/sfrm1200.pfb
%{_fontdir}/sfrm1440.pfb
%{_fontdir}/sfrm1728.pfb
%{_fontdir}/sfrm2074.pfb
%{_fontdir}/sfrm2488.pfb
%{_fontdir}/sfrm2986.pfb
%{_fontdir}/sfrm3583.pfb
%{_fontdir}/sfsc0500.pfb
%{_fontdir}/sfsc0600.pfb
%{_fontdir}/sfsc0700.pfb
%{_fontdir}/sfsc0800.pfb
%{_fontdir}/sfsc0900.pfb
%{_fontdir}/sfsc1000.pfb
%{_fontdir}/sfsc1095.pfb
%{_fontdir}/sfsc1200.pfb
%{_fontdir}/sfsc1440.pfb
%{_fontdir}/sfsc1728.pfb
%{_fontdir}/sfsc2074.pfb
%{_fontdir}/sfsc2488.pfb
%{_fontdir}/sfsc2986.pfb
%{_fontdir}/sfsc3583.pfb
%{_fontdir}/sfsi0500.pfb
%{_fontdir}/sfsi0600.pfb
%{_fontdir}/sfsi0700.pfb
%{_fontdir}/sfsi0800.pfb
%{_fontdir}/sfsi0900.pfb
%{_fontdir}/sfsi1000.pfb
%{_fontdir}/sfsi1095.pfb
%{_fontdir}/sfsi1200.pfb
%{_fontdir}/sfsi1440.pfb
%{_fontdir}/sfsi1728.pfb
%{_fontdir}/sfsi2074.pfb
%{_fontdir}/sfsi2488.pfb
%{_fontdir}/sfsi2986.pfb
%{_fontdir}/sfsi3583.pfb
%{_fontdir}/sfsl0500.pfb
%{_fontdir}/sfsl0600.pfb
%{_fontdir}/sfsl0700.pfb
%{_fontdir}/sfsl0800.pfb
%{_fontdir}/sfsl0900.pfb
%{_fontdir}/sfsl1000.pfb
%{_fontdir}/sfsl1095.pfb
%{_fontdir}/sfsl1200.pfb
%{_fontdir}/sfsl1440.pfb
%{_fontdir}/sfsl1728.pfb
%{_fontdir}/sfsl2074.pfb
%{_fontdir}/sfsl2488.pfb
%{_fontdir}/sfsl2986.pfb
%{_fontdir}/sfsl3583.pfb
%{_fontdir}/sfso0500.pfb
%{_fontdir}/sfso0600.pfb
%{_fontdir}/sfso0700.pfb
%{_fontdir}/sfso0800.pfb
%{_fontdir}/sfso0900.pfb
%{_fontdir}/sfso1000.pfb
%{_fontdir}/sfso1095.pfb
%{_fontdir}/sfso1200.pfb
%{_fontdir}/sfso1440.pfb
%{_fontdir}/sfso1728.pfb
%{_fontdir}/sfso2074.pfb
%{_fontdir}/sfso2488.pfb
%{_fontdir}/sfso2986.pfb
%{_fontdir}/sfso3583.pfb
%{_fontdir}/sfsq8.pfb
%{_fontdir}/sfss0500.pfb
%{_fontdir}/sfss0600.pfb
%{_fontdir}/sfss0700.pfb
%{_fontdir}/sfss0800.pfb
%{_fontdir}/sfss0900.pfb
%{_fontdir}/sfss1000.pfb
%{_fontdir}/sfss1095.pfb
%{_fontdir}/sfss1200.pfb
%{_fontdir}/sfss1440.pfb
%{_fontdir}/sfss1728.pfb
%{_fontdir}/sfss2074.pfb
%{_fontdir}/sfss2488.pfb
%{_fontdir}/sfss2986.pfb
%{_fontdir}/sfss3583.pfb
%{_fontdir}/sfssdc10.pfb
%{_fontdir}/sfst0800.pfb
%{_fontdir}/sfst0900.pfb
%{_fontdir}/sfst1000.pfb
%{_fontdir}/sfst1095.pfb
%{_fontdir}/sfst1200.pfb
%{_fontdir}/sfst1440.pfb
%{_fontdir}/sfst1728.pfb
%{_fontdir}/sfst2074.pfb
%{_fontdir}/sfst2488.pfb
%{_fontdir}/sfst2986.pfb
%{_fontdir}/sfst3583.pfb
%{_fontdir}/sfsx0500.pfb
%{_fontdir}/sfsx0600.pfb
%{_fontdir}/sfsx0700.pfb
%{_fontdir}/sfsx0800.pfb
%{_fontdir}/sfsx0900.pfb
%{_fontdir}/sfsx1000.pfb
%{_fontdir}/sfsx1095.pfb
%{_fontdir}/sfsx1200.pfb
%{_fontdir}/sfsx1440.pfb
%{_fontdir}/sfsx1728.pfb
%{_fontdir}/sfsx2074.pfb
%{_fontdir}/sfsx2488.pfb
%{_fontdir}/sfsx2986.pfb
%{_fontdir}/sfsx3583.pfb
%{_fontdir}/sftc0800.pfb
%{_fontdir}/sftc0900.pfb
%{_fontdir}/sftc1000.pfb
%{_fontdir}/sftc1095.pfb
%{_fontdir}/sftc1200.pfb
%{_fontdir}/sftc1440.pfb
%{_fontdir}/sftc1728.pfb
%{_fontdir}/sftc2074.pfb
%{_fontdir}/sftc2488.pfb
%{_fontdir}/sftc2986.pfb
%{_fontdir}/sftc3583.pfb
%{_fontdir}/sfti0500.pfb
%{_fontdir}/sfti0600.pfb
%{_fontdir}/sfti0700.pfb
%{_fontdir}/sfti0800.pfb
%{_fontdir}/sfti0900.pfb
%{_fontdir}/sfti1000.pfb
%{_fontdir}/sfti1095.pfb
%{_fontdir}/sfti1200.pfb
%{_fontdir}/sfti1440.pfb
%{_fontdir}/sfti1728.pfb
%{_fontdir}/sfti2074.pfb
%{_fontdir}/sfti2488.pfb
%{_fontdir}/sfti2986.pfb
%{_fontdir}/sfti3583.pfb
%{_fontdir}/sftt0800.pfb
%{_fontdir}/sftt0900.pfb
%{_fontdir}/sftt1000.pfb
%{_fontdir}/sftt1095.pfb
%{_fontdir}/sftt1200.pfb
%{_fontdir}/sftt1440.pfb
%{_fontdir}/sftt1728.pfb
%{_fontdir}/sftt2074.pfb
%{_fontdir}/sftt2488.pfb
%{_fontdir}/sftt2986.pfb
%{_fontdir}/sftt3583.pfb
%{_fontdir}/sfui0500.pfb
%{_fontdir}/sfui0600.pfb
%{_fontdir}/sfui0700.pfb
%{_fontdir}/sfui0800.pfb
%{_fontdir}/sfui0900.pfb
%{_fontdir}/sfui1000.pfb
%{_fontdir}/sfui1095.pfb
%{_fontdir}/sfui1200.pfb
%{_fontdir}/sfui1440.pfb
%{_fontdir}/sfui1728.pfb
%{_fontdir}/sfui2074.pfb
%{_fontdir}/sfui2488.pfb
%{_fontdir}/sfui2986.pfb
%{_fontdir}/sfui3583.pfb
%{_fontdir}/sfvi0800.pfb
%{_fontdir}/sfvi0900.pfb
%{_fontdir}/sfvi1000.pfb
%{_fontdir}/sfvi1095.pfb
%{_fontdir}/sfvi1200.pfb
%{_fontdir}/sfvi1440.pfb
%{_fontdir}/sfvi1728.pfb
%{_fontdir}/sfvi2074.pfb
%{_fontdir}/sfvi2488.pfb
%{_fontdir}/sfvi2986.pfb
%{_fontdir}/sfvi3583.pfb
%{_fontdir}/sfvt0800.pfb
%{_fontdir}/sfvt0900.pfb
%{_fontdir}/sfvt1000.pfb
%{_fontdir}/sfvt1095.pfb
%{_fontdir}/sfvt1200.pfb
%{_fontdir}/sfvt1440.pfb
%{_fontdir}/sfvt1728.pfb
%{_fontdir}/sfvt2074.pfb
%{_fontdir}/sfvt2488.pfb
%{_fontdir}/sfvt2986.pfb
%{_fontdir}/sfvt3583.pfb
%{_fontdir}/sfxc0500.pfb
%{_fontdir}/sfxc0600.pfb
%{_fontdir}/sfxc0700.pfb
%{_fontdir}/sfxc0800.pfb
%{_fontdir}/sfxc0900.pfb
%{_fontdir}/sfxc1000.pfb
%{_fontdir}/sfxc1095.pfb
%{_fontdir}/sfxc1200.pfb
%{_fontdir}/sfxc1440.pfb
%{_fontdir}/sfxc1728.pfb
%{_fontdir}/sfxc2074.pfb
%{_fontdir}/sfxc2488.pfb
%{_fontdir}/sfxc2986.pfb
%{_fontdir}/sfxc3583.pfb

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
