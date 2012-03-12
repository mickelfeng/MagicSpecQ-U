%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/gothic.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/gothic.doc.tar.xz

Name: texlive-gothic
License: Public Domain
Summary: A collection of old German-style fonts
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-gothic-fedora-fonts = %{tl_version}

%description
A collection of fonts that reproduce those used in "old German"
printing. The set comprises Gothic, Schwabacher and Fraktur
fonts, a pair of handwriting fonts, Suetterlin and Schwell, and
a font containing decorative initials. In addition, there are
two re-encoding packages for Haralambous's fonts, providing T1,
using virtual fonts, and OT1 and T1, using Metafont.

date: 2009-01-16 17:12:15 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map yfrak.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map yfrak.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for gothic
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for gothic

%package fedora-fonts
Summary: Fonts for gothic
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-gothic = %{tl_version}
BuildArch: noarch

%description fedora-fonts
A collection of fonts that reproduce those used in "old German"
printing. The set comprises Gothic, Schwabacher and Fraktur
fonts, a pair of handwriting fonts, Suetterlin and Schwell, and
a font containing decorative initials. In addition, there are
two re-encoding packages for Haralambous's fonts, providing T1,
using virtual fonts, and OT1 and T1, using Metafont.

date: 2009-01-16 17:12:15 +0100


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/collection.txt collection.txt
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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gothic/yfrak.pfb .
ln -s %{_fontdir}/yfrak.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gothic/yfrak.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gothic/ygoth.pfb .
ln -s %{_fontdir}/ygoth.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gothic/ygoth.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gothic/yswab.pfb .
ln -s %{_fontdir}/yswab.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gothic/yswab.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc collection.txt
%{_texdir}/texmf-dist/dvips/gothic/config.yfrak
%{_texdir}/texmf-dist/fonts/afm/public/gothic/yfrak.afm
%{_texdir}/texmf-dist/fonts/afm/public/gothic/ygoth.afm
%{_texdir}/texmf-dist/fonts/afm/public/gothic/yswab.afm
%{_texdir}/texmf-dist/fonts/map/dvips/gothic/yfrak.map
%{_texdir}/texmf-dist/fonts/source/public/gothic/cmfrabase.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/cmfrak.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/cmfraklow.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/cmfrakmis.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/cmfraknum.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/cmfrakoth.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/cmfrakupp.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/schwell.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/su-lig.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/su-low.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/su-spec.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/su-upp.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/suet14.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/xxfrak.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yfrabase.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yfrak.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yfraklow.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yfrakmis.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yfraknum.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yfrakoth.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yfrakupp.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/ygotbase.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/ygoth.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/ygothgen.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/ygothlig.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/ygothlow.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/ygothmis.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/ygothnum.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/ygothupp.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinit.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitA.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitB.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitC.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitD.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitE.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitF.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitG.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitH.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitJ.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitK.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitL.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitM.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitN.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitO.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitP.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitQ.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitR.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitS.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitT.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitU.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitV.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitW.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitX.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitY.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitZ.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitas.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yinitdd.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yintbase.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/ysmfrak.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yswab.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yswabase.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yswablow.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yswabmis.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yswabnum.mf
%{_texdir}/texmf-dist/fonts/source/public/gothic/yswabupp.mf
%{_texdir}/texmf-dist/fonts/tfm/public/gothic/cmfrak.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gothic/schwell.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gothic/suet14.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gothic/tfrak.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gothic/tfrakls.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gothic/tgoth.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gothic/tswab.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gothic/yfrak.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gothic/ygoth.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gothic/yinit.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gothic/yinitas.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gothic/yinitdd.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gothic/yswab.tfm
%{_texdir}/texmf-dist/fonts/type1/public/gothic/yfrak.pfb
%{_texdir}/texmf-dist/fonts/type1/public/gothic/ygoth.pfb
%{_texdir}/texmf-dist/fonts/type1/public/gothic/yswab.pfb
%{_texdir}/texmf-dist/fonts/vf/public/gothic/tfrak.vf
%{_texdir}/texmf-dist/fonts/vf/public/gothic/tfrakls.vf
%{_texdir}/texmf-dist/fonts/vf/public/gothic/tgoth.vf
%{_texdir}/texmf-dist/fonts/vf/public/gothic/tswab.vf

%files doc
%defattr(-,root,root)
%doc collection.txt
%{_texdir}/texmf-dist/doc/fonts/gothic/README

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/yfrak.pfb
%{_fontdir}/ygoth.pfb
%{_fontdir}/yswab.pfb

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
