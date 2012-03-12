%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/vntex.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/vntex.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/vntex.source.tar.xz

Name: texlive-vntex
License: Freely redistributable without restriction
Summary: Support for Vietnamese
Version: %{tl_version}
Release: %{tl_noarch_release}.3.2.svn18845%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(dblaccnt.sty)
Provides: tex(swpvntex.sty)
Provides: tex(varioref-vi.sty)
Provides: tex(vietnam.sty)
Provides: tex(vietnamese.sty)
Provides: tex(vntex.sty)
Requires: tex(ifthen.sty)
Requires: tex(ucs.sty)
Requires: tex(ifpdf.sty)
Requires: tex(cmap.sty)
Requires: tex(fontenc.sty)
Requires: tex(inputenc.sty)
Requires: texlive-vntex-fedora-fonts = %{tl_version}

%description
The vntex bundle provides fonts, Plain TeX, texinfo and LaTeX
macros for typesetting documents in Vietnamese. Users of the
fonts (in both MetaFont and Adobe Type 1 format) of this bundle
may alternatively use the lm fonts bundle, for which map files
are available to provide a Vietnamese version.

date: 2010-06-09 11:52:21 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map arevvn.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map chartervn.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map cmbrightvn.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map concretevn.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map grotesqvn.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map txttvn.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map urwvn.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "MixedMap vnrother.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "MixedMap vnrtext.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map vntopia.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map arevvn.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map chartervn.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map cmbrightvn.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map concretevn.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map grotesqvn.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map txttvn.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map urwvn.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^MixedMap vnrother.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^MixedMap vnrtext.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map vntopia.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for vntex
Version: %{tl_version}
Release: %{tl_noarch_release}.3.2.svn18845%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for vntex

%package fedora-fonts
Summary: Fonts for vntex
Version: %{tl_version}
Release: %{tl_noarch_release}.3.2.svn18845%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-vntex = %{tl_version}
BuildArch: noarch

%description fedora-fonts
The vntex bundle provides fonts, Plain TeX, texinfo and LaTeX
macros for typesetting documents in Vietnamese. Users of the
fonts (in both MetaFont and Adobe Type 1 format) of this bundle
may alternatively use the lm fonts bundle, for which map files
are available to provide a Vietnamese version.

