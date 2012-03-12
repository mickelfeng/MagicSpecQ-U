%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/gfsartemisia.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/gfsartemisia.doc.tar.xz

Name: texlive-gfsartemisia
License: Freely redistributable without restriction
Summary: A modern Greek font design
Version: %{tl_version}
Release: %{tl_noarch_release}.1.0.svn19469%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(gfsartemisia-euler.sty)
Provides: tex(gfsartemisia.sty)
Requires: tex(euler.sty)
Requires: tex(txfonts.sty)
Requires: texlive-gfsartemisia-fedora-fonts = %{tl_version}

%description
GFS Artemisia is a relatively modern font, designed as a
'general purpose' font in the same sense as Times is nowadays
treated. The present version has been provided by the Greek
Font Society. The font supports the Greek and Latin alphabets.
LaTeX support is provided, using the OT1, T1 and LGR encodings.

date: 2008-08-19 21:00:04 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map gfsartemisia.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map gfsartemisia.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for gfsartemisia
Version: %{tl_version}
Release: %{tl_noarch_release}.1.0.svn19469%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for gfsartemisia

%package fedora-fonts
Summary: Fonts for gfsartemisia
Version: %{tl_version}
Release: %{tl_noarch_release}.1.0.svn19469%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-gfsartemisia = %{tl_version}
BuildArch: noarch

%description fedora-fonts
GFS Artemisia is a relatively modern font, designed as a
'general purpose' font in the same sense as Times is nowadays
treated. The present version has been provided by the Greek
Font Society. The font supports the Greek and Latin alphabets.
LaTeX support is provided, using the OT1, T1 and LGR encodings.

