%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/tools.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/tools.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/tools.source.tar.xz

Name: texlive-tools
License: LPPL
Summary: The LaTeX standard tools bundle
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(afterpage.sty)
Provides: tex(array.sty)
Provides: tex(bm.sty)
Provides: tex(calc.sty)
Provides: tex(dcolumn.sty)
Provides: tex(delarray.sty)
Provides: tex(enumerate.sty)
Provides: tex(fontsmpl.sty)
Provides: tex(ftnright.sty)
Provides: tex(hhline.sty)
Provides: tex(indentfirst.sty)
Provides: tex(layout.sty)
Provides: tex(longtable.sty)
Provides: tex(multicol.sty)
Provides: tex(rawfonts.sty)
Provides: tex(showkeys.sty)
Provides: tex(somedefs.sty)
Provides: tex(tabularx.sty)
Provides: tex(thb.sty)
Provides: tex(thc.sty)
Provides: tex(thcb.sty)
Provides: tex(theorem.sty)
Provides: tex(thm.sty)
Provides: tex(thmb.sty)
Provides: tex(thp.sty)
Provides: tex(trace.sty)
Provides: tex(varioref.sty)
Provides: tex(verbatim.sty)
Provides: tex(xr.sty)
Provides: tex(xspace.sty)
Requires: tex(color.sty)

%description
A collection of (variously) simple tools provided as part of
the LaTeX required tools distribution, comprising: afterpage,
array, calc, dcolumn, delarray, enumerate, fileerr, fontsmpl,
ftnright, hhline, indentfirst, layout, longtable, multicol,
rawfonts, showkeys, somedefs, theorem, tabularx, trace,
varioref, verbatim, xr, and xspace.

date: 2009-10-23 17:37:57 +0200

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
Summary: Documentation for tools
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for tools


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
%{_texdir}/texmf-dist/tex/latex/tools/.tex
%{_texdir}/texmf-dist/tex/latex/tools/afterpage.sty
%{_texdir}/texmf-dist/tex/latex/tools/array.sty
%{_texdir}/texmf-dist/tex/latex/tools/bm.sty
%{_texdir}/texmf-dist/tex/latex/tools/calc.sty
%{_texdir}/texmf-dist/tex/latex/tools/dcolumn.sty
%{_texdir}/texmf-dist/tex/latex/tools/delarray.sty
%{_texdir}/texmf-dist/tex/latex/tools/e.tex
%{_texdir}/texmf-dist/tex/latex/tools/enumerate.sty
%{_texdir}/texmf-dist/tex/latex/tools/fontsmpl.sty
%{_texdir}/texmf-dist/tex/latex/tools/fontsmpl.tex
%{_texdir}/texmf-dist/tex/latex/tools/ftnright.sty
%{_texdir}/texmf-dist/tex/latex/tools/h.tex
%{_texdir}/texmf-dist/tex/latex/tools/hhline.sty
%{_texdir}/texmf-dist/tex/latex/tools/indentfirst.sty
%{_texdir}/texmf-dist/tex/latex/tools/layout.sty
%{_texdir}/texmf-dist/tex/latex/tools/longtable.sty
%{_texdir}/texmf-dist/tex/latex/tools/multicol.sty
%{_texdir}/texmf-dist/tex/latex/tools/q.tex
%{_texdir}/texmf-dist/tex/latex/tools/r.tex
%{_texdir}/texmf-dist/tex/latex/tools/rawfonts.sty
%{_texdir}/texmf-dist/tex/latex/tools/s.tex
%{_texdir}/texmf-dist/tex/latex/tools/showkeys.sty
%{_texdir}/texmf-dist/tex/latex/tools/somedefs.sty
%{_texdir}/texmf-dist/tex/latex/tools/tabularx.sty
%{_texdir}/texmf-dist/tex/latex/tools/thb.sty
%{_texdir}/texmf-dist/tex/latex/tools/thc.sty
%{_texdir}/texmf-dist/tex/latex/tools/thcb.sty
%{_texdir}/texmf-dist/tex/latex/tools/theorem.sty
%{_texdir}/texmf-dist/tex/latex/tools/thm.sty
%{_texdir}/texmf-dist/tex/latex/tools/thmb.sty
%{_texdir}/texmf-dist/tex/latex/tools/thp.sty
%{_texdir}/texmf-dist/tex/latex/tools/trace.sty
%{_texdir}/texmf-dist/tex/latex/tools/varioref.sty
%{_texdir}/texmf-dist/tex/latex/tools/verbatim.sty
%{_texdir}/texmf-dist/tex/latex/tools/verbtest.tex
%{_texdir}/texmf-dist/tex/latex/tools/x.tex
%{_texdir}/texmf-dist/tex/latex/tools/xr.sty
%{_texdir}/texmf-dist/tex/latex/tools/xspace.sty

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/tools/afterpage.pdf
%{_texdir}/texmf-dist/doc/latex/tools/array.pdf
%{_texdir}/texmf-dist/doc/latex/tools/bm.pdf
%{_texdir}/texmf-dist/doc/latex/tools/calc.pdf
%{_texdir}/texmf-dist/doc/latex/tools/changes.txt
%{_texdir}/texmf-dist/doc/latex/tools/dcolumn.pdf
%{_texdir}/texmf-dist/doc/latex/tools/delarray.pdf
%{_texdir}/texmf-dist/doc/latex/tools/enumerate.pdf
%{_texdir}/texmf-dist/doc/latex/tools/fileerr.pdf
%{_texdir}/texmf-dist/doc/latex/tools/fontsmpl.pdf
%{_texdir}/texmf-dist/doc/latex/tools/ftnright.pdf
%{_texdir}/texmf-dist/doc/latex/tools/hhline.pdf
%{_texdir}/texmf-dist/doc/latex/tools/indentfirst.pdf
%{_texdir}/texmf-dist/doc/latex/tools/layout.pdf
%{_texdir}/texmf-dist/doc/latex/tools/longtable.pdf
%{_texdir}/texmf-dist/doc/latex/tools/manifest.txt
%{_texdir}/texmf-dist/doc/latex/tools/multicol.pdf
%{_texdir}/texmf-dist/doc/latex/tools/rawfonts.pdf
%{_texdir}/texmf-dist/doc/latex/tools/readme.txt
%{_texdir}/texmf-dist/doc/latex/tools/showkeys.pdf
%{_texdir}/texmf-dist/doc/latex/tools/somedefs.pdf
%{_texdir}/texmf-dist/doc/latex/tools/tabularx.pdf
%{_texdir}/texmf-dist/doc/latex/tools/theorem.pdf
%{_texdir}/texmf-dist/doc/latex/tools/tools.pdf
%{_texdir}/texmf-dist/doc/latex/tools/trace.pdf
%{_texdir}/texmf-dist/doc/latex/tools/varioref.pdf
%{_texdir}/texmf-dist/doc/latex/tools/verbatim.pdf
%{_texdir}/texmf-dist/doc/latex/tools/xr.pdf
%{_texdir}/texmf-dist/doc/latex/tools/xspace.pdf


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
