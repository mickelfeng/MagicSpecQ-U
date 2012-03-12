%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cm-unicode.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cm-unicode.doc.tar.xz

Name: texlive-cm-unicode
License: OFSFLD
Summary: Computer Modern Unicode font family
Version: %{tl_version}
Release: %{tl_noarch_release}.0.7.0.svn19445%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-cm-unicode-fedora-fonts = %{tl_version}

%description
Computer Modern Unicode fonts were converted from metafont
sources using mftrace with autotrace backend and fontforge.
Some characters in several fonts are copied from Blue Sky type
1 fonts released by AMS. Currently the fonts contain glyphs
from Latin (Metafont ec, tc, vnr), Cyrillic (lh), Greek
(cbgreek when available) code sets and IPA extensions (from
tipa). This font set contains 33 fonts. This archive contains
AFM, PFB and OTF versions; the OTF version of the Computer
Modern Unicode fonts works with TeX engines that directly
support OpenType features, such as XeTeX and LuaTeX.

date: 2010-07-13 15:28:23 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
:

%postun
if [ $1 == 1 ]; then
  mkdir -p /var/run/texlive
  touch /var/run/run-texhash
else
  %{_bindir}/texhash 2> /dev/null
fi
:

%posttrans
[ -e /var/run/texlive/run-texhash ] && %{_bindir}/texhash 2> /dev/null && rm -f /var/run/texlive/run-texhash
[ -e /var/run/texlive ] && rm -rf /var/run/texlive
:

%package doc
Summary: Documentation for cm-unicode
Version: %{tl_version}
Release: %{tl_noarch_release}.0.7.0.svn19445%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for cm-unicode

%package fedora-fonts
Summary: Fonts for cm-unicode
Version: %{tl_version}
Release: %{tl_noarch_release}.0.7.0.svn19445%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-cm-unicode = %{tl_version}
BuildArch: noarch

%description fedora-fonts
Computer Modern Unicode fonts were converted from metafont
sources using mftrace with autotrace backend and fontforge.
Some characters in several fonts are copied from Blue Sky type
1 fonts released by AMS. Currently the fonts contain glyphs
from Latin (Metafont ec, tc, vnr), Cyrillic (lh), Greek
(cbgreek when available) code sets and IPA extensions (from
tipa). This font set contains 33 fonts. This archive contains
AFM, PFB and OTF versions; the OTF version of the Computer
Modern Unicode fonts works with TeX engines that directly
support OpenType features, such as XeTeX and LuaTeX.

