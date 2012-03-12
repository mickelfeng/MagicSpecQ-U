%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/babel.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/babel.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/babel.source.tar.xz

Name: texlive-babel
License: LPPL
Summary: Multilingual support for Plain TeX or LaTeX
Version: %{tl_version}
Release: %{tl_noarch_release}.3.8l.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(UKenglish.sty)
Provides: tex(USenglish.sty)
Provides: tex(afrikaans.sty)
Provides: tex(albanian.sty)
Provides: tex(american.sty)
Provides: tex(athnum.sty)
Provides: tex(austrian.sty)
Provides: tex(babel.sty)
Provides: tex(bahasa.sty)
Provides: tex(bahasai.sty)
Provides: tex(bahasam.sty)
Provides: tex(basque.sty)
Provides: tex(breton.sty)
Provides: tex(british.sty)
Provides: tex(bulgarian.sty)
Provides: tex(catalan.sty)
Provides: tex(croatian.sty)
Provides: tex(czech.sty)
Provides: tex(danish.sty)
Provides: tex(dutch.sty)
Provides: tex(english.sty)
Provides: tex(esperanto.sty)
Provides: tex(estonian.sty)
Provides: tex(finnish.sty)
Provides: tex(francais.sty)
Provides: tex(frenchb.sty)
Provides: tex(galician.sty)
Provides: tex(germanb.sty)
Provides: tex(greek.sty)
Provides: tex(grmath.sty)
Provides: tex(grsymb.sty)
Provides: tex(hebcal.sty)
Provides: tex(hebfont.sty)
Provides: tex(hebrew.sty)
Provides: tex(hebrew_newcode.sty)
Provides: tex(hebrew_oldcode.sty)
Provides: tex(hebrew_p.sty)
Provides: tex(icelandic.sty)
Provides: tex(interlingua.sty)
Provides: tex(irish.sty)
Provides: tex(italian.sty)
Provides: tex(kurmanji.sty)
Provides: tex(latin.sty)
Provides: tex(lsorbian.sty)
Provides: tex(magyar.sty)
Provides: tex(naustrian.sty)
Provides: tex(ngermanb.sty)
Provides: tex(norsk.sty)
Provides: tex(polish.sty)
Provides: tex(portuges.sty)
Provides: tex(romanian.sty)
Provides: tex(romanidx.sty)
Provides: tex(russianb.sty)
Provides: tex(samin.sty)
Provides: tex(scottish.sty)
Provides: tex(serbian.sty)
Provides: tex(slovak.sty)
Provides: tex(slovene.sty)
Provides: tex(spanish.sty)
Provides: tex(swedish.sty)
Provides: tex(turkish.sty)
Provides: tex(ukraineb.sty)
Provides: tex(usorbian.sty)
Provides: tex(welsh.sty)
Requires: tex(scalefnt.sty)
Requires: tex(keyval.sty)
Requires: tex(inputenc.sty)

%description
The package manages culturally-determined typographical (and
other) rules, and hyphenation patterns for a wide range of
languages. A document may select a single language to be
supported, or it may select several, and the document may then
switch from one language to another in a variety of ways.

