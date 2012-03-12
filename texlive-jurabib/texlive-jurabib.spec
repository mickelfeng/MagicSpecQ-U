%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/jurabib.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/jurabib.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/jurabib.source.tar.xz

Name: texlive-jurabib
License: GPL+
Summary: Extended BibTeX citation support for the humanities and legal texts
Version: %{tl_version}
Release: %{tl_noarch_release}.0.6.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(dajbbib.sty)
Provides: tex(dejbbib.sty)
Provides: tex(dujbbib.sty)
Provides: tex(enjbbib.sty)
Provides: tex(fijbbib.sty)
Provides: tex(frjbbib.sty)
Provides: tex(itjbbib.sty)
Provides: tex(jurabib.sty)
Provides: tex(nojbbib.sty)
Provides: tex(ptjbbib.sty)
Provides: tex(spjbbib.sty)
Requires: tex(ifthen.sty)
Requires: tex(calc.sty)
Requires: tex(keyval.sty)
Requires: tex(url.sty)
Requires: tex(array.sty)

%description
This package enables automated citation with BibTeX for legal
studies and the humanities. In addition, the package provides
commands for specifying editors in a commentary in a convenient
way. Simplified formatting of the citation as well as the
bibliography entry is also provided. It is possible to display
the (short) title of a work only if an authors is cited with
multiple works. Giving a full citation in the text, conforming
to the bibliography entry, is supported. Several options are
provided which might be of special interest for those outside
legal studies--for instance, displaying multiple full
citations. In addition, the format of last names and first
names of authors may be changed easily. Cross references to
other footnotes are possible. Language dependent handling of
bibliography entries is possible by the special language field.

date: 2007-01-08 14:12:54 +0100

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
Summary: Documentation for jurabib
Version: %{tl_version}
Release: %{tl_noarch_release}.0.6.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for jurabib


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
%{_texdir}/texmf-dist/bibtex/bib/jurabib/book.bib
%{_texdir}/texmf-dist/bibtex/bib/jurabib/comment.bib
%{_texdir}/texmf-dist/bibtex/bib/jurabib/jbtest.bib
%{_texdir}/texmf-dist/bibtex/bib/jurabib/jbtesthu.bib
%{_texdir}/texmf-dist/bibtex/bst/jurabib/jox.bst
%{_texdir}/texmf-dist/bibtex/bst/jurabib/jurabib.bst
%{_texdir}/texmf-dist/bibtex/bst/jurabib/jureco.bst
%{_texdir}/texmf-dist/bibtex/bst/jurabib/jurunsrt.bst
%{_texdir}/texmf-dist/tex/latex/jurabib/dajbbib.ldf
%{_texdir}/texmf-dist/tex/latex/jurabib/dejbbib.ldf
%{_texdir}/texmf-dist/tex/latex/jurabib/dujbbib.ldf
%{_texdir}/texmf-dist/tex/latex/jurabib/enjbbib.ldf
%{_texdir}/texmf-dist/tex/latex/jurabib/fijbbib.ldf
%{_texdir}/texmf-dist/tex/latex/jurabib/frjbbib.ldf
%{_texdir}/texmf-dist/tex/latex/jurabib/itjbbib.ldf
%{_texdir}/texmf-dist/tex/latex/jurabib/jblong.cfg
%{_texdir}/texmf-dist/tex/latex/jurabib/jurabib.cfg
%{_texdir}/texmf-dist/tex/latex/jurabib/jurabib.sty
%{_texdir}/texmf-dist/tex/latex/jurabib/nojbbib.ldf
%{_texdir}/texmf-dist/tex/latex/jurabib/ptjbbib.ldf
%{_texdir}/texmf-dist/tex/latex/jurabib/spjbbib.ldf

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/latex/jurabib/changes.txt
%{_texdir}/texmf-dist/doc/latex/jurabib/jbtest.pdf
%{_texdir}/texmf-dist/doc/latex/jurabib/jbtest.tex
%{_texdir}/texmf-dist/doc/latex/jurabib/jbtest.url
%{_texdir}/texmf-dist/doc/latex/jurabib/jbtestbt.tex
%{_texdir}/texmf-dist/doc/latex/jurabib/jbtestbu.tex
%{_texdir}/texmf-dist/doc/latex/jurabib/jbtestcb.tex
%{_texdir}/texmf-dist/doc/latex/jurabib/jbtestcb1.tex
%{_texdir}/texmf-dist/doc/latex/jurabib/jbtestcb2.tex
%{_texdir}/texmf-dist/doc/latex/jurabib/jbtesthu.tex
%{_texdir}/texmf-dist/doc/latex/jurabib/jbtestmb.tex
%{_texdir}/texmf-dist/doc/latex/jurabib/docs/english/jbendoc.pdf
%{_texdir}/texmf-dist/doc/latex/jurabib/docs/english/jbendoc.tex
%{_texdir}/texmf-dist/doc/latex/jurabib/docs/german/jbgerdoc.pdf
%{_texdir}/texmf-dist/doc/latex/jurabib/docs/german/jbgerdoc.tex


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
