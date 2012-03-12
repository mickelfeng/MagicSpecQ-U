%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/mnsymbol.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/mnsymbol.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/mnsymbol.source.tar.xz

Name: texlive-mnsymbol
License: Public Domain
Summary: Mathematical symbol font for Adobe MinionPro
Version: %{tl_version}
Release: %{tl_noarch_release}.1.4.svn18651%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(MnSymbol.sty)
Requires: tex(textcomp.sty)
Requires: tex(eufrak.sty)
Requires: tex(amsmath.sty)
Requires: texlive-mnsymbol-fedora-fonts = %{tl_version}

%description
MnSymbol is a symbol font family, designed to be used in
conjunction with Adobe Minion Pro (via the MinionPro package).
Almost all of LaTeX and AMS mathematical symbols are provided;
remaining coverage is available from the MinionPro font with
the MinionPro package. The fonts are available in both MetaFont
and Adobe Type 1 formats, and a comprehensive support package
is provided. While the fonts were designed to fit with Minon
Pro, the design should fit well with other renaissance or
baroque faces: indeed, it will probably work with most fonts
that are neither too wide nor too thin, for example Palatino or
Times; it is known to look good with Sabon. There is no package
designed to configure its use with any font other than Minion
Pro, but (for example) simply loading mnsymbol after mathpazo
will probably do what is needed.

date: 2008-08-22 15:19:59 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map MnSymbol.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map MnSymbol.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for mnsymbol
Version: %{tl_version}
Release: %{tl_noarch_release}.1.4.svn18651%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for mnsymbol

%package fedora-fonts
Summary: Fonts for mnsymbol
Version: %{tl_version}
Release: %{tl_noarch_release}.1.4.svn18651%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-mnsymbol = %{tl_version}
BuildArch: noarch

%description fedora-fonts
MnSymbol is a symbol font family, designed to be used in
conjunction with Adobe Minion Pro (via the MinionPro package).
Almost all of LaTeX and AMS mathematical symbols are provided;
remaining coverage is available from the MinionPro font with
the MinionPro package. The fonts are available in both MetaFont
and Adobe Type 1 formats, and a comprehensive support package
is provided. While the fonts were designed to fit with Minon
Pro, the design should fit well with other renaissance or
baroque faces: indeed, it will probably work with most fonts
that are neither too wide nor too thin, for example Palatino or
Times; it is known to look good with Sabon. There is no package
designed to configure its use with any font other than Minion
Pro, but (for example) simply loading mnsymbol after mathpazo
will probably do what is needed.

