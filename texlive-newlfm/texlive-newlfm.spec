%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/newlfm.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/newlfm.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/newlfm.source.tar.xz

Name: texlive-newlfm
License: GPL+
Summary: Write letters, facsimiles, and memos
Version: %{tl_version}
Release: %{tl_noarch_release}.9.4.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(addrset.sty)
Provides: tex(newlfm.sty)
Provides: tex(setdim.sty)
Requires: tex(keyval.sty)
Requires: tex(ifthen.sty)
Requires: tex(ifpdf.sty)
Requires: tex(fancyhdr.sty)
Requires: tex(eso-pic.sty)
Requires: tex(setspace.sty)
Requires: tex(lastpage.sty)
Requires: tex(calc.sty)
Requires: tex(graphicx.sty)
Requires: tex(rotating.sty)
Requires: tex(afterpage.sty)
Requires: tex(envlab.sty)

%description
Integrates the letter class with fancyhdr and geometry to
automatically make letterhead stationery. Useful for writing
letters, fax, and memos. You can set up an address book using
'wrapper' macros. You put all the information for a person into
a wrapper and then put the wrapper in a document. The class
handles letterheads automatically. You place the object for the
letterhead (picture, information, etc.) in a box and all sizing
is set automatically.

date: 2009-04-12 19:35:00 +0200

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
Summary: Documentation for newlfm
Version: %{tl_version}
Release: %{tl_noarch_release}.9.4.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for newlfm


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
%{_texdir}/texmf-dist/tex/latex/newlfm/addrset.sty
%{_texdir}/texmf-dist/tex/latex/newlfm/newlfm.cls
%{_texdir}/texmf-dist/tex/latex/newlfm/setdim.sty

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/latex/newlfm/README
%{_texdir}/texmf-dist/doc/latex/newlfm/chk1.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/demoa.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/draft.eps
%{_texdir}/texmf-dist/doc/latex/newlfm/draft.pdf
%{_texdir}/texmf-dist/doc/latex/newlfm/extracd.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/hletrinf.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/letrinfo.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/lvb.eps
%{_texdir}/texmf-dist/doc/latex/newlfm/lvb.pdf
%{_texdir}/texmf-dist/doc/latex/newlfm/make_clean
%{_texdir}/texmf-dist/doc/latex/newlfm/make_unix
%{_texdir}/texmf-dist/doc/latex/newlfm/make_win.bat
%{_texdir}/texmf-dist/doc/latex/newlfm/makeclean_win.bat
%{_texdir}/texmf-dist/doc/latex/newlfm/manual.pdf
%{_texdir}/texmf-dist/doc/latex/newlfm/mintrx.bat
%{_texdir}/texmf-dist/doc/latex/newlfm/newlfm.pdf
%{_texdir}/texmf-dist/doc/latex/newlfm/newlfm.txt
%{_texdir}/texmf-dist/doc/latex/newlfm/palm.eps
%{_texdir}/texmf-dist/doc/latex/newlfm/palm.pdf
%{_texdir}/texmf-dist/doc/latex/newlfm/problems.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/prx.bat
%{_texdir}/texmf-dist/doc/latex/newlfm/setup.bat
%{_texdir}/texmf-dist/doc/latex/newlfm/sfaxpage.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/smemosec.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/sprsrls.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/test1.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/test10.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/test11.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/test12.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/test1alt.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/test2.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/test2a.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/test2alt.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/test3.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/test3alt.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/test4.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/test4alt.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/test5.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/test5alt.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/test6.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/test6alt.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/test7.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/test7alt.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/test8.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/test8alt.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/test9.tex
%{_texdir}/texmf-dist/doc/latex/newlfm/testms.pdf
%{_texdir}/texmf-dist/doc/latex/newlfm/wine.eps
%{_texdir}/texmf-dist/doc/latex/newlfm/wine.pdf


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
