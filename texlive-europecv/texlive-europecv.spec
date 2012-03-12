%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/europecv.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/europecv.doc.tar.xz

Name: texlive-europecv
License: LPPL
Summary: Unofficial class for European curricula vitae
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(europecv.sty)
Requires: tex(totpages.sty)
Requires: tex(booktabs.sty)
Requires: tex(ucs.sty)
Requires: tex(inputenc.sty)
Requires: tex(array.sty)
Requires: tex(longtable.sty)
Requires: tex(fancyhdr.sty)

%description
The europecv class is an unofficial LaTeX implementation of the
standard model for curricula vitae (the "Europass CV") as
recommended by the European Commission. Although primarily
intended for users in the European Union, the class is flexible
enough to be used for any kind of curriculum vitae. The class
has localisations for all the official languages of the EU
(plus Catalan), as well as options permitting input in UTF-8
and koi8-r.

date: 2006-12-09 23:51:48 +0100

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
Summary: Documentation for europecv
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for europecv


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
%{_texdir}/texmf-dist/tex/latex/europecv/EuropeFlagBW.eps
%{_texdir}/texmf-dist/tex/latex/europecv/EuropeFlagBW.pdf
%{_texdir}/texmf-dist/tex/latex/europecv/EuropeFlagBlueCMYK.eps
%{_texdir}/texmf-dist/tex/latex/europecv/EuropeFlagBlueCMYK.pdf
%{_texdir}/texmf-dist/tex/latex/europecv/EuropeFlagCMYK.eps
%{_texdir}/texmf-dist/tex/latex/europecv/EuropeFlagCMYK.pdf
%{_texdir}/texmf-dist/tex/latex/europecv/EuropeFlagWB.eps
%{_texdir}/texmf-dist/tex/latex/europecv/EuropeFlagWB.pdf
%{_texdir}/texmf-dist/tex/latex/europecv/ecvbg.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecvca.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecvcs.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecvda.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecvde.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecven.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecves.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecvet.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecvfi.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecvfr.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecvgl.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecvgr.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecvhu.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecvis.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecvit.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecvlt.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecvlv.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecvmt.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecvnl.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecvno.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecvpl.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecvpt.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecvro.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecvsk.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecvsl.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecvsr.def
%{_texdir}/texmf-dist/tex/latex/europecv/ecvsv.def
%{_texdir}/texmf-dist/tex/latex/europecv/europasslogo.eps
%{_texdir}/texmf-dist/tex/latex/europecv/europasslogo.pdf
%{_texdir}/texmf-dist/tex/latex/europecv/europecv.cls

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/europecv/europecv.pdf
%{_texdir}/texmf-dist/doc/latex/europecv/europecv.tex
%{_texdir}/texmf-dist/doc/latex/europecv/examples/at.pdf
%{_texdir}/texmf-dist/doc/latex/europecv/examples/bulgarian-koi8-r.tex
%{_texdir}/texmf-dist/doc/latex/europecv/examples/bulgarian-utf8.tex
%{_texdir}/texmf-dist/doc/latex/europecv/examples/greek-utf8.pdf
%{_texdir}/texmf-dist/doc/latex/europecv/examples/greek-utf8.tex
%{_texdir}/texmf-dist/doc/latex/europecv/examples/maltese-maltese.tex
%{_texdir}/texmf-dist/doc/latex/europecv/examples/maltese-utf8.tex
%{_texdir}/texmf-dist/doc/latex/europecv/examples/minimal.pdf
%{_texdir}/texmf-dist/doc/latex/europecv/examples/minimal.tex
%{_texdir}/texmf-dist/doc/latex/europecv/templates/cv_template_de.pdf
%{_texdir}/texmf-dist/doc/latex/europecv/templates/cv_template_de.tex
%{_texdir}/texmf-dist/doc/latex/europecv/templates/cv_template_en.pdf
%{_texdir}/texmf-dist/doc/latex/europecv/templates/cv_template_en.tex
%{_texdir}/texmf-dist/doc/latex/europecv/templates/cv_template_it.pdf
%{_texdir}/texmf-dist/doc/latex/europecv/templates/cv_template_it.tex
%{_texdir}/texmf-dist/doc/latex/europecv/templates/cv_template_pl.pdf
%{_texdir}/texmf-dist/doc/latex/europecv/templates/cv_template_pl.tex
%{_texdir}/texmf-dist/doc/latex/europecv/templates/publications.bib


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
