%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/amsrefs.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/amsrefs.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/amsrefs.source.tar.xz

Name: texlive-amsrefs
License: LPPL
Summary: A LaTeX-based replacement for BibTeX
Version: %{tl_version}
Release: %{tl_noarch_release}.2.03.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(amsbst.sty)
Provides: tex(amsrefs.sty)
Provides: tex(ifoption.sty)
Provides: tex(mathscinet.sty)
Provides: tex(pcatcode.sty)
Provides: tex(rkeyval.sty)
Provides: tex(textcmds.sty)
Requires: tex(url.sty)
Requires: tex(backref.sty)
Requires: tex(hyperref.sty)

%description
Amsrefs is a LaTeX package for bibliographies that provides an
archival data format similar to the format of BibTeX database
files, but adapted to make direct processing by LaTeX easier.
The package can be used either in conjunction with BibTeX or as
a replacement for BibTeX.

date: 2010-05-13 18:19:43 +0200

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
Summary: Documentation for amsrefs
Version: %{tl_version}
Release: %{tl_noarch_release}.2.03.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for amsrefs


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
%{_texdir}/texmf-dist/bibtex/bib/amsrefs/amsj.bib
%{_texdir}/texmf-dist/bibtex/bst/amsrefs/amsra.bst
%{_texdir}/texmf-dist/bibtex/bst/amsrefs/amsrn.bst
%{_texdir}/texmf-dist/bibtex/bst/amsrefs/amsrs.bst
%{_texdir}/texmf-dist/bibtex/bst/amsrefs/amsru.bst
%{_texdir}/texmf-dist/bibtex/bst/amsrefs/amsry.bst
%{_texdir}/texmf-dist/tex/latex/amsrefs/amsbst.sty
%{_texdir}/texmf-dist/tex/latex/amsrefs/amsrefs.sty
%{_texdir}/texmf-dist/tex/latex/amsrefs/ifoption.sty
%{_texdir}/texmf-dist/tex/latex/amsrefs/mathscinet.sty
%{_texdir}/texmf-dist/tex/latex/amsrefs/pcatcode.sty
%{_texdir}/texmf-dist/tex/latex/amsrefs/rkeyval.sty
%{_texdir}/texmf-dist/tex/latex/amsrefs/textcmds.sty

%files doc
%defattr(-,root,root)
%doc lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/amsrefs/amsrdoc.pdf
%{_texdir}/texmf-dist/doc/latex/amsrefs/amsrefs.faq
%{_texdir}/texmf-dist/doc/latex/amsrefs/amsrefs.pdf
%{_texdir}/texmf-dist/doc/latex/amsrefs/amsxport.pdf
%{_texdir}/texmf-dist/doc/latex/amsrefs/changes.pdf
%{_texdir}/texmf-dist/doc/latex/amsrefs/cite-xa.pdf
%{_texdir}/texmf-dist/doc/latex/amsrefs/cite-xa.tex
%{_texdir}/texmf-dist/doc/latex/amsrefs/cite-xb.pdf
%{_texdir}/texmf-dist/doc/latex/amsrefs/cite-xb.tex
%{_texdir}/texmf-dist/doc/latex/amsrefs/cite-xh.pdf
%{_texdir}/texmf-dist/doc/latex/amsrefs/cite-xh.tex
%{_texdir}/texmf-dist/doc/latex/amsrefs/cite-xs.pdf
%{_texdir}/texmf-dist/doc/latex/amsrefs/cite-xs.tex
%{_texdir}/texmf-dist/doc/latex/amsrefs/gktest.ltb
%{_texdir}/texmf-dist/doc/latex/amsrefs/ifoption.pdf
%{_texdir}/texmf-dist/doc/latex/amsrefs/jr.bib
%{_texdir}/texmf-dist/doc/latex/amsrefs/mathscinet.pdf
%{_texdir}/texmf-dist/doc/latex/amsrefs/pcatcode.pdf
%{_texdir}/texmf-dist/doc/latex/amsrefs/rkeyval.pdf
%{_texdir}/texmf-dist/doc/latex/amsrefs/textcmds.pdf


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
