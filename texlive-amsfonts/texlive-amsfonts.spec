%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/amsfonts.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/amsfonts.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/amsfonts.source.tar.xz

Name: texlive-amsfonts
License: OFSFLD
Summary: TeX fonts from the American Mathematical Society
Version: %{tl_version}
Release: %{tl_noarch_release}.3.0.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(amsfonts.sty)
Provides: tex(amssymb.sty)
Provides: tex(cmmib57.sty)
Provides: tex(eucal.sty)
Provides: tex(eufrak.sty)
Provides: tex(euscript.sty)
Requires: texlive-amsfonts-fedora-fonts = %{tl_version}

%description
An extended set of fonts for use in mathematics, including:
extra mathematical symbols; blackboard bold letters (uppercase
only); fraktur letters; subscript sizes of bold math italic and
bold Greek letters; subscript sizes of large symbols such as
sum and product; added sizes of the Computer Modern small caps
font; cyrillic fonts (from the University of Washington); Euler
mathematical fonts. All fonts are provided as Adobe Type 1
files, and all except the Euler fonts are provided as MetaFont
source. The distribution also includes the canonical Type 1
versions of the Computer Modern family of fonts. Plain TeX and
LaTeX macros for using the fonts are provided.

date: 2009-06-24 20:29:01 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "MixedMap cm.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "MixedMap cmextra.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "MixedMap cyrillic.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map      euler.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "MixedMap latxfont.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "MixedMap symbols.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^MixedMap cm.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^MixedMap cmextra.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^MixedMap cyrillic.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map      euler.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^MixedMap latxfont.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^MixedMap symbols.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for amsfonts
Version: %{tl_version}
Release: %{tl_noarch_release}.3.0.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for amsfonts

%package fedora-fonts
Summary: Fonts for amsfonts
Version: %{tl_version}
Release: %{tl_noarch_release}.3.0.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-amsfonts = %{tl_version}
BuildArch: noarch

%description fedora-fonts
An extended set of fonts for use in mathematics, including:
extra mathematical symbols; blackboard bold letters (uppercase
only); fraktur letters; subscript sizes of bold math italic and
bold Greek letters; subscript sizes of large symbols such as
sum and product; added sizes of the Computer Modern small caps
font; cyrillic fonts (from the University of Washington); Euler
mathematical fonts. All fonts are provided as Adobe Type 1
files, and all except the Euler fonts are provided as MetaFont
source. The distribution also includes the canonical Type 1
versions of the Computer Modern family of fonts. Plain TeX and
LaTeX macros for using the fonts are provided.