date: 2009-09-24 15:05:48 +0200

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
Summary: Documentation for babel
Version: %{tl_version}
Release: %{tl_noarch_release}.3.8l.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for babel


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
%{_texdir}/texmf-dist/makeindex/babel/bbglo.ist
%{_texdir}/texmf-dist/makeindex/babel/bbind.ist
%{_texdir}/texmf-dist/tex/generic/babel/8859-8.def
%{_texdir}/texmf-dist/tex/generic/babel/UKenglish.sty
%{_texdir}/texmf-dist/tex/generic/babel/USenglish.sty
%{_texdir}/texmf-dist/tex/generic/babel/afrikaans.sty
%{_texdir}/texmf-dist/tex/generic/babel/albanian.ldf
%{_texdir}/texmf-dist/tex/generic/babel/albanian.sty
%{_texdir}/texmf-dist/tex/generic/babel/american.sty
%{_texdir}/texmf-dist/tex/generic/babel/athnum.sty
%{_texdir}/texmf-dist/tex/generic/babel/austrian.sty
%{_texdir}/texmf-dist/tex/generic/babel/babel.def
%{_texdir}/texmf-dist/tex/generic/babel/babel.sty
%{_texdir}/texmf-dist/tex/generic/babel/bahasa.sty
%{_texdir}/texmf-dist/tex/generic/babel/bahasai.ldf
%{_texdir}/texmf-dist/tex/generic/babel/bahasam.ldf
%{_texdir}/texmf-dist/tex/generic/babel/bahasam.sty
%{_texdir}/texmf-dist/tex/generic/babel/basque.ldf
%{_texdir}/texmf-dist/tex/generic/babel/basque.sty
%{_texdir}/texmf-dist/tex/generic/babel/blplain.tex
%{_texdir}/texmf-dist/tex/generic/babel/bplain.tex
%{_texdir}/texmf-dist/tex/generic/babel/breton.ldf
%{_texdir}/texmf-dist/tex/generic/babel/breton.sty
%{_texdir}/texmf-dist/tex/generic/babel/british.sty
%{_texdir}/texmf-dist/tex/generic/babel/bulgarian.ldf
%{_texdir}/texmf-dist/tex/generic/babel/bulgarian.sty
%{_texdir}/texmf-dist/tex/generic/babel/catalan.ldf
%{_texdir}/texmf-dist/tex/generic/babel/catalan.sty
%{_texdir}/texmf-dist/tex/generic/babel/cp1255.def
%{_texdir}/texmf-dist/tex/generic/babel/cp862.def
%{_texdir}/texmf-dist/tex/generic/babel/croatian.ldf
%{_texdir}/texmf-dist/tex/generic/babel/croatian.sty
%{_texdir}/texmf-dist/tex/generic/babel/czech.ldf
%{_texdir}/texmf-dist/tex/generic/babel/czech.sty
%{_texdir}/texmf-dist/tex/generic/babel/danish.ldf
%{_texdir}/texmf-dist/tex/generic/babel/danish.sty
%{_texdir}/texmf-dist/tex/generic/babel/dutch.ldf
%{_texdir}/texmf-dist/tex/generic/babel/dutch.sty
%{_texdir}/texmf-dist/tex/generic/babel/english.ldf
%{_texdir}/texmf-dist/tex/generic/babel/english.sty
%{_texdir}/texmf-dist/tex/generic/babel/esperanto.ldf
%{_texdir}/texmf-dist/tex/generic/babel/esperanto.sty
%{_texdir}/texmf-dist/tex/generic/babel/estonian.ldf
%{_texdir}/texmf-dist/tex/generic/babel/estonian.sty
%{_texdir}/texmf-dist/tex/generic/babel/finnish.ldf
%{_texdir}/texmf-dist/tex/generic/babel/finnish.sty
%{_texdir}/texmf-dist/tex/generic/babel/francais.sty
%{_texdir}/texmf-dist/tex/generic/babel/frenchb.cfg
%{_texdir}/texmf-dist/tex/generic/babel/frenchb.ldf
%{_texdir}/texmf-dist/tex/generic/babel/galician.ldf
%{_texdir}/texmf-dist/tex/generic/babel/galician.sty
%{_texdir}/texmf-dist/tex/generic/babel/germanb.ldf
%{_texdir}/texmf-dist/tex/generic/babel/germanb.sty
%{_texdir}/texmf-dist/tex/generic/babel/glbst.tex
%{_texdir}/texmf-dist/tex/generic/babel/glromidx.tex
%{_texdir}/texmf-dist/tex/generic/babel/greek.ldf
%{_texdir}/texmf-dist/tex/generic/babel/greek.sty
%{_texdir}/texmf-dist/tex/generic/babel/grmath.sty
%{_texdir}/texmf-dist/tex/generic/babel/grsymb.sty
%{_texdir}/texmf-dist/tex/generic/babel/he8OmegaHebrew.fd
%{_texdir}/texmf-dist/tex/generic/babel/he8aharoni.fd
%{_texdir}/texmf-dist/tex/generic/babel/he8cmr.fd
%{_texdir}/texmf-dist/tex/generic/babel/he8cmss.fd
%{_texdir}/texmf-dist/tex/generic/babel/he8cmtt.fd
%{_texdir}/texmf-dist/tex/generic/babel/he8david.fd
%{_texdir}/texmf-dist/tex/generic/babel/he8drugulin.fd
%{_texdir}/texmf-dist/tex/generic/babel/he8enc.def
%{_texdir}/texmf-dist/tex/generic/babel/he8frankruehl.fd
%{_texdir}/texmf-dist/tex/generic/babel/he8miriam.fd
%{_texdir}/texmf-dist/tex/generic/babel/he8nachlieli.fd
%{_texdir}/texmf-dist/tex/generic/babel/he8yad.fd
%{_texdir}/texmf-dist/tex/generic/babel/hebcal.sty
%{_texdir}/texmf-dist/tex/generic/babel/hebfont.sty
%{_texdir}/texmf-dist/tex/generic/babel/hebrew.ldf
%{_texdir}/texmf-dist/tex/generic/babel/hebrew.sty
%{_texdir}/texmf-dist/tex/generic/babel/hebrew_newcode.sty
%{_texdir}/texmf-dist/tex/generic/babel/hebrew_oldcode.sty
%{_texdir}/texmf-dist/tex/generic/babel/hebrew_p.sty
%{_texdir}/texmf-dist/tex/generic/babel/hyphen.cfg
%{_texdir}/texmf-dist/tex/generic/babel/icelandic.ldf
%{_texdir}/texmf-dist/tex/generic/babel/icelandic.sty
%{_texdir}/texmf-dist/tex/generic/babel/interlingua.ldf
%{_texdir}/texmf-dist/tex/generic/babel/interlingua.sty
%{_texdir}/texmf-dist/tex/generic/babel/irish.ldf
%{_texdir}/texmf-dist/tex/generic/babel/irish.sty
%{_texdir}/texmf-dist/tex/generic/babel/italian.ldf
%{_texdir}/texmf-dist/tex/generic/babel/italian.sty
%{_texdir}/texmf-dist/tex/generic/babel/kurmanji.ldf
%{_texdir}/texmf-dist/tex/generic/babel/latin.ldf
%{_texdir}/texmf-dist/tex/generic/babel/latin.sty
%{_texdir}/texmf-dist/tex/generic/babel/lgrcmr.fd
%{_texdir}/texmf-dist/tex/generic/babel/lgrcmro.fd
%{_texdir}/texmf-dist/tex/generic/babel/lgrcmss.fd
%{_texdir}/texmf-dist/tex/generic/babel/lgrcmtt.fd
%{_texdir}/texmf-dist/tex/generic/babel/lgrenc.def
%{_texdir}/texmf-dist/tex/generic/babel/lgrlcmss.fd
%{_texdir}/texmf-dist/tex/generic/babel/lgrlcmtt.fd
%{_texdir}/texmf-dist/tex/generic/babel/lgrlmr.fd
%{_texdir}/texmf-dist/tex/generic/babel/lgrlmro.fd
%{_texdir}/texmf-dist/tex/generic/babel/lgrlmss.fd
%{_texdir}/texmf-dist/tex/generic/babel/lgrlmtt.fd
%{_texdir}/texmf-dist/tex/generic/babel/lheclas.fd
%{_texdir}/texmf-dist/tex/generic/babel/lhecmr.fd
%{_texdir}/texmf-dist/tex/generic/babel/lhecmss.fd
%{_texdir}/texmf-dist/tex/generic/babel/lhecmtt.fd
%{_texdir}/texmf-dist/tex/generic/babel/lhecrml.fd
%{_texdir}/texmf-dist/tex/generic/babel/lheenc.def
%{_texdir}/texmf-dist/tex/generic/babel/lhefr.fd
%{_texdir}/texmf-dist/tex/generic/babel/lheredis.fd
%{_texdir}/texmf-dist/tex/generic/babel/lheshold.fd
%{_texdir}/texmf-dist/tex/generic/babel/lheshscr.fd
%{_texdir}/texmf-dist/tex/generic/babel/lheshstk.fd
%{_texdir}/texmf-dist/tex/generic/babel/lsorbian.ldf
%{_texdir}/texmf-dist/tex/generic/babel/lsorbian.sty
%{_texdir}/texmf-dist/tex/generic/babel/magyar.ldf
%{_texdir}/texmf-dist/tex/generic/babel/magyar.sty
%{_texdir}/texmf-dist/tex/generic/babel/naustrian.sty
%{_texdir}/texmf-dist/tex/generic/babel/ngermanb.ldf
%{_texdir}/texmf-dist/tex/generic/babel/ngermanb.sty
%{_texdir}/texmf-dist/tex/generic/babel/norsk.ldf
%{_texdir}/texmf-dist/tex/generic/babel/norsk.sty
%{_texdir}/texmf-dist/tex/generic/babel/plain.def
%{_texdir}/texmf-dist/tex/generic/babel/polish.ldf
%{_texdir}/texmf-dist/tex/generic/babel/polish.sty
%{_texdir}/texmf-dist/tex/generic/babel/portuges.ldf
%{_texdir}/texmf-dist/tex/generic/babel/portuges.sty
%{_texdir}/texmf-dist/tex/generic/babel/rlbabel.def
%{_texdir}/texmf-dist/tex/generic/babel/romanian.ldf
%{_texdir}/texmf-dist/tex/generic/babel/romanian.sty
%{_texdir}/texmf-dist/tex/generic/babel/romanidx.sty
%{_texdir}/texmf-dist/tex/generic/babel/russianb.ldf
%{_texdir}/texmf-dist/tex/generic/babel/russianb.sty
%{_texdir}/texmf-dist/tex/generic/babel/samin.ldf
%{_texdir}/texmf-dist/tex/generic/babel/samin.sty
%{_texdir}/texmf-dist/tex/generic/babel/scottish.ldf
%{_texdir}/texmf-dist/tex/generic/babel/scottish.sty
%{_texdir}/texmf-dist/tex/generic/babel/serbian.ldf
%{_texdir}/texmf-dist/tex/generic/babel/serbian.sty
%{_texdir}/texmf-dist/tex/generic/babel/si960.def
%{_texdir}/texmf-dist/tex/generic/babel/slovak.ldf
%{_texdir}/texmf-dist/tex/generic/babel/slovak.sty
%{_texdir}/texmf-dist/tex/generic/babel/slovene.ldf
%{_texdir}/texmf-dist/tex/generic/babel/slovene.sty
%{_texdir}/texmf-dist/tex/generic/babel/spanish.ldf
%{_texdir}/texmf-dist/tex/generic/babel/spanish.sty
%{_texdir}/texmf-dist/tex/generic/babel/swedish.ldf
%{_texdir}/texmf-dist/tex/generic/babel/swedish.sty
%{_texdir}/texmf-dist/tex/generic/babel/switch.def
%{_texdir}/texmf-dist/tex/generic/babel/turkish.ldf
%{_texdir}/texmf-dist/tex/generic/babel/turkish.sty
%{_texdir}/texmf-dist/tex/generic/babel/ukraineb.ldf
%{_texdir}/texmf-dist/tex/generic/babel/ukraineb.sty
%{_texdir}/texmf-dist/tex/generic/babel/usorbian.ldf
%{_texdir}/texmf-dist/tex/generic/babel/usorbian.sty
%{_texdir}/texmf-dist/tex/generic/babel/welsh.ldf
%{_texdir}/texmf-dist/tex/generic/babel/welsh.sty

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/generic/babel/00readme.heb
%{_texdir}/texmf-dist/doc/generic/babel/00readme.txt
%{_texdir}/texmf-dist/doc/generic/babel/GreekFonts.txt
%{_texdir}/texmf-dist/doc/generic/babel/announce.txt
%{_texdir}/texmf-dist/doc/generic/babel/athnum.pdf
%{_texdir}/texmf-dist/doc/generic/babel/babel.pdf
%{_texdir}/texmf-dist/doc/generic/babel/bbcompat.pdf
%{_texdir}/texmf-dist/doc/generic/babel/bbidxglo.pdf
%{_texdir}/texmf-dist/doc/generic/babel/bugs.txt
%{_texdir}/texmf-dist/doc/generic/babel/changes.txt
%{_texdir}/texmf-dist/doc/generic/babel/fixes.txt
%{_texdir}/texmf-dist/doc/generic/babel/greek-fdd.pdf
%{_texdir}/texmf-dist/doc/generic/babel/greek-usage.pdf
%{_texdir}/texmf-dist/doc/generic/babel/grmath.pdf
%{_texdir}/texmf-dist/doc/generic/babel/grsymb.pdf
%{_texdir}/texmf-dist/doc/generic/babel/howtoget.txt
%{_texdir}/texmf-dist/doc/generic/babel/install.OzTeX-4
%{_texdir}/texmf-dist/doc/generic/babel/install.OzTeX-pre4
%{_texdir}/texmf-dist/doc/generic/babel/install.txt
%{_texdir}/texmf-dist/doc/generic/babel/language.dat
%{_texdir}/texmf-dist/doc/generic/babel/language.skeleton
%{_texdir}/texmf-dist/doc/generic/babel/legal.bbl
%{_texdir}/texmf-dist/doc/generic/babel/manifest.bbl
%{_texdir}/texmf-dist/doc/generic/babel/tb1202.pdf
%{_texdir}/texmf-dist/doc/generic/babel/tb1401.pdf
%{_texdir}/texmf-dist/doc/generic/babel/tb1604.pdf
%{_texdir}/texmf-dist/doc/generic/babel/todo.txt


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
