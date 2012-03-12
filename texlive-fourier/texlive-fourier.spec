%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/fourier.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/fourier.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/fourier.source.tar.xz

Name: texlive-fourier
License: LPPL
Summary: Using Utopia fonts in LaTeX documents
Version: %{tl_version}
Release: %{tl_noarch_release}.1.3.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(fourier-orns.sty)
Provides: tex(fourier.sty)
Requires: tex(fontenc.sty)
Requires: tex(textcomp.sty)
Requires: texlive-fourier-fedora-fonts = %{tl_version}

%description
Fourier-GUTenberg is a LaTeX typesetting system which uses
Adobe Utopia as its standard base font. Fourier-GUTenberg
provides all complementary typefaces needed to allow Utopia
based TeX typesetting, including an extensive mathematics set
and several other symbols. The system is absolutely stand-
alone: apart from Utopia and Fourier, no other typefaces are
required. The fourier fonts will also work with Adobe Utopia
Expert fonts, which are only available for purchase. Utopia is
a registered trademark of Adobe Systems Incorporated

date: 2008-12-13 14:57:21 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map fourier.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map fourier-utopia-expert.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map fourier.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map fourier-utopia-expert.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for fourier
Version: %{tl_version}
Release: %{tl_noarch_release}.1.3.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for fourier

%package fedora-fonts
Summary: Fonts for fourier
Version: %{tl_version}
Release: %{tl_noarch_release}.1.3.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-fourier = %{tl_version}
BuildArch: noarch

%description fedora-fonts
Fourier-GUTenberg is a LaTeX typesetting system which uses
Adobe Utopia as its standard base font. Fourier-GUTenberg
provides all complementary typefaces needed to allow Utopia
based TeX typesetting, including an extensive mathematics set
and several other symbols. The system is absolutely stand-
alone: apart from Utopia and Fourier, no other typefaces are
required. The fourier fonts will also work with Adobe Utopia
Expert fonts, which are only available for purchase. Utopia is
a registered trademark of Adobe Systems Incorporated

