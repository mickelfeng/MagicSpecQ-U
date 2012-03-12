%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/fpl.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/fpl.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/fpl.source.tar.xz

Name: texlive-fpl
License: GPL+
Summary: SC and OsF fonts for URW Palladio L
Version: %{tl_version}
Release: %{tl_noarch_release}.1.002.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-fpl-fedora-fonts = %{tl_version}

%description
The FPL Fonts provide a set of SC/OsF fonts for URW Palladio L
which are compatible with respect to metrics with the Palatino
SC/OsF fonts from Adobe. Note that it is not my aim to exactly
reproduce the outlines of the original Adobe fonts. The SC and
OsF in the FPL Fonts were designed with the glyphs from URW
Palladio L as starting point. For some glyphs (e.g. 'o') I got
the best result by scaling and boldening. For others (e.g. 'h')
shifting selected portions of the character gave more
satisfying results. All this was done using the free font
editor FontForge. The kerning data in these fonts comes from
Walter Schmidt's improved Palatino metrics. LaTeX use is
enabled by the mathpazo package, which is part of the psnfss
distribution.

date: 2007-09-28 22:20:10 +0200

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
Summary: Documentation for fpl
Version: %{tl_version}
Release: %{tl_noarch_release}.1.002.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for fpl

%package fedora-fonts
Summary: Fonts for fpl
Version: %{tl_version}
Release: %{tl_noarch_release}.1.002.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-fpl = %{tl_version}
BuildArch: noarch

%description fedora-fonts
The FPL Fonts provide a set of SC/OsF fonts for URW Palladio L
which are compatible with respect to metrics with the Palatino
SC/OsF fonts from Adobe. Note that it is not my aim to exactly
reproduce the outlines of the original Adobe fonts. The SC and
OsF in the FPL Fonts were designed with the glyphs from URW
Palladio L as starting point. For some glyphs (e.g. 'o') I got
the best result by scaling and boldening. For others (e.g. 'h')
shifting selected portions of the character gave more
satisfying results. All this was done using the free font
editor FontForge. The kerning data in these fonts comes from
Walter Schmidt's improved Palatino metrics. LaTeX use is
enabled by the mathpazo package, which is part of the psnfss
distribution.

date: 2007-09-28 22:20:10 +0200


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/gpl.txt gpl.txt
xz -dc %{SOURCE0} | tar x -C %{buildroot}%{_texdir}/texmf-dist
xz -dc %{SOURCE1} | tar x -C %{buildroot}%{_texdir}/texmf-dist
# nuke useless tlmgr packaging stuff and doc droppings
rm -rf %{buildroot}%{_texdir}/tlpkg/tlpobj/
rm -rf %{buildroot}%{_texdir}/texmf-dist/tlpkg/tlpobj/
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/man*/*.pdf
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/Makefile
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/man*/Makefile
rm -rf %{buildroot}%{_texdir}/texmf/doc/info/dir

# link installed fonts with Fedora
install -d -m 0755 %{buildroot}%{_fontdir}
pushd %{buildroot}%{_fontdir}
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fpl/fplbij8a.pfb .
ln -s %{_fontdir}/fplbij8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fpl/fplbij8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fpl/fplbj8a.pfb .
ln -s %{_fontdir}/fplbj8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fpl/fplbj8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fpl/fplrc8a.pfb .
ln -s %{_fontdir}/fplrc8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fpl/fplrc8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fpl/fplrij8a.pfb .
ln -s %{_fontdir}/fplrij8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fpl/fplrij8a.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/fonts/afm/public/fpl/fplbij8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/fpl/fplbj8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/fpl/fplrc8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/fpl/fplrij8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/fpl/pplb9d-kern.afm
%{_texdir}/texmf-dist/fonts/afm/public/fpl/pplbi9d-kern.afm
%{_texdir}/texmf-dist/fonts/afm/public/fpl/pplrc9d-kern.afm
%{_texdir}/texmf-dist/fonts/afm/public/fpl/pplri9d-kern.afm
%{_texdir}/texmf-dist/fonts/type1/public/fpl/fplbij8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/fpl/fplbij8a.pfm
%{_texdir}/texmf-dist/fonts/type1/public/fpl/fplbj8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/fpl/fplbj8a.pfm
%{_texdir}/texmf-dist/fonts/type1/public/fpl/fplrc8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/fpl/fplrc8a.pfm
%{_texdir}/texmf-dist/fonts/type1/public/fpl/fplrij8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/fpl/fplrij8a.pfm

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/fonts/fpl/COPYING
%{_texdir}/texmf-dist/doc/fonts/fpl/README

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/fplbij8a.pfb
%{_fontdir}/fplbj8a.pfb
%{_fontdir}/fplrc8a.pfb
%{_fontdir}/fplrij8a.pfb

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
