%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cm-lgc.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cm-lgc.doc.tar.xz

Name: texlive-cm-lgc
License: GPL+
Summary: Type 1 CM-based fonts for Latin, Greek and Cyrillic
Version: %{tl_version}
Release: %{tl_noarch_release}.0.5.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(antcmlgc.sty)
Provides: tex(cmlgc.sty)
Requires: texlive-cm-lgc-fedora-fonts = %{tl_version}

%description
The fonts are converted from MetaFont sources of the Computer
Modern font families, using textrace. Supported encodings are:
T1 (Latin), T2A (Cyrillic), LGR (Greek) and TS1. The package
also includes Unicode virtual fonts for use with Omega. The
font set is not a replacement for any of the other Computer
Modern-based font sets (for example, cm-super for Latin and
Cyrillic, or cbgreek for Greek), since it is available at a
single size only; it offers a compact set for 'general'
working. The fonts themselves are encoded to external
standards, and virtual fonts are provided for use with TeX.

date: 2008-06-12 19:44:55 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map cm-lgc.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map cm-lgc.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for cm-lgc
Version: %{tl_version}
Release: %{tl_noarch_release}.0.5.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for cm-lgc

%package fedora-fonts
Summary: Fonts for cm-lgc
Version: %{tl_version}
Release: %{tl_noarch_release}.0.5.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-cm-lgc = %{tl_version}
BuildArch: noarch

%description fedora-fonts
The fonts are converted from MetaFont sources of the Computer
Modern font families, using textrace. Supported encodings are:
T1 (Latin), T2A (Cyrillic), LGR (Greek) and TS1. The package
also includes Unicode virtual fonts for use with Omega. The
font set is not a replacement for any of the other Computer
Modern-based font sets (for example, cm-super for Latin and
Cyrillic, or cbgreek for Greek), since it is available at a
single size only; it offers a compact set for 'general'
working. The fonts themselves are encoded to external
standards, and virtual fonts are provided for use with TeX.

