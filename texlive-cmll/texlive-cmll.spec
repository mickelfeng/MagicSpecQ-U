%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cmll.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cmll.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cmll.source.tar.xz

Name: texlive-cmll
License: LPPL
Summary: Symbols for linear logic
Version: %{tl_version}
Release: %{tl_noarch_release}.svn17964%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(cmll.sty)
Requires: tex(ifthen.sty)
Requires: tex(graphicx.sty)
Requires: tex(relsize.sty)
Requires: texlive-cmll-fedora-fonts = %{tl_version}

%description
This is a very small font set that contain some symbols useful
in linear logic, which are apparently not available elsewhere.
Variants are included for use with Computer Modern serif and
sans-serif and with the AMS Euler series. The font is provided
both as MetaFont source, and in Adobe Type 1 format. LaTeX
support is provided. format.

date: 2010-04-20 23:51:50 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "MixedMap cmll.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^MixedMap cmll.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for cmll
Version: %{tl_version}
Release: %{tl_noarch_release}.svn17964%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for cmll

%package fedora-fonts
Summary: Fonts for cmll
Version: %{tl_version}
Release: %{tl_noarch_release}.svn17964%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-cmll = %{tl_version}
BuildArch: noarch

%description fedora-fonts
This is a very small font set that contain some symbols useful
in linear logic, which are apparently not available elsewhere.
Variants are included for use with Computer Modern serif and
sans-serif and with the AMS Euler series. The font is provided
both as MetaFont source, and in Adobe Type 1 format. LaTeX
support is provided. format.

