%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/grotesq.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/grotesq.doc.tar.xz

Name: texlive-grotesq
License: GPL+
Summary: URW Grotesq font pack for LaTeX
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-grotesq-fedora-fonts = %{tl_version}

%description
The directory contains a copy of the Type 1 font "URW Grotesq
2031 Bold' released under the GPL by URW, with supporting files
for use with (La)TeX.

date: 2007-11-03 13:04:21 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map ugq.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map ugq.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  %{_bindir}/texhash 2> /dev/null
  %{_bindir}/updmap-sys --nohash --quiet &> /dev/null
else
  mkdir -p /var/run/texlive
  touch /var/run/texlive/run-texhash
  touch /var/run/texlive/run-updmap
fi
:

%posttrans
[ -e /var/run/texlive/run-texhash ] && %{_bindir}/texhash 2> /dev/null && rm -f /var/run/texlive/run-texhash
[ -e /var/run/texlive/run-updmap ] && %{_bindir}/updmap-sys --nohash --quiet &> /dev/null && rm -f /var/run/texlive/run-updmap
[ -e /var/run/texlive ] && rm -rf /var/run/texlive
:

%package doc
Summary: Documentation for grotesq
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for grotesq

%package fedora-fonts
Summary: Fonts for grotesq
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-grotesq = %{tl_version}
BuildArch: noarch

%description fedora-fonts
The directory contains a copy of the Type 1 font "URW Grotesq
2031 Bold' released under the GPL by URW, with supporting files
for use with (La)TeX.

date: 2007-11-03 13:04:21 +0100


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/grotesq/ugqb8a.pfb .
ln -s %{_fontdir}/ugqb8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/grotesq/ugqb8a.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/dvips/grotesq/config.ugq
%{_texdir}/texmf-dist/fonts/afm/urw/grotesq/ugqb8a.afm
%{_texdir}/texmf-dist/fonts/map/dvips/grotesq/ugq.map
%{_texdir}/texmf-dist/fonts/tfm/urw/grotesq/ugqb.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw/grotesq/ugqb7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw/grotesq/ugqb8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw/grotesq/ugqb8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw/grotesq/ugqb8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw/grotesq/ugqb8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw/grotesq/ugqbc7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw/grotesq/ugqbc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw/grotesq/ugqbo7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw/grotesq/ugqbo8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw/grotesq/ugqbo8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw/grotesq/ugqbo8t.tfm
%{_texdir}/texmf-dist/fonts/type1/urw/grotesq/ugqb8a.pfb
%{_texdir}/texmf-dist/fonts/vf/urw/grotesq/ugqb.vf
%{_texdir}/texmf-dist/fonts/vf/urw/grotesq/ugqb7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw/grotesq/ugqb8c.vf
%{_texdir}/texmf-dist/fonts/vf/urw/grotesq/ugqb8t.vf
%{_texdir}/texmf-dist/fonts/vf/urw/grotesq/ugqbc7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw/grotesq/ugqbc8t.vf
%{_texdir}/texmf-dist/fonts/vf/urw/grotesq/ugqbo7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw/grotesq/ugqbo8c.vf
%{_texdir}/texmf-dist/fonts/vf/urw/grotesq/ugqbo8t.vf
%{_texdir}/texmf-dist/tex/latex/grotesq/ot1ugq.fd
%{_texdir}/texmf-dist/tex/latex/grotesq/t1ugq.fd
%{_texdir}/texmf-dist/tex/latex/grotesq/ts1ugq.fd

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/fonts/grotesq/grotesq.txt
%{_texdir}/texmf-dist/doc/fonts/grotesq/readme.grotesq

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/ugqb8a.pfb

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
