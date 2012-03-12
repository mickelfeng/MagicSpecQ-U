%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cyrillic.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cyrillic.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cyrillic.source.tar.xz

Name: texlive-cyrillic
License: LPPL
Summary: Support for Cyrillic fonts in LaTeX
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-cyrillic-bin = %{tl_version}
Provides: tex(lcy.sty)
Requires: tex(fontenc.sty)

%description
This bundle of macros files provides macro support (including
font encoding macros) for the use of Cyrillic characters in
fonts encoded under the T2* and X2 encodings. These encodings
cover (between them) pretty much every language that is written
in a Cyrillic alphabet. This directory is part of the LaTeX
"required" distribution.

date: 2009-09-24 20:53:04 +0200

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
Summary: Documentation for cyrillic
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for cyrillic


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
%{_texdir}/texmf-dist/tex/latex/cyrillic/cp1251.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/cp855.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/cp866.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/cp866av.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/cp866mav.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/cp866nav.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/cp866tat.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/ctt.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/dbk.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/iso88595.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/isoir111.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/koi8-r.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/koi8-ru.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/koi8-u.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/lcy.sty
%{_texdir}/texmf-dist/tex/latex/cyrillic/lcyccr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/lcycmbr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/lcycmdh.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/lcycmfib.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/lcycmfr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/lcycmr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/lcycmss.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/lcycmtl.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/lcycmtt.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/lcycmvtt.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/lcydefs.tex
%{_texdir}/texmf-dist/tex/latex/cyrillic/lcyenc.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/lcylcmss.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/lcylcmtt.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/maccyr.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/macukr.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/mik.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/mls.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/mnk.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/mos.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/ncc.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/ot2ccr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/ot2cmbr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/ot2cmdh.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/ot2cmfib.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/ot2cmfr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/ot2cmr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/ot2cmss.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/ot2cmtl.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/ot2cmtt.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/ot2cmvtt.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/ot2enc.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/ot2lcmss.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/ot2lcmtt.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/ot2wlcyr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/ot2wlcyss.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/ot2wncyr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/ot2wncyss.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/pt154.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/pt254.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2accr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2acmbr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2acmdh.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2acmfib.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2acmfr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2acmr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2acmss.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2acmtl.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2acmtt.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2acmvtt.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2aenc.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2alcmss.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2alcmtt.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2bccr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2bcmbr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2bcmdh.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2bcmfib.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2bcmfr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2bcmr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2bcmss.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2bcmtl.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2bcmtt.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2bcmvtt.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2benc.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2blcmss.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2blcmtt.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2cccr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2ccmbr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2ccmdh.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2ccmfib.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2ccmfr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2ccmr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2ccmss.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2ccmtl.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2ccmtt.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2ccmvtt.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2cenc.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2clcmss.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/t2clcmtt.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/x2ccr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/x2cmbr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/x2cmdh.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/x2cmfib.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/x2cmfr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/x2cmr.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/x2cmss.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/x2cmtl.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/x2cmtt.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/x2cmvtt.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/x2enc.def
%{_texdir}/texmf-dist/tex/latex/cyrillic/x2lcmss.fd
%{_texdir}/texmf-dist/tex/latex/cyrillic/x2lcmtt.fd

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/cyrillic/00readme.txt
%{_texdir}/texmf-dist/doc/latex/cyrillic/changes.txt
%{_texdir}/texmf-dist/doc/latex/cyrillic/cyinpenc.pdf
%{_texdir}/texmf-dist/doc/latex/cyrillic/cyoutenc.pdf
%{_texdir}/texmf-dist/doc/latex/cyrillic/lcy.pdf
%{_texdir}/texmf-dist/doc/latex/cyrillic/lcycmlh.pdf
%{_texdir}/texmf-dist/doc/latex/cyrillic/manifest.txt
%{_texdir}/texmf-dist/doc/latex/cyrillic/ot2.pdf
%{_texdir}/texmf-dist/doc/latex/cyrillic/ot2cmams.pdf
%{_texdir}/texmf-dist/doc/latex/cyrillic/ot2cmlh.pdf
%{_texdir}/texmf-dist/doc/latex/cyrillic/t2lhfnt.pdf


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