date: 2009-06-24 20:29:01 +0200


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/ofl.txt ofl.txt
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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmb10.pfb .
ln -s %{_fontdir}/cmb10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmb10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbsy10.pfb .
ln -s %{_fontdir}/cmbsy10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbsy10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb .
ln -s %{_fontdir}/cmbx10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfb .
ln -s %{_fontdir}/cmbx12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx5.pfb .
ln -s %{_fontdir}/cmbx5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx6.pfb .
ln -s %{_fontdir}/cmbx6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx7.pfb .
ln -s %{_fontdir}/cmbx7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx8.pfb .
ln -s %{_fontdir}/cmbx8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb .
ln -s %{_fontdir}/cmbx9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbxsl10.pfb .
ln -s %{_fontdir}/cmbxsl10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbxsl10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbxti10.pfb .
ln -s %{_fontdir}/cmbxti10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbxti10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmcsc10.pfb .
ln -s %{_fontdir}/cmcsc10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmcsc10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmdunh10.pfb .
ln -s %{_fontdir}/cmdunh10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmdunh10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb .
ln -s %{_fontdir}/cmex10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmff10.pfb .
ln -s %{_fontdir}/cmff10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmff10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmfi10.pfb .
ln -s %{_fontdir}/cmfi10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmfi10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmfib8.pfb .
ln -s %{_fontdir}/cmfib8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmfib8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cminch.pfb .
ln -s %{_fontdir}/cminch.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cminch.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmitt10.pfb .
ln -s %{_fontdir}/cmitt10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmitt10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb .
ln -s %{_fontdir}/cmmi10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb .
ln -s %{_fontdir}/cmmi12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi5.pfb .
ln -s %{_fontdir}/cmmi5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb .
ln -s %{_fontdir}/cmmi6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb .
ln -s %{_fontdir}/cmmi7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb .
ln -s %{_fontdir}/cmmi8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb .
ln -s %{_fontdir}/cmmi9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfb .
ln -s %{_fontdir}/cmmib10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb .
ln -s %{_fontdir}/cmr10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb .
ln -s %{_fontdir}/cmr12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb .
ln -s %{_fontdir}/cmr17.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr5.pfb .
ln -s %{_fontdir}/cmr5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb .
ln -s %{_fontdir}/cmr6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb .
ln -s %{_fontdir}/cmr7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb .
ln -s %{_fontdir}/cmr8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb .
ln -s %{_fontdir}/cmr9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsl10.pfb .
ln -s %{_fontdir}/cmsl10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsl10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsl12.pfb .
ln -s %{_fontdir}/cmsl12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsl12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsl8.pfb .
ln -s %{_fontdir}/cmsl8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsl8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsl9.pfb .
ln -s %{_fontdir}/cmsl9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsl9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsltt10.pfb .
ln -s %{_fontdir}/cmsltt10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsltt10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss10.pfb .
ln -s %{_fontdir}/cmss10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss12.pfb .
ln -s %{_fontdir}/cmss12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss17.pfb .
ln -s %{_fontdir}/cmss17.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss17.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss8.pfb .
ln -s %{_fontdir}/cmss8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss9.pfb .
ln -s %{_fontdir}/cmss9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssbx10.pfb .
ln -s %{_fontdir}/cmssbx10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssbx10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssdc10.pfb .
ln -s %{_fontdir}/cmssdc10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssdc10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi10.pfb .
ln -s %{_fontdir}/cmssi10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi12.pfb .
ln -s %{_fontdir}/cmssi12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi17.pfb .
ln -s %{_fontdir}/cmssi17.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi17.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi8.pfb .
ln -s %{_fontdir}/cmssi8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi9.pfb .
ln -s %{_fontdir}/cmssi9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssq8.pfb .
ln -s %{_fontdir}/cmssq8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssq8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssqi8.pfb .
ln -s %{_fontdir}/cmssqi8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssqi8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb .
ln -s %{_fontdir}/cmsy10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy5.pfb .
ln -s %{_fontdir}/cmsy5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb .
ln -s %{_fontdir}/cmsy6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb .
ln -s %{_fontdir}/cmsy7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb .
ln -s %{_fontdir}/cmsy8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb .
ln -s %{_fontdir}/cmsy9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtcsc10.pfb .
ln -s %{_fontdir}/cmtcsc10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtcsc10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtex10.pfb .
ln -s %{_fontdir}/cmtex10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtex10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtex8.pfb .
ln -s %{_fontdir}/cmtex8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtex8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtex9.pfb .
ln -s %{_fontdir}/cmtex9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtex9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb .
ln -s %{_fontdir}/cmti10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti12.pfb .
ln -s %{_fontdir}/cmti12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti7.pfb .
ln -s %{_fontdir}/cmti7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti8.pfb .
ln -s %{_fontdir}/cmti8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb .
ln -s %{_fontdir}/cmti9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfb .
ln -s %{_fontdir}/cmtt10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt12.pfb .
ln -s %{_fontdir}/cmtt12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt8.pfb .
ln -s %{_fontdir}/cmtt8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt9.pfb .
ln -s %{_fontdir}/cmtt9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmu10.pfb .
ln -s %{_fontdir}/cmu10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmu10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmvtt10.pfb .
ln -s %{_fontdir}/cmvtt10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmvtt10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy5.pfb .
ln -s %{_fontdir}/cmbsy5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy6.pfb .
ln -s %{_fontdir}/cmbsy6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy7.pfb .
ln -s %{_fontdir}/cmbsy7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy8.pfb .
ln -s %{_fontdir}/cmbsy8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy9.pfb .
ln -s %{_fontdir}/cmbsy9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmcsc8.pfb .
ln -s %{_fontdir}/cmcsc8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmcsc8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmcsc9.pfb .
ln -s %{_fontdir}/cmcsc9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmcsc9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex7.pfb .
ln -s %{_fontdir}/cmex7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex8.pfb .
ln -s %{_fontdir}/cmex8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex9.pfb .
ln -s %{_fontdir}/cmex9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib5.pfb .
ln -s %{_fontdir}/cmmib5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib6.pfb .
ln -s %{_fontdir}/cmmib6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib7.pfb .
ln -s %{_fontdir}/cmmib7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib8.pfb .
ln -s %{_fontdir}/cmmib8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib9.pfb .
ln -s %{_fontdir}/cmmib9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncyb10.pfb .
ln -s %{_fontdir}/wncyb10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncyb10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncyi10.pfb .
ln -s %{_fontdir}/wncyi10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncyi10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncyr10.pfb .
ln -s %{_fontdir}/wncyr10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncyr10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncysc10.pfb .
ln -s %{_fontdir}/wncysc10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncysc10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncyss10.pfb .
ln -s %{_fontdir}/wncyss10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncyss10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/euex10.pfb .
ln -s %{_fontdir}/euex10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/euex10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/euex7.pfb .
ln -s %{_fontdir}/euex7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/euex7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/euex8.pfb .
ln -s %{_fontdir}/euex8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/euex8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/euex9.pfb .
ln -s %{_fontdir}/euex9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/euex9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufb10.pfb .
ln -s %{_fontdir}/eufb10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufb10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufb5.pfb .
ln -s %{_fontdir}/eufb5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufb5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufb7.pfb .
ln -s %{_fontdir}/eufb7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufb7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufm10.pfb .
ln -s %{_fontdir}/eufm10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufm10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufm5.pfb .
ln -s %{_fontdir}/eufm5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufm5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufm7.pfb .
ln -s %{_fontdir}/eufm7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufm7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurb10.pfb .
ln -s %{_fontdir}/eurb10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurb10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurb5.pfb .
ln -s %{_fontdir}/eurb5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurb5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurb7.pfb .
ln -s %{_fontdir}/eurb7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurb7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurm10.pfb .
ln -s %{_fontdir}/eurm10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurm10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurm5.pfb .
ln -s %{_fontdir}/eurm5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurm5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurm7.pfb .
ln -s %{_fontdir}/eurm7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurm7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusb10.pfb .
ln -s %{_fontdir}/eusb10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusb10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusb5.pfb .
ln -s %{_fontdir}/eusb5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusb5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusb7.pfb .
ln -s %{_fontdir}/eusb7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusb7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusm10.pfb .
ln -s %{_fontdir}/eusm10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusm10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusm5.pfb .
ln -s %{_fontdir}/eusm5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusm5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusm7.pfb .
ln -s %{_fontdir}/eusm7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusm7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy10.pfb .
ln -s %{_fontdir}/lasy10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy5.pfb .
ln -s %{_fontdir}/lasy5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy6.pfb .
ln -s %{_fontdir}/lasy6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy7.pfb .
ln -s %{_fontdir}/lasy7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy8.pfb .
ln -s %{_fontdir}/lasy8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy9.pfb .
ln -s %{_fontdir}/lasy9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasyb10.pfb .
ln -s %{_fontdir}/lasyb10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasyb10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcircle1.pfb .
ln -s %{_fontdir}/lcircle1.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcircle1.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcirclew.pfb .
ln -s %{_fontdir}/lcirclew.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcirclew.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcmss8.pfb .
ln -s %{_fontdir}/lcmss8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcmss8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcmssb8.pfb .
ln -s %{_fontdir}/lcmssb8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcmssb8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcmssi8.pfb .
ln -s %{_fontdir}/lcmssi8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcmssi8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/line10.pfb .
ln -s %{_fontdir}/line10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/line10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/linew10.pfb .
ln -s %{_fontdir}/linew10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/linew10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb .
ln -s %{_fontdir}/msam10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam5.pfb .
ln -s %{_fontdir}/msam5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam6.pfb .
ln -s %{_fontdir}/msam6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam7.pfb .
ln -s %{_fontdir}/msam7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam8.pfb .
ln -s %{_fontdir}/msam8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam9.pfb .
ln -s %{_fontdir}/msam9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb .
ln -s %{_fontdir}/msbm10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm5.pfb .
ln -s %{_fontdir}/msbm5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm6.pfb .
ln -s %{_fontdir}/msbm6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm7.pfb .
ln -s %{_fontdir}/msbm7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm8.pfb .
ln -s %{_fontdir}/msbm8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm9.pfb .
ln -s %{_fontdir}/msbm9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm9.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc ofl.txt
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmb10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmbsy10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmbx10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmbx12.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmbx5.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmbx6.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmbx7.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmbx8.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmbx9.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmbxsl10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmbxti10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmcsc10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmdunh10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmex10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmff10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmfi10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmfib8.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cminch.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmitt10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmmi10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmmi12.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmmi5.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmmi6.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmmi7.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmmi8.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmmi9.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmmib10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmr10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmr12.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmr17.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmr5.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmr6.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmr7.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmr8.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmr9.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmsl10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmsl12.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmsl8.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmsl9.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmsltt10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmss10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmss12.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmss17.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmss8.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmss9.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmssbx10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmssdc10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmssi10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmssi12.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmssi17.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmssi8.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmssi9.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmssq8.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmssqi8.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmsy10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmsy5.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmsy6.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmsy7.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmsy8.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmsy9.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmtcsc10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmtex10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmtex8.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmtex9.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmti10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmti12.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmti7.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmti8.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmti9.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmtt10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmtt12.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmtt8.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmtt9.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmu10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmvtt10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmbsy5.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmbsy6.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmbsy7.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmbsy8.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmbsy9.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmcsc8.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmcsc9.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmex7.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmex8.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmex9.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmmib5.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmmib6.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmmib7.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmmib8.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmmib9.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cyrillic/wncyb10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cyrillic/wncyi10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cyrillic/wncyr10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cyrillic/wncysc10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cyrillic/wncyss10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/euler/euex10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/euler/euex7.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/euler/euex8.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/euler/euex9.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/euler/eufb10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/euler/eufb5.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/euler/eufb7.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/euler/eufm10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/euler/eufm5.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/euler/eufm7.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/euler/eurb10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/euler/eurb5.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/euler/eurb7.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/euler/eurm10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/euler/eurm5.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/euler/eurm7.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/euler/eusb10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/euler/eusb5.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/euler/eusb7.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/euler/eusm10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/euler/eusm5.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/euler/eusm7.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/lasy10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/lasy5.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/lasy6.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/lasy7.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/lasy8.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/lasy9.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/lasyb10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/lcircle1.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/lcirclew.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/lcmss8.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/lcmssb8.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/lcmssi8.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/line10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/linew10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/symbols/msam10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/symbols/msam5.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/symbols/msam6.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/symbols/msam7.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/symbols/msam8.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/symbols/msam9.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/symbols/msbm10.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/symbols/msbm5.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/symbols/msbm6.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/symbols/msbm7.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/symbols/msbm8.afm
%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/symbols/msbm9.afm
%{_texdir}/texmf-dist/fonts/map/dvips/amsfonts/cm.map
%{_texdir}/texmf-dist/fonts/map/dvips/amsfonts/cmextra.map
%{_texdir}/texmf-dist/fonts/map/dvips/amsfonts/cyrillic.map
%{_texdir}/texmf-dist/fonts/map/dvips/amsfonts/euler.map
%{_texdir}/texmf-dist/fonts/map/dvips/amsfonts/latxfont.map
%{_texdir}/texmf-dist/fonts/map/dvips/amsfonts/symbols.map
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmbsy5.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmbsy6.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmbsy7.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmbsy8.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmbsy9.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmcsc8.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmcsc9.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmex7.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmex8.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmex9.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmmib5.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmmib6.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmmib7.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmmib8.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmmib9.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/cyrcsc.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/cyrfont.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/cyrilu.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/cyrital.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/cyrmax.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/cyrpunc.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/cyrspl.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/cyrspu.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/cyrti.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/serb.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/serbspu.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyb10.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyb5.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyb6.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyb7.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyb8.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyb9.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyi10.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyi5.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyi6.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyi7.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyi8.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyi9.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyr10.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyr5.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyr6.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyr7.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyr8.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyr9.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncysc10.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyss10.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyss8.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyss9.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/dummy/dummy.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/symbols/amsya.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/symbols/amsyb.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/symbols/asymbols.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/symbols/bsymbols.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/symbols/msam10.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/symbols/msam5.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/symbols/msam6.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/symbols/msam7.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/symbols/msam8.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/symbols/msam9.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/symbols/msbm10.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/symbols/msbm5.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/symbols/msbm6.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/symbols/msbm7.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/symbols/msbm8.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/symbols/msbm9.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/symbols/xbbase.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/symbols/xbbold.mf
%{_texdir}/texmf-dist/fonts/source/public/amsfonts/symbols/xbcaps.mf
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmbsy5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmbsy6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmbsy7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmbsy8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmbsy9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmcsc8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmcsc9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmex7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmex8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmex9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmmib5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmmib6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmmib7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmmib8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmmib9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyb5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyb6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyb7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyb8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyb9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyi10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyi5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyi6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyi7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyi8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyi9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyr5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyr6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyr7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyr8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyr9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncysc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyss10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyss8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyss9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/dummy/dummy.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/euex10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/euex7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/euex8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/euex9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eufb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eufb5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eufb6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eufb7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eufb8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eufb9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eufm10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eufm5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eufm6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eufm7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eufm8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eufm9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eurb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eurb5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eurb6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eurb7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eurb8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eurb9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eurm10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eurm5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eurm6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eurm7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eurm8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eurm9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eusb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eusb5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eusb6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eusb7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eusb8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eusb9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eusm10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eusm5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eusm6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eusm7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eusm8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eusm9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm9.tfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmb10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmb10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbsy10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbsy10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx5.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx6.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx7.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbxsl10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbxsl10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbxti10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbxti10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmcsc10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmcsc10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmdunh10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmdunh10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmff10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmff10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmfi10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmfi10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmfib8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmfib8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cminch.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cminch.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmitt10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmitt10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi5.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr5.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsl10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsl10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsl12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsl12.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsl8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsl8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsl9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsl9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsltt10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsltt10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss12.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss17.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss17.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssbx10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssbx10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssdc10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssdc10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi12.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi17.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi17.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssq8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssq8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssqi8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssqi8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy5.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtcsc10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtcsc10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtex10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtex10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtex8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtex8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtex9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtex9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti12.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti7.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt12.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmu10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmu10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmvtt10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmvtt10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy5.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy6.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy7.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmcsc8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmcsc8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmcsc9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmcsc9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex7.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib5.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib6.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib7.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncyb10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncyb10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncyi10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncyi10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncyr10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncyr10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncysc10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncysc10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncyss10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncyss10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/euex10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/euex10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/euex7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/euex7.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/euex8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/euex8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/euex9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/euex9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufb10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufb10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufb5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufb5.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufb7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufb7.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufm10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufm10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufm5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufm5.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufm7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufm7.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurb10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurb10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurb5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurb5.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurb7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurb7.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurm10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurm10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurm5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurm5.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurm7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurm7.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusb10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusb10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusb5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusb5.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusb7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusb7.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusm10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusm10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusm5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusm5.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusm7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusm7.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy5.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy6.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy7.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasyb10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasyb10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcircle1.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcircle1.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcirclew.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcirclew.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcmss8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcmss8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcmssb8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcmssb8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcmssi8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcmssi8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/line10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/line10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/linew10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/linew10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam5.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam6.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam7.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm5.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm6.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm7.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm9.pfm
%{_texdir}/texmf-dist/tex/latex/amsfonts/amsfonts.sty
%{_texdir}/texmf-dist/tex/latex/amsfonts/amssymb.sty
%{_texdir}/texmf-dist/tex/latex/amsfonts/cmmib57.sty
%{_texdir}/texmf-dist/tex/latex/amsfonts/eucal.sty
%{_texdir}/texmf-dist/tex/latex/amsfonts/eufrak.sty
%{_texdir}/texmf-dist/tex/latex/amsfonts/euscript.sty
%{_texdir}/texmf-dist/tex/latex/amsfonts/ueuex.fd
%{_texdir}/texmf-dist/tex/latex/amsfonts/ueuf.fd
%{_texdir}/texmf-dist/tex/latex/amsfonts/ueur.fd
%{_texdir}/texmf-dist/tex/latex/amsfonts/ueus.fd
%{_texdir}/texmf-dist/tex/latex/amsfonts/umsa.fd
%{_texdir}/texmf-dist/tex/latex/amsfonts/umsb.fd
%{_texdir}/texmf-dist/tex/plain/amsfonts/amssym.def
%{_texdir}/texmf-dist/tex/plain/amsfonts/amssym.tex
%{_texdir}/texmf-dist/tex/plain/amsfonts/cyracc.def

