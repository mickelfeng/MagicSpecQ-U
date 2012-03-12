%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/ncclatex.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/ncclatex.doc.tar.xz

Name: texlive-ncclatex
License: LPPL
Summary: An extended general-purpose class
Version: %{tl_version}
Release: %{tl_noarch_release}.1.5.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(ncc.sty)
Provides: tex(nccbiblist.sty)
Provides: tex(nccdefaults.sty)
Provides: tex(ncchdr.sty)
Provides: tex(nccheadings.sty)
Provides: tex(nccindex.sty)
Provides: tex(ncclatex.sty)
Provides: tex(nccltrus.sty)
Provides: tex(nccold.sty)
Provides: tex(nccproc.sty)
Provides: tex(nccsections.sty)
Provides: tex(ncctheorems.sty)
Provides: tex(ncctitle.sty)
Provides: tex(ncctitlepage.sty)
Provides: tex(sibjnm.sty)
Requires: tex(afterpackage.sty)
Requires: tex(tocenter.sty)
Requires: tex(dcounter.sty)
Requires: tex(makeidx.sty)
Requires: tex(topsection.sty)
Requires: tex(watermark.sty)
Requires: tex(nccfancyhdr.sty)
Requires: tex(multicol.sty)
Requires: tex(desclist.sty)
Requires: tex(extdash.sty)
Requires: tex(nccmath.sty)
Requires: tex(nccsect.sty)
Requires: tex(nccthm.sty)
Requires: tex(nccboxes.sty)
Requires: tex(nccfoots.sty)
Requires: tex(nccpic.sty)
Requires: tex(nccfloats.sty)
Requires: tex(fontenc.sty)
Requires: tex(babel.sty)
Requires: tex(amstext.sty)
Requires: tex(textarea.sty)

%description
The ncc class provides a framework for a common class to
replace the standard article, book and report classes, and
providing a "preprint" class. The class's extensions are
provided in a number of small packages, some of which may also
be used with the standard classes. The ncclatex package also
loads many of the packages of, and requires the latest version
of the ncctools bundle.

date: 2007-02-23 22:01:12 +0100

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
Summary: Documentation for ncclatex
Version: %{tl_version}
Release: %{tl_noarch_release}.1.5.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for ncclatex


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
%{_texdir}/texmf-dist/tex/latex/ncclatex/cp1251-light.def
%{_texdir}/texmf-dist/tex/latex/ncclatex/ncc.cls
%{_texdir}/texmf-dist/tex/latex/ncclatex/ncc10.clo
%{_texdir}/texmf-dist/tex/latex/ncclatex/ncc11.clo
%{_texdir}/texmf-dist/tex/latex/ncclatex/ncc12.clo
%{_texdir}/texmf-dist/tex/latex/ncclatex/ncc14.clo
%{_texdir}/texmf-dist/tex/latex/ncclatex/nccart.clo
%{_texdir}/texmf-dist/tex/latex/ncclatex/nccbiblist.sty
%{_texdir}/texmf-dist/tex/latex/ncclatex/nccbook.clo
%{_texdir}/texmf-dist/tex/latex/ncclatex/nccdefaults.sty
%{_texdir}/texmf-dist/tex/latex/ncclatex/nccfit.clo
%{_texdir}/texmf-dist/tex/latex/ncclatex/ncchdr.sty
%{_texdir}/texmf-dist/tex/latex/ncclatex/nccheadings.sty
%{_texdir}/texmf-dist/tex/latex/ncclatex/nccindex.sty
%{_texdir}/texmf-dist/tex/latex/ncclatex/ncclatex.sty
%{_texdir}/texmf-dist/tex/latex/ncclatex/nccltrus.sty
%{_texdir}/texmf-dist/tex/latex/ncclatex/nccold.sty
%{_texdir}/texmf-dist/tex/latex/ncclatex/nccproc.cls
%{_texdir}/texmf-dist/tex/latex/ncclatex/nccsections.sty
%{_texdir}/texmf-dist/tex/latex/ncclatex/ncctheorems.sty
%{_texdir}/texmf-dist/tex/latex/ncclatex/ncctitle.clo
%{_texdir}/texmf-dist/tex/latex/ncclatex/ncctitle.sty
%{_texdir}/texmf-dist/tex/latex/ncclatex/ncctitlepage.sty
%{_texdir}/texmf-dist/tex/latex/ncclatex/sibjnm.cls

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/ncclatex/README
%{_texdir}/texmf-dist/doc/latex/ncclatex/changes.txt
%{_texdir}/texmf-dist/doc/latex/ncclatex/manifest.txt
%{_texdir}/texmf-dist/doc/latex/ncclatex/ncclatex.pdf
%{_texdir}/texmf-dist/doc/latex/ncclatex/ncclatex.tex
%{_texdir}/texmf-dist/doc/latex/ncclatex/nccnews.pdf


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
