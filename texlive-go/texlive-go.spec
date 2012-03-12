%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/go.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/go.source.tar.xz

Name: texlive-go
License: Public Domain
Summary: Fonts and macros for typesetting go games
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(go.sty)

%description
The macros provide for nothing more complicated than the
standard 19x19 board; the fonts are written in MetaFont.

date: 2010-02-19 00:25:14 +0100

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
ln -s %{_texdir}/licenses/pd.txt pd.txt
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
%doc pd.txt
%{_texdir}/texmf-dist/fonts/source/public/go/go.mf
%{_texdir}/texmf-dist/fonts/source/public/go/go10.mf
%{_texdir}/texmf-dist/fonts/source/public/go/go15.mf
%{_texdir}/texmf-dist/fonts/source/public/go/go1bla10.mf
%{_texdir}/texmf-dist/fonts/source/public/go/go1bla15.mf
%{_texdir}/texmf-dist/fonts/source/public/go/go1bla20.mf
%{_texdir}/texmf-dist/fonts/source/public/go/go1black.mf
%{_texdir}/texmf-dist/fonts/source/public/go/go1whi10.mf
%{_texdir}/texmf-dist/fonts/source/public/go/go1whi15.mf
%{_texdir}/texmf-dist/fonts/source/public/go/go1whi20.mf
%{_texdir}/texmf-dist/fonts/source/public/go/go1white.mf
%{_texdir}/texmf-dist/fonts/source/public/go/go20.mf
%{_texdir}/texmf-dist/fonts/source/public/go/go2bla10.mf
%{_texdir}/texmf-dist/fonts/source/public/go/go2bla15.mf
%{_texdir}/texmf-dist/fonts/source/public/go/go2bla20.mf
%{_texdir}/texmf-dist/fonts/source/public/go/go2black.mf
%{_texdir}/texmf-dist/fonts/source/public/go/go2whi10.mf
%{_texdir}/texmf-dist/fonts/source/public/go/go2whi15.mf
%{_texdir}/texmf-dist/fonts/source/public/go/go2whi20.mf
%{_texdir}/texmf-dist/fonts/source/public/go/go2white.mf
%{_texdir}/texmf-dist/fonts/source/public/go/gosign50.mf
%{_texdir}/texmf-dist/fonts/tfm/public/go/go10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/go/go15.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/go/go1bla10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/go/go1bla15.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/go/go1bla20.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/go/go1whi10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/go/go1whi15.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/go/go1whi20.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/go/go20.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/go/go2bla10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/go/go2bla15.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/go/go2bla20.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/go/go2whi10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/go/go2whi15.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/go/go2whi20.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/go/gosign50.tfm
%{_texdir}/texmf-dist/tex/latex/go/go.sty


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