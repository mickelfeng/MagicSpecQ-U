%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/skaknew.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/skaknew.doc.tar.xz

Name: texlive-skaknew
License: LPPL
Summary: The skak chess fonts redone in Adobe Type 1
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18651%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-skaknew-fedora-fonts = %{tl_version}

%description
This package offers Adobe Type 1 versions of the fonts provided
as MetaFont source by the skak bundle.

date: 2009-02-21 22:13:29 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map SkakNew.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map SkakNew.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for skaknew
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18651%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for skaknew

%package fedora-fonts
Summary: Fonts for skaknew
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18651%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-skaknew = %{tl_version}
BuildArch: noarch

%description fedora-fonts
This package offers Adobe Type 1 versions of the fonts provided
as MetaFont source by the skak bundle.

date: 2009-02-21 22:13:29 +0100


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

# link installed fonts with Fedora
install -d -m 0755 %{buildroot}%{_fontdir}
pushd %{buildroot}%{_fontdir}
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/skaknew/AlphaDia.otf .
ln -s %{_fontdir}/AlphaDia.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/skaknew/AlphaDia.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/skaknew/SkakNew-Diagram.otf .
ln -s %{_fontdir}/SkakNew-Diagram.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/skaknew/SkakNew-Diagram.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/skaknew/SkakNew-DiagramT.otf .
ln -s %{_fontdir}/SkakNew-DiagramT.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/skaknew/SkakNew-DiagramT.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/skaknew/SkakNew-Figurine.otf .
ln -s %{_fontdir}/SkakNew-Figurine.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/skaknew/SkakNew-Figurine.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/skaknew/SkakNew-FigurineBold.otf .
ln -s %{_fontdir}/SkakNew-FigurineBold.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/skaknew/SkakNew-FigurineBold.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/skaknew/AlphaDia.pfb .
ln -s %{_fontdir}/AlphaDia.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/skaknew/AlphaDia.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/skaknew/SkakNew-Diagram.pfb .
ln -s %{_fontdir}/SkakNew-Diagram.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/skaknew/SkakNew-Diagram.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/skaknew/SkakNew-DiagramT.pfb .
ln -s %{_fontdir}/SkakNew-DiagramT.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/skaknew/SkakNew-DiagramT.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/skaknew/SkakNew-Figurine.pfb .
ln -s %{_fontdir}/SkakNew-Figurine.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/skaknew/SkakNew-Figurine.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/skaknew/SkakNew-FigurineBold.pfb .
ln -s %{_fontdir}/SkakNew-FigurineBold.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/skaknew/SkakNew-FigurineBold.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/fonts/afm/public/skaknew/AlphaDia.afm
%{_texdir}/texmf-dist/fonts/afm/public/skaknew/SkakNew-Diagram.afm
%{_texdir}/texmf-dist/fonts/afm/public/skaknew/SkakNew-DiagramT.afm
%{_texdir}/texmf-dist/fonts/afm/public/skaknew/SkakNew-Figurine.afm
%{_texdir}/texmf-dist/fonts/afm/public/skaknew/SkakNew-FigurineBold.afm
%{_texdir}/texmf-dist/fonts/map/dvips/skaknew/SkakNew.map
%{_texdir}/texmf-dist/fonts/opentype/public/skaknew/AlphaDia.otf
%{_texdir}/texmf-dist/fonts/opentype/public/skaknew/SkakNew-Diagram.otf
%{_texdir}/texmf-dist/fonts/opentype/public/skaknew/SkakNew-DiagramT.otf
%{_texdir}/texmf-dist/fonts/opentype/public/skaknew/SkakNew-Figurine.otf
%{_texdir}/texmf-dist/fonts/opentype/public/skaknew/SkakNew-FigurineBold.otf
%{_texdir}/texmf-dist/fonts/tfm/public/skaknew/AlphaDia.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/skaknew/SkakNew-Diagram.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/skaknew/SkakNew-DiagramT.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/skaknew/SkakNew-Figurine.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/skaknew/SkakNew-FigurineBold.tfm
%{_texdir}/texmf-dist/fonts/type1/public/skaknew/AlphaDia.inf
%{_texdir}/texmf-dist/fonts/type1/public/skaknew/AlphaDia.pfb
%{_texdir}/texmf-dist/fonts/type1/public/skaknew/AlphaDia.pfm
%{_texdir}/texmf-dist/fonts/type1/public/skaknew/SkakNew-Diagram.inf
%{_texdir}/texmf-dist/fonts/type1/public/skaknew/SkakNew-Diagram.pfb
%{_texdir}/texmf-dist/fonts/type1/public/skaknew/SkakNew-Diagram.pfm
%{_texdir}/texmf-dist/fonts/type1/public/skaknew/SkakNew-DiagramT.inf
%{_texdir}/texmf-dist/fonts/type1/public/skaknew/SkakNew-DiagramT.pfb
%{_texdir}/texmf-dist/fonts/type1/public/skaknew/SkakNew-DiagramT.pfm
%{_texdir}/texmf-dist/fonts/type1/public/skaknew/SkakNew-Figurine.inf
%{_texdir}/texmf-dist/fonts/type1/public/skaknew/SkakNew-Figurine.pfb
%{_texdir}/texmf-dist/fonts/type1/public/skaknew/SkakNew-Figurine.pfm
%{_texdir}/texmf-dist/fonts/type1/public/skaknew/SkakNew-FigurineBold.inf
%{_texdir}/texmf-dist/fonts/type1/public/skaknew/SkakNew-FigurineBold.pfb
%{_texdir}/texmf-dist/fonts/type1/public/skaknew/SkakNew-FigurineBold.pfm

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/fonts/skaknew/README
%{_texdir}/texmf-dist/doc/fonts/skaknew/SkakNew.pdf
%{_texdir}/texmf-dist/doc/fonts/skaknew/SkakNew.tex
%{_texdir}/texmf-dist/doc/fonts/skaknew/fonttables.pdf
%{_texdir}/texmf-dist/doc/fonts/skaknew/install.vtex

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/AlphaDia.otf
%{_fontdir}/SkakNew-Diagram.otf
%{_fontdir}/SkakNew-DiagramT.otf
%{_fontdir}/SkakNew-Figurine.otf
%{_fontdir}/SkakNew-FigurineBold.otf
%{_fontdir}/AlphaDia.pfb
%{_fontdir}/SkakNew-Diagram.pfb
%{_fontdir}/SkakNew-DiagramT.pfb
%{_fontdir}/SkakNew-Figurine.pfb
%{_fontdir}/SkakNew-FigurineBold.pfb

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
