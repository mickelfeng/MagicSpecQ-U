%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/utopia.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/utopia.doc.tar.xz

Name: texlive-utopia
License: Freely redistributable without restriction
Summary: Adobe Utopia fonts
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-utopia-fedora-fonts = %{tl_version}

%description
The Adobe Standard Encoding set (upright and italic shapes,
medium and bold weights) of the Utopia font family, which Adobe
donated to the X Consortium. Macro support, and maths fonts
that match the Utopia family, are provided by the Fourier and
the Mathdesign Utopia font packages.

date: 2007-10-04 10:35:17 +0200

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
Summary: Documentation for utopia
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for utopia

%package fedora-fonts
Summary: Fonts for utopia
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-utopia = %{tl_version}
BuildArch: noarch

%description fedora-fonts
The Adobe Standard Encoding set (upright and italic shapes,
medium and bold weights) of the Utopia font family, which Adobe
donated to the X Consortium. Macro support, and maths fonts
that match the Utopia family, are provided by the Fourier and
the Mathdesign Utopia font packages.

date: 2007-10-04 10:35:17 +0200


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/adobe/utopia/putb8a.pfb .
ln -s %{_fontdir}/putb8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/adobe/utopia/putb8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/adobe/utopia/putbi8a.pfb .
ln -s %{_fontdir}/putbi8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/adobe/utopia/putbi8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/adobe/utopia/putr8a.pfb .
ln -s %{_fontdir}/putr8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/adobe/utopia/putr8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/adobe/utopia/putri8a.pfb .
ln -s %{_fontdir}/putri8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/adobe/utopia/putri8a.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/fonts/afm/adobe/utopia/putb8a.afm
%{_texdir}/texmf-dist/fonts/afm/adobe/utopia/putbi8a.afm
%{_texdir}/texmf-dist/fonts/afm/adobe/utopia/putr8a.afm
%{_texdir}/texmf-dist/fonts/afm/adobe/utopia/putri8a.afm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putb7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putb8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putb8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putb8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putbc7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putbc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putbi7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putbi8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putbi8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putbi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putbo7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putbo8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putbo8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putbo8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putr7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putr8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putr8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putr8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putrc7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putrc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putri7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putri8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putri8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putri8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putro7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putro8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putro8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia/putro8t.tfm
%{_texdir}/texmf-dist/fonts/type1/adobe/utopia/putb8a.pfb
%{_texdir}/texmf-dist/fonts/type1/adobe/utopia/putbi8a.pfb
%{_texdir}/texmf-dist/fonts/type1/adobe/utopia/putr8a.pfb
%{_texdir}/texmf-dist/fonts/type1/adobe/utopia/putri8a.pfb
%{_texdir}/texmf-dist/fonts/vf/adobe/utopia/putb7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/utopia/putb8c.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/utopia/putb8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/utopia/putbc7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/utopia/putbc8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/utopia/putbi7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/utopia/putbi8c.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/utopia/putbi8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/utopia/putbo7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/utopia/putbo8c.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/utopia/putbo8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/utopia/putr7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/utopia/putr8c.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/utopia/putr8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/utopia/putrc7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/utopia/putrc8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/utopia/putri7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/utopia/putri8c.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/utopia/putri8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/utopia/putro7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/utopia/putro8c.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/utopia/putro8t.vf

%files doc
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/doc/fonts/utopia/LICENSE-utopia.txt
%{_texdir}/texmf-dist/doc/fonts/utopia/README-utopia.txt

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/putb8a.pfb
%{_fontdir}/putbi8a.pfb
%{_fontdir}/putr8a.pfb
%{_fontdir}/putri8a.pfb

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
