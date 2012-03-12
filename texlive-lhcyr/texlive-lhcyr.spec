%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/lhcyr.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/lhcyr.source.tar.xz

Name: texlive-lhcyr
License: Freely redistributable without restriction
Summary: A non-standard Cyrillic input scheme
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(lhcyralt.sty)
Provides: tex(lhcyrkoi.sty)
Provides: tex(lhcyrwin.sty)

%description
A collection of three LaTeX 2e styles intended for typesetting
Russian and bilingual English-Russian documents, using the lh
fonts and without the benefit of babel's language-switching
mechanisms. The packages (lhcyralt and lhcyrwin for use under
emTeX, and lhcyrkoi for use under teTeX) provide mappings
between the input encoding and the font encoding (which is
described as OT1). The way this is done does not match the way
inputenc would do the job, for output via fontenc to one of the
T2 series of font encodings.

date: 2008-04-06 23:48:41 +0200

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


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/other-free.txt other-free.txt
xz -dc %{SOURCE0} | tar x -C %{buildroot}%{_texdir}/texmf-dist
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
%doc other-free.txt
%{_texdir}/texmf-dist/tex/latex/lhcyr/karabas.tex
%{_texdir}/texmf-dist/tex/latex/lhcyr/kniga.tex
%{_texdir}/texmf-dist/tex/latex/lhcyr/otchet.tex
%{_texdir}/texmf-dist/tex/latex/lhcyr/pismo.tex
%{_texdir}/texmf-dist/tex/latex/lhcyr/rusfonts.tex
%{_texdir}/texmf-dist/tex/latex/lhcyr/statya.tex
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyralt/README
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyralt/lhcyralt-hyphen.cfg
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyralt/lhcyralt-rhyphen.tex
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyralt/lhcyralt.sty
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyralt/ot1lhdh.fd
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyralt/ot1lhfib.fd
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyralt/ot1lhfr.fd
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyralt/ot1lhr.fd
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyralt/ot1lhss.fd
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyralt/ot1lhtt.fd
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyralt/ot1lhvtt.fd
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrkoi/README
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrkoi/kcmf.tgz
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrkoi/lhcyrkoi-hyphen.cfg
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrkoi/lhcyrkoi-rhyphen.tex
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrkoi/lhcyrkoi.sty
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrkoi/maketfms.sh
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrkoi/ot1kcdh.fd
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrkoi/ot1kcfib.fd
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrkoi/ot1kcfr.fd
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrkoi/ot1kcr.fd
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrkoi/ot1kcss.fd
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrkoi/ot1kctt.fd
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrkoi/ot1kcvtt.fd
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrkoi/special.kc
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrwin/README
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrwin/lhcyrwin-hyphen.cfg
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrwin/lhcyrwin-rhyphen.tex
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrwin/lhcyrwin.sty
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrwin/ot1wcdh.fd
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrwin/ot1wcfib.fd
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrwin/ot1wcfr.fd
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrwin/ot1wcr.fd
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrwin/ot1wcss.fd
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrwin/ot1wctt.fd
%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrwin/ot1wcvtt.fd


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
