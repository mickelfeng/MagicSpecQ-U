%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/mathabx.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/mathabx.doc.tar.xz

Name: texlive-mathabx
License: LPPL
Summary: Three series of mathematical symbols
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(mathabx.sty)

%description
Mathabx is a set of 3 mathematical symbols font series: matha,
mathb and mathx. They are defined by MetaFont code and should
be of reasonable quality (bitmap output). Things change from
time to time, so there is no claim of stability (encoding,
metrics, design). The package includes Plain TeX and LaTeX
support macros.

date: 2008-09-15 13:48:16 +0200

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
Summary: Documentation for mathabx
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for mathabx


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
%{_texdir}/texmf-dist/fonts/source/public/mathabx/matha10.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/matha12.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/matha5.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/matha6.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/matha7.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/matha8.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/matha9.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathacnt.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathadrv.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/matharrw.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathastr.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathastrotest10.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathastrotestdrv.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathasym.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathb10.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathb12.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathb5.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathb6.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathb7.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathb8.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathb9.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathbase.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathbdel.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathbdrv.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathbigs.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathbsym.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathc10.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathcall.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathcallgreek.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathcdrv.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathfine.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathgrey.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathhbrw.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathineq.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathltlk.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathmbcb.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathprmt.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathsmsy.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathsubs.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathsymb.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathu10.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathudrv.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathusym.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathux10.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathuxdrv.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathx10.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathx12.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathx5.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathx6.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathx7.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathx8.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathx9.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/mathxdrv.mf
%{_texdir}/texmf-dist/fonts/source/public/mathabx/maydigit.mf
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/matha10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/matha12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/matha5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/matha6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/matha7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/matha8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/matha9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/mathastrotest10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/mathb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/mathb12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/mathb5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/mathb6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/mathb7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/mathb8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/mathb9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/mathc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/mathu10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/mathux10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/mathx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/mathx12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/mathx5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/mathx6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/mathx7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/mathx8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mathabx/mathx9.tfm
%{_texdir}/texmf-dist/tex/generic/mathabx/mathabx.dcl
%{_texdir}/texmf-dist/tex/generic/mathabx/mathabx.sty
%{_texdir}/texmf-dist/tex/generic/mathabx/mathabx.tex

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/fonts/mathabx/README
%{_texdir}/texmf-dist/doc/fonts/mathabx/mathtest.pdf
%{_texdir}/texmf-dist/doc/fonts/mathabx/mathtest.tex
%{_texdir}/texmf-dist/doc/fonts/mathabx/testmac.tex


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
