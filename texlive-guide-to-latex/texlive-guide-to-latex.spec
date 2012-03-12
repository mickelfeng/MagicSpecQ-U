%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/guide-to-latex.doc.tar.xz

Name: texlive-guide-to-latex-doc
License: LPPL
Summary: Documentation for guide-to-latex
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description
Documentation for guide-to-latex


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
xz -dc %{SOURCE0} | tar x -C %{buildroot}%{_texdir}/texmf-dist
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
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/README.txt
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/demo.eps
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/demo.pdf
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/demodoc.pdf
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/demodoc.ps
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/demodoc.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/mpletter.cls
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/palette.pdf
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/palette.ps
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/palette.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/seminar.con
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/sempdftx.sty
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap10/exer10-1.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap10/exer10-10.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap10/exer10-2.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap10/exer10-3.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap10/exer10-4.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap10/exer10-5.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap10/exer10-6.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap10/exer10-7.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap10/exer10-8.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap10/exer10-9.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap11/exer1.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap11/exer11-1.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap11/exer11-2.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap11/exer11-3.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap11/exer11-4.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap11/exer11-5.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap11/exer2.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap11/exer3.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap15/exer15-1.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap15/exer15-2.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap15/exer15-3.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap15/exer15-4.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap15/exer15-5.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap15/exer15-6.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap15/exer15-7.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap2/exer2-1.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap2/exer2-2.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap2/exer2-3a.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap2/exer2-3b.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap2/exer2-3c.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap3/exer3-10.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap3/exer3-11.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap3/exer3-12.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap3/exer3-12.toc
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap3/exer3-1a.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap3/exer3-1b.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap3/exer3-2.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap3/exer3-3.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap3/exer3-4a.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap3/exer3-4b.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap3/exer3-5a.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap3/exer3-5b.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap3/exer3-6.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap3/exer3-7a.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap3/exer3-7b.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap3/exer3-8a.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap3/exer3-8b.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap3/exer3-9.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap4/exer4-1.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap4/exer4-10.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap4/exer4-2.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap4/exer4-3.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap4/exer4-4.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap4/exer4-5.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap4/exer4-6.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap4/exer4-7.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap4/exer4-8.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap4/exer4-9.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap5/exer5-1.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap5/exer5-2.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap5/exer5-3.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap5/exer5-4.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap6/exer6-1.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap6/exer6-2.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap6/exer6-3.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap6/exer6-4.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap6/exer6-5.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap7/exer7-1.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap7/exer7-10.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap7/exer7-11.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap7/exer7-12.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap7/exer7-13.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap7/exer7-14.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap7/exer7-15.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap7/exer7-16.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap7/exer7-17.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap7/exer7-18.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap7/exer7-19.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap7/exer7-2.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap7/exer7-20.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap7/exer7-21a.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap7/exer7-21b.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap7/exer7-3.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap7/exer7-4.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap7/exer7-5.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap7/exer7-6.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap7/exer7-7.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap7/exer7-8.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap7/exer7-9.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap8/exer8-1.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap8/exer8-2.tex
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap8/exer8-3.tex


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
