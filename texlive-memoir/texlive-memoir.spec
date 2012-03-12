%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/memoir.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/memoir.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/memoir.source.tar.xz

Name: texlive-memoir
License: LPPL
Summary: Typeset fiction, non-fiction and mathematical books
Version: %{tl_version}
Release: %{tl_noarch_release}.3.6d_patch_6.0g.svn19217%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(memhfixc.sty)
Provides: tex(memoir.sty)
Provides: tex(mempatch.sty)
Requires: tex(ifpdf.sty)
Requires: tex(ifxetex.sty)
Requires: tex(ifluatex.sty)
Requires: tex(etex.sty)

%description
The memoir class is for typesetting poetry, fiction, non-
fiction, and mathematical works. Permissible document 'base'
font sizes range from 9 to 60pt. There is a range of page-
styles and well over a dozen chapter-styles to choose from, as
well as methods for specifying your own layouts and designs.
The class also provides the functionality of over thirty of the
more popular packages, thus simplifying document sources. The
class automatically loads an associated patch file mempatch;
the patch file may be updated from time to time, between
releases of the class itself. (The patch file stays around even
when there are no extant patches.) Users who wish to use the
hyperref package, in a document written with the memoir class,
should also use the memhfixc package (part of this bundle).
Note, however, that current versions of hyperref actually load
the package automatically if they detect that they are running
under memoir.

date: 2010-07-01 20:01:23 +0200

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
Summary: Documentation for memoir
Version: %{tl_version}
Release: %{tl_noarch_release}.3.6d_patch_6.0g.svn19217%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for memoir


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
%{_texdir}/texmf-dist/makeindex/memoir/basic.gst
%{_texdir}/texmf-dist/tex/latex/memoir/mem10.clo
%{_texdir}/texmf-dist/tex/latex/memoir/mem11.clo
%{_texdir}/texmf-dist/tex/latex/memoir/mem12.clo
%{_texdir}/texmf-dist/tex/latex/memoir/mem14.clo
%{_texdir}/texmf-dist/tex/latex/memoir/mem17.clo
%{_texdir}/texmf-dist/tex/latex/memoir/mem20.clo
%{_texdir}/texmf-dist/tex/latex/memoir/mem25.clo
%{_texdir}/texmf-dist/tex/latex/memoir/mem30.clo
%{_texdir}/texmf-dist/tex/latex/memoir/mem36.clo
%{_texdir}/texmf-dist/tex/latex/memoir/mem48.clo
%{_texdir}/texmf-dist/tex/latex/memoir/mem60.clo
%{_texdir}/texmf-dist/tex/latex/memoir/mem9.clo
%{_texdir}/texmf-dist/tex/latex/memoir/memhfixc.sty
%{_texdir}/texmf-dist/tex/latex/memoir/memoir.cls
%{_texdir}/texmf-dist/tex/latex/memoir/mempatch.sty

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/memoir/Makeidxglo
%{_texdir}/texmf-dist/doc/latex/memoir/README
%{_texdir}/texmf-dist/doc/latex/memoir/anvil2.mps
%{_texdir}/texmf-dist/doc/latex/memoir/memfonts.sty
%{_texdir}/texmf-dist/doc/latex/memoir/memlays.sty
%{_texdir}/texmf-dist/doc/latex/memoir/memman.gst
%{_texdir}/texmf-dist/doc/latex/memoir/memman.ist
%{_texdir}/texmf-dist/doc/latex/memoir/memman.pdf
%{_texdir}/texmf-dist/doc/latex/memoir/memman.tex
%{_texdir}/texmf-dist/doc/latex/memoir/memnoidxnum.tex
%{_texdir}/texmf-dist/doc/latex/memoir/memsty.sty
%{_texdir}/texmf-dist/doc/latex/memoir/titlepages.sty
%{_texdir}/texmf-dist/doc/latex/memoir/trims-example.tex


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
