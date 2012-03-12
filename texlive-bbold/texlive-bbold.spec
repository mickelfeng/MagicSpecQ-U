%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/bbold.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/bbold.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/bbold.source.tar.xz

Name: texlive-bbold
License: BSD
Summary: Sans serif blackboard bold
Version: %{tl_version}
Release: %{tl_noarch_release}.1.01.svn17187%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(bbold.sty)

%description
A geometric sans serif blackboard bold font, for use in
mathematics; MetaFont sources are provided, as well as macros
for use with LaTeX. The Sauter font package has MetaFont
parameter source files for building the fonts at more sizes
than you could reasonably imagine. See the blackboard sampler
for a feel for the font's appearance.

date: 2010-02-15 23:28:51 +0100

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
Summary: Documentation for bbold
Version: %{tl_version}
Release: %{tl_noarch_release}.1.01.svn17187%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for bbold


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/bsd.txt bsd.txt
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
%doc bsd.txt
%{_texdir}/texmf-dist/fonts/source/public/bbold/bbbase.mf
%{_texdir}/texmf-dist/fonts/source/public/bbold/bbgreekl.mf
%{_texdir}/texmf-dist/fonts/source/public/bbold/bbgreeku.mf
%{_texdir}/texmf-dist/fonts/source/public/bbold/bbligs.mf
%{_texdir}/texmf-dist/fonts/source/public/bbold/bblower.mf
%{_texdir}/texmf-dist/fonts/source/public/bbold/bbnum.mf
%{_texdir}/texmf-dist/fonts/source/public/bbold/bbold.mf
%{_texdir}/texmf-dist/fonts/source/public/bbold/bbold10.mf
%{_texdir}/texmf-dist/fonts/source/public/bbold/bbold12.mf
%{_texdir}/texmf-dist/fonts/source/public/bbold/bbold17.mf
%{_texdir}/texmf-dist/fonts/source/public/bbold/bbold5.mf
%{_texdir}/texmf-dist/fonts/source/public/bbold/bbold6.mf
%{_texdir}/texmf-dist/fonts/source/public/bbold/bbold7.mf
%{_texdir}/texmf-dist/fonts/source/public/bbold/bbold8.mf
%{_texdir}/texmf-dist/fonts/source/public/bbold/bbold9.mf
%{_texdir}/texmf-dist/fonts/source/public/bbold/bbparams.mf
%{_texdir}/texmf-dist/fonts/source/public/bbold/bbpunc.mf
%{_texdir}/texmf-dist/fonts/source/public/bbold/bbupper.mf
%{_texdir}/texmf-dist/fonts/tfm/public/bbold/bbold10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbold/bbold12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbold/bbold17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbold/bbold5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbold/bbold6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbold/bbold7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbold/bbold8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbold/bbold9.tfm
%{_texdir}/texmf-dist/tex/latex/bbold/Ubbold.fd
%{_texdir}/texmf-dist/tex/latex/bbold/bbold.sty

%files doc
%defattr(-,root,root)
%doc bsd.txt
%{_texdir}/texmf-dist/doc/latex/bbold/INSTALL
%{_texdir}/texmf-dist/doc/latex/bbold/README
%{_texdir}/texmf-dist/doc/latex/bbold/bbold.pdf


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