date: 2010-04-20 23:51:50 +0200


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllbx10.pfb .
ln -s %{_fontdir}/cmllbx10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllbx10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllbx12.pfb .
ln -s %{_fontdir}/cmllbx12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllbx12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllbx5.pfb .
ln -s %{_fontdir}/cmllbx5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllbx5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllbx6.pfb .
ln -s %{_fontdir}/cmllbx6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllbx6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllbx7.pfb .
ln -s %{_fontdir}/cmllbx7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllbx7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllbx8.pfb .
ln -s %{_fontdir}/cmllbx8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllbx8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllbx9.pfb .
ln -s %{_fontdir}/cmllbx9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllbx9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllr10.pfb .
ln -s %{_fontdir}/cmllr10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllr10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllr12.pfb .
ln -s %{_fontdir}/cmllr12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllr12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllr17.pfb .
ln -s %{_fontdir}/cmllr17.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllr17.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllr5.pfb .
ln -s %{_fontdir}/cmllr5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllr5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllr6.pfb .
ln -s %{_fontdir}/cmllr6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllr6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllr7.pfb .
ln -s %{_fontdir}/cmllr7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllr7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllr8.pfb .
ln -s %{_fontdir}/cmllr8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllr8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllr9.pfb .
ln -s %{_fontdir}/cmllr9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllr9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllss10.pfb .
ln -s %{_fontdir}/cmllss10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllss10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllss12.pfb .
ln -s %{_fontdir}/cmllss12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllss12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllss17.pfb .
ln -s %{_fontdir}/cmllss17.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllss17.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllss8.pfb .
ln -s %{_fontdir}/cmllss8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllss8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllss9.pfb .
ln -s %{_fontdir}/cmllss9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllss9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllssbx10.pfb .
ln -s %{_fontdir}/cmllssbx10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllssbx10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullbx10.pfb .
ln -s %{_fontdir}/eullbx10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullbx10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullbx5.pfb .
ln -s %{_fontdir}/eullbx5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullbx5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullbx6.pfb .
ln -s %{_fontdir}/eullbx6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullbx6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullbx7.pfb .
ln -s %{_fontdir}/eullbx7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullbx7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullbx8.pfb .
ln -s %{_fontdir}/eullbx8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullbx8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullbx9.pfb .
ln -s %{_fontdir}/eullbx9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullbx9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullr10.pfb .
ln -s %{_fontdir}/eullr10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullr10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullr5.pfb .
ln -s %{_fontdir}/eullr5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullr5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullr6.pfb .
ln -s %{_fontdir}/eullr6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullr6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullr7.pfb .
ln -s %{_fontdir}/eullr7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullr7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullr8.pfb .
ln -s %{_fontdir}/eullr8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullr8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullr9.pfb .
ln -s %{_fontdir}/eullr9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullr9.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/fonts/map/dvips/cmll/cmll.map
%{_texdir}/texmf-dist/fonts/source/public/cmll/cmllbx10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/cmllbx12.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/cmllbx5.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/cmllbx6.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/cmllbx7.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/cmllbx8.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/cmllbx9.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/cmllr10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/cmllr12.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/cmllr17.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/cmllr5.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/cmllr6.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/cmllr7.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/cmllr8.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/cmllr9.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/cmllss10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/cmllss12.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/cmllss17.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/cmllss8.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/cmllss9.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/cmllssbx10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/eullbx10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/eullbx5.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/eullbx6.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/eullbx7.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/eullbx8.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/eullbx9.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/eullr10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/eullr5.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/eullr6.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/eullr7.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/eullr8.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/eullr9.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/llcommon.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/lleusym.mf
%{_texdir}/texmf-dist/fonts/source/public/cmll/llsymbols.mf
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/cmllbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/cmllbx12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/cmllbx5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/cmllbx6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/cmllbx7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/cmllbx8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/cmllbx9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/cmllr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/cmllr12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/cmllr17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/cmllr5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/cmllr6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/cmllr7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/cmllr8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/cmllr9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/cmllss10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/cmllss12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/cmllss17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/cmllss8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/cmllss9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/cmllssbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/eullbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/eullbx5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/eullbx6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/eullbx7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/eullbx8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/eullbx9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/eullr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/eullr5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/eullr6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/eullr7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/eullr8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/eullr9.tfm
%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllbx10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllbx12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllbx5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllbx6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllbx7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllbx8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllbx9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllr10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllr12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllr17.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllr5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllr6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllr7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllr8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllr9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllss10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllss12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllss17.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllss8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllss9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/cmllssbx10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullbx10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullbx5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullbx6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullbx7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullbx8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullbx9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullr10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullr5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullr6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullr7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullr8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cmll/eullr9.pfb
%{_texdir}/texmf-dist/tex/latex/cmll/cmll.sty
%{_texdir}/texmf-dist/tex/latex/cmll/ucmllr.fd
%{_texdir}/texmf-dist/tex/latex/cmll/ucmllss.fd
%{_texdir}/texmf-dist/tex/latex/cmll/ueull.fd

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/fonts/cmll/README
%{_texdir}/texmf-dist/doc/fonts/cmll/cmll.pdf

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/cmllbx10.pfb
%{_fontdir}/cmllbx12.pfb
%{_fontdir}/cmllbx5.pfb
%{_fontdir}/cmllbx6.pfb
%{_fontdir}/cmllbx7.pfb
%{_fontdir}/cmllbx8.pfb
%{_fontdir}/cmllbx9.pfb
%{_fontdir}/cmllr10.pfb
%{_fontdir}/cmllr12.pfb
%{_fontdir}/cmllr17.pfb
%{_fontdir}/cmllr5.pfb
%{_fontdir}/cmllr6.pfb
%{_fontdir}/cmllr7.pfb
%{_fontdir}/cmllr8.pfb
%{_fontdir}/cmllr9.pfb
%{_fontdir}/cmllss10.pfb
%{_fontdir}/cmllss12.pfb
%{_fontdir}/cmllss17.pfb
%{_fontdir}/cmllss8.pfb
%{_fontdir}/cmllss9.pfb
%{_fontdir}/cmllssbx10.pfb
%{_fontdir}/eullbx10.pfb
%{_fontdir}/eullbx5.pfb
%{_fontdir}/eullbx6.pfb
%{_fontdir}/eullbx7.pfb
%{_fontdir}/eullbx8.pfb
%{_fontdir}/eullbx9.pfb
%{_fontdir}/eullr10.pfb
%{_fontdir}/eullr5.pfb
%{_fontdir}/eullr6.pfb
%{_fontdir}/eullr7.pfb
%{_fontdir}/eullr8.pfb
%{_fontdir}/eullr9.pfb

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
