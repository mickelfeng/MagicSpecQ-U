%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/prosper.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/prosper.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/prosper.source.tar.xz

Name: texlive-prosper
License: LPPL
Summary: LaTeX class for high quality slides
Version: %{tl_version}
Release: %{tl_noarch_release}.1.0h.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(PPRalcatel.sty)
Provides: tex(PPRalienglow.sty)
Provides: tex(PPRautumn.sty)
Provides: tex(PPRazure.sty)
Provides: tex(PPRblends.sty)
Provides: tex(PPRcapsules.sty)
Provides: tex(PPRcontemporain.sty)
Provides: tex(PPRcorners.sty)
Provides: tex(PPRdarkblue.sty)
Provides: tex(PPRdefault.sty)
Provides: tex(PPRframes.sty)
Provides: tex(PPRfyma.sty)
Provides: tex(PPRgyom.sty)
Provides: tex(PPRlignesbleues.sty)
Provides: tex(PPRmancini.sty)
Provides: tex(PPRnuancegris.sty)
Provides: tex(PPRprettybox.sty)
Provides: tex(PPRrico.sty)
Provides: tex(PPRserpaggi.sty)
Provides: tex(PPRthomasd.sty)
Provides: tex(PPRtroispoints.sty)
Provides: tex(PPRwhitecross.sty)
Provides: tex(PPRwinter.sty)
Provides: tex(PPRwj.sty)
Provides: tex(prosper.sty)
Requires: tex(amssymb.sty)
Requires: tex(pst-grad.sty)
Requires: tex(semhelv.sty)
Requires: tex(times.sty)
Requires: tex(palatino.sty)
Requires: tex(mathpazo.sty)
Requires: tex(pst-slpe.sty)
Requires: tex(multido.sty)
Requires: tex(ifthen.sty)
Requires: tex(fp.sty)
Requires: tex(graphicx.sty)
Requires: tex(hyperref.sty)
Provides: tetex-prosper = %{tl_version}
Obsoletes: tetex-prosper < %{tl_version}

%description
Prosper is a LaTeX class for writing transparencies. It is
written as an extension of the seminar class by Timothy Van
Zandt. Prosper offers a friendly environment for creating
slides for both presentations with an overhead projector and a
video projector. Slides prepared for a presentation with a
computer and a video projector may integrate animation effects,
incremental display, and so on. Various visual styles are
supported (including some that mimic PowerPoint) and others are
being contributed.

date: 2010-05-17 14:53:01 +0200

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
Summary: Documentation for prosper
Version: %{tl_version}
Release: %{tl_noarch_release}.1.0h.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for prosper


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
%{_texdir}/texmf-dist/tex/latex/prosper/PPRalcatel.sty
%{_texdir}/texmf-dist/tex/latex/prosper/PPRalienglow.sty
%{_texdir}/texmf-dist/tex/latex/prosper/PPRautumn.sty
%{_texdir}/texmf-dist/tex/latex/prosper/PPRazure.sty
%{_texdir}/texmf-dist/tex/latex/prosper/PPRblends.sty
%{_texdir}/texmf-dist/tex/latex/prosper/PPRcapsules.sty
%{_texdir}/texmf-dist/tex/latex/prosper/PPRcontemporain.sty
%{_texdir}/texmf-dist/tex/latex/prosper/PPRcorners.sty
%{_texdir}/texmf-dist/tex/latex/prosper/PPRdarkblue.sty
%{_texdir}/texmf-dist/tex/latex/prosper/PPRdefault.sty
%{_texdir}/texmf-dist/tex/latex/prosper/PPRframes.sty
%{_texdir}/texmf-dist/tex/latex/prosper/PPRfyma.sty
%{_texdir}/texmf-dist/tex/latex/prosper/PPRgyom.sty
%{_texdir}/texmf-dist/tex/latex/prosper/PPRlignesbleues.sty
%{_texdir}/texmf-dist/tex/latex/prosper/PPRmancini.sty
%{_texdir}/texmf-dist/tex/latex/prosper/PPRnuancegris.sty
%{_texdir}/texmf-dist/tex/latex/prosper/PPRprettybox.sty
%{_texdir}/texmf-dist/tex/latex/prosper/PPRrico.sty
%{_texdir}/texmf-dist/tex/latex/prosper/PPRserpaggi.sty
%{_texdir}/texmf-dist/tex/latex/prosper/PPRthomasd.sty
%{_texdir}/texmf-dist/tex/latex/prosper/PPRtroispoints.sty
%{_texdir}/texmf-dist/tex/latex/prosper/PPRwhitecross.sty
%{_texdir}/texmf-dist/tex/latex/prosper/PPRwinter.sty
%{_texdir}/texmf-dist/tex/latex/prosper/PPRwj.sty
%{_texdir}/texmf-dist/tex/latex/prosper/angleHG.ps
%{_texdir}/texmf-dist/tex/latex/prosper/arrow-glow.ps
%{_texdir}/texmf-dist/tex/latex/prosper/barre-rico.ps
%{_texdir}/texmf-dist/tex/latex/prosper/blue-inverted-arrow.ps
%{_texdir}/texmf-dist/tex/latex/prosper/boule-base.eps
%{_texdir}/texmf-dist/tex/latex/prosper/boulebleue-fondblanc.eps
%{_texdir}/texmf-dist/tex/latex/prosper/boulerouge-fondblanc.eps
%{_texdir}/texmf-dist/tex/latex/prosper/bouleverte-fondblanc.eps
%{_texdir}/texmf-dist/tex/latex/prosper/bullet-glow.ps
%{_texdir}/texmf-dist/tex/latex/prosper/compilation.eps
%{_texdir}/texmf-dist/tex/latex/prosper/degrade-base.eps
%{_texdir}/texmf-dist/tex/latex/prosper/degrade-blanc-bleu.eps
%{_texdir}/texmf-dist/tex/latex/prosper/green-bullet-on-blue-wc.ps
%{_texdir}/texmf-dist/tex/latex/prosper/green-bullet-on-blue.ps
%{_texdir}/texmf-dist/tex/latex/prosper/green-bullet-on-white.ps
%{_texdir}/texmf-dist/tex/latex/prosper/green-inverted-arrow.ps
%{_texdir}/texmf-dist/tex/latex/prosper/gyom.ps
%{_texdir}/texmf-dist/tex/latex/prosper/prosper-structure.eps
%{_texdir}/texmf-dist/tex/latex/prosper/prosper.cls
%{_texdir}/texmf-dist/tex/latex/prosper/red-bullet-on-blue-wc.ps
%{_texdir}/texmf-dist/tex/latex/prosper/red-bullet-on-blue.ps
%{_texdir}/texmf-dist/tex/latex/prosper/red-bullet-on-white.ps
%{_texdir}/texmf-dist/tex/latex/prosper/red-inverted-arrow.ps
%{_texdir}/texmf-dist/tex/latex/prosper/rico.ps
%{_texdir}/texmf-dist/tex/latex/prosper/rico_bullet1.ps
%{_texdir}/texmf-dist/tex/latex/prosper/rico_bullet2.ps
%{_texdir}/texmf-dist/tex/latex/prosper/rico_bullet3.ps
%{_texdir}/texmf-dist/tex/latex/prosper/rotation.ps
%{_texdir}/texmf-dist/tex/latex/prosper/rule-glow.ps
%{_texdir}/texmf-dist/tex/latex/prosper/yellow-bullet-on-blue-wc.ps
%{_texdir}/texmf-dist/tex/latex/prosper/yellow-bullet-on-blue.ps
%{_texdir}/texmf-dist/tex/latex/prosper/yellow-bullet-on-white.ps

