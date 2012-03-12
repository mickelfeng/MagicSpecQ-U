%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/isodate.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/isodate.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/isodate.source.tar.xz

Name: texlive-isodate
License: LPPL
Summary: Tune the output format of dates according to language
Version: %{tl_version}
Release: %{tl_noarch_release}.2.28.svn16613%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(isodate.sty)
Provides: tex(isodateo.sty)
Requires: tex(ifthen.sty)
Requires: tex(substr.sty)
Requires: tex(calc.sty)

%description
This package provides ten output formats of the commands
\today, \printdate, \printdateTeX, and \daterange (partly
language dependent). Formats available are: ISO (yyyy-mm-dd),
numeric (e.g. dd.\,mm.~yyyy), short (e.g. dd.\,mm.\,yy), TeX
(yyyy/mm/dd), original (e.g. dd. mmm yyyy), short original
(e.g. dd. mmm yy), as well as numerical formats with Roman
numerals for the month. The commands \printdate and
\printdateTeX print any date. The command \daterange prints a
date range and leaves out unnecessary year or month entries.
This package supports German (old and new rules), Austrian, US
English, British English, French, Danish, Swedish, and
Norwegian.

date: 2006-12-08 14:34:19 +0100

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
Summary: Documentation for isodate
Version: %{tl_version}
Release: %{tl_noarch_release}.2.28.svn16613%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for isodate


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
%{_texdir}/texmf-dist/tex/latex/isodate/danish.idf
%{_texdir}/texmf-dist/tex/latex/isodate/english.idf
%{_texdir}/texmf-dist/tex/latex/isodate/french.idf
%{_texdir}/texmf-dist/tex/latex/isodate/german.idf
%{_texdir}/texmf-dist/tex/latex/isodate/isodate.sty
%{_texdir}/texmf-dist/tex/latex/isodate/isodateo.sty
%{_texdir}/texmf-dist/tex/latex/isodate/italian.idf
%{_texdir}/texmf-dist/tex/latex/isodate/norsk.idf
%{_texdir}/texmf-dist/tex/latex/isodate/swedish.idf

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/isodate/ChangeLog
%{_texdir}/texmf-dist/doc/latex/isodate/README
%{_texdir}/texmf-dist/doc/latex/isodate/getversion.tex
%{_texdir}/texmf-dist/doc/latex/isodate/isodate.pdf
%{_texdir}/texmf-dist/doc/latex/isodate/isodate.xml
%{_texdir}/texmf-dist/doc/latex/isodate/isodateo.pdf
%{_texdir}/texmf-dist/doc/latex/isodate/testdate.pdf
%{_texdir}/texmf-dist/doc/latex/isodate/testdate.tex
%{_texdir}/texmf-dist/doc/latex/isodate/testisodate_without_babel.tex


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
