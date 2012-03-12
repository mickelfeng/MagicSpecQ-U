%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/revtex.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/revtex.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/revtex.source.tar.xz

Name: texlive-revtex
License: LPPL
Summary: Styles for various Physics Journals
Version: %{tl_version}
Release: %{tl_noarch_release}.4.1p.svn17498%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(ltxdocext.sty)
Provides: tex(ltxfront.sty)
Provides: tex(ltxgrid.sty)
Provides: tex(ltxutil.sty)
Provides: tex(revsymb4-1.sty)
Provides: tex(revtex4-1.sty)
Requires: tex(verbatim.sty)
Requires: tex(shortvrb.sty)
Requires: tex(textcase.sty)
Requires: tex(amsfonts.sty)
Requires: tex(amssymb.sty)
Requires: tex(amsmath.sty)
Requires: tex(lineno.sty)
Requires: tex(url.sty)
Requires: tex(natbib.sty)

%description
Includes styles for American Physical Society, American
Institute of Physics, and Optical Society of America. The
distribution consists of the RevTeX class itself, and several
support packages.

date: 2010-03-18 08:29:11 +0100

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
Summary: Documentation for revtex
Version: %{tl_version}
Release: %{tl_noarch_release}.4.1p.svn17498%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for revtex


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/lppl1.3.txt lppl1.3.txt
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
%doc lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bst/revtex/aipauth4-1.bst
%{_texdir}/texmf-dist/bibtex/bst/revtex/aipnum4-1.bst
%{_texdir}/texmf-dist/bibtex/bst/revtex/apsrev4-1.bst
%{_texdir}/texmf-dist/bibtex/bst/revtex/apsrmp4-1.bst
%{_texdir}/texmf-dist/tex/latex/revtex/aip4-1.rtx
%{_texdir}/texmf-dist/tex/latex/revtex/aps10pt4-1.rtx
%{_texdir}/texmf-dist/tex/latex/revtex/aps11pt4-1.rtx
%{_texdir}/texmf-dist/tex/latex/revtex/aps12pt4-1.rtx
%{_texdir}/texmf-dist/tex/latex/revtex/aps4-1.rtx
%{_texdir}/texmf-dist/tex/latex/revtex/apsrmp4-1.rtx
%{_texdir}/texmf-dist/tex/latex/revtex/ltxdocext.sty
%{_texdir}/texmf-dist/tex/latex/revtex/ltxfront.sty
%{_texdir}/texmf-dist/tex/latex/revtex/ltxgrid.sty
%{_texdir}/texmf-dist/tex/latex/revtex/ltxutil.sty
%{_texdir}/texmf-dist/tex/latex/revtex/reftest4-1.tex
%{_texdir}/texmf-dist/tex/latex/revtex/revsymb4-1.sty
%{_texdir}/texmf-dist/tex/latex/revtex/revtex4-1.cls

%files doc
%defattr(-,root,root)
%doc lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/revtex/00readme.tex
%{_texdir}/texmf-dist/doc/latex/revtex/DOWNLOAD
%{_texdir}/texmf-dist/doc/latex/revtex/README
%{_texdir}/texmf-dist/doc/latex/revtex/aip/aipguide4-1.pdf
%{_texdir}/texmf-dist/doc/latex/revtex/aip/aipguide4-1.tex
%{_texdir}/texmf-dist/doc/latex/revtex/aip/docs.sty
%{_texdir}/texmf-dist/doc/latex/revtex/aps/apsguide4-1.pdf
%{_texdir}/texmf-dist/doc/latex/revtex/aps/apsguide4-1.tex
%{_texdir}/texmf-dist/doc/latex/revtex/auguide/auguide4-1.pdf
%{_texdir}/texmf-dist/doc/latex/revtex/auguide/auguide4-1.tex
%{_texdir}/texmf-dist/doc/latex/revtex/auguide/docs.sty
%{_texdir}/texmf-dist/doc/latex/revtex/auguide/summary4-1.pdf
%{_texdir}/texmf-dist/doc/latex/revtex/auguide/summary4-1.tex
%{_texdir}/texmf-dist/doc/latex/revtex/auguide/whatsnew4-1.pdf
%{_texdir}/texmf-dist/doc/latex/revtex/auguide/whatsnew4-1.tex
%{_texdir}/texmf-dist/doc/latex/revtex/sample/aip/aipsamp.bib
%{_texdir}/texmf-dist/doc/latex/revtex/sample/aip/aipsamp.pdf
%{_texdir}/texmf-dist/doc/latex/revtex/sample/aip/aipsamp.tex
%{_texdir}/texmf-dist/doc/latex/revtex/sample/aip/aiptemplate.tex
%{_texdir}/texmf-dist/doc/latex/revtex/sample/aip/fig_1.eps
%{_texdir}/texmf-dist/doc/latex/revtex/sample/aip/fig_2.eps
%{_texdir}/texmf-dist/doc/latex/revtex/sample/aps/apssamp.bib
%{_texdir}/texmf-dist/doc/latex/revtex/sample/aps/apssamp.pdf
%{_texdir}/texmf-dist/doc/latex/revtex/sample/aps/apssamp.tex
%{_texdir}/texmf-dist/doc/latex/revtex/sample/aps/apstemplate.tex
%{_texdir}/texmf-dist/doc/latex/revtex/sample/aps/fig_1.eps
%{_texdir}/texmf-dist/doc/latex/revtex/sample/aps/fig_2.eps
%{_texdir}/texmf-dist/doc/latex/revtex/sample/aps/vid_1a.eps
%{_texdir}/texmf-dist/doc/latex/revtex/sample/aps/vid_1b.eps
%{_texdir}/texmf-dist/doc/latex/revtex/source/aip.pdf
%{_texdir}/texmf-dist/doc/latex/revtex/source/ltxdocext.pdf
%{_texdir}/texmf-dist/doc/latex/revtex/source/ltxfront.pdf
%{_texdir}/texmf-dist/doc/latex/revtex/source/ltxgrid.pdf
%{_texdir}/texmf-dist/doc/latex/revtex/source/ltxutil.pdf
%{_texdir}/texmf-dist/doc/latex/revtex/source/revtex4-1.pdf


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