date: 2010-07-13 15:28:23 +0200


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbbx.otf .
ln -s %{_fontdir}/cmunbbx.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbbx.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbi.otf .
ln -s %{_fontdir}/cmunbi.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbi.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbl.otf .
ln -s %{_fontdir}/cmunbl.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbl.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbmo.otf .
ln -s %{_fontdir}/cmunbmo.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbmo.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbmr.otf .
ln -s %{_fontdir}/cmunbmr.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbmr.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbso.otf .
ln -s %{_fontdir}/cmunbso.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbso.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbsr.otf .
ln -s %{_fontdir}/cmunbsr.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbsr.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbtl.otf .
ln -s %{_fontdir}/cmunbtl.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbtl.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbto.otf .
ln -s %{_fontdir}/cmunbto.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbto.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbx.otf .
ln -s %{_fontdir}/cmunbx.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbx.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbxo.otf .
ln -s %{_fontdir}/cmunbxo.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbxo.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunci.otf .
ln -s %{_fontdir}/cmunci.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunci.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunit.otf .
ln -s %{_fontdir}/cmunit.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunit.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunobi.otf .
ln -s %{_fontdir}/cmunobi.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunobi.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunobx.otf .
ln -s %{_fontdir}/cmunobx.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunobx.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunorm.otf .
ln -s %{_fontdir}/cmunorm.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunorm.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunoti.otf .
ln -s %{_fontdir}/cmunoti.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunoti.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunrb.otf .
ln -s %{_fontdir}/cmunrb.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunrb.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunrm.otf .
ln -s %{_fontdir}/cmunrm.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunrm.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunsi.otf .
ln -s %{_fontdir}/cmunsi.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunsi.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunsl.otf .
ln -s %{_fontdir}/cmunsl.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunsl.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunso.otf .
ln -s %{_fontdir}/cmunso.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunso.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunss.otf .
ln -s %{_fontdir}/cmunss.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunss.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunssdc.otf .
ln -s %{_fontdir}/cmunssdc.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunssdc.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunst.otf .
ln -s %{_fontdir}/cmunst.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunst.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunsx.otf .
ln -s %{_fontdir}/cmunsx.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunsx.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmuntb.otf .
ln -s %{_fontdir}/cmuntb.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmuntb.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunti.otf .
ln -s %{_fontdir}/cmunti.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunti.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmuntt.otf .
ln -s %{_fontdir}/cmuntt.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmuntt.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmuntx.otf .
ln -s %{_fontdir}/cmuntx.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmuntx.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunui.otf .
ln -s %{_fontdir}/cmunui.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunui.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunvi.otf .
ln -s %{_fontdir}/cmunvi.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunvi.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunvt.otf .
ln -s %{_fontdir}/cmunvt.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunvt.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbbx.pfb .
ln -s %{_fontdir}/cmunbbx.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbbx.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbi.pfb .
ln -s %{_fontdir}/cmunbi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbl.pfb .
ln -s %{_fontdir}/cmunbl.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbl.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbmo.pfb .
ln -s %{_fontdir}/cmunbmo.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbmo.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbmr.pfb .
ln -s %{_fontdir}/cmunbmr.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbmr.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbso.pfb .
ln -s %{_fontdir}/cmunbso.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbso.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbsr.pfb .
ln -s %{_fontdir}/cmunbsr.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbsr.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbtl.pfb .
ln -s %{_fontdir}/cmunbtl.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbtl.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbto.pfb .
ln -s %{_fontdir}/cmunbto.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbto.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbx.pfb .
ln -s %{_fontdir}/cmunbx.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbx.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbxo.pfb .
ln -s %{_fontdir}/cmunbxo.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbxo.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunci.pfb .
ln -s %{_fontdir}/cmunci.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunci.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunit.pfb .
ln -s %{_fontdir}/cmunit.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunit.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunobi.pfb .
ln -s %{_fontdir}/cmunobi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunobi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunobx.pfb .
ln -s %{_fontdir}/cmunobx.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunobx.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunorm.pfb .
ln -s %{_fontdir}/cmunorm.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunorm.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunoti.pfb .
ln -s %{_fontdir}/cmunoti.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunoti.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunrb.pfb .
ln -s %{_fontdir}/cmunrb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunrb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunrm.pfb .
ln -s %{_fontdir}/cmunrm.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunrm.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunsi.pfb .
ln -s %{_fontdir}/cmunsi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunsi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunsl.pfb .
ln -s %{_fontdir}/cmunsl.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunsl.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunso.pfb .
ln -s %{_fontdir}/cmunso.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunso.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunss.pfb .
ln -s %{_fontdir}/cmunss.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunss.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunssdc.pfb .
ln -s %{_fontdir}/cmunssdc.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunssdc.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunst.pfb .
ln -s %{_fontdir}/cmunst.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunst.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunsx.pfb .
ln -s %{_fontdir}/cmunsx.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunsx.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmuntb.pfb .
ln -s %{_fontdir}/cmuntb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmuntb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunti.pfb .
ln -s %{_fontdir}/cmunti.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunti.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmuntt.pfb .
ln -s %{_fontdir}/cmuntt.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmuntt.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmuntx.pfb .
ln -s %{_fontdir}/cmuntx.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmuntx.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunui.pfb .
ln -s %{_fontdir}/cmunui.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunui.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunvi.pfb .
ln -s %{_fontdir}/cmunvi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunvi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunvt.pfb .
ln -s %{_fontdir}/cmunvt.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunvt.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc ofl.txt
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunbbx.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunbl.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunbmo.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunbmr.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunbso.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunbsr.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunbtl.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunbto.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunbx.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunbxo.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunci.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunit.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunobi.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunobx.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunorm.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunoti.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunrb.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunrm.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunsi.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunsl.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunso.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunss.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunssdc.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunst.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunsx.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmuntb.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunti.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmuntt.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmuntx.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunui.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunvi.afm
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/cmunvt.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-unicode/cmu-ec.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-unicode/cmu-ecsc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-unicode/cmu-g.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-unicode/cmu-gsc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-unicode/cmu-la.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-unicode/cmu-lasc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-unicode/cmu-lb.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-unicode/cmu-lc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-unicode/cmu-ld.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-unicode/cmu-rx.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-unicode/cmu-tc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-unicode/cmu-tipa.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-unicode/cmu-tipx.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-unicode/cmu-ux.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-unicode/cmu-uxsc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-unicode/cmu-vn.enc
%{_texdir}/texmf-dist/fonts/map/dvips/cm-unicode/cmu.map
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbbx.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbi.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbl.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbmo.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbmr.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbso.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbsr.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbtl.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbto.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbx.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunbxo.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunci.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunit.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunobi.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunobx.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunorm.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunoti.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunrb.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunrm.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunsi.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunsl.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunso.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunss.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunssdc.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunst.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunsx.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmuntb.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunti.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmuntt.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmuntx.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunui.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunvi.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/cmunvt.otf
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbbx.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbl.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbmo.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbmr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbso.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbsr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbtl.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbto.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbx.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunbxo.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunci.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunit.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunobi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunobx.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunorm.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunoti.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunrb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunrm.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunsi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunsl.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunso.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunss.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunssdc.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunst.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunsx.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmuntb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunti.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmuntt.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmuntx.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunui.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunvi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/cmunvt.pfb

