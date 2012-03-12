%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/songbook.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/songbook.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/songbook.source.tar.xz

Name: texlive-songbook
License: LGPLv2+
Summary: Package for typesetting song lyrics and chord books
Version: %{tl_version}
Release: %{tl_noarch_release}.4.5.svn18136%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(conditionals.sty)
Provides: tex(songbook.sty)
Requires: tex(calc.sty)
Requires: tex(ifthen.sty)
Requires: tex(xstring.sty)
Requires: tex(multicol.sty)

%description
The package provides an all purpose songbook style. Three types
of output may be created from a single input file: "words and
chords" books for the musicians to play from, "words only"
songbooks for the congregation to sing from, and overhead
transparency masters for congregational use. The package will
also print a table of contents, an index sorted by title and
first line, and an index sorted by key, or by artist/composer.
The package attempts to handle songs in multiple keys, as well
as songs in multiple languages.

date: 2010-05-06 13:38:32 +0200

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
Summary: Documentation for songbook
Version: %{tl_version}
Release: %{tl_noarch_release}.4.5.svn18136%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for songbook


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/lgpl.txt lgpl.txt
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
%doc lgpl.txt
%{_texdir}/texmf-dist/makeindex/songbook/songbook.ist
%{_texdir}/texmf-dist/tex/latex/songbook/conditionals.sty
%{_texdir}/texmf-dist/tex/latex/songbook/songbook.sty

%files doc
%defattr(-,root,root)
%doc lgpl.txt
%{_texdir}/texmf-dist/doc/latex/songbook/LesserGPL.txt
%{_texdir}/texmf-dist/doc/latex/songbook/README
%{_texdir}/texmf-dist/doc/latex/songbook/install.txt
%{_texdir}/texmf-dist/doc/latex/songbook/mksbadx
%{_texdir}/texmf-dist/doc/latex/songbook/mksbkdx
%{_texdir}/texmf-dist/doc/latex/songbook/mksbtdx
%{_texdir}/texmf-dist/doc/latex/songbook/sample-sb.tex
%{_texdir}/texmf-dist/doc/latex/songbook/sampleAdx.pdf
%{_texdir}/texmf-dist/doc/latex/songbook/sampleAdx.tex
%{_texdir}/texmf-dist/doc/latex/songbook/sampleCBK.pdf
%{_texdir}/texmf-dist/doc/latex/songbook/sampleCSBK.pdf
%{_texdir}/texmf-dist/doc/latex/songbook/sampleKdx.pdf
%{_texdir}/texmf-dist/doc/latex/songbook/sampleKdx.tex
%{_texdir}/texmf-dist/doc/latex/songbook/sampleOH.pdf
%{_texdir}/texmf-dist/doc/latex/songbook/sampleTdx.pdf
%{_texdir}/texmf-dist/doc/latex/songbook/sampleTdx.tex
%{_texdir}/texmf-dist/doc/latex/songbook/sampleToc.pdf
%{_texdir}/texmf-dist/doc/latex/songbook/sampleToc.tex
%{_texdir}/texmf-dist/doc/latex/songbook/sampleWBK.pdf
%{_texdir}/texmf-dist/doc/latex/songbook/songbook.pdf
%{_texdir}/texmf-dist/doc/latex/songbook/contrib/CarolBook/CarolBook.tex
%{_texdir}/texmf-dist/doc/latex/songbook/contrib/CarolBook/CarolBookOH.pdf
%{_texdir}/texmf-dist/doc/latex/songbook/contrib/CarolBook/CarolBookWB.pdf
%{_texdir}/texmf-dist/doc/latex/songbook/contrib/README
%{_texdir}/texmf-dist/doc/latex/songbook/contrib/modulate
%{_texdir}/texmf-dist/doc/latex/songbook/contrib/texchord.sty
%{_texdir}/texmf-dist/doc/latex/songbook/contrib/crd2sb/NothingButTheBlood.crd
%{_texdir}/texmf-dist/doc/latex/songbook/contrib/crd2sb/crd2sb
%{_texdir}/texmf-dist/doc/latex/songbook/contrib/crd2sb/crd2sb.txt


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
