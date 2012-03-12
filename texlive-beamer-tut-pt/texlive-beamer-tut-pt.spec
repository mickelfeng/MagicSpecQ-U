%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/beamer-tut-pt.doc.tar.xz

Name: texlive-beamer-tut-pt-doc
License: GPL+
Summary: Documentation for beamer-tut-pt
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description
Documentation for beamer-tut-pt


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/gpl.txt gpl.txt
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
%doc gpl.txt
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/AnnArbor1.ps
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/AnnArbor2.ps
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/CambridgeUS1.ps
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/CambridgeUS2.ps
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/LEIAME
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/README
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/anim1.ps
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/anim2.ps
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/anim3.ps
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/anim4.ps
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/automato1.jpg
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/automato2.jpg
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/automato3.jpg
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/automato4.jpg
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/automato5.jpg
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/berkeley1.ps
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/berkeley2.ps
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/blocos.ps
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/boadilla1.ps
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/boadilla2.ps
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/exemplo.tex
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/madrid1.ps
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/madrid2.ps
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/montpellier1.ps
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/montpellier2.ps
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/tutorialbeamer.pdf
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/tutorialbeamer.tex
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/ufpellogo.jpg


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
