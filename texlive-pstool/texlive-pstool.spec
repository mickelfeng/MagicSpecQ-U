%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/pstool.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/pstool.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/pstool.source.tar.xz

Name: texlive-pstool
License: LPPL
Summary: Support for psfrag within pdfLaTeX
Version: %{tl_version}
Release: %{tl_noarch_release}.1.3.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(pstool.sty)
Requires: tex(catchfile.sty)
Requires: tex(color.sty)
Requires: tex(ifpdf.sty)
Requires: tex(ifplatform.sty)
Requires: tex(graphicx.sty)
Requires: tex(pdftexcmds.sty)
Requires: tex(psfrag.sty)
Requires: tex(suffix.sty)
Requires: tex(xkeyval.sty)

%description
The package works in the same sort of way as pst-pdf,
processing PostScript graphics with psfrag labels within
documents running with pdfLaTeX. Pstool ensures that each
version of each graphic is compiled once only (the graphic is
(re-)compiled only if it has changed since the previous
compilation of the document). This drastically speeds up the
running of the package in the typical case (though the first
run of any document is inevitably just as slow as with any
similar package).

date: 2009-08-04 11:31:22 +0200

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
Summary: Documentation for pstool
Version: %{tl_version}
Release: %{tl_noarch_release}.1.3.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for pstool


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
%{_texdir}/texmf-dist/tex/latex/pstool/pstool.sty

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/pstool/.tex
%{_texdir}/texmf-dist/doc/latex/pstool/README
%{_texdir}/texmf-dist/doc/latex/pstool/example.aux
%{_texdir}/texmf-dist/doc/latex/pstool/example.log
%{_texdir}/texmf-dist/doc/latex/pstool/example.pdf
%{_texdir}/texmf-dist/doc/latex/pstool/example.synctex
%{_texdir}/texmf-dist/doc/latex/pstool/example.tex
%{_texdir}/texmf-dist/doc/latex/pstool/macros.tex
%{_texdir}/texmf-dist/doc/latex/pstool/pstool.pdf
%{_texdir}/texmf-dist/doc/latex/pstool/trial.eps
%{_texdir}/texmf-dist/doc/latex/pstool/trial.pdf
%{_texdir}/texmf-dist/doc/latex/pstool/trial.tex
%{_texdir}/texmf-dist/doc/latex/pstool/subdir/trial2-psfrag.eps
%{_texdir}/texmf-dist/doc/latex/pstool/subdir/trial2-psfrag.pdf
%{_texdir}/texmf-dist/doc/latex/pstool/subdir/trial2-psfrag.tex


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
