%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/mflogo.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/mflogo.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/mflogo.source.tar.xz

Name: texlive-mflogo
License: LPPL
Summary: LaTeX support for MetaFont logo fonts
Version: %{tl_version}
Release: %{tl_noarch_release}.svn17487%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(mflogo.sty)
Requires: texlive-mflogo-fedora-fonts = %{tl_version}

%description
LaTeX package and font definition file to access the Knuthian
mflogo fonts described in 'The MetaFontbook' and to typeset
MetaFont logos in LaTeX documents.

date: 2010-03-14 23:46:18 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "MixedMap mflogo.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^MixedMap mflogo.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for mflogo
Version: %{tl_version}
Release: %{tl_noarch_release}.svn17487%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for mflogo

%package fedora-fonts
Summary: Fonts for mflogo
Version: %{tl_version}
Release: %{tl_noarch_release}.svn17487%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-mflogo = %{tl_version}
BuildArch: noarch

%description fedora-fonts
LaTeX package and font definition file to access the Knuthian
mflogo fonts described in 'The MetaFontbook' and to typeset
MetaFont logos in LaTeX documents.

date: 2010-03-14 23:46:18 +0100


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo/logo10.pfb .
ln -s %{_fontdir}/logo10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo/logo10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo/logo8.pfb .
ln -s %{_fontdir}/logo8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo/logo8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo/logo9.pfb .
ln -s %{_fontdir}/logo9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo/logo9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo/logobf10.pfb .
ln -s %{_fontdir}/logobf10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo/logobf10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo/logod10.pfb .
ln -s %{_fontdir}/logod10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo/logod10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo/logosl10.pfb .
ln -s %{_fontdir}/logosl10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo/logosl10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo/logosl8.pfb .
ln -s %{_fontdir}/logosl8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo/logosl8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo/logosl9.pfb .
ln -s %{_fontdir}/logosl9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo/logosl9.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/fonts/afm/hoekwater/mflogo/logo10.afm
%{_texdir}/texmf-dist/fonts/afm/hoekwater/mflogo/logo8.afm
%{_texdir}/texmf-dist/fonts/afm/hoekwater/mflogo/logo9.afm
%{_texdir}/texmf-dist/fonts/afm/hoekwater/mflogo/logobf10.afm
%{_texdir}/texmf-dist/fonts/afm/hoekwater/mflogo/logod10.afm
%{_texdir}/texmf-dist/fonts/afm/hoekwater/mflogo/logosl10.afm
%{_texdir}/texmf-dist/fonts/afm/hoekwater/mflogo/logosl8.afm
%{_texdir}/texmf-dist/fonts/afm/hoekwater/mflogo/logosl9.afm
%{_texdir}/texmf-dist/fonts/map/dvips/mflogo/mflogo.map
%{_texdir}/texmf-dist/fonts/source/public/mflogo/flogo.mf
%{_texdir}/texmf-dist/fonts/source/public/mflogo/logo.mf
%{_texdir}/texmf-dist/fonts/source/public/mflogo/logo10.mf
%{_texdir}/texmf-dist/fonts/source/public/mflogo/logo8.mf
%{_texdir}/texmf-dist/fonts/source/public/mflogo/logo9.mf
%{_texdir}/texmf-dist/fonts/source/public/mflogo/logobf10.mf
%{_texdir}/texmf-dist/fonts/source/public/mflogo/logod10.mf
%{_texdir}/texmf-dist/fonts/source/public/mflogo/logosl10.mf
%{_texdir}/texmf-dist/fonts/source/public/mflogo/logosl8.mf
%{_texdir}/texmf-dist/fonts/source/public/mflogo/logosl9.mf
%{_texdir}/texmf-dist/fonts/source/public/mflogo/nlogo.mf
%{_texdir}/texmf-dist/fonts/source/public/mflogo/sklogo.mf
%{_texdir}/texmf-dist/fonts/tfm/public/mflogo/logo10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mflogo/logo8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mflogo/logo9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mflogo/logobf10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mflogo/logod10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mflogo/logosl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mflogo/logosl8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/mflogo/logosl9.tfm
%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo/logo10.pfb
%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo/logo8.pfb
%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo/logo9.pfb
%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo/logobf10.pfb
%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo/logod10.pfb
%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo/logosl10.pfb
%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo/logosl8.pfb
%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo/logosl9.pfb
%{_texdir}/texmf-dist/tex/latex/mflogo/mflogo.sty
%{_texdir}/texmf-dist/tex/latex/mflogo/ulogo.fd

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/mflogo/mflogo.pdf

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/logo10.pfb
%{_fontdir}/logo8.pfb
%{_fontdir}/logo9.pfb
%{_fontdir}/logobf10.pfb
%{_fontdir}/logod10.pfb
%{_fontdir}/logosl10.pfb
%{_fontdir}/logosl8.pfb
%{_fontdir}/logosl9.pfb

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
