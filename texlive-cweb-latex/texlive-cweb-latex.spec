%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cweb-latex.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cweb-latex.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cweb-latex.source.tar.xz

Name: texlive-cweb-latex
License: GPL+
Summary: A LaTeX version of CWEB
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(cwbl-german.sty)
Provides: tex(cweb.sty)
Provides: tex(cwebarray.sty)
Provides: tex(keyvald.sty)
Requires: tex(array.sty)

%description
This bundle allows marking-up of CWEB code in LaTeX. The
distribution includes the "Counting Words" program distributed
with CWEB, edited to run with LaTeX.

date: 2008-08-18 10:38:42 +0200

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
Summary: Documentation for cweb-latex
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for cweb-latex


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/gpl.txt gpl.txt
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
%doc gpl.txt
%{_texdir}/texmf-dist/tex/latex/cweb-latex/cwbl-german.sty
%{_texdir}/texmf-dist/tex/latex/cweb-latex/cweb.cls
%{_texdir}/texmf-dist/tex/latex/cweb-latex/cweb.cls.patch
%{_texdir}/texmf-dist/tex/latex/cweb-latex/cwebarray.sty
%{_texdir}/texmf-dist/tex/latex/cweb-latex/keyvald.sty

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/latex/cweb-latex/CATALOG
%{_texdir}/texmf-dist/doc/latex/cweb-latex/History
%{_texdir}/texmf-dist/doc/latex/cweb-latex/INSTALL
%{_texdir}/texmf-dist/doc/latex/cweb-latex/License
%{_texdir}/texmf-dist/doc/latex/cweb-latex/MANIFEST
%{_texdir}/texmf-dist/doc/latex/cweb-latex/README
%{_texdir}/texmf-dist/doc/latex/cweb-latex/cweb-conf.pdf
%{_texdir}/texmf-dist/doc/latex/cweb-latex/cweb-user.pdf
%{_texdir}/texmf-dist/doc/latex/cweb-latex/cwebbase.tex
%{_texdir}/texmf-dist/doc/latex/cweb-latex/contrib/Index
%{_texdir}/texmf-dist/doc/latex/cweb-latex/contrib/cwbl-deutsch.sty
%{_texdir}/texmf-dist/doc/latex/cweb-latex/contrib/cwbl-french.sty
%{_texdir}/texmf-dist/doc/latex/cweb-latex/contrib/cwbl-italian.sty
%{_texdir}/texmf-dist/doc/latex/cweb-latex/contrib/cweb-hy/README.txt
%{_texdir}/texmf-dist/doc/latex/cweb-latex/contrib/cweb-hy/cwbasehy.tex
%{_texdir}/texmf-dist/doc/latex/cweb-latex/contrib/cweb-hy/cweb-hy.cls
%{_texdir}/texmf-dist/doc/latex/cweb-latex/contrib/cweb-hy/nodoc.tex
%{_texdir}/texmf-dist/doc/latex/cweb-latex/contrib/wagner/cwebzw.sty
%{_texdir}/texmf-dist/doc/latex/cweb-latex/examples/Makefile
%{_texdir}/texmf-dist/doc/latex/cweb-latex/examples/rcs.sty
%{_texdir}/texmf-dist/doc/latex/cweb-latex/examples/tex-it
%{_texdir}/texmf-dist/doc/latex/cweb-latex/examples/wcltx.bib
%{_texdir}/texmf-dist/doc/latex/cweb-latex/examples/wcltx.w
%{_texdir}/texmf-dist/doc/latex/cweb-latex/examples/compare/wcltx.aux
%{_texdir}/texmf-dist/doc/latex/cweb-latex/examples/compare/wcltx.bbl
%{_texdir}/texmf-dist/doc/latex/cweb-latex/examples/compare/wcltx.dvi
%{_texdir}/texmf-dist/doc/latex/cweb-latex/examples/compare/wcltx.idx
%{_texdir}/texmf-dist/doc/latex/cweb-latex/examples/compare/wcltx.log
%{_texdir}/texmf-dist/doc/latex/cweb-latex/examples/compare/wcltx.scn
%{_texdir}/texmf-dist/doc/latex/cweb-latex/examples/compare/wcltx.tex
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/Imakefile
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/README
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/TODO
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/cwbl-german.sty
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/cweave-spec.tex
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/cweb-conf.tex
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/cweb-doc.sty
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/cweb-fsa.fig
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/cweb-fsa.latex
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/cweb-fsa.ltx
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/cweb-user.tex
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/cweb.doc
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/cwebarray.sty
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/cwebbase.doc
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/cwebparts.doc
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/cwebx.sty
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/keyvald.dtx
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/keyvald.ins
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/style/cweb-doc.el
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/Imakefile
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/badend.w
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/badopts.w
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/change.ch
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/change.w
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/enddocbegin.w
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/flat.w
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/german.w
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/language-german.ch
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/language-german.w
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/minimal.w
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/modes.w
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/newif.w
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/nolists.w
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/parts-code.w
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/parts.tex
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/refname.w
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/report.w
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/section.w
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/sup-changes.w
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/sup-format.w
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/sup-lists.w
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/titlepage.w
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/token.w
%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test/vbar.w


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