date: 2008-08-19 21:00:04 +0200


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsartemisia/GFSArtemisia.otf .
ln -s %{_fontdir}/GFSArtemisia.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsartemisia/GFSArtemisia.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsartemisia/GFSArtemisiaBold.otf .
ln -s %{_fontdir}/GFSArtemisiaBold.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsartemisia/GFSArtemisiaBold.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsartemisia/GFSArtemisiaBoldIt.otf .
ln -s %{_fontdir}/GFSArtemisiaBoldIt.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsartemisia/GFSArtemisiaBoldIt.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsartemisia/GFSArtemisiaIt.otf .
ln -s %{_fontdir}/GFSArtemisiaIt.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsartemisia/GFSArtemisiaIt.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsartemisia/GFSArtemisia-Bold.pfb .
ln -s %{_fontdir}/GFSArtemisia-Bold.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsartemisia/GFSArtemisia-Bold.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsartemisia/GFSArtemisia-BoldItalic.pfb .
ln -s %{_fontdir}/GFSArtemisia-BoldItalic.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsartemisia/GFSArtemisia-BoldItalic.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsartemisia/GFSArtemisia-Italic.pfb .
ln -s %{_fontdir}/GFSArtemisia-Italic.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsartemisia/GFSArtemisia-Italic.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsartemisia/GFSArtemisia-Regular.pfb .
ln -s %{_fontdir}/GFSArtemisia-Regular.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsartemisia/GFSArtemisia-Regular.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/fonts/afm/public/gfsartemisia/GFSArtemisia-Bold.afm
%{_texdir}/texmf-dist/fonts/afm/public/gfsartemisia/GFSArtemisia-BoldItalic.afm
%{_texdir}/texmf-dist/fonts/afm/public/gfsartemisia/GFSArtemisia-Italic.afm
%{_texdir}/texmf-dist/fonts/afm/public/gfsartemisia/GFSArtemisia-Regular.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsartemisia/artemisia.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsartemisia/artemisiadenomnums.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsartemisia/artemisiaec.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsartemisia/artemisiaecsc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsartemisia/artemisiael.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsartemisia/artemisiaelsc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsartemisia/artemisiamath.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsartemisia/artemisianumnums.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsartemisia/artemisiasc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsartemisia/artemisiatabnums.enc
%{_texdir}/texmf-dist/fonts/map/dvips/gfsartemisia/gfsartemisia.map
%{_texdir}/texmf-dist/fonts/opentype/public/gfsartemisia/GFSArtemisia.otf
%{_texdir}/texmf-dist/fonts/opentype/public/gfsartemisia/GFSArtemisiaBold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/gfsartemisia/GFSArtemisiaBoldIt.otf
%{_texdir}/texmf-dist/fonts/opentype/public/gfsartemisia/GFSArtemisiaIt.otf
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiab8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiab8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiab9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiab9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiabi8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiabi8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiabi9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiabi9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiabo8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiabo8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiabo9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiabo9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiadenomnums8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiadenomnums8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiai8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiai8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiai9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiai9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiamath8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiamath8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisianumnums8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisianumnums8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiao8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiao8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiao9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiao9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiarg8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiarg8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiarg9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiarg9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiasc8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiasc8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiasc9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiasc9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiasco8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiasco8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiasco9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiasco9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiatabnums8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/artemisiatabnums8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/gartemisiab6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/gartemisiab6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/gartemisiabi6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/gartemisiabi6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/gartemisiabo6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/gartemisiabo6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/gartemisiai6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/gartemisiai6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/gartemisiao6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/gartemisiao6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/gartemisiarg6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/gartemisiarg6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/gartemisiasc6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/gartemisiasc6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/gartemisiasco6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/gartemisiasco6r.tfm
%{_texdir}/texmf-dist/fonts/type1/public/gfsartemisia/GFSArtemisia-Bold.pfb
%{_texdir}/texmf-dist/fonts/type1/public/gfsartemisia/GFSArtemisia-BoldItalic.pfb
%{_texdir}/texmf-dist/fonts/type1/public/gfsartemisia/GFSArtemisia-Italic.pfb
%{_texdir}/texmf-dist/fonts/type1/public/gfsartemisia/GFSArtemisia-Regular.pfb
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/artemisiab8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/artemisiab9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/artemisiabi8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/artemisiabi9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/artemisiabo8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/artemisiabo9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/artemisiadenomnums8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/artemisiai8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/artemisiai9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/artemisiamath8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/artemisianumnums8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/artemisiao8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/artemisiao9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/artemisiarg8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/artemisiarg9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/artemisiasc8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/artemisiasc9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/artemisiasco8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/artemisiasco9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/artemisiatabnums8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/gartemisiab6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/gartemisiabi6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/gartemisiabo6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/gartemisiai6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/gartemisiao6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/gartemisiarg6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/gartemisiasc6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/gartemisiasco6a.vf
%{_texdir}/texmf-dist/tex/latex/gfsartemisia/gfsartemisia-euler.sty
%{_texdir}/texmf-dist/tex/latex/gfsartemisia/gfsartemisia.sty
%{_texdir}/texmf-dist/tex/latex/gfsartemisia/lgrartemisia.fd
%{_texdir}/texmf-dist/tex/latex/gfsartemisia/lgrartemisiaeuler.fd
%{_texdir}/texmf-dist/tex/latex/gfsartemisia/ot1artemisia.fd
%{_texdir}/texmf-dist/tex/latex/gfsartemisia/ot1artemisiaeuler.fd
%{_texdir}/texmf-dist/tex/latex/gfsartemisia/t1artemisia.fd
%{_texdir}/texmf-dist/tex/latex/gfsartemisia/t1artemisiaeuler.fd
%{_texdir}/texmf-dist/tex/latex/gfsartemisia/uartemisiaeulernums.fd
%{_texdir}/texmf-dist/tex/latex/gfsartemisia/uartemisianums.fd

%files doc
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/doc/fonts/gfsartemisia/OFL-FAQ.txt
%{_texdir}/texmf-dist/doc/fonts/gfsartemisia/OFL.txt
%{_texdir}/texmf-dist/doc/fonts/gfsartemisia/README
%{_texdir}/texmf-dist/doc/fonts/gfsartemisia/README.TEXLIVE
%{_texdir}/texmf-dist/doc/fonts/gfsartemisia/gfsartemisia.pdf
%{_texdir}/texmf-dist/doc/fonts/gfsartemisia/gfsartemisia.tex

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/GFSArtemisia.otf
%{_fontdir}/GFSArtemisiaBold.otf
%{_fontdir}/GFSArtemisiaBoldIt.otf
%{_fontdir}/GFSArtemisiaIt.otf
%{_fontdir}/GFSArtemisia-Bold.pfb
%{_fontdir}/GFSArtemisia-BoldItalic.pfb
%{_fontdir}/GFSArtemisia-Italic.pfb
%{_fontdir}/GFSArtemisia-Regular.pfb

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
