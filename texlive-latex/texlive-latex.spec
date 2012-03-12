%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/latex.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/latex.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/latex.source.tar.xz

Name: texlive-latex
License: LPPL
Summary: A TeX macro package that defines LaTeX
Version: %{tl_version}
Release: %{tl_noarch_release}.svn16172%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-luatex = %{tl_version}
Requires: texlive-pdftex = %{tl_version}
Requires: texlive-latexconfig = %{tl_version}
Requires: texlive-latex-fonts = %{tl_version}
Provides: tex(alltt.sty)
Provides: tex(article.sty)
Provides: tex(bezier.sty)
Provides: tex(book.sty)
Provides: tex(doc.sty)
Provides: tex(exscale.sty)
Provides: tex(fix-cm.sty)
Provides: tex(fixltx2e.sty)
Provides: tex(flafter.sty)
Provides: tex(fleqn.sty)
Provides: tex(fontenc.sty)
Provides: tex(graphpap.sty)
Provides: tex(ifthen.sty)
Provides: tex(inputenc.sty)
Provides: tex(latexsym.sty)
Provides: tex(leqno.sty)
Provides: tex(letter.sty)
Provides: tex(ltnews.sty)
Provides: tex(ltxdoc.sty)
Provides: tex(ltxguide.sty)
Provides: tex(makeidx.sty)
Provides: tex(minimal.sty)
Provides: tex(newlfont.sty)
Provides: tex(oldlfont.sty)
Provides: tex(openbib.sty)
Provides: tex(proc.sty)
Provides: tex(report.sty)
Provides: tex(shortvrb.sty)
Provides: tex(showidx.sty)
Provides: tex(slides.sty)
Provides: tex(syntonly.sty)
Provides: tex(t1enc.sty)
Provides: tex(textcomp.sty)
Provides: tex(tracefnt.sty)
Requires: tex(multicol.sty)
Requires: tex(url.sty)
Requires: tex(hyperref.sty)
Provides: tetex-latex = 3.1-99, texlive-latex = %{tl_version}, texlive-texmf-latex = %{tl_version}
Obsoletes: tetex-latex < 3.1-99, texlive-latex < %{tl_version}, texlive-texmf-latex < %{tl_version}

%description
LaTeX is a widely-used macro package for TeX, providing many
basic document formating commands extended by a wide range of
packages. It is a development of Leslie Lamport's original
LaTeX 2.09, and superseded the older system in June 1994. The
basic distribution is catalogued separately, at latex-base;
apart from a large set of contributed packages and third-party
documentation (elsewhere on the archive), the distribution
includes: - a bunch of required packages, which LaTeX authors
are "entitled to assume" will be present on any system running
LaTeX; and - a minimal set of documentation detailing
differences from the 'old' version of LaTeX in the areas of
user commands, font selection and control, class and package
writing, font encodings, configuration options and modification
of LaTeX. For downloading details, see the linked catalogue
entries above.

date: 2009-10-10 00:35:28 +0200

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
Summary: Documentation for latex
Version: %{tl_version}
Release: %{tl_noarch_release}.svn16172%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch
Requires: texlive-luatex-doc
Requires: texlive-pdftex-doc

