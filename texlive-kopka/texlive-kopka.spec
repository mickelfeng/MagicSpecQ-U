%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/kopka.doc.tar.xz

Name: texlive-kopka-doc
License: LPPL
Summary: Documentation for kopka
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description
Documentation for kopka


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
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel2/a4.sty
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel2/readme_2
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel2/ueb2-1.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel2/ueb2-1a.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel2/ueb2-1b.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel2/ueb2-1c.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel2/ueb2-1d.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel2/ueb2-2.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel2/ueb2-2a.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel2/ueb2-2b.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel2/ueb2-2c.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel2/ueb2-2d.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel2/ueb2-3.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel2/ueb2-3a.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel2/ueb2-3b.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/a4.sty
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/readme_3
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/ueb3-10.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/ueb3-11.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/ueb3-12.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/ueb3-14.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/ueb3-14a.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/ueb3-14b.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/ueb3-1a.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/ueb3-1b.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/ueb3-2.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/ueb3-3a.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/ueb3-3b.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/ueb3-4.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/ueb3-5a.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/ueb3-5b.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/ueb3-6a.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/ueb3-6b.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/ueb3-6c.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/ueb3-7a.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/ueb3-7b.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/ueb3-7c.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/ueb3-8.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/ueb3-9.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3/ueb3.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/a4.sty
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/readme_4
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/ueb4-1.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/ueb4-10.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/ueb4-11.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/ueb4-12.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/ueb4-13.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/ueb4-14.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/ueb4-15.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/ueb4-16.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/ueb4-17.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/ueb4-18.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/ueb4-19.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/ueb4-2.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/ueb4-20.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/ueb4-21.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/ueb4-22.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/ueb4-3.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/ueb4-4.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/ueb4-5.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/ueb4-6.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/ueb4-7.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/ueb4-8.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/ueb4-9a.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4/ueb4-9b.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5/a4.sty
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5/math.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5/readme_5
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5/ueb5-1.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5/ueb5-10.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5/ueb5-11.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5/ueb5-12.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5/ueb5-13.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5/ueb5-14.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5/ueb5-15.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5/ueb5-16.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5/ueb5-17.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5/ueb5-18.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5/ueb5-19.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5/ueb5-2.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5/ueb5-20.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5/ueb5-21.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5/ueb5-3.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5/ueb5-4.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5/ueb5-5.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5/ueb5-6.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5/ueb5-7.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5/ueb5-8.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5/ueb5-9.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel6/a4.sty
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel6/bild.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel6/readme_6
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel6/ueb6-1.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel6/ueb6-10.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel6/ueb6-2.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel6/ueb6-3.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel6/ueb6-4.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel6/ueb6-5.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel6/ueb6-6.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel6/ueb6-7.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel6/ueb6-8.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel6/ueb6-9.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel7/ueb7-1.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel7/ueb7-10.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel7/ueb7-11.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel7/ueb7-12.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel7/ueb7-2.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel7/ueb7-3.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel7/ueb7-4.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel7/ueb7-5.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel7/ueb7-6.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel7/ueb7-7.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel7/ueb7-8a.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel7/ueb7-8b.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel7/ueb7-9.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel8/ueb8-1.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel8/ueb8-2.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel8/ueb8-3.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel8/ueba.aux
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel8/ueba.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel8/uebb.aux
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel8/uebb.tex
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel8/uebc.aux
%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel8/uebc.tex


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
