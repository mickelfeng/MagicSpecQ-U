%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/epslatex-fr.doc.tar.xz

Name: texlive-epslatex-fr-doc
License: GPL+
Summary: Documentation for epslatex-fr
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19440%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description
Documentation for epslatex-fr


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
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/Ball.eps
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/CHAP2.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/Construction.eps
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/Franc-chap.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/README
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/README.TEXLIVE
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/Warning.eps
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/alltex.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/auteurs.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/bases.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/block.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/box1.eps
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/box2.eps
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/boxes.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/btxdoc.bib
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/cm.eps
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/cm.ps
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/danger.eps
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/divers.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/ebnf.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/export.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/fepslatex.pdf
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/fepslatex.tex
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/fill.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/fmparhack.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/foot.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/fr.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/franc.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/frnew.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/g_toc_entry.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/graphic.eps
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/hands.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/header.tex
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/indentondemand.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/makecmds.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/makerobust.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/mass.eps
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/mypatches.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/myvarioref.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/nrfoot.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/origin.eps
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/overlay.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/pale.eps
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/pend.eps
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/pretzel.eps
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/pretzel.ps
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/rdanger.eps
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/rosette.eps
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/rosette.ps
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/sgte.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/smaller.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/square.eps
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/topcapt.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/topfig.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/warn.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/wdesc.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/whitecdp.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/wide.eps
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/widecenter.sty
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/xb.sty


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
