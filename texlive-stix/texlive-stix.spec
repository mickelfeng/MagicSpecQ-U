%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/stix.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/stix.doc.tar.xz

Name: texlive-stix
License: OFSFLD
Summary: OpenType Unicode maths fonts
Version: %{tl_version}
Release: %{tl_noarch_release}.1.0.svn19440%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-stix-fedora-fonts = %{tl_version}

%description
The STIX fonts are a suite of unicode OpenType fonts containing
a complete set of mathematical glyphs. The CTAN copy is a
mirror of their official release, organised as specified by the
TeX Directory Structure, for inclusion in standard TeX
distributions.

date: 2010-06-06 13:50:32 +0200

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
Summary: Documentation for stix
Version: %{tl_version}
Release: %{tl_noarch_release}.1.0.svn19440%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for stix

%package fedora-fonts
Summary: Fonts for stix
Version: %{tl_version}
Release: %{tl_noarch_release}.1.0.svn19440%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-stix = %{tl_version}
BuildArch: noarch

%description fedora-fonts
The STIX fonts are a suite of unicode OpenType fonts containing
a complete set of mathematical glyphs. The CTAN copy is a
mirror of their official release, organised as specified by the
TeX Directory Structure, for inclusion in standard TeX
distributions.

date: 2010-06-06 13:50:32 +0200


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXGeneral.otf .
ln -s %{_fontdir}/STIXGeneral.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXGeneral.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXGeneralBol.otf .
ln -s %{_fontdir}/STIXGeneralBol.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXGeneralBol.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXGeneralBolIta.otf .
ln -s %{_fontdir}/STIXGeneralBolIta.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXGeneralBolIta.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXGeneralItalic.otf .
ln -s %{_fontdir}/STIXGeneralItalic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXGeneralItalic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntDBol.otf .
ln -s %{_fontdir}/STIXIntDBol.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntDBol.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntDReg.otf .
ln -s %{_fontdir}/STIXIntDReg.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntDReg.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntSmBol.otf .
ln -s %{_fontdir}/STIXIntSmBol.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntSmBol.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntSmReg.otf .
ln -s %{_fontdir}/STIXIntSmReg.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntSmReg.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntUpBol.otf .
ln -s %{_fontdir}/STIXIntUpBol.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntUpBol.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntUpDBol.otf .
ln -s %{_fontdir}/STIXIntUpDBol.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntUpDBol.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntUpDReg.otf .
ln -s %{_fontdir}/STIXIntUpDReg.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntUpDReg.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntUpReg.otf .
ln -s %{_fontdir}/STIXIntUpReg.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntUpReg.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntUpSmBol.otf .
ln -s %{_fontdir}/STIXIntUpSmBol.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntUpSmBol.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntUpSmReg.otf .
ln -s %{_fontdir}/STIXIntUpSmReg.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntUpSmReg.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXNonUni.otf .
ln -s %{_fontdir}/STIXNonUni.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXNonUni.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXNonUniBol.otf .
ln -s %{_fontdir}/STIXNonUniBol.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXNonUniBol.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXNonUniBolIta.otf .
ln -s %{_fontdir}/STIXNonUniBolIta.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXNonUniBolIta.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXNonUniIta.otf .
ln -s %{_fontdir}/STIXNonUniIta.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXNonUniIta.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizFiveSymReg.otf .
ln -s %{_fontdir}/STIXSizFiveSymReg.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizFiveSymReg.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizFourSymBol.otf .
ln -s %{_fontdir}/STIXSizFourSymBol.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizFourSymBol.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizFourSymReg.otf .
ln -s %{_fontdir}/STIXSizFourSymReg.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizFourSymReg.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizOneSymBol.otf .
ln -s %{_fontdir}/STIXSizOneSymBol.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizOneSymBol.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizOneSymReg.otf .
ln -s %{_fontdir}/STIXSizOneSymReg.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizOneSymReg.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizThreeSymBol.otf .
ln -s %{_fontdir}/STIXSizThreeSymBol.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizThreeSymBol.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizThreeSymReg.otf .
ln -s %{_fontdir}/STIXSizThreeSymReg.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizThreeSymReg.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizTwoSymBol.otf .
ln -s %{_fontdir}/STIXSizTwoSymBol.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizTwoSymBol.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizTwoSymReg.otf .
ln -s %{_fontdir}/STIXSizTwoSymReg.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizTwoSymReg.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXVar.otf .
ln -s %{_fontdir}/STIXVar.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXVar.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXVarBol.otf .
ln -s %{_fontdir}/STIXVarBol.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXVarBol.otf
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc ofl.txt
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXGeneral.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXGeneralBol.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXGeneralBolIta.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXGeneralItalic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntDBol.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntDReg.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntSmBol.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntSmReg.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntUpBol.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntUpDBol.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntUpDReg.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntUpReg.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntUpSmBol.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXIntUpSmReg.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXNonUni.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXNonUniBol.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXNonUniBolIta.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXNonUniIta.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizFiveSymReg.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizFourSymBol.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizFourSymReg.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizOneSymBol.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizOneSymReg.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizThreeSymBol.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizThreeSymReg.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizTwoSymBol.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXSizTwoSymReg.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXVar.otf
%{_texdir}/texmf-dist/fonts/opentype/public/stix/STIXVarBol.otf

