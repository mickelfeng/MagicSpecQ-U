%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/economic.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/economic.doc.tar.xz

Name: texlive-economic
License: LPPL
Summary: BibTeX support for submitting to Economics journals
Version: %{tl_version}
Release: %{tl_noarch_release}.svn16184%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(aer.sty)
Provides: tex(aertt.sty)
Provides: tex(agecon.sty)
Provides: tex(ajae.sty)
Provides: tex(apecon.sty)
Provides: tex(cje.sty)
Provides: tex(ecca.sty)
Provides: tex(erae.sty)
Provides: tex(itaxpf.sty)
Provides: tex(jrurstud.sty)
Provides: tex(njf.sty)
Provides: tex(oegatb.sty)
Provides: tex(pocoec.sty)
Provides: tex(regstud.sty)
Provides: tex(worlddev.sty)
Requires: tex(ulem.sty)
Requires: tex(ifthen.sty)
Requires: tex(babel.sty)
Requires: tex(geometry.sty)
Requires: tex(setspace.sty)
Requires: tex(titlesec.sty)
Requires: tex(lmodern.sty)
Requires: tex(amsmath.sty)
Requires: tex(url.sty)
Requires: tex(natbib.sty)
Requires: tex(endfloat.sty)
Requires: tex(mathptmx.sty)
Requires: tex(helvet.sty)
Requires: tex(courier.sty)
Requires: tex(bm.sty)
Requires: tex(endnotes.sty)
Requires: tex(textcomp.sty)
Requires: tex(stringstrings.sty)
Requires: tex(fancyhdr.sty)
Requires: tex(soul.sty)
Requires: tex(verbatim.sty)

%description
The bundle offers macros and BibTeX styles for the American
Economic Review (AER), the American Journal of Agricultural
Economics (AJAE), the Canadian Journal of Economics (CJE), the
European Review of Agricultural Economics (ERAE), the
International Economic Review (IER) and Economica. The macro
sets are based on (and require) the harvard package, and all
provide variations of author-date styles of presentation.

