%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/arphic.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/arphic.doc.tar.xz

Name: texlive-arphic
License: Freely redistributable without restriction
Summary: Arphic (Chinese) font packages
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-arphic-fedora-fonts = %{tl_version}

%description
These are font bundles for the Chinese Arphic fonts which work
with the CJK package. Arphic is actually the name of the
company that which created the fonts (and put them under a GPL-
like licence).

date: 2007-05-25 18:39:01 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map bkaiu.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map bsmiu.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map gbsnu.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map gkaiu.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map bkaiu.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map bsmiu.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map gbsnu.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map gkaiu.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for arphic
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for arphic

%package fedora-fonts
Summary: Fonts for arphic
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-arphic = %{tl_version}
BuildArch: noarch

%description fedora-fonts
These are font bundles for the Chinese Arphic fonts which work
with the CJK package. Arphic is actually the name of the
company that which created the fonts (and put them under a GPL-
like licence).

date: 2007-05-25 18:39:01 +0200


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/other-free.txt other-free.txt
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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu00.pfb .
ln -s %{_fontdir}/bkaiu00.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu00.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu02.pfb .
ln -s %{_fontdir}/bkaiu02.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu02.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu03.pfb .
ln -s %{_fontdir}/bkaiu03.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu03.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu20.pfb .
ln -s %{_fontdir}/bkaiu20.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu20.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu21.pfb .
ln -s %{_fontdir}/bkaiu21.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu21.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu22.pfb .
ln -s %{_fontdir}/bkaiu22.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu22.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu25.pfb .
ln -s %{_fontdir}/bkaiu25.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu25.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu26.pfb .
ln -s %{_fontdir}/bkaiu26.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu26.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu30.pfb .
ln -s %{_fontdir}/bkaiu30.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu30.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu31.pfb .
ln -s %{_fontdir}/bkaiu31.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu31.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu32.pfb .
ln -s %{_fontdir}/bkaiu32.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu32.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu33.pfb .
ln -s %{_fontdir}/bkaiu33.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu33.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu4e.pfb .
ln -s %{_fontdir}/bkaiu4e.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu4e.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu4f.pfb .
ln -s %{_fontdir}/bkaiu4f.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu4f.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu50.pfb .
ln -s %{_fontdir}/bkaiu50.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu50.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu51.pfb .
ln -s %{_fontdir}/bkaiu51.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu51.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu52.pfb .
ln -s %{_fontdir}/bkaiu52.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu52.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu53.pfb .
ln -s %{_fontdir}/bkaiu53.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu53.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu54.pfb .
ln -s %{_fontdir}/bkaiu54.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu54.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu55.pfb .
ln -s %{_fontdir}/bkaiu55.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu55.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu56.pfb .
ln -s %{_fontdir}/bkaiu56.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu56.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu57.pfb .
ln -s %{_fontdir}/bkaiu57.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu57.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu58.pfb .
ln -s %{_fontdir}/bkaiu58.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu58.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu59.pfb .
ln -s %{_fontdir}/bkaiu59.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu59.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu5a.pfb .
ln -s %{_fontdir}/bkaiu5a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu5a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu5b.pfb .
ln -s %{_fontdir}/bkaiu5b.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu5b.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu5c.pfb .
ln -s %{_fontdir}/bkaiu5c.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu5c.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu5d.pfb .
ln -s %{_fontdir}/bkaiu5d.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu5d.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu5e.pfb .
ln -s %{_fontdir}/bkaiu5e.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu5e.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu5f.pfb .
ln -s %{_fontdir}/bkaiu5f.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu5f.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu60.pfb .
ln -s %{_fontdir}/bkaiu60.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu60.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu61.pfb .
ln -s %{_fontdir}/bkaiu61.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu61.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu62.pfb .
ln -s %{_fontdir}/bkaiu62.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu62.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu63.pfb .
ln -s %{_fontdir}/bkaiu63.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu63.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu64.pfb .
ln -s %{_fontdir}/bkaiu64.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu64.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu65.pfb .
ln -s %{_fontdir}/bkaiu65.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu65.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu66.pfb .
ln -s %{_fontdir}/bkaiu66.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu66.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu67.pfb .
ln -s %{_fontdir}/bkaiu67.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu67.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu68.pfb .
ln -s %{_fontdir}/bkaiu68.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu68.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu69.pfb .
ln -s %{_fontdir}/bkaiu69.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu69.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu6a.pfb .
ln -s %{_fontdir}/bkaiu6a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu6a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu6b.pfb .
ln -s %{_fontdir}/bkaiu6b.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu6b.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu6c.pfb .
ln -s %{_fontdir}/bkaiu6c.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu6c.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu6d.pfb .
ln -s %{_fontdir}/bkaiu6d.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu6d.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu6e.pfb .
ln -s %{_fontdir}/bkaiu6e.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu6e.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu6f.pfb .
ln -s %{_fontdir}/bkaiu6f.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu6f.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu70.pfb .
ln -s %{_fontdir}/bkaiu70.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu70.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu71.pfb .
ln -s %{_fontdir}/bkaiu71.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu71.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu72.pfb .
ln -s %{_fontdir}/bkaiu72.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu72.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu73.pfb .
ln -s %{_fontdir}/bkaiu73.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu73.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu74.pfb .
ln -s %{_fontdir}/bkaiu74.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu74.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu75.pfb .
ln -s %{_fontdir}/bkaiu75.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu75.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu76.pfb .
ln -s %{_fontdir}/bkaiu76.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu76.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu77.pfb .
ln -s %{_fontdir}/bkaiu77.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu77.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu78.pfb .
ln -s %{_fontdir}/bkaiu78.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu78.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu79.pfb .
ln -s %{_fontdir}/bkaiu79.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu79.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu7a.pfb .
ln -s %{_fontdir}/bkaiu7a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu7a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu7b.pfb .
ln -s %{_fontdir}/bkaiu7b.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu7b.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu7c.pfb .
ln -s %{_fontdir}/bkaiu7c.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu7c.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu7d.pfb .
ln -s %{_fontdir}/bkaiu7d.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu7d.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu7e.pfb .
ln -s %{_fontdir}/bkaiu7e.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu7e.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu7f.pfb .
ln -s %{_fontdir}/bkaiu7f.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu7f.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu80.pfb .
ln -s %{_fontdir}/bkaiu80.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu80.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu81.pfb .
ln -s %{_fontdir}/bkaiu81.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu81.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu82.pfb .
ln -s %{_fontdir}/bkaiu82.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu82.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu83.pfb .
ln -s %{_fontdir}/bkaiu83.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu83.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu84.pfb .
ln -s %{_fontdir}/bkaiu84.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu84.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu85.pfb .
ln -s %{_fontdir}/bkaiu85.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu85.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu86.pfb .
ln -s %{_fontdir}/bkaiu86.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu86.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu87.pfb .
ln -s %{_fontdir}/bkaiu87.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu87.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu88.pfb .
ln -s %{_fontdir}/bkaiu88.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu88.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu89.pfb .
ln -s %{_fontdir}/bkaiu89.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu89.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu8a.pfb .
ln -s %{_fontdir}/bkaiu8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu8b.pfb .
ln -s %{_fontdir}/bkaiu8b.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu8b.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu8c.pfb .
ln -s %{_fontdir}/bkaiu8c.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu8c.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu8d.pfb .
ln -s %{_fontdir}/bkaiu8d.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu8d.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu8e.pfb .
ln -s %{_fontdir}/bkaiu8e.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu8e.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu8f.pfb .
ln -s %{_fontdir}/bkaiu8f.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu8f.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu90.pfb .
ln -s %{_fontdir}/bkaiu90.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu90.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu91.pfb .
ln -s %{_fontdir}/bkaiu91.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu91.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu92.pfb .
ln -s %{_fontdir}/bkaiu92.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu92.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu93.pfb .
ln -s %{_fontdir}/bkaiu93.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu93.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu94.pfb .
ln -s %{_fontdir}/bkaiu94.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu94.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu95.pfb .
ln -s %{_fontdir}/bkaiu95.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu95.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu96.pfb .
ln -s %{_fontdir}/bkaiu96.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu96.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu97.pfb .
ln -s %{_fontdir}/bkaiu97.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu97.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu98.pfb .
ln -s %{_fontdir}/bkaiu98.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu98.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu99.pfb .
ln -s %{_fontdir}/bkaiu99.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu99.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu9a.pfb .
ln -s %{_fontdir}/bkaiu9a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu9a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu9b.pfb .
ln -s %{_fontdir}/bkaiu9b.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu9b.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu9c.pfb .
ln -s %{_fontdir}/bkaiu9c.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu9c.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu9d.pfb .
ln -s %{_fontdir}/bkaiu9d.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu9d.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu9e.pfb .
ln -s %{_fontdir}/bkaiu9e.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu9e.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu9f.pfb .
ln -s %{_fontdir}/bkaiu9f.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu9f.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiuee.pfb .
ln -s %{_fontdir}/bkaiuee.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiuee.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiuf6.pfb .
ln -s %{_fontdir}/bkaiuf6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiuf6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiuf7.pfb .
ln -s %{_fontdir}/bkaiuf7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiuf7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiuf8.pfb .
ln -s %{_fontdir}/bkaiuf8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiuf8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiufa.pfb .
ln -s %{_fontdir}/bkaiufa.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiufa.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiufe.pfb .
ln -s %{_fontdir}/bkaiufe.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiufe.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiuff.pfb .
ln -s %{_fontdir}/bkaiuff.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiuff.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiuv.pfb .
ln -s %{_fontdir}/bkaiuv.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiuv.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu00.pfb .
ln -s %{_fontdir}/bsmiu00.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu00.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu02.pfb .
ln -s %{_fontdir}/bsmiu02.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu02.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu03.pfb .
ln -s %{_fontdir}/bsmiu03.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu03.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu20.pfb .
ln -s %{_fontdir}/bsmiu20.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu20.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu21.pfb .
ln -s %{_fontdir}/bsmiu21.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu21.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu22.pfb .
ln -s %{_fontdir}/bsmiu22.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu22.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu25.pfb .
ln -s %{_fontdir}/bsmiu25.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu25.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu26.pfb .
ln -s %{_fontdir}/bsmiu26.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu26.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu30.pfb .
ln -s %{_fontdir}/bsmiu30.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu30.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu31.pfb .
ln -s %{_fontdir}/bsmiu31.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu31.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu32.pfb .
ln -s %{_fontdir}/bsmiu32.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu32.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu33.pfb .
ln -s %{_fontdir}/bsmiu33.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu33.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu4e.pfb .
ln -s %{_fontdir}/bsmiu4e.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu4e.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu4f.pfb .
ln -s %{_fontdir}/bsmiu4f.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu4f.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu50.pfb .
ln -s %{_fontdir}/bsmiu50.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu50.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu51.pfb .
ln -s %{_fontdir}/bsmiu51.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu51.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu52.pfb .
ln -s %{_fontdir}/bsmiu52.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu52.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu53.pfb .
ln -s %{_fontdir}/bsmiu53.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu53.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu54.pfb .
ln -s %{_fontdir}/bsmiu54.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu54.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu55.pfb .
ln -s %{_fontdir}/bsmiu55.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu55.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu56.pfb .
ln -s %{_fontdir}/bsmiu56.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu56.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu57.pfb .
ln -s %{_fontdir}/bsmiu57.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu57.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu58.pfb .
ln -s %{_fontdir}/bsmiu58.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu58.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu59.pfb .
ln -s %{_fontdir}/bsmiu59.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu59.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu5a.pfb .
ln -s %{_fontdir}/bsmiu5a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu5a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu5b.pfb .
ln -s %{_fontdir}/bsmiu5b.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu5b.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu5c.pfb .
ln -s %{_fontdir}/bsmiu5c.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu5c.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu5d.pfb .
ln -s %{_fontdir}/bsmiu5d.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu5d.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu5e.pfb .
ln -s %{_fontdir}/bsmiu5e.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu5e.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu5f.pfb .
ln -s %{_fontdir}/bsmiu5f.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu5f.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu60.pfb .
ln -s %{_fontdir}/bsmiu60.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu60.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu61.pfb .
ln -s %{_fontdir}/bsmiu61.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu61.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu62.pfb .
ln -s %{_fontdir}/bsmiu62.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu62.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu63.pfb .
ln -s %{_fontdir}/bsmiu63.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu63.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu64.pfb .
ln -s %{_fontdir}/bsmiu64.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu64.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu65.pfb .
ln -s %{_fontdir}/bsmiu65.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu65.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu66.pfb .
ln -s %{_fontdir}/bsmiu66.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu66.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu67.pfb .
ln -s %{_fontdir}/bsmiu67.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu67.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu68.pfb .
ln -s %{_fontdir}/bsmiu68.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu68.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu69.pfb .
ln -s %{_fontdir}/bsmiu69.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu69.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu6a.pfb .
ln -s %{_fontdir}/bsmiu6a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu6a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu6b.pfb .
ln -s %{_fontdir}/bsmiu6b.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu6b.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu6c.pfb .
ln -s %{_fontdir}/bsmiu6c.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu6c.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu6d.pfb .
ln -s %{_fontdir}/bsmiu6d.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu6d.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu6e.pfb .
ln -s %{_fontdir}/bsmiu6e.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu6e.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu6f.pfb .
ln -s %{_fontdir}/bsmiu6f.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu6f.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu70.pfb .
ln -s %{_fontdir}/bsmiu70.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu70.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu71.pfb .
ln -s %{_fontdir}/bsmiu71.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu71.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu72.pfb .
ln -s %{_fontdir}/bsmiu72.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu72.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu73.pfb .
ln -s %{_fontdir}/bsmiu73.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu73.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu74.pfb .
ln -s %{_fontdir}/bsmiu74.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu74.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu75.pfb .
ln -s %{_fontdir}/bsmiu75.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu75.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu76.pfb .
ln -s %{_fontdir}/bsmiu76.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu76.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu77.pfb .
ln -s %{_fontdir}/bsmiu77.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu77.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu78.pfb .
ln -s %{_fontdir}/bsmiu78.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu78.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu79.pfb .
ln -s %{_fontdir}/bsmiu79.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu79.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu7a.pfb .
ln -s %{_fontdir}/bsmiu7a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu7a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu7b.pfb .
ln -s %{_fontdir}/bsmiu7b.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu7b.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu7c.pfb .
ln -s %{_fontdir}/bsmiu7c.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu7c.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu7d.pfb .
ln -s %{_fontdir}/bsmiu7d.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu7d.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu7e.pfb .
ln -s %{_fontdir}/bsmiu7e.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu7e.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu7f.pfb .
ln -s %{_fontdir}/bsmiu7f.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu7f.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu80.pfb .
ln -s %{_fontdir}/bsmiu80.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu80.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu81.pfb .
ln -s %{_fontdir}/bsmiu81.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu81.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu82.pfb .
ln -s %{_fontdir}/bsmiu82.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu82.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu83.pfb .
ln -s %{_fontdir}/bsmiu83.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu83.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu84.pfb .
ln -s %{_fontdir}/bsmiu84.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu84.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu85.pfb .
ln -s %{_fontdir}/bsmiu85.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu85.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu86.pfb .
ln -s %{_fontdir}/bsmiu86.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu86.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu87.pfb .
ln -s %{_fontdir}/bsmiu87.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu87.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu88.pfb .
ln -s %{_fontdir}/bsmiu88.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu88.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu89.pfb .
ln -s %{_fontdir}/bsmiu89.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu89.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu8a.pfb .
ln -s %{_fontdir}/bsmiu8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu8b.pfb .
ln -s %{_fontdir}/bsmiu8b.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu8b.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu8c.pfb .
ln -s %{_fontdir}/bsmiu8c.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu8c.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu8d.pfb .
ln -s %{_fontdir}/bsmiu8d.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu8d.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu8e.pfb .
ln -s %{_fontdir}/bsmiu8e.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu8e.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu8f.pfb .
ln -s %{_fontdir}/bsmiu8f.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu8f.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu90.pfb .
ln -s %{_fontdir}/bsmiu90.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu90.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu91.pfb .
ln -s %{_fontdir}/bsmiu91.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu91.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu92.pfb .
ln -s %{_fontdir}/bsmiu92.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu92.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu93.pfb .
ln -s %{_fontdir}/bsmiu93.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu93.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu94.pfb .
ln -s %{_fontdir}/bsmiu94.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu94.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu95.pfb .
ln -s %{_fontdir}/bsmiu95.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu95.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu96.pfb .
ln -s %{_fontdir}/bsmiu96.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu96.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu97.pfb .
ln -s %{_fontdir}/bsmiu97.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu97.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu98.pfb .
ln -s %{_fontdir}/bsmiu98.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu98.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu99.pfb .
ln -s %{_fontdir}/bsmiu99.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu99.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu9a.pfb .
ln -s %{_fontdir}/bsmiu9a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu9a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu9b.pfb .
ln -s %{_fontdir}/bsmiu9b.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu9b.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu9c.pfb .
ln -s %{_fontdir}/bsmiu9c.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu9c.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu9d.pfb .
ln -s %{_fontdir}/bsmiu9d.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu9d.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu9e.pfb .
ln -s %{_fontdir}/bsmiu9e.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu9e.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu9f.pfb .
ln -s %{_fontdir}/bsmiu9f.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu9f.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiuee.pfb .
ln -s %{_fontdir}/bsmiuee.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiuee.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiuf6.pfb .
ln -s %{_fontdir}/bsmiuf6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiuf6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiuf7.pfb .
ln -s %{_fontdir}/bsmiuf7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiuf7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiuf8.pfb .
ln -s %{_fontdir}/bsmiuf8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiuf8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiufa.pfb .
ln -s %{_fontdir}/bsmiufa.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiufa.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiufe.pfb .
ln -s %{_fontdir}/bsmiufe.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiufe.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiuff.pfb .
ln -s %{_fontdir}/bsmiuff.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiuff.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiuv.pfb .
ln -s %{_fontdir}/bsmiuv.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiuv.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu00.pfb .
ln -s %{_fontdir}/gbsnu00.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu00.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu01.pfb .
ln -s %{_fontdir}/gbsnu01.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu01.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu02.pfb .
ln -s %{_fontdir}/gbsnu02.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu02.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu03.pfb .
ln -s %{_fontdir}/gbsnu03.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu03.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu04.pfb .
ln -s %{_fontdir}/gbsnu04.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu04.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu20.pfb .
ln -s %{_fontdir}/gbsnu20.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu20.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu21.pfb .
ln -s %{_fontdir}/gbsnu21.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu21.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu22.pfb .
ln -s %{_fontdir}/gbsnu22.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu22.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu23.pfb .
ln -s %{_fontdir}/gbsnu23.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu23.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu24.pfb .
ln -s %{_fontdir}/gbsnu24.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu24.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu25.pfb .
ln -s %{_fontdir}/gbsnu25.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu25.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu26.pfb .
ln -s %{_fontdir}/gbsnu26.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu26.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu30.pfb .
ln -s %{_fontdir}/gbsnu30.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu30.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu31.pfb .
ln -s %{_fontdir}/gbsnu31.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu31.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu32.pfb .
ln -s %{_fontdir}/gbsnu32.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu32.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu4e.pfb .
ln -s %{_fontdir}/gbsnu4e.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu4e.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu4f.pfb .
ln -s %{_fontdir}/gbsnu4f.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu4f.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu50.pfb .
ln -s %{_fontdir}/gbsnu50.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu50.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu51.pfb .
ln -s %{_fontdir}/gbsnu51.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu51.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu52.pfb .
ln -s %{_fontdir}/gbsnu52.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu52.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu53.pfb .
ln -s %{_fontdir}/gbsnu53.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu53.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu54.pfb .
ln -s %{_fontdir}/gbsnu54.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu54.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu55.pfb .
ln -s %{_fontdir}/gbsnu55.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu55.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu56.pfb .
ln -s %{_fontdir}/gbsnu56.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu56.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu57.pfb .
ln -s %{_fontdir}/gbsnu57.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu57.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu58.pfb .
ln -s %{_fontdir}/gbsnu58.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu58.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu59.pfb .
ln -s %{_fontdir}/gbsnu59.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu59.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu5a.pfb .
ln -s %{_fontdir}/gbsnu5a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu5a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu5b.pfb .
ln -s %{_fontdir}/gbsnu5b.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu5b.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu5c.pfb .
ln -s %{_fontdir}/gbsnu5c.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu5c.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu5d.pfb .
ln -s %{_fontdir}/gbsnu5d.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu5d.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu5e.pfb .
ln -s %{_fontdir}/gbsnu5e.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu5e.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu5f.pfb .
ln -s %{_fontdir}/gbsnu5f.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu5f.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu60.pfb .
ln -s %{_fontdir}/gbsnu60.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu60.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu61.pfb .
ln -s %{_fontdir}/gbsnu61.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu61.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu62.pfb .
ln -s %{_fontdir}/gbsnu62.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu62.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu63.pfb .
ln -s %{_fontdir}/gbsnu63.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu63.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu64.pfb .
ln -s %{_fontdir}/gbsnu64.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu64.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu65.pfb .
ln -s %{_fontdir}/gbsnu65.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu65.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu66.pfb .
ln -s %{_fontdir}/gbsnu66.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu66.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu67.pfb .
ln -s %{_fontdir}/gbsnu67.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu67.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu68.pfb .
ln -s %{_fontdir}/gbsnu68.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu68.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu69.pfb .
ln -s %{_fontdir}/gbsnu69.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu69.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu6a.pfb .
ln -s %{_fontdir}/gbsnu6a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu6a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu6b.pfb .
ln -s %{_fontdir}/gbsnu6b.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu6b.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu6c.pfb .
ln -s %{_fontdir}/gbsnu6c.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu6c.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu6d.pfb .
ln -s %{_fontdir}/gbsnu6d.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu6d.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu6e.pfb .
ln -s %{_fontdir}/gbsnu6e.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu6e.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu6f.pfb .
ln -s %{_fontdir}/gbsnu6f.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu6f.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu70.pfb .
ln -s %{_fontdir}/gbsnu70.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu70.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu71.pfb .
ln -s %{_fontdir}/gbsnu71.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu71.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu72.pfb .
ln -s %{_fontdir}/gbsnu72.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu72.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu73.pfb .
ln -s %{_fontdir}/gbsnu73.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu73.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu74.pfb .
ln -s %{_fontdir}/gbsnu74.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu74.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu75.pfb .
ln -s %{_fontdir}/gbsnu75.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu75.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu76.pfb .
ln -s %{_fontdir}/gbsnu76.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu76.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu77.pfb .
ln -s %{_fontdir}/gbsnu77.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu77.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu78.pfb .
ln -s %{_fontdir}/gbsnu78.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu78.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu79.pfb .
ln -s %{_fontdir}/gbsnu79.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu79.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu7a.pfb .
ln -s %{_fontdir}/gbsnu7a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu7a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu7b.pfb .
ln -s %{_fontdir}/gbsnu7b.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu7b.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu7c.pfb .
ln -s %{_fontdir}/gbsnu7c.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu7c.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu7d.pfb .
ln -s %{_fontdir}/gbsnu7d.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu7d.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu7e.pfb .
ln -s %{_fontdir}/gbsnu7e.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu7e.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu7f.pfb .
ln -s %{_fontdir}/gbsnu7f.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu7f.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu80.pfb .
ln -s %{_fontdir}/gbsnu80.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu80.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu81.pfb .
ln -s %{_fontdir}/gbsnu81.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu81.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu82.pfb .
ln -s %{_fontdir}/gbsnu82.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu82.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu83.pfb .
ln -s %{_fontdir}/gbsnu83.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu83.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu84.pfb .
ln -s %{_fontdir}/gbsnu84.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu84.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu85.pfb .
ln -s %{_fontdir}/gbsnu85.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu85.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu86.pfb .
ln -s %{_fontdir}/gbsnu86.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu86.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu87.pfb .
ln -s %{_fontdir}/gbsnu87.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu87.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu88.pfb .
ln -s %{_fontdir}/gbsnu88.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu88.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu89.pfb .
ln -s %{_fontdir}/gbsnu89.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu89.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu8a.pfb .
ln -s %{_fontdir}/gbsnu8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu8b.pfb .
ln -s %{_fontdir}/gbsnu8b.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu8b.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu8c.pfb .
ln -s %{_fontdir}/gbsnu8c.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu8c.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu8d.pfb .
ln -s %{_fontdir}/gbsnu8d.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu8d.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu8e.pfb .
ln -s %{_fontdir}/gbsnu8e.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu8e.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu8f.pfb .
ln -s %{_fontdir}/gbsnu8f.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu8f.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu90.pfb .
ln -s %{_fontdir}/gbsnu90.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu90.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu91.pfb .
ln -s %{_fontdir}/gbsnu91.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu91.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu92.pfb .
ln -s %{_fontdir}/gbsnu92.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu92.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu93.pfb .
ln -s %{_fontdir}/gbsnu93.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu93.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu94.pfb .
ln -s %{_fontdir}/gbsnu94.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu94.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu95.pfb .
ln -s %{_fontdir}/gbsnu95.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu95.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu96.pfb .
ln -s %{_fontdir}/gbsnu96.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu96.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu97.pfb .
ln -s %{_fontdir}/gbsnu97.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu97.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu98.pfb .
ln -s %{_fontdir}/gbsnu98.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu98.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu99.pfb .
ln -s %{_fontdir}/gbsnu99.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu99.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu9a.pfb .
ln -s %{_fontdir}/gbsnu9a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu9a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu9b.pfb .
ln -s %{_fontdir}/gbsnu9b.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu9b.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu9c.pfb .
ln -s %{_fontdir}/gbsnu9c.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu9c.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu9e.pfb .
ln -s %{_fontdir}/gbsnu9e.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu9e.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu9f.pfb .
ln -s %{_fontdir}/gbsnu9f.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu9f.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnufe.pfb .
ln -s %{_fontdir}/gbsnufe.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnufe.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnuff.pfb .
ln -s %{_fontdir}/gbsnuff.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnuff.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu00.pfb .
ln -s %{_fontdir}/gkaiu00.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu00.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu01.pfb .
ln -s %{_fontdir}/gkaiu01.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu01.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu02.pfb .
ln -s %{_fontdir}/gkaiu02.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu02.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu03.pfb .
ln -s %{_fontdir}/gkaiu03.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu03.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu04.pfb .
ln -s %{_fontdir}/gkaiu04.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu04.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu20.pfb .
ln -s %{_fontdir}/gkaiu20.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu20.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu21.pfb .
ln -s %{_fontdir}/gkaiu21.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu21.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu22.pfb .
ln -s %{_fontdir}/gkaiu22.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu22.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu23.pfb .
ln -s %{_fontdir}/gkaiu23.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu23.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu24.pfb .
ln -s %{_fontdir}/gkaiu24.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu24.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu25.pfb .
ln -s %{_fontdir}/gkaiu25.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu25.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu26.pfb .
ln -s %{_fontdir}/gkaiu26.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu26.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu30.pfb .
ln -s %{_fontdir}/gkaiu30.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu30.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu31.pfb .
ln -s %{_fontdir}/gkaiu31.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu31.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu32.pfb .
ln -s %{_fontdir}/gkaiu32.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu32.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu4e.pfb .
ln -s %{_fontdir}/gkaiu4e.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu4e.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu4f.pfb .
ln -s %{_fontdir}/gkaiu4f.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu4f.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu50.pfb .
ln -s %{_fontdir}/gkaiu50.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu50.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu51.pfb .
ln -s %{_fontdir}/gkaiu51.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu51.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu52.pfb .
ln -s %{_fontdir}/gkaiu52.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu52.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu53.pfb .
ln -s %{_fontdir}/gkaiu53.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu53.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu54.pfb .
ln -s %{_fontdir}/gkaiu54.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu54.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu55.pfb .
ln -s %{_fontdir}/gkaiu55.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu55.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu56.pfb .
ln -s %{_fontdir}/gkaiu56.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu56.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu57.pfb .
ln -s %{_fontdir}/gkaiu57.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu57.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu58.pfb .
ln -s %{_fontdir}/gkaiu58.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu58.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu59.pfb .
ln -s %{_fontdir}/gkaiu59.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu59.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu5a.pfb .
ln -s %{_fontdir}/gkaiu5a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu5a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu5b.pfb .
ln -s %{_fontdir}/gkaiu5b.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu5b.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu5c.pfb .
ln -s %{_fontdir}/gkaiu5c.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu5c.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu5d.pfb .
ln -s %{_fontdir}/gkaiu5d.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu5d.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu5e.pfb .
ln -s %{_fontdir}/gkaiu5e.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu5e.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu5f.pfb .
ln -s %{_fontdir}/gkaiu5f.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu5f.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu60.pfb .
ln -s %{_fontdir}/gkaiu60.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu60.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu61.pfb .
ln -s %{_fontdir}/gkaiu61.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu61.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu62.pfb .
ln -s %{_fontdir}/gkaiu62.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu62.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu63.pfb .
ln -s %{_fontdir}/gkaiu63.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu63.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu64.pfb .
ln -s %{_fontdir}/gkaiu64.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu64.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu65.pfb .
ln -s %{_fontdir}/gkaiu65.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu65.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu66.pfb .
ln -s %{_fontdir}/gkaiu66.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu66.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu67.pfb .
ln -s %{_fontdir}/gkaiu67.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu67.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu68.pfb .
ln -s %{_fontdir}/gkaiu68.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu68.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu69.pfb .
ln -s %{_fontdir}/gkaiu69.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu69.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu6a.pfb .
ln -s %{_fontdir}/gkaiu6a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu6a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu6b.pfb .
ln -s %{_fontdir}/gkaiu6b.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu6b.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu6c.pfb .
ln -s %{_fontdir}/gkaiu6c.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu6c.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu6d.pfb .
ln -s %{_fontdir}/gkaiu6d.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu6d.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu6e.pfb .
ln -s %{_fontdir}/gkaiu6e.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu6e.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu6f.pfb .
ln -s %{_fontdir}/gkaiu6f.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu6f.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu70.pfb .
ln -s %{_fontdir}/gkaiu70.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu70.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu71.pfb .
ln -s %{_fontdir}/gkaiu71.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu71.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu72.pfb .
ln -s %{_fontdir}/gkaiu72.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu72.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu73.pfb .
ln -s %{_fontdir}/gkaiu73.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu73.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu74.pfb .
ln -s %{_fontdir}/gkaiu74.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu74.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu75.pfb .
ln -s %{_fontdir}/gkaiu75.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu75.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu76.pfb .
ln -s %{_fontdir}/gkaiu76.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu76.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu77.pfb .
ln -s %{_fontdir}/gkaiu77.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu77.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu78.pfb .
ln -s %{_fontdir}/gkaiu78.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu78.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu79.pfb .
ln -s %{_fontdir}/gkaiu79.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu79.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu7a.pfb .
ln -s %{_fontdir}/gkaiu7a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu7a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu7b.pfb .
ln -s %{_fontdir}/gkaiu7b.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu7b.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu7c.pfb .
ln -s %{_fontdir}/gkaiu7c.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu7c.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu7d.pfb .
ln -s %{_fontdir}/gkaiu7d.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu7d.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu7e.pfb .
ln -s %{_fontdir}/gkaiu7e.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu7e.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu7f.pfb .
ln -s %{_fontdir}/gkaiu7f.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu7f.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu80.pfb .
ln -s %{_fontdir}/gkaiu80.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu80.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu81.pfb .
ln -s %{_fontdir}/gkaiu81.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu81.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu82.pfb .
ln -s %{_fontdir}/gkaiu82.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu82.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu83.pfb .
ln -s %{_fontdir}/gkaiu83.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu83.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu84.pfb .
ln -s %{_fontdir}/gkaiu84.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu84.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu85.pfb .
ln -s %{_fontdir}/gkaiu85.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu85.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu86.pfb .
ln -s %{_fontdir}/gkaiu86.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu86.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu87.pfb .
ln -s %{_fontdir}/gkaiu87.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu87.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu88.pfb .
ln -s %{_fontdir}/gkaiu88.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu88.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu89.pfb .
ln -s %{_fontdir}/gkaiu89.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu89.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu8a.pfb .
ln -s %{_fontdir}/gkaiu8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu8b.pfb .
ln -s %{_fontdir}/gkaiu8b.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu8b.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu8c.pfb .
ln -s %{_fontdir}/gkaiu8c.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu8c.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu8d.pfb .
ln -s %{_fontdir}/gkaiu8d.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu8d.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu8e.pfb .
ln -s %{_fontdir}/gkaiu8e.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu8e.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu8f.pfb .
ln -s %{_fontdir}/gkaiu8f.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu8f.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu90.pfb .
ln -s %{_fontdir}/gkaiu90.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu90.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu91.pfb .
ln -s %{_fontdir}/gkaiu91.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu91.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu92.pfb .
ln -s %{_fontdir}/gkaiu92.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu92.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu93.pfb .
ln -s %{_fontdir}/gkaiu93.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu93.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu94.pfb .
ln -s %{_fontdir}/gkaiu94.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu94.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu95.pfb .
ln -s %{_fontdir}/gkaiu95.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu95.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu96.pfb .
ln -s %{_fontdir}/gkaiu96.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu96.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu97.pfb .
ln -s %{_fontdir}/gkaiu97.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu97.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu98.pfb .
ln -s %{_fontdir}/gkaiu98.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu98.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu99.pfb .
ln -s %{_fontdir}/gkaiu99.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu99.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu9a.pfb .
ln -s %{_fontdir}/gkaiu9a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu9a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu9b.pfb .
ln -s %{_fontdir}/gkaiu9b.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu9b.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu9c.pfb .
ln -s %{_fontdir}/gkaiu9c.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu9c.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu9e.pfb .
ln -s %{_fontdir}/gkaiu9e.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu9e.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu9f.pfb .
ln -s %{_fontdir}/gkaiu9f.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu9f.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiufe.pfb .
ln -s %{_fontdir}/gkaiufe.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiufe.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiuff.pfb .
ln -s %{_fontdir}/gkaiuff.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiuff.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/dvips/arphic/config.bkaiu
%{_texdir}/texmf-dist/dvips/arphic/config.bsmiu
%{_texdir}/texmf-dist/dvips/arphic/config.gbsnu
%{_texdir}/texmf-dist/dvips/arphic/config.gkaiu
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu00.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu02.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu03.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu20.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu21.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu22.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu25.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu26.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu30.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu31.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu32.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu33.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu4e.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu4f.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu50.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu51.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu52.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu53.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu54.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu55.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu56.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu57.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu58.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu59.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu5a.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu5b.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu5c.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu5d.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu5e.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu5f.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu60.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu61.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu62.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu63.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu64.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu65.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu66.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu67.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu68.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu69.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu6a.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu6b.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu6c.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu6d.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu6e.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu6f.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu70.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu71.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu72.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu73.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu74.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu75.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu76.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu77.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu78.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu79.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu7a.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu7b.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu7c.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu7d.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu7e.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu7f.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu80.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu81.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu82.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu83.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu84.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu85.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu86.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu87.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu88.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu89.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu8a.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu8b.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu8c.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu8d.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu8e.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu8f.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu90.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu91.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu92.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu93.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu94.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu95.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu96.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu97.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu98.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu99.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu9a.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu9b.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu9c.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu9d.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu9e.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiu9f.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiuee.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiuf6.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiuf7.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiuf8.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiufa.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiufe.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiuff.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu/bkaiuv.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu00.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu02.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu03.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu20.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu21.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu22.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu25.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu26.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu30.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu31.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu32.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu33.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu4e.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu4f.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu50.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu51.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu52.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu53.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu54.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu55.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu56.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu57.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu58.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu59.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu5a.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu5b.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu5c.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu5d.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu5e.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu5f.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu60.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu61.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu62.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu63.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu64.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu65.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu66.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu67.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu68.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu69.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu6a.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu6b.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu6c.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu6d.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu6e.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu6f.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu70.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu71.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu72.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu73.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu74.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu75.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu76.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu77.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu78.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu79.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu7a.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu7b.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu7c.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu7d.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu7e.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu7f.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu80.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu81.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu82.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu83.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu84.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu85.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu86.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu87.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu88.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu89.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu8a.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu8b.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu8c.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu8d.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu8e.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu8f.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu90.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu91.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu92.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu93.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu94.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu95.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu96.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu97.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu98.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu99.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu9a.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu9b.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu9c.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu9d.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu9e.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiu9f.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiuee.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiuf6.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiuf7.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiuf8.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiufa.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiufe.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiuff.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu/bsmiuv.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu00.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu01.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu02.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu03.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu04.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu20.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu21.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu22.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu23.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu24.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu25.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu26.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu30.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu31.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu32.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu4e.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu4f.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu50.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu51.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu52.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu53.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu54.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu55.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu56.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu57.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu58.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu59.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu5a.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu5b.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu5c.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu5d.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu5e.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu5f.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu60.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu61.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu62.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu63.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu64.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu65.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu66.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu67.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu68.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu69.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu6a.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu6b.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu6c.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu6d.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu6e.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu6f.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu70.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu71.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu72.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu73.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu74.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu75.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu76.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu77.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu78.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu79.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu7a.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu7b.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu7c.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu7d.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu7e.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu7f.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu80.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu81.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu82.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu83.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu84.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu85.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu86.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu87.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu88.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu89.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu8a.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu8b.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu8c.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu8d.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu8e.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu8f.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu90.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu91.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu92.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu93.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu94.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu95.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu96.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu97.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu98.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu99.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu9a.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu9b.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu9c.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu9e.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnu9f.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnufe.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu/gbsnuff.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu00.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu01.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu02.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu03.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu04.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu20.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu21.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu22.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu23.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu24.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu25.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu26.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu30.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu31.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu32.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu4e.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu4f.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu50.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu51.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu52.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu53.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu54.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu55.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu56.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu57.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu58.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu59.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu5a.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu5b.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu5c.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu5d.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu5e.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu5f.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu60.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu61.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu62.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu63.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu64.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu65.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu66.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu67.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu68.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu69.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu6a.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu6b.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu6c.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu6d.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu6e.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu6f.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu70.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu71.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu72.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu73.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu74.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu75.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu76.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu77.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu78.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu79.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu7a.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu7b.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu7c.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu7d.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu7e.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu7f.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu80.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu81.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu82.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu83.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu84.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu85.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu86.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu87.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu88.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu89.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu8a.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu8b.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu8c.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu8d.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu8e.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu8f.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu90.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu91.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu92.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu93.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu94.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu95.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu96.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu97.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu98.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu99.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu9a.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu9b.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu9c.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu9e.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiu9f.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiufe.afm
%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu/gkaiuff.afm
%{_texdir}/texmf-dist/fonts/map/dvips/arphic/bkaiu.map
%{_texdir}/texmf-dist/fonts/map/dvips/arphic/bsmiu.map
%{_texdir}/texmf-dist/fonts/map/dvips/arphic/gbsnu.map
%{_texdir}/texmf-dist/fonts/map/dvips/arphic/gkaiu.map
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp00.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp01.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp02.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp03.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp04.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp05.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp06.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp07.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp08.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp09.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp10.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp11.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp12.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp13.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp14.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp15.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp16.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp17.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp18.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp19.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp20.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp21.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp22.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp23.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp25.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp26.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp27.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp28.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp29.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp30.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp31.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp32.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp33.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp34.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp35.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp36.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp37.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp38.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp39.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp40.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp41.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp42.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp43.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp44.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp45.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp46.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp47.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp48.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp49.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp50.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp51.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp52.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp53.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp54.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimp55.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp/bkaimpv.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu00.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu02.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu03.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu20.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu21.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu22.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu25.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu26.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu30.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu31.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu32.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu33.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu4e.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu4f.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu50.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu51.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu52.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu53.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu54.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu55.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu56.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu57.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu58.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu59.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu5a.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu5b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu5c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu5d.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu5e.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu5f.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu60.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu61.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu62.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu63.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu64.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu65.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu66.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu67.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu68.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu69.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu6b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu6c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu6d.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu6e.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu6f.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu70.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu71.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu72.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu73.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu74.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu75.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu76.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu77.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu78.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu79.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu7b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu7c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu7d.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu7e.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu7f.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu80.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu81.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu82.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu83.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu84.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu85.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu86.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu87.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu88.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu89.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu8b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu8d.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu8e.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu8f.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu90.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu91.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu92.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu93.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu94.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu95.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu96.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu97.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu98.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu99.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu9b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu9c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu9d.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu9e.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiu9f.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiuee.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiuf6.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiuf7.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiuf8.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiufa.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiufe.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiuff.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu/bkaiuv.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp00.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp01.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp02.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp03.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp04.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp05.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp06.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp07.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp08.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp09.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp10.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp11.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp12.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp13.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp14.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp15.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp16.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp17.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp18.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp19.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp20.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp21.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp22.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp23.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp25.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp26.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp27.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp28.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp29.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp30.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp31.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp32.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp33.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp34.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp35.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp36.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp37.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp38.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp39.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp40.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp41.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp42.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp43.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp44.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp45.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp46.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp47.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp48.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp49.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp50.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp51.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp52.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp53.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp54.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilp55.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp/bsmilpv.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu00.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu02.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu03.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu20.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu21.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu22.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu25.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu26.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu30.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu31.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu32.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu33.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu4e.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu4f.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu50.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu51.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu52.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu53.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu54.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu55.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu56.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu57.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu58.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu59.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu5a.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu5b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu5c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu5d.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu5e.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu5f.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu60.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu61.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu62.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu63.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu64.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu65.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu66.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu67.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu68.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu69.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu6b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu6c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu6d.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu6e.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu6f.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu70.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu71.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu72.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu73.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu74.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu75.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu76.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu77.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu78.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu79.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu7b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu7c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu7d.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu7e.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu7f.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu80.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu81.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu82.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu83.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu84.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu85.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu86.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu87.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu88.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu89.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu8b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu8d.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu8e.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu8f.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu90.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu91.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu92.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu93.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu94.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu95.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu96.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu97.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu98.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu99.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu9b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu9c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu9d.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu9e.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiu9f.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiuee.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiuf6.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiuf7.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiuf8.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiufa.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiufe.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiuff.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu/bsmiuv.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp00.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp01.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp02.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp03.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp04.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp06.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp07.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp08.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp09.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp10.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp11.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp12.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp13.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp14.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp15.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp16.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp17.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp18.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp19.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp20.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp21.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp22.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp23.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp24.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp25.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp26.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp27.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp28.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp29.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp30.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp31.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp/gbsnlp32.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu00.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu01.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu02.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu03.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu04.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu20.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu21.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu22.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu23.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu24.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu25.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu26.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu30.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu31.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu32.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu4e.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu4f.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu50.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu51.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu52.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu53.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu54.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu55.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu56.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu57.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu58.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu59.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu5a.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu5b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu5c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu5d.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu5e.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu5f.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu60.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu61.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu62.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu63.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu64.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu65.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu66.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu67.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu68.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu69.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu6b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu6c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu6d.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu6e.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu6f.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu70.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu71.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu72.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu73.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu74.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu75.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu76.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu77.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu78.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu79.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu7b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu7c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu7d.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu7e.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu7f.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu80.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu81.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu82.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu83.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu84.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu85.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu86.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu87.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu88.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu89.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu8b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu8d.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu8e.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu8f.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu90.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu91.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu92.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu93.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu94.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu95.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu96.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu97.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu98.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu99.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu9b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu9c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu9e.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnu9f.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnufe.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu/gbsnuff.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp00.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp01.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp02.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp03.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp04.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp06.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp07.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp08.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp09.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp10.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp11.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp12.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp13.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp14.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp15.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp16.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp17.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp18.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp19.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp20.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp21.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp22.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp23.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp24.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp25.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp26.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp27.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp28.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp29.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp30.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp31.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp/gkaimp32.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu00.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu01.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu02.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu03.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu04.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu20.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu21.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu22.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu23.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu24.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu25.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu26.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu30.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu31.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu32.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu4e.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu4f.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu50.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu51.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu52.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu53.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu54.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu55.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu56.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu57.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu58.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu59.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu5a.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu5b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu5c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu5d.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu5e.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu5f.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu60.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu61.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu62.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu63.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu64.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu65.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu66.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu67.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu68.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu69.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu6b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu6c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu6d.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu6e.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu6f.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu70.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu71.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu72.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu73.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu74.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu75.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu76.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu77.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu78.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu79.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu7b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu7c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu7d.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu7e.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu7f.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu80.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu81.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu82.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu83.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu84.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu85.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu86.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu87.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu88.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu89.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu8b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu8d.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu8e.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu8f.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu90.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu91.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu92.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu93.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu94.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu95.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu96.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu97.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu98.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu99.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu9b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu9c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu9e.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiu9f.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiufe.tfm
%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu/gkaiuff.tfm
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu00.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu02.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu03.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu20.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu21.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu22.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu25.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu26.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu30.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu31.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu32.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu33.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu4e.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu4f.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu50.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu51.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu52.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu53.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu54.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu55.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu56.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu57.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu58.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu59.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu5a.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu5b.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu5c.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu5d.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu5e.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu5f.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu60.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu61.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu62.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu63.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu64.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu65.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu66.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu67.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu68.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu69.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu6a.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu6b.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu6c.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu6d.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu6e.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu6f.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu70.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu71.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu72.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu73.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu74.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu75.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu76.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu77.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu78.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu79.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu7a.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu7b.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu7c.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu7d.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu7e.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu7f.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu80.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu81.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu82.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu83.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu84.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu85.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu86.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu87.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu88.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu89.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu8b.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu8c.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu8d.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu8e.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu8f.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu90.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu91.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu92.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu93.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu94.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu95.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu96.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu97.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu98.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu99.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu9a.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu9b.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu9c.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu9d.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu9e.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiu9f.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiuee.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiuf6.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiuf7.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiuf8.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiufa.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiufe.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiuff.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu/bkaiuv.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu00.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu02.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu03.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu20.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu21.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu22.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu25.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu26.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu30.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu31.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu32.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu33.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu4e.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu4f.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu50.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu51.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu52.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu53.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu54.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu55.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu56.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu57.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu58.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu59.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu5a.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu5b.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu5c.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu5d.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu5e.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu5f.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu60.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu61.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu62.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu63.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu64.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu65.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu66.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu67.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu68.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu69.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu6a.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu6b.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu6c.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu6d.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu6e.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu6f.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu70.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu71.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu72.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu73.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu74.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu75.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu76.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu77.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu78.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu79.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu7a.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu7b.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu7c.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu7d.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu7e.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu7f.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu80.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu81.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu82.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu83.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu84.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu85.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu86.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu87.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu88.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu89.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu8b.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu8c.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu8d.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu8e.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu8f.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu90.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu91.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu92.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu93.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu94.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu95.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu96.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu97.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu98.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu99.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu9a.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu9b.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu9c.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu9d.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu9e.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiu9f.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiuee.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiuf6.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiuf7.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiuf8.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiufa.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiufe.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiuff.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu/bsmiuv.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu00.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu01.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu02.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu03.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu04.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu20.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu21.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu22.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu23.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu24.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu25.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu26.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu30.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu31.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu32.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu4e.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu4f.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu50.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu51.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu52.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu53.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu54.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu55.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu56.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu57.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu58.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu59.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu5a.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu5b.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu5c.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu5d.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu5e.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu5f.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu60.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu61.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu62.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu63.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu64.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu65.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu66.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu67.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu68.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu69.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu6a.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu6b.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu6c.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu6d.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu6e.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu6f.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu70.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu71.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu72.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu73.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu74.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu75.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu76.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu77.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu78.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu79.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu7a.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu7b.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu7c.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu7d.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu7e.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu7f.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu80.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu81.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu82.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu83.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu84.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu85.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu86.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu87.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu88.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu89.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu8b.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu8c.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu8d.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu8e.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu8f.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu90.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu91.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu92.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu93.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu94.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu95.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu96.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu97.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu98.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu99.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu9a.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu9b.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu9c.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu9e.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnu9f.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnufe.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu/gbsnuff.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu00.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu01.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu02.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu03.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu04.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu20.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu21.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu22.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu23.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu24.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu25.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu26.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu30.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu31.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu32.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu4e.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu4f.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu50.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu51.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu52.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu53.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu54.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu55.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu56.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu57.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu58.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu59.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu5a.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu5b.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu5c.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu5d.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu5e.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu5f.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu60.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu61.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu62.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu63.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu64.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu65.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu66.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu67.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu68.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu69.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu6a.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu6b.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu6c.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu6d.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu6e.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu6f.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu70.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu71.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu72.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu73.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu74.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu75.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu76.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu77.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu78.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu79.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu7a.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu7b.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu7c.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu7d.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu7e.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu7f.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu80.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu81.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu82.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu83.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu84.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu85.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu86.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu87.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu88.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu89.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu8b.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu8c.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu8d.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu8e.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu8f.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu90.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu91.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu92.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu93.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu94.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu95.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu96.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu97.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu98.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu99.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu9a.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu9b.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu9c.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu9e.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiu9f.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiufe.pfb
%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu/gkaiuff.pfb
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp00.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp01.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp02.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp03.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp04.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp05.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp06.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp07.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp08.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp09.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp10.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp11.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp12.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp13.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp14.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp15.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp16.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp17.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp18.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp19.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp20.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp21.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp22.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp23.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp25.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp26.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp27.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp28.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp29.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp30.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp31.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp32.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp33.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp34.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp35.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp36.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp37.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp38.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp39.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp40.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp41.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp42.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp43.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp44.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp45.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp46.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp47.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp48.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp49.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp50.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp51.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp52.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp53.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp54.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimp55.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp/bkaimpv.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp00.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp01.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp02.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp03.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp04.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp05.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp06.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp07.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp08.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp09.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp10.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp11.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp12.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp13.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp14.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp15.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp16.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp17.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp18.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp19.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp20.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp21.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp22.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp23.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp25.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp26.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp27.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp28.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp29.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp30.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp31.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp32.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp33.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp34.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp35.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp36.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp37.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp38.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp39.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp40.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp41.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp42.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp43.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp44.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp45.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp46.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp47.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp48.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp49.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp50.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp51.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp52.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp53.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp54.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilp55.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp/bsmilpv.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp00.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp01.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp02.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp03.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp04.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp06.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp07.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp08.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp09.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp10.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp11.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp12.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp13.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp14.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp15.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp16.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp17.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp18.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp19.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp20.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp21.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp22.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp23.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp24.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp25.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp26.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp27.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp28.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp29.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp30.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp31.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp/gbsnlp32.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp00.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp01.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp02.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp03.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp04.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp06.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp07.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp08.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp09.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp10.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp11.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp12.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp13.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp14.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp15.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp16.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp17.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp18.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp19.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp20.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp21.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp22.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp23.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp24.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp25.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp26.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp27.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp28.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp29.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp30.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp31.vf
%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp/gkaimp32.vf

