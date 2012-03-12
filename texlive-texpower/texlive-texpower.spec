%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/texpower.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/texpower.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/texpower.source.tar.xz

Name: texlive-texpower
License: GPL+
Summary: Create dynamic online presentations with LaTeX
Version: %{tl_version}
Release: %{tl_noarch_release}.0.2.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tpslifonts = %{tl_version}
Provides: tex(automata.sty)
Provides: tex(fixseminar.sty)
Provides: tex(powersem.sty)
Provides: tex(texpower.sty)
Provides: tex(tplists.sty)
Provides: tex(tppstcol.sty)
Provides: tex(tpsem-a4.sty)
Requires: tex(ifthen.sty)
Requires: tex(relsize.sty)
Requires: tex(ifpdf.sty)
Requires: tex(graphics.sty)
Requires: tex(calc.sty)
Requires: tex(keyval.sty)
Requires: tex(color.sty)
Requires: tex(pstricks.sty)

%description
TeXPower is a bundle of packages intended to provide an all-
inclusive environment for designing pdf screen presentations to
be viewed in full-screen mode, especially for projecting
`online' with a video beamer. For some of its core functions,
it uses code derived from ppower4 packages. It is, however, not
a complete environment in itself: it relies on an existing
class for preparing slides (such as foiltex or seminar) or
another package such as pdfslide.

date: 2007-01-16 09:34:54 +0100

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
Summary: Documentation for texpower
Version: %{tl_version}
Release: %{tl_noarch_release}.0.2.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch
Requires: texlive-tpslifonts-doc

%description doc
Documentation for texpower


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

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/tex/latex/texpower/automata.sty
%{_texdir}/texmf-dist/tex/latex/texpower/fixseminar.sty
%{_texdir}/texmf-dist/tex/latex/texpower/powersem.cls
%{_texdir}/texmf-dist/tex/latex/texpower/texpower.sty
%{_texdir}/texmf-dist/tex/latex/texpower/tpcolors.cfg
%{_texdir}/texmf-dist/tex/latex/texpower/tplists.sty
%{_texdir}/texmf-dist/tex/latex/texpower/tpoptions.cfg
%{_texdir}/texmf-dist/tex/latex/texpower/tppstcol.sty
%{_texdir}/texmf-dist/tex/latex/texpower/tpsem-a4.sty
%{_texdir}/texmf-dist/tex/latex/texpower/tpsettings.cfg

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/latex/texpower/00readme.txt
%{_texdir}/texmf-dist/doc/latex/texpower/01install.txt
%{_texdir}/texmf-dist/doc/latex/texpower/02changes.txt
%{_texdir}/texmf-dist/doc/latex/texpower/FAQ-display.tex
%{_texdir}/texmf-dist/doc/latex/texpower/FAQ-printout.tex
%{_texdir}/texmf-dist/doc/latex/texpower/MakeExamples.sh
%{_texdir}/texmf-dist/doc/latex/texpower/__TPcfg.tex
%{_texdir}/texmf-dist/doc/latex/texpower/__TPindexing.tex
%{_texdir}/texmf-dist/doc/latex/texpower/__TPpreamble.tex
%{_texdir}/texmf-dist/doc/latex/texpower/bckwrdexample.tex
%{_texdir}/texmf-dist/doc/latex/texpower/bgndexample.tex
%{_texdir}/texmf-dist/doc/latex/texpower/divexample.tex
%{_texdir}/texmf-dist/doc/latex/texpower/dummy.java
%{_texdir}/texmf-dist/doc/latex/texpower/fancyexample.tex
%{_texdir}/texmf-dist/doc/latex/texpower/fig-1.mps
%{_texdir}/texmf-dist/doc/latex/texpower/fig-2.mps
%{_texdir}/texmf-dist/doc/latex/texpower/fig-3.mps
%{_texdir}/texmf-dist/doc/latex/texpower/foilsdemo.tex
%{_texdir}/texmf-dist/doc/latex/texpower/fulldemo.tex
%{_texdir}/texmf-dist/doc/latex/texpower/hilitexample.tex
%{_texdir}/texmf-dist/doc/latex/texpower/ifmslidemo.tex
%{_texdir}/texmf-dist/doc/latex/texpower/manual.pdf
%{_texdir}/texmf-dist/doc/latex/texpower/manual.tex
%{_texdir}/texmf-dist/doc/latex/texpower/mathexample.tex
%{_texdir}/texmf-dist/doc/latex/texpower/panelexample.tex
%{_texdir}/texmf-dist/doc/latex/texpower/parexample.tex
%{_texdir}/texmf-dist/doc/latex/texpower/pdfscrdemo.tex
%{_texdir}/texmf-dist/doc/latex/texpower/pdfslidemo.tex
%{_texdir}/texmf-dist/doc/latex/texpower/picexample.tex
%{_texdir}/texmf-dist/doc/latex/texpower/picltxexample.tex
%{_texdir}/texmf-dist/doc/latex/texpower/picpsexample.tex
%{_texdir}/texmf-dist/doc/latex/texpower/pp4sldemo.tex
%{_texdir}/texmf-dist/doc/latex/texpower/prosperdemo.tex
%{_texdir}/texmf-dist/doc/latex/texpower/seminardemo.tex
%{_texdir}/texmf-dist/doc/latex/texpower/simpledemo.tex
%{_texdir}/texmf-dist/doc/latex/texpower/slidesdemo.tex
%{_texdir}/texmf-dist/doc/latex/texpower/spanelexample.tex
%{_texdir}/texmf-dist/doc/latex/texpower/tabexample.tex
%{_texdir}/texmf-dist/doc/latex/texpower/tpslifonts.zip
%{_texdir}/texmf-dist/doc/latex/texpower/verbexample.tex
%{_texdir}/texmf-dist/doc/latex/texpower/contrib/00readme.txt
%{_texdir}/texmf-dist/doc/latex/texpower/contrib/config.landscapeplus
%{_texdir}/texmf-dist/doc/latex/texpower/contrib/tpmultiinc.tar
%{_texdir}/texmf-dist/doc/latex/texpower/tpslifonts/00readme.txt
%{_texdir}/texmf-dist/doc/latex/texpower/tpslifonts/01install.txt
%{_texdir}/texmf-dist/doc/latex/texpower/tpslifonts/Makefile
%{_texdir}/texmf-dist/doc/latex/texpower/tpslifonts/slifontsexample.tex
%{_texdir}/texmf-dist/doc/latex/texpower/tpslifonts/tpslifonts.dtx
%{_texdir}/texmf-dist/doc/latex/texpower/tpslifonts/tpslifonts.ins


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