date: 2008-06-12 19:44:55 +0200


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmb6y.pfb .
ln -s %{_fontdir}/fcmb6y.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmb6y.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmb6z.pfb .
ln -s %{_fontdir}/fcmb6z.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmb6z.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmb8a.pfb .
ln -s %{_fontdir}/fcmb8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmb8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbc6y.pfb .
ln -s %{_fontdir}/fcmbc6y.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbc6y.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbc6z.pfb .
ln -s %{_fontdir}/fcmbc6z.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbc6z.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbc8a.pfb .
ln -s %{_fontdir}/fcmbc8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbc8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbcpg.pfb .
ln -s %{_fontdir}/fcmbcpg.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbcpg.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbi6y.pfb .
ln -s %{_fontdir}/fcmbi6y.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbi6y.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbi6z.pfb .
ln -s %{_fontdir}/fcmbi6z.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbi6z.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbi8a.pfb .
ln -s %{_fontdir}/fcmbi8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbi8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbij6y.pfb .
ln -s %{_fontdir}/fcmbij6y.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbij6y.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbij6z.pfb .
ln -s %{_fontdir}/fcmbij6z.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbij6z.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbij8a.pfb .
ln -s %{_fontdir}/fcmbij8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbij8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbijpg.pfb .
ln -s %{_fontdir}/fcmbijpg.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbijpg.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbipg.pfb .
ln -s %{_fontdir}/fcmbipg.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbipg.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbpg.pfb .
ln -s %{_fontdir}/fcmbpg.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbpg.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmr6y.pfb .
ln -s %{_fontdir}/fcmr6y.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmr6y.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmr6z.pfb .
ln -s %{_fontdir}/fcmr6z.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmr6z.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmr8a.pfb .
ln -s %{_fontdir}/fcmr8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmr8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrc6y.pfb .
ln -s %{_fontdir}/fcmrc6y.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrc6y.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrc6z.pfb .
ln -s %{_fontdir}/fcmrc6z.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrc6z.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrc8a.pfb .
ln -s %{_fontdir}/fcmrc8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrc8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrcpg.pfb .
ln -s %{_fontdir}/fcmrcpg.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrcpg.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmri6y.pfb .
ln -s %{_fontdir}/fcmri6y.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmri6y.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmri6z.pfb .
ln -s %{_fontdir}/fcmri6z.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmri6z.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmri8a.pfb .
ln -s %{_fontdir}/fcmri8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmri8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrij6y.pfb .
ln -s %{_fontdir}/fcmrij6y.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrij6y.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrij6z.pfb .
ln -s %{_fontdir}/fcmrij6z.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrij6z.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrij8a.pfb .
ln -s %{_fontdir}/fcmrij8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrij8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrijpg.pfb .
ln -s %{_fontdir}/fcmrijpg.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrijpg.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmripg.pfb .
ln -s %{_fontdir}/fcmripg.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmripg.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrpg.pfb .
ln -s %{_fontdir}/fcmrpg.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrpg.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsb6y.pfb .
ln -s %{_fontdir}/fcsb6y.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsb6y.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsb6z.pfb .
ln -s %{_fontdir}/fcsb6z.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsb6z.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsb8a.pfb .
ln -s %{_fontdir}/fcsb8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsb8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsbo6y.pfb .
ln -s %{_fontdir}/fcsbo6y.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsbo6y.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsbo6z.pfb .
ln -s %{_fontdir}/fcsbo6z.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsbo6z.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsbo8a.pfb .
ln -s %{_fontdir}/fcsbo8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsbo8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsbopg.pfb .
ln -s %{_fontdir}/fcsbopg.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsbopg.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsbpg.pfb .
ln -s %{_fontdir}/fcsbpg.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsbpg.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsr6y.pfb .
ln -s %{_fontdir}/fcsr6y.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsr6y.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsr6z.pfb .
ln -s %{_fontdir}/fcsr6z.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsr6z.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsr8a.pfb .
ln -s %{_fontdir}/fcsr8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsr8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsro6y.pfb .
ln -s %{_fontdir}/fcsro6y.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsro6y.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsro6z.pfb .
ln -s %{_fontdir}/fcsro6z.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsro6z.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsro8a.pfb .
ln -s %{_fontdir}/fcsro8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsro8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsropg.pfb .
ln -s %{_fontdir}/fcsropg.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsropg.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsrpg.pfb .
ln -s %{_fontdir}/fcsrpg.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsrpg.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctr6y.pfb .
ln -s %{_fontdir}/fctr6y.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctr6y.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctr6z.pfb .
ln -s %{_fontdir}/fctr6z.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctr6z.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctr8a.pfb .
ln -s %{_fontdir}/fctr8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctr8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrc6y.pfb .
ln -s %{_fontdir}/fctrc6y.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrc6y.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrc6z.pfb .
ln -s %{_fontdir}/fctrc6z.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrc6z.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrc8a.pfb .
ln -s %{_fontdir}/fctrc8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrc8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrcpg.pfb .
ln -s %{_fontdir}/fctrcpg.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrcpg.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctri6y.pfb .
ln -s %{_fontdir}/fctri6y.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctri6y.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctri6z.pfb .
ln -s %{_fontdir}/fctri6z.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctri6z.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctri8a.pfb .
ln -s %{_fontdir}/fctri8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctri8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrij6y.pfb .
ln -s %{_fontdir}/fctrij6y.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrij6y.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrij6z.pfb .
ln -s %{_fontdir}/fctrij6z.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrij6z.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrij8a.pfb .
ln -s %{_fontdir}/fctrij8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrij8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrijpg.pfb .
ln -s %{_fontdir}/fctrijpg.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrijpg.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctripg.pfb .
ln -s %{_fontdir}/fctripg.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctripg.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrpg.pfb .
ln -s %{_fontdir}/fctrpg.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrpg.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmb6y.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmb6z.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmb8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmbc6y.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmbc6z.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmbc8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmbcpg.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmbi6y.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmbi6z.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmbi8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmbij6y.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmbij6z.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmbij8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmbijpg.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmbipg.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmbpg.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmr6y.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmr6z.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmr8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmrc6y.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmrc6z.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmrc8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmrcpg.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmri6y.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmri6z.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmri8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmrij6y.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmrij6z.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmrij8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmrijpg.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmripg.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcmrpg.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcsb6y.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcsb6z.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcsb8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcsbo6y.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcsbo6z.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcsbo8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcsbopg.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcsbpg.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcsr6y.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcsr6z.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcsr8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcsro6y.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcsro6z.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcsro8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcsropg.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fcsrpg.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fctr6y.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fctr6z.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fctr8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fctrc6y.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fctrc6z.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fctrc8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fctrcpg.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fctri6y.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fctri6z.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fctri8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fctrij6y.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fctrij6z.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fctrij8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fctrijpg.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fctripg.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/fctrpg.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-lgc/8r-mod.enc
%{_texdir}/texmf-dist/fonts/map/dvips/cm-lgc/cm-lgc.map
%{_texdir}/texmf-dist/fonts/ofm/public/cm-lgc/fcmbcut.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/cm-lgc/fcmbiut.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/cm-lgc/fcmbut.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/cm-lgc/fcmrcut.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/cm-lgc/fcmriut.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/cm-lgc/fcmrut.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/cm-lgc/fcsbout.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/cm-lgc/fcsbut.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/cm-lgc/fcsrout.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/cm-lgc/fcsrut.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/cm-lgc/fctrcut.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/cm-lgc/fctriut.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/cm-lgc/fctrut.ofm
%{_texdir}/texmf-dist/fonts/ovf/public/cm-lgc/fcmbcut.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/cm-lgc/fcmbiut.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/cm-lgc/fcmbut.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/cm-lgc/fcmrcut.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/cm-lgc/fcmriut.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/cm-lgc/fcmrut.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/cm-lgc/fcsbout.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/cm-lgc/fcsbut.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/cm-lgc/fcsrout.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/cm-lgc/fcsrut.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/cm-lgc/fctrcut.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/cm-lgc/fctriut.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/cm-lgc/fctrut.ovf
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmb6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmb6y.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmb6z.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmb8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmb8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmb8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmb8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmbc6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmbc6y.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmbc6z.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmbc8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmbc8r-nokern.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmbc8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmbc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmbcgr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmbcpg.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmbgr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmbi6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmbi6y.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmbi6z.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmbi8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmbi8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmbi8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmbi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmbigr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmbij6z.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmbij8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmbij8r-nokern.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmbij8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmbipg.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmbpg.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmr6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmr6y.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmr6z.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmr8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmr8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmr8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmr8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmrc6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmrc6y.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmrc6z.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmrc8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmrc8r-nokern.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmrc8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmrc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmrcgr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmrcpg.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmrgr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmri6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmri6y.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmri6z.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmri8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmri8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmri8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmri8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmrigr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmrij6z.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmrij8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmrij8r-nokern.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmrij8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmripg.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcmrpg.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsb6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsb6y.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsb6z.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsb8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsb8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsb8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsb8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsbgr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsbo6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsbo6y.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsbo6z.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsbo8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsbo8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsbo8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsbo8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsbogr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsbopg.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsbpg.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsr6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsr6y.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsr6z.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsr8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsr8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsr8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsr8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsrgr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsro6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsro6y.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsro6z.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsro8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsro8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsro8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsro8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsrogr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsropg.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fcsrpg.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctr6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctr6y.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctr6z.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctr8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctr8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctr8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctr8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctrc6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctrc6y.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctrc6z.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctrc8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctrc8r-nokern.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctrc8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctrc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctrcgr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctrcpg.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctrgr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctri6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctri6y.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctri6z.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctri8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctri8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctri8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctri8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctrigr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctrij6z.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctrij8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctrij8r-nokern.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctrij8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctripg.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/fctrpg.tfm
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmb6y.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmb6y.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmb6z.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmb6z.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmb8a.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmb8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbc6y.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbc6y.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbc6z.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbc6z.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbc8a.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbc8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbcpg.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbcpg.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbi6y.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbi6y.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbi6z.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbi6z.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbi8a.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbi8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbij6y.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbij6y.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbij6z.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbij6z.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbij8a.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbij8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbijpg.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbijpg.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbipg.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbipg.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbpg.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmbpg.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmr6y.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmr6y.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmr6z.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmr6z.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmr8a.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmr8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrc6y.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrc6y.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrc6z.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrc6z.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrc8a.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrc8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrcpg.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrcpg.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmri6y.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmri6y.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmri6z.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmri6z.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmri8a.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmri8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrij6y.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrij6y.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrij6z.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrij6z.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrij8a.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrij8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrijpg.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrijpg.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmripg.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmripg.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrpg.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcmrpg.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsb6y.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsb6y.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsb6z.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsb6z.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsb8a.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsb8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsbo6y.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsbo6y.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsbo6z.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsbo6z.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsbo8a.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsbo8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsbopg.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsbopg.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsbpg.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsbpg.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsr6y.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsr6y.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsr6z.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsr6z.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsr8a.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsr8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsro6y.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsro6y.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsro6z.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsro6z.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsro8a.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsro8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsropg.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsropg.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsrpg.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fcsrpg.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctr6y.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctr6y.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctr6z.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctr6z.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctr8a.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctr8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrc6y.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrc6y.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrc6z.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrc6z.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrc8a.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrc8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrcpg.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrcpg.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctri6y.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctri6y.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctri6z.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctri6z.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctri8a.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctri8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrij6y.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrij6y.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrij6z.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrij6z.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrij8a.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrij8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrijpg.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrijpg.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctripg.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctripg.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrpg.inf
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/fctrpg.pfb
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcmb6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcmb8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcmb8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcmbc6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcmbc8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcmbcgr.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcmbgr.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcmbi6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcmbi8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcmbi8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcmbigr.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcmr6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcmr8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcmr8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcmrc6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcmrc8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcmrcgr.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcmrgr.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcmri6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcmri8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcmri8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcmrigr.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcsb6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcsb8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcsb8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcsbgr.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcsbo6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcsbo8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcsbo8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcsbogr.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcsr6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcsr8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcsr8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcsrgr.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcsro6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcsro8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcsro8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fcsrogr.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fctr6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fctr8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fctr8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fctrc6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fctrc8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fctrcgr.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fctrgr.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fctri6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fctri8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fctri8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/fctrigr.vf
%{_texdir}/texmf-dist/tex/latex/cm-lgc/antcmlgc.sty
%{_texdir}/texmf-dist/tex/latex/cm-lgc/cmlgc.sty
%{_texdir}/texmf-dist/tex/latex/cm-lgc/lgrfcm.fd
%{_texdir}/texmf-dist/tex/latex/cm-lgc/lgrfcs.fd
%{_texdir}/texmf-dist/tex/latex/cm-lgc/lgrfct.fd
%{_texdir}/texmf-dist/tex/latex/cm-lgc/t1fcm.fd
%{_texdir}/texmf-dist/tex/latex/cm-lgc/t1fcs.fd
%{_texdir}/texmf-dist/tex/latex/cm-lgc/t1fct.fd
%{_texdir}/texmf-dist/tex/latex/cm-lgc/t2afcm.fd
%{_texdir}/texmf-dist/tex/latex/cm-lgc/t2afcs.fd
%{_texdir}/texmf-dist/tex/latex/cm-lgc/t2afct.fd
%{_texdir}/texmf-dist/tex/latex/cm-lgc/ts1fcm.fd
%{_texdir}/texmf-dist/tex/latex/cm-lgc/ts1fcs.fd
%{_texdir}/texmf-dist/tex/latex/cm-lgc/ts1fct.fd
%{_texdir}/texmf-dist/tex/latex/cm-lgc/ut1fcm.fd
%{_texdir}/texmf-dist/tex/latex/cm-lgc/ut1fcs.fd
%{_texdir}/texmf-dist/tex/latex/cm-lgc/ut1fct.fd

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/latex/cm-lgc/COPYING
%{_texdir}/texmf-dist/doc/latex/cm-lgc/HISTORY
%{_texdir}/texmf-dist/doc/latex/cm-lgc/INSTALL
%{_texdir}/texmf-dist/doc/latex/cm-lgc/README

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/fcmb6y.pfb
%{_fontdir}/fcmb6z.pfb
%{_fontdir}/fcmb8a.pfb
%{_fontdir}/fcmbc6y.pfb
%{_fontdir}/fcmbc6z.pfb
%{_fontdir}/fcmbc8a.pfb
%{_fontdir}/fcmbcpg.pfb
%{_fontdir}/fcmbi6y.pfb
%{_fontdir}/fcmbi6z.pfb
%{_fontdir}/fcmbi8a.pfb
%{_fontdir}/fcmbij6y.pfb
%{_fontdir}/fcmbij6z.pfb
%{_fontdir}/fcmbij8a.pfb
%{_fontdir}/fcmbijpg.pfb
%{_fontdir}/fcmbipg.pfb
%{_fontdir}/fcmbpg.pfb
%{_fontdir}/fcmr6y.pfb
%{_fontdir}/fcmr6z.pfb
%{_fontdir}/fcmr8a.pfb
%{_fontdir}/fcmrc6y.pfb
%{_fontdir}/fcmrc6z.pfb
%{_fontdir}/fcmrc8a.pfb
%{_fontdir}/fcmrcpg.pfb
%{_fontdir}/fcmri6y.pfb
%{_fontdir}/fcmri6z.pfb
%{_fontdir}/fcmri8a.pfb
%{_fontdir}/fcmrij6y.pfb
%{_fontdir}/fcmrij6z.pfb
%{_fontdir}/fcmrij8a.pfb
%{_fontdir}/fcmrijpg.pfb
%{_fontdir}/fcmripg.pfb
%{_fontdir}/fcmrpg.pfb
%{_fontdir}/fcsb6y.pfb
%{_fontdir}/fcsb6z.pfb
%{_fontdir}/fcsb8a.pfb
%{_fontdir}/fcsbo6y.pfb
%{_fontdir}/fcsbo6z.pfb
%{_fontdir}/fcsbo8a.pfb
%{_fontdir}/fcsbopg.pfb
%{_fontdir}/fcsbpg.pfb
%{_fontdir}/fcsr6y.pfb
%{_fontdir}/fcsr6z.pfb
%{_fontdir}/fcsr8a.pfb
%{_fontdir}/fcsro6y.pfb
%{_fontdir}/fcsro6z.pfb
%{_fontdir}/fcsro8a.pfb
%{_fontdir}/fcsropg.pfb
%{_fontdir}/fcsrpg.pfb
%{_fontdir}/fctr6y.pfb
%{_fontdir}/fctr6z.pfb
%{_fontdir}/fctr8a.pfb
%{_fontdir}/fctrc6y.pfb
%{_fontdir}/fctrc6z.pfb
%{_fontdir}/fctrc8a.pfb
%{_fontdir}/fctrcpg.pfb
%{_fontdir}/fctri6y.pfb
%{_fontdir}/fctri6z.pfb
%{_fontdir}/fctri8a.pfb
%{_fontdir}/fctrij6y.pfb
%{_fontdir}/fctrij6z.pfb
%{_fontdir}/fctrij8a.pfb
%{_fontdir}/fctrijpg.pfb
%{_fontdir}/fctripg.pfb
%{_fontdir}/fctrpg.pfb

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
