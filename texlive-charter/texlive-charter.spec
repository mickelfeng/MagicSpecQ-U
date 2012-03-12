%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/charter.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/charter.doc.tar.xz

Name: texlive-charter
License: Freely redistributable without restriction
Summary: Charter fonts
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-charter-fedora-fonts = %{tl_version}

%description
A commercial text font donated for the common good. Support for
use with LaTeX is available in freenfss, part of psnfss.

date: 2009-05-23 20:19:02 +0200

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
Summary: Documentation for charter
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for charter

%package fedora-fonts
Summary: Fonts for charter
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-charter = %{tl_version}
BuildArch: noarch

%description fedora-fonts
A commercial text font donated for the common good. Support for
use with LaTeX is available in freenfss, part of psnfss.

date: 2009-05-23 20:19:02 +0200


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

# link installed fonts with Fedora
install -d -m 0755 %{buildroot}%{_fontdir}
pushd %{buildroot}%{_fontdir}
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/bitstrea/charter/bchb8a.pfb .
ln -s %{_fontdir}/bchb8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/bitstrea/charter/bchb8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/bitstrea/charter/bchbi8a.pfb .
ln -s %{_fontdir}/bchbi8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/bitstrea/charter/bchbi8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/bitstrea/charter/bchr8a.pfb .
ln -s %{_fontdir}/bchr8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/bitstrea/charter/bchr8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/bitstrea/charter/bchri8a.pfb .
ln -s %{_fontdir}/bchri8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/bitstrea/charter/bchri8a.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/fonts/afm/bitstrea/charter/bchb8a.afm
%{_texdir}/texmf-dist/fonts/afm/bitstrea/charter/bchbi8a.afm
%{_texdir}/texmf-dist/fonts/afm/bitstrea/charter/bchr8a.afm
%{_texdir}/texmf-dist/fonts/afm/bitstrea/charter/bchri8a.afm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchb7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchb8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchb8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchb8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchbc7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchbc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchbi7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchbi8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchbi8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchbi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchbo7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchbo8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchbo8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchbo8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchr7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchr8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchr8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchr8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchrc7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchrc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchri7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchri8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchri8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchri8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchro7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchro8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchro8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/bchro8t.tfm
%{_texdir}/texmf-dist/fonts/type1/bitstrea/charter/bchb8a.pfb
%{_texdir}/texmf-dist/fonts/type1/bitstrea/charter/bchbi8a.pfb
%{_texdir}/texmf-dist/fonts/type1/bitstrea/charter/bchr8a.pfb
%{_texdir}/texmf-dist/fonts/type1/bitstrea/charter/bchri8a.pfb
%{_texdir}/texmf-dist/fonts/vf/bitstrea/charter/bchb7t.vf
%{_texdir}/texmf-dist/fonts/vf/bitstrea/charter/bchb8c.vf
%{_texdir}/texmf-dist/fonts/vf/bitstrea/charter/bchb8t.vf
%{_texdir}/texmf-dist/fonts/vf/bitstrea/charter/bchbc7t.vf
%{_texdir}/texmf-dist/fonts/vf/bitstrea/charter/bchbc8t.vf
%{_texdir}/texmf-dist/fonts/vf/bitstrea/charter/bchbi7t.vf
%{_texdir}/texmf-dist/fonts/vf/bitstrea/charter/bchbi8c.vf
%{_texdir}/texmf-dist/fonts/vf/bitstrea/charter/bchbi8t.vf
%{_texdir}/texmf-dist/fonts/vf/bitstrea/charter/bchbo7t.vf
%{_texdir}/texmf-dist/fonts/vf/bitstrea/charter/bchbo8c.vf
%{_texdir}/texmf-dist/fonts/vf/bitstrea/charter/bchbo8t.vf
%{_texdir}/texmf-dist/fonts/vf/bitstrea/charter/bchr7t.vf
%{_texdir}/texmf-dist/fonts/vf/bitstrea/charter/bchr8c.vf
%{_texdir}/texmf-dist/fonts/vf/bitstrea/charter/bchr8t.vf
%{_texdir}/texmf-dist/fonts/vf/bitstrea/charter/bchrc7t.vf
%{_texdir}/texmf-dist/fonts/vf/bitstrea/charter/bchrc8t.vf
%{_texdir}/texmf-dist/fonts/vf/bitstrea/charter/bchri7t.vf
%{_texdir}/texmf-dist/fonts/vf/bitstrea/charter/bchri8c.vf
%{_texdir}/texmf-dist/fonts/vf/bitstrea/charter/bchri8t.vf
%{_texdir}/texmf-dist/fonts/vf/bitstrea/charter/bchro7t.vf
%{_texdir}/texmf-dist/fonts/vf/bitstrea/charter/bchro8c.vf
%{_texdir}/texmf-dist/fonts/vf/bitstrea/charter/bchro8t.vf

%files doc
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/doc/fonts/charter/readme.charter

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/bchb8a.pfb
%{_fontdir}/bchbi8a.pfb
%{_fontdir}/bchr8a.pfb
%{_fontdir}/bchri8a.pfb

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
