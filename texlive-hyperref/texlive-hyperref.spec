%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/hyperref.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/hyperref.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/hyperref.source.tar.xz

Name: texlive-hyperref
License: LPPL
Summary: Extensive support for hypertext in LaTeX
Version: %{tl_version}
Release: %{tl_noarch_release}.6.81f.svn19066%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(backref.sty)
Provides: tex(hyperref.sty)
Provides: tex(minitoc-hyper.sty)
Provides: tex(minitoc.sty)
Provides: tex(nameref.sty)
Provides: tex(nohyperref.sty)
Provides: tex(ntheorem-hyper.sty)
Provides: tex(xr-hyper.sty)
Requires: tex(rerunfilecheck.sty)
Requires: tex(ltxcmds.sty)
Requires: tex(keyval.sty)
Requires: tex(kvsetkeys.sty)
Requires: tex(pdfescape.sty)
Requires: tex(ifpdf.sty)
Requires: tex(ifvtex.sty)
Requires: tex(ifxetex.sty)
Requires: tex(hycolor.sty)
Requires: tex(letltxmacro.sty)
Requires: tex(pdftexcmds.sty)
Requires: tex(intcalc.sty)
Requires: tex(etexcmds.sty)
Requires: tex(memhfixc.sty)
Requires: tex(stringenc.sty)
Requires: tex(kvoptions.sty)
Requires: tex(color.sty)
Requires: tex(url.sty)
Requires: tex(bitset.sty)
Requires: tex(atbegshi.sty)
Requires: tex(refcount.sty)
Requires: tex(gettitlestring.sty)

%description
The hyperref package is used to handle cross-referencing
commands in LaTeX to produce hypertext links in the document.
The package provides backends for the \special set defined for
HyperTeX DVI processors; for embedded pdfmark commands for
processing by Acrobat Distiller (dvips and Y&Y's dvipsone); for
Y&Y's dviwindo; for PDF control within pdfTeX and dvipdfm; for
TeX4ht; and for VTeX's pdf and HTML backends. The package is
distributed with the backref and nameref packages, which make
use of the facilities of hyperref. The package depends on the
author's kvoptions, ltxcmdsand refcount packages.

date: 2010-06-05 08:36:56 +0200

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
Summary: Documentation for hyperref
Version: %{tl_version}
Release: %{tl_noarch_release}.6.81f.svn19066%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for hyperref


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
%{_texdir}/texmf-dist/tex/latex/hyperref/backref.sty
%{_texdir}/texmf-dist/tex/latex/hyperref/hdvipdfm.def
%{_texdir}/texmf-dist/tex/latex/hyperref/hdvips.def
%{_texdir}/texmf-dist/tex/latex/hyperref/hdvipson.def
%{_texdir}/texmf-dist/tex/latex/hyperref/hdviwind.def
%{_texdir}/texmf-dist/tex/latex/hyperref/hpdftex.def
%{_texdir}/texmf-dist/tex/latex/hyperref/htex4ht.cfg
%{_texdir}/texmf-dist/tex/latex/hyperref/htex4ht.def
%{_texdir}/texmf-dist/tex/latex/hyperref/htexture.def
%{_texdir}/texmf-dist/tex/latex/hyperref/hvtex.def
%{_texdir}/texmf-dist/tex/latex/hyperref/hvtexhtm.def
%{_texdir}/texmf-dist/tex/latex/hyperref/hvtexmrk.def
%{_texdir}/texmf-dist/tex/latex/hyperref/hxetex.def
%{_texdir}/texmf-dist/tex/latex/hyperref/hylatex.ltx
%{_texdir}/texmf-dist/tex/latex/hyperref/hyperref.sty
%{_texdir}/texmf-dist/tex/latex/hyperref/hypertex.def
%{_texdir}/texmf-dist/tex/latex/hyperref/minitoc-hyper.sty
%{_texdir}/texmf-dist/tex/latex/hyperref/nameref.sty
%{_texdir}/texmf-dist/tex/latex/hyperref/nohyperref.sty
%{_texdir}/texmf-dist/tex/latex/hyperref/ntheorem-hyper.sty
%{_texdir}/texmf-dist/tex/latex/hyperref/pd1enc.def
%{_texdir}/texmf-dist/tex/latex/hyperref/pdfmark.def
%{_texdir}/texmf-dist/tex/latex/hyperref/puarenc.def
%{_texdir}/texmf-dist/tex/latex/hyperref/puenc.def
%{_texdir}/texmf-dist/tex/latex/hyperref/puvnenc.def
%{_texdir}/texmf-dist/tex/latex/hyperref/xr-hyper.sty

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/hyperref/ChangeLog
%{_texdir}/texmf-dist/doc/latex/hyperref/ChangeLog.pdf
%{_texdir}/texmf-dist/doc/latex/hyperref/README
%{_texdir}/texmf-dist/doc/latex/hyperref/README.pdf
%{_texdir}/texmf-dist/doc/latex/hyperref/backref.pdf
%{_texdir}/texmf-dist/doc/latex/hyperref/cmmi10-22.gif
%{_texdir}/texmf-dist/doc/latex/hyperref/cmsy10-21.gif
%{_texdir}/texmf-dist/doc/latex/hyperref/hyperref.pdf
%{_texdir}/texmf-dist/doc/latex/hyperref/manual.css
%{_texdir}/texmf-dist/doc/latex/hyperref/manual.html
%{_texdir}/texmf-dist/doc/latex/hyperref/manual.pdf
%{_texdir}/texmf-dist/doc/latex/hyperref/manual2.html
%{_texdir}/texmf-dist/doc/latex/hyperref/manual3.html
%{_texdir}/texmf-dist/doc/latex/hyperref/nameref.pdf
%{_texdir}/texmf-dist/doc/latex/hyperref/options.pdf
%{_texdir}/texmf-dist/doc/latex/hyperref/paper.pdf
%{_texdir}/texmf-dist/doc/latex/hyperref/slides.pdf


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