%description doc
Documentation for latex


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
%{_texdir}/texmf-dist/makeindex/latex/gglo.ist
%{_texdir}/texmf-dist/makeindex/latex/gind.ist
%{_texdir}/texmf-dist/tex/latex/base/alltt.sty
%{_texdir}/texmf-dist/tex/latex/base/ansinew.def
%{_texdir}/texmf-dist/tex/latex/base/applemac.def
%{_texdir}/texmf-dist/tex/latex/base/article.cls
%{_texdir}/texmf-dist/tex/latex/base/article.sty
%{_texdir}/texmf-dist/tex/latex/base/ascii.def
%{_texdir}/texmf-dist/tex/latex/base/bezier.sty
%{_texdir}/texmf-dist/tex/latex/base/bk10.clo
%{_texdir}/texmf-dist/tex/latex/base/bk11.clo
%{_texdir}/texmf-dist/tex/latex/base/bk12.clo
%{_texdir}/texmf-dist/tex/latex/base/book.cls
%{_texdir}/texmf-dist/tex/latex/base/book.sty
%{_texdir}/texmf-dist/tex/latex/base/cp1250.def
%{_texdir}/texmf-dist/tex/latex/base/cp1252.def
%{_texdir}/texmf-dist/tex/latex/base/cp1257.def
%{_texdir}/texmf-dist/tex/latex/base/cp437.def
%{_texdir}/texmf-dist/tex/latex/base/cp437de.def
%{_texdir}/texmf-dist/tex/latex/base/cp850.def
%{_texdir}/texmf-dist/tex/latex/base/cp852.def
%{_texdir}/texmf-dist/tex/latex/base/cp858.def
%{_texdir}/texmf-dist/tex/latex/base/cp865.def
%{_texdir}/texmf-dist/tex/latex/base/decmulti.def
%{_texdir}/texmf-dist/tex/latex/base/doc.sty
%{_texdir}/texmf-dist/tex/latex/base/docstrip.tex
%{_texdir}/texmf-dist/tex/latex/base/exscale.sty
%{_texdir}/texmf-dist/tex/latex/base/fix-cm.sty
%{_texdir}/texmf-dist/tex/latex/base/fixltx2e.sty
%{_texdir}/texmf-dist/tex/latex/base/flafter.sty
%{_texdir}/texmf-dist/tex/latex/base/fleqn.clo
%{_texdir}/texmf-dist/tex/latex/base/fleqn.sty
%{_texdir}/texmf-dist/tex/latex/base/fontenc.sty
%{_texdir}/texmf-dist/tex/latex/base/fontmath.cfg
%{_texdir}/texmf-dist/tex/latex/base/fontmath.ltx
%{_texdir}/texmf-dist/tex/latex/base/fonttext.cfg
%{_texdir}/texmf-dist/tex/latex/base/fonttext.ltx
%{_texdir}/texmf-dist/tex/latex/base/graphpap.sty
%{_texdir}/texmf-dist/tex/latex/base/hyphen.ltx
%{_texdir}/texmf-dist/tex/latex/base/idx.tex
%{_texdir}/texmf-dist/tex/latex/base/ifthen.sty
%{_texdir}/texmf-dist/tex/latex/base/inputenc.sty
%{_texdir}/texmf-dist/tex/latex/base/lablst.tex
%{_texdir}/texmf-dist/tex/latex/base/latex.ltx
%{_texdir}/texmf-dist/tex/latex/base/latex209.def
%{_texdir}/texmf-dist/tex/latex/base/latexbug.tex
%{_texdir}/texmf-dist/tex/latex/base/latexsym.sty
%{_texdir}/texmf-dist/tex/latex/base/latin1.def
%{_texdir}/texmf-dist/tex/latex/base/latin10.def
%{_texdir}/texmf-dist/tex/latex/base/latin2.def
%{_texdir}/texmf-dist/tex/latex/base/latin3.def
%{_texdir}/texmf-dist/tex/latex/base/latin4.def
%{_texdir}/texmf-dist/tex/latex/base/latin5.def
%{_texdir}/texmf-dist/tex/latex/base/latin9.def
%{_texdir}/texmf-dist/tex/latex/base/lcyenc.dfu
%{_texdir}/texmf-dist/tex/latex/base/leqno.clo
%{_texdir}/texmf-dist/tex/latex/base/leqno.sty
%{_texdir}/texmf-dist/tex/latex/base/letter.cls
%{_texdir}/texmf-dist/tex/latex/base/letter.sty
%{_texdir}/texmf-dist/tex/latex/base/lppl.tex
%{_texdir}/texmf-dist/tex/latex/base/ltnews.cls
%{_texdir}/texmf-dist/tex/latex/base/ltpatch.ltx
%{_texdir}/texmf-dist/tex/latex/base/ltxcheck.tex
%{_texdir}/texmf-dist/tex/latex/base/ltxdoc.cls
%{_texdir}/texmf-dist/tex/latex/base/ltxguide.cls
%{_texdir}/texmf-dist/tex/latex/base/ly1enc.dfu
%{_texdir}/texmf-dist/tex/latex/base/macce.def
%{_texdir}/texmf-dist/tex/latex/base/makeidx.sty
%{_texdir}/texmf-dist/tex/latex/base/minimal.cls
%{_texdir}/texmf-dist/tex/latex/base/newlfont.sty
%{_texdir}/texmf-dist/tex/latex/base/next.def
%{_texdir}/texmf-dist/tex/latex/base/nfssfont.tex
%{_texdir}/texmf-dist/tex/latex/base/oldlfont.sty
%{_texdir}/texmf-dist/tex/latex/base/omlcmm.fd
%{_texdir}/texmf-dist/tex/latex/base/omlcmr.fd
%{_texdir}/texmf-dist/tex/latex/base/omlenc.def
%{_texdir}/texmf-dist/tex/latex/base/omllcmm.fd
%{_texdir}/texmf-dist/tex/latex/base/omscmr.fd
%{_texdir}/texmf-dist/tex/latex/base/omscmsy.fd
%{_texdir}/texmf-dist/tex/latex/base/omsenc.def
%{_texdir}/texmf-dist/tex/latex/base/omsenc.dfu
%{_texdir}/texmf-dist/tex/latex/base/omslcmsy.fd
%{_texdir}/texmf-dist/tex/latex/base/omxcmex.fd
%{_texdir}/texmf-dist/tex/latex/base/omxlcmex.fd
%{_texdir}/texmf-dist/tex/latex/base/openbib.sty
%{_texdir}/texmf-dist/tex/latex/base/ot1cmdh.fd
%{_texdir}/texmf-dist/tex/latex/base/ot1cmfib.fd
%{_texdir}/texmf-dist/tex/latex/base/ot1cmfr.fd
%{_texdir}/texmf-dist/tex/latex/base/ot1cmr.fd
%{_texdir}/texmf-dist/tex/latex/base/ot1cmss.fd
%{_texdir}/texmf-dist/tex/latex/base/ot1cmtt.fd
%{_texdir}/texmf-dist/tex/latex/base/ot1cmvtt.fd
%{_texdir}/texmf-dist/tex/latex/base/ot1enc.def
%{_texdir}/texmf-dist/tex/latex/base/ot1enc.dfu
%{_texdir}/texmf-dist/tex/latex/base/ot1lcmss.fd
%{_texdir}/texmf-dist/tex/latex/base/ot1lcmtt.fd
%{_texdir}/texmf-dist/tex/latex/base/ot2enc.dfu
%{_texdir}/texmf-dist/tex/latex/base/ot4enc.def
%{_texdir}/texmf-dist/tex/latex/base/preload.cfg
%{_texdir}/texmf-dist/tex/latex/base/preload.ltx
%{_texdir}/texmf-dist/tex/latex/base/proc.cls
%{_texdir}/texmf-dist/tex/latex/base/proc.sty
%{_texdir}/texmf-dist/tex/latex/base/report.cls
%{_texdir}/texmf-dist/tex/latex/base/report.sty
%{_texdir}/texmf-dist/tex/latex/base/sample2e.tex
%{_texdir}/texmf-dist/tex/latex/base/sfonts.def
%{_texdir}/texmf-dist/tex/latex/base/shortvrb.sty
%{_texdir}/texmf-dist/tex/latex/base/showidx.sty
%{_texdir}/texmf-dist/tex/latex/base/size10.clo
%{_texdir}/texmf-dist/tex/latex/base/size11.clo
%{_texdir}/texmf-dist/tex/latex/base/size12.clo
%{_texdir}/texmf-dist/tex/latex/base/slides.cls
%{_texdir}/texmf-dist/tex/latex/base/slides.def
%{_texdir}/texmf-dist/tex/latex/base/slides.sty
%{_texdir}/texmf-dist/tex/latex/base/small2e.tex
%{_texdir}/texmf-dist/tex/latex/base/syntonly.sty
%{_texdir}/texmf-dist/tex/latex/base/t1cmdh.fd
%{_texdir}/texmf-dist/tex/latex/base/t1cmfib.fd
%{_texdir}/texmf-dist/tex/latex/base/t1cmfr.fd
%{_texdir}/texmf-dist/tex/latex/base/t1cmr.fd
%{_texdir}/texmf-dist/tex/latex/base/t1cmss.fd
%{_texdir}/texmf-dist/tex/latex/base/t1cmtt.fd
%{_texdir}/texmf-dist/tex/latex/base/t1cmvtt.fd
%{_texdir}/texmf-dist/tex/latex/base/t1enc.def
%{_texdir}/texmf-dist/tex/latex/base/t1enc.dfu
%{_texdir}/texmf-dist/tex/latex/base/t1enc.sty
%{_texdir}/texmf-dist/tex/latex/base/t1lcmss.fd
%{_texdir}/texmf-dist/tex/latex/base/t1lcmtt.fd
%{_texdir}/texmf-dist/tex/latex/base/t2aenc.dfu
%{_texdir}/texmf-dist/tex/latex/base/t2benc.dfu
%{_texdir}/texmf-dist/tex/latex/base/t2cenc.dfu
%{_texdir}/texmf-dist/tex/latex/base/testpage.tex
%{_texdir}/texmf-dist/tex/latex/base/texsys.cfg
%{_texdir}/texmf-dist/tex/latex/base/textcomp.sty
%{_texdir}/texmf-dist/tex/latex/base/tracefnt.sty
%{_texdir}/texmf-dist/tex/latex/base/ts1cmr.fd
%{_texdir}/texmf-dist/tex/latex/base/ts1cmss.fd
%{_texdir}/texmf-dist/tex/latex/base/ts1cmtt.fd
%{_texdir}/texmf-dist/tex/latex/base/ts1cmvtt.fd
%{_texdir}/texmf-dist/tex/latex/base/ts1enc.def
%{_texdir}/texmf-dist/tex/latex/base/ts1enc.dfu
%{_texdir}/texmf-dist/tex/latex/base/ucmr.fd
%{_texdir}/texmf-dist/tex/latex/base/ucmss.fd
%{_texdir}/texmf-dist/tex/latex/base/ucmtt.fd
%{_texdir}/texmf-dist/tex/latex/base/ulasy.fd
%{_texdir}/texmf-dist/tex/latex/base/ullasy.fd
%{_texdir}/texmf-dist/tex/latex/base/utf8-test.tex
%{_texdir}/texmf-dist/tex/latex/base/utf8.def
%{_texdir}/texmf-dist/tex/latex/base/utf8enc.dfu
%{_texdir}/texmf-dist/tex/latex/base/utf8test.tex
%{_texdir}/texmf-dist/tex/latex/base/x2enc.dfu

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/base/00readme.txt
%{_texdir}/texmf-dist/doc/latex/base/alltt.pdf
%{_texdir}/texmf-dist/doc/latex/base/autoload.txt
%{_texdir}/texmf-dist/doc/latex/base/bugs.txt
%{_texdir}/texmf-dist/doc/latex/base/cfgguide.pdf
%{_texdir}/texmf-dist/doc/latex/base/changes.txt
%{_texdir}/texmf-dist/doc/latex/base/classes.pdf
%{_texdir}/texmf-dist/doc/latex/base/clsguide.pdf
%{_texdir}/texmf-dist/doc/latex/base/cmfonts.pdf
%{_texdir}/texmf-dist/doc/latex/base/cyrguide.pdf
%{_texdir}/texmf-dist/doc/latex/base/doc.pdf
%{_texdir}/texmf-dist/doc/latex/base/docstrip.pdf
%{_texdir}/texmf-dist/doc/latex/base/encguide.pdf
%{_texdir}/texmf-dist/doc/latex/base/exscale.pdf
%{_texdir}/texmf-dist/doc/latex/base/fixltx2e.pdf
%{_texdir}/texmf-dist/doc/latex/base/fntguide.pdf
%{_texdir}/texmf-dist/doc/latex/base/graphpap.pdf
%{_texdir}/texmf-dist/doc/latex/base/ifthen.pdf
%{_texdir}/texmf-dist/doc/latex/base/inputenc.pdf
%{_texdir}/texmf-dist/doc/latex/base/latex209.pdf
%{_texdir}/texmf-dist/doc/latex/base/latexsym.pdf
%{_texdir}/texmf-dist/doc/latex/base/lb2.pdf
%{_texdir}/texmf-dist/doc/latex/base/legal.txt
%{_texdir}/texmf-dist/doc/latex/base/letter.pdf
%{_texdir}/texmf-dist/doc/latex/base/lgc2.pdf
%{_texdir}/texmf-dist/doc/latex/base/lppl-1-0.txt
%{_texdir}/texmf-dist/doc/latex/base/lppl-1-1.txt
%{_texdir}/texmf-dist/doc/latex/base/lppl-1-2.txt
%{_texdir}/texmf-dist/doc/latex/base/lppl.pdf
%{_texdir}/texmf-dist/doc/latex/base/lppl.txt
%{_texdir}/texmf-dist/doc/latex/base/ltnews.pdf
%{_texdir}/texmf-dist/doc/latex/base/ltx3info.pdf
%{_texdir}/texmf-dist/doc/latex/base/ltxcheck.pdf
%{_texdir}/texmf-dist/doc/latex/base/ltxdoc.pdf
%{_texdir}/texmf-dist/doc/latex/base/makeindx.pdf
%{_texdir}/texmf-dist/doc/latex/base/manifest.txt
%{_texdir}/texmf-dist/doc/latex/base/manual.pdf
%{_texdir}/texmf-dist/doc/latex/base/modguide.pdf
%{_texdir}/texmf-dist/doc/latex/base/newlfont.pdf
%{_texdir}/texmf-dist/doc/latex/base/oldlfont.pdf
%{_texdir}/texmf-dist/doc/latex/base/patches.txt
%{_texdir}/texmf-dist/doc/latex/base/proc.pdf
%{_texdir}/texmf-dist/doc/latex/base/slides.pdf
%{_texdir}/texmf-dist/doc/latex/base/slifonts.pdf
%{_texdir}/texmf-dist/doc/latex/base/source2e.pdf
%{_texdir}/texmf-dist/doc/latex/base/syntonly.pdf
%{_texdir}/texmf-dist/doc/latex/base/tex2.txt
%{_texdir}/texmf-dist/doc/latex/base/texpert.txt
%{_texdir}/texmf-dist/doc/latex/base/tlc2.pdf
%{_texdir}/texmf-dist/doc/latex/base/usrguide.pdf
%{_texdir}/texmf-dist/doc/latex/base/utf8ienc.pdf
%{_texdir}/texmf-dist/doc/latex/base/webcomp.pdf


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