%files doc
%defattr(-,root,root)
%doc ofl.txt
%{_texdir}/texmf-dist/doc/fonts/cm-unicode/Changes
%{_texdir}/texmf-dist/doc/fonts/cm-unicode/FAQ
%{_texdir}/texmf-dist/doc/fonts/cm-unicode/FontLog.txt
%{_texdir}/texmf-dist/doc/fonts/cm-unicode/Fontmap.CMU.alias
%{_texdir}/texmf-dist/doc/fonts/cm-unicode/Fontmap.CMU.otf
%{_texdir}/texmf-dist/doc/fonts/cm-unicode/Fontmap.CMU.pfb
%{_texdir}/texmf-dist/doc/fonts/cm-unicode/INSTALL
%{_texdir}/texmf-dist/doc/fonts/cm-unicode/OFL-FAQ.txt
%{_texdir}/texmf-dist/doc/fonts/cm-unicode/OFL.txt
%{_texdir}/texmf-dist/doc/fonts/cm-unicode/README
%{_texdir}/texmf-dist/doc/fonts/cm-unicode/README.doc
%{_texdir}/texmf-dist/doc/fonts/cm-unicode/TODO
%{_texdir}/texmf-dist/doc/fonts/cm-unicode/cmunrm.pdf
%{_texdir}/texmf-dist/doc/fonts/cm-unicode/cmunti.pdf
%{_texdir}/texmf-dist/doc/fonts/cm-unicode/config.cmu

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/cmunbbx.otf
%{_fontdir}/cmunbi.otf
%{_fontdir}/cmunbl.otf
%{_fontdir}/cmunbmo.otf
%{_fontdir}/cmunbmr.otf
%{_fontdir}/cmunbso.otf
%{_fontdir}/cmunbsr.otf
%{_fontdir}/cmunbtl.otf
%{_fontdir}/cmunbto.otf
%{_fontdir}/cmunbx.otf
%{_fontdir}/cmunbxo.otf
%{_fontdir}/cmunci.otf
%{_fontdir}/cmunit.otf
%{_fontdir}/cmunobi.otf
%{_fontdir}/cmunobx.otf
%{_fontdir}/cmunorm.otf
%{_fontdir}/cmunoti.otf
%{_fontdir}/cmunrb.otf
%{_fontdir}/cmunrm.otf
%{_fontdir}/cmunsi.otf
%{_fontdir}/cmunsl.otf
%{_fontdir}/cmunso.otf
%{_fontdir}/cmunss.otf
%{_fontdir}/cmunssdc.otf
%{_fontdir}/cmunst.otf
%{_fontdir}/cmunsx.otf
%{_fontdir}/cmuntb.otf
%{_fontdir}/cmunti.otf
%{_fontdir}/cmuntt.otf
%{_fontdir}/cmuntx.otf
%{_fontdir}/cmunui.otf
%{_fontdir}/cmunvi.otf
%{_fontdir}/cmunvt.otf
%{_fontdir}/cmunbbx.pfb
%{_fontdir}/cmunbi.pfb
%{_fontdir}/cmunbl.pfb
%{_fontdir}/cmunbmo.pfb
%{_fontdir}/cmunbmr.pfb
%{_fontdir}/cmunbso.pfb
%{_fontdir}/cmunbsr.pfb
%{_fontdir}/cmunbtl.pfb
%{_fontdir}/cmunbto.pfb
%{_fontdir}/cmunbx.pfb
%{_fontdir}/cmunbxo.pfb
%{_fontdir}/cmunci.pfb
%{_fontdir}/cmunit.pfb
%{_fontdir}/cmunobi.pfb
%{_fontdir}/cmunobx.pfb
%{_fontdir}/cmunorm.pfb
%{_fontdir}/cmunoti.pfb
%{_fontdir}/cmunrb.pfb
%{_fontdir}/cmunrm.pfb
%{_fontdir}/cmunsi.pfb
%{_fontdir}/cmunsl.pfb
%{_fontdir}/cmunso.pfb
%{_fontdir}/cmunss.pfb
%{_fontdir}/cmunssdc.pfb
%{_fontdir}/cmunst.pfb
%{_fontdir}/cmunsx.pfb
%{_fontdir}/cmuntb.pfb
%{_fontdir}/cmunti.pfb
%{_fontdir}/cmuntt.pfb
%{_fontdir}/cmuntx.pfb
%{_fontdir}/cmunui.pfb
%{_fontdir}/cmunvi.pfb
%{_fontdir}/cmunvt.pfb

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
