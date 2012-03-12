%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/AkkTeX.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/AkkTeX.doc.tar.xz

Name: texlive-AkkTeX
License: LPPL
Summary: A collection of packages and classes
Version: %{tl_version}
Release: %{tl_noarch_release}.0.3.2.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(akkconditional.sty)
Provides: tex(akkcounterlabelpattern.sty)
Provides: tex(akkcs.sty)
Provides: tex(akkdoc.sty)
Provides: tex(akkgerman.sty)
Provides: tex(akkgermanabbreviations.sty)
Provides: tex(akklecture.sty)
Provides: tex(akklongpage.sty)
Provides: tex(akkmath.sty)
Provides: tex(akkmathbasic.sty)
Provides: tex(akkmathdisc.sty)
Provides: tex(akkmathfun.sty)
Provides: tex(akkmathnum.sty)
Provides: tex(akkmathpaper.sty)
Provides: tex(akkmathproof.sty)
Provides: tex(akkmathrel.sty)
Provides: tex(akkmathset.sty)
Provides: tex(akkmathtext.sty)
Provides: tex(akknum.sty)
Provides: tex(akkparskip.sty)
Provides: tex(akkscript.sty)
Provides: tex(akksection.sty)
Provides: tex(akkstring.sty)
Provides: tex(akktecdoc.sty)
Provides: tex(akktex.sty)
Provides: tex(akkwidepage.sty)
Requires: tex(ifthen.sty)
Requires: tex(amsmath.sty)
Requires: tex(amssymb.sty)
Requires: tex(latexsym.sty)
Requires: tex(inputenc.sty)
Requires: tex(fontenc.sty)
Requires: tex(babel.sty)
Requires: tex(xspace.sty)
Requires: tex(fancyhdr.sty)
Requires: tex(amstext.sty)
Requires: tex(array.sty)
Requires: tex(theorem.sty)
Requires: tex(lscape.sty)
Requires: tex(longtable.sty)
Requires: tex(float.sty)
Requires: tex(enumerate.sty)
Requires: tex(verbatim.sty)
Requires: tex(calc.sty)

%description
The bundle provides: - new document classes for technical
documents, thesis works, manuscripts and lecture notes; - many
mathematical packages providing a large number of macros for
mathematical texts; - layout providing a non-empty parskip with
extended length corrections and new section definition
commands; - easy label creation for counters; and - german
language tools and predefined abbreviations.

date: 2008-05-16 01:27:14 +0200

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
Summary: Documentation for AkkTeX
Version: %{tl_version}
Release: %{tl_noarch_release}.0.3.2.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for AkkTeX


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
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akkconditional.sty
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akkcounterlabelpattern.sty
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akkcs.sty
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akkdoc.sty
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akkgerman.sty
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akkgermanabbreviations.sty
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akklecture.cls
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akklongpage.sty
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akkmath.sty
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akkmathbasic.sty
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akkmathdisc.sty
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akkmathfun.sty
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akkmathnum.sty
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akkmathpaper.sty
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akkmathproof.sty
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akkmathrel.sty
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akkmathset.sty
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akkmathtext.sty
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akknum.sty
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akkparskip.sty
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akkscript.cls
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akksection.sty
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akkstring.sty
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akktecdoc.cls
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akktex.sty
%{_texdir}/texmf-dist/tex/latex/AkkTeX/akkwidepage.sty

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/AkkTeX/README


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
