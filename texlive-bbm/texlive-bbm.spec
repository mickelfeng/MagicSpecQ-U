%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/bbm.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/bbm.doc.tar.xz

Name: texlive-bbm
License: Freely redistributable without restriction
Summary: "Blackboard-style" cm fonts
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}

%description
Blackboard variants of Computer Modern fonts. The fonts are
distributed as MetaFont source (only); LaTeX support is
available with the bbm-macros package. The Sauter font package
has MetaFont parameter source files for building the fonts at
more sizes than you could reasonably imagine. A sample of these
fonts appears in the blackboard bold sampler.

date: 2009-11-19 15:03:53 +0100

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
Summary: Documentation for bbm
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for bbm


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/other-free.txt other-free.txt
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
%doc other-free.txt
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbm10.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbm12.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbm17.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbm5.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbm6.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbm7.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbm8.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbm9.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmb10.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmbx10.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmbx12.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmbx5.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmbx6.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmbx7.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmbx8.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmbx9.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmbxsl10.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmdunh10.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmfib8.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmfxib8.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbminch.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmsl10.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmsl12.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmsl8.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmsl9.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmsltt10.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmss10.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmss12.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmss17.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmss8.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmss9.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmssbx10.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmssdc10.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmssi10.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmssi12.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmssi17.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmssi8.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmssi9.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmssq8.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmssqi8.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmtt10.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmtt12.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmtt8.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmtt9.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/bbmvtt10.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/blbbase.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/blbord.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/blbordl.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/blbordsp.mf
%{_texdir}/texmf-dist/fonts/source/public/bbm/blbordu.mf
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbm10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbm12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbm17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbm5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbm6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbm7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbm8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbm9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmbx12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmbx5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmbx6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmbx7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmbx8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmbx9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmbxsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmdunh10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmfib8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmfxib8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmsl12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmsl8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmsl9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmss10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmss12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmss17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmss8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmss9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmssbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmssdc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmssi10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmssi12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmssi17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmssi8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmssi9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmssq8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmssqi8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmtt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmtt12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmtt8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/bbmtt9.tfm

%files doc
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/doc/fonts/bbm/README
%{_texdir}/texmf-dist/doc/fonts/bbm/gfbatch.batch
%{_texdir}/texmf-dist/doc/fonts/bbm/mfbatch.batch
%{_texdir}/texmf-dist/doc/fonts/bbm/test.tex


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