%files doc
%defattr(-,root,root)
%doc lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/prosper/Example.tex
%{_texdir}/texmf-dist/doc/latex/prosper/ExampleAlienglow.tex
%{_texdir}/texmf-dist/doc/latex/prosper/ExampleAutumn.tex
%{_texdir}/texmf-dist/doc/latex/prosper/ExampleAzure.tex
%{_texdir}/texmf-dist/doc/latex/prosper/ExampleContemporain.tex
%{_texdir}/texmf-dist/doc/latex/prosper/ExampleDarkblue.tex
%{_texdir}/texmf-dist/doc/latex/prosper/ExampleFrames.tex
%{_texdir}/texmf-dist/doc/latex/prosper/ExampleLignesbleues.tex
%{_texdir}/texmf-dist/doc/latex/prosper/ExampleNuanceGris.tex
%{_texdir}/texmf-dist/doc/latex/prosper/ExampleTroisPoints.tex
%{_texdir}/texmf-dist/doc/latex/prosper/FAQ
%{_texdir}/texmf-dist/doc/latex/prosper/NEWS
%{_texdir}/texmf-dist/doc/latex/prosper/README
%{_texdir}/texmf-dist/doc/latex/prosper/green-bullet-on-blue-wc.gif
%{_texdir}/texmf-dist/doc/latex/prosper/green-bullet-on-blue.gif
%{_texdir}/texmf-dist/doc/latex/prosper/green-bullet-on-white.gif
%{_texdir}/texmf-dist/doc/latex/prosper/gyom.tex
%{_texdir}/texmf-dist/doc/latex/prosper/manifest.txt
%{_texdir}/texmf-dist/doc/latex/prosper/prosper-doc.pdf
%{_texdir}/texmf-dist/doc/latex/prosper/prosper-doc.tex
%{_texdir}/texmf-dist/doc/latex/prosper/prosper-template.jpg
%{_texdir}/texmf-dist/doc/latex/prosper/prosper-tour.pdf
%{_texdir}/texmf-dist/doc/latex/prosper/prosper-tour.tex
%{_texdir}/texmf-dist/doc/latex/prosper/red-bullet-on-blue-wc.gif
%{_texdir}/texmf-dist/doc/latex/prosper/red-bullet-on-blue.gif
%{_texdir}/texmf-dist/doc/latex/prosper/red-bullet-on-white.gif
%{_texdir}/texmf-dist/doc/latex/prosper/rico.tex
%{_texdir}/texmf-dist/doc/latex/prosper/rotation.tex
%{_texdir}/texmf-dist/doc/latex/prosper/yellow-bullet-on-blue-wc.gif
%{_texdir}/texmf-dist/doc/latex/prosper/yellow-bullet-on-blue.gif
%{_texdir}/texmf-dist/doc/latex/prosper/yellow-bullet-on-white.gif


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