date: 2008-08-22 15:19:59 +0200


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol-Bold10.otf .
ln -s %{_fontdir}/MnSymbol-Bold10.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol-Bold10.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol-Bold12.otf .
ln -s %{_fontdir}/MnSymbol-Bold12.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol-Bold12.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol-Bold5.otf .
ln -s %{_fontdir}/MnSymbol-Bold5.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol-Bold5.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol-Bold6.otf .
ln -s %{_fontdir}/MnSymbol-Bold6.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol-Bold6.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol-Bold7.otf .
ln -s %{_fontdir}/MnSymbol-Bold7.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol-Bold7.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol-Bold8.otf .
ln -s %{_fontdir}/MnSymbol-Bold8.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol-Bold8.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol-Bold9.otf .
ln -s %{_fontdir}/MnSymbol-Bold9.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol-Bold9.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol10.otf .
ln -s %{_fontdir}/MnSymbol10.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol10.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol12.otf .
ln -s %{_fontdir}/MnSymbol12.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol12.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol5.otf .
ln -s %{_fontdir}/MnSymbol5.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol5.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol6.otf .
ln -s %{_fontdir}/MnSymbol6.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol6.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol7.otf .
ln -s %{_fontdir}/MnSymbol7.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol7.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol8.otf .
ln -s %{_fontdir}/MnSymbol8.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol8.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol9.otf .
ln -s %{_fontdir}/MnSymbol9.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol9.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol-Bold10.pfb .
ln -s %{_fontdir}/MnSymbol-Bold10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol-Bold10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol-Bold12.pfb .
ln -s %{_fontdir}/MnSymbol-Bold12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol-Bold12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol-Bold5.pfb .
ln -s %{_fontdir}/MnSymbol-Bold5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol-Bold5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol-Bold6.pfb .
ln -s %{_fontdir}/MnSymbol-Bold6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol-Bold6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol-Bold7.pfb .
ln -s %{_fontdir}/MnSymbol-Bold7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol-Bold7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol-Bold8.pfb .
ln -s %{_fontdir}/MnSymbol-Bold8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol-Bold8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol-Bold9.pfb .
ln -s %{_fontdir}/MnSymbol-Bold9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol-Bold9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol10.pfb .
ln -s %{_fontdir}/MnSymbol10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol12.pfb .
ln -s %{_fontdir}/MnSymbol12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol5.pfb .
ln -s %{_fontdir}/MnSymbol5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol6.pfb .
ln -s %{_fontdir}/MnSymbol6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol7.pfb .
ln -s %{_fontdir}/MnSymbol7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol8.pfb .
ln -s %{_fontdir}/MnSymbol8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol9.pfb .
ln -s %{_fontdir}/MnSymbol9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol9.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc pd.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/mnsymbol/MnSymbolA.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/mnsymbol/MnSymbolB.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/mnsymbol/MnSymbolC.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/mnsymbol/MnSymbolD.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/mnsymbol/MnSymbolE.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/mnsymbol/MnSymbolF.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/mnsymbol/MnSymbolS.enc
%{_texdir}/texmf-dist/fonts/map/dvips/mnsymbol/MnSymbol.map
%{_texdir}/texmf-dist/fonts/map/vtex/mnsymbol/MnSymbol.ali
%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol-Bold10.otf
%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol-Bold12.otf
%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol-Bold5.otf
%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol-Bold6.otf
%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol-Bold7.otf
%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol-Bold8.otf
%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol-Bold9.otf
%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol10.otf
%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol12.otf
%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol5.otf
%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol6.otf
%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol7.otf
%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol8.otf
%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol/MnSymbol9.otf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbol-Parameter.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolA-Bold.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolA-Bold10.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolA-Bold12.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolA-Bold5.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolA-Bold6.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolA-Bold7.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolA-Bold8.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolA-Bold9.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolA.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolA10.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolA12.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolA5.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolA6.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolA7.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolA8.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolA9.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolB-Bold.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolB-Bold10.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolB-Bold12.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolB-Bold5.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolB-Bold6.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolB-Bold7.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolB-Bold8.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolB-Bold9.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolB.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolB10.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolB12.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolB5.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolB6.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolB7.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolB8.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolB9.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolC-Bold.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolC-Bold10.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolC-Bold12.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolC-Bold5.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolC-Bold6.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolC-Bold7.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolC-Bold8.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolC-Bold9.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolC.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolC10.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolC12.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolC5.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolC6.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolC7.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolC8.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolC9.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolD-Bold.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolD-Bold10.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolD-Bold12.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolD-Bold5.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolD-Bold6.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolD-Bold7.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolD-Bold8.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolD-Bold9.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolD.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolD10.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolD12.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolD5.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolD6.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolD7.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolD8.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolD9.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolE-Bold.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolE-Bold10.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolE-Bold12.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolE-Bold5.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolE-Bold6.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolE-Bold7.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolE-Bold8.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolE-Bold9.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolE.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolE10.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolE12.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolE5.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolE6.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolE7.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolE8.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolE9.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolF-Bold.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolF-Bold10.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolF-Bold12.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolF-Bold5.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolF-Bold6.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolF-Bold7.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolF-Bold8.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolF-Bold9.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolF.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolF10.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolF12.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolF5.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolF6.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolF7.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolF8.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolF9.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolS-Bold.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolS-Bold10.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolS-Bold12.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolS-Bold5.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolS-Bold6.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolS-Bold7.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolS-Bold8.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolS-Bold9.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolS.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolS10.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolS12.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolS5.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolS6.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolS7.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolS8.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/MnSymbolS9.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/Sym-Accent.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/Sym-Arrows.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/Sym-Base.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/Sym-Delim.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/Sym-Geometric.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/Sym-Init.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/Sym-Operators.mf
%{_texdir}/texmf-dist/fonts/source/public/mnsymbol/Sym-Order.mf
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolA-Bold10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolA-Bold12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolA-Bold5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolA-Bold6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolA-Bold7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolA-Bold8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolA-Bold9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolA10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolA12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolA5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolA6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolA7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolA8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolA9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolB-Bold10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolB-Bold12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolB-Bold5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolB-Bold6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolB-Bold7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolB-Bold8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolB-Bold9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolB10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolB12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolB5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolB6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolB7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolB8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolB9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolC-Bold10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolC-Bold12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolC-Bold5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolC-Bold6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolC-Bold7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolC-Bold8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolC-Bold9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolC10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolC12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolC5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolC6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolC7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolC8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolC9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolD-Bold10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolD-Bold12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolD-Bold5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolD-Bold6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolD-Bold7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolD-Bold8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolD-Bold9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolD10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolD12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolD5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolD6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolD7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolD8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolD9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolE-Bold10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolE-Bold12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolE-Bold5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolE-Bold6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolE-Bold7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolE-Bold8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolE-Bold9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolE10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolE12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolE5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolE6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolE7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolE8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolE9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolF-Bold10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolF-Bold12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolF-Bold5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolF-Bold6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolF-Bold7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolF-Bold8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolF-Bold9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolF10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolF12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolF5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolF6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolF7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolF8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolF9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolS-Bold10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolS-Bold12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolS-Bold5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolS-Bold6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolS-Bold7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolS-Bold8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolS-Bold9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolS10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolS12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolS5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolS6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolS7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolS8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol/MnSymbolS9.tfm
%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol-Bold10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol-Bold12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol-Bold5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol-Bold6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol-Bold7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol-Bold8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol-Bold9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol/MnSymbol9.pfb
%{_texdir}/texmf-dist/tex/latex/mnsymbol/MnSymbol.sty

