%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/powerdot.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/powerdot.doc.tar.xz

Name: texlive-powerdot
License: LPPL
Summary: A presentation class
Version: %{tl_version}
Release: %{tl_noarch_release}.1.3.svn17345%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(powerdot-aggie.sty)
Provides: tex(powerdot-bframe.sty)
Provides: tex(powerdot-ciment.sty)
Provides: tex(powerdot-default.sty)
Provides: tex(powerdot-elcolors.sty)
Provides: tex(powerdot-fyma.sty)
Provides: tex(powerdot-horatio.sty)
Provides: tex(powerdot-husky.sty)
Provides: tex(powerdot-ikeda.sty)
Provides: tex(powerdot-jefka.sty)
Provides: tex(powerdot-klope.sty)
Provides: tex(powerdot-paintings.sty)
Provides: tex(powerdot-pazik.sty)
Provides: tex(powerdot-sailor.sty)
Provides: tex(powerdot-simple.sty)
Provides: tex(powerdot-tycja.sty)
Provides: tex(powerdot-upen.sty)
Provides: tex(powerdot.sty)
Requires: tex(times.sty)
Requires: tex(pifont.sty)
Requires: tex(pst-grad.sty)
Requires: tex(pst-blur.sty)
Requires: tex(calc.sty)
Requires: tex(pst-slpe.sty)
Requires: tex(pst-char.sty)
Requires: tex(type1cm.sty)
Requires: tex(amssymb.sty)
Requires: tex(xkeyval.sty)
Requires: tex(geometry.sty)
Requires: tex(hyperref.sty)
Requires: tex(graphicx.sty)
Requires: tex(pstricks.sty)
Requires: tex(xcolor.sty)
Requires: tex(enumitem.sty)
Requires: tex(verbatim.sty)

%description
Powerdot is a presentation class for LaTeX that allows for the
quick and easy development of professional presentations. It
comes with many tools that enhance presentations and aid the
presenter. Examples are automatic overlays, personal notes and
a handout mode. To view a presentation, DVI, PS or PDF output
can be used. A powerful template system is available to easily
develop new styles. A LyX layout file is provided.

date: 2009-04-26 18:42:19 +0200

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
Summary: Documentation for powerdot
Version: %{tl_version}
Release: %{tl_noarch_release}.1.3.svn17345%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for powerdot


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
%{_texdir}/texmf-dist/tex/latex/powerdot/powerdot-aggie.sty
%{_texdir}/texmf-dist/tex/latex/powerdot/powerdot-bframe.sty
%{_texdir}/texmf-dist/tex/latex/powerdot/powerdot-ciment.sty
%{_texdir}/texmf-dist/tex/latex/powerdot/powerdot-default.ps
%{_texdir}/texmf-dist/tex/latex/powerdot/powerdot-default.sty
%{_texdir}/texmf-dist/tex/latex/powerdot/powerdot-elcolors.sty
%{_texdir}/texmf-dist/tex/latex/powerdot/powerdot-fyma.sty
%{_texdir}/texmf-dist/tex/latex/powerdot/powerdot-horatio.sty
%{_texdir}/texmf-dist/tex/latex/powerdot/powerdot-husky.sty
%{_texdir}/texmf-dist/tex/latex/powerdot/powerdot-ikeda.sty
%{_texdir}/texmf-dist/tex/latex/powerdot/powerdot-jefka.sty
%{_texdir}/texmf-dist/tex/latex/powerdot/powerdot-klope.sty
%{_texdir}/texmf-dist/tex/latex/powerdot/powerdot-paintings.sty
%{_texdir}/texmf-dist/tex/latex/powerdot/powerdot-pazik.sty
%{_texdir}/texmf-dist/tex/latex/powerdot/powerdot-sailor.sty
%{_texdir}/texmf-dist/tex/latex/powerdot/powerdot-simple.sty
%{_texdir}/texmf-dist/tex/latex/powerdot/powerdot-tycja.sty
%{_texdir}/texmf-dist/tex/latex/powerdot/powerdot-upen.sty
%{_texdir}/texmf-dist/tex/latex/powerdot/powerdot.cls

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/powerdot/README
%{_texdir}/texmf-dist/doc/latex/powerdot/manifest.txt
%{_texdir}/texmf-dist/doc/latex/powerdot/powerdot-example.lyx
%{_texdir}/texmf-dist/doc/latex/powerdot/powerdot-example.tex
%{_texdir}/texmf-dist/doc/latex/powerdot/powerdot-example1.tex
%{_texdir}/texmf-dist/doc/latex/powerdot/powerdot-example2.tex
%{_texdir}/texmf-dist/doc/latex/powerdot/powerdot-example3.tex
%{_texdir}/texmf-dist/doc/latex/powerdot/powerdot-styleexample.tex
%{_texdir}/texmf-dist/doc/latex/powerdot/powerdot-styletest.tex
%{_texdir}/texmf-dist/doc/latex/powerdot/powerdot.bib
%{_texdir}/texmf-dist/doc/latex/powerdot/powerdot.layout
%{_texdir}/texmf-dist/doc/latex/powerdot/powerdot.pdf
%{_texdir}/texmf-dist/doc/latex/powerdot/Changes
%{_texdir}/texmf-dist/doc/latex/powerdot/RunDoc
%{_texdir}/texmf-dist/doc/latex/powerdot/RunExamples
%{_texdir}/texmf-dist/doc/latex/powerdot/RunSlideDoc
%{_texdir}/texmf-dist/doc/latex/powerdot/powerdot-de.pdf
%{_texdir}/texmf-dist/doc/latex/powerdot/powerdot-de.tex
%{_texdir}/texmf-dist/doc/latex/powerdot/powerdot-example1.pdf
%{_texdir}/texmf-dist/doc/latex/powerdot/powerdot-example2.pdf
%{_texdir}/texmf-dist/doc/latex/powerdot/powerdot-example3.pdf
%{_texdir}/texmf-dist/doc/latex/powerdot/powerdot.tex
%{_texdir}/texmf-dist/doc/latex/powerdot/powerdotSlide.pdf
%{_texdir}/texmf-dist/doc/latex/powerdot/powerdotSlide.tex

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
