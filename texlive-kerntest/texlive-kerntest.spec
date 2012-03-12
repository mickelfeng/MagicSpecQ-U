%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/kerntest.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/kerntest.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/kerntest.source.tar.xz

Name: texlive-kerntest
License: LPPL
Summary: Print tables and generate control files to adjust kernings
Version: %{tl_version}
Release: %{tl_noarch_release}.1.32.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(kerntest.sty)
Requires: tex(geometry.sty)
Requires: tex(helvet.sty)
Requires: tex(calc.sty)
Requires: tex(longtable.sty)
Requires: tex(array.sty)
Requires: tex(color.sty)
Requires: tex(ifthen.sty)
Requires: tex(keyval.sty)
Requires: tex(fontenc.sty)

%description
This class makes it easy to generate tables that show many
different kerning pairs of an arbitrary font, usable by LaTeX.
It shows the kerning values that are used in the the font by
default. In addition, this class enables the user to alter the
kernings and to observe the results. Kerning pairs can be
defined for groups of similar glyphs at the same time. An mtx
file is generated automatically. The mtx file may then be
loaded by fontinst to introduce the user-made kernings into the
virtual font for later use in LaTeX.

date: 2007-03-08 21:58:53 +0100

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
Summary: Documentation for kerntest
Version: %{tl_version}
Release: %{tl_noarch_release}.1.32.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for kerntest


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
%{_texdir}/texmf-dist/tex/latex/kerntest/kerntest.cls
%{_texdir}/texmf-dist/tex/latex/kerntest/ly1mtx.clo
%{_texdir}/texmf-dist/tex/latex/kerntest/ot1mtx.clo
%{_texdir}/texmf-dist/tex/latex/kerntest/t1cmr-1200.fd
%{_texdir}/texmf-dist/tex/latex/kerntest/t1mtx.clo
%{_texdir}/texmf-dist/tex/latex/kerntest/t2amtx.clo
%{_texdir}/texmf-dist/tex/latex/kerntest/t2bmtx.clo
%{_texdir}/texmf-dist/tex/latex/kerntest/ts1mtx.clo

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/kerntest/ChangeLog
%{_texdir}/texmf-dist/doc/latex/kerntest/README
%{_texdir}/texmf-dist/doc/latex/kerntest/ToDo
%{_texdir}/texmf-dist/doc/latex/kerntest/kerntest.pdf
%{_texdir}/texmf-dist/doc/latex/kerntest/krntst-v.tex
%{_texdir}/texmf-dist/doc/latex/kerntest/ot1-XXX-m-n.tex
%{_texdir}/texmf-dist/doc/latex/kerntest/schoolb.map
%{_texdir}/texmf-dist/doc/latex/kerntest/schoolb1.tex
%{_texdir}/texmf-dist/doc/latex/kerntest/schoolb2.tex
%{_texdir}/texmf-dist/doc/latex/kerntest/t1-9nc-m-n-1.tex
%{_texdir}/texmf-dist/doc/latex/kerntest/t1-9nc-m-n-2.tex
%{_texdir}/texmf-dist/doc/latex/kerntest/t1-XXX-m-n.tex
%{_texdir}/texmf-dist/doc/latex/kerntest/t1-cmr-m-n-1200.tex
%{_texdir}/texmf-dist/doc/latex/kerntest/t1-ptm-bx-n-example.tex
%{_texdir}/texmf-dist/doc/latex/kerntest/t1-ptm-m-n-shortexample.tex
%{_texdir}/texmf-dist/doc/latex/kerntest/t1-ptm-m-n.tex
%{_texdir}/texmf-dist/doc/latex/kerntest/testschoolb.tex
%{_texdir}/texmf-dist/doc/latex/kerntest/ts1-XXX-m-n.tex


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
