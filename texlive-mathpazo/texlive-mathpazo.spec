%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/mathpazo.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/mathpazo.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/mathpazo.source.tar.xz

Name: texlive-mathpazo
License: GPL+
Summary: Fonts to typeset mathematics to match Palatino
Version: %{tl_version}
Release: %{tl_noarch_release}.1.003.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-mathpazo-fedora-fonts = %{tl_version}

%description
The Pazo Math fonts are a family of PostScript fonts suitable
for typesetting mathematics in combination with the Palatino
family of text fonts. The Pazo Math family is made up of five
fonts provided in Adobe Type 1 format (PazoMath, PazoMath-
Italic, PazoMath-Bold, PazoMath-BoldItalic, and
PazoMathBlackboardBold). These contain, in designs that match
Palatino, glyphs that are usually not available in Palatino and
for which Computer Modern looks odd when combined with
Palatino. These glyphs include the uppercase Greek alphabet in
upright and slanted shapes in regular and bold weights, the
lowercase Greek alphabet in slanted shape in regular and bold
weights, several mathematical glyphs (partialdiff, summation,
product, coproduct, emptyset, infinity, and proportional) in
regular and bold weights, other glyphs (Euro and dotlessj) in
upright and slanted shapes in regular and bold weights, and the
uppercase letters commonly used to represent various number
sets (C, I, N, Q, R, and Z) in blackboard bold. The set also
includes a set of 'true' small-caps fonts, also suitable for
use with Palatino (or one of its clones). LaTeX macro support
(using package mathpazo.sty) is provided in psnfss (a required
part of any LaTeX distribution).

date: 2009-10-06 20:42:53 +0200

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
Summary: Documentation for mathpazo
Version: %{tl_version}
Release: %{tl_noarch_release}.1.003.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for mathpazo

%package fedora-fonts
Summary: Fonts for mathpazo
Version: %{tl_version}
Release: %{tl_noarch_release}.1.003.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-mathpazo = %{tl_version}
BuildArch: noarch

%description fedora-fonts
The Pazo Math fonts are a family of PostScript fonts suitable
for typesetting mathematics in combination with the Palatino
family of text fonts. The Pazo Math family is made up of five
fonts provided in Adobe Type 1 format (PazoMath, PazoMath-
Italic, PazoMath-Bold, PazoMath-BoldItalic, and
PazoMathBlackboardBold). These contain, in designs that match
Palatino, glyphs that are usually not available in Palatino and
for which Computer Modern looks odd when combined with
Palatino. These glyphs include the uppercase Greek alphabet in
upright and slanted shapes in regular and bold weights, the
lowercase Greek alphabet in slanted shape in regular and bold
weights, several mathematical glyphs (partialdiff, summation,
product, coproduct, emptyset, infinity, and proportional) in
regular and bold weights, other glyphs (Euro and dotlessj) in
upright and slanted shapes in regular and bold weights, and the
uppercase letters commonly used to represent various number
sets (C, I, N, Q, R, and Z) in blackboard bold. The set also
includes a set of 'true' small-caps fonts, also suitable for
use with Palatino (or one of its clones). LaTeX macro support
(using package mathpazo.sty) is provided in psnfss (a required
part of any LaTeX distribution).

date: 2009-10-06 20:42:53 +0200


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mathpazo/fplmb.pfb .
ln -s %{_fontdir}/fplmb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mathpazo/fplmb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mathpazo/fplmbb.pfb .
ln -s %{_fontdir}/fplmbb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mathpazo/fplmbb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mathpazo/fplmbi.pfb .
ln -s %{_fontdir}/fplmbi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mathpazo/fplmbi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mathpazo/fplmr.pfb .
ln -s %{_fontdir}/fplmr.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mathpazo/fplmr.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mathpazo/fplmri.pfb .
ln -s %{_fontdir}/fplmri.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mathpazo/fplmri.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/fonts/afm/public/mathpazo/fplmb.afm
%{_texdir}/texmf-dist/fonts/afm/public/mathpazo/fplmbb.afm
%{_texdir}/texmf-dist/fonts/afm/public/mathpazo/fplmbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/mathpazo/fplmr.afm
%{_texdir}/texmf-dist/fonts/afm/public/mathpazo/fplmri.afm
%{_texdir}/texmf-dist/fonts/tfm/public/mathpazo/fplmb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathpazo/fplmbb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathpazo/fplmbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathpazo/fplmr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathpazo/fplmri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathpazo/zplmb7m.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathpazo/zplmb7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathpazo/zplmb7y.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathpazo/zplmr7m.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathpazo/zplmr7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathpazo/zplmr7v.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathpazo/zplmr7y.tfm
%{_texdir}/texmf-dist/fonts/type1/public/mathpazo/fplmb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/mathpazo/fplmbb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/mathpazo/fplmbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/mathpazo/fplmr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/mathpazo/fplmri.pfb
%{_texdir}/texmf-dist/fonts/vf/public/mathpazo/zplmb7m.vf
%{_texdir}/texmf-dist/fonts/vf/public/mathpazo/zplmb7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/mathpazo/zplmb7y.vf
%{_texdir}/texmf-dist/fonts/vf/public/mathpazo/zplmr7m.vf
%{_texdir}/texmf-dist/fonts/vf/public/mathpazo/zplmr7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/mathpazo/zplmr7v.vf
%{_texdir}/texmf-dist/fonts/vf/public/mathpazo/zplmr7y.vf

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/latex/mathpazo/README.txt
%{_texdir}/texmf-dist/doc/latex/mathpazo/gpl.txt
%{_texdir}/texmf-dist/doc/latex/mathpazo/mapfplm.tex
%{_texdir}/texmf-dist/doc/latex/mathpazo/mapppl.tex
%{_texdir}/texmf-dist/doc/latex/mathpazo/mapzplm.tex
%{_texdir}/texmf-dist/doc/latex/mathpazo/pazofnst.tex
%{_texdir}/texmf-dist/doc/latex/mathpazo/pazotest.pdf

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/fplmb.pfb
%{_fontdir}/fplmbb.pfb
%{_fontdir}/fplmbi.pfb
%{_fontdir}/fplmr.pfb
%{_fontdir}/fplmri.pfb

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
