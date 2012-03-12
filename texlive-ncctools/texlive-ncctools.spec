%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/ncctools.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/ncctools.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/ncctools.source.tar.xz

Name: texlive-ncctools
License: LPPL
Summary: A collection of general packages for LaTeX
Version: %{tl_version}
Release: %{tl_noarch_release}.3.5.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(afterpackage.sty)
Provides: tex(dcounter.sty)
Provides: tex(desclist.sty)
Provides: tex(extdash.sty)
Provides: tex(manyfoot.sty)
Provides: tex(mboxfill.sty)
Provides: tex(nccbbb.sty)
Provides: tex(nccboxes.sty)
Provides: tex(ncccomma.sty)
Provides: tex(ncccropbox.sty)
Provides: tex(ncccropmark.sty)
Provides: tex(nccfancyhdr.sty)
Provides: tex(nccfloats.sty)
Provides: tex(nccfoots.sty)
Provides: tex(nccmath.sty)
Provides: tex(nccparskip.sty)
Provides: tex(nccpic.sty)
Provides: tex(nccrules.sty)
Provides: tex(nccsect.sty)
Provides: tex(nccstretch.sty)
Provides: tex(nccthm.sty)
Provides: tex(textarea.sty)
Provides: tex(tocenter.sty)
Provides: tex(topsection.sty)
Provides: tex(watermark.sty)
Requires: tex(perpage.sty)
Requires: tex(amsmath.sty)
Requires: tex(graphicx.sty)
Requires: tex(amsgen.sty)

%description
The NCCtools bundle contains many packages for general use
under LaTeX; many are also used by NCC LaTeX. The bundle
includes tools for: - executing commands after a package is
loaded; - watermarks; - counter manipulation (dynamic counters,
changing counter numbering with another counter); -
improvements to the description environment; - hyphenation of
compound words; - new levels of footnotes; - space-filling
patterns; - "poor man's" Black Board Bold symbols; - alignment
of the content of a box; - use comma as decimal separator; -
boxes with their own crop marks; - page cropmarks; -
improvements to fancy headers; - float "styles", mini floats,
side floats; - manually marked footnotes; - extension of
amsmath; - control of paragraph skip; - an envelope to the
graphicx package; - dashed and multiple rules; - alternative
techniques for declarations of sections, captions, and toc-
entries; - generalised text-stretching; - generation of new
theorem-like environments; - control of the text area; -
centred page layouts; and - an un-numbered top-level section.

date: 2008-02-08 09:08:04 +0100

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
Summary: Documentation for ncctools
Version: %{tl_version}
Release: %{tl_noarch_release}.3.5.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for ncctools


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
%{_texdir}/texmf-dist/tex/latex/ncctools/afterpackage.sty
%{_texdir}/texmf-dist/tex/latex/ncctools/dcounter.sty
%{_texdir}/texmf-dist/tex/latex/ncctools/desclist.sty
%{_texdir}/texmf-dist/tex/latex/ncctools/extdash.sty
%{_texdir}/texmf-dist/tex/latex/ncctools/manyfoot.sty
%{_texdir}/texmf-dist/tex/latex/ncctools/mboxfill.sty
%{_texdir}/texmf-dist/tex/latex/ncctools/nccbbb.sty
%{_texdir}/texmf-dist/tex/latex/ncctools/nccboxes.sty
%{_texdir}/texmf-dist/tex/latex/ncctools/ncccomma.sty
%{_texdir}/texmf-dist/tex/latex/ncctools/ncccropbox.sty
%{_texdir}/texmf-dist/tex/latex/ncctools/ncccropmark.sty
%{_texdir}/texmf-dist/tex/latex/ncctools/nccfancyhdr.sty
%{_texdir}/texmf-dist/tex/latex/ncctools/nccfloats.sty
%{_texdir}/texmf-dist/tex/latex/ncctools/nccfoots.sty
%{_texdir}/texmf-dist/tex/latex/ncctools/nccmath.sty
%{_texdir}/texmf-dist/tex/latex/ncctools/nccparskip.sty
%{_texdir}/texmf-dist/tex/latex/ncctools/nccpic.sty
%{_texdir}/texmf-dist/tex/latex/ncctools/nccrules.sty
%{_texdir}/texmf-dist/tex/latex/ncctools/nccsect.sty
%{_texdir}/texmf-dist/tex/latex/ncctools/nccstretch.sty
%{_texdir}/texmf-dist/tex/latex/ncctools/nccthm.sty
%{_texdir}/texmf-dist/tex/latex/ncctools/textarea.sty
%{_texdir}/texmf-dist/tex/latex/ncctools/tocenter.sty
%{_texdir}/texmf-dist/tex/latex/ncctools/topsection.sty
%{_texdir}/texmf-dist/tex/latex/ncctools/watermark.sty

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/ncctools/README
%{_texdir}/texmf-dist/doc/latex/ncctools/README.source
%{_texdir}/texmf-dist/doc/latex/ncctools/afterpackage.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/changes.txt
%{_texdir}/texmf-dist/doc/latex/ncctools/dcounter.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/desclist.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/extdash.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/manifest.txt
%{_texdir}/texmf-dist/doc/latex/ncctools/manyfoot.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/mboxfill.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/nccbbb.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/nccboxes.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/ncccomma.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/ncccropbox.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/ncccropmark.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/nccfancyhdr.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/nccfloats.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/nccfoots.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/nccmath.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/nccparskip.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/nccpic.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/nccrules.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/nccsect.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/nccstretch.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/nccthm.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/ncctools.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/ncctools.tex
%{_texdir}/texmf-dist/doc/latex/ncctools/textarea.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/tocenter.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/topsection.pdf
%{_texdir}/texmf-dist/doc/latex/ncctools/watermark.pdf


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
