%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/xypic.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/xypic.doc.tar.xz

Name: texlive-xypic
License: GPL+
Summary: Flexible diagramming macros
Version: %{tl_version}
Release: %{tl_noarch_release}.3.8.3.svn19311%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(movie.sty)
Provides: tex(xy.sty)
Provides: tex(xypic.sty)
Requires: tex(keyval.sty)
Requires: tex(ifpdf.sty)
Requires: texlive-xypic-fedora-fonts = %{tl_version}

%description
A package for typesetting a variety of graphs and diagrams with
TeX. Xy-pic works with most formats (including LaTeX, AMS-
LaTeX, AMS-TeX, and plain TeX).

date: 2010-07-07 08:59:36 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "MixedMap xypic.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^MixedMap xypic.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for xypic
Version: %{tl_version}
Release: %{tl_noarch_release}.3.8.3.svn19311%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for xypic

%package fedora-fonts
Summary: Fonts for xypic
Version: %{tl_version}
Release: %{tl_noarch_release}.3.8.3.svn19311%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-xypic = %{tl_version}
BuildArch: noarch

%description fedora-fonts
A package for typesetting a variety of graphs and diagrams with
TeX. Xy-pic works with most formats (including LaTeX, AMS-
LaTeX, AMS-TeX, and plain TeX).

