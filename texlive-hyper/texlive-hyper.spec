%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/hyper.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/hyper.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/hyper.source.tar.xz

Name: texlive-hyper
License: LPPL
Summary: Hypertext cross referencing
Version: %{tl_version}
Release: %{tl_noarch_release}.4.2d.svn17357%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(hxt-bc.sty)
Provides: tex(hyper.sty)
Requires: tex(defpattern.sty)
Requires: tex(color.sty)

%description
Redefines LaTeX cross-referencing commands to insert \special
commands for HyperTeX dvi viewers, such as recent versions of
xdvi. The package is now largely superseded by hyperref.

date: 2010-03-06 16:54:30 +0100

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
Summary: Documentation for hyper
Version: %{tl_version}
Release: %{tl_noarch_release}.4.2d.svn17357%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for hyper


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
%{_texdir}/texmf-dist/tex/latex/hyper/amsart.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/amsbook.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/amsdtx.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/amsldoc.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/amsmath.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/amsproc.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/amstex.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/amsthm.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/article.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/book.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/cweb.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/doc.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/fancyheadings.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/ftnright.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/hxt-bc.sty
%{_texdir}/texmf-dist/tex/latex/hyper/hyper.sty
%{_texdir}/texmf-dist/tex/latex/hyper/leqno.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/letter.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/longtable.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/ltnews.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/ltxdoc.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/ltxguide.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/natbib.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/proc.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/report.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/slides.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/subeqnarray.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/theorem.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/upref.hyp
%{_texdir}/texmf-dist/tex/latex/hyper/xr.hyp

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/hyper/README
%{_texdir}/texmf-dist/doc/latex/hyper/TODO
%{_texdir}/texmf-dist/doc/latex/hyper/defpattern.sty
%{_texdir}/texmf-dist/doc/latex/hyper/hyper.pdf
%{_texdir}/texmf-dist/doc/latex/hyper/contrib/README
%{_texdir}/texmf-dist/doc/latex/hyper/contrib/harvard-to.hyp
%{_texdir}/texmf-dist/doc/latex/hyper/scontrib/README
%{_texdir}/texmf-dist/doc/latex/hyper/scontrib/harvard.hyp


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