%files doc
%defattr(-,root,root)
%doc ofl.txt
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXGeneral.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXGeneralBol.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXGeneralBolIta.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXGeneralItalic.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXIntDBol.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXIntDReg.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXIntSmBol.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXIntSmReg.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXIntUpBol.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXIntUpDBol.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXIntUpDReg.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXIntUpReg.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXIntUpSmBol.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXIntUpSmReg.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXNonUni.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXNonUniBol.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXNonUniBolIta.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXNonUniIta.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXSizFiveSymReg.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXSizFourSymBol.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXSizFourSymReg.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXSizOneSymBol.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXSizOneSymReg.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXSizThreeSymBol.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXSizThreeSymReg.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXSizTwoSymBol.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXSizTwoSymReg.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXVar.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs/STIXVarBol.otf.pdf
%{_texdir}/texmf-dist/doc/fonts/stix/README
%{_texdir}/texmf-dist/doc/fonts/stix/README.TEXLIVE
%{_texdir}/texmf-dist/doc/fonts/stix/STIX_Font_License_2010.pdf

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/STIXGeneral.otf
%{_fontdir}/STIXGeneralBol.otf
%{_fontdir}/STIXGeneralBolIta.otf
%{_fontdir}/STIXGeneralItalic.otf
%{_fontdir}/STIXIntDBol.otf
%{_fontdir}/STIXIntDReg.otf
%{_fontdir}/STIXIntSmBol.otf
%{_fontdir}/STIXIntSmReg.otf
%{_fontdir}/STIXIntUpBol.otf
%{_fontdir}/STIXIntUpDBol.otf
%{_fontdir}/STIXIntUpDReg.otf
%{_fontdir}/STIXIntUpReg.otf
%{_fontdir}/STIXIntUpSmBol.otf
%{_fontdir}/STIXIntUpSmReg.otf
%{_fontdir}/STIXNonUni.otf
%{_fontdir}/STIXNonUniBol.otf
%{_fontdir}/STIXNonUniBolIta.otf
%{_fontdir}/STIXNonUniIta.otf
%{_fontdir}/STIXSizFiveSymReg.otf
%{_fontdir}/STIXSizFourSymBol.otf
%{_fontdir}/STIXSizFourSymReg.otf
%{_fontdir}/STIXSizOneSymBol.otf
%{_fontdir}/STIXSizOneSymReg.otf
%{_fontdir}/STIXSizThreeSymBol.otf
%{_fontdir}/STIXSizThreeSymReg.otf
%{_fontdir}/STIXSizTwoSymBol.otf
%{_fontdir}/STIXSizTwoSymReg.otf
%{_fontdir}/STIXVar.otf
%{_fontdir}/STIXVarBol.otf

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