date: 2009-11-25 18:21:28 +0100

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
Summary: Documentation for economic
Version: %{tl_version}
Release: %{tl_noarch_release}.svn16184%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for economic


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
%{_texdir}/texmf-dist/bibtex/bst/economic/aer.bst
%{_texdir}/texmf-dist/bibtex/bst/economic/aertt.bst
%{_texdir}/texmf-dist/bibtex/bst/economic/agecon.bst
%{_texdir}/texmf-dist/bibtex/bst/economic/ajae.bst
%{_texdir}/texmf-dist/bibtex/bst/economic/apecon.bst
%{_texdir}/texmf-dist/bibtex/bst/economic/cje.bst
%{_texdir}/texmf-dist/bibtex/bst/economic/ecca.bst
%{_texdir}/texmf-dist/bibtex/bst/economic/econometrica-fr.bst
%{_texdir}/texmf-dist/bibtex/bst/economic/econometrica.bst
%{_texdir}/texmf-dist/bibtex/bst/economic/ecta.bst
%{_texdir}/texmf-dist/bibtex/bst/economic/erae.bst
%{_texdir}/texmf-dist/bibtex/bst/economic/ier.bst
%{_texdir}/texmf-dist/bibtex/bst/economic/itaxpf.bst
%{_texdir}/texmf-dist/bibtex/bst/economic/jae.bst
%{_texdir}/texmf-dist/bibtex/bst/economic/jpe.bst
%{_texdir}/texmf-dist/bibtex/bst/economic/jss2.bst
%{_texdir}/texmf-dist/bibtex/bst/economic/oega.bst
%{_texdir}/texmf-dist/bibtex/bst/economic/regstud.bst
%{_texdir}/texmf-dist/bibtex/bst/economic/tandfx.bst
%{_texdir}/texmf-dist/bibtex/bst/economic/worlddev.bst
%{_texdir}/texmf-dist/tex/latex/economic/aer.sty
%{_texdir}/texmf-dist/tex/latex/economic/aertt.sty
%{_texdir}/texmf-dist/tex/latex/economic/agecon.cls
%{_texdir}/texmf-dist/tex/latex/economic/ajae.cls
%{_texdir}/texmf-dist/tex/latex/economic/apecon.cls
%{_texdir}/texmf-dist/tex/latex/economic/cje.sty
%{_texdir}/texmf-dist/tex/latex/economic/ecca.cls
%{_texdir}/texmf-dist/tex/latex/economic/erae.cls
%{_texdir}/texmf-dist/tex/latex/economic/itaxpf.cls
%{_texdir}/texmf-dist/tex/latex/economic/jrurstud.cls
%{_texdir}/texmf-dist/tex/latex/economic/njf.cls
%{_texdir}/texmf-dist/tex/latex/economic/oegatb.cls
%{_texdir}/texmf-dist/tex/latex/economic/pocoec.cls
%{_texdir}/texmf-dist/tex/latex/economic/regstud.cls
%{_texdir}/texmf-dist/tex/latex/economic/worlddev.cls

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/bibtex/economic/CHANGELOG
%{_texdir}/texmf-dist/doc/bibtex/economic/NEWS
%{_texdir}/texmf-dist/doc/bibtex/economic/README
%{_texdir}/texmf-dist/doc/bibtex/economic/aer-cje-ex.bib
%{_texdir}/texmf-dist/doc/bibtex/economic/aer-cje-ex.tex
%{_texdir}/texmf-dist/doc/bibtex/economic/aer-natbib-ex.tex
%{_texdir}/texmf-dist/doc/bibtex/economic/ajae-ex.bib
%{_texdir}/texmf-dist/doc/bibtex/economic/ajae-ex.pdf
%{_texdir}/texmf-dist/doc/bibtex/economic/ajae-ex.tex
%{_texdir}/texmf-dist/doc/bibtex/economic/apecon-ex.bib
%{_texdir}/texmf-dist/doc/bibtex/economic/apecon-ex.pdf
%{_texdir}/texmf-dist/doc/bibtex/economic/apecon-ex.tex
%{_texdir}/texmf-dist/doc/bibtex/economic/ecca-ex.bib
%{_texdir}/texmf-dist/doc/bibtex/economic/ecca-ex.pdf
%{_texdir}/texmf-dist/doc/bibtex/economic/ecca-ex.tex
%{_texdir}/texmf-dist/doc/bibtex/economic/erae-ex.bib
%{_texdir}/texmf-dist/doc/bibtex/economic/erae-ex.pdf
%{_texdir}/texmf-dist/doc/bibtex/economic/erae-ex.tex
%{_texdir}/texmf-dist/doc/bibtex/economic/ier-bib-test.pdf
%{_texdir}/texmf-dist/doc/bibtex/economic/ier-bib-test.tex
%{_texdir}/texmf-dist/doc/bibtex/economic/ier-ex.bib
%{_texdir}/texmf-dist/doc/bibtex/economic/itaxpf-ex-title.pdf
%{_texdir}/texmf-dist/doc/bibtex/economic/itaxpf-ex-title.tex
%{_texdir}/texmf-dist/doc/bibtex/economic/itaxpf-ex.bib
%{_texdir}/texmf-dist/doc/bibtex/economic/itaxpf-ex.pdf
%{_texdir}/texmf-dist/doc/bibtex/economic/itaxpf-ex.tex
%{_texdir}/texmf-dist/doc/bibtex/economic/oegatb-ex.bib
%{_texdir}/texmf-dist/doc/bibtex/economic/oegatb-ex.pdf
%{_texdir}/texmf-dist/doc/bibtex/economic/oegatb-ex.png
%{_texdir}/texmf-dist/doc/bibtex/economic/oegatb-ex.tex


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