%files doc
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/doc/fonts/arphic/arphic-sampler.pdf
%{_texdir}/texmf-dist/doc/fonts/arphic/arphic-sampler.tex
%{_texdir}/texmf-dist/doc/fonts/arphic/bkaiu/README
%{_texdir}/texmf-dist/doc/fonts/arphic/bsmiu/README
%{_texdir}/texmf-dist/doc/fonts/arphic/gbsnu/README
%{_texdir}/texmf-dist/doc/fonts/arphic/gkaiu/README

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/bkaiu00.pfb
%{_fontdir}/bkaiu02.pfb
%{_fontdir}/bkaiu03.pfb
%{_fontdir}/bkaiu20.pfb
%{_fontdir}/bkaiu21.pfb
%{_fontdir}/bkaiu22.pfb
%{_fontdir}/bkaiu25.pfb
%{_fontdir}/bkaiu26.pfb
%{_fontdir}/bkaiu30.pfb
%{_fontdir}/bkaiu31.pfb
%{_fontdir}/bkaiu32.pfb
%{_fontdir}/bkaiu33.pfb
%{_fontdir}/bkaiu4e.pfb
%{_fontdir}/bkaiu4f.pfb
%{_fontdir}/bkaiu50.pfb
%{_fontdir}/bkaiu51.pfb
%{_fontdir}/bkaiu52.pfb
%{_fontdir}/bkaiu53.pfb
%{_fontdir}/bkaiu54.pfb
%{_fontdir}/bkaiu55.pfb
%{_fontdir}/bkaiu56.pfb
%{_fontdir}/bkaiu57.pfb
%{_fontdir}/bkaiu58.pfb
%{_fontdir}/bkaiu59.pfb
%{_fontdir}/bkaiu5a.pfb
%{_fontdir}/bkaiu5b.pfb
%{_fontdir}/bkaiu5c.pfb
%{_fontdir}/bkaiu5d.pfb
%{_fontdir}/bkaiu5e.pfb
%{_fontdir}/bkaiu5f.pfb
%{_fontdir}/bkaiu60.pfb
%{_fontdir}/bkaiu61.pfb
%{_fontdir}/bkaiu62.pfb
%{_fontdir}/bkaiu63.pfb
%{_fontdir}/bkaiu64.pfb
%{_fontdir}/bkaiu65.pfb
%{_fontdir}/bkaiu66.pfb
%{_fontdir}/bkaiu67.pfb
%{_fontdir}/bkaiu68.pfb
%{_fontdir}/bkaiu69.pfb
%{_fontdir}/bkaiu6a.pfb
%{_fontdir}/bkaiu6b.pfb
%{_fontdir}/bkaiu6c.pfb
%{_fontdir}/bkaiu6d.pfb
%{_fontdir}/bkaiu6e.pfb
%{_fontdir}/bkaiu6f.pfb
%{_fontdir}/bkaiu70.pfb
%{_fontdir}/bkaiu71.pfb
%{_fontdir}/bkaiu72.pfb
%{_fontdir}/bkaiu73.pfb
%{_fontdir}/bkaiu74.pfb
%{_fontdir}/bkaiu75.pfb
%{_fontdir}/bkaiu76.pfb
%{_fontdir}/bkaiu77.pfb
%{_fontdir}/bkaiu78.pfb
%{_fontdir}/bkaiu79.pfb
%{_fontdir}/bkaiu7a.pfb
%{_fontdir}/bkaiu7b.pfb
%{_fontdir}/bkaiu7c.pfb
%{_fontdir}/bkaiu7d.pfb
%{_fontdir}/bkaiu7e.pfb
%{_fontdir}/bkaiu7f.pfb
%{_fontdir}/bkaiu80.pfb
%{_fontdir}/bkaiu81.pfb
%{_fontdir}/bkaiu82.pfb
%{_fontdir}/bkaiu83.pfb
%{_fontdir}/bkaiu84.pfb
%{_fontdir}/bkaiu85.pfb
%{_fontdir}/bkaiu86.pfb
%{_fontdir}/bkaiu87.pfb
%{_fontdir}/bkaiu88.pfb
%{_fontdir}/bkaiu89.pfb
%{_fontdir}/bkaiu8a.pfb
%{_fontdir}/bkaiu8b.pfb
%{_fontdir}/bkaiu8c.pfb
%{_fontdir}/bkaiu8d.pfb
%{_fontdir}/bkaiu8e.pfb
%{_fontdir}/bkaiu8f.pfb
%{_fontdir}/bkaiu90.pfb
%{_fontdir}/bkaiu91.pfb
%{_fontdir}/bkaiu92.pfb
%{_fontdir}/bkaiu93.pfb
%{_fontdir}/bkaiu94.pfb
%{_fontdir}/bkaiu95.pfb
%{_fontdir}/bkaiu96.pfb
%{_fontdir}/bkaiu97.pfb
%{_fontdir}/bkaiu98.pfb
%{_fontdir}/bkaiu99.pfb
%{_fontdir}/bkaiu9a.pfb
%{_fontdir}/bkaiu9b.pfb
%{_fontdir}/bkaiu9c.pfb
%{_fontdir}/bkaiu9d.pfb
%{_fontdir}/bkaiu9e.pfb
%{_fontdir}/bkaiu9f.pfb
%{_fontdir}/bkaiuee.pfb
%{_fontdir}/bkaiuf6.pfb
%{_fontdir}/bkaiuf7.pfb
%{_fontdir}/bkaiuf8.pfb
%{_fontdir}/bkaiufa.pfb
%{_fontdir}/bkaiufe.pfb
%{_fontdir}/bkaiuff.pfb
%{_fontdir}/bkaiuv.pfb
%{_fontdir}/bsmiu00.pfb
%{_fontdir}/bsmiu02.pfb
%{_fontdir}/bsmiu03.pfb
%{_fontdir}/bsmiu20.pfb
%{_fontdir}/bsmiu21.pfb
%{_fontdir}/bsmiu22.pfb
%{_fontdir}/bsmiu25.pfb
%{_fontdir}/bsmiu26.pfb
%{_fontdir}/bsmiu30.pfb
%{_fontdir}/bsmiu31.pfb
%{_fontdir}/bsmiu32.pfb
%{_fontdir}/bsmiu33.pfb
%{_fontdir}/bsmiu4e.pfb
%{_fontdir}/bsmiu4f.pfb
%{_fontdir}/bsmiu50.pfb
%{_fontdir}/bsmiu51.pfb
%{_fontdir}/bsmiu52.pfb
%{_fontdir}/bsmiu53.pfb
%{_fontdir}/bsmiu54.pfb
%{_fontdir}/bsmiu55.pfb
%{_fontdir}/bsmiu56.pfb
%{_fontdir}/bsmiu57.pfb
%{_fontdir}/bsmiu58.pfb
%{_fontdir}/bsmiu59.pfb
%{_fontdir}/bsmiu5a.pfb
%{_fontdir}/bsmiu5b.pfb
%{_fontdir}/bsmiu5c.pfb
%{_fontdir}/bsmiu5d.pfb
%{_fontdir}/bsmiu5e.pfb
%{_fontdir}/bsmiu5f.pfb
%{_fontdir}/bsmiu60.pfb
%{_fontdir}/bsmiu61.pfb
%{_fontdir}/bsmiu62.pfb
%{_fontdir}/bsmiu63.pfb
%{_fontdir}/bsmiu64.pfb
%{_fontdir}/bsmiu65.pfb
%{_fontdir}/bsmiu66.pfb
%{_fontdir}/bsmiu67.pfb
%{_fontdir}/bsmiu68.pfb
%{_fontdir}/bsmiu69.pfb
%{_fontdir}/bsmiu6a.pfb
%{_fontdir}/bsmiu6b.pfb
%{_fontdir}/bsmiu6c.pfb
%{_fontdir}/bsmiu6d.pfb
%{_fontdir}/bsmiu6e.pfb
%{_fontdir}/bsmiu6f.pfb
%{_fontdir}/bsmiu70.pfb
%{_fontdir}/bsmiu71.pfb
%{_fontdir}/bsmiu72.pfb
%{_fontdir}/bsmiu73.pfb
%{_fontdir}/bsmiu74.pfb
%{_fontdir}/bsmiu75.pfb
%{_fontdir}/bsmiu76.pfb
%{_fontdir}/bsmiu77.pfb
%{_fontdir}/bsmiu78.pfb
%{_fontdir}/bsmiu79.pfb
%{_fontdir}/bsmiu7a.pfb
%{_fontdir}/bsmiu7b.pfb
%{_fontdir}/bsmiu7c.pfb
%{_fontdir}/bsmiu7d.pfb
%{_fontdir}/bsmiu7e.pfb
%{_fontdir}/bsmiu7f.pfb
%{_fontdir}/bsmiu80.pfb
%{_fontdir}/bsmiu81.pfb
%{_fontdir}/bsmiu82.pfb
%{_fontdir}/bsmiu83.pfb
%{_fontdir}/bsmiu84.pfb
%{_fontdir}/bsmiu85.pfb
%{_fontdir}/bsmiu86.pfb
%{_fontdir}/bsmiu87.pfb
%{_fontdir}/bsmiu88.pfb
%{_fontdir}/bsmiu89.pfb
%{_fontdir}/bsmiu8a.pfb
%{_fontdir}/bsmiu8b.pfb
%{_fontdir}/bsmiu8c.pfb
%{_fontdir}/bsmiu8d.pfb
%{_fontdir}/bsmiu8e.pfb
%{_fontdir}/bsmiu8f.pfb
%{_fontdir}/bsmiu90.pfb
%{_fontdir}/bsmiu91.pfb
%{_fontdir}/bsmiu92.pfb
%{_fontdir}/bsmiu93.pfb
%{_fontdir}/bsmiu94.pfb
%{_fontdir}/bsmiu95.pfb
%{_fontdir}/bsmiu96.pfb
%{_fontdir}/bsmiu97.pfb
%{_fontdir}/bsmiu98.pfb
%{_fontdir}/bsmiu99.pfb
%{_fontdir}/bsmiu9a.pfb
%{_fontdir}/bsmiu9b.pfb
%{_fontdir}/bsmiu9c.pfb
%{_fontdir}/bsmiu9d.pfb
%{_fontdir}/bsmiu9e.pfb
%{_fontdir}/bsmiu9f.pfb
%{_fontdir}/bsmiuee.pfb
%{_fontdir}/bsmiuf6.pfb
%{_fontdir}/bsmiuf7.pfb
%{_fontdir}/bsmiuf8.pfb
%{_fontdir}/bsmiufa.pfb
%{_fontdir}/bsmiufe.pfb
%{_fontdir}/bsmiuff.pfb
%{_fontdir}/bsmiuv.pfb
%{_fontdir}/gbsnu00.pfb
%{_fontdir}/gbsnu01.pfb
%{_fontdir}/gbsnu02.pfb
%{_fontdir}/gbsnu03.pfb
%{_fontdir}/gbsnu04.pfb
%{_fontdir}/gbsnu20.pfb
%{_fontdir}/gbsnu21.pfb
%{_fontdir}/gbsnu22.pfb
%{_fontdir}/gbsnu23.pfb
%{_fontdir}/gbsnu24.pfb
%{_fontdir}/gbsnu25.pfb
%{_fontdir}/gbsnu26.pfb
%{_fontdir}/gbsnu30.pfb
%{_fontdir}/gbsnu31.pfb
%{_fontdir}/gbsnu32.pfb
%{_fontdir}/gbsnu4e.pfb
%{_fontdir}/gbsnu4f.pfb
%{_fontdir}/gbsnu50.pfb
%{_fontdir}/gbsnu51.pfb
%{_fontdir}/gbsnu52.pfb
%{_fontdir}/gbsnu53.pfb
%{_fontdir}/gbsnu54.pfb
%{_fontdir}/gbsnu55.pfb
%{_fontdir}/gbsnu56.pfb
%{_fontdir}/gbsnu57.pfb
%{_fontdir}/gbsnu58.pfb
%{_fontdir}/gbsnu59.pfb
%{_fontdir}/gbsnu5a.pfb
%{_fontdir}/gbsnu5b.pfb
%{_fontdir}/gbsnu5c.pfb
%{_fontdir}/gbsnu5d.pfb
%{_fontdir}/gbsnu5e.pfb
%{_fontdir}/gbsnu5f.pfb
%{_fontdir}/gbsnu60.pfb
%{_fontdir}/gbsnu61.pfb
%{_fontdir}/gbsnu62.pfb
%{_fontdir}/gbsnu63.pfb
%{_fontdir}/gbsnu64.pfb
%{_fontdir}/gbsnu65.pfb
%{_fontdir}/gbsnu66.pfb
%{_fontdir}/gbsnu67.pfb
%{_fontdir}/gbsnu68.pfb
%{_fontdir}/gbsnu69.pfb
%{_fontdir}/gbsnu6a.pfb
%{_fontdir}/gbsnu6b.pfb
%{_fontdir}/gbsnu6c.pfb
%{_fontdir}/gbsnu6d.pfb
%{_fontdir}/gbsnu6e.pfb
%{_fontdir}/gbsnu6f.pfb
%{_fontdir}/gbsnu70.pfb
%{_fontdir}/gbsnu71.pfb
%{_fontdir}/gbsnu72.pfb
%{_fontdir}/gbsnu73.pfb
%{_fontdir}/gbsnu74.pfb
%{_fontdir}/gbsnu75.pfb
%{_fontdir}/gbsnu76.pfb
%{_fontdir}/gbsnu77.pfb
%{_fontdir}/gbsnu78.pfb
%{_fontdir}/gbsnu79.pfb
%{_fontdir}/gbsnu7a.pfb
%{_fontdir}/gbsnu7b.pfb
%{_fontdir}/gbsnu7c.pfb
%{_fontdir}/gbsnu7d.pfb
%{_fontdir}/gbsnu7e.pfb
%{_fontdir}/gbsnu7f.pfb
%{_fontdir}/gbsnu80.pfb
%{_fontdir}/gbsnu81.pfb
%{_fontdir}/gbsnu82.pfb
%{_fontdir}/gbsnu83.pfb
%{_fontdir}/gbsnu84.pfb
%{_fontdir}/gbsnu85.pfb
%{_fontdir}/gbsnu86.pfb
%{_fontdir}/gbsnu87.pfb
%{_fontdir}/gbsnu88.pfb
%{_fontdir}/gbsnu89.pfb
%{_fontdir}/gbsnu8a.pfb
%{_fontdir}/gbsnu8b.pfb
%{_fontdir}/gbsnu8c.pfb
%{_fontdir}/gbsnu8d.pfb
%{_fontdir}/gbsnu8e.pfb
%{_fontdir}/gbsnu8f.pfb
%{_fontdir}/gbsnu90.pfb
%{_fontdir}/gbsnu91.pfb
%{_fontdir}/gbsnu92.pfb
%{_fontdir}/gbsnu93.pfb
%{_fontdir}/gbsnu94.pfb
%{_fontdir}/gbsnu95.pfb
%{_fontdir}/gbsnu96.pfb
%{_fontdir}/gbsnu97.pfb
%{_fontdir}/gbsnu98.pfb
%{_fontdir}/gbsnu99.pfb
%{_fontdir}/gbsnu9a.pfb
%{_fontdir}/gbsnu9b.pfb
%{_fontdir}/gbsnu9c.pfb
%{_fontdir}/gbsnu9e.pfb
%{_fontdir}/gbsnu9f.pfb
%{_fontdir}/gbsnufe.pfb
%{_fontdir}/gbsnuff.pfb
%{_fontdir}/gkaiu00.pfb
%{_fontdir}/gkaiu01.pfb
%{_fontdir}/gkaiu02.pfb
%{_fontdir}/gkaiu03.pfb
%{_fontdir}/gkaiu04.pfb
%{_fontdir}/gkaiu20.pfb
%{_fontdir}/gkaiu21.pfb
%{_fontdir}/gkaiu22.pfb
%{_fontdir}/gkaiu23.pfb
%{_fontdir}/gkaiu24.pfb
%{_fontdir}/gkaiu25.pfb
%{_fontdir}/gkaiu26.pfb
%{_fontdir}/gkaiu30.pfb
%{_fontdir}/gkaiu31.pfb
%{_fontdir}/gkaiu32.pfb
%{_fontdir}/gkaiu4e.pfb
%{_fontdir}/gkaiu4f.pfb
%{_fontdir}/gkaiu50.pfb
%{_fontdir}/gkaiu51.pfb
%{_fontdir}/gkaiu52.pfb
%{_fontdir}/gkaiu53.pfb
%{_fontdir}/gkaiu54.pfb
%{_fontdir}/gkaiu55.pfb
%{_fontdir}/gkaiu56.pfb
%{_fontdir}/gkaiu57.pfb
%{_fontdir}/gkaiu58.pfb
%{_fontdir}/gkaiu59.pfb
%{_fontdir}/gkaiu5a.pfb
%{_fontdir}/gkaiu5b.pfb
%{_fontdir}/gkaiu5c.pfb
%{_fontdir}/gkaiu5d.pfb
%{_fontdir}/gkaiu5e.pfb
%{_fontdir}/gkaiu5f.pfb
%{_fontdir}/gkaiu60.pfb
%{_fontdir}/gkaiu61.pfb
%{_fontdir}/gkaiu62.pfb
%{_fontdir}/gkaiu63.pfb
%{_fontdir}/gkaiu64.pfb
%{_fontdir}/gkaiu65.pfb
%{_fontdir}/gkaiu66.pfb
%{_fontdir}/gkaiu67.pfb
%{_fontdir}/gkaiu68.pfb
%{_fontdir}/gkaiu69.pfb
%{_fontdir}/gkaiu6a.pfb
%{_fontdir}/gkaiu6b.pfb
%{_fontdir}/gkaiu6c.pfb
%{_fontdir}/gkaiu6d.pfb
%{_fontdir}/gkaiu6e.pfb
%{_fontdir}/gkaiu6f.pfb
%{_fontdir}/gkaiu70.pfb
%{_fontdir}/gkaiu71.pfb
%{_fontdir}/gkaiu72.pfb
%{_fontdir}/gkaiu73.pfb
%{_fontdir}/gkaiu74.pfb
%{_fontdir}/gkaiu75.pfb
%{_fontdir}/gkaiu76.pfb
%{_fontdir}/gkaiu77.pfb
%{_fontdir}/gkaiu78.pfb
%{_fontdir}/gkaiu79.pfb
%{_fontdir}/gkaiu7a.pfb
%{_fontdir}/gkaiu7b.pfb
%{_fontdir}/gkaiu7c.pfb
%{_fontdir}/gkaiu7d.pfb
%{_fontdir}/gkaiu7e.pfb
%{_fontdir}/gkaiu7f.pfb
%{_fontdir}/gkaiu80.pfb
%{_fontdir}/gkaiu81.pfb
%{_fontdir}/gkaiu82.pfb
%{_fontdir}/gkaiu83.pfb
%{_fontdir}/gkaiu84.pfb
%{_fontdir}/gkaiu85.pfb
%{_fontdir}/gkaiu86.pfb
%{_fontdir}/gkaiu87.pfb
%{_fontdir}/gkaiu88.pfb
%{_fontdir}/gkaiu89.pfb
%{_fontdir}/gkaiu8a.pfb
%{_fontdir}/gkaiu8b.pfb
%{_fontdir}/gkaiu8c.pfb
%{_fontdir}/gkaiu8d.pfb
%{_fontdir}/gkaiu8e.pfb
%{_fontdir}/gkaiu8f.pfb
%{_fontdir}/gkaiu90.pfb
%{_fontdir}/gkaiu91.pfb
%{_fontdir}/gkaiu92.pfb
%{_fontdir}/gkaiu93.pfb
%{_fontdir}/gkaiu94.pfb
%{_fontdir}/gkaiu95.pfb
%{_fontdir}/gkaiu96.pfb
%{_fontdir}/gkaiu97.pfb
%{_fontdir}/gkaiu98.pfb
%{_fontdir}/gkaiu99.pfb
%{_fontdir}/gkaiu9a.pfb
%{_fontdir}/gkaiu9b.pfb
%{_fontdir}/gkaiu9c.pfb
%{_fontdir}/gkaiu9e.pfb
%{_fontdir}/gkaiu9f.pfb
%{_fontdir}/gkaiufe.pfb
%{_fontdir}/gkaiuff.pfb

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
