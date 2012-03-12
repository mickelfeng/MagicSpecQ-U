%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/venturisadf.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/venturisadf.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/venturisadf.source.tar.xz

Name: texlive-venturisadf
License: Freely redistributable without restriction
Summary: Venturis ADF fonts collection
Version: %{tl_version}
Release: %{tl_noarch_release}.1.005.svn19444%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(venturis.sty)
Provides: tex(venturis2.sty)
Provides: tex(venturisold.sty)
Requires: tex(xkeyval.sty)
Requires: tex(fontenc.sty)
Requires: tex(textcomp.sty)
Requires: tex(nfssext-cfr.sty)
Requires: texlive-venturisadf-fedora-fonts = %{tl_version}

%description
Serif and sans serif complete text font families, in both Adobe
Type 1 and OpenType formats for publication. The family is
based on Utopia family, and has been modified and developed by
the Arkandis Digital foundry. Support for using the fonts, in
LaTeX, is also provided (and makes use of the nfssext-cfr
package).

date: 2010-07-12 22:26:03 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map yv1.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map yv2.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map yv3.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map yvo.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map yvt.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map yv1.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map yv2.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map yv3.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map yvo.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map yvt.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for venturisadf
Version: %{tl_version}
Release: %{tl_noarch_release}.1.005.svn19444%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for venturisadf

%package fedora-fonts
Summary: Fonts for venturisadf
Version: %{tl_version}
Release: %{tl_noarch_release}.1.005.svn19444%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-venturisadf = %{tl_version}
BuildArch: noarch

%description fedora-fonts
Serif and sans serif complete text font families, in both Adobe
Type 1 and OpenType formats for publication. The family is
based on Utopia family, and has been modified and developed by
the Arkandis Digital foundry. Support for using the fonts, in
LaTeX, is also provided (and makes use of the nfssext-cfr
package).

