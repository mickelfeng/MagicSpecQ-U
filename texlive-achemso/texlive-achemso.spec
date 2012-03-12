%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/achemso.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/achemso.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/achemso.source.tar.xz

Name: texlive-achemso
License: LPPL
Summary: Support for American Chemical Society journal submissions
Version: %{tl_version}
Release: %{tl_noarch_release}.3.5.svn19190%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(achemso.sty)
Provides: tex(natmove.sty)
Requires: tex(xkeyval.sty)
Requires: tex(mciteplus.sty)
Requires: tex(fontenc.sty)
Requires: tex(geometry.sty)
Requires: tex(helvet.sty)
Requires: tex(caption.sty)
Requires: tex(courier.sty)
Requires: tex(float.sty)
Requires: tex(graphicx.sty)
Requires: tex(mathptmx.sty)
Requires: tex(setspace.sty)
Requires: tex(url.sty)
Requires: tex(cleveref.sty)
Requires: tex(natbib.sty)

%description
The bundle provides the official macros and BibTeX style for
submission to the journals of the American Chemical Society.
Also provided is a BibTeX style file to be used for
bibliography database listings. The natmove package, which
moves citations relative to punctuation, is distributed as part
of the bundle.

date: 2010-06-27 17:16:06 +0200

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
Summary: Documentation for achemso
Version: %{tl_version}
Release: %{tl_noarch_release}.3.5.svn19190%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for achemso


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/lppl1.3.txt lppl1.3.txt
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
%doc lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bst/achemso/achemso.bst
%{_texdir}/texmf-dist/bibtex/bst/achemso/biochem.bst
%{_texdir}/texmf-dist/tex/latex/achemso/achemso.cls
%{_texdir}/texmf-dist/tex/latex/achemso/achemso.sty
%{_texdir}/texmf-dist/tex/latex/achemso/natmove.sty
%{_texdir}/texmf-dist/tex/latex/achemso/config/acbcct.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/accacs.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/acsccc.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/achre4.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/acncdm.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/ancac3.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/ancham.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/bcches.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/bichaw.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/bipret.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/bomaf6.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/cgdefu.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/chreay.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/cmatex.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/crtoec.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/enfuem.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/esthag.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/iecred.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/inoraj.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/jacsat.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/jafcau.cfg
#%{_texdir}/texmf-dist/tex/latex/achemso/config/jcchff.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/jceaax.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/jceda8.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/jcisd8.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/jctcce.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/jmcmar.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/jnprdf.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/joceah.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/jpcafh.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/jpcbfk.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/jpccck.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/jpclcd.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/jprobs.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/langd5.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/mamobx.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/mpohbp.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/nalefd.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/oprdfk.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/orgnd7.cfg
%{_texdir}/texmf-dist/tex/latex/achemso/config/orlef7.cfg

%files doc
%defattr(-,root,root)
#%doc lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/achemso/README
%{_texdir}/texmf-dist/doc/latex/achemso/achemso-demo.bib
%{_texdir}/texmf-dist/doc/latex/achemso/achemso-demo.pdf
%{_texdir}/texmf-dist/doc/latex/achemso/achemso-demo.tex
%{_texdir}/texmf-dist/doc/latex/achemso/achemso.pdf


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