date: 2010-07-07 08:59:36 +0200


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyatip10.pfb .
ln -s %{_fontdir}/xyatip10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyatip10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xybsql10.pfb .
ln -s %{_fontdir}/xybsql10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xybsql10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xybtip10.pfb .
ln -s %{_fontdir}/xybtip10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xybtip10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycirc10.pfb .
ln -s %{_fontdir}/xycirc10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycirc10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycmat10.pfb .
ln -s %{_fontdir}/xycmat10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycmat10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycmat11.pfb .
ln -s %{_fontdir}/xycmat11.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycmat11.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycmat12.pfb .
ln -s %{_fontdir}/xycmat12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycmat12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycmbt10.pfb .
ln -s %{_fontdir}/xycmbt10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycmbt10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycmbt11.pfb .
ln -s %{_fontdir}/xycmbt11.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycmbt11.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycmbt12.pfb .
ln -s %{_fontdir}/xycmbt12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycmbt12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xydash10.pfb .
ln -s %{_fontdir}/xydash10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xydash10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyeuat10.pfb .
ln -s %{_fontdir}/xyeuat10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyeuat10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyeuat11.pfb .
ln -s %{_fontdir}/xyeuat11.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyeuat11.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyeuat12.pfb .
ln -s %{_fontdir}/xyeuat12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyeuat12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyeubt10.pfb .
ln -s %{_fontdir}/xyeubt10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyeubt10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyeubt11.pfb .
ln -s %{_fontdir}/xyeubt11.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyeubt11.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyeubt12.pfb .
ln -s %{_fontdir}/xyeubt12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyeubt12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyluat10.pfb .
ln -s %{_fontdir}/xyluat10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyluat10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyluat11.pfb .
ln -s %{_fontdir}/xyluat11.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyluat11.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyluat12.pfb .
ln -s %{_fontdir}/xyluat12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyluat12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xylubt10.pfb .
ln -s %{_fontdir}/xylubt10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xylubt10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xylubt11.pfb .
ln -s %{_fontdir}/xylubt11.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xylubt11.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xylubt12.pfb .
ln -s %{_fontdir}/xylubt12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic/xylubt12.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/dvips/xypic/xy386dict.pro
%{_texdir}/texmf-dist/fonts/afm/public/xypic/xyatip10.afm
%{_texdir}/texmf-dist/fonts/afm/public/xypic/xybsql10.afm
%{_texdir}/texmf-dist/fonts/afm/public/xypic/xybtip10.afm
%{_texdir}/texmf-dist/fonts/afm/public/xypic/xycirc10.afm
%{_texdir}/texmf-dist/fonts/afm/public/xypic/xycmat10.afm
%{_texdir}/texmf-dist/fonts/afm/public/xypic/xycmat11.afm
%{_texdir}/texmf-dist/fonts/afm/public/xypic/xycmat12.afm
%{_texdir}/texmf-dist/fonts/afm/public/xypic/xycmbt10.afm
%{_texdir}/texmf-dist/fonts/afm/public/xypic/xycmbt11.afm
%{_texdir}/texmf-dist/fonts/afm/public/xypic/xycmbt12.afm
%{_texdir}/texmf-dist/fonts/afm/public/xypic/xydash10.afm
%{_texdir}/texmf-dist/fonts/afm/public/xypic/xyeuat10.afm
%{_texdir}/texmf-dist/fonts/afm/public/xypic/xyeuat11.afm
%{_texdir}/texmf-dist/fonts/afm/public/xypic/xyeuat12.afm
%{_texdir}/texmf-dist/fonts/afm/public/xypic/xyeubt10.afm
%{_texdir}/texmf-dist/fonts/afm/public/xypic/xyeubt11.afm
%{_texdir}/texmf-dist/fonts/afm/public/xypic/xyeubt12.afm
%{_texdir}/texmf-dist/fonts/afm/public/xypic/xyluat10.afm
%{_texdir}/texmf-dist/fonts/afm/public/xypic/xyluat11.afm
%{_texdir}/texmf-dist/fonts/afm/public/xypic/xyluat12.afm
%{_texdir}/texmf-dist/fonts/afm/public/xypic/xylubt10.afm
%{_texdir}/texmf-dist/fonts/afm/public/xypic/xylubt11.afm
%{_texdir}/texmf-dist/fonts/afm/public/xypic/xylubt12.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/xypic/xycirc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/xypic/xyd.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/xypic/xyd2.enc
%{_texdir}/texmf-dist/fonts/map/dvips/xypic/xypic.map
%{_texdir}/texmf-dist/fonts/source/public/xypic/xyatip.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xyatip10.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xyatri.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xybsql10.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xybtip.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xybtip10.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xybtri.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xycirc10.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xycm.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xycmat10.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xycmat11.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xycmat12.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xycmbt10.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xycmbt11.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xycmbt12.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xyd.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xyd2.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xydash10.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xyeuat10.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xyeuat11.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xyeuat12.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xyeubt10.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xyeubt11.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xyeubt12.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xyeuler.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xyline10.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xylu.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xyluat10.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xyluat11.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xyluat12.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xylubt10.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xylubt11.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xylubt12.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xymisc10.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xyqc10.mf
%{_texdir}/texmf-dist/fonts/source/public/xypic/xytech.mf
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xyatip10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xybsql10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xybtip10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xycirc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xycmat10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xycmat11.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xycmat12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xycmbt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xycmbt11.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xycmbt12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xydash10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xyeuat10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xyeuat11.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xyeuat12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xyeubt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xyeubt11.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xyeubt12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xyline10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xyluat10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xyluat11.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xyluat12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xylubt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xylubt11.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xylubt12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xymisc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/xypic/xyqc10.tfm
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyatip10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyatip10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xybsql10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xybsql10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xybtip10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xybtip10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycirc10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycirc10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycmat10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycmat10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycmat11.pfb
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycmat11.pfm
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycmat12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycmat12.pfm
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycmbt10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycmbt10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycmbt11.pfb
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycmbt11.pfm
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycmbt12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xycmbt12.pfm
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xydash10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xydash10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyeuat10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyeuat10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyeuat11.pfb
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyeuat11.pfm
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyeuat12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyeuat12.pfm
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyeubt10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyeubt10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyeubt11.pfb
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyeubt11.pfm
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyeubt12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyeubt12.pfm
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyluat10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyluat10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyluat11.pfb
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyluat11.pfm
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyluat12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xyluat12.pfm
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xylubt10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xylubt10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xylubt11.pfb
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xylubt11.pfm
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xylubt12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/xypic/xylubt12.pfm
%{_texdir}/texmf-dist/tex/generic/xypic/movie.cls
%{_texdir}/texmf-dist/tex/generic/xypic/xy.sty
%{_texdir}/texmf-dist/tex/generic/xypic/xy.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xy16textures.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xy17oztex.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xy2cell.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyall.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyarc.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyarrow.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xycmactex.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xycmtip.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xycolor.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xycrayon.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xycurve.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xydummy.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xydvidrv.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xydvips.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xydvitops.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyemtex.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyframe.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xygraph.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyidioms.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyimport.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyknot.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyline.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xymacpat.xyp
%{_texdir}/texmf-dist/tex/generic/xypic/xymatrix.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xymovie.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xynecula.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyoztex.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xypdf-co.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xypdf-cu.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xypdf-fr.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xypdf-li.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xypdf-ro.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xypdf.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xypic.sty
%{_texdir}/texmf-dist/tex/generic/xypic/xypic.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xypicture.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xypoly.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyps-c.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyps-col.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyps-f.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyps-l.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyps-pro.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyps-ps.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyps-r.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyps-s.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyps-t.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyps.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xypsdict.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xypspatt.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyrecat.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyrotate.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xysmart.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xytextures.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xytile.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xytips.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xytp-f.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xytpic.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyv2.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyweb.tex
%{_texdir}/texmf-dist/tex/generic/xypic/xyxdvi.tex

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/generic/xypic/CATALOG
%{_texdir}/texmf-dist/doc/generic/xypic/COPYING
%{_texdir}/texmf-dist/doc/generic/xypic/FONTCOPYING
%{_texdir}/texmf-dist/doc/generic/xypic/INSTALL
%{_texdir}/texmf-dist/doc/generic/xypic/MANIFEST
%{_texdir}/texmf-dist/doc/generic/xypic/README
%{_texdir}/texmf-dist/doc/generic/xypic/TRAILER
%{_texdir}/texmf-dist/doc/generic/xypic/VERSIONS
%{_texdir}/texmf-dist/doc/generic/xypic/Xy-logo.png
%{_texdir}/texmf-dist/doc/generic/xypic/Xy-pic.html
%{_texdir}/texmf-dist/doc/generic/xypic/xy386src.tar.gz
%{_texdir}/texmf-dist/doc/generic/xypic/xyguide.pdf
%{_texdir}/texmf-dist/doc/generic/xypic/xypdf.pdf
%{_texdir}/texmf-dist/doc/generic/xypic/xyrefer.pdf
%{_texdir}/texmf-dist/doc/generic/xypic/xysource.pdf
%{_texdir}/texmf-dist/doc/generic/xypic/support/dvitogif89a
%{_texdir}/texmf-dist/doc/generic/xypic/support/install-tds
%{_texdir}/texmf-dist/doc/generic/xypic/support/pnmrawtopcropwhite.c

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/xyatip10.pfb
%{_fontdir}/xybsql10.pfb
%{_fontdir}/xybtip10.pfb
%{_fontdir}/xycirc10.pfb
%{_fontdir}/xycmat10.pfb
%{_fontdir}/xycmat11.pfb
%{_fontdir}/xycmat12.pfb
%{_fontdir}/xycmbt10.pfb
%{_fontdir}/xycmbt11.pfb
%{_fontdir}/xycmbt12.pfb
%{_fontdir}/xydash10.pfb
%{_fontdir}/xyeuat10.pfb
%{_fontdir}/xyeuat11.pfb
%{_fontdir}/xyeuat12.pfb
%{_fontdir}/xyeubt10.pfb
%{_fontdir}/xyeubt11.pfb
%{_fontdir}/xyeubt12.pfb
%{_fontdir}/xyluat10.pfb
%{_fontdir}/xyluat11.pfb
%{_fontdir}/xyluat12.pfb
%{_fontdir}/xylubt10.pfb
%{_fontdir}/xylubt11.pfb
%{_fontdir}/xylubt12.pfb

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