date: 2010-07-12 22:26:03 +0200


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtb8a.pfb .
ln -s %{_fontdir}/yvtb8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtb8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtb8ac.pfb .
ln -s %{_fontdir}/yvtb8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtb8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbc8a.pfb .
ln -s %{_fontdir}/yvtbc8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbc8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbc8ac.pfb .
ln -s %{_fontdir}/yvtbc8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbc8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbci8a.pfb .
ln -s %{_fontdir}/yvtbci8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbci8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbci8ac.pfb .
ln -s %{_fontdir}/yvtbci8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbci8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbd8ac.pfb .
ln -s %{_fontdir}/yvtbd8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbd8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbi8a.pfb .
ln -s %{_fontdir}/yvtbi8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbi8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbi8ac.pfb .
ln -s %{_fontdir}/yvtbi8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbi8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvth8a.pfb .
ln -s %{_fontdir}/yvth8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvth8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvthi8a.pfb .
ln -s %{_fontdir}/yvthi8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvthi8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtr8a.pfb .
ln -s %{_fontdir}/yvtr8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtr8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtr8ac.pfb .
ln -s %{_fontdir}/yvtr8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtr8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtrc8a.pfb .
ln -s %{_fontdir}/yvtrc8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtrc8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtrc8ac.pfb .
ln -s %{_fontdir}/yvtrc8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtrc8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtrci8a.pfb .
ln -s %{_fontdir}/yvtrci8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtrci8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtrci8ac.pfb .
ln -s %{_fontdir}/yvtrci8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtrci8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtrdl8a.pfb .
ln -s %{_fontdir}/yvtrdl8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtrdl8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtri8a.pfb .
ln -s %{_fontdir}/yvtri8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtri8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtri8ac.pfb .
ln -s %{_fontdir}/yvtri8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtri8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2b8a.pfb .
ln -s %{_fontdir}/yv2b8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2b8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2b8ac.pfb .
ln -s %{_fontdir}/yv2b8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2b8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2bi8a.pfb .
ln -s %{_fontdir}/yv2bi8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2bi8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2bi8ac.pfb .
ln -s %{_fontdir}/yv2bi8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2bi8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2m8a.pfb .
ln -s %{_fontdir}/yv2m8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2m8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2mi8a.pfb .
ln -s %{_fontdir}/yv2mi8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2mi8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2r8a.pfb .
ln -s %{_fontdir}/yv2r8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2r8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2r8ac.pfb .
ln -s %{_fontdir}/yv2r8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2r8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2ri8a.pfb .
ln -s %{_fontdir}/yv2ri8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2ri8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2ri8ac.pfb .
ln -s %{_fontdir}/yv2ri8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2ri8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2x8a.pfb .
ln -s %{_fontdir}/yv2x8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2x8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2xi8a.pfb .
ln -s %{_fontdir}/yv2xi8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2xi8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturisold/yvob8a.pfb .
ln -s %{_fontdir}/yvob8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturisold/yvob8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturisold/yvobi8a.pfb .
ln -s %{_fontdir}/yvobi8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturisold/yvobi8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturisold/yvodd8a.pfb .
ln -s %{_fontdir}/yvodd8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturisold/yvodd8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturisold/yvor8a.pfb .
ln -s %{_fontdir}/yvor8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturisold/yvor8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturisold/yvori8a.pfb .
ln -s %{_fontdir}/yvori8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturisold/yvori8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1b8a.pfb .
ln -s %{_fontdir}/yv1b8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1b8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1b8ac.pfb .
ln -s %{_fontdir}/yv1b8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1b8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1b8ax.pfb .
ln -s %{_fontdir}/yv1b8ax.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1b8ax.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1bd8a.pfb .
ln -s %{_fontdir}/yv1bd8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1bd8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1bi8a.pfb .
ln -s %{_fontdir}/yv1bi8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1bi8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1bi8ac.pfb .
ln -s %{_fontdir}/yv1bi8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1bi8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1bi8ax.pfb .
ln -s %{_fontdir}/yv1bi8ax.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1bi8ax.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1d8a.pfb .
ln -s %{_fontdir}/yv1d8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1d8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1dd8au.pfb .
ln -s %{_fontdir}/yv1dd8au.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1dd8au.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1di8a.pfb .
ln -s %{_fontdir}/yv1di8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1di8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1h8a.pfb .
ln -s %{_fontdir}/yv1h8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1h8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1ho8a.pfb .
ln -s %{_fontdir}/yv1ho8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1ho8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1l8a.pfb .
ln -s %{_fontdir}/yv1l8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1l8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1li8a.pfb .
ln -s %{_fontdir}/yv1li8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1li8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1r8a.pfb .
ln -s %{_fontdir}/yv1r8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1r8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1r8ac.pfb .
ln -s %{_fontdir}/yv1r8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1r8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1r8ax.pfb .
ln -s %{_fontdir}/yv1r8ax.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1r8ax.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1ri8a.pfb .
ln -s %{_fontdir}/yv1ri8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1ri8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1ri8ac.pfb .
ln -s %{_fontdir}/yv1ri8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1ri8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1ri8ax.pfb .
ln -s %{_fontdir}/yv1ri8ax.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1ri8ax.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3b8a.pfb .
ln -s %{_fontdir}/yv3b8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3b8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3b8ac.pfb .
ln -s %{_fontdir}/yv3b8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3b8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3b8ax.pfb .
ln -s %{_fontdir}/yv3b8ax.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3b8ax.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3bi8a.pfb .
ln -s %{_fontdir}/yv3bi8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3bi8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3bi8ac.pfb .
ln -s %{_fontdir}/yv3bi8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3bi8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3bi8ax.pfb .
ln -s %{_fontdir}/yv3bi8ax.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3bi8ax.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3r8a.pfb .
ln -s %{_fontdir}/yv3r8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3r8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3r8ac.pfb .
ln -s %{_fontdir}/yv3r8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3r8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3r8ax.pfb .
ln -s %{_fontdir}/yv3r8ax.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3r8ax.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3ri8a.pfb .
ln -s %{_fontdir}/yv3ri8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3ri8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3ri8ac.pfb .
ln -s %{_fontdir}/yv3ri8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3ri8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3ri8ax.pfb .
ln -s %{_fontdir}/yv3ri8ax.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3ri8ax.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis/yvtb8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis/yvtb8ac.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis/yvtbc8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis/yvtbc8ac.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis/yvtbci8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis/yvtbci8ac.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis/yvtbd8ac.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis/yvtbi8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis/yvtbi8ac.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis/yvth8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis/yvthi8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis/yvtr8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis/yvtr8ac.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis/yvtrc8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis/yvtrc8ac.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis/yvtrci8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis/yvtrci8ac.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis/yvtrdl8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis/yvtri8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis/yvtri8ac.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis2/yv2b8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis2/yv2b8ac.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis2/yv2bi8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis2/yv2bi8ac.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis2/yv2m8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis2/yv2mi8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis2/yv2r8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis2/yv2r8ac.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis2/yv2ri8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis2/yv2ri8ac.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis2/yv2x8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis2/yv2xi8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturisold/yvob8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturisold/yvobi8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturisold/yvodd8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturisold/yvor8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturisold/yvori8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans/yv1b8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans/yv1b8ac.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans/yv1b8ax.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans/yv1bd8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans/yv1bi8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans/yv1bi8ac.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans/yv1bi8ax.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans/yv1d8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans/yv1dd8au.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans/yv1di8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans/yv1h8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans/yv1ho8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans/yv1l8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans/yv1li8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans/yv1r8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans/yv1r8ac.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans/yv1r8ax.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans/yv1ri8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans/yv1ri8ac.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans/yv1ri8ax.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans2/yv3b8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans2/yv3b8ac.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans2/yv3b8ax.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans2/yv3bi8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans2/yv3bi8ac.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans2/yv3bi8ax.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans2/yv3r8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans2/yv3r8ac.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans2/yv3r8ax.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans2/yv3ri8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans2/yv3ri8ac.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans2/yv3ri8ax.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/venturisadf/t1-dotalt-f_f-venturisadf.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/venturisadf/t1-f_f-venturisadf.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/venturisadf/t1-venturis.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/venturisadf/t1-venturisold-longs.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/venturisadf/ts1-euro-venturisadf.enc
%{_texdir}/texmf-dist/fonts/map/dvips/venturis/yvt.map
%{_texdir}/texmf-dist/fonts/map/dvips/venturis2/yv2.map
%{_texdir}/texmf-dist/fonts/map/dvips/venturisold/yvo.map
%{_texdir}/texmf-dist/fonts/map/dvips/venturissans/yv1.map
%{_texdir}/texmf-dist/fonts/map/dvips/venturissans2/yv3.map
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1-yvtb-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1-yvtb.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1-yvtbc-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1-yvtbc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1-yvtbci-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1-yvtbci.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1-yvtbd-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1-yvtbi-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1-yvtbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1-yvth.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1-yvthi.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1-yvtr-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1-yvtr.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1-yvtrc-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1-yvtrc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1-yvtrci-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1-yvtrci.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1-yvtrdl.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1-yvtri-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1-yvtri.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1alt-yvtbc-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1alt-yvtbc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1alt-yvtbci-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1alt-yvtbci.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1alt-yvtrc-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1alt-yvtrc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1alt-yvtrci-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/t1alt-yvtrci.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/ts1-yvtb-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/ts1-yvtb.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/ts1-yvtbc-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/ts1-yvtbc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/ts1-yvtbci-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/ts1-yvtbci.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/ts1-yvtbd-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/ts1-yvtbi-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/ts1-yvtbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/ts1-yvth.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/ts1-yvthi.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/ts1-yvtr-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/ts1-yvtr.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/ts1-yvtrc-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/ts1-yvtrc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/ts1-yvtrci-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/ts1-yvtrci.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/ts1-yvtrdl.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/ts1-yvtri-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/ts1-yvtri.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/vent-yvtr.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtb8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtb8cc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtb8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtb8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbc8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbc8cc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbc8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbci8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbci8cc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbci8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbci8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbcij8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbcij8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbcijw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbcijw8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbciw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbciw8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbcj8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbcj8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbcjw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbcjw8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbcw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbcw8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbd8cc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbd8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbi8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbi8cc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbi8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbij8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbij8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbijw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbijw8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbiw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbiw8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbj8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbj8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbjw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbjw8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtbw8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvth8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvth8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvthi8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvthi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtr8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtr8cc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtr8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtr8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrajw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtraw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrc8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrc8cc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrc8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrci8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrci8cc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrci8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrci8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrcij8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrcij8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrcijw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrcijw8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrciw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrciw8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrcj8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrcj8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrcjw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrcjw8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrcw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrcw8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrdl8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrdl8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtri8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtri8cc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtri8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtri8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrij8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrij8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrijw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrijw8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtriw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtriw8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrj8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrj8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrjw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrjw8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis/yvtrw8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/t1-yv2b-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/t1-yv2b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/t1-yv2bi-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/t1-yv2bi.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/t1-yv2m.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/t1-yv2mi.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/t1-yv2r-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/t1-yv2r.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/t1-yv2ri-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/t1-yv2ri.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/t1-yv2x.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/t1-yv2xi.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/ts1-yv2b-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/ts1-yv2b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/ts1-yv2bi-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/ts1-yv2bi.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/ts1-yv2m.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/ts1-yv2mi.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/ts1-yv2r-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/ts1-yv2r.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/ts1-yv2ri-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/ts1-yv2ri.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/ts1-yv2x.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/ts1-yv2xi.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/yv2b8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/yv2b8cc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/yv2b8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/yv2b8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/yv2bi8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/yv2bi8cc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/yv2bi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/yv2bi8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/yv2m8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/yv2m8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/yv2mi8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/yv2mi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/yv2r8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/yv2r8cc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/yv2r8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/yv2r8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/yv2ri8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/yv2ri8cc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/yv2ri8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/yv2ri8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/yv2x8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/yv2x8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/yv2xi8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2/yv2xi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/t1-yvob.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/t1-yvobi.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/t1-yvodd.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/t1-yvor.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/t1-yvori.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/ts1-yvob.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/ts1-yvobi.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/ts1-yvodd.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/ts1-yvor.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/ts1-yvori.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/yvoab8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/yvoabi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/yvoar8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/yvoari8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/yvob8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/yvob8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/yvobi8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/yvobi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/yvodd8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/yvodd8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/yvor8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/yvor8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/yvori8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold/yvori8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/t1-yv1b-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/t1-yv1b-x.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/t1-yv1b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/t1-yv1bd.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/t1-yv1bi-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/t1-yv1bi-x.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/t1-yv1bi.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/t1-yv1d.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/t1-yv1dd-u.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/t1-yv1di.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/t1-yv1h.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/t1-yv1ho.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/t1-yv1l.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/t1-yv1li.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/t1-yv1r-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/t1-yv1r-x.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/t1-yv1r.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/t1-yv1ri-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/t1-yv1ri-x.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/t1-yv1ri.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/ts1-yv1b-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/ts1-yv1b-x.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/ts1-yv1b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/ts1-yv1bd.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/ts1-yv1bi-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/ts1-yv1bi-x.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/ts1-yv1bi.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/ts1-yv1d.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/ts1-yv1dd-u.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/ts1-yv1di.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/ts1-yv1h.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/ts1-yv1ho.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/ts1-yv1l.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/ts1-yv1li.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/ts1-yv1r-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/ts1-yv1r-x.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/ts1-yv1r.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/ts1-yv1ri-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/ts1-yv1ri-x.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/ts1-yv1ri.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1b8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1b8cc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1b8cx.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1b8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1b8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1b8tx.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1bd8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1bd8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1bi8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1bi8cc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1bi8cx.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1bi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1bi8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1bi8tx.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1d8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1d8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1dd8cu.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1dd8tu.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1di8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1di8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1h8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1h8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1ho8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1ho8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1l8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1l8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1li8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1li8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1r8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1r8cc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1r8cx.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1r8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1r8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1r8tx.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1ri8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1ri8cc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1ri8cx.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1ri8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1ri8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans/yv1ri8tx.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/t1-yv3b-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/t1-yv3b-x.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/t1-yv3b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/t1-yv3bi-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/t1-yv3bi-x.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/t1-yv3bi.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/t1-yv3r-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/t1-yv3r-x.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/t1-yv3r.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/t1-yv3ri-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/t1-yv3ri-x.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/t1-yv3ri.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/ts1-yv3b-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/ts1-yv3b-x.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/ts1-yv3b.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/ts1-yv3bi-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/ts1-yv3bi-x.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/ts1-yv3bi.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/ts1-yv3r-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/ts1-yv3r-x.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/ts1-yv3r.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/ts1-yv3ri-c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/ts1-yv3ri-x.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/ts1-yv3ri.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/yv3b8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/yv3b8cc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/yv3b8cx.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/yv3b8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/yv3b8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/yv3b8tx.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/yv3bi8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/yv3bi8cc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/yv3bi8cx.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/yv3bi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/yv3bi8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/yv3bi8tx.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/yv3r8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/yv3r8cc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/yv3r8cx.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/yv3r8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/yv3r8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/yv3r8tx.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/yv3ri8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/yv3ri8cc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/yv3ri8cx.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/yv3ri8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/yv3ri8tc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2/yv3ri8tx.tfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtb8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtb8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtb8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtb8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbc8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbc8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbc8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbc8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbci8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbci8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbci8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbci8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbd8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbd8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbi8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbi8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbi8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtbi8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvth8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvth8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvthi8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvthi8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtr8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtr8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtr8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtr8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtrc8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtrc8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtrc8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtrc8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtrci8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtrci8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtrci8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtrci8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtrdl8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtrdl8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtri8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtri8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtri8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis/yvtri8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2b8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2b8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2b8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2b8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2bi8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2bi8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2bi8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2bi8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2m8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2m8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2mi8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2mi8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2r8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2r8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2r8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2r8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2ri8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2ri8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2ri8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2ri8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2x8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2x8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2xi8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2/yv2xi8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturisold/yvob8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturisold/yvob8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturisold/yvobi8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturisold/yvobi8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturisold/yvodd8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturisold/yvodd8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturisold/yvor8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturisold/yvor8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturisold/yvori8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturisold/yvori8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1b8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1b8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1b8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1b8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1b8ax.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1b8ax.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1bd8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1bd8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1bi8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1bi8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1bi8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1bi8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1bi8ax.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1bi8ax.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1d8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1d8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1dd8au.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1dd8au.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1di8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1di8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1h8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1h8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1ho8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1ho8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1l8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1l8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1li8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1li8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1r8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1r8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1r8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1r8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1r8ax.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1r8ax.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1ri8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1ri8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1ri8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1ri8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1ri8ax.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans/yv1ri8ax.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3b8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3b8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3b8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3b8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3b8ax.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3b8ax.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3bi8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3bi8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3bi8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3bi8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3bi8ax.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3bi8ax.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3r8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3r8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3r8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3r8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3r8ax.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3r8ax.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3ri8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3ri8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3ri8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3ri8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3ri8ax.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2/yv3ri8ax.pfm
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtb8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtb8cc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtb8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtb8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbc8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbc8cc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbc8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbc8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbci8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbci8cc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbci8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbci8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbcij8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbcij8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbcijw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbcijw8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbciw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbciw8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbcj8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbcj8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbcjw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbcjw8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbcw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbcw8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbd8cc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbd8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbi8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbi8cc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbi8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbi8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbij8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbij8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbijw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbijw8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbiw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbiw8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbj8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbj8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbjw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbjw8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtbw8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvth8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvth8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvthi8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvthi8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtr8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtr8cc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtr8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtr8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrajw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtraw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrc8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrc8cc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrc8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrc8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrci8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrci8cc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrci8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrci8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrcij8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrcij8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrcijw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrcijw8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrciw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrciw8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrcj8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrcj8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrcjw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrcjw8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrcw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrcw8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrdl8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrdl8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtri8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtri8cc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtri8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtri8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrij8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrij8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrijw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrijw8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtriw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtriw8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrj8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrj8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrjw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrjw8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis/yvtrw8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/yv2b8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/yv2b8cc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/yv2b8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/yv2b8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/yv2bi8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/yv2bi8cc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/yv2bi8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/yv2bi8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/yv2m8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/yv2m8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/yv2mi8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/yv2mi8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/yv2r8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/yv2r8cc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/yv2r8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/yv2r8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/yv2ri8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/yv2ri8cc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/yv2ri8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/yv2ri8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/yv2x8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/yv2x8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/yv2xi8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2/yv2xi8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturisold/yvoab8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturisold/yvoabi8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturisold/yvoar8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturisold/yvoari8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturisold/yvob8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturisold/yvob8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturisold/yvobi8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturisold/yvobi8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturisold/yvodd8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturisold/yvodd8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturisold/yvor8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturisold/yvor8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturisold/yvori8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturisold/yvori8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1b8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1b8cc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1b8cx.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1b8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1b8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1b8tx.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1bd8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1bd8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1bi8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1bi8cc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1bi8cx.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1bi8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1bi8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1bi8tx.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1d8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1d8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1dd8cu.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1dd8tu.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1di8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1di8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1h8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1h8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1ho8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1ho8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1l8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1l8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1li8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1li8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1r8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1r8cc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1r8cx.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1r8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1r8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1r8tx.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1ri8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1ri8cc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1ri8cx.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1ri8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1ri8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans/yv1ri8tx.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/yv3b8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/yv3b8cc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/yv3b8cx.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/yv3b8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/yv3b8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/yv3b8tx.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/yv3bi8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/yv3bi8cc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/yv3bi8cx.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/yv3bi8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/yv3bi8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/yv3bi8tx.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/yv3r8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/yv3r8cc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/yv3r8cx.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/yv3r8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/yv3r8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/yv3r8tx.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/yv3ri8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/yv3ri8cc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/yv3ri8cx.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/yv3ri8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/yv3ri8tc.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2/yv3ri8tx.vf
%{_texdir}/texmf-dist/tex/latex/venturis/t1yvt.fd
%{_texdir}/texmf-dist/tex/latex/venturis/t1yvtajw.fd
%{_texdir}/texmf-dist/tex/latex/venturis/t1yvtaw.fd
%{_texdir}/texmf-dist/tex/latex/venturis/t1yvtd.fd
%{_texdir}/texmf-dist/tex/latex/venturis/t1yvtj.fd
%{_texdir}/texmf-dist/tex/latex/venturis/t1yvtjw.fd
%{_texdir}/texmf-dist/tex/latex/venturis/t1yvtw.fd
%{_texdir}/texmf-dist/tex/latex/venturis/ts1yvt.fd
%{_texdir}/texmf-dist/tex/latex/venturis/ts1yvtajw.fd
%{_texdir}/texmf-dist/tex/latex/venturis/ts1yvtaw.fd
%{_texdir}/texmf-dist/tex/latex/venturis/ts1yvtd.fd
%{_texdir}/texmf-dist/tex/latex/venturis/ts1yvtj.fd
%{_texdir}/texmf-dist/tex/latex/venturis/ts1yvtjw.fd
%{_texdir}/texmf-dist/tex/latex/venturis/ts1yvtw.fd
%{_texdir}/texmf-dist/tex/latex/venturis2/t1yv2.fd
%{_texdir}/texmf-dist/tex/latex/venturis2/ts1yv2.fd
%{_texdir}/texmf-dist/tex/latex/venturisadf/venturis.sty
%{_texdir}/texmf-dist/tex/latex/venturisadf/venturis2.sty
%{_texdir}/texmf-dist/tex/latex/venturisadf/venturisold.sty
%{_texdir}/texmf-dist/tex/latex/venturisold/t1yvo.fd
%{_texdir}/texmf-dist/tex/latex/venturisold/t1yvoa.fd
%{_texdir}/texmf-dist/tex/latex/venturisold/t1yvoad.fd
%{_texdir}/texmf-dist/tex/latex/venturisold/t1yvod.fd
%{_texdir}/texmf-dist/tex/latex/venturisold/ts1yvo.fd
%{_texdir}/texmf-dist/tex/latex/venturisold/ts1yvoa.fd
%{_texdir}/texmf-dist/tex/latex/venturisold/ts1yvoad.fd
%{_texdir}/texmf-dist/tex/latex/venturisold/ts1yvod.fd
%{_texdir}/texmf-dist/tex/latex/venturissans/t1yv1.fd
%{_texdir}/texmf-dist/tex/latex/venturissans/t1yv1d.fd
%{_texdir}/texmf-dist/tex/latex/venturissans/ts1yv1.fd
%{_texdir}/texmf-dist/tex/latex/venturissans/ts1yv1d.fd
%{_texdir}/texmf-dist/tex/latex/venturissans2/t1yv3.fd
%{_texdir}/texmf-dist/tex/latex/venturissans2/ts1yv3.fd