date: 2008-12-13 14:57:21 +0100


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-alt-black.pfb .
ln -s %{_fontdir}/fourier-alt-black.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-alt-black.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-alt-bold.pfb .
ln -s %{_fontdir}/fourier-alt-bold.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-alt-bold.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-alt-boldita.pfb .
ln -s %{_fontdir}/fourier-alt-boldita.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-alt-boldita.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-alt-ita.pfb .
ln -s %{_fontdir}/fourier-alt-ita.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-alt-ita.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-alt-semi.pfb .
ln -s %{_fontdir}/fourier-alt-semi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-alt-semi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-alt-semiita.pfb .
ln -s %{_fontdir}/fourier-alt-semiita.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-alt-semiita.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-alt.pfb .
ln -s %{_fontdir}/fourier-alt.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-alt.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-bb.pfb .
ln -s %{_fontdir}/fourier-bb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-bb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-mcl.pfb .
ln -s %{_fontdir}/fourier-mcl.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-mcl.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-mex.pfb .
ln -s %{_fontdir}/fourier-mex.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-mex.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-ml.pfb .
ln -s %{_fontdir}/fourier-ml.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-ml.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-mlb.pfb .
ln -s %{_fontdir}/fourier-mlb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-mlb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-mlit.pfb .
ln -s %{_fontdir}/fourier-mlit.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-mlit.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-mlitb.pfb .
ln -s %{_fontdir}/fourier-mlitb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-mlitb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-ms.pfb .
ln -s %{_fontdir}/fourier-ms.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-ms.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-orns.pfb .
ln -s %{_fontdir}/fourier-orns.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-orns.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/fonts/afm/public/fourier/fourier-alt-black.afm
%{_texdir}/texmf-dist/fonts/afm/public/fourier/fourier-alt-bold.afm
%{_texdir}/texmf-dist/fonts/afm/public/fourier/fourier-alt-boldita.afm
%{_texdir}/texmf-dist/fonts/afm/public/fourier/fourier-alt-ita.afm
%{_texdir}/texmf-dist/fonts/afm/public/fourier/fourier-alt-semi.afm
%{_texdir}/texmf-dist/fonts/afm/public/fourier/fourier-alt-semiita.afm
%{_texdir}/texmf-dist/fonts/afm/public/fourier/fourier-alt.afm
%{_texdir}/texmf-dist/fonts/afm/public/fourier/fourier-bb.afm
%{_texdir}/texmf-dist/fonts/afm/public/fourier/fourier-mcl.afm
%{_texdir}/texmf-dist/fonts/afm/public/fourier/fourier-mex.afm
%{_texdir}/texmf-dist/fonts/afm/public/fourier/fourier-ml.afm
%{_texdir}/texmf-dist/fonts/afm/public/fourier/fourier-mlb.afm
%{_texdir}/texmf-dist/fonts/afm/public/fourier/fourier-mlit.afm
%{_texdir}/texmf-dist/fonts/afm/public/fourier/fourier-mlitb.afm
%{_texdir}/texmf-dist/fonts/afm/public/fourier/fourier-ms.afm
%{_texdir}/texmf-dist/fonts/afm/public/fourier/fourier-orns.afm
%{_texdir}/texmf-dist/fonts/map/dvips/fourier/fourier-utopia-expert.map
%{_texdir}/texmf-dist/fonts/map/dvips/fourier/fourier.map
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/fourier-alt-black.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/fourier-alt-bold-sl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/fourier-alt-bold.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/fourier-alt-boldita.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/fourier-alt-ita.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/fourier-alt-semi-sl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/fourier-alt-semi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/fourier-alt-semiita.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/fourier-alt-sl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/fourier-alt.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/fourier-bb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/fourier-mcl.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/fourier-mex.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/fourier-ml.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/fourier-mlb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/fourier-mlit.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/fourier-mlitb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/fourier-ms.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/fourier-orns.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futb8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futb8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futb8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futb8x.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futb9c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futb9d.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futb9e.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futbc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futbi8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futbi8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futbi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futbi8x.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futbi9c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futbi9d.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futbi9e.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futbo8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futbo8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futbo8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futbo8x.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futbo9c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futbo9d.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futbo9e.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futboorn.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futborn.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futc8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futc8x.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futc9c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futc9d.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futc9e.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futcorn.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futmib.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futmii.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futmiib.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futr8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futr8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futr8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futr8x.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futr9c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futr9d.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futr9e.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futrc8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futrc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futrc9d.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futrc9e.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futrd8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futrd8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futri8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futri8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futri8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futri8x.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futri9c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futri9d.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futri9e.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futro8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futro8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futro8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futro8x.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futro9c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futro9d.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futro9e.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futroorn.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futrorn.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futs8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futs8x.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futs9c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futs9d.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futs9e.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futsc8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futsc9d.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futsc9e.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futsi8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futsi8x.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futsi9c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futsi9d.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futsi9e.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futso8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futso8x.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futso9c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futso9d.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futso9e.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futsoorn.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futsorn.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/fourier/futsy.tfm
%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-alt-black.pfb
%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-alt-bold.pfb
%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-alt-boldita.pfb
%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-alt-ita.pfb
%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-alt-semi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-alt-semiita.pfb
%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-alt.pfb
%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-bb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-mcl.pfb
%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-mex.pfb
%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-ml.pfb
%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-mlb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-mlit.pfb
%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-mlitb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-ms.pfb
%{_texdir}/texmf-dist/fonts/type1/public/fourier/fourier-orns.pfb
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futb8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futb8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futb9c.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futb9d.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futb9e.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futbc8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futbi8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futbi8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futbi9c.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futbi9d.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futbi9e.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futbo8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futbo8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futbo9c.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futbo9d.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futbo9e.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futboorn.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futborn.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futc9c.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futc9d.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futc9e.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futcorn.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futmi.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futmib.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futmii.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futmiib.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futr8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futr8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futr9c.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futr9d.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futr9e.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futrc8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futrc9d.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futrc9e.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futrd8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futri8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futri8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futri9c.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futri9d.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futri9e.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futro8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futro8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futro9c.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futro9d.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futro9e.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futroorn.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futrorn.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futs9c.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futs9d.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futs9e.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futsc9d.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futsc9e.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futsi9c.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futsi9d.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futsi9e.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futso9c.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futso9d.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futso9e.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futsoorn.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futsorn.vf
%{_texdir}/texmf-dist/fonts/vf/public/fourier/futsy.vf
%{_texdir}/texmf-dist/tex/latex/fourier/fmlfutm.fd
%{_texdir}/texmf-dist/tex/latex/fourier/fmlfutmi.fd
%{_texdir}/texmf-dist/tex/latex/fourier/fmsfutm.fd
%{_texdir}/texmf-dist/tex/latex/fourier/fmxfutm.fd
%{_texdir}/texmf-dist/tex/latex/fourier/fourier-orns.sty
%{_texdir}/texmf-dist/tex/latex/fourier/fourier.sty
%{_texdir}/texmf-dist/tex/latex/fourier/t1futj.fd
%{_texdir}/texmf-dist/tex/latex/fourier/t1futs.fd
%{_texdir}/texmf-dist/tex/latex/fourier/t1futx.fd
%{_texdir}/texmf-dist/tex/latex/fourier/ts1futj.fd
%{_texdir}/texmf-dist/tex/latex/fourier/ts1futs.fd
%{_texdir}/texmf-dist/tex/latex/fourier/ts1futx.fd
%{_texdir}/texmf-dist/tex/latex/fourier/ufuts.fd

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/fonts/fourier/README
%{_texdir}/texmf-dist/doc/fonts/fourier/fourier-doc-en.pdf
%{_texdir}/texmf-dist/doc/fonts/fourier/fourier-doc-en.tex
%{_texdir}/texmf-dist/doc/fonts/fourier/fourier-orns.pdf
%{_texdir}/texmf-dist/doc/fonts/fourier/fourier-orns.tex

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/fourier-alt-black.pfb
%{_fontdir}/fourier-alt-bold.pfb
%{_fontdir}/fourier-alt-boldita.pfb
%{_fontdir}/fourier-alt-ita.pfb
%{_fontdir}/fourier-alt-semi.pfb
%{_fontdir}/fourier-alt-semiita.pfb
%{_fontdir}/fourier-alt.pfb
%{_fontdir}/fourier-bb.pfb
%{_fontdir}/fourier-mcl.pfb
%{_fontdir}/fourier-mex.pfb
%{_fontdir}/fourier-ml.pfb
%{_fontdir}/fourier-mlb.pfb
%{_fontdir}/fourier-mlit.pfb
%{_fontdir}/fourier-mlitb.pfb
%{_fontdir}/fourier-ms.pfb
%{_fontdir}/fourier-orns.pfb

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
