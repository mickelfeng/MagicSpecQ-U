%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/asymptote-manual-zh-cn.doc.tar.xz

Name: texlive-asymptote-manual-zh-cn-doc
License: LGPLv2+
Summary: Documentation for asymptote-manual-zh-cn
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description
Documentation for asymptote-manual-zh-cn


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/lgpl.txt lgpl.txt
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
%doc lgpl.txt
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/README
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/asymptote-manual-zh-cn.pdf
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/CDlabel.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/CLEAN.bat
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/Coons.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/Gouraud.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/MAKEPDF.bat
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/Pythagoras.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/adobefonts.tex
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/asycolors.sty
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/asysyntex.tex
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/axialshade.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/bezier2.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/beziercurve.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/bigsquare.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/cleantmp
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/clippath.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/colons.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/colors.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/cube.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/diagonal.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/dots.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/fzfonts.tex
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/hatch.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/join.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/labelalign.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/labelsquare.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/latticeshading.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/linecap.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/linejoin.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/linetype.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/logo.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/main.tex
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/makepdf
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/makepen.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/mexicanhat.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/quartercircle.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/shadedtiling.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/shadestroke.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/square.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/subpictures.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/superpath.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/tile.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/transparency.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/windingnumber.asy
%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/winfonts.tex


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
