%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/wasy.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/wasy.doc.tar.xz

Name: texlive-wasy
License: Public Domain
Summary: The wasy fonts (Waldi symbol fonts)
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-wasy-fedora-fonts = %{tl_version}

%description
These are the wasy (Waldi symbol) fonts, second release. This
bundle presents the fonts in MetaFont format, but they are also
available in Adobe Type 1 format. Support under LaTeX is
provided by the wasysym package.

date: 2006-09-12 08:29:26 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "MixedMap wasy.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^MixedMap wasy.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for wasy
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for wasy

%package fedora-fonts
Summary: Fonts for wasy
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-wasy = %{tl_version}
BuildArch: noarch

%description fedora-fonts
These are the wasy (Waldi symbol) fonts, second release. This
bundle presents the fonts in MetaFont format, but they are also
available in Adobe Type 1 format. Support under LaTeX is
provided by the wasysym package.

date: 2006-09-12 08:29:26 +0200


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/pd.txt pd.txt
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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasy10.pfb .
ln -s %{_fontdir}/wasy10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasy10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasy5.pfb .
ln -s %{_fontdir}/wasy5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasy5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasy6.pfb .
ln -s %{_fontdir}/wasy6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasy6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasy7.pfb .
ln -s %{_fontdir}/wasy7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasy7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasy8.pfb .
ln -s %{_fontdir}/wasy8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasy8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasy9.pfb .
ln -s %{_fontdir}/wasy9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasy9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasyb10.pfb .
ln -s %{_fontdir}/wasyb10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasyb10.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc pd.txt
%{_texdir}/texmf-dist/fonts/afm/public/wasy/wasy10.afm
%{_texdir}/texmf-dist/fonts/afm/public/wasy/wasy5.afm
%{_texdir}/texmf-dist/fonts/afm/public/wasy/wasy6.afm
%{_texdir}/texmf-dist/fonts/afm/public/wasy/wasy7.afm
%{_texdir}/texmf-dist/fonts/afm/public/wasy/wasy8.afm
%{_texdir}/texmf-dist/fonts/afm/public/wasy/wasy9.afm
%{_texdir}/texmf-dist/fonts/afm/public/wasy/wasyb10.afm
%{_texdir}/texmf-dist/fonts/map/dvips/wasy/wasy.map
%{_texdir}/texmf-dist/fonts/source/public/wasy/lasychr.mf
%{_texdir}/texmf-dist/fonts/source/public/wasy/rsym.mf
%{_texdir}/texmf-dist/fonts/source/public/wasy/wasy10.mf
%{_texdir}/texmf-dist/fonts/source/public/wasy/wasy5.mf
%{_texdir}/texmf-dist/fonts/source/public/wasy/wasy6.mf
%{_texdir}/texmf-dist/fonts/source/public/wasy/wasy7.mf
%{_texdir}/texmf-dist/fonts/source/public/wasy/wasy8.mf
%{_texdir}/texmf-dist/fonts/source/public/wasy/wasy9.mf
%{_texdir}/texmf-dist/fonts/source/public/wasy/wasyb10.mf
%{_texdir}/texmf-dist/fonts/source/public/wasy/wasychr.mf
%{_texdir}/texmf-dist/fonts/tfm/public/wasy/wasy10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/wasy/wasy5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/wasy/wasy6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/wasy/wasy7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/wasy/wasy8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/wasy/wasy9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/wasy/wasyb10.tfm
%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasy10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasy10.pfm
%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasy5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasy5.pfm
%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasy6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasy6.pfm
%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasy7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasy7.pfm
%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasy8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasy8.pfm
%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasy9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasy9.pfm
%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasyb10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/wasy/wasyb10.pfm
%{_texdir}/texmf-dist/tex/plain/wasy/wasyfont.tex

%files doc
%defattr(-,root,root)
%doc pd.txt
%{_texdir}/texmf-dist/doc/fonts/wasy/README
%{_texdir}/texmf-dist/doc/fonts/wasy/legal.txt
%{_texdir}/texmf-dist/doc/fonts/wasy/wasydoc.pdf
%{_texdir}/texmf-dist/doc/fonts/wasy/wasydoc.tex
%{_texdir}/texmf-dist/doc/fonts/wasy/wasyfont.2

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/wasy10.pfb
%{_fontdir}/wasy5.pfb
%{_fontdir}/wasy6.pfb
%{_fontdir}/wasy7.pfb
%{_fontdir}/wasy8.pfb
%{_fontdir}/wasy9.pfb
%{_fontdir}/wasyb10.pfb

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