%files doc
%defattr(-,root,root)
%doc ofl.txt
%{_texdir}/texmf-dist/doc/fonts/amsfonts/00README
%{_texdir}/texmf-dist/doc/fonts/amsfonts/OFL-FAQ.txt
%{_texdir}/texmf-dist/doc/fonts/amsfonts/OFL.txt
%{_texdir}/texmf-dist/doc/fonts/amsfonts/amsfndoc.pdf
%{_texdir}/texmf-dist/doc/fonts/amsfonts/amsfonts.pdf
%{_texdir}/texmf-dist/doc/fonts/amsfonts/amssymb.pdf
%{_texdir}/texmf-dist/doc/fonts/amsfonts/cmmib57.pdf
%{_texdir}/texmf-dist/doc/fonts/amsfonts/eufrak.pdf
%{_texdir}/texmf-dist/doc/fonts/amsfonts/euscript.pdf

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/cmb10.pfb
%{_fontdir}/cmbsy10.pfb
%{_fontdir}/cmbx10.pfb
%{_fontdir}/cmbx12.pfb
%{_fontdir}/cmbx5.pfb
%{_fontdir}/cmbx6.pfb
%{_fontdir}/cmbx7.pfb
%{_fontdir}/cmbx8.pfb
%{_fontdir}/cmbx9.pfb
%{_fontdir}/cmbxsl10.pfb
%{_fontdir}/cmbxti10.pfb
%{_fontdir}/cmcsc10.pfb
%{_fontdir}/cmdunh10.pfb
%{_fontdir}/cmex10.pfb
%{_fontdir}/cmff10.pfb
%{_fontdir}/cmfi10.pfb
%{_fontdir}/cmfib8.pfb
%{_fontdir}/cminch.pfb
%{_fontdir}/cmitt10.pfb
%{_fontdir}/cmmi10.pfb
%{_fontdir}/cmmi12.pfb
%{_fontdir}/cmmi5.pfb
%{_fontdir}/cmmi6.pfb
%{_fontdir}/cmmi7.pfb
%{_fontdir}/cmmi8.pfb
%{_fontdir}/cmmi9.pfb
%{_fontdir}/cmmib10.pfb
%{_fontdir}/cmr10.pfb
%{_fontdir}/cmr12.pfb
%{_fontdir}/cmr17.pfb
%{_fontdir}/cmr5.pfb
%{_fontdir}/cmr6.pfb
%{_fontdir}/cmr7.pfb
%{_fontdir}/cmr8.pfb
%{_fontdir}/cmr9.pfb
%{_fontdir}/cmsl10.pfb
%{_fontdir}/cmsl12.pfb
%{_fontdir}/cmsl8.pfb
%{_fontdir}/cmsl9.pfb
%{_fontdir}/cmsltt10.pfb
%{_fontdir}/cmss10.pfb
%{_fontdir}/cmss12.pfb
%{_fontdir}/cmss17.pfb
%{_fontdir}/cmss8.pfb
%{_fontdir}/cmss9.pfb
%{_fontdir}/cmssbx10.pfb
%{_fontdir}/cmssdc10.pfb
%{_fontdir}/cmssi10.pfb
%{_fontdir}/cmssi12.pfb
%{_fontdir}/cmssi17.pfb
%{_fontdir}/cmssi8.pfb
%{_fontdir}/cmssi9.pfb
%{_fontdir}/cmssq8.pfb
%{_fontdir}/cmssqi8.pfb
%{_fontdir}/cmsy10.pfb
%{_fontdir}/cmsy5.pfb
%{_fontdir}/cmsy6.pfb
%{_fontdir}/cmsy7.pfb
%{_fontdir}/cmsy8.pfb
%{_fontdir}/cmsy9.pfb
%{_fontdir}/cmtcsc10.pfb
%{_fontdir}/cmtex10.pfb
%{_fontdir}/cmtex8.pfb
%{_fontdir}/cmtex9.pfb
%{_fontdir}/cmti10.pfb
%{_fontdir}/cmti12.pfb
%{_fontdir}/cmti7.pfb
%{_fontdir}/cmti8.pfb
%{_fontdir}/cmti9.pfb
%{_fontdir}/cmtt10.pfb
%{_fontdir}/cmtt12.pfb
%{_fontdir}/cmtt8.pfb
%{_fontdir}/cmtt9.pfb
%{_fontdir}/cmu10.pfb
%{_fontdir}/cmvtt10.pfb
%{_fontdir}/cmbsy5.pfb
%{_fontdir}/cmbsy6.pfb
%{_fontdir}/cmbsy7.pfb
%{_fontdir}/cmbsy8.pfb
%{_fontdir}/cmbsy9.pfb
%{_fontdir}/cmcsc8.pfb
%{_fontdir}/cmcsc9.pfb
%{_fontdir}/cmex7.pfb
%{_fontdir}/cmex8.pfb
%{_fontdir}/cmex9.pfb
%{_fontdir}/cmmib5.pfb
%{_fontdir}/cmmib6.pfb
%{_fontdir}/cmmib7.pfb
%{_fontdir}/cmmib8.pfb
%{_fontdir}/cmmib9.pfb
%{_fontdir}/wncyb10.pfb
%{_fontdir}/wncyi10.pfb
%{_fontdir}/wncyr10.pfb
%{_fontdir}/wncysc10.pfb
%{_fontdir}/wncyss10.pfb
%{_fontdir}/euex10.pfb
%{_fontdir}/euex7.pfb
%{_fontdir}/euex8.pfb
%{_fontdir}/euex9.pfb
%{_fontdir}/eufb10.pfb
%{_fontdir}/eufb5.pfb
%{_fontdir}/eufb7.pfb
%{_fontdir}/eufm10.pfb
%{_fontdir}/eufm5.pfb
%{_fontdir}/eufm7.pfb
%{_fontdir}/eurb10.pfb
%{_fontdir}/eurb5.pfb
%{_fontdir}/eurb7.pfb
%{_fontdir}/eurm10.pfb
%{_fontdir}/eurm5.pfb
%{_fontdir}/eurm7.pfb
%{_fontdir}/eusb10.pfb
%{_fontdir}/eusb5.pfb
%{_fontdir}/eusb7.pfb
%{_fontdir}/eusm10.pfb
%{_fontdir}/eusm5.pfb
%{_fontdir}/eusm7.pfb
%{_fontdir}/lasy10.pfb
%{_fontdir}/lasy5.pfb
%{_fontdir}/lasy6.pfb
%{_fontdir}/lasy7.pfb
%{_fontdir}/lasy8.pfb
%{_fontdir}/lasy9.pfb
%{_fontdir}/lasyb10.pfb
%{_fontdir}/lcircle1.pfb
%{_fontdir}/lcirclew.pfb
%{_fontdir}/lcmss8.pfb
%{_fontdir}/lcmssb8.pfb
%{_fontdir}/lcmssi8.pfb
%{_fontdir}/line10.pfb
%{_fontdir}/linew10.pfb
%{_fontdir}/msam10.pfb
%{_fontdir}/msam5.pfb
%{_fontdir}/msam6.pfb
%{_fontdir}/msam7.pfb
%{_fontdir}/msam8.pfb
%{_fontdir}/msam9.pfb
%{_fontdir}/msbm10.pfb
%{_fontdir}/msbm5.pfb
%{_fontdir}/msbm6.pfb
%{_fontdir}/msbm7.pfb
%{_fontdir}/msbm8.pfb
%{_fontdir}/msbm9.pfb

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
