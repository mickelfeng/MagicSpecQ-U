%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/skak.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/skak.doc.tar.xz

Name: texlive-skak
License: LPPL
Summary: Fonts and macros for typesetting chess games
Version: %{tl_version}
Release: %{tl_noarch_release}.1.5.svn16453%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(chess-workshop-symbols.sty)
Provides: tex(lambda.sty)
Provides: tex(skak.sty)
Requires: tex(latexsym.sty)
Requires: tex(chessfss.sty)
Requires: tex(pstricks.sty)
Requires: tex(pst-node.sty)

%description
This package provides macros and fonts in MetaFont format which
can be used to typeset chess games using PGN, and to show
diagrams of the current board in a document. The package builds
on work by Piet Tutelaers -- the main novelty is the use of PGN
for input instead of the more cumbersome coordinate notation
(g1f3 becomes the more readable Nf3 in PGN). An Adobe Type 1
implementation of skak's fonts is available as package skaknew;
an alternative chess notational scheme is available in package
texmate, and a general mechanism for selecting chess fonts is
provided in chessfss.

date: 2008-10-16 14:41:43 +0200

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
Summary: Documentation for skak
Version: %{tl_version}
Release: %{tl_noarch_release}.1.5.svn16453%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for skak


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

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/fonts/source/public/skak/skak10.mf
%{_texdir}/texmf-dist/fonts/source/public/skak/skak15.mf
%{_texdir}/texmf-dist/fonts/source/public/skak/skak20.mf
%{_texdir}/texmf-dist/fonts/source/public/skak/skak30.mf
%{_texdir}/texmf-dist/fonts/source/public/skak/skakbase.mf
%{_texdir}/texmf-dist/fonts/source/public/skak/skakbrikker.mf
%{_texdir}/texmf-dist/fonts/source/public/skak/skakf10.mf
%{_texdir}/texmf-dist/fonts/source/public/skak/skakf10b.mf
%{_texdir}/texmf-dist/fonts/source/public/skak/skakinf.mf
%{_texdir}/texmf-dist/fonts/tfm/public/skak/skak10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/skak/skak15.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/skak/skak20.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/skak/skak30.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/skak/skakf10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/skak/skakf10b.tfm
%{_texdir}/texmf-dist/tex/latex/skak/chess-workshop-symbols.sty
%{_texdir}/texmf-dist/tex/latex/skak/lambda.sty
%{_texdir}/texmf-dist/tex/latex/skak/skak.fd
%{_texdir}/texmf-dist/tex/latex/skak/skak.sty
%{_texdir}/texmf-dist/tex/latex/skak/uskak.fd

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/skak/README
%{_texdir}/texmf-dist/doc/latex/skak/WC-2004-S-00007.tex
%{_texdir}/texmf-dist/doc/latex/skak/_region_.tex
%{_texdir}/texmf-dist/doc/latex/skak/andreas_wilm_1.tex
%{_texdir}/texmf-dist/doc/latex/skak/angletst.tex
%{_texdir}/texmf-dist/doc/latex/skak/debug_storegame.tex
%{_texdir}/texmf-dist/doc/latex/skak/demo-symbols.tex
%{_texdir}/texmf-dist/doc/latex/skak/fen_with_black.tex
%{_texdir}/texmf-dist/doc/latex/skak/font.tex
%{_texdir}/texmf-dist/doc/latex/skak/font2.tex
%{_texdir}/texmf-dist/doc/latex/skak/hightest.tex
%{_texdir}/texmf-dist/doc/latex/skak/informator.pdf
%{_texdir}/texmf-dist/doc/latex/skak/informator.tex
%{_texdir}/texmf-dist/doc/latex/skak/ingo-bug1.tex
%{_texdir}/texmf-dist/doc/latex/skak/lambda.tex
%{_texdir}/texmf-dist/doc/latex/skak/longmoves.tex
%{_texdir}/texmf-dist/doc/latex/skak/makefile
%{_texdir}/texmf-dist/doc/latex/skak/promotion_problem_Ulrike.tex
%{_texdir}/texmf-dist/doc/latex/skak/refman.pdf
%{_texdir}/texmf-dist/doc/latex/skak/refman.tex
%{_texdir}/texmf-dist/doc/latex/skak/show.tex
%{_texdir}/texmf-dist/doc/latex/skak/skakdoc.pdf
%{_texdir}/texmf-dist/doc/latex/skak/skakdoc.tex
%{_texdir}/texmf-dist/doc/latex/skak/special.map
%{_texdir}/texmf-dist/doc/latex/skak/syntax.tex
%{_texdir}/texmf-dist/doc/latex/skak/test1.tex
%{_texdir}/texmf-dist/doc/latex/skak/test2.tex
%{_texdir}/texmf-dist/doc/latex/skak/test_capture.tex
%{_texdir}/texmf-dist/doc/latex/skak/tuggame.pdf
%{_texdir}/texmf-dist/doc/latex/skak/tuggame.tex


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
