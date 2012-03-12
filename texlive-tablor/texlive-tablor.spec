%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/tablor.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/tablor.doc.tar.xz

Name: texlive-tablor
License: LPPL
Summary: Create tables of signs and of variations
Version: %{tl_version}
Release: %{tl_noarch_release}.4.07.svn18250%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(tablor-xetex.sty)
Provides: tex(tablor.sty)
Requires: tex(filecontents.sty)
Requires: tex(ifthen.sty)
Requires: tex(fancyvrb.sty)
Requires: tex(ifpdf.sty)
Requires: tex(ifxetex.sty)

%description
The package allows the user to use the computer algebra system
XCAS to generate tables of signs and of variations (the actual
plotting of the tables uses the MetaPost macro package
tableauVariations). Tables with forbidden regions may be
developed using the package. A configuration file permits some
configuration of the language to be used in the diagrams. The
tablor package requires that shell escape be enabled.

date: 2010-05-10 13:49:50 +0200

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
Summary: Documentation for tablor
Version: %{tl_version}
Release: %{tl_noarch_release}.4.07.svn18250%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for tablor


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
%{_texdir}/texmf-dist/tex/latex/tablor/tablor-xetex.sty
%{_texdir}/texmf-dist/tex/latex/tablor/tablor.cfg
%{_texdir}/texmf-dist/tex/latex/tablor/tablor.sty

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/TSav-105.mp
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/capture.eps
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.0
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.1
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.10
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.105
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.11
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.12
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.13
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.14
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.15
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.16
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.17
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.18
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.19
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.2
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.20
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.21
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.22
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.23
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.24
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.25
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.26
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.27
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.28
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.29
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.3
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.30
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.31
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.32
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.33
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.35
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.36
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.37
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.38
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.39
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.4
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.40
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.41
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.42
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.43
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.44
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.45
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.47
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.48
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.49
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.5
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.50
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.51
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.52
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.53
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.54
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.55
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.56
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.57
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.6
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.7
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.8
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.9
%{_texdir}/texmf-dist/doc/latex/tablor/Figures/tablor_Tab.mp
%{_texdir}/texmf-dist/doc/latex/tablor/README
%{_texdir}/texmf-dist/doc/latex/tablor/README-fr.txt
%{_texdir}/texmf-dist/doc/latex/tablor/tablor.html
%{_texdir}/texmf-dist/doc/latex/tablor/tablor.pdf
%{_texdir}/texmf-dist/doc/latex/tablor/tablor.tex


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