date: 2010-06-09 11:52:21 +0200


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/arevvn/ArevSans-Bold-T5.pfb .
ln -s %{_fontdir}/ArevSans-Bold-T5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/arevvn/ArevSans-Bold-T5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/arevvn/ArevSans-BoldOblique-T5.pfb .
ln -s %{_fontdir}/ArevSans-BoldOblique-T5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/arevvn/ArevSans-BoldOblique-T5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/arevvn/ArevSans-Oblique-T5.pfb .
ln -s %{_fontdir}/ArevSans-Oblique-T5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/arevvn/ArevSans-Oblique-T5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/arevvn/ArevSans-Roman-T5.pfb .
ln -s %{_fontdir}/ArevSans-Roman-T5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/arevvn/ArevSans-Roman-T5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/chartervn/bchb8v.pfb .
ln -s %{_fontdir}/bchb8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/chartervn/bchb8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/chartervn/bchbi8v.pfb .
ln -s %{_fontdir}/bchbi8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/chartervn/bchbi8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/chartervn/bchr8v.pfb .
ln -s %{_fontdir}/bchr8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/chartervn/bchr8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/chartervn/bchri8v.pfb .
ln -s %{_fontdir}/bchri8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/chartervn/bchri8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbr10.pfb .
ln -s %{_fontdir}/vncmbr10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbr10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbr17.pfb .
ln -s %{_fontdir}/vncmbr17.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbr17.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbr8.pfb .
ln -s %{_fontdir}/vncmbr8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbr8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbr9.pfb .
ln -s %{_fontdir}/vncmbr9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbr9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbrbx10.pfb .
ln -s %{_fontdir}/vncmbrbx10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbrbx10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbrsl10.pfb .
ln -s %{_fontdir}/vncmbrsl10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbrsl10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbrsl17.pfb .
ln -s %{_fontdir}/vncmbrsl17.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbrsl17.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbrsl8.pfb .
ln -s %{_fontdir}/vncmbrsl8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbrsl8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbrsl9.pfb .
ln -s %{_fontdir}/vncmbrsl9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbrsl9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmsltl10.pfb .
ln -s %{_fontdir}/vncmsltl10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmsltl10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmtl10.pfb .
ln -s %{_fontdir}/vncmtl10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmtl10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/concretevn/CMConcrete8v.pfb .
ln -s %{_fontdir}/CMConcrete8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/concretevn/CMConcrete8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/concretevn/CMConcreteItalic8v.pfb .
ln -s %{_fontdir}/CMConcreteItalic8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/concretevn/CMConcreteItalic8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/concretevn/CMConcreteSlanted8v.pfb .
ln -s %{_fontdir}/CMConcreteSlanted8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/concretevn/CMConcreteSlanted8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/concretevn/CMConcreteSmallCaps8v.pfb .
ln -s %{_fontdir}/CMConcreteSmallCaps8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/concretevn/CMConcreteSmallCaps8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/grotesqvn/ugqb8v.pfb .
ln -s %{_fontdir}/ugqb8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/grotesqvn/ugqb8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/txttvn/txbtt8v.pfb .
ln -s %{_fontdir}/txbtt8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/txttvn/txbtt8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/txttvn/txbttsc8v.pfb .
ln -s %{_fontdir}/txbttsc8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/txttvn/txbttsc8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/txttvn/txtt8v.pfb .
ln -s %{_fontdir}/txtt8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/txttvn/txtt8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/txttvn/txttsc8v.pfb .
ln -s %{_fontdir}/txttsc8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/txttvn/txttsc8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/fplrc8v.pfb .
ln -s %{_fontdir}/fplrc8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/fplrc8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uagd8v.pfb .
ln -s %{_fontdir}/uagd8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uagd8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uagdo8v.pfb .
ln -s %{_fontdir}/uagdo8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uagdo8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uagk8v.pfb .
ln -s %{_fontdir}/uagk8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uagk8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uagko8v.pfb .
ln -s %{_fontdir}/uagko8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uagko8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/ubkd8v.pfb .
ln -s %{_fontdir}/ubkd8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/ubkd8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/ubkdi8v.pfb .
ln -s %{_fontdir}/ubkdi8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/ubkdi8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/ubkl8v.pfb .
ln -s %{_fontdir}/ubkl8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/ubkl8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/ubkli8v.pfb .
ln -s %{_fontdir}/ubkli8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/ubkli8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/ucrb8v.pfb .
ln -s %{_fontdir}/ucrb8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/ucrb8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/ucrbo8v.pfb .
ln -s %{_fontdir}/ucrbo8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/ucrbo8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/ucrr8v.pfb .
ln -s %{_fontdir}/ucrr8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/ucrr8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/ucrro8v.pfb .
ln -s %{_fontdir}/ucrro8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/ucrro8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uhvb8v.pfb .
ln -s %{_fontdir}/uhvb8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uhvb8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uhvbo8v.pfb .
ln -s %{_fontdir}/uhvbo8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uhvbo8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uhvr8v.pfb .
ln -s %{_fontdir}/uhvr8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uhvr8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uhvro8v.pfb .
ln -s %{_fontdir}/uhvro8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uhvro8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uncb8v.pfb .
ln -s %{_fontdir}/uncb8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uncb8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uncbi8v.pfb .
ln -s %{_fontdir}/uncbi8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uncbi8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uncr8v.pfb .
ln -s %{_fontdir}/uncr8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uncr8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uncri8v.pfb .
ln -s %{_fontdir}/uncri8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uncri8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uplb8v.pfb .
ln -s %{_fontdir}/uplb8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uplb8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uplbi8v.pfb .
ln -s %{_fontdir}/uplbi8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uplbi8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uplr8v.pfb .
ln -s %{_fontdir}/uplr8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uplr8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uplri8v.pfb .
ln -s %{_fontdir}/uplri8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uplri8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/utmb8v.pfb .
ln -s %{_fontdir}/utmb8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/utmb8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/utmbi8v.pfb .
ln -s %{_fontdir}/utmbi8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/utmbi8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/utmr8v.pfb .
ln -s %{_fontdir}/utmr8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/utmr8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/utmri8v.pfb .
ln -s %{_fontdir}/utmri8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/utmri8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uzcmi8v.pfb .
ln -s %{_fontdir}/uzcmi8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uzcmi8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnb10.pfb .
ln -s %{_fontdir}/vnb10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnb10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbx10.pfb .
ln -s %{_fontdir}/vnbx10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbx10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbx12.pfb .
ln -s %{_fontdir}/vnbx12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbx12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbx5.pfb .
ln -s %{_fontdir}/vnbx5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbx5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbx6.pfb .
ln -s %{_fontdir}/vnbx6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbx6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbx7.pfb .
ln -s %{_fontdir}/vnbx7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbx7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbx8.pfb .
ln -s %{_fontdir}/vnbx8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbx8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbx9.pfb .
ln -s %{_fontdir}/vnbx9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbx9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbxsl10.pfb .
ln -s %{_fontdir}/vnbxsl10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbxsl10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbxti10.pfb .
ln -s %{_fontdir}/vnbxti10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbxti10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vncsc10.pfb .
ln -s %{_fontdir}/vncsc10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vncsc10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vndunh10.pfb .
ln -s %{_fontdir}/vndunh10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vndunh10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnff10.pfb .
ln -s %{_fontdir}/vnff10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnff10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnfi10.pfb .
ln -s %{_fontdir}/vnfi10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnfi10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnfib8.pfb .
ln -s %{_fontdir}/vnfib8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnfib8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnitt10.pfb .
ln -s %{_fontdir}/vnitt10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnitt10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnr10.pfb .
ln -s %{_fontdir}/vnr10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnr10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnr12.pfb .
ln -s %{_fontdir}/vnr12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnr12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnr17.pfb .
ln -s %{_fontdir}/vnr17.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnr17.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnr5.pfb .
ln -s %{_fontdir}/vnr5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnr5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnr6.pfb .
ln -s %{_fontdir}/vnr6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnr6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnr7.pfb .
ln -s %{_fontdir}/vnr7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnr7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnr8.pfb .
ln -s %{_fontdir}/vnr8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnr8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnr9.pfb .
ln -s %{_fontdir}/vnr9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnr9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnsl10.pfb .
ln -s %{_fontdir}/vnsl10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnsl10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnsl12.pfb .
ln -s %{_fontdir}/vnsl12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnsl12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnsl8.pfb .
ln -s %{_fontdir}/vnsl8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnsl8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnsl9.pfb .
ln -s %{_fontdir}/vnsl9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnsl9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnsltt10.pfb .
ln -s %{_fontdir}/vnsltt10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnsltt10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnss10.pfb .
ln -s %{_fontdir}/vnss10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnss10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnss12.pfb .
ln -s %{_fontdir}/vnss12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnss12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnss17.pfb .
ln -s %{_fontdir}/vnss17.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnss17.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnss8.pfb .
ln -s %{_fontdir}/vnss8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnss8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnss9.pfb .
ln -s %{_fontdir}/vnss9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnss9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssbx10.pfb .
ln -s %{_fontdir}/vnssbx10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssbx10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssdc10.pfb .
ln -s %{_fontdir}/vnssdc10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssdc10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssi10.pfb .
ln -s %{_fontdir}/vnssi10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssi10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssi12.pfb .
ln -s %{_fontdir}/vnssi12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssi12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssi17.pfb .
ln -s %{_fontdir}/vnssi17.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssi17.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssi8.pfb .
ln -s %{_fontdir}/vnssi8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssi8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssi9.pfb .
ln -s %{_fontdir}/vnssi9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssi9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssq8.pfb .
ln -s %{_fontdir}/vnssq8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssq8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssqi8.pfb .
ln -s %{_fontdir}/vnssqi8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssqi8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vntcsc10.pfb .
ln -s %{_fontdir}/vntcsc10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vntcsc10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnti10.pfb .
ln -s %{_fontdir}/vnti10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnti10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnti12.pfb .
ln -s %{_fontdir}/vnti12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnti12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnti7.pfb .
ln -s %{_fontdir}/vnti7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnti7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnti8.pfb .
ln -s %{_fontdir}/vnti8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnti8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnti9.pfb .
ln -s %{_fontdir}/vnti9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnti9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vntt10.pfb .
ln -s %{_fontdir}/vntt10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vntt10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vntt12.pfb .
ln -s %{_fontdir}/vntt12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vntt12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vntt8.pfb .
ln -s %{_fontdir}/vntt8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vntt8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vntt9.pfb .
ln -s %{_fontdir}/vntt9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vntt9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnu10.pfb .
ln -s %{_fontdir}/vnu10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnu10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnvtt10.pfb .
ln -s %{_fontdir}/vnvtt10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnvtt10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vntopia/putb8v.pfb .
ln -s %{_fontdir}/putb8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vntopia/putb8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vntopia/putbi8v.pfb .
ln -s %{_fontdir}/putbi8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vntopia/putbi8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vntopia/putr8v.pfb .
ln -s %{_fontdir}/putr8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vntopia/putr8v.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vntopia/putri8v.pfb .
ln -s %{_fontdir}/putri8v.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vntopia/putri8v.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/fonts/afm/vntex/chartervn/bchb8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/chartervn/bchbi8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/chartervn/bchr8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/chartervn/bchri8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/grotesqvn/ugqb8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/fplrc8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/uagd8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/uagdo8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/uagk8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/uagko8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/ubkd8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/ubkdi8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/ubkl8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/ubkli8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/ucrb8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/ucrbo8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/ucrr8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/ucrro8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/uhvb8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/uhvbo8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/uhvr8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/uhvro8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/uncb8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/uncbi8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/uncr8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/uncri8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/uplb8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/uplbi8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/uplr8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/uplri8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/utmb8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/utmbi8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/utmr8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/utmri8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn/uzcmi8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/vntopia/putb8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/vntopia/putbi8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/vntopia/putr8v.afm
%{_texdir}/texmf-dist/fonts/afm/vntex/vntopia/putri8v.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/vntex/t5.enc
%{_texdir}/texmf-dist/fonts/enc/pdftex/vntex/t5d.enc
%{_texdir}/texmf-dist/fonts/enc/pdftex/vntex/t5uni.enc
%{_texdir}/texmf-dist/fonts/map/dvips/vntex/arevvn.map
%{_texdir}/texmf-dist/fonts/map/dvips/vntex/chartervn.map
%{_texdir}/texmf-dist/fonts/map/dvips/vntex/cmbrightvn.map
%{_texdir}/texmf-dist/fonts/map/dvips/vntex/concretevn.map
%{_texdir}/texmf-dist/fonts/map/dvips/vntex/grotesqvn.map
%{_texdir}/texmf-dist/fonts/map/dvips/vntex/txttvn.map
%{_texdir}/texmf-dist/fonts/map/dvips/vntex/urwvn.map
%{_texdir}/texmf-dist/fonts/map/dvips/vntex/vnrother.map
%{_texdir}/texmf-dist/fonts/map/dvips/vntex/vnrtext.map
%{_texdir}/texmf-dist/fonts/map/dvips/vntex/vntopia.map
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnaccent.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnacomp.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnb10.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnbase.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnbx10.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnbx12.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnbx5.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnbx6.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnbx7.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnbx8.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnbx9.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnbxsl10.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnbxti10.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vncligtb.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vncode.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vncombac.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vncsc.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vncsc10.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vndothook.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vndunh10.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnecomp.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnff10.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnfi10.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnfib8.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnicomp.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vniligtb.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnitt10.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnlacc.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnlai.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnlar.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnldi.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnldr.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnlei.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnler.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnlii.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnlir.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnloi.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnlor.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnlui.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnlur.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnlyi.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnlyr.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnminus.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnmligtb.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnocomp.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnr10.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnr12.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnr17.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnr5.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnr6.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnr7.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnr8.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnr9.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnrligtb.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnrm.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnroman.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnsl10.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnsl12.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnsl8.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnsl9.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnsltt10.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnss10.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnss12.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnss17.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnss8.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnss9.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnssbx10.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnssdc10.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnssi10.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnssi12.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnssi17.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnssi8.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnssi9.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnssq8.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnssqi8.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vntcsc10.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vntextit.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnti10.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnti12.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnti7.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnti8.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnti9.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vntt10.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vntt12.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vntt8.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vntt9.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnu10.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnuacc.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnuar.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnucomp.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnudr.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnuer.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnuir.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnuor.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnuur.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnuyr.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnvtt10.mf
%{_texdir}/texmf-dist/fonts/source/vntex/vnr/vnycomp.mf
%{_texdir}/texmf-dist/fonts/tfm/vntex/arevvn/favb8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/arevvn/favbi8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/arevvn/favr8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/arevvn/favri8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/chartervn/bchb8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/chartervn/bchbc8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/chartervn/bchbi8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/chartervn/bchbo8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/chartervn/bchr8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/chartervn/bchrc8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/chartervn/bchri8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/chartervn/bchro8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/cmbrightvn/vncmbr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/cmbrightvn/vncmbr17.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/cmbrightvn/vncmbr8.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/cmbrightvn/vncmbr9.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/cmbrightvn/vncmbrbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/cmbrightvn/vncmbrsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/cmbrightvn/vncmbrsl17.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/cmbrightvn/vncmbrsl8.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/cmbrightvn/vncmbrsl9.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/cmbrightvn/vncmsltl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/cmbrightvn/vncmtl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/concretevn/vncccsc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/concretevn/vnccr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/concretevn/vnccsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/concretevn/vnccti10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/grotesqvn/ugqb8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/grotesqvn/ugqbo8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/txttvn/txbtt8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/txttvn/txbttsc8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/txttvn/txbttsl8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/txttvn/txtt8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/txttvn/txttsc8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/txttvn/txttsl8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/fplrc8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uagd8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uagdc8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uagdo8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uagk8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uagkc8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uagko8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/ubkd8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/ubkdc8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/ubkdi8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/ubkdo8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/ubkl8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/ubklc8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/ubkli8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/ubklo8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/ucrb8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/ucrbc8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/ucrbo8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/ucrr8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/ucrrc8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/ucrro8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uhvb8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uhvbc8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uhvbo8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uhvr8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uhvrc8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uhvro8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uncb8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uncbc8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uncbi8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uncbo8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uncr8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uncrc8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uncri8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uncro8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uplb8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uplbc8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uplbi8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uplbo8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uplr8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uplrc8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uplri8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uplro8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/utmb8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/utmbc8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/utmbi8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/utmbo8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/utmr8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/utmrc8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/utmri8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/utmro8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn/uzcmi8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnbx12.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnbx5.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnbx6.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnbx7.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnbx8.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnbx9.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnbxsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnbxti10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vncsc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vndunh10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnff10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnfi10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnfib8.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnitt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnr12.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnr17.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnr5.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnr6.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnr7.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnr8.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnr9.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnsl12.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnsl8.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnsl9.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnsltt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnss10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnss12.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnss17.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnss8.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnss9.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnssbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnssdc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnssi10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnssi12.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnssi17.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnssi8.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnssi9.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnssq8.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnssqi8.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vntcsc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnti10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnti12.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnti7.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnti8.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnti9.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vntt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vntt12.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vntt8.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vntt9.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnu10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr/vnvtt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vntopia/putb8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vntopia/putbc8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vntopia/putbi8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vntopia/putbo8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vntopia/putr8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vntopia/putrc8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vntopia/putri8v.tfm
%{_texdir}/texmf-dist/fonts/tfm/vntex/vntopia/putro8v.tfm
%{_texdir}/texmf-dist/fonts/type1/vntex/arevvn/ArevSans-Bold-T5.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/arevvn/ArevSans-BoldOblique-T5.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/arevvn/ArevSans-Oblique-T5.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/arevvn/ArevSans-Roman-T5.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/chartervn/bchb8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/chartervn/bchbi8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/chartervn/bchr8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/chartervn/bchri8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbr10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbr17.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbr8.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbr9.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbrbx10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbrsl10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbrsl17.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbrsl8.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmbrsl9.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmsltl10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn/vncmtl10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/concretevn/CMConcrete8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/concretevn/CMConcreteItalic8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/concretevn/CMConcreteSlanted8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/concretevn/CMConcreteSmallCaps8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/grotesqvn/ugqb8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/txttvn/txbtt8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/txttvn/txbttsc8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/txttvn/txtt8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/txttvn/txttsc8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/fplrc8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uagd8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uagdo8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uagk8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uagko8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/ubkd8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/ubkdi8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/ubkl8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/ubkli8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/ucrb8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/ucrbo8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/ucrr8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/ucrro8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uhvb8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uhvbo8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uhvr8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uhvro8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uncb8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uncbi8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uncr8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uncri8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uplb8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uplbi8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uplr8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uplri8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/utmb8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/utmbi8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/utmr8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/utmri8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn/uzcmi8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnb10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbx10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbx12.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbx5.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbx6.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbx7.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbx8.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbx9.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbxsl10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnbxti10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vncsc10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vndunh10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnff10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnfi10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnfib8.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnitt10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnr10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnr12.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnr17.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnr5.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnr6.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnr7.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnr8.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnr9.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnsl10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnsl12.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnsl8.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnsl9.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnsltt10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnss10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnss12.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnss17.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnss8.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnss9.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssbx10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssdc10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssi10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssi12.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssi17.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssi8.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssi9.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssq8.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnssqi8.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vntcsc10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnti10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnti12.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnti7.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnti8.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnti9.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vntt10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vntt12.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vntt8.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vntt9.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnu10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vnr/vnvtt10.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vntopia/putb8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vntopia/putbi8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vntopia/putr8v.pfb
%{_texdir}/texmf-dist/fonts/type1/vntex/vntopia/putri8v.pfb
%{_texdir}/texmf-dist/fonts/vf/vntex/chartervn/bchbc8v.vf
%{_texdir}/texmf-dist/fonts/vf/vntex/chartervn/bchrc8v.vf
%{_texdir}/texmf-dist/fonts/vf/vntex/urwvn/uagdc8v.vf
%{_texdir}/texmf-dist/fonts/vf/vntex/urwvn/uagkc8v.vf
%{_texdir}/texmf-dist/fonts/vf/vntex/urwvn/ubkdc8v.vf
%{_texdir}/texmf-dist/fonts/vf/vntex/urwvn/ubklc8v.vf
%{_texdir}/texmf-dist/fonts/vf/vntex/urwvn/ucrbc8v.vf
%{_texdir}/texmf-dist/fonts/vf/vntex/urwvn/ucrrc8v.vf
%{_texdir}/texmf-dist/fonts/vf/vntex/urwvn/uhvbc8v.vf
%{_texdir}/texmf-dist/fonts/vf/vntex/urwvn/uhvrc8v.vf
%{_texdir}/texmf-dist/fonts/vf/vntex/urwvn/uncbc8v.vf
%{_texdir}/texmf-dist/fonts/vf/vntex/urwvn/uncrc8v.vf
%{_texdir}/texmf-dist/fonts/vf/vntex/urwvn/uplbc8v.vf
%{_texdir}/texmf-dist/fonts/vf/vntex/urwvn/uplrc8v.vf
%{_texdir}/texmf-dist/fonts/vf/vntex/urwvn/utmbc8v.vf
%{_texdir}/texmf-dist/fonts/vf/vntex/urwvn/utmrc8v.vf
%{_texdir}/texmf-dist/fonts/vf/vntex/vntopia/putbc8v.vf
%{_texdir}/texmf-dist/fonts/vf/vntex/vntopia/putrc8v.vf
%{_texdir}/texmf-dist/tex/latex/vntex/dblaccnt.sty
%{_texdir}/texmf-dist/tex/latex/vntex/mcviscii.def
%{_texdir}/texmf-dist/tex/latex/vntex/pd1supp.def
%{_texdir}/texmf-dist/tex/latex/vntex/swpvntex.sty
%{_texdir}/texmf-dist/tex/latex/vntex/t5bch.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5ccr.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5cmbr.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5cmdh.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5cmfib.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5cmfr.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5cmr.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5cmss.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5cmssq.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5cmtl.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5cmtt.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5cmvtt.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5enc.def
%{_texdir}/texmf-dist/tex/latex/vntex/t5enc.dfu
%{_texdir}/texmf-dist/tex/latex/vntex/t5fav.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5fnc.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5fpl.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5futs.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5mak.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5mdbch.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5mdput.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5mdugm.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5pag.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5pbk.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5pcr.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5phv.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5pnc.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5ppl.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5ptm.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5ptmom.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5put.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5pxr.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5txr.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5txtt.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5uag.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5ubk.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5ucr.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5ugq.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5uhv.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5unc.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5upl.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5utm.fd
%{_texdir}/texmf-dist/tex/latex/vntex/t5uzcm.fd
%{_texdir}/texmf-dist/tex/latex/vntex/tcvn.def
%{_texdir}/texmf-dist/tex/latex/vntex/varioref-vi.sty
%{_texdir}/texmf-dist/tex/latex/vntex/vietnam.ldf
%{_texdir}/texmf-dist/tex/latex/vntex/vietnam.sty
%{_texdir}/texmf-dist/tex/latex/vntex/vietnamese.ldf
%{_texdir}/texmf-dist/tex/latex/vntex/viscii.def
%{_texdir}/texmf-dist/tex/latex/vntex/vncaps.tex
%{_texdir}/texmf-dist/tex/latex/vntex/vntex.sty
%{_texdir}/texmf-dist/tex/latex/vntex/vps.def
%{_texdir}/texmf-dist/tex/plain/vntex/dblaccnt.tex
%{_texdir}/texmf-dist/tex/plain/vntex/t5code.tex
%{_texdir}/texmf-dist/tex/plain/vntex/vntexinfo.tex