%files doc
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/doc/fonts/venturisadf/LICENSE-utopia.txt
%{_texdir}/texmf-dist/doc/fonts/venturisadf/LIST-Venturis.txt
%{_texdir}/texmf-dist/doc/fonts/venturisadf/README
%{_texdir}/texmf-dist/doc/fonts/venturisadf/manifest.txt
%{_texdir}/texmf-dist/doc/fonts/venturisadf/venturisadf.pdf
%{_texdir}/texmf-dist/doc/fonts/venturisadf/venturisadf.tex

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/yvtb8a.pfb
%{_fontdir}/yvtb8ac.pfb
%{_fontdir}/yvtbc8a.pfb
%{_fontdir}/yvtbc8ac.pfb
%{_fontdir}/yvtbci8a.pfb
%{_fontdir}/yvtbci8ac.pfb
%{_fontdir}/yvtbd8ac.pfb
%{_fontdir}/yvtbi8a.pfb
%{_fontdir}/yvtbi8ac.pfb
%{_fontdir}/yvth8a.pfb
%{_fontdir}/yvthi8a.pfb
%{_fontdir}/yvtr8a.pfb
%{_fontdir}/yvtr8ac.pfb
%{_fontdir}/yvtrc8a.pfb
%{_fontdir}/yvtrc8ac.pfb
%{_fontdir}/yvtrci8a.pfb
%{_fontdir}/yvtrci8ac.pfb
%{_fontdir}/yvtrdl8a.pfb
%{_fontdir}/yvtri8a.pfb
%{_fontdir}/yvtri8ac.pfb
%{_fontdir}/yv2b8a.pfb
%{_fontdir}/yv2b8ac.pfb
%{_fontdir}/yv2bi8a.pfb
%{_fontdir}/yv2bi8ac.pfb
%{_fontdir}/yv2m8a.pfb
%{_fontdir}/yv2mi8a.pfb
%{_fontdir}/yv2r8a.pfb
%{_fontdir}/yv2r8ac.pfb
%{_fontdir}/yv2ri8a.pfb
%{_fontdir}/yv2ri8ac.pfb
%{_fontdir}/yv2x8a.pfb
%{_fontdir}/yv2xi8a.pfb
%{_fontdir}/yvob8a.pfb
%{_fontdir}/yvobi8a.pfb
%{_fontdir}/yvodd8a.pfb
%{_fontdir}/yvor8a.pfb
%{_fontdir}/yvori8a.pfb
%{_fontdir}/yv1b8a.pfb
%{_fontdir}/yv1b8ac.pfb
%{_fontdir}/yv1b8ax.pfb
%{_fontdir}/yv1bd8a.pfb
%{_fontdir}/yv1bi8a.pfb
%{_fontdir}/yv1bi8ac.pfb
%{_fontdir}/yv1bi8ax.pfb
%{_fontdir}/yv1d8a.pfb
%{_fontdir}/yv1dd8au.pfb
%{_fontdir}/yv1di8a.pfb
%{_fontdir}/yv1h8a.pfb
%{_fontdir}/yv1ho8a.pfb
%{_fontdir}/yv1l8a.pfb
%{_fontdir}/yv1li8a.pfb
%{_fontdir}/yv1r8a.pfb
%{_fontdir}/yv1r8ac.pfb
%{_fontdir}/yv1r8ax.pfb
%{_fontdir}/yv1ri8a.pfb
%{_fontdir}/yv1ri8ac.pfb
%{_fontdir}/yv1ri8ax.pfb
%{_fontdir}/yv3b8a.pfb
%{_fontdir}/yv3b8ac.pfb
%{_fontdir}/yv3b8ax.pfb
%{_fontdir}/yv3bi8a.pfb
%{_fontdir}/yv3bi8ac.pfb
%{_fontdir}/yv3bi8ax.pfb
%{_fontdir}/yv3r8a.pfb
%{_fontdir}/yv3r8ac.pfb
%{_fontdir}/yv3r8ax.pfb
%{_fontdir}/yv3ri8a.pfb
%{_fontdir}/yv3ri8ac.pfb
%{_fontdir}/yv3ri8ax.pfb

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
