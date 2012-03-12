%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/antomega.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/antomega.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/antomega.source.tar.xz

Name: texlive-antomega
License: LPPL
Summary: Alternative language support for Omega/Lambda
Version: %{tl_version}
Release: %{tl_noarch_release}.0.8.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-omega = %{tl_version}
Provides: tex(antomega.sty)
Provides: tex(omega-english.sty)
Provides: tex(omega-french.sty)
Provides: tex(omega-german.sty)
Provides: tex(omega-greek.sty)
Provides: tex(omega-latin.sty)
Provides: tex(omega-latvian.sty)
Provides: tex(omega-polish.sty)
Provides: tex(omega-russian.sty)
Provides: tex(omega-spanish.sty)
Requires: tex(keyval.sty)
Requires: tex(ifthen.sty)
Requires: tex(calc.sty)

%description
A language support package for Omega/Lambda. This replaces the
original omega package for use with Lambda, and provides extra
facilities (including Babel-like language switching, which
eases porting of LaTeX documents to Lambda).

date: 2007-01-23 22:34:44 +0100

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
Summary: Documentation for antomega
Version: %{tl_version}
Release: %{tl_noarch_release}.0.8.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch
Requires: texlive-omega-doc

%description doc
Documentation for antomega


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
%{_texdir}/texmf-dist/omega/ocp/antomega/babel2de.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/babel2es.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/babel2la.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/babel2pl.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/babel2punct.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/babel2ru.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/bblgrk2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/dosrus2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/greek2punct.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/iso2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/isobaltic2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/isoce2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/isocyr2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/isogrk2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/koirus2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/latcyr2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/oldstyle.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/rhobre.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/rhonobre.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/tex2punct.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/texgrk2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/uni2accents.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/uni2lgr.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/uni2lig.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/uni2omega.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/uni2t1.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/uni2t2a.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/uniutf2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/uppercase-dflt.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/win2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/winbaltic2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/wince2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/wincyr2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/latin/la-lig.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/latin/la-longs.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/latin/la-noj.ocp
%{_texdir}/texmf-dist/omega/ocp/antomega/latin/la-nouv.ocp
%{_texdir}/texmf-dist/omega/otp/antomega/babel2de.otp
%{_texdir}/texmf-dist/omega/otp/antomega/babel2es.otp
%{_texdir}/texmf-dist/omega/otp/antomega/babel2la.otp
%{_texdir}/texmf-dist/omega/otp/antomega/babel2pl.otp
%{_texdir}/texmf-dist/omega/otp/antomega/babel2punct.otp
%{_texdir}/texmf-dist/omega/otp/antomega/babel2ru.otp
%{_texdir}/texmf-dist/omega/otp/antomega/bblgrk2uni.otp
%{_texdir}/texmf-dist/omega/otp/antomega/dosrus2uni.otp
%{_texdir}/texmf-dist/omega/otp/antomega/greek2punct.otp
%{_texdir}/texmf-dist/omega/otp/antomega/iso2uni.otp
%{_texdir}/texmf-dist/omega/otp/antomega/isobaltic2uni.otp
%{_texdir}/texmf-dist/omega/otp/antomega/isoce2uni.otp
%{_texdir}/texmf-dist/omega/otp/antomega/isocyr2uni.otp
%{_texdir}/texmf-dist/omega/otp/antomega/isogrk2uni.otp
%{_texdir}/texmf-dist/omega/otp/antomega/koirus2uni.otp
%{_texdir}/texmf-dist/omega/otp/antomega/latcyr2uni.otp
%{_texdir}/texmf-dist/omega/otp/antomega/rhobre.otp
%{_texdir}/texmf-dist/omega/otp/antomega/rhonobre.otp
%{_texdir}/texmf-dist/omega/otp/antomega/tex2punct.otp
%{_texdir}/texmf-dist/omega/otp/antomega/texgrk2uni.otp
%{_texdir}/texmf-dist/omega/otp/antomega/uni2accents.otp
%{_texdir}/texmf-dist/omega/otp/antomega/uni2lgr.otp
%{_texdir}/texmf-dist/omega/otp/antomega/uni2lig.otp
%{_texdir}/texmf-dist/omega/otp/antomega/uni2omega.otp
%{_texdir}/texmf-dist/omega/otp/antomega/uni2t1.otp
%{_texdir}/texmf-dist/omega/otp/antomega/uni2t2a.otp
%{_texdir}/texmf-dist/omega/otp/antomega/uniutf2uni.otp
%{_texdir}/texmf-dist/omega/otp/antomega/uppercase-dflt.otp
%{_texdir}/texmf-dist/omega/otp/antomega/win2uni.otp
%{_texdir}/texmf-dist/omega/otp/antomega/winbaltic2uni.otp
%{_texdir}/texmf-dist/omega/otp/antomega/wince2uni.otp
%{_texdir}/texmf-dist/omega/otp/antomega/wincyr2uni.otp
%{_texdir}/texmf-dist/omega/otp/antomega/latin/la-lig.otp
%{_texdir}/texmf-dist/omega/otp/antomega/latin/la-longs.otp
%{_texdir}/texmf-dist/omega/otp/antomega/latin/la-noj.otp
%{_texdir}/texmf-dist/omega/otp/antomega/latin/la-nouv.otp
%{_texdir}/texmf-dist/tex/lambda/antomega/antomega.cfg
%{_texdir}/texmf-dist/tex/lambda/antomega/antomega.sty
%{_texdir}/texmf-dist/tex/lambda/antomega/grhyph16.tex
%{_texdir}/texmf-dist/tex/lambda/antomega/hyphen.cfg
%{_texdir}/texmf-dist/tex/lambda/antomega/language.dat.sample
%{_texdir}/texmf-dist/tex/lambda/antomega/lgc0700.def
%{_texdir}/texmf-dist/tex/lambda/antomega/lgrenc-antomega.def
%{_texdir}/texmf-dist/tex/lambda/antomega/ograhyph4.tex
%{_texdir}/texmf-dist/tex/lambda/antomega/ogrmhyph4.tex
%{_texdir}/texmf-dist/tex/lambda/antomega/ogrphyph4.tex
%{_texdir}/texmf-dist/tex/lambda/antomega/omega-english.ldf
%{_texdir}/texmf-dist/tex/lambda/antomega/omega-french.ldf
%{_texdir}/texmf-dist/tex/lambda/antomega/omega-german.ldf
%{_texdir}/texmf-dist/tex/lambda/antomega/omega-greek.ldf
%{_texdir}/texmf-dist/tex/lambda/antomega/omega-latin.ldf
%{_texdir}/texmf-dist/tex/lambda/antomega/omega-latvian.ldf
%{_texdir}/texmf-dist/tex/lambda/antomega/omega-polish.ldf
%{_texdir}/texmf-dist/tex/lambda/antomega/omega-russian.ldf
%{_texdir}/texmf-dist/tex/lambda/antomega/omega-spanish.ldf
%{_texdir}/texmf-dist/tex/lambda/antomega/ruhyph16.tex
%{_texdir}/texmf-dist/tex/lambda/antomega/t1enc-antomega.def
%{_texdir}/texmf-dist/tex/lambda/antomega/t2aenc-antomega.def
%{_texdir}/texmf-dist/tex/lambda/antomega/uni0100.def
%{_texdir}/texmf-dist/tex/lambda/antomega/uni0370.def
%{_texdir}/texmf-dist/tex/lambda/antomega/uni0400.def
%{_texdir}/texmf-dist/tex/lambda/antomega/uni1f00.def
%{_texdir}/texmf-dist/tex/lambda/antomega/ut1enc-antomega.def

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/omega/antomega/README
%{_texdir}/texmf-dist/doc/omega/antomega/antomega.pdf


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
