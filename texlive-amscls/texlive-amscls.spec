%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/amscls.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/amscls.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/amscls.source.tar.xz

Name: texlive-amscls
License: LPPL
Summary: AMS document classes for LaTeX
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18435%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(amsart.sty)
Provides: tex(amsbook.sty)
Provides: tex(amsbooka.sty)
Provides: tex(amsdtx.sty)
Provides: tex(amsmidx.sty)
Provides: tex(amsproc.sty)
Provides: tex(amsthm.sty)
Provides: tex(rkvbeta.sty)
Provides: tex(upref.sty)
Requires: tex(amstex.sty)
Requires: tex(amsmath.sty)
Requires: tex(amsfonts.sty)
Requires: tex(url.sty)
Requires: tex(doc.sty)

%description
This directory contains three AMS classes, amsart (for writing
articles for the AMS), amsbook (for books) and amsproc (for
proceedings), together with some supporting material. The
material is made available as part of the AMS-LaTeX
distribution.

date: 2010-05-23 11:16:41 +0200

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
Summary: Documentation for amscls
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18435%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for amscls


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
%{_texdir}/texmf-dist/bibtex/bst/amscls/amsalpha.bst
%{_texdir}/texmf-dist/bibtex/bst/amscls/amsplain.bst
%{_texdir}/texmf-dist/tex/latex/amscls/amsart.cls
%{_texdir}/texmf-dist/tex/latex/amscls/amsbook.cls
%{_texdir}/texmf-dist/tex/latex/amscls/amsbooka.sty
%{_texdir}/texmf-dist/tex/latex/amscls/amsdtx.cls
%{_texdir}/texmf-dist/tex/latex/amscls/amsmidx.sty
%{_texdir}/texmf-dist/tex/latex/amscls/amsproc.cls
%{_texdir}/texmf-dist/tex/latex/amscls/amsthm.sty
#%{_texdir}/texmf-dist/tex/latex/amscls/rkvbeta.sty
%{_texdir}/texmf-dist/tex/latex/amscls/upref.sty
%{_texdir}/texmf-dist/tex/latex/amscls/amsldoc.cls

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/amscls/00LICENSE.txt
%{_texdir}/texmf-dist/doc/latex/amscls/amsart.template
%{_texdir}/texmf-dist/doc/latex/amscls/amsbook.template
%{_texdir}/texmf-dist/doc/latex/amscls/amsclass.pdf
%{_texdir}/texmf-dist/doc/latex/amscls/amsdtx.pdf
%{_texdir}/texmf-dist/doc/latex/amscls/amsmidx.pdf
%{_texdir}/texmf-dist/doc/latex/amscls/amsproc.template
%{_texdir}/texmf-dist/doc/latex/amscls/amsthdoc.pdf
%{_texdir}/texmf-dist/doc/latex/amscls/diffs-c.txt
%{_texdir}/texmf-dist/doc/latex/amscls/instr-l.pdf
%{_texdir}/texmf-dist/doc/latex/amscls/thmtest.pdf
%{_texdir}/texmf-dist/doc/latex/amscls/upref.pdf


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
