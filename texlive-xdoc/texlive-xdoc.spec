%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/xdoc.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/xdoc.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/xdoc.source.tar.xz

Name: texlive-xdoc
License: LPPL
Summary: Extending the LaTeX doc system
Version: %{tl_version}
Release: %{tl_noarch_release}.prot2.5.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(docidx2e.sty)
Provides: tex(docindex.sty)
Provides: tex(xdoc2.sty)
Requires: tex(multicol.sty)
Requires: tex(doc.sty)

%description
Xdoc is a project to rewrite the implementation of the LaTeX
doc package (in a broader sense) to make its features more
general and flexible. For example, where doc only provides
commands for documenting macros and environments, xdoc also
provides commands for similarly documenting package options and
switches. This is furthermore done in such a way that it is
very easy to add more such commands for documenting things,
such as e.g., templates (an important concept in the future
LaTeX3) and program components for other languages (functions,
classes, procedures, etc.). A side effect is that many minor
bugs in doc are fixed. The design aims to take advantage of
many still experimental features of future versions of LaTeX,
but since these are neither reasonably stable nor widely
available, the configuration interfaces and package author
commands of xdoc are likely to change. To still provide a
stable interface for other packages to build upon, the actual
package names include a "major version number" of sorts. The
drop-in replacement package for standard doc is xdoc2; it
requires nothing outside standard LaTeX2e. The
docindex/docidx2e package changes the index and list of changes
typesetting so that none of the formatting has to be controlled
via the index style file. The docindex package provides control
of formatting via templates (nice interface, but requires
several experimental packages), whereas the docidx2e package
has traditional raw macro interfaces and works with standard
LaTeX2e.

date: 2006-12-05 00:47:24 +0100

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
Summary: Documentation for xdoc
Version: %{tl_version}
Release: %{tl_noarch_release}.prot2.5.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for xdoc


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
%{_texdir}/texmf-dist/makeindex/xdoc/docindex.ist
%{_texdir}/texmf-dist/tex/latex/xdoc/docidx2e.sty
%{_texdir}/texmf-dist/tex/latex/xdoc/docindex.sty
%{_texdir}/texmf-dist/tex/latex/xdoc/xdoc2.sty

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/xdoc/README
%{_texdir}/texmf-dist/doc/latex/xdoc/docindex.pdf
%{_texdir}/texmf-dist/doc/latex/xdoc/xdoc2.pdf
%{_texdir}/texmf-dist/doc/latex/xdoc/xdocdemo.pdf
%{_texdir}/texmf-dist/doc/latex/xdoc/xdocdemo.tex


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