%files doc
%defattr(-,root,root)
%doc pd.txt
%{_texdir}/texmf-dist/doc/latex/mnsymbol/MnSymbol.pdf
%{_texdir}/texmf-dist/doc/latex/mnsymbol/README

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/MnSymbol-Bold10.otf
%{_fontdir}/MnSymbol-Bold12.otf
%{_fontdir}/MnSymbol-Bold5.otf
%{_fontdir}/MnSymbol-Bold6.otf
%{_fontdir}/MnSymbol-Bold7.otf
%{_fontdir}/MnSymbol-Bold8.otf
%{_fontdir}/MnSymbol-Bold9.otf
%{_fontdir}/MnSymbol10.otf
%{_fontdir}/MnSymbol12.otf
%{_fontdir}/MnSymbol5.otf
%{_fontdir}/MnSymbol6.otf
%{_fontdir}/MnSymbol7.otf
%{_fontdir}/MnSymbol8.otf
%{_fontdir}/MnSymbol9.otf
%{_fontdir}/MnSymbol-Bold10.pfb
%{_fontdir}/MnSymbol-Bold12.pfb
%{_fontdir}/MnSymbol-Bold5.pfb
%{_fontdir}/MnSymbol-Bold6.pfb
%{_fontdir}/MnSymbol-Bold7.pfb
%{_fontdir}/MnSymbol-Bold8.pfb
%{_fontdir}/MnSymbol-Bold9.pfb
%{_fontdir}/MnSymbol10.pfb
%{_fontdir}/MnSymbol12.pfb
%{_fontdir}/MnSymbol5.pfb
%{_fontdir}/MnSymbol6.pfb
%{_fontdir}/MnSymbol7.pfb
%{_fontdir}/MnSymbol8.pfb
%{_fontdir}/MnSymbol9.pfb

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
