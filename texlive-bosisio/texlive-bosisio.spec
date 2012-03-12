%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/bosisio.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/bosisio.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/bosisio.source.tar.xz

Name: texlive-bosisio
License: LPPL
Summary: A collection of packages by Francesco Bosisio
Version: %{tl_version}
Release: %{tl_noarch_release}.svn16989%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(accenti.sty)
Provides: tex(dblfont.sty)
Provides: tex(envmath.sty)
Provides: tex(evenpage.sty)
Provides: tex(graphfig.sty)
Provides: tex(mathcmd.sty)
Provides: tex(quotes.sty)
Provides: tex(sobolev.sty)
Requires: tex(xspace.sty)
Requires: tex(graphics.sty)
Requires: tex(subfigure.sty)
Requires: tex(float.sty)

%description
A collection of packages containing: accenti dblfont; envmath;
evenpage; graphfig; mathcmd; quotes; and sobolev.

date: 2010-02-10 21:47:34 +0100

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
Summary: Documentation for bosisio
Version: %{tl_version}
Release: %{tl_noarch_release}.svn16989%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for bosisio


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
%{_texdir}/texmf-dist/tex/latex/bosisio/accenti.sty
%{_texdir}/texmf-dist/tex/latex/bosisio/dblfont.sty
%{_texdir}/texmf-dist/tex/latex/bosisio/envmath.sty
%{_texdir}/texmf-dist/tex/latex/bosisio/evenpage.sty
%{_texdir}/texmf-dist/tex/latex/bosisio/graphfig.sty
%{_texdir}/texmf-dist/tex/latex/bosisio/mathcmd.sty
%{_texdir}/texmf-dist/tex/latex/bosisio/quotes.sty
%{_texdir}/texmf-dist/tex/latex/bosisio/sobolev.sty

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/bosisio/README
%{_texdir}/texmf-dist/doc/latex/bosisio/accenti.html
%{_texdir}/texmf-dist/doc/latex/bosisio/accenti.pdf
%{_texdir}/texmf-dist/doc/latex/bosisio/dblfont.html
%{_texdir}/texmf-dist/doc/latex/bosisio/dblfont.pdf
%{_texdir}/texmf-dist/doc/latex/bosisio/envmath.html
%{_texdir}/texmf-dist/doc/latex/bosisio/envmath.pdf
%{_texdir}/texmf-dist/doc/latex/bosisio/evenpage.html
%{_texdir}/texmf-dist/doc/latex/bosisio/evenpage.pdf
%{_texdir}/texmf-dist/doc/latex/bosisio/graphfig.html
%{_texdir}/texmf-dist/doc/latex/bosisio/graphfig.pdf
%{_texdir}/texmf-dist/doc/latex/bosisio/index.html
%{_texdir}/texmf-dist/doc/latex/bosisio/makedoc
%{_texdir}/texmf-dist/doc/latex/bosisio/mathcmd.html
%{_texdir}/texmf-dist/doc/latex/bosisio/mathcmd.pdf
%{_texdir}/texmf-dist/doc/latex/bosisio/quotes.html
%{_texdir}/texmf-dist/doc/latex/bosisio/quotes.pdf
%{_texdir}/texmf-dist/doc/latex/bosisio/sobolev.html
%{_texdir}/texmf-dist/doc/latex/bosisio/sobolev.pdf


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
