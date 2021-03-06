%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/labels.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/labels.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/labels.source.tar.xz

Name: texlive-labels
License: LPPL
Summary: Print sheets of sticky labels
Version: %{tl_version}
Release: %{tl_noarch_release}.13.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(labels.sty)
Provides: tex(olabels.sty)

%description
A LaTeX package to print a regular grid of ragged-right labels
on a page, suitable for sheets of labels which can be fed
through a printer. Macros are provided to allow easy input of
names and addresses in a form free of TeX markup. Equally
useful is a feature for making multiple copies of a single
label, e.g., return address stickers to go with the labels.
Rows, columns, borders can all be specified to match the label
sheet being used.

date: 2009-09-29 00:01:21 +0200

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
Summary: Documentation for labels
Version: %{tl_version}
Release: %{tl_noarch_release}.13.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for labels


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/lppl1.2.txt lppl1.2.txt
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
%doc lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/labels/labels.sty
%{_texdir}/texmf-dist/tex/latex/labels/olabels.sty

%files doc
%defattr(-,root,root)
%doc lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/labels/README
%{_texdir}/texmf-dist/doc/latex/labels/labels.pdf
%{_texdir}/texmf-dist/doc/latex/labels/test/avery5162.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/badge.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/beebe.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/door.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/door209.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/names.dat
%{_texdir}/texmf-dist/doc/latex/labels/test/news.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/test.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/test1.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/test10.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/test11.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/test12.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/test2.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/test3.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/test4.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/test5.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/test6.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/test7.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/test8.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/test9.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/testnew.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/testnew1.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/testnew10.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/testnew11.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/testnew12.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/testnew13.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/testnew2.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/testnew3.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/testnew4.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/testnew5.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/testnew6.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/testnew7.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/testnew8.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/testnew9.tex
%{_texdir}/texmf-dist/doc/latex/labels/test/zwekform.tex


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
