%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cbfonts.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cbfonts.doc.tar.xz

Name: texlive-cbfonts
License: LPPL
Summary: Complete set of Greek fonts
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18157%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-cbfonts-fedora-fonts = %{tl_version}

%description
This bundle presents the whole of Beccari's original Greek font
set, both as MetaFont source and in Adobe Type 1 format. The
set is available at the same wide set of design sizes as are
such font sets as the EC fonts.

date: 2008-06-12 00:46:38 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "MixedMap cbgreek-full.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^MixedMap cbgreek-full.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for cbfonts
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18157%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for cbfonts

%package fedora-fonts
Summary: Fonts for cbfonts
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18157%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-cbfonts = %{tl_version}
BuildArch: noarch

%description fedora-fonts
This bundle presents the whole of Beccari's original Greek font
set, both as MetaFont source and in Adobe Type 1 format. The
set is available at the same wide set of design sizes as are
such font sets as the EC fonts.

date: 2008-06-12 00:46:38 +0200


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic0700.pfb .
ln -s %{_fontdir}/glic0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic0800.pfb .
ln -s %{_fontdir}/glic0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic1000.pfb .
ln -s %{_fontdir}/glic1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic1200.pfb .
ln -s %{_fontdir}/glic1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic1382.pfb .
ln -s %{_fontdir}/glic1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic1659.pfb .
ln -s %{_fontdir}/glic1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic1991.pfb .
ln -s %{_fontdir}/glic1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic2389.pfb .
ln -s %{_fontdir}/glic2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic2866.pfb .
ln -s %{_fontdir}/glic2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic3440.pfb .
ln -s %{_fontdir}/glic3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic4128.pfb .
ln -s %{_fontdir}/glic4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii0700.pfb .
ln -s %{_fontdir}/glii0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii0800.pfb .
ln -s %{_fontdir}/glii0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii1000.pfb .
ln -s %{_fontdir}/glii1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii1200.pfb .
ln -s %{_fontdir}/glii1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii1382.pfb .
ln -s %{_fontdir}/glii1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii1659.pfb .
ln -s %{_fontdir}/glii1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii1991.pfb .
ln -s %{_fontdir}/glii1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii2389.pfb .
ln -s %{_fontdir}/glii2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii2866.pfb .
ln -s %{_fontdir}/glii2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii3440.pfb .
ln -s %{_fontdir}/glii3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii4128.pfb .
ln -s %{_fontdir}/glii4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin0700.pfb .
ln -s %{_fontdir}/glin0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin0800.pfb .
ln -s %{_fontdir}/glin0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin1000.pfb .
ln -s %{_fontdir}/glin1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin1200.pfb .
ln -s %{_fontdir}/glin1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin1382.pfb .
ln -s %{_fontdir}/glin1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin1659.pfb .
ln -s %{_fontdir}/glin1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin1991.pfb .
ln -s %{_fontdir}/glin1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin2389.pfb .
ln -s %{_fontdir}/glin2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin2866.pfb .
ln -s %{_fontdir}/glin2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin3440.pfb .
ln -s %{_fontdir}/glin3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin4128.pfb .
ln -s %{_fontdir}/glin4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio0700.pfb .
ln -s %{_fontdir}/glio0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio0800.pfb .
ln -s %{_fontdir}/glio0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio1000.pfb .
ln -s %{_fontdir}/glio1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio1200.pfb .
ln -s %{_fontdir}/glio1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio1382.pfb .
ln -s %{_fontdir}/glio1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio1659.pfb .
ln -s %{_fontdir}/glio1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio1991.pfb .
ln -s %{_fontdir}/glio1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio2389.pfb .
ln -s %{_fontdir}/glio2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio2866.pfb .
ln -s %{_fontdir}/glio2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio3440.pfb .
ln -s %{_fontdir}/glio3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio4128.pfb .
ln -s %{_fontdir}/glio4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu0700.pfb .
ln -s %{_fontdir}/gliu0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu0800.pfb .
ln -s %{_fontdir}/gliu0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu1000.pfb .
ln -s %{_fontdir}/gliu1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu1200.pfb .
ln -s %{_fontdir}/gliu1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu1382.pfb .
ln -s %{_fontdir}/gliu1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu1659.pfb .
ln -s %{_fontdir}/gliu1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu1991.pfb .
ln -s %{_fontdir}/gliu1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu2389.pfb .
ln -s %{_fontdir}/gliu2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu2866.pfb .
ln -s %{_fontdir}/gliu2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu3440.pfb .
ln -s %{_fontdir}/gliu3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu4128.pfb .
ln -s %{_fontdir}/gliu4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc0700.pfb .
ln -s %{_fontdir}/gljc0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc0800.pfb .
ln -s %{_fontdir}/gljc0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc1000.pfb .
ln -s %{_fontdir}/gljc1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc1200.pfb .
ln -s %{_fontdir}/gljc1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc1382.pfb .
ln -s %{_fontdir}/gljc1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc1659.pfb .
ln -s %{_fontdir}/gljc1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc1991.pfb .
ln -s %{_fontdir}/gljc1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc2389.pfb .
ln -s %{_fontdir}/gljc2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc2866.pfb .
ln -s %{_fontdir}/gljc2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc3440.pfb .
ln -s %{_fontdir}/gljc3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc4128.pfb .
ln -s %{_fontdir}/gljc4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn0700.pfb .
ln -s %{_fontdir}/gljn0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn0800.pfb .
ln -s %{_fontdir}/gljn0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn1000.pfb .
ln -s %{_fontdir}/gljn1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn1200.pfb .
ln -s %{_fontdir}/gljn1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn1382.pfb .
ln -s %{_fontdir}/gljn1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn1659.pfb .
ln -s %{_fontdir}/gljn1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn1991.pfb .
ln -s %{_fontdir}/gljn1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn2389.pfb .
ln -s %{_fontdir}/gljn2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn2866.pfb .
ln -s %{_fontdir}/gljn2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn3440.pfb .
ln -s %{_fontdir}/gljn3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn4128.pfb .
ln -s %{_fontdir}/gljn4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo0700.pfb .
ln -s %{_fontdir}/gljo0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo0800.pfb .
ln -s %{_fontdir}/gljo0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo1000.pfb .
ln -s %{_fontdir}/gljo1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo1200.pfb .
ln -s %{_fontdir}/gljo1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo1382.pfb .
ln -s %{_fontdir}/gljo1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo1659.pfb .
ln -s %{_fontdir}/gljo1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo1991.pfb .
ln -s %{_fontdir}/gljo1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo2389.pfb .
ln -s %{_fontdir}/gljo2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo2866.pfb .
ln -s %{_fontdir}/gljo2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo3440.pfb .
ln -s %{_fontdir}/gljo3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo4128.pfb .
ln -s %{_fontdir}/gljo4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc0700.pfb .
ln -s %{_fontdir}/glmc0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc0800.pfb .
ln -s %{_fontdir}/glmc0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc1000.pfb .
ln -s %{_fontdir}/glmc1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc1200.pfb .
ln -s %{_fontdir}/glmc1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc1382.pfb .
ln -s %{_fontdir}/glmc1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc1659.pfb .
ln -s %{_fontdir}/glmc1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc1991.pfb .
ln -s %{_fontdir}/glmc1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc2389.pfb .
ln -s %{_fontdir}/glmc2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc2866.pfb .
ln -s %{_fontdir}/glmc2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc3440.pfb .
ln -s %{_fontdir}/glmc3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc4128.pfb .
ln -s %{_fontdir}/glmc4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi0700.pfb .
ln -s %{_fontdir}/glmi0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi0800.pfb .
ln -s %{_fontdir}/glmi0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi1000.pfb .
ln -s %{_fontdir}/glmi1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi1200.pfb .
ln -s %{_fontdir}/glmi1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi1382.pfb .
ln -s %{_fontdir}/glmi1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi1659.pfb .
ln -s %{_fontdir}/glmi1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi1991.pfb .
ln -s %{_fontdir}/glmi1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi2389.pfb .
ln -s %{_fontdir}/glmi2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi2866.pfb .
ln -s %{_fontdir}/glmi2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi3440.pfb .
ln -s %{_fontdir}/glmi3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi4128.pfb .
ln -s %{_fontdir}/glmi4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn0700.pfb .
ln -s %{_fontdir}/glmn0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn0800.pfb .
ln -s %{_fontdir}/glmn0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn1000.pfb .
ln -s %{_fontdir}/glmn1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn1200.pfb .
ln -s %{_fontdir}/glmn1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn1382.pfb .
ln -s %{_fontdir}/glmn1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn1659.pfb .
ln -s %{_fontdir}/glmn1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn1991.pfb .
ln -s %{_fontdir}/glmn1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn2389.pfb .
ln -s %{_fontdir}/glmn2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn2866.pfb .
ln -s %{_fontdir}/glmn2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn3440.pfb .
ln -s %{_fontdir}/glmn3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn4128.pfb .
ln -s %{_fontdir}/glmn4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo0700.pfb .
ln -s %{_fontdir}/glmo0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo0800.pfb .
ln -s %{_fontdir}/glmo0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo1000.pfb .
ln -s %{_fontdir}/glmo1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo1200.pfb .
ln -s %{_fontdir}/glmo1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo1382.pfb .
ln -s %{_fontdir}/glmo1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo1659.pfb .
ln -s %{_fontdir}/glmo1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo1991.pfb .
ln -s %{_fontdir}/glmo1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo2389.pfb .
ln -s %{_fontdir}/glmo2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo2866.pfb .
ln -s %{_fontdir}/glmo2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo3440.pfb .
ln -s %{_fontdir}/glmo3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo4128.pfb .
ln -s %{_fontdir}/glmo4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu0700.pfb .
ln -s %{_fontdir}/glmu0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu0800.pfb .
ln -s %{_fontdir}/glmu0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu1000.pfb .
ln -s %{_fontdir}/glmu1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu1200.pfb .
ln -s %{_fontdir}/glmu1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu1382.pfb .
ln -s %{_fontdir}/glmu1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu1659.pfb .
ln -s %{_fontdir}/glmu1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu1991.pfb .
ln -s %{_fontdir}/glmu1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu2389.pfb .
ln -s %{_fontdir}/glmu2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu2866.pfb .
ln -s %{_fontdir}/glmu2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu3440.pfb .
ln -s %{_fontdir}/glmu3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu4128.pfb .
ln -s %{_fontdir}/glmu4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc0700.pfb .
ln -s %{_fontdir}/gltc0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc0800.pfb .
ln -s %{_fontdir}/gltc0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc1000.pfb .
ln -s %{_fontdir}/gltc1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc1200.pfb .
ln -s %{_fontdir}/gltc1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc1382.pfb .
ln -s %{_fontdir}/gltc1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc1659.pfb .
ln -s %{_fontdir}/gltc1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc1991.pfb .
ln -s %{_fontdir}/gltc1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc2389.pfb .
ln -s %{_fontdir}/gltc2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc2866.pfb .
ln -s %{_fontdir}/gltc2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc3440.pfb .
ln -s %{_fontdir}/gltc3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc4128.pfb .
ln -s %{_fontdir}/gltc4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn0700.pfb .
ln -s %{_fontdir}/gltn0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn0800.pfb .
ln -s %{_fontdir}/gltn0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn1000.pfb .
ln -s %{_fontdir}/gltn1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn1200.pfb .
ln -s %{_fontdir}/gltn1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn1382.pfb .
ln -s %{_fontdir}/gltn1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn1659.pfb .
ln -s %{_fontdir}/gltn1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn1991.pfb .
ln -s %{_fontdir}/gltn1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn2389.pfb .
ln -s %{_fontdir}/gltn2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn2866.pfb .
ln -s %{_fontdir}/gltn2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn3440.pfb .
ln -s %{_fontdir}/gltn3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn4128.pfb .
ln -s %{_fontdir}/gltn4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto0700.pfb .
ln -s %{_fontdir}/glto0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto0800.pfb .
ln -s %{_fontdir}/glto0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto1000.pfb .
ln -s %{_fontdir}/glto1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto1200.pfb .
ln -s %{_fontdir}/glto1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto1382.pfb .
ln -s %{_fontdir}/glto1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto1659.pfb .
ln -s %{_fontdir}/glto1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto1991.pfb .
ln -s %{_fontdir}/glto1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto2389.pfb .
ln -s %{_fontdir}/glto2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto2866.pfb .
ln -s %{_fontdir}/glto2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto3440.pfb .
ln -s %{_fontdir}/glto3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto4128.pfb .
ln -s %{_fontdir}/glto4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc0700.pfb .
ln -s %{_fontdir}/glwc0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc0800.pfb .
ln -s %{_fontdir}/glwc0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc1000.pfb .
ln -s %{_fontdir}/glwc1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc1200.pfb .
ln -s %{_fontdir}/glwc1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc1382.pfb .
ln -s %{_fontdir}/glwc1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc1659.pfb .
ln -s %{_fontdir}/glwc1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc1991.pfb .
ln -s %{_fontdir}/glwc1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc2389.pfb .
ln -s %{_fontdir}/glwc2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc2866.pfb .
ln -s %{_fontdir}/glwc2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc3440.pfb .
ln -s %{_fontdir}/glwc3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc4128.pfb .
ln -s %{_fontdir}/glwc4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi0700.pfb .
ln -s %{_fontdir}/glwi0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi0800.pfb .
ln -s %{_fontdir}/glwi0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi1000.pfb .
ln -s %{_fontdir}/glwi1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi1200.pfb .
ln -s %{_fontdir}/glwi1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi1382.pfb .
ln -s %{_fontdir}/glwi1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi1659.pfb .
ln -s %{_fontdir}/glwi1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi1991.pfb .
ln -s %{_fontdir}/glwi1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi2389.pfb .
ln -s %{_fontdir}/glwi2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi2866.pfb .
ln -s %{_fontdir}/glwi2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi3440.pfb .
ln -s %{_fontdir}/glwi3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi4128.pfb .
ln -s %{_fontdir}/glwi4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn0700.pfb .
ln -s %{_fontdir}/glwn0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn0800.pfb .
ln -s %{_fontdir}/glwn0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn1000.pfb .
ln -s %{_fontdir}/glwn1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn1200.pfb .
ln -s %{_fontdir}/glwn1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn1382.pfb .
ln -s %{_fontdir}/glwn1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn1659.pfb .
ln -s %{_fontdir}/glwn1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn1991.pfb .
ln -s %{_fontdir}/glwn1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn2389.pfb .
ln -s %{_fontdir}/glwn2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn2866.pfb .
ln -s %{_fontdir}/glwn2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn3440.pfb .
ln -s %{_fontdir}/glwn3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn4128.pfb .
ln -s %{_fontdir}/glwn4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo0700.pfb .
ln -s %{_fontdir}/glwo0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo0800.pfb .
ln -s %{_fontdir}/glwo0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo1000.pfb .
ln -s %{_fontdir}/glwo1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo1200.pfb .
ln -s %{_fontdir}/glwo1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo1382.pfb .
ln -s %{_fontdir}/glwo1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo1659.pfb .
ln -s %{_fontdir}/glwo1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo1991.pfb .
ln -s %{_fontdir}/glwo1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo2389.pfb .
ln -s %{_fontdir}/glwo2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo2866.pfb .
ln -s %{_fontdir}/glwo2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo3440.pfb .
ln -s %{_fontdir}/glwo3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo4128.pfb .
ln -s %{_fontdir}/glwo4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu0700.pfb .
ln -s %{_fontdir}/glwu0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu0800.pfb .
ln -s %{_fontdir}/glwu0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu1000.pfb .
ln -s %{_fontdir}/glwu1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu1200.pfb .
ln -s %{_fontdir}/glwu1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu1382.pfb .
ln -s %{_fontdir}/glwu1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu1659.pfb .
ln -s %{_fontdir}/glwu1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu1991.pfb .
ln -s %{_fontdir}/glwu1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu2389.pfb .
ln -s %{_fontdir}/glwu2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu2866.pfb .
ln -s %{_fontdir}/glwu2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu3440.pfb .
ln -s %{_fontdir}/glwu3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu4128.pfb .
ln -s %{_fontdir}/glwu4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc0700.pfb .
ln -s %{_fontdir}/glxc0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc0800.pfb .
ln -s %{_fontdir}/glxc0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc1000.pfb .
ln -s %{_fontdir}/glxc1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc1200.pfb .
ln -s %{_fontdir}/glxc1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc1382.pfb .
ln -s %{_fontdir}/glxc1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc1659.pfb .
ln -s %{_fontdir}/glxc1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc1991.pfb .
ln -s %{_fontdir}/glxc1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc2389.pfb .
ln -s %{_fontdir}/glxc2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc2866.pfb .
ln -s %{_fontdir}/glxc2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc3440.pfb .
ln -s %{_fontdir}/glxc3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc4128.pfb .
ln -s %{_fontdir}/glxc4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi0700.pfb .
ln -s %{_fontdir}/glxi0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi0800.pfb .
ln -s %{_fontdir}/glxi0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi1000.pfb .
ln -s %{_fontdir}/glxi1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi1200.pfb .
ln -s %{_fontdir}/glxi1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi1382.pfb .
ln -s %{_fontdir}/glxi1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi1659.pfb .
ln -s %{_fontdir}/glxi1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi1991.pfb .
ln -s %{_fontdir}/glxi1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi2389.pfb .
ln -s %{_fontdir}/glxi2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi2866.pfb .
ln -s %{_fontdir}/glxi2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi3440.pfb .
ln -s %{_fontdir}/glxi3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi4128.pfb .
ln -s %{_fontdir}/glxi4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn0700.pfb .
ln -s %{_fontdir}/glxn0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn0800.pfb .
ln -s %{_fontdir}/glxn0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn1000.pfb .
ln -s %{_fontdir}/glxn1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn1200.pfb .
ln -s %{_fontdir}/glxn1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn1382.pfb .
ln -s %{_fontdir}/glxn1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn1659.pfb .
ln -s %{_fontdir}/glxn1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn1991.pfb .
ln -s %{_fontdir}/glxn1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn2389.pfb .
ln -s %{_fontdir}/glxn2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn2866.pfb .
ln -s %{_fontdir}/glxn2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn3440.pfb .
ln -s %{_fontdir}/glxn3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn4128.pfb .
ln -s %{_fontdir}/glxn4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo0700.pfb .
ln -s %{_fontdir}/glxo0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo0800.pfb .
ln -s %{_fontdir}/glxo0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo1000.pfb .
ln -s %{_fontdir}/glxo1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo1200.pfb .
ln -s %{_fontdir}/glxo1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo1382.pfb .
ln -s %{_fontdir}/glxo1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo1659.pfb .
ln -s %{_fontdir}/glxo1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo1991.pfb .
ln -s %{_fontdir}/glxo1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo2389.pfb .
ln -s %{_fontdir}/glxo2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo2866.pfb .
ln -s %{_fontdir}/glxo2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo3440.pfb .
ln -s %{_fontdir}/glxo3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo4128.pfb .
ln -s %{_fontdir}/glxo4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu0700.pfb .
ln -s %{_fontdir}/glxu0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu0800.pfb .
ln -s %{_fontdir}/glxu0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu1000.pfb .
ln -s %{_fontdir}/glxu1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu1200.pfb .
ln -s %{_fontdir}/glxu1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu1382.pfb .
ln -s %{_fontdir}/glxu1382.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu1382.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu1659.pfb .
ln -s %{_fontdir}/glxu1659.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu1659.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu1991.pfb .
ln -s %{_fontdir}/glxu1991.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu1991.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu2389.pfb .
ln -s %{_fontdir}/glxu2389.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu2389.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu2866.pfb .
ln -s %{_fontdir}/glxu2866.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu2866.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu3440.pfb .
ln -s %{_fontdir}/glxu3440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu3440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu4128.pfb .
ln -s %{_fontdir}/glxu4128.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu4128.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn0500.pfb .
ln -s %{_fontdir}/gmmn0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn0600.pfb .
ln -s %{_fontdir}/gmmn0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn0700.pfb .
ln -s %{_fontdir}/gmmn0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn0800.pfb .
ln -s %{_fontdir}/gmmn0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn0900.pfb .
ln -s %{_fontdir}/gmmn0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn1000.pfb .
ln -s %{_fontdir}/gmmn1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn1095.pfb .
ln -s %{_fontdir}/gmmn1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn1200.pfb .
ln -s %{_fontdir}/gmmn1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn1440.pfb .
ln -s %{_fontdir}/gmmn1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn1728.pfb .
ln -s %{_fontdir}/gmmn1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn2074.pfb .
ln -s %{_fontdir}/gmmn2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn2488.pfb .
ln -s %{_fontdir}/gmmn2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn2986.pfb .
ln -s %{_fontdir}/gmmn2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn3583.pfb .
ln -s %{_fontdir}/gmmn3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo0500.pfb .
ln -s %{_fontdir}/gmmo0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo0600.pfb .
ln -s %{_fontdir}/gmmo0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo0700.pfb .
ln -s %{_fontdir}/gmmo0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo0800.pfb .
ln -s %{_fontdir}/gmmo0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo0900.pfb .
ln -s %{_fontdir}/gmmo0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo1000.pfb .
ln -s %{_fontdir}/gmmo1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo1095.pfb .
ln -s %{_fontdir}/gmmo1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo1200.pfb .
ln -s %{_fontdir}/gmmo1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo1440.pfb .
ln -s %{_fontdir}/gmmo1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo1728.pfb .
ln -s %{_fontdir}/gmmo1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo2074.pfb .
ln -s %{_fontdir}/gmmo2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo2488.pfb .
ln -s %{_fontdir}/gmmo2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo2986.pfb .
ln -s %{_fontdir}/gmmo2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo3583.pfb .
ln -s %{_fontdir}/gmmo3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr0500.pfb .
ln -s %{_fontdir}/gmtr0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr0600.pfb .
ln -s %{_fontdir}/gmtr0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr0700.pfb .
ln -s %{_fontdir}/gmtr0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr0800.pfb .
ln -s %{_fontdir}/gmtr0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr0900.pfb .
ln -s %{_fontdir}/gmtr0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr1000.pfb .
ln -s %{_fontdir}/gmtr1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr1095.pfb .
ln -s %{_fontdir}/gmtr1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr1200.pfb .
ln -s %{_fontdir}/gmtr1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr1440.pfb .
ln -s %{_fontdir}/gmtr1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr1728.pfb .
ln -s %{_fontdir}/gmtr1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr2074.pfb .
ln -s %{_fontdir}/gmtr2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr2488.pfb .
ln -s %{_fontdir}/gmtr2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr2986.pfb .
ln -s %{_fontdir}/gmtr2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr3583.pfb .
ln -s %{_fontdir}/gmtr3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn0500.pfb .
ln -s %{_fontdir}/gmxn0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn0600.pfb .
ln -s %{_fontdir}/gmxn0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn0700.pfb .
ln -s %{_fontdir}/gmxn0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn0800.pfb .
ln -s %{_fontdir}/gmxn0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn0900.pfb .
ln -s %{_fontdir}/gmxn0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn1000.pfb .
ln -s %{_fontdir}/gmxn1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn1095.pfb .
ln -s %{_fontdir}/gmxn1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn1200.pfb .
ln -s %{_fontdir}/gmxn1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn1440.pfb .
ln -s %{_fontdir}/gmxn1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn1728.pfb .
ln -s %{_fontdir}/gmxn1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn2074.pfb .
ln -s %{_fontdir}/gmxn2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn2488.pfb .
ln -s %{_fontdir}/gmxn2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn2986.pfb .
ln -s %{_fontdir}/gmxn2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn3583.pfb .
ln -s %{_fontdir}/gmxn3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo0500.pfb .
ln -s %{_fontdir}/gmxo0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo0600.pfb .
ln -s %{_fontdir}/gmxo0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo0700.pfb .
ln -s %{_fontdir}/gmxo0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo0800.pfb .
ln -s %{_fontdir}/gmxo0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo0900.pfb .
ln -s %{_fontdir}/gmxo0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo1000.pfb .
ln -s %{_fontdir}/gmxo1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo1095.pfb .
ln -s %{_fontdir}/gmxo1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo1200.pfb .
ln -s %{_fontdir}/gmxo1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo1440.pfb .
ln -s %{_fontdir}/gmxo1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo1728.pfb .
ln -s %{_fontdir}/gmxo1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo2074.pfb .
ln -s %{_fontdir}/gmxo2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo2488.pfb .
ln -s %{_fontdir}/gmxo2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo2986.pfb .
ln -s %{_fontdir}/gmxo2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo3583.pfb .
ln -s %{_fontdir}/gmxo3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc0500.pfb .
ln -s %{_fontdir}/gomc0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc0600.pfb .
ln -s %{_fontdir}/gomc0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc0700.pfb .
ln -s %{_fontdir}/gomc0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc0800.pfb .
ln -s %{_fontdir}/gomc0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc0900.pfb .
ln -s %{_fontdir}/gomc0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc1000.pfb .
ln -s %{_fontdir}/gomc1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc1095.pfb .
ln -s %{_fontdir}/gomc1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc1200.pfb .
ln -s %{_fontdir}/gomc1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc1440.pfb .
ln -s %{_fontdir}/gomc1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc1728.pfb .
ln -s %{_fontdir}/gomc1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc2074.pfb .
ln -s %{_fontdir}/gomc2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc2488.pfb .
ln -s %{_fontdir}/gomc2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc2986.pfb .
ln -s %{_fontdir}/gomc2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc3583.pfb .
ln -s %{_fontdir}/gomc3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi0500.pfb .
ln -s %{_fontdir}/gomi0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi0600.pfb .
ln -s %{_fontdir}/gomi0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi0700.pfb .
ln -s %{_fontdir}/gomi0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi0800.pfb .
ln -s %{_fontdir}/gomi0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi0900.pfb .
ln -s %{_fontdir}/gomi0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi1000.pfb .
ln -s %{_fontdir}/gomi1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi1095.pfb .
ln -s %{_fontdir}/gomi1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi1200.pfb .
ln -s %{_fontdir}/gomi1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi1440.pfb .
ln -s %{_fontdir}/gomi1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi1728.pfb .
ln -s %{_fontdir}/gomi1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi2074.pfb .
ln -s %{_fontdir}/gomi2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi2488.pfb .
ln -s %{_fontdir}/gomi2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi2986.pfb .
ln -s %{_fontdir}/gomi2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi3583.pfb .
ln -s %{_fontdir}/gomi3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn0500.pfb .
ln -s %{_fontdir}/gomn0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn0600.pfb .
ln -s %{_fontdir}/gomn0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn0700.pfb .
ln -s %{_fontdir}/gomn0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn0800.pfb .
ln -s %{_fontdir}/gomn0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn0900.pfb .
ln -s %{_fontdir}/gomn0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn1000.pfb .
ln -s %{_fontdir}/gomn1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn1095.pfb .
ln -s %{_fontdir}/gomn1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn1200.pfb .
ln -s %{_fontdir}/gomn1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn1440.pfb .
ln -s %{_fontdir}/gomn1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn1728.pfb .
ln -s %{_fontdir}/gomn1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn2074.pfb .
ln -s %{_fontdir}/gomn2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn2488.pfb .
ln -s %{_fontdir}/gomn2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn2986.pfb .
ln -s %{_fontdir}/gomn2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn3583.pfb .
ln -s %{_fontdir}/gomn3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo0500.pfb .
ln -s %{_fontdir}/gomo0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo0600.pfb .
ln -s %{_fontdir}/gomo0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo0700.pfb .
ln -s %{_fontdir}/gomo0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo0800.pfb .
ln -s %{_fontdir}/gomo0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo0900.pfb .
ln -s %{_fontdir}/gomo0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo1000.pfb .
ln -s %{_fontdir}/gomo1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo1095.pfb .
ln -s %{_fontdir}/gomo1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo1200.pfb .
ln -s %{_fontdir}/gomo1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo1440.pfb .
ln -s %{_fontdir}/gomo1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo1728.pfb .
ln -s %{_fontdir}/gomo1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo2074.pfb .
ln -s %{_fontdir}/gomo2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo2488.pfb .
ln -s %{_fontdir}/gomo2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo2986.pfb .
ln -s %{_fontdir}/gomo2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo3583.pfb .
ln -s %{_fontdir}/gomo3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu0500.pfb .
ln -s %{_fontdir}/gomu0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu0600.pfb .
ln -s %{_fontdir}/gomu0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu0700.pfb .
ln -s %{_fontdir}/gomu0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu0800.pfb .
ln -s %{_fontdir}/gomu0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu0900.pfb .
ln -s %{_fontdir}/gomu0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu1000.pfb .
ln -s %{_fontdir}/gomu1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu1095.pfb .
ln -s %{_fontdir}/gomu1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu1200.pfb .
ln -s %{_fontdir}/gomu1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu1440.pfb .
ln -s %{_fontdir}/gomu1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu1728.pfb .
ln -s %{_fontdir}/gomu1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu2074.pfb .
ln -s %{_fontdir}/gomu2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu2488.pfb .
ln -s %{_fontdir}/gomu2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu2986.pfb .
ln -s %{_fontdir}/gomu2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu3583.pfb .
ln -s %{_fontdir}/gomu3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc0500.pfb .
ln -s %{_fontdir}/goxc0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc0600.pfb .
ln -s %{_fontdir}/goxc0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc0700.pfb .
ln -s %{_fontdir}/goxc0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc0800.pfb .
ln -s %{_fontdir}/goxc0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc0900.pfb .
ln -s %{_fontdir}/goxc0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc1000.pfb .
ln -s %{_fontdir}/goxc1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc1095.pfb .
ln -s %{_fontdir}/goxc1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc1200.pfb .
ln -s %{_fontdir}/goxc1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc1440.pfb .
ln -s %{_fontdir}/goxc1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc1728.pfb .
ln -s %{_fontdir}/goxc1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc2074.pfb .
ln -s %{_fontdir}/goxc2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc2488.pfb .
ln -s %{_fontdir}/goxc2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc2986.pfb .
ln -s %{_fontdir}/goxc2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc3583.pfb .
ln -s %{_fontdir}/goxc3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi0500.pfb .
ln -s %{_fontdir}/goxi0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi0600.pfb .
ln -s %{_fontdir}/goxi0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi0700.pfb .
ln -s %{_fontdir}/goxi0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi0800.pfb .
ln -s %{_fontdir}/goxi0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi0900.pfb .
ln -s %{_fontdir}/goxi0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi1000.pfb .
ln -s %{_fontdir}/goxi1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi1095.pfb .
ln -s %{_fontdir}/goxi1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi1200.pfb .
ln -s %{_fontdir}/goxi1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi1440.pfb .
ln -s %{_fontdir}/goxi1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi1728.pfb .
ln -s %{_fontdir}/goxi1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi2074.pfb .
ln -s %{_fontdir}/goxi2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi2488.pfb .
ln -s %{_fontdir}/goxi2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi2986.pfb .
ln -s %{_fontdir}/goxi2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi3583.pfb .
ln -s %{_fontdir}/goxi3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn0500.pfb .
ln -s %{_fontdir}/goxn0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn0600.pfb .
ln -s %{_fontdir}/goxn0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn0700.pfb .
ln -s %{_fontdir}/goxn0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn0800.pfb .
ln -s %{_fontdir}/goxn0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn0900.pfb .
ln -s %{_fontdir}/goxn0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn1000.pfb .
ln -s %{_fontdir}/goxn1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn1095.pfb .
ln -s %{_fontdir}/goxn1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn1200.pfb .
ln -s %{_fontdir}/goxn1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn1440.pfb .
ln -s %{_fontdir}/goxn1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn1728.pfb .
ln -s %{_fontdir}/goxn1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn2074.pfb .
ln -s %{_fontdir}/goxn2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn2488.pfb .
ln -s %{_fontdir}/goxn2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn2986.pfb .
ln -s %{_fontdir}/goxn2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn3583.pfb .
ln -s %{_fontdir}/goxn3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo0500.pfb .
ln -s %{_fontdir}/goxo0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo0600.pfb .
ln -s %{_fontdir}/goxo0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo0700.pfb .
ln -s %{_fontdir}/goxo0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo0800.pfb .
ln -s %{_fontdir}/goxo0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo0900.pfb .
ln -s %{_fontdir}/goxo0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo1000.pfb .
ln -s %{_fontdir}/goxo1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo1095.pfb .
ln -s %{_fontdir}/goxo1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo1200.pfb .
ln -s %{_fontdir}/goxo1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo1440.pfb .
ln -s %{_fontdir}/goxo1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo1728.pfb .
ln -s %{_fontdir}/goxo1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo2074.pfb .
ln -s %{_fontdir}/goxo2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo2488.pfb .
ln -s %{_fontdir}/goxo2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo2986.pfb .
ln -s %{_fontdir}/goxo2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo3583.pfb .
ln -s %{_fontdir}/goxo3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu0500.pfb .
ln -s %{_fontdir}/goxu0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu0600.pfb .
ln -s %{_fontdir}/goxu0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu0700.pfb .
ln -s %{_fontdir}/goxu0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu0800.pfb .
ln -s %{_fontdir}/goxu0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu0900.pfb .
ln -s %{_fontdir}/goxu0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu1000.pfb .
ln -s %{_fontdir}/goxu1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu1095.pfb .
ln -s %{_fontdir}/goxu1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu1200.pfb .
ln -s %{_fontdir}/goxu1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu1440.pfb .
ln -s %{_fontdir}/goxu1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu1728.pfb .
ln -s %{_fontdir}/goxu1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu2074.pfb .
ln -s %{_fontdir}/goxu2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu2488.pfb .
ln -s %{_fontdir}/goxu2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu2986.pfb .
ln -s %{_fontdir}/goxu2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu3583.pfb .
ln -s %{_fontdir}/goxu3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl0500.pfb .
ln -s %{_fontdir}/grbl0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl0600.pfb .
ln -s %{_fontdir}/grbl0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl0700.pfb .
ln -s %{_fontdir}/grbl0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl0800.pfb .
ln -s %{_fontdir}/grbl0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl0900.pfb .
ln -s %{_fontdir}/grbl0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl1000.pfb .
ln -s %{_fontdir}/grbl1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl1095.pfb .
ln -s %{_fontdir}/grbl1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl1200.pfb .
ln -s %{_fontdir}/grbl1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl1440.pfb .
ln -s %{_fontdir}/grbl1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl1728.pfb .
ln -s %{_fontdir}/grbl1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl2074.pfb .
ln -s %{_fontdir}/grbl2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl2488.pfb .
ln -s %{_fontdir}/grbl2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl2986.pfb .
ln -s %{_fontdir}/grbl2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl3583.pfb .
ln -s %{_fontdir}/grbl3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc0500.pfb .
ln -s %{_fontdir}/grmc0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc0600.pfb .
ln -s %{_fontdir}/grmc0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc0700.pfb .
ln -s %{_fontdir}/grmc0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc0800.pfb .
ln -s %{_fontdir}/grmc0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc0900.pfb .
ln -s %{_fontdir}/grmc0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc1000.pfb .
ln -s %{_fontdir}/grmc1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc1095.pfb .
ln -s %{_fontdir}/grmc1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc1200.pfb .
ln -s %{_fontdir}/grmc1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc1440.pfb .
ln -s %{_fontdir}/grmc1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc1728.pfb .
ln -s %{_fontdir}/grmc1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc2074.pfb .
ln -s %{_fontdir}/grmc2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc2488.pfb .
ln -s %{_fontdir}/grmc2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc2986.pfb .
ln -s %{_fontdir}/grmc2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc3583.pfb .
ln -s %{_fontdir}/grmc3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi0500.pfb .
ln -s %{_fontdir}/grmi0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi0600.pfb .
ln -s %{_fontdir}/grmi0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi0700.pfb .
ln -s %{_fontdir}/grmi0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi0800.pfb .
ln -s %{_fontdir}/grmi0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi0900.pfb .
ln -s %{_fontdir}/grmi0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi1000.pfb .
ln -s %{_fontdir}/grmi1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi1095.pfb .
ln -s %{_fontdir}/grmi1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi1200.pfb .
ln -s %{_fontdir}/grmi1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi1440.pfb .
ln -s %{_fontdir}/grmi1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi1728.pfb .
ln -s %{_fontdir}/grmi1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi2074.pfb .
ln -s %{_fontdir}/grmi2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi2488.pfb .
ln -s %{_fontdir}/grmi2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi2986.pfb .
ln -s %{_fontdir}/grmi2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi3583.pfb .
ln -s %{_fontdir}/grmi3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml0500.pfb .
ln -s %{_fontdir}/grml0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml0600.pfb .
ln -s %{_fontdir}/grml0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml0700.pfb .
ln -s %{_fontdir}/grml0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml0800.pfb .
ln -s %{_fontdir}/grml0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml0900.pfb .
ln -s %{_fontdir}/grml0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml1000.pfb .
ln -s %{_fontdir}/grml1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml1095.pfb .
ln -s %{_fontdir}/grml1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml1200.pfb .
ln -s %{_fontdir}/grml1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml1440.pfb .
ln -s %{_fontdir}/grml1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml1728.pfb .
ln -s %{_fontdir}/grml1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml2074.pfb .
ln -s %{_fontdir}/grml2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml2488.pfb .
ln -s %{_fontdir}/grml2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml2986.pfb .
ln -s %{_fontdir}/grml2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml3583.pfb .
ln -s %{_fontdir}/grml3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn0500.pfb .
ln -s %{_fontdir}/grmn0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn0600.pfb .
ln -s %{_fontdir}/grmn0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn0700.pfb .
ln -s %{_fontdir}/grmn0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn0800.pfb .
ln -s %{_fontdir}/grmn0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn0900.pfb .
ln -s %{_fontdir}/grmn0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn1000.pfb .
ln -s %{_fontdir}/grmn1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn1095.pfb .
ln -s %{_fontdir}/grmn1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn1200.pfb .
ln -s %{_fontdir}/grmn1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn1440.pfb .
ln -s %{_fontdir}/grmn1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn1728.pfb .
ln -s %{_fontdir}/grmn1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn2074.pfb .
ln -s %{_fontdir}/grmn2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn2488.pfb .
ln -s %{_fontdir}/grmn2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn2986.pfb .
ln -s %{_fontdir}/grmn2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn3583.pfb .
ln -s %{_fontdir}/grmn3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo0500.pfb .
ln -s %{_fontdir}/grmo0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo0600.pfb .
ln -s %{_fontdir}/grmo0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo0700.pfb .
ln -s %{_fontdir}/grmo0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo0800.pfb .
ln -s %{_fontdir}/grmo0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo0900.pfb .
ln -s %{_fontdir}/grmo0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo1000.pfb .
ln -s %{_fontdir}/grmo1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo1095.pfb .
ln -s %{_fontdir}/grmo1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo1200.pfb .
ln -s %{_fontdir}/grmo1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo1440.pfb .
ln -s %{_fontdir}/grmo1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo1728.pfb .
ln -s %{_fontdir}/grmo1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo2074.pfb .
ln -s %{_fontdir}/grmo2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo2488.pfb .
ln -s %{_fontdir}/grmo2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo2986.pfb .
ln -s %{_fontdir}/grmo2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo3583.pfb .
ln -s %{_fontdir}/grmo3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu0500.pfb .
ln -s %{_fontdir}/grmu0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu0600.pfb .
ln -s %{_fontdir}/grmu0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu0700.pfb .
ln -s %{_fontdir}/grmu0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu0800.pfb .
ln -s %{_fontdir}/grmu0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu0900.pfb .
ln -s %{_fontdir}/grmu0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu1000.pfb .
ln -s %{_fontdir}/grmu1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu1095.pfb .
ln -s %{_fontdir}/grmu1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu1200.pfb .
ln -s %{_fontdir}/grmu1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu1440.pfb .
ln -s %{_fontdir}/grmu1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu1728.pfb .
ln -s %{_fontdir}/grmu1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu2074.pfb .
ln -s %{_fontdir}/grmu2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu2488.pfb .
ln -s %{_fontdir}/grmu2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu2986.pfb .
ln -s %{_fontdir}/grmu2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu3583.pfb .
ln -s %{_fontdir}/grmu3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc0500.pfb .
ln -s %{_fontdir}/grxc0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc0600.pfb .
ln -s %{_fontdir}/grxc0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc0700.pfb .
ln -s %{_fontdir}/grxc0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc0800.pfb .
ln -s %{_fontdir}/grxc0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc0900.pfb .
ln -s %{_fontdir}/grxc0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc1000.pfb .
ln -s %{_fontdir}/grxc1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc1095.pfb .
ln -s %{_fontdir}/grxc1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc1200.pfb .
ln -s %{_fontdir}/grxc1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc1440.pfb .
ln -s %{_fontdir}/grxc1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc1728.pfb .
ln -s %{_fontdir}/grxc1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc2074.pfb .
ln -s %{_fontdir}/grxc2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc2488.pfb .
ln -s %{_fontdir}/grxc2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc2986.pfb .
ln -s %{_fontdir}/grxc2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc3583.pfb .
ln -s %{_fontdir}/grxc3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi0500.pfb .
ln -s %{_fontdir}/grxi0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi0600.pfb .
ln -s %{_fontdir}/grxi0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi0700.pfb .
ln -s %{_fontdir}/grxi0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi0800.pfb .
ln -s %{_fontdir}/grxi0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi0900.pfb .
ln -s %{_fontdir}/grxi0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi1000.pfb .
ln -s %{_fontdir}/grxi1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi1095.pfb .
ln -s %{_fontdir}/grxi1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi1200.pfb .
ln -s %{_fontdir}/grxi1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi1440.pfb .
ln -s %{_fontdir}/grxi1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi1728.pfb .
ln -s %{_fontdir}/grxi1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi2074.pfb .
ln -s %{_fontdir}/grxi2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi2488.pfb .
ln -s %{_fontdir}/grxi2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi2986.pfb .
ln -s %{_fontdir}/grxi2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi3583.pfb .
ln -s %{_fontdir}/grxi3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl0500.pfb .
ln -s %{_fontdir}/grxl0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl0600.pfb .
ln -s %{_fontdir}/grxl0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl0700.pfb .
ln -s %{_fontdir}/grxl0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl0800.pfb .
ln -s %{_fontdir}/grxl0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl0900.pfb .
ln -s %{_fontdir}/grxl0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl1000.pfb .
ln -s %{_fontdir}/grxl1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl1095.pfb .
ln -s %{_fontdir}/grxl1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl1200.pfb .
ln -s %{_fontdir}/grxl1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl1440.pfb .
ln -s %{_fontdir}/grxl1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl1728.pfb .
ln -s %{_fontdir}/grxl1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl2074.pfb .
ln -s %{_fontdir}/grxl2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl2488.pfb .
ln -s %{_fontdir}/grxl2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl2986.pfb .
ln -s %{_fontdir}/grxl2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl3583.pfb .
ln -s %{_fontdir}/grxl3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn0500.pfb .
ln -s %{_fontdir}/grxn0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn0600.pfb .
ln -s %{_fontdir}/grxn0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn0700.pfb .
ln -s %{_fontdir}/grxn0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn0800.pfb .
ln -s %{_fontdir}/grxn0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn0900.pfb .
ln -s %{_fontdir}/grxn0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn1000.pfb .
ln -s %{_fontdir}/grxn1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn1095.pfb .
ln -s %{_fontdir}/grxn1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn1200.pfb .
ln -s %{_fontdir}/grxn1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn1440.pfb .
ln -s %{_fontdir}/grxn1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn1728.pfb .
ln -s %{_fontdir}/grxn1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn2074.pfb .
ln -s %{_fontdir}/grxn2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn2488.pfb .
ln -s %{_fontdir}/grxn2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn2986.pfb .
ln -s %{_fontdir}/grxn2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn3583.pfb .
ln -s %{_fontdir}/grxn3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo0500.pfb .
ln -s %{_fontdir}/grxo0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo0600.pfb .
ln -s %{_fontdir}/grxo0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo0700.pfb .
ln -s %{_fontdir}/grxo0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo0800.pfb .
ln -s %{_fontdir}/grxo0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo0900.pfb .
ln -s %{_fontdir}/grxo0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo1000.pfb .
ln -s %{_fontdir}/grxo1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo1095.pfb .
ln -s %{_fontdir}/grxo1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo1200.pfb .
ln -s %{_fontdir}/grxo1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo1440.pfb .
ln -s %{_fontdir}/grxo1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo1728.pfb .
ln -s %{_fontdir}/grxo1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo2074.pfb .
ln -s %{_fontdir}/grxo2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo2488.pfb .
ln -s %{_fontdir}/grxo2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo2986.pfb .
ln -s %{_fontdir}/grxo2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo3583.pfb .
ln -s %{_fontdir}/grxo3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu0500.pfb .
ln -s %{_fontdir}/grxu0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu0600.pfb .
ln -s %{_fontdir}/grxu0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu0700.pfb .
ln -s %{_fontdir}/grxu0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu0800.pfb .
ln -s %{_fontdir}/grxu0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu0900.pfb .
ln -s %{_fontdir}/grxu0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu1000.pfb .
ln -s %{_fontdir}/grxu1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu1095.pfb .
ln -s %{_fontdir}/grxu1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu1200.pfb .
ln -s %{_fontdir}/grxu1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu1440.pfb .
ln -s %{_fontdir}/grxu1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu1728.pfb .
ln -s %{_fontdir}/grxu1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu2074.pfb .
ln -s %{_fontdir}/grxu2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu2488.pfb .
ln -s %{_fontdir}/grxu2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu2986.pfb .
ln -s %{_fontdir}/grxu2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu3583.pfb .
ln -s %{_fontdir}/grxu3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma0500.pfb .
ln -s %{_fontdir}/gsma0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma0600.pfb .
ln -s %{_fontdir}/gsma0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma0700.pfb .
ln -s %{_fontdir}/gsma0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma0800.pfb .
ln -s %{_fontdir}/gsma0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma0900.pfb .
ln -s %{_fontdir}/gsma0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma1000.pfb .
ln -s %{_fontdir}/gsma1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma1095.pfb .
ln -s %{_fontdir}/gsma1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma1200.pfb .
ln -s %{_fontdir}/gsma1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma1440.pfb .
ln -s %{_fontdir}/gsma1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma1728.pfb .
ln -s %{_fontdir}/gsma1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma2074.pfb .
ln -s %{_fontdir}/gsma2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma2488.pfb .
ln -s %{_fontdir}/gsma2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma2986.pfb .
ln -s %{_fontdir}/gsma2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma3583.pfb .
ln -s %{_fontdir}/gsma3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc0500.pfb .
ln -s %{_fontdir}/gsmc0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc0600.pfb .
ln -s %{_fontdir}/gsmc0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc0700.pfb .
ln -s %{_fontdir}/gsmc0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc0800.pfb .
ln -s %{_fontdir}/gsmc0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc0900.pfb .
ln -s %{_fontdir}/gsmc0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc1000.pfb .
ln -s %{_fontdir}/gsmc1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc1095.pfb .
ln -s %{_fontdir}/gsmc1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc1200.pfb .
ln -s %{_fontdir}/gsmc1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc1440.pfb .
ln -s %{_fontdir}/gsmc1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc1728.pfb .
ln -s %{_fontdir}/gsmc1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc2074.pfb .
ln -s %{_fontdir}/gsmc2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc2488.pfb .
ln -s %{_fontdir}/gsmc2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc2986.pfb .
ln -s %{_fontdir}/gsmc2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc3583.pfb .
ln -s %{_fontdir}/gsmc3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme0500.pfb .
ln -s %{_fontdir}/gsme0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme0600.pfb .
ln -s %{_fontdir}/gsme0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme0700.pfb .
ln -s %{_fontdir}/gsme0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme0800.pfb .
ln -s %{_fontdir}/gsme0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme0900.pfb .
ln -s %{_fontdir}/gsme0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme1000.pfb .
ln -s %{_fontdir}/gsme1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme1095.pfb .
ln -s %{_fontdir}/gsme1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme1200.pfb .
ln -s %{_fontdir}/gsme1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme1440.pfb .
ln -s %{_fontdir}/gsme1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme1728.pfb .
ln -s %{_fontdir}/gsme1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme2074.pfb .
ln -s %{_fontdir}/gsme2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme2488.pfb .
ln -s %{_fontdir}/gsme2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme2986.pfb .
ln -s %{_fontdir}/gsme2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme3583.pfb .
ln -s %{_fontdir}/gsme3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi0500.pfb .
ln -s %{_fontdir}/gsmi0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi0600.pfb .
ln -s %{_fontdir}/gsmi0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi0700.pfb .
ln -s %{_fontdir}/gsmi0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi0800.pfb .
ln -s %{_fontdir}/gsmi0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi0900.pfb .
ln -s %{_fontdir}/gsmi0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi1000.pfb .
ln -s %{_fontdir}/gsmi1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi1095.pfb .
ln -s %{_fontdir}/gsmi1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi1200.pfb .
ln -s %{_fontdir}/gsmi1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi1440.pfb .
ln -s %{_fontdir}/gsmi1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi1728.pfb .
ln -s %{_fontdir}/gsmi1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi2074.pfb .
ln -s %{_fontdir}/gsmi2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi2488.pfb .
ln -s %{_fontdir}/gsmi2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi2986.pfb .
ln -s %{_fontdir}/gsmi2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi3583.pfb .
ln -s %{_fontdir}/gsmi3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn0500.pfb .
ln -s %{_fontdir}/gsmn0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn0600.pfb .
ln -s %{_fontdir}/gsmn0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn0700.pfb .
ln -s %{_fontdir}/gsmn0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn0800.pfb .
ln -s %{_fontdir}/gsmn0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn0900.pfb .
ln -s %{_fontdir}/gsmn0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn1000.pfb .
ln -s %{_fontdir}/gsmn1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn1095.pfb .
ln -s %{_fontdir}/gsmn1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn1200.pfb .
ln -s %{_fontdir}/gsmn1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn1440.pfb .
ln -s %{_fontdir}/gsmn1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn1728.pfb .
ln -s %{_fontdir}/gsmn1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn2074.pfb .
ln -s %{_fontdir}/gsmn2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn2488.pfb .
ln -s %{_fontdir}/gsmn2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn2986.pfb .
ln -s %{_fontdir}/gsmn2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn3583.pfb .
ln -s %{_fontdir}/gsmn3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo0500.pfb .
ln -s %{_fontdir}/gsmo0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo0600.pfb .
ln -s %{_fontdir}/gsmo0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo0700.pfb .
ln -s %{_fontdir}/gsmo0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo0800.pfb .
ln -s %{_fontdir}/gsmo0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo0900.pfb .
ln -s %{_fontdir}/gsmo0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo1000.pfb .
ln -s %{_fontdir}/gsmo1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo1095.pfb .
ln -s %{_fontdir}/gsmo1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo1200.pfb .
ln -s %{_fontdir}/gsmo1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo1440.pfb .
ln -s %{_fontdir}/gsmo1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo1728.pfb .
ln -s %{_fontdir}/gsmo1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo2074.pfb .
ln -s %{_fontdir}/gsmo2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo2488.pfb .
ln -s %{_fontdir}/gsmo2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo2986.pfb .
ln -s %{_fontdir}/gsmo2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo3583.pfb .
ln -s %{_fontdir}/gsmo3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu0500.pfb .
ln -s %{_fontdir}/gsmu0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu0600.pfb .
ln -s %{_fontdir}/gsmu0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu0700.pfb .
ln -s %{_fontdir}/gsmu0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu0800.pfb .
ln -s %{_fontdir}/gsmu0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu0900.pfb .
ln -s %{_fontdir}/gsmu0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu1000.pfb .
ln -s %{_fontdir}/gsmu1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu1095.pfb .
ln -s %{_fontdir}/gsmu1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu1200.pfb .
ln -s %{_fontdir}/gsmu1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu1440.pfb .
ln -s %{_fontdir}/gsmu1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu1728.pfb .
ln -s %{_fontdir}/gsmu1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu2074.pfb .
ln -s %{_fontdir}/gsmu2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu2488.pfb .
ln -s %{_fontdir}/gsmu2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu2986.pfb .
ln -s %{_fontdir}/gsmu2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu3583.pfb .
ln -s %{_fontdir}/gsmu3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa0500.pfb .
ln -s %{_fontdir}/gsxa0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa0600.pfb .
ln -s %{_fontdir}/gsxa0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa0700.pfb .
ln -s %{_fontdir}/gsxa0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa0800.pfb .
ln -s %{_fontdir}/gsxa0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa0900.pfb .
ln -s %{_fontdir}/gsxa0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa1000.pfb .
ln -s %{_fontdir}/gsxa1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa1095.pfb .
ln -s %{_fontdir}/gsxa1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa1200.pfb .
ln -s %{_fontdir}/gsxa1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa1440.pfb .
ln -s %{_fontdir}/gsxa1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa1728.pfb .
ln -s %{_fontdir}/gsxa1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa2074.pfb .
ln -s %{_fontdir}/gsxa2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa2488.pfb .
ln -s %{_fontdir}/gsxa2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa2986.pfb .
ln -s %{_fontdir}/gsxa2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa3583.pfb .
ln -s %{_fontdir}/gsxa3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc0500.pfb .
ln -s %{_fontdir}/gsxc0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc0600.pfb .
ln -s %{_fontdir}/gsxc0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc0700.pfb .
ln -s %{_fontdir}/gsxc0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc0800.pfb .
ln -s %{_fontdir}/gsxc0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc0900.pfb .
ln -s %{_fontdir}/gsxc0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc1000.pfb .
ln -s %{_fontdir}/gsxc1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc1095.pfb .
ln -s %{_fontdir}/gsxc1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc1200.pfb .
ln -s %{_fontdir}/gsxc1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc1440.pfb .
ln -s %{_fontdir}/gsxc1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc1728.pfb .
ln -s %{_fontdir}/gsxc1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc2074.pfb .
ln -s %{_fontdir}/gsxc2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc2488.pfb .
ln -s %{_fontdir}/gsxc2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc2986.pfb .
ln -s %{_fontdir}/gsxc2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc3583.pfb .
ln -s %{_fontdir}/gsxc3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe0500.pfb .
ln -s %{_fontdir}/gsxe0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe0600.pfb .
ln -s %{_fontdir}/gsxe0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe0700.pfb .
ln -s %{_fontdir}/gsxe0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe0800.pfb .
ln -s %{_fontdir}/gsxe0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe0900.pfb .
ln -s %{_fontdir}/gsxe0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe1000.pfb .
ln -s %{_fontdir}/gsxe1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe1095.pfb .
ln -s %{_fontdir}/gsxe1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe1200.pfb .
ln -s %{_fontdir}/gsxe1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe1440.pfb .
ln -s %{_fontdir}/gsxe1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe1728.pfb .
ln -s %{_fontdir}/gsxe1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe2074.pfb .
ln -s %{_fontdir}/gsxe2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe2488.pfb .
ln -s %{_fontdir}/gsxe2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe2986.pfb .
ln -s %{_fontdir}/gsxe2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe3583.pfb .
ln -s %{_fontdir}/gsxe3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi0500.pfb .
ln -s %{_fontdir}/gsxi0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi0600.pfb .
ln -s %{_fontdir}/gsxi0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi0700.pfb .
ln -s %{_fontdir}/gsxi0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi0800.pfb .
ln -s %{_fontdir}/gsxi0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi0900.pfb .
ln -s %{_fontdir}/gsxi0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi1000.pfb .
ln -s %{_fontdir}/gsxi1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi1095.pfb .
ln -s %{_fontdir}/gsxi1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi1200.pfb .
ln -s %{_fontdir}/gsxi1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi1440.pfb .
ln -s %{_fontdir}/gsxi1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi1728.pfb .
ln -s %{_fontdir}/gsxi1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi2074.pfb .
ln -s %{_fontdir}/gsxi2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi2488.pfb .
ln -s %{_fontdir}/gsxi2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi2986.pfb .
ln -s %{_fontdir}/gsxi2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi3583.pfb .
ln -s %{_fontdir}/gsxi3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn0500.pfb .
ln -s %{_fontdir}/gsxn0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn0600.pfb .
ln -s %{_fontdir}/gsxn0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn0700.pfb .
ln -s %{_fontdir}/gsxn0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn0800.pfb .
ln -s %{_fontdir}/gsxn0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn0900.pfb .
ln -s %{_fontdir}/gsxn0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn1000.pfb .
ln -s %{_fontdir}/gsxn1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn1095.pfb .
ln -s %{_fontdir}/gsxn1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn1200.pfb .
ln -s %{_fontdir}/gsxn1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn1440.pfb .
ln -s %{_fontdir}/gsxn1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn1728.pfb .
ln -s %{_fontdir}/gsxn1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn2074.pfb .
ln -s %{_fontdir}/gsxn2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn2488.pfb .
ln -s %{_fontdir}/gsxn2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn2986.pfb .
ln -s %{_fontdir}/gsxn2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn3583.pfb .
ln -s %{_fontdir}/gsxn3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo0500.pfb .
ln -s %{_fontdir}/gsxo0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo0600.pfb .
ln -s %{_fontdir}/gsxo0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo0700.pfb .
ln -s %{_fontdir}/gsxo0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo0800.pfb .
ln -s %{_fontdir}/gsxo0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo0900.pfb .
ln -s %{_fontdir}/gsxo0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo1000.pfb .
ln -s %{_fontdir}/gsxo1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo1095.pfb .
ln -s %{_fontdir}/gsxo1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo1200.pfb .
ln -s %{_fontdir}/gsxo1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo1440.pfb .
ln -s %{_fontdir}/gsxo1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo1728.pfb .
ln -s %{_fontdir}/gsxo1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo2074.pfb .
ln -s %{_fontdir}/gsxo2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo2488.pfb .
ln -s %{_fontdir}/gsxo2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo2986.pfb .
ln -s %{_fontdir}/gsxo2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo3583.pfb .
ln -s %{_fontdir}/gsxo3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu0500.pfb .
ln -s %{_fontdir}/gsxu0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu0600.pfb .
ln -s %{_fontdir}/gsxu0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu0700.pfb .
ln -s %{_fontdir}/gsxu0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu0800.pfb .
ln -s %{_fontdir}/gsxu0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu0900.pfb .
ln -s %{_fontdir}/gsxu0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu1000.pfb .
ln -s %{_fontdir}/gsxu1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu1095.pfb .
ln -s %{_fontdir}/gsxu1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu1200.pfb .
ln -s %{_fontdir}/gsxu1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu1440.pfb .
ln -s %{_fontdir}/gsxu1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu1728.pfb .
ln -s %{_fontdir}/gsxu1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu2074.pfb .
ln -s %{_fontdir}/gsxu2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu2488.pfb .
ln -s %{_fontdir}/gsxu2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu2986.pfb .
ln -s %{_fontdir}/gsxu2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu3583.pfb .
ln -s %{_fontdir}/gsxu3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc0500.pfb .
ln -s %{_fontdir}/gttc0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc0600.pfb .
ln -s %{_fontdir}/gttc0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc0700.pfb .
ln -s %{_fontdir}/gttc0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc0800.pfb .
ln -s %{_fontdir}/gttc0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc0900.pfb .
ln -s %{_fontdir}/gttc0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc1000.pfb .
ln -s %{_fontdir}/gttc1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc1095.pfb .
ln -s %{_fontdir}/gttc1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc1200.pfb .
ln -s %{_fontdir}/gttc1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc1440.pfb .
ln -s %{_fontdir}/gttc1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc1728.pfb .
ln -s %{_fontdir}/gttc1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc2074.pfb .
ln -s %{_fontdir}/gttc2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc2488.pfb .
ln -s %{_fontdir}/gttc2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc2986.pfb .
ln -s %{_fontdir}/gttc2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc3583.pfb .
ln -s %{_fontdir}/gttc3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti0500.pfb .
ln -s %{_fontdir}/gtti0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti0600.pfb .
ln -s %{_fontdir}/gtti0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti0700.pfb .
ln -s %{_fontdir}/gtti0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti0800.pfb .
ln -s %{_fontdir}/gtti0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti0900.pfb .
ln -s %{_fontdir}/gtti0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti1000.pfb .
ln -s %{_fontdir}/gtti1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti1095.pfb .
ln -s %{_fontdir}/gtti1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti1200.pfb .
ln -s %{_fontdir}/gtti1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti1440.pfb .
ln -s %{_fontdir}/gtti1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti1728.pfb .
ln -s %{_fontdir}/gtti1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti2074.pfb .
ln -s %{_fontdir}/gtti2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti2488.pfb .
ln -s %{_fontdir}/gtti2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti2986.pfb .
ln -s %{_fontdir}/gtti2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti3583.pfb .
ln -s %{_fontdir}/gtti3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn0500.pfb .
ln -s %{_fontdir}/gttn0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn0600.pfb .
ln -s %{_fontdir}/gttn0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn0700.pfb .
ln -s %{_fontdir}/gttn0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn0800.pfb .
ln -s %{_fontdir}/gttn0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn0900.pfb .
ln -s %{_fontdir}/gttn0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn1000.pfb .
ln -s %{_fontdir}/gttn1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn1095.pfb .
ln -s %{_fontdir}/gttn1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn1200.pfb .
ln -s %{_fontdir}/gttn1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn1440.pfb .
ln -s %{_fontdir}/gttn1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn1728.pfb .
ln -s %{_fontdir}/gttn1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn2074.pfb .
ln -s %{_fontdir}/gttn2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn2488.pfb .
ln -s %{_fontdir}/gttn2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn2986.pfb .
ln -s %{_fontdir}/gttn2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn3583.pfb .
ln -s %{_fontdir}/gttn3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto0500.pfb .
ln -s %{_fontdir}/gtto0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto0600.pfb .
ln -s %{_fontdir}/gtto0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto0700.pfb .
ln -s %{_fontdir}/gtto0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto0800.pfb .
ln -s %{_fontdir}/gtto0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto0900.pfb .
ln -s %{_fontdir}/gtto0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto1000.pfb .
ln -s %{_fontdir}/gtto1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto1095.pfb .
ln -s %{_fontdir}/gtto1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto1200.pfb .
ln -s %{_fontdir}/gtto1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto1440.pfb .
ln -s %{_fontdir}/gtto1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto1728.pfb .
ln -s %{_fontdir}/gtto1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto2074.pfb .
ln -s %{_fontdir}/gtto2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto2488.pfb .
ln -s %{_fontdir}/gtto2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto2986.pfb .
ln -s %{_fontdir}/gtto2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto3583.pfb .
ln -s %{_fontdir}/gtto3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto3583.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu0500.pfb .
ln -s %{_fontdir}/gttu0500.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu0500.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu0600.pfb .
ln -s %{_fontdir}/gttu0600.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu0600.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu0700.pfb .
ln -s %{_fontdir}/gttu0700.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu0700.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu0800.pfb .
ln -s %{_fontdir}/gttu0800.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu0800.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu0900.pfb .
ln -s %{_fontdir}/gttu0900.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu0900.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu1000.pfb .
ln -s %{_fontdir}/gttu1000.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu1000.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu1095.pfb .
ln -s %{_fontdir}/gttu1095.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu1095.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu1200.pfb .
ln -s %{_fontdir}/gttu1200.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu1200.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu1440.pfb .
ln -s %{_fontdir}/gttu1440.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu1440.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu1728.pfb .
ln -s %{_fontdir}/gttu1728.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu1728.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu2074.pfb .
ln -s %{_fontdir}/gttu2074.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu2074.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu2488.pfb .
ln -s %{_fontdir}/gttu2488.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu2488.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu2986.pfb .
ln -s %{_fontdir}/gttu2986.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu2986.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu3583.pfb .
ln -s %{_fontdir}/gttu3583.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu3583.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/cbfonts/CB.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cbfonts/gmtr.enc
%{_texdir}/texmf-dist/fonts/map/dvips/cbfonts/cbgreek-full.map
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/cbaccent.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/cbbase.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/cbdigits.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/cbgreek.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/cblig.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/cbligit.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/cbligrm.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/cbligsc.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/cbligtt.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/cblower.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/cbmetre.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/cbpunct.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/cbspline.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/cbupper.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glic.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glic0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glic0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glic1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glic1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glic1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glic1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glic1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glic2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glic2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glic3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glic4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glii.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glii0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glii0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glii1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glii1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glii1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glii1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glii1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glii2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glii2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glii3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glii4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glin.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glin0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glin0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glin1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glin1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glin1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glin1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glin1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glin2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glin2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glin3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glin4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glio.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glio0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glio0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glio1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glio1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glio1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glio1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glio1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glio2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glio2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glio3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glio4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gliu.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gliu0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gliu0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gliu1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gliu1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gliu1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gliu1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gliu1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gliu2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gliu2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gliu3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gliu4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljc.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljc0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljc0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljc1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljc1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljc1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljc1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljc1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljc2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljc2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljc3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljc4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljn.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljn0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljn0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljn1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljn1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljn1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljn1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljn1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljn2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljn2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljn3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljn4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljo.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljo0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljo0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljo1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljo1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljo1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljo1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljo1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljo2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljo2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljo3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gljo4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmc.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmc0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmc0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmc1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmc1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmc1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmc1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmc1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmc2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmc2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmc3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmc4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmi.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmi0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmi0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmi1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmi1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmi1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmi1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmi1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmi2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmi2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmi3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmi4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmn.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmn0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmn0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmn1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmn1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmn1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmn1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmn1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmn2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmn2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmn3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmn4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmo.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmo0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmo0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmo1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmo1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmo1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmo1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmo1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmo2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmo2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmo3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmo4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmu.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmu0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmu0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmu1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmu1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmu1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmu1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmu1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmu2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmu2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmu3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glmu4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gltc.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gltc0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gltc0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gltc1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gltc1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gltc1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gltc1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gltc1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gltc2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gltc2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gltc3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gltc4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gltn.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gltn0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gltn0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gltn1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gltn1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gltn1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gltn1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gltn1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gltn2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gltn2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gltn3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gltn4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glto.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glto0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glto0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glto1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glto1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glto1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glto1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glto1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glto2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glto2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glto3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glto4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwc.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwc0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwc0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwc1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwc1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwc1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwc1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwc1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwc2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwc2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwc3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwc4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwi.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwi0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwi0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwi1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwi1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwi1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwi1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwi1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwi2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwi2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwi3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwi4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwn.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwn0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwn0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwn1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwn1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwn1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwn1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwn1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwn2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwn2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwn3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwn4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwo.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwo0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwo0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwo1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwo1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwo1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwo1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwo1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwo2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwo2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwo3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwo4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwu.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwu0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwu0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwu1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwu1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwu1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwu1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwu1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwu2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwu2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwu3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glwu4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxc.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxc0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxc0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxc1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxc1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxc1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxc1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxc1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxc2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxc2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxc3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxc4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxi.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxi0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxi0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxi1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxi1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxi1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxi1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxi1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxi2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxi2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxi3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxi4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxn.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxn0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxn0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxn1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxn1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxn1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxn1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxn1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxn2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxn2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxn3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxn4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxo.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxo0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxo0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxo1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxo1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxo1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxo1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxo1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxo2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxo2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxo3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxo4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxu.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxu0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxu0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxu1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxu1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxu1382.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxu1659.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxu1991.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxu2389.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxu2866.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxu3440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/glxu4128.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmn.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmn0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmn0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmn0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmn0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmn0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmn1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmn1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmn1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmn1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmn1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmn2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmn2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmn2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmn3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmo.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmo0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmo0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmo0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmo0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmo0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmo1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmo1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmo1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmo1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmo1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmo2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmo2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmo2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmmo3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmtr.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmtr0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmtr0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmtr0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmtr0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmtr0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmtr1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmtr1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmtr1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmtr1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmtr1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmtr2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmtr2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmtr2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmtr3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxn.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxn0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxn0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxn0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxn0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxn0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxn1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxn1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxn1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxn1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxn1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxn2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxn2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxn2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxn3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxo.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxo0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxo0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxo0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxo0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxo0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxo1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxo1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxo1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxo1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxo1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxo2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxo2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxo2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gmxo3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomc.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomc0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomc0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomc0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomc0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomc0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomc1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomc1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomc1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomc1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomc1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomc2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomc2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomc2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomc3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomi.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomi0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomi0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomi0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomi0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomi0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomi1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomi1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomi1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomi1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomi1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomi2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomi2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomi2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomi3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomn.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomn0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomn0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomn0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomn0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomn0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomn1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomn1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomn1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomn1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomn1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomn2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomn2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomn2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomn3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomo.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomo0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomo0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomo0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomo0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomo0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomo1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomo1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomo1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomo1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomo1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomo2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomo2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomo2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomo3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomu.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomu0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomu0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomu0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomu0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomu0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomu1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomu1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomu1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomu1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomu1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomu2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomu2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomu2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gomu3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxc.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxc0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxc0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxc0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxc0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxc0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxc1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxc1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxc1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxc1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxc1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxc2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxc2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxc2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxc3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxi.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxi0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxi0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxi0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxi0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxi0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxi1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxi1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxi1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxi1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxi1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxi2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxi2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxi2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxi3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxn.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxn0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxn0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxn0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxn0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxn0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxn1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxn1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxn1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxn1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxn1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxn2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxn2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxn2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxn3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxo.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxo0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxo0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxo0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxo0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxo0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxo1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxo1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxo1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxo1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxo1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxo2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxo2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxo2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxo3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxu.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxu0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxu0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxu0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxu0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxu0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxu1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxu1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxu1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxu1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxu1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxu2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxu2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxu2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/goxu3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grbl.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grbl0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grbl0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grbl0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grbl0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grbl0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grbl1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grbl1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grbl1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grbl1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grbl1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grbl2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grbl2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grbl2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grbl3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmc.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmc0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmc0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmc0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmc0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmc0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmc1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmc1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmc1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmc1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmc1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmc2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmc2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmc2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmc3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmi.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmi0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmi0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmi0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmi0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmi0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmi1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmi1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmi1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmi1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmi1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmi2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmi2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmi2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmi3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grml.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grml0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grml0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grml0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grml0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grml0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grml1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grml1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grml1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grml1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grml1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grml2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grml2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grml2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grml3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmn.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmn0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmn0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmn0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmn0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmn0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmn1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmn1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmn1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmn1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmn1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmn2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmn2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmn2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmn3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmo.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmo0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmo0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmo0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmo0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmo0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmo1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmo1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmo1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmo1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmo1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmo2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmo2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmo2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmo3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmu.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmu0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmu0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmu0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmu0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmu0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmu1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmu1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmu1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmu1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmu1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmu2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmu2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmu2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grmu3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxc.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxc0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxc0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxc0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxc0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxc0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxc1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxc1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxc1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxc1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxc1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxc2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxc2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxc2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxc3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxi.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxi0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxi0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxi0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxi0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxi0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxi1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxi1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxi1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxi1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxi1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxi2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxi2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxi2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxi3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxl.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxl0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxl0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxl0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxl0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxl0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxl1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxl1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxl1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxl1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxl1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxl2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxl2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxl2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxl3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxn.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxn0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxn0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxn0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxn0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxn0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxn1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxn1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxn1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxn1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxn1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxn2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxn2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxn2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxn3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxo.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxo0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxo0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxo0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxo0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxo0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxo1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxo1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxo1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxo1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxo1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxo2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxo2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxo2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxo3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxu.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxu0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxu0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxu0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxu0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxu0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxu1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxu1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxu1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxu1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxu1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxu2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxu2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxu2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/grxu3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsma.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsma0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsma0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsma0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsma0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsma0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsma1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsma1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsma1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsma1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsma1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsma2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsma2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsma2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsma3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmc.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmc0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmc0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmc0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmc0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmc0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmc1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmc1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmc1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmc1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmc1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmc2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmc2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmc2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmc3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsme.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsme0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsme0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsme0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsme0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsme0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsme1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsme1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsme1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsme1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsme1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsme2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsme2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsme2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsme3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmi.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmi0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmi0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmi0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmi0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmi0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmi1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmi1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmi1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmi1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmi1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmi2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmi2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmi2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmi3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmn.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmn0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmn0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmn0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmn0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmn0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmn1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmn1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmn1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmn1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmn1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmn2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmn2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmn2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmn3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmo.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmo0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmo0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmo0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmo0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmo0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmo1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmo1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmo1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmo1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmo1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmo2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmo2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmo2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmo3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmu.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmu0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmu0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmu0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmu0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmu0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmu1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmu1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmu1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmu1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmu1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmu2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmu2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmu2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsmu3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxa.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxa0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxa0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxa0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxa0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxa0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxa1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxa1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxa1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxa1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxa1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxa2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxa2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxa2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxa3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxc.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxc0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxc0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxc0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxc0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxc0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxc1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxc1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxc1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxc1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxc1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxc2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxc2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxc2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxc3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxe.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxe0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxe0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxe0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxe0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxe0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxe1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxe1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxe1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxe1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxe1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxe2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxe2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxe2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxe3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxi.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxi0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxi0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxi0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxi0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxi0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxi1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxi1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxi1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxi1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxi1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxi2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxi2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxi2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxi3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxn.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxn0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxn0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxn0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxn0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxn0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxn1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxn1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxn1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxn1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxn1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxn2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxn2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxn2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxn3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxo.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxo0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxo0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxo0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxo0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxo0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxo1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxo1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxo1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxo1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxo1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxo2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxo2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxo2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxo3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxu.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxu0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxu0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxu0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxu0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxu0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxu1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxu1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxu1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxu1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxu1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxu2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxu2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxu2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gsxu3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttc.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttc0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttc0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttc0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttc0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttc0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttc1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttc1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttc1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttc1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttc1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttc2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttc2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttc2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttc3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtti.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtti0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtti0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtti0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtti0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtti0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtti1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtti1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtti1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtti1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtti1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtti2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtti2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtti2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtti3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttn.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttn0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttn0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttn0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttn0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttn0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttn1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttn1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttn1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttn1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttn1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttn2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttn2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttn2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttn3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtto.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtto0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtto0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtto0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtto0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtto0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtto1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtto1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtto1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtto1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtto1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtto2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtto2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtto2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gtto3583.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttu.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttu0500.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttu0600.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttu0700.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttu0800.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttu0900.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttu1000.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttu1095.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttu1200.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttu1440.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttu1728.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttu2074.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttu2488.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttu2986.mf
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/gttu3583.mf
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glic0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glic0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glic1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glic1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glic1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glic1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glic1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glic2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glic2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glic3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glic4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glii0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glii0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glii1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glii1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glii1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glii1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glii1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glii2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glii2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glii3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glii4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glin0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glin0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glin1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glin1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glin1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glin1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glin1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glin2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glin2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glin3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glin4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glio0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glio0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glio1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glio1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glio1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glio1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glio1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glio2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glio2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glio3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glio4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gliu0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gliu0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gliu1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gliu1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gliu1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gliu1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gliu1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gliu2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gliu2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gliu3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gliu4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljc0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljc0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljc1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljc1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljc1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljc1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljc1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljc2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljc2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljc3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljc4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljn0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljn0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljn1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljn1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljn1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljn1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljn1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljn2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljn2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljn3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljn4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljo0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljo0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljo1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljo1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljo1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljo1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljo1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljo2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljo2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljo3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gljo4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmc0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmc0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmc1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmc1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmc1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmc1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmc1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmc2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmc2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmc3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmc4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmi0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmi0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmi1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmi1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmi1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmi1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmi1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmi2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmi2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmi3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmi4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmn0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmn0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmn1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmn1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmn1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmn1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmn1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmn2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmn2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmn3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmn4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmo0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmo0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmo1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmo1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmo1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmo1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmo1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmo2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmo2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmo3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmo4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmu0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmu0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmu1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmu1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmu1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmu1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmu1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmu2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmu2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmu3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glmu4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gltc0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gltc0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gltc1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gltc1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gltc1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gltc1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gltc1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gltc2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gltc2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gltc3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gltc4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gltn0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gltn0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gltn1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gltn1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gltn1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gltn1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gltn1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gltn2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gltn2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gltn3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gltn4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glto0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glto0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glto1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glto1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glto1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glto1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glto1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glto2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glto2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glto3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glto4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwc0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwc0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwc1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwc1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwc1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwc1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwc1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwc2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwc2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwc3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwc4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwi0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwi0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwi1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwi1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwi1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwi1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwi1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwi2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwi2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwi3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwi4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwn0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwn0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwn1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwn1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwn1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwn1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwn1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwn2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwn2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwn3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwn4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwo0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwo0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwo1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwo1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwo1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwo1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwo1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwo2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwo2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwo3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwo4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwu0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwu0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwu1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwu1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwu1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwu1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwu1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwu2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwu2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwu3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glwu4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxc0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxc0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxc1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxc1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxc1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxc1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxc1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxc2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxc2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxc3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxc4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxi0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxi0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxi1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxi1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxi1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxi1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxi1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxi2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxi2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxi3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxi4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxn0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxn0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxn1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxn1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxn1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxn1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxn1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxn2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxn2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxn3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxn4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxo0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxo0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxo1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxo1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxo1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxo1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxo1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxo2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxo2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxo3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxo4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxu0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxu0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxu1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxu1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxu1382.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxu1659.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxu1991.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxu2389.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxu2866.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxu3440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/glxu4128.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmn0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmn0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmn0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmn0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmn0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmn1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmn1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmn1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmn1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmn1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmn2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmn2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmn2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmn3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmo0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmo0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmo0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmo0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmo0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmo1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmo1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmo1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmo1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmo1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmo2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmo2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmo2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmmo3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmtr0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmtr0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmtr0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmtr0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmtr0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmtr1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmtr1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmtr1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmtr1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmtr1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmtr2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmtr2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmtr2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmtr3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxn0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxn0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxn0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxn0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxn0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxn1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxn1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxn1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxn1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxn1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxn2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxn2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxn2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxn3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxo0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxo0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxo0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxo0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxo0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxo1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxo1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxo1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxo1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxo1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxo2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxo2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxo2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gmxo3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomc0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomc0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomc0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomc0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomc0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomc1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomc1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomc1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomc1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomc1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomc2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomc2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomc2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomc3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomi0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomi0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomi0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomi0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomi0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomi1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomi1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomi1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomi1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomi1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomi2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomi2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomi2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomi3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomn0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomn0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomn0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomn0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomn0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomn1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomn1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomn1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomn1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomn1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomn2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomn2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomn2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomn3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomo0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomo0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomo0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomo0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomo0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomo1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomo1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomo1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomo1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomo1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomo2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomo2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomo2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomo3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomu0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomu0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomu0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomu0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomu0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomu1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomu1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomu1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomu1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomu1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomu2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomu2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomu2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gomu3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxc0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxc0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxc0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxc0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxc0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxc1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxc1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxc1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxc1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxc1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxc2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxc2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxc2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxc3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxi0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxi0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxi0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxi0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxi0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxi1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxi1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxi1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxi1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxi1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxi2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxi2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxi2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxi3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxn0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxn0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxn0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxn0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxn0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxn1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxn1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxn1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxn1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxn1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxn2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxn2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxn2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxn3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxo0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxo0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxo0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxo0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxo0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxo1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxo1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxo1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxo1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxo1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxo2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxo2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxo2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxo3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxu0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxu0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxu0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxu0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxu0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxu1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxu1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxu1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxu1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxu1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxu2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxu2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxu2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/goxu3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grbl0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grbl0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grbl0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grbl0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grbl0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grbl1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grbl1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grbl1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grbl1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grbl1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grbl2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grbl2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grbl2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grbl3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmc0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmc0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmc0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmc0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmc0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmc1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmc1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmc1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmc1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmc1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmc2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmc2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmc2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmc3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmi0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmi0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmi0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmi0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmi0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmi1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmi1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmi1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmi1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmi1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmi2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmi2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmi2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmi3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grml0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grml0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grml0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grml0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grml0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grml1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grml1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grml1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grml1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grml1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grml2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grml2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grml2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grml3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmn0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmn0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmn0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmn0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmn0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmn1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmn1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmn1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmn1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmn1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmn2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmn2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmn2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmn3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmo0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmo0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmo0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmo0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmo0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmo1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmo1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmo1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmo1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmo1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmo2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmo2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmo2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmo3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmu0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmu0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmu0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmu0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmu0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmu1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmu1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmu1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmu1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmu1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmu2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmu2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmu2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grmu3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxc0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxc0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxc0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxc0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxc0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxc1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxc1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxc1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxc1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxc1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxc2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxc2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxc2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxc3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxi0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxi0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxi0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxi0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxi0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxi1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxi1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxi1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxi1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxi1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxi2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxi2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxi2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxi3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxl0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxl0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxl0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxl0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxl0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxl1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxl1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxl1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxl1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxl1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxl2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxl2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxl2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxl3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxn0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxn0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxn0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxn0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxn0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxn1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxn1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxn1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxn1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxn1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxn2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxn2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxn2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxn3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxo0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxo0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxo0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxo0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxo0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxo1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxo1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxo1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxo1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxo1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxo2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxo2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxo2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxo3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxu0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxu0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxu0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxu0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxu0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxu1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxu1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxu1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxu1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxu1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxu2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxu2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxu2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/grxu3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsma0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsma0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsma0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsma0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsma0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsma1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsma1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsma1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsma1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsma1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsma2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsma2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsma2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsma3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmc0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmc0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmc0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmc0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmc0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmc1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmc1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmc1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmc1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmc1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmc2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmc2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmc2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmc3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsme0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsme0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsme0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsme0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsme0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsme1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsme1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsme1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsme1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsme1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsme2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsme2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsme2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsme3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmi0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmi0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmi0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmi0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmi0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmi1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmi1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmi1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmi1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmi1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmi2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmi2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmi2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmi3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmn0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmn0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmn0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmn0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmn0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmn1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmn1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmn1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmn1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmn1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmn2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmn2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmn2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmn3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmo0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmo0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmo0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmo0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmo0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmo1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmo1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmo1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmo1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmo1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmo2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmo2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmo2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmo3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmu0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmu0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmu0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmu0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmu0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmu1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmu1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmu1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmu1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmu1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmu2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmu2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmu2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsmu3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxa0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxa0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxa0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxa0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxa0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxa1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxa1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxa1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxa1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxa1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxa2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxa2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxa2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxa3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxc0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxc0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxc0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxc0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxc0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxc1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxc1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxc1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxc1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxc1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxc2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxc2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxc2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxc3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxe0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxe0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxe0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxe0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxe0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxe1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxe1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxe1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxe1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxe1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxe2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxe2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxe2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxe3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxi0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxi0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxi0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxi0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxi0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxi1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxi1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxi1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxi1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxi1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxi2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxi2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxi2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxi3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxn0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxn0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxn0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxn0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxn0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxn1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxn1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxn1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxn1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxn1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxn2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxn2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxn2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxn3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxo0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxo0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxo0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxo0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxo0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxo1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxo1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxo1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxo1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxo1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxo2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxo2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxo2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxo3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxu0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxu0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxu0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxu0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxu0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxu1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxu1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxu1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxu1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxu1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxu2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxu2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxu2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gsxu3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttc0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttc0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttc0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttc0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttc0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttc1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttc1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttc1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttc1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttc1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttc2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttc2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttc2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttc3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtti0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtti0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtti0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtti0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtti0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtti1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtti1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtti1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtti1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtti1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtti2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtti2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtti2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtti3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttn0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttn0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttn0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttn0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttn0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttn1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttn1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttn1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttn1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttn1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttn2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttn2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttn2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttn3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtto0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtto0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtto0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtto0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtto0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtto1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtto1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtto1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtto1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtto1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtto2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtto2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtto2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gtto3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttu0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttu0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttu0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttu0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttu0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttu1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttu1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttu1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttu1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttu1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttu2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttu2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttu2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/gttu3583.tfm
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glic4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glii4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glin4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glio4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gliu4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljc4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljn4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gljo4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmc4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmi4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmn4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmo4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glmu4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltc4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gltn4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glto4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwc4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwi4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwn4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwo4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glwu4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxc4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxi4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxn4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxo4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu1382.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu1659.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu1991.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu2389.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu2866.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu3440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/glxu4128.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmn3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmmo3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmtr3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxn3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gmxo3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomc3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomi3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomn3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomo3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gomu3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxc3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxi3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxn3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxo3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/goxu3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grbl3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmc3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmi3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grml3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmn3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmo3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grmu3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxc3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxi3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxl3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxn3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxo3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/grxu3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsma3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmc3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsme3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmi3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmn3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmo3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsmu3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxa3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxc3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxe3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxi3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxn3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxo3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gsxu3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttc3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtti3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttn3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gtto3583.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu0500.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu0600.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu0700.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu0800.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu0900.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu1000.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu1095.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu1200.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu1440.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu1728.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu2074.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu2488.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu2986.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/gttu3583.pfb

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/fonts/cbfonts/README
%{_texdir}/texmf-dist/doc/fonts/cbfonts/cbgreek.pdf
%{_texdir}/texmf-dist/doc/fonts/cbfonts/cbgreek.tex
%{_texdir}/texmf-dist/doc/fonts/cbfonts/grmn1000table.pdf

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/glic0700.pfb
%{_fontdir}/glic0800.pfb
%{_fontdir}/glic1000.pfb
%{_fontdir}/glic1200.pfb
%{_fontdir}/glic1382.pfb
%{_fontdir}/glic1659.pfb
%{_fontdir}/glic1991.pfb
%{_fontdir}/glic2389.pfb
%{_fontdir}/glic2866.pfb
%{_fontdir}/glic3440.pfb
%{_fontdir}/glic4128.pfb
%{_fontdir}/glii0700.pfb
%{_fontdir}/glii0800.pfb
%{_fontdir}/glii1000.pfb
%{_fontdir}/glii1200.pfb
%{_fontdir}/glii1382.pfb
%{_fontdir}/glii1659.pfb
%{_fontdir}/glii1991.pfb
%{_fontdir}/glii2389.pfb
%{_fontdir}/glii2866.pfb
%{_fontdir}/glii3440.pfb
%{_fontdir}/glii4128.pfb
%{_fontdir}/glin0700.pfb
%{_fontdir}/glin0800.pfb
%{_fontdir}/glin1000.pfb
%{_fontdir}/glin1200.pfb
%{_fontdir}/glin1382.pfb
%{_fontdir}/glin1659.pfb
%{_fontdir}/glin1991.pfb
%{_fontdir}/glin2389.pfb
%{_fontdir}/glin2866.pfb
%{_fontdir}/glin3440.pfb
%{_fontdir}/glin4128.pfb
%{_fontdir}/glio0700.pfb
%{_fontdir}/glio0800.pfb
%{_fontdir}/glio1000.pfb
%{_fontdir}/glio1200.pfb
%{_fontdir}/glio1382.pfb
%{_fontdir}/glio1659.pfb
%{_fontdir}/glio1991.pfb
%{_fontdir}/glio2389.pfb
%{_fontdir}/glio2866.pfb
%{_fontdir}/glio3440.pfb
%{_fontdir}/glio4128.pfb
%{_fontdir}/gliu0700.pfb
%{_fontdir}/gliu0800.pfb
%{_fontdir}/gliu1000.pfb
%{_fontdir}/gliu1200.pfb
%{_fontdir}/gliu1382.pfb
%{_fontdir}/gliu1659.pfb
%{_fontdir}/gliu1991.pfb
%{_fontdir}/gliu2389.pfb
%{_fontdir}/gliu2866.pfb
%{_fontdir}/gliu3440.pfb
%{_fontdir}/gliu4128.pfb
%{_fontdir}/gljc0700.pfb
%{_fontdir}/gljc0800.pfb
%{_fontdir}/gljc1000.pfb
%{_fontdir}/gljc1200.pfb
%{_fontdir}/gljc1382.pfb
%{_fontdir}/gljc1659.pfb
%{_fontdir}/gljc1991.pfb
%{_fontdir}/gljc2389.pfb
%{_fontdir}/gljc2866.pfb
%{_fontdir}/gljc3440.pfb
%{_fontdir}/gljc4128.pfb
%{_fontdir}/gljn0700.pfb
%{_fontdir}/gljn0800.pfb
%{_fontdir}/gljn1000.pfb
%{_fontdir}/gljn1200.pfb
%{_fontdir}/gljn1382.pfb
%{_fontdir}/gljn1659.pfb
%{_fontdir}/gljn1991.pfb
%{_fontdir}/gljn2389.pfb
%{_fontdir}/gljn2866.pfb
%{_fontdir}/gljn3440.pfb
%{_fontdir}/gljn4128.pfb
%{_fontdir}/gljo0700.pfb
%{_fontdir}/gljo0800.pfb
%{_fontdir}/gljo1000.pfb
%{_fontdir}/gljo1200.pfb
%{_fontdir}/gljo1382.pfb
%{_fontdir}/gljo1659.pfb
%{_fontdir}/gljo1991.pfb
%{_fontdir}/gljo2389.pfb
%{_fontdir}/gljo2866.pfb
%{_fontdir}/gljo3440.pfb
%{_fontdir}/gljo4128.pfb
%{_fontdir}/glmc0700.pfb
%{_fontdir}/glmc0800.pfb
%{_fontdir}/glmc1000.pfb
%{_fontdir}/glmc1200.pfb
%{_fontdir}/glmc1382.pfb
%{_fontdir}/glmc1659.pfb
%{_fontdir}/glmc1991.pfb
%{_fontdir}/glmc2389.pfb
%{_fontdir}/glmc2866.pfb
%{_fontdir}/glmc3440.pfb
%{_fontdir}/glmc4128.pfb
%{_fontdir}/glmi0700.pfb
%{_fontdir}/glmi0800.pfb
%{_fontdir}/glmi1000.pfb
%{_fontdir}/glmi1200.pfb
%{_fontdir}/glmi1382.pfb
%{_fontdir}/glmi1659.pfb
%{_fontdir}/glmi1991.pfb
%{_fontdir}/glmi2389.pfb
%{_fontdir}/glmi2866.pfb
%{_fontdir}/glmi3440.pfb
%{_fontdir}/glmi4128.pfb
%{_fontdir}/glmn0700.pfb
%{_fontdir}/glmn0800.pfb
%{_fontdir}/glmn1000.pfb
%{_fontdir}/glmn1200.pfb
%{_fontdir}/glmn1382.pfb
%{_fontdir}/glmn1659.pfb
%{_fontdir}/glmn1991.pfb
%{_fontdir}/glmn2389.pfb
%{_fontdir}/glmn2866.pfb
%{_fontdir}/glmn3440.pfb
%{_fontdir}/glmn4128.pfb
%{_fontdir}/glmo0700.pfb
%{_fontdir}/glmo0800.pfb
%{_fontdir}/glmo1000.pfb
%{_fontdir}/glmo1200.pfb
%{_fontdir}/glmo1382.pfb
%{_fontdir}/glmo1659.pfb
%{_fontdir}/glmo1991.pfb
%{_fontdir}/glmo2389.pfb
%{_fontdir}/glmo2866.pfb
%{_fontdir}/glmo3440.pfb
%{_fontdir}/glmo4128.pfb
%{_fontdir}/glmu0700.pfb
%{_fontdir}/glmu0800.pfb
%{_fontdir}/glmu1000.pfb
%{_fontdir}/glmu1200.pfb
%{_fontdir}/glmu1382.pfb
%{_fontdir}/glmu1659.pfb
%{_fontdir}/glmu1991.pfb
%{_fontdir}/glmu2389.pfb
%{_fontdir}/glmu2866.pfb
%{_fontdir}/glmu3440.pfb
%{_fontdir}/glmu4128.pfb
%{_fontdir}/gltc0700.pfb
%{_fontdir}/gltc0800.pfb
%{_fontdir}/gltc1000.pfb
%{_fontdir}/gltc1200.pfb
%{_fontdir}/gltc1382.pfb
%{_fontdir}/gltc1659.pfb
%{_fontdir}/gltc1991.pfb
%{_fontdir}/gltc2389.pfb
%{_fontdir}/gltc2866.pfb
%{_fontdir}/gltc3440.pfb
%{_fontdir}/gltc4128.pfb
%{_fontdir}/gltn0700.pfb
%{_fontdir}/gltn0800.pfb
%{_fontdir}/gltn1000.pfb
%{_fontdir}/gltn1200.pfb
%{_fontdir}/gltn1382.pfb
%{_fontdir}/gltn1659.pfb
%{_fontdir}/gltn1991.pfb
%{_fontdir}/gltn2389.pfb
%{_fontdir}/gltn2866.pfb
%{_fontdir}/gltn3440.pfb
%{_fontdir}/gltn4128.pfb
%{_fontdir}/glto0700.pfb
%{_fontdir}/glto0800.pfb
%{_fontdir}/glto1000.pfb
%{_fontdir}/glto1200.pfb
%{_fontdir}/glto1382.pfb
%{_fontdir}/glto1659.pfb
%{_fontdir}/glto1991.pfb
%{_fontdir}/glto2389.pfb
%{_fontdir}/glto2866.pfb
%{_fontdir}/glto3440.pfb
%{_fontdir}/glto4128.pfb
%{_fontdir}/glwc0700.pfb
%{_fontdir}/glwc0800.pfb
%{_fontdir}/glwc1000.pfb
%{_fontdir}/glwc1200.pfb
%{_fontdir}/glwc1382.pfb
%{_fontdir}/glwc1659.pfb
%{_fontdir}/glwc1991.pfb
%{_fontdir}/glwc2389.pfb
%{_fontdir}/glwc2866.pfb
%{_fontdir}/glwc3440.pfb
%{_fontdir}/glwc4128.pfb
%{_fontdir}/glwi0700.pfb
%{_fontdir}/glwi0800.pfb
%{_fontdir}/glwi1000.pfb
%{_fontdir}/glwi1200.pfb
%{_fontdir}/glwi1382.pfb
%{_fontdir}/glwi1659.pfb
%{_fontdir}/glwi1991.pfb
%{_fontdir}/glwi2389.pfb
%{_fontdir}/glwi2866.pfb
%{_fontdir}/glwi3440.pfb
%{_fontdir}/glwi4128.pfb
%{_fontdir}/glwn0700.pfb
%{_fontdir}/glwn0800.pfb
%{_fontdir}/glwn1000.pfb
%{_fontdir}/glwn1200.pfb
%{_fontdir}/glwn1382.pfb
%{_fontdir}/glwn1659.pfb
%{_fontdir}/glwn1991.pfb
%{_fontdir}/glwn2389.pfb
%{_fontdir}/glwn2866.pfb
%{_fontdir}/glwn3440.pfb
%{_fontdir}/glwn4128.pfb
%{_fontdir}/glwo0700.pfb
%{_fontdir}/glwo0800.pfb
%{_fontdir}/glwo1000.pfb
%{_fontdir}/glwo1200.pfb
%{_fontdir}/glwo1382.pfb
%{_fontdir}/glwo1659.pfb
%{_fontdir}/glwo1991.pfb
%{_fontdir}/glwo2389.pfb
%{_fontdir}/glwo2866.pfb
%{_fontdir}/glwo3440.pfb
%{_fontdir}/glwo4128.pfb
%{_fontdir}/glwu0700.pfb
%{_fontdir}/glwu0800.pfb
%{_fontdir}/glwu1000.pfb
%{_fontdir}/glwu1200.pfb
%{_fontdir}/glwu1382.pfb
%{_fontdir}/glwu1659.pfb
%{_fontdir}/glwu1991.pfb
%{_fontdir}/glwu2389.pfb
%{_fontdir}/glwu2866.pfb
%{_fontdir}/glwu3440.pfb
%{_fontdir}/glwu4128.pfb
%{_fontdir}/glxc0700.pfb
%{_fontdir}/glxc0800.pfb
%{_fontdir}/glxc1000.pfb
%{_fontdir}/glxc1200.pfb
%{_fontdir}/glxc1382.pfb
%{_fontdir}/glxc1659.pfb
%{_fontdir}/glxc1991.pfb
%{_fontdir}/glxc2389.pfb
%{_fontdir}/glxc2866.pfb
%{_fontdir}/glxc3440.pfb
%{_fontdir}/glxc4128.pfb
%{_fontdir}/glxi0700.pfb
%{_fontdir}/glxi0800.pfb
%{_fontdir}/glxi1000.pfb
%{_fontdir}/glxi1200.pfb
%{_fontdir}/glxi1382.pfb
%{_fontdir}/glxi1659.pfb
%{_fontdir}/glxi1991.pfb
%{_fontdir}/glxi2389.pfb
%{_fontdir}/glxi2866.pfb
%{_fontdir}/glxi3440.pfb
%{_fontdir}/glxi4128.pfb
%{_fontdir}/glxn0700.pfb
%{_fontdir}/glxn0800.pfb
%{_fontdir}/glxn1000.pfb
%{_fontdir}/glxn1200.pfb
%{_fontdir}/glxn1382.pfb
%{_fontdir}/glxn1659.pfb
%{_fontdir}/glxn1991.pfb
%{_fontdir}/glxn2389.pfb
%{_fontdir}/glxn2866.pfb
%{_fontdir}/glxn3440.pfb
%{_fontdir}/glxn4128.pfb
%{_fontdir}/glxo0700.pfb
%{_fontdir}/glxo0800.pfb
%{_fontdir}/glxo1000.pfb
%{_fontdir}/glxo1200.pfb
%{_fontdir}/glxo1382.pfb
%{_fontdir}/glxo1659.pfb
%{_fontdir}/glxo1991.pfb
%{_fontdir}/glxo2389.pfb
%{_fontdir}/glxo2866.pfb
%{_fontdir}/glxo3440.pfb
%{_fontdir}/glxo4128.pfb
%{_fontdir}/glxu0700.pfb
%{_fontdir}/glxu0800.pfb
%{_fontdir}/glxu1000.pfb
%{_fontdir}/glxu1200.pfb
%{_fontdir}/glxu1382.pfb
%{_fontdir}/glxu1659.pfb
%{_fontdir}/glxu1991.pfb
%{_fontdir}/glxu2389.pfb
%{_fontdir}/glxu2866.pfb
%{_fontdir}/glxu3440.pfb
%{_fontdir}/glxu4128.pfb
%{_fontdir}/gmmn0500.pfb
%{_fontdir}/gmmn0600.pfb
%{_fontdir}/gmmn0700.pfb
%{_fontdir}/gmmn0800.pfb
%{_fontdir}/gmmn0900.pfb
%{_fontdir}/gmmn1000.pfb
%{_fontdir}/gmmn1095.pfb
%{_fontdir}/gmmn1200.pfb
%{_fontdir}/gmmn1440.pfb
%{_fontdir}/gmmn1728.pfb
%{_fontdir}/gmmn2074.pfb
%{_fontdir}/gmmn2488.pfb
%{_fontdir}/gmmn2986.pfb
%{_fontdir}/gmmn3583.pfb
%{_fontdir}/gmmo0500.pfb
%{_fontdir}/gmmo0600.pfb
%{_fontdir}/gmmo0700.pfb
%{_fontdir}/gmmo0800.pfb
%{_fontdir}/gmmo0900.pfb
%{_fontdir}/gmmo1000.pfb
%{_fontdir}/gmmo1095.pfb
%{_fontdir}/gmmo1200.pfb
%{_fontdir}/gmmo1440.pfb
%{_fontdir}/gmmo1728.pfb
%{_fontdir}/gmmo2074.pfb
%{_fontdir}/gmmo2488.pfb
%{_fontdir}/gmmo2986.pfb
%{_fontdir}/gmmo3583.pfb
%{_fontdir}/gmtr0500.pfb
%{_fontdir}/gmtr0600.pfb
%{_fontdir}/gmtr0700.pfb
%{_fontdir}/gmtr0800.pfb
%{_fontdir}/gmtr0900.pfb
%{_fontdir}/gmtr1000.pfb
%{_fontdir}/gmtr1095.pfb
%{_fontdir}/gmtr1200.pfb
%{_fontdir}/gmtr1440.pfb
%{_fontdir}/gmtr1728.pfb
%{_fontdir}/gmtr2074.pfb
%{_fontdir}/gmtr2488.pfb
%{_fontdir}/gmtr2986.pfb
%{_fontdir}/gmtr3583.pfb
%{_fontdir}/gmxn0500.pfb
%{_fontdir}/gmxn0600.pfb
%{_fontdir}/gmxn0700.pfb
%{_fontdir}/gmxn0800.pfb
%{_fontdir}/gmxn0900.pfb
%{_fontdir}/gmxn1000.pfb
%{_fontdir}/gmxn1095.pfb
%{_fontdir}/gmxn1200.pfb
%{_fontdir}/gmxn1440.pfb
%{_fontdir}/gmxn1728.pfb
%{_fontdir}/gmxn2074.pfb
%{_fontdir}/gmxn2488.pfb
%{_fontdir}/gmxn2986.pfb
%{_fontdir}/gmxn3583.pfb
%{_fontdir}/gmxo0500.pfb
%{_fontdir}/gmxo0600.pfb
%{_fontdir}/gmxo0700.pfb
%{_fontdir}/gmxo0800.pfb
%{_fontdir}/gmxo0900.pfb
%{_fontdir}/gmxo1000.pfb
%{_fontdir}/gmxo1095.pfb
%{_fontdir}/gmxo1200.pfb
%{_fontdir}/gmxo1440.pfb
%{_fontdir}/gmxo1728.pfb
%{_fontdir}/gmxo2074.pfb
%{_fontdir}/gmxo2488.pfb
%{_fontdir}/gmxo2986.pfb
%{_fontdir}/gmxo3583.pfb
%{_fontdir}/gomc0500.pfb
%{_fontdir}/gomc0600.pfb
%{_fontdir}/gomc0700.pfb
%{_fontdir}/gomc0800.pfb
%{_fontdir}/gomc0900.pfb
%{_fontdir}/gomc1000.pfb
%{_fontdir}/gomc1095.pfb
%{_fontdir}/gomc1200.pfb
%{_fontdir}/gomc1440.pfb
%{_fontdir}/gomc1728.pfb
%{_fontdir}/gomc2074.pfb
%{_fontdir}/gomc2488.pfb
%{_fontdir}/gomc2986.pfb
%{_fontdir}/gomc3583.pfb
%{_fontdir}/gomi0500.pfb
%{_fontdir}/gomi0600.pfb
%{_fontdir}/gomi0700.pfb
%{_fontdir}/gomi0800.pfb
%{_fontdir}/gomi0900.pfb
%{_fontdir}/gomi1000.pfb
%{_fontdir}/gomi1095.pfb
%{_fontdir}/gomi1200.pfb
%{_fontdir}/gomi1440.pfb
%{_fontdir}/gomi1728.pfb
%{_fontdir}/gomi2074.pfb
%{_fontdir}/gomi2488.pfb
%{_fontdir}/gomi2986.pfb
%{_fontdir}/gomi3583.pfb
%{_fontdir}/gomn0500.pfb
%{_fontdir}/gomn0600.pfb
%{_fontdir}/gomn0700.pfb
%{_fontdir}/gomn0800.pfb
%{_fontdir}/gomn0900.pfb
%{_fontdir}/gomn1000.pfb
%{_fontdir}/gomn1095.pfb
%{_fontdir}/gomn1200.pfb
%{_fontdir}/gomn1440.pfb
%{_fontdir}/gomn1728.pfb
%{_fontdir}/gomn2074.pfb
%{_fontdir}/gomn2488.pfb
%{_fontdir}/gomn2986.pfb
%{_fontdir}/gomn3583.pfb
%{_fontdir}/gomo0500.pfb
%{_fontdir}/gomo0600.pfb
%{_fontdir}/gomo0700.pfb
%{_fontdir}/gomo0800.pfb
%{_fontdir}/gomo0900.pfb
%{_fontdir}/gomo1000.pfb
%{_fontdir}/gomo1095.pfb
%{_fontdir}/gomo1200.pfb
%{_fontdir}/gomo1440.pfb
%{_fontdir}/gomo1728.pfb
%{_fontdir}/gomo2074.pfb
%{_fontdir}/gomo2488.pfb
%{_fontdir}/gomo2986.pfb
%{_fontdir}/gomo3583.pfb
%{_fontdir}/gomu0500.pfb
%{_fontdir}/gomu0600.pfb
%{_fontdir}/gomu0700.pfb
%{_fontdir}/gomu0800.pfb
%{_fontdir}/gomu0900.pfb
%{_fontdir}/gomu1000.pfb
%{_fontdir}/gomu1095.pfb
%{_fontdir}/gomu1200.pfb
%{_fontdir}/gomu1440.pfb
%{_fontdir}/gomu1728.pfb
%{_fontdir}/gomu2074.pfb
%{_fontdir}/gomu2488.pfb
%{_fontdir}/gomu2986.pfb
%{_fontdir}/gomu3583.pfb
%{_fontdir}/goxc0500.pfb
%{_fontdir}/goxc0600.pfb
%{_fontdir}/goxc0700.pfb
%{_fontdir}/goxc0800.pfb
%{_fontdir}/goxc0900.pfb
%{_fontdir}/goxc1000.pfb
%{_fontdir}/goxc1095.pfb
%{_fontdir}/goxc1200.pfb
%{_fontdir}/goxc1440.pfb
%{_fontdir}/goxc1728.pfb
%{_fontdir}/goxc2074.pfb
%{_fontdir}/goxc2488.pfb
%{_fontdir}/goxc2986.pfb
%{_fontdir}/goxc3583.pfb
%{_fontdir}/goxi0500.pfb
%{_fontdir}/goxi0600.pfb
%{_fontdir}/goxi0700.pfb
%{_fontdir}/goxi0800.pfb
%{_fontdir}/goxi0900.pfb
%{_fontdir}/goxi1000.pfb
%{_fontdir}/goxi1095.pfb
%{_fontdir}/goxi1200.pfb
%{_fontdir}/goxi1440.pfb
%{_fontdir}/goxi1728.pfb
%{_fontdir}/goxi2074.pfb
%{_fontdir}/goxi2488.pfb
%{_fontdir}/goxi2986.pfb
%{_fontdir}/goxi3583.pfb
%{_fontdir}/goxn0500.pfb
%{_fontdir}/goxn0600.pfb
%{_fontdir}/goxn0700.pfb
%{_fontdir}/goxn0800.pfb
%{_fontdir}/goxn0900.pfb
%{_fontdir}/goxn1000.pfb
%{_fontdir}/goxn1095.pfb
%{_fontdir}/goxn1200.pfb
%{_fontdir}/goxn1440.pfb
%{_fontdir}/goxn1728.pfb
%{_fontdir}/goxn2074.pfb
%{_fontdir}/goxn2488.pfb
%{_fontdir}/goxn2986.pfb
%{_fontdir}/goxn3583.pfb
%{_fontdir}/goxo0500.pfb
%{_fontdir}/goxo0600.pfb
%{_fontdir}/goxo0700.pfb
%{_fontdir}/goxo0800.pfb
%{_fontdir}/goxo0900.pfb
%{_fontdir}/goxo1000.pfb
%{_fontdir}/goxo1095.pfb
%{_fontdir}/goxo1200.pfb
%{_fontdir}/goxo1440.pfb
%{_fontdir}/goxo1728.pfb
%{_fontdir}/goxo2074.pfb
%{_fontdir}/goxo2488.pfb
%{_fontdir}/goxo2986.pfb
%{_fontdir}/goxo3583.pfb
%{_fontdir}/goxu0500.pfb
%{_fontdir}/goxu0600.pfb
%{_fontdir}/goxu0700.pfb
%{_fontdir}/goxu0800.pfb
%{_fontdir}/goxu0900.pfb
%{_fontdir}/goxu1000.pfb
%{_fontdir}/goxu1095.pfb
%{_fontdir}/goxu1200.pfb
%{_fontdir}/goxu1440.pfb
%{_fontdir}/goxu1728.pfb
%{_fontdir}/goxu2074.pfb
%{_fontdir}/goxu2488.pfb
%{_fontdir}/goxu2986.pfb
%{_fontdir}/goxu3583.pfb
%{_fontdir}/grbl0500.pfb
%{_fontdir}/grbl0600.pfb
%{_fontdir}/grbl0700.pfb
%{_fontdir}/grbl0800.pfb
%{_fontdir}/grbl0900.pfb
%{_fontdir}/grbl1000.pfb
%{_fontdir}/grbl1095.pfb
%{_fontdir}/grbl1200.pfb
%{_fontdir}/grbl1440.pfb
%{_fontdir}/grbl1728.pfb
%{_fontdir}/grbl2074.pfb
%{_fontdir}/grbl2488.pfb
%{_fontdir}/grbl2986.pfb
%{_fontdir}/grbl3583.pfb
%{_fontdir}/grmc0500.pfb
%{_fontdir}/grmc0600.pfb
%{_fontdir}/grmc0700.pfb
%{_fontdir}/grmc0800.pfb
%{_fontdir}/grmc0900.pfb
%{_fontdir}/grmc1000.pfb
%{_fontdir}/grmc1095.pfb
%{_fontdir}/grmc1200.pfb
%{_fontdir}/grmc1440.pfb
%{_fontdir}/grmc1728.pfb
%{_fontdir}/grmc2074.pfb
%{_fontdir}/grmc2488.pfb
%{_fontdir}/grmc2986.pfb
%{_fontdir}/grmc3583.pfb
%{_fontdir}/grmi0500.pfb
%{_fontdir}/grmi0600.pfb
%{_fontdir}/grmi0700.pfb
%{_fontdir}/grmi0800.pfb
%{_fontdir}/grmi0900.pfb
%{_fontdir}/grmi1000.pfb
%{_fontdir}/grmi1095.pfb
%{_fontdir}/grmi1200.pfb
%{_fontdir}/grmi1440.pfb
%{_fontdir}/grmi1728.pfb
%{_fontdir}/grmi2074.pfb
%{_fontdir}/grmi2488.pfb
%{_fontdir}/grmi2986.pfb
%{_fontdir}/grmi3583.pfb
%{_fontdir}/grml0500.pfb
%{_fontdir}/grml0600.pfb
%{_fontdir}/grml0700.pfb
%{_fontdir}/grml0800.pfb
%{_fontdir}/grml0900.pfb
%{_fontdir}/grml1000.pfb
%{_fontdir}/grml1095.pfb
%{_fontdir}/grml1200.pfb
%{_fontdir}/grml1440.pfb
%{_fontdir}/grml1728.pfb
%{_fontdir}/grml2074.pfb
%{_fontdir}/grml2488.pfb
%{_fontdir}/grml2986.pfb
%{_fontdir}/grml3583.pfb
%{_fontdir}/grmn0500.pfb
%{_fontdir}/grmn0600.pfb
%{_fontdir}/grmn0700.pfb
%{_fontdir}/grmn0800.pfb
%{_fontdir}/grmn0900.pfb
%{_fontdir}/grmn1000.pfb
%{_fontdir}/grmn1095.pfb
%{_fontdir}/grmn1200.pfb
%{_fontdir}/grmn1440.pfb
%{_fontdir}/grmn1728.pfb
%{_fontdir}/grmn2074.pfb
%{_fontdir}/grmn2488.pfb
%{_fontdir}/grmn2986.pfb
%{_fontdir}/grmn3583.pfb
%{_fontdir}/grmo0500.pfb
%{_fontdir}/grmo0600.pfb
%{_fontdir}/grmo0700.pfb
%{_fontdir}/grmo0800.pfb
%{_fontdir}/grmo0900.pfb
%{_fontdir}/grmo1000.pfb
%{_fontdir}/grmo1095.pfb
%{_fontdir}/grmo1200.pfb
%{_fontdir}/grmo1440.pfb
%{_fontdir}/grmo1728.pfb
%{_fontdir}/grmo2074.pfb
%{_fontdir}/grmo2488.pfb
%{_fontdir}/grmo2986.pfb
%{_fontdir}/grmo3583.pfb
%{_fontdir}/grmu0500.pfb
%{_fontdir}/grmu0600.pfb
%{_fontdir}/grmu0700.pfb
%{_fontdir}/grmu0800.pfb
%{_fontdir}/grmu0900.pfb
%{_fontdir}/grmu1000.pfb
%{_fontdir}/grmu1095.pfb
%{_fontdir}/grmu1200.pfb
%{_fontdir}/grmu1440.pfb
%{_fontdir}/grmu1728.pfb
%{_fontdir}/grmu2074.pfb
%{_fontdir}/grmu2488.pfb
%{_fontdir}/grmu2986.pfb
%{_fontdir}/grmu3583.pfb
%{_fontdir}/grxc0500.pfb
%{_fontdir}/grxc0600.pfb
%{_fontdir}/grxc0700.pfb
%{_fontdir}/grxc0800.pfb
%{_fontdir}/grxc0900.pfb
%{_fontdir}/grxc1000.pfb
%{_fontdir}/grxc1095.pfb
%{_fontdir}/grxc1200.pfb
%{_fontdir}/grxc1440.pfb
%{_fontdir}/grxc1728.pfb
%{_fontdir}/grxc2074.pfb
%{_fontdir}/grxc2488.pfb
%{_fontdir}/grxc2986.pfb
%{_fontdir}/grxc3583.pfb
%{_fontdir}/grxi0500.pfb
%{_fontdir}/grxi0600.pfb
%{_fontdir}/grxi0700.pfb
%{_fontdir}/grxi0800.pfb
%{_fontdir}/grxi0900.pfb
%{_fontdir}/grxi1000.pfb
%{_fontdir}/grxi1095.pfb
%{_fontdir}/grxi1200.pfb
%{_fontdir}/grxi1440.pfb
%{_fontdir}/grxi1728.pfb
%{_fontdir}/grxi2074.pfb
%{_fontdir}/grxi2488.pfb
%{_fontdir}/grxi2986.pfb
%{_fontdir}/grxi3583.pfb
%{_fontdir}/grxl0500.pfb
%{_fontdir}/grxl0600.pfb
%{_fontdir}/grxl0700.pfb
%{_fontdir}/grxl0800.pfb
%{_fontdir}/grxl0900.pfb
%{_fontdir}/grxl1000.pfb
%{_fontdir}/grxl1095.pfb
%{_fontdir}/grxl1200.pfb
%{_fontdir}/grxl1440.pfb
%{_fontdir}/grxl1728.pfb
%{_fontdir}/grxl2074.pfb
%{_fontdir}/grxl2488.pfb
%{_fontdir}/grxl2986.pfb
%{_fontdir}/grxl3583.pfb
%{_fontdir}/grxn0500.pfb
%{_fontdir}/grxn0600.pfb
%{_fontdir}/grxn0700.pfb
%{_fontdir}/grxn0800.pfb
%{_fontdir}/grxn0900.pfb
%{_fontdir}/grxn1000.pfb
%{_fontdir}/grxn1095.pfb
%{_fontdir}/grxn1200.pfb
%{_fontdir}/grxn1440.pfb
%{_fontdir}/grxn1728.pfb
%{_fontdir}/grxn2074.pfb
%{_fontdir}/grxn2488.pfb
%{_fontdir}/grxn2986.pfb
%{_fontdir}/grxn3583.pfb
%{_fontdir}/grxo0500.pfb
%{_fontdir}/grxo0600.pfb
%{_fontdir}/grxo0700.pfb
%{_fontdir}/grxo0800.pfb
%{_fontdir}/grxo0900.pfb
%{_fontdir}/grxo1000.pfb
%{_fontdir}/grxo1095.pfb
%{_fontdir}/grxo1200.pfb
%{_fontdir}/grxo1440.pfb
%{_fontdir}/grxo1728.pfb
%{_fontdir}/grxo2074.pfb
%{_fontdir}/grxo2488.pfb
%{_fontdir}/grxo2986.pfb
%{_fontdir}/grxo3583.pfb
%{_fontdir}/grxu0500.pfb
%{_fontdir}/grxu0600.pfb
%{_fontdir}/grxu0700.pfb
%{_fontdir}/grxu0800.pfb
%{_fontdir}/grxu0900.pfb
%{_fontdir}/grxu1000.pfb
%{_fontdir}/grxu1095.pfb
%{_fontdir}/grxu1200.pfb
%{_fontdir}/grxu1440.pfb
%{_fontdir}/grxu1728.pfb
%{_fontdir}/grxu2074.pfb
%{_fontdir}/grxu2488.pfb
%{_fontdir}/grxu2986.pfb
%{_fontdir}/grxu3583.pfb
%{_fontdir}/gsma0500.pfb
%{_fontdir}/gsma0600.pfb
%{_fontdir}/gsma0700.pfb
%{_fontdir}/gsma0800.pfb
%{_fontdir}/gsma0900.pfb
%{_fontdir}/gsma1000.pfb
%{_fontdir}/gsma1095.pfb
%{_fontdir}/gsma1200.pfb
%{_fontdir}/gsma1440.pfb
%{_fontdir}/gsma1728.pfb
%{_fontdir}/gsma2074.pfb
%{_fontdir}/gsma2488.pfb
%{_fontdir}/gsma2986.pfb
%{_fontdir}/gsma3583.pfb
%{_fontdir}/gsmc0500.pfb
%{_fontdir}/gsmc0600.pfb
%{_fontdir}/gsmc0700.pfb
%{_fontdir}/gsmc0800.pfb
%{_fontdir}/gsmc0900.pfb
%{_fontdir}/gsmc1000.pfb
%{_fontdir}/gsmc1095.pfb
%{_fontdir}/gsmc1200.pfb
%{_fontdir}/gsmc1440.pfb
%{_fontdir}/gsmc1728.pfb
%{_fontdir}/gsmc2074.pfb
%{_fontdir}/gsmc2488.pfb
%{_fontdir}/gsmc2986.pfb
%{_fontdir}/gsmc3583.pfb
%{_fontdir}/gsme0500.pfb
%{_fontdir}/gsme0600.pfb
%{_fontdir}/gsme0700.pfb
%{_fontdir}/gsme0800.pfb
%{_fontdir}/gsme0900.pfb
%{_fontdir}/gsme1000.pfb
%{_fontdir}/gsme1095.pfb
%{_fontdir}/gsme1200.pfb
%{_fontdir}/gsme1440.pfb
%{_fontdir}/gsme1728.pfb
%{_fontdir}/gsme2074.pfb
%{_fontdir}/gsme2488.pfb
%{_fontdir}/gsme2986.pfb
%{_fontdir}/gsme3583.pfb
%{_fontdir}/gsmi0500.pfb
%{_fontdir}/gsmi0600.pfb
%{_fontdir}/gsmi0700.pfb
%{_fontdir}/gsmi0800.pfb
%{_fontdir}/gsmi0900.pfb
%{_fontdir}/gsmi1000.pfb
%{_fontdir}/gsmi1095.pfb
%{_fontdir}/gsmi1200.pfb
%{_fontdir}/gsmi1440.pfb
%{_fontdir}/gsmi1728.pfb
%{_fontdir}/gsmi2074.pfb
%{_fontdir}/gsmi2488.pfb
%{_fontdir}/gsmi2986.pfb
%{_fontdir}/gsmi3583.pfb
%{_fontdir}/gsmn0500.pfb
%{_fontdir}/gsmn0600.pfb
%{_fontdir}/gsmn0700.pfb
%{_fontdir}/gsmn0800.pfb
%{_fontdir}/gsmn0900.pfb
%{_fontdir}/gsmn1000.pfb
%{_fontdir}/gsmn1095.pfb
%{_fontdir}/gsmn1200.pfb
%{_fontdir}/gsmn1440.pfb
%{_fontdir}/gsmn1728.pfb
%{_fontdir}/gsmn2074.pfb
%{_fontdir}/gsmn2488.pfb
%{_fontdir}/gsmn2986.pfb
%{_fontdir}/gsmn3583.pfb
%{_fontdir}/gsmo0500.pfb
%{_fontdir}/gsmo0600.pfb
%{_fontdir}/gsmo0700.pfb
%{_fontdir}/gsmo0800.pfb
%{_fontdir}/gsmo0900.pfb
%{_fontdir}/gsmo1000.pfb
%{_fontdir}/gsmo1095.pfb
%{_fontdir}/gsmo1200.pfb
%{_fontdir}/gsmo1440.pfb
%{_fontdir}/gsmo1728.pfb
%{_fontdir}/gsmo2074.pfb
%{_fontdir}/gsmo2488.pfb
%{_fontdir}/gsmo2986.pfb
%{_fontdir}/gsmo3583.pfb
%{_fontdir}/gsmu0500.pfb
%{_fontdir}/gsmu0600.pfb
%{_fontdir}/gsmu0700.pfb
%{_fontdir}/gsmu0800.pfb
%{_fontdir}/gsmu0900.pfb
%{_fontdir}/gsmu1000.pfb
%{_fontdir}/gsmu1095.pfb
%{_fontdir}/gsmu1200.pfb
%{_fontdir}/gsmu1440.pfb
%{_fontdir}/gsmu1728.pfb
%{_fontdir}/gsmu2074.pfb
%{_fontdir}/gsmu2488.pfb
%{_fontdir}/gsmu2986.pfb
%{_fontdir}/gsmu3583.pfb
%{_fontdir}/gsxa0500.pfb
%{_fontdir}/gsxa0600.pfb
%{_fontdir}/gsxa0700.pfb
%{_fontdir}/gsxa0800.pfb
%{_fontdir}/gsxa0900.pfb
%{_fontdir}/gsxa1000.pfb
%{_fontdir}/gsxa1095.pfb
%{_fontdir}/gsxa1200.pfb
%{_fontdir}/gsxa1440.pfb
%{_fontdir}/gsxa1728.pfb
%{_fontdir}/gsxa2074.pfb
%{_fontdir}/gsxa2488.pfb
%{_fontdir}/gsxa2986.pfb
%{_fontdir}/gsxa3583.pfb
%{_fontdir}/gsxc0500.pfb
%{_fontdir}/gsxc0600.pfb
%{_fontdir}/gsxc0700.pfb
%{_fontdir}/gsxc0800.pfb
%{_fontdir}/gsxc0900.pfb
%{_fontdir}/gsxc1000.pfb
%{_fontdir}/gsxc1095.pfb
%{_fontdir}/gsxc1200.pfb
%{_fontdir}/gsxc1440.pfb
%{_fontdir}/gsxc1728.pfb
%{_fontdir}/gsxc2074.pfb
%{_fontdir}/gsxc2488.pfb
%{_fontdir}/gsxc2986.pfb
%{_fontdir}/gsxc3583.pfb
%{_fontdir}/gsxe0500.pfb
%{_fontdir}/gsxe0600.pfb
%{_fontdir}/gsxe0700.pfb
%{_fontdir}/gsxe0800.pfb
%{_fontdir}/gsxe0900.pfb
%{_fontdir}/gsxe1000.pfb
%{_fontdir}/gsxe1095.pfb
%{_fontdir}/gsxe1200.pfb
%{_fontdir}/gsxe1440.pfb
%{_fontdir}/gsxe1728.pfb
%{_fontdir}/gsxe2074.pfb
%{_fontdir}/gsxe2488.pfb
%{_fontdir}/gsxe2986.pfb
%{_fontdir}/gsxe3583.pfb
%{_fontdir}/gsxi0500.pfb
%{_fontdir}/gsxi0600.pfb
%{_fontdir}/gsxi0700.pfb
%{_fontdir}/gsxi0800.pfb
%{_fontdir}/gsxi0900.pfb
%{_fontdir}/gsxi1000.pfb
%{_fontdir}/gsxi1095.pfb
%{_fontdir}/gsxi1200.pfb
%{_fontdir}/gsxi1440.pfb
%{_fontdir}/gsxi1728.pfb
%{_fontdir}/gsxi2074.pfb
%{_fontdir}/gsxi2488.pfb
%{_fontdir}/gsxi2986.pfb
%{_fontdir}/gsxi3583.pfb
%{_fontdir}/gsxn0500.pfb
%{_fontdir}/gsxn0600.pfb
%{_fontdir}/gsxn0700.pfb
%{_fontdir}/gsxn0800.pfb
%{_fontdir}/gsxn0900.pfb
%{_fontdir}/gsxn1000.pfb
%{_fontdir}/gsxn1095.pfb
%{_fontdir}/gsxn1200.pfb
%{_fontdir}/gsxn1440.pfb
%{_fontdir}/gsxn1728.pfb
%{_fontdir}/gsxn2074.pfb
%{_fontdir}/gsxn2488.pfb
%{_fontdir}/gsxn2986.pfb
%{_fontdir}/gsxn3583.pfb
%{_fontdir}/gsxo0500.pfb
%{_fontdir}/gsxo0600.pfb
%{_fontdir}/gsxo0700.pfb
%{_fontdir}/gsxo0800.pfb
%{_fontdir}/gsxo0900.pfb
%{_fontdir}/gsxo1000.pfb
%{_fontdir}/gsxo1095.pfb
%{_fontdir}/gsxo1200.pfb
%{_fontdir}/gsxo1440.pfb
%{_fontdir}/gsxo1728.pfb
%{_fontdir}/gsxo2074.pfb
%{_fontdir}/gsxo2488.pfb
%{_fontdir}/gsxo2986.pfb
%{_fontdir}/gsxo3583.pfb
%{_fontdir}/gsxu0500.pfb
%{_fontdir}/gsxu0600.pfb
%{_fontdir}/gsxu0700.pfb
%{_fontdir}/gsxu0800.pfb
%{_fontdir}/gsxu0900.pfb
%{_fontdir}/gsxu1000.pfb
%{_fontdir}/gsxu1095.pfb
%{_fontdir}/gsxu1200.pfb
%{_fontdir}/gsxu1440.pfb
%{_fontdir}/gsxu1728.pfb
%{_fontdir}/gsxu2074.pfb
%{_fontdir}/gsxu2488.pfb
%{_fontdir}/gsxu2986.pfb
%{_fontdir}/gsxu3583.pfb
%{_fontdir}/gttc0500.pfb
%{_fontdir}/gttc0600.pfb
%{_fontdir}/gttc0700.pfb
%{_fontdir}/gttc0800.pfb
%{_fontdir}/gttc0900.pfb
%{_fontdir}/gttc1000.pfb
%{_fontdir}/gttc1095.pfb
%{_fontdir}/gttc1200.pfb
%{_fontdir}/gttc1440.pfb
%{_fontdir}/gttc1728.pfb
%{_fontdir}/gttc2074.pfb
%{_fontdir}/gttc2488.pfb
%{_fontdir}/gttc2986.pfb
%{_fontdir}/gttc3583.pfb
%{_fontdir}/gtti0500.pfb
%{_fontdir}/gtti0600.pfb
%{_fontdir}/gtti0700.pfb
%{_fontdir}/gtti0800.pfb
%{_fontdir}/gtti0900.pfb
%{_fontdir}/gtti1000.pfb
%{_fontdir}/gtti1095.pfb
%{_fontdir}/gtti1200.pfb
%{_fontdir}/gtti1440.pfb
%{_fontdir}/gtti1728.pfb
%{_fontdir}/gtti2074.pfb
%{_fontdir}/gtti2488.pfb
%{_fontdir}/gtti2986.pfb
%{_fontdir}/gtti3583.pfb
%{_fontdir}/gttn0500.pfb
%{_fontdir}/gttn0600.pfb
%{_fontdir}/gttn0700.pfb
%{_fontdir}/gttn0800.pfb
%{_fontdir}/gttn0900.pfb
%{_fontdir}/gttn1000.pfb
%{_fontdir}/gttn1095.pfb
%{_fontdir}/gttn1200.pfb
%{_fontdir}/gttn1440.pfb
%{_fontdir}/gttn1728.pfb
%{_fontdir}/gttn2074.pfb
%{_fontdir}/gttn2488.pfb
%{_fontdir}/gttn2986.pfb
%{_fontdir}/gttn3583.pfb
%{_fontdir}/gtto0500.pfb
%{_fontdir}/gtto0600.pfb
%{_fontdir}/gtto0700.pfb
%{_fontdir}/gtto0800.pfb
%{_fontdir}/gtto0900.pfb
%{_fontdir}/gtto1000.pfb
%{_fontdir}/gtto1095.pfb
%{_fontdir}/gtto1200.pfb
%{_fontdir}/gtto1440.pfb
%{_fontdir}/gtto1728.pfb
%{_fontdir}/gtto2074.pfb
%{_fontdir}/gtto2488.pfb
%{_fontdir}/gtto2986.pfb
%{_fontdir}/gtto3583.pfb
%{_fontdir}/gttu0500.pfb
%{_fontdir}/gttu0600.pfb
%{_fontdir}/gttu0700.pfb
%{_fontdir}/gttu0800.pfb
%{_fontdir}/gttu0900.pfb
%{_fontdir}/gttu1000.pfb
%{_fontdir}/gttu1095.pfb
%{_fontdir}/gttu1200.pfb
%{_fontdir}/gttu1440.pfb
%{_fontdir}/gttu1728.pfb
%{_fontdir}/gttu2074.pfb
%{_fontdir}/gttu2488.pfb
%{_fontdir}/gttu2986.pfb
%{_fontdir}/gttu3583.pfb

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
