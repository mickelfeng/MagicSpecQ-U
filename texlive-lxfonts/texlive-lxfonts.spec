%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/lxfonts.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/lxfonts.doc.tar.xz

Name: texlive-lxfonts
License: LPPL
Summary: Set of slide fonts based on CM
Version: %{tl_version}
Release: %{tl_noarch_release}.0.4.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(lxfonts.sty)
Requires: texlive-lxfonts-fedora-fonts = %{tl_version}

%description
The bundle contains the traditional slides fonts revised to be
completely usable both as text fonts and mathematics fonts;
they are fully integrate with the new operators, letters,
symbols and extensible delimiter fonts, as well as with the AMS
fonts, all redone with the same stylistic parameters.

date: 2008-08-22 10:50:40 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "MixedMap lxfonts.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^MixedMap lxfonts.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for lxfonts
Version: %{tl_version}
Release: %{tl_noarch_release}.0.4.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for lxfonts

%package fedora-fonts
Summary: Fonts for lxfonts
Version: %{tl_version}
Release: %{tl_noarch_release}.0.4.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-lxfonts = %{tl_version}
BuildArch: noarch

%description fedora-fonts
The bundle contains the traditional slides fonts revised to be
completely usable both as text fonts and mathematics fonts;
they are fully integrate with the new operators, letters,
symbols and extensible delimiter fonts, as well as with the AMS
fonts, all redone with the same stylistic parameters.

date: 2008-08-22 10:50:40 +0200


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/lcmbsy8.pfb .
ln -s %{_fontdir}/lcmbsy8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/lcmbsy8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/lcmex8.pfb .
ln -s %{_fontdir}/lcmex8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/lcmex8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/lcmmi8.pfb .
ln -s %{_fontdir}/lcmmi8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/lcmmi8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/lcmmib8.pfb .
ln -s %{_fontdir}/lcmmib8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/lcmmib8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/lcmsy8.pfb .
ln -s %{_fontdir}/lcmsy8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/lcmsy8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/leclb8.pfb .
ln -s %{_fontdir}/leclb8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/leclb8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/lecli8.pfb .
ln -s %{_fontdir}/lecli8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/lecli8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/leclo8.pfb .
ln -s %{_fontdir}/leclo8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/leclo8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/leclq8.pfb .
ln -s %{_fontdir}/leclq8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/leclq8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/llasy8.pfb .
ln -s %{_fontdir}/llasy8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/llasy8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/llasyb8.pfb .
ln -s %{_fontdir}/llasyb8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/llasyb8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/llcmss8.pfb .
ln -s %{_fontdir}/llcmss8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/llcmss8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/llcmssb8.pfb .
ln -s %{_fontdir}/llcmssb8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/llcmssb8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/llcmssi8.pfb .
ln -s %{_fontdir}/llcmssi8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/llcmssi8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/llcmsso8.pfb .
ln -s %{_fontdir}/llcmsso8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/llcmsso8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/lmsam8.pfb .
ln -s %{_fontdir}/lmsam8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/lmsam8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/lmsbm8.pfb .
ln -s %{_fontdir}/lmsbm8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/lmsbm8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/ltclb8.pfb .
ln -s %{_fontdir}/ltclb8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/ltclb8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/ltcli8.pfb .
ln -s %{_fontdir}/ltcli8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/ltcli8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/ltclo8.pfb .
ln -s %{_fontdir}/ltclo8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/ltclo8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/ltclq8.pfb .
ln -s %{_fontdir}/ltclq8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/ltclq8.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/fonts/map/dvips/lxfonts/lxfonts.map
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/lamsya.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/lamsyb.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/lasymbols.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/lbigacc.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/lbigdel.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/lbigop.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/lbsymbols.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/lcmbsy8.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/lcmex8.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/lcmmi8.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/lcmmib8.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/lcmsy8.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/leclb8.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/lecli8.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/leclo8.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/leclq8.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/lexroman.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/lexslides.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/llasy.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/llasy8.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/llasyb8.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/llcmss8.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/llcmssb8.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/llcmssi8.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/llcmsso8.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/lmathex.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/lmathit.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/lmathsy.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/lmsam8.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/lmsbm8.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/lroman.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/ltclb8.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/ltcli8.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/ltclo8.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/ltclq8.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/ltxsymb.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/lxbbase.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/lxbbold.mf
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/lxbcaps.mf
%{_texdir}/texmf-dist/fonts/tfm/public/lxfonts/lcmbsy8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lxfonts/lcmex8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lxfonts/lcmmi8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lxfonts/lcmmib8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lxfonts/lcmsy8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lxfonts/leclb8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lxfonts/lecli8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lxfonts/leclo8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lxfonts/leclq8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lxfonts/llasy8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lxfonts/llasyb8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lxfonts/llcmss8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lxfonts/llcmssb8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lxfonts/llcmssi8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lxfonts/llcmsso8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lxfonts/lmsam8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lxfonts/lmsbm8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lxfonts/ltclb8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lxfonts/ltcli8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lxfonts/ltclo8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lxfonts/ltclq8.tfm
%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/lcmbsy8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/lcmex8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/lcmmi8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/lcmmib8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/lcmsy8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/leclb8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/lecli8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/leclo8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/leclq8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/llasy8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/llasyb8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/llcmss8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/llcmssb8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/llcmssi8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/llcmsso8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/lmsam8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/lmsbm8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/ltclb8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/ltcli8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/ltclo8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/ltclq8.pfb
%{_texdir}/texmf-dist/tex/latex/lxfonts/lxfonts.sty

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/fonts/lxfonts/LXfonts-demo.pdf
%{_texdir}/texmf-dist/doc/fonts/lxfonts/LXfonts-demo.tex
%{_texdir}/texmf-dist/doc/fonts/lxfonts/LXfonts.readme
%{_texdir}/texmf-dist/doc/fonts/lxfonts/manifest

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/lcmbsy8.pfb
%{_fontdir}/lcmex8.pfb
%{_fontdir}/lcmmi8.pfb
%{_fontdir}/lcmmib8.pfb
%{_fontdir}/lcmsy8.pfb
%{_fontdir}/leclb8.pfb
%{_fontdir}/lecli8.pfb
%{_fontdir}/leclo8.pfb
%{_fontdir}/leclq8.pfb
%{_fontdir}/llasy8.pfb
%{_fontdir}/llasyb8.pfb
%{_fontdir}/llcmss8.pfb
%{_fontdir}/llcmssb8.pfb
%{_fontdir}/llcmssi8.pfb
%{_fontdir}/llcmsso8.pfb
%{_fontdir}/lmsam8.pfb
%{_fontdir}/lmsbm8.pfb
%{_fontdir}/ltclb8.pfb
%{_fontdir}/ltcli8.pfb
%{_fontdir}/ltclo8.pfb
%{_fontdir}/ltclq8.pfb

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