%files doc
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/doc/generic/vntex/INSTALL
%{_texdir}/texmf-dist/doc/generic/vntex/ReleaseNotes.pdf
%{_texdir}/texmf-dist/doc/generic/vntex/vn-fonts-print.pdf
%{_texdir}/texmf-dist/doc/generic/vntex/vn-fonts.pdf
%{_texdir}/texmf-dist/doc/generic/vntex/vn-min-print.pdf
%{_texdir}/texmf-dist/doc/generic/vntex/vn-min.pdf
%{_texdir}/texmf-dist/doc/generic/vntex/vntex-man-print.pdf
%{_texdir}/texmf-dist/doc/generic/vntex/vntex-man.pdf
%{_texdir}/texmf-dist/doc/generic/vntex/vntex-print.pdf
%{_texdir}/texmf-dist/doc/generic/vntex/vntex-update-maps
%{_texdir}/texmf-dist/doc/generic/vntex/vntex.pdf

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/ArevSans-Bold-T5.pfb
%{_fontdir}/ArevSans-BoldOblique-T5.pfb
%{_fontdir}/ArevSans-Oblique-T5.pfb
%{_fontdir}/ArevSans-Roman-T5.pfb
%{_fontdir}/bchb8v.pfb
%{_fontdir}/bchbi8v.pfb
%{_fontdir}/bchr8v.pfb
%{_fontdir}/bchri8v.pfb
%{_fontdir}/vncmbr10.pfb
%{_fontdir}/vncmbr17.pfb
%{_fontdir}/vncmbr8.pfb
%{_fontdir}/vncmbr9.pfb
%{_fontdir}/vncmbrbx10.pfb
%{_fontdir}/vncmbrsl10.pfb
%{_fontdir}/vncmbrsl17.pfb
%{_fontdir}/vncmbrsl8.pfb
%{_fontdir}/vncmbrsl9.pfb
%{_fontdir}/vncmsltl10.pfb
%{_fontdir}/vncmtl10.pfb
%{_fontdir}/CMConcrete8v.pfb
%{_fontdir}/CMConcreteItalic8v.pfb
%{_fontdir}/CMConcreteSlanted8v.pfb
%{_fontdir}/CMConcreteSmallCaps8v.pfb
%{_fontdir}/ugqb8v.pfb
%{_fontdir}/txbtt8v.pfb
%{_fontdir}/txbttsc8v.pfb
%{_fontdir}/txtt8v.pfb
%{_fontdir}/txttsc8v.pfb
%{_fontdir}/fplrc8v.pfb
%{_fontdir}/uagd8v.pfb
%{_fontdir}/uagdo8v.pfb
%{_fontdir}/uagk8v.pfb
%{_fontdir}/uagko8v.pfb
%{_fontdir}/ubkd8v.pfb
%{_fontdir}/ubkdi8v.pfb
%{_fontdir}/ubkl8v.pfb
%{_fontdir}/ubkli8v.pfb
%{_fontdir}/ucrb8v.pfb
%{_fontdir}/ucrbo8v.pfb
%{_fontdir}/ucrr8v.pfb
%{_fontdir}/ucrro8v.pfb
%{_fontdir}/uhvb8v.pfb
%{_fontdir}/uhvbo8v.pfb
%{_fontdir}/uhvr8v.pfb
%{_fontdir}/uhvro8v.pfb
%{_fontdir}/uncb8v.pfb
%{_fontdir}/uncbi8v.pfb
%{_fontdir}/uncr8v.pfb
%{_fontdir}/uncri8v.pfb
%{_fontdir}/uplb8v.pfb
%{_fontdir}/uplbi8v.pfb
%{_fontdir}/uplr8v.pfb
%{_fontdir}/uplri8v.pfb
%{_fontdir}/utmb8v.pfb
%{_fontdir}/utmbi8v.pfb
%{_fontdir}/utmr8v.pfb
%{_fontdir}/utmri8v.pfb
%{_fontdir}/uzcmi8v.pfb
%{_fontdir}/vnb10.pfb
%{_fontdir}/vnbx10.pfb
%{_fontdir}/vnbx12.pfb
%{_fontdir}/vnbx5.pfb
%{_fontdir}/vnbx6.pfb
%{_fontdir}/vnbx7.pfb
%{_fontdir}/vnbx8.pfb
%{_fontdir}/vnbx9.pfb
%{_fontdir}/vnbxsl10.pfb
%{_fontdir}/vnbxti10.pfb
%{_fontdir}/vncsc10.pfb
%{_fontdir}/vndunh10.pfb
%{_fontdir}/vnff10.pfb
%{_fontdir}/vnfi10.pfb
%{_fontdir}/vnfib8.pfb
%{_fontdir}/vnitt10.pfb
%{_fontdir}/vnr10.pfb
%{_fontdir}/vnr12.pfb
%{_fontdir}/vnr17.pfb
%{_fontdir}/vnr5.pfb
%{_fontdir}/vnr6.pfb
%{_fontdir}/vnr7.pfb
%{_fontdir}/vnr8.pfb
%{_fontdir}/vnr9.pfb
%{_fontdir}/vnsl10.pfb
%{_fontdir}/vnsl12.pfb
%{_fontdir}/vnsl8.pfb
%{_fontdir}/vnsl9.pfb
%{_fontdir}/vnsltt10.pfb
%{_fontdir}/vnss10.pfb
%{_fontdir}/vnss12.pfb
%{_fontdir}/vnss17.pfb
%{_fontdir}/vnss8.pfb
%{_fontdir}/vnss9.pfb
%{_fontdir}/vnssbx10.pfb
%{_fontdir}/vnssdc10.pfb
%{_fontdir}/vnssi10.pfb
%{_fontdir}/vnssi12.pfb
%{_fontdir}/vnssi17.pfb
%{_fontdir}/vnssi8.pfb
%{_fontdir}/vnssi9.pfb
%{_fontdir}/vnssq8.pfb
%{_fontdir}/vnssqi8.pfb
%{_fontdir}/vntcsc10.pfb
%{_fontdir}/vnti10.pfb
%{_fontdir}/vnti12.pfb
%{_fontdir}/vnti7.pfb
%{_fontdir}/vnti8.pfb
%{_fontdir}/vnti9.pfb
%{_fontdir}/vntt10.pfb
%{_fontdir}/vntt12.pfb
%{_fontdir}/vntt8.pfb
%{_fontdir}/vntt9.pfb
%{_fontdir}/vnu10.pfb
%{_fontdir}/vnvtt10.pfb
%{_fontdir}/putb8v.pfb
%{_fontdir}/putbi8v.pfb
%{_fontdir}/putr8v.pfb
%{_fontdir}/putri8v.pfb

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
