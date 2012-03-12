%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/ibygrk.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/ibygrk.doc.tar.xz

Name: texlive-ibygrk
License: GPL+
Summary: Fonts and macros to typeset ancient Greek
Version: %{tl_version}
Release: %{tl_noarch_release}.4.5.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(ibycus4.sty)
Provides: tex(psibycus.sty)
Requires: texlive-ibygrk-fedora-fonts = %{tl_version}

%description
Ibycus is a Greek typeface, based on Silvio Levy's realisation
of a classic Didot cut of Greek type from around 1800. The
fonts are available both as MetaFont source and in Adobe Type 1
format. This distribution of ibycus is accompanied by a set of
macro packages to use it with Plain TeX or LaTeX, but for use
with Babel, see the ibycus-babel package.

date: 2007-07-29 11:26:52 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "MixedMap iby.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^MixedMap iby.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for ibygrk
Version: %{tl_version}
Release: %{tl_noarch_release}.4.5.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for ibygrk

%package fedora-fonts
Summary: Fonts for ibygrk
Version: %{tl_version}
Release: %{tl_noarch_release}.4.5.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-ibygrk = %{tl_version}
BuildArch: noarch

%description fedora-fonts
Ibycus is a Greek typeface, based on Silvio Levy's realisation
of a classic Didot cut of Greek type from around 1800. The
fonts are available both as MetaFont source and in Adobe Type 1
format. This distribution of ibycus is accompanied by a set of
macro packages to use it with Plain TeX or LaTeX, but for use
with Babel, see the ibycus-babel package.

date: 2007-07-29 11:26:52 +0200


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ibygrk/fibb84.pfb .
ln -s %{_fontdir}/fibb84.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ibygrk/fibb84.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ibygrk/fibr84.pfb .
ln -s %{_fontdir}/fibr84.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ibygrk/fibr84.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/fonts/afm/public/ibygrk/fibb84.afm
%{_texdir}/texmf-dist/fonts/afm/public/ibygrk/fibr84.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/ibygrk/IbycusHTG.enc
%{_texdir}/texmf-dist/fonts/map/dvips/ibygrk/iby.map
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/abary4.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/cigma4.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/digamma4.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/ebary4.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/fibb84.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/fibb848.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/fibb849.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/fibo84.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/fibo848.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/fibo849.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/fibr84.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/fibr848.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/fibr849.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/hbary4.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/ibary4.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/ibyacc4.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/ibycus4.map
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/ibycus4.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/ibylig4.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/ibylwr4.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/ibypnct4.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/ibyupr4.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/koppa4.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/obary4.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/sampi4.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/ubary4.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/version4.mf
%{_texdir}/texmf-dist/fonts/source/public/ibygrk/wbary4.mf
%{_texdir}/texmf-dist/fonts/tfm/public/ibygrk/fibb84.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ibygrk/fibb848.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ibygrk/fibb849.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ibygrk/fibo84.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ibygrk/fibo848.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ibygrk/fibo849.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ibygrk/fibr84.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ibygrk/fibr848.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ibygrk/fibr849.tfm
%{_texdir}/texmf-dist/fonts/type1/public/ibygrk/fibb84.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ibygrk/fibr84.pfb
%{_texdir}/texmf-dist/tex/generic/ibygrk/Uibycus.fd
%{_texdir}/texmf-dist/tex/generic/ibygrk/Uibycus4.fd
%{_texdir}/texmf-dist/tex/generic/ibygrk/iby4extr.tex
%{_texdir}/texmf-dist/tex/generic/ibygrk/ibycus4.map
%{_texdir}/texmf-dist/tex/generic/ibygrk/ibycus4.sty
%{_texdir}/texmf-dist/tex/generic/ibygrk/ibycus4.tex
%{_texdir}/texmf-dist/tex/generic/ibygrk/ibycusps.tex
%{_texdir}/texmf-dist/tex/generic/ibygrk/psibycus.sty
%{_texdir}/texmf-dist/tex/generic/ibygrk/pssetiby.tex
%{_texdir}/texmf-dist/tex/generic/ibygrk/setiby4.tex
%{_texdir}/texmf-dist/tex/generic/ibygrk/tlgsqq.tex
%{_texdir}/texmf-dist/tex/generic/ibygrk/version4.tex

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/fonts/ibygrk/COPYING
%{_texdir}/texmf-dist/doc/fonts/ibygrk/NEWS
%{_texdir}/texmf-dist/doc/fonts/ibygrk/README
%{_texdir}/texmf-dist/doc/fonts/ibygrk/README.ibycus4
%{_texdir}/texmf-dist/doc/fonts/ibygrk/iby4text.tex
%{_texdir}/texmf-dist/doc/fonts/ibygrk/ibycus3.RME
%{_texdir}/texmf-dist/doc/fonts/ibygrk/ibycus4.ltx
%{_texdir}/texmf-dist/doc/fonts/ibygrk/psibycus.ltx
%{_texdir}/texmf-dist/doc/fonts/ibygrk/psibycus.tex

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/fibb84.pfb
%{_fontdir}/fibr84.pfb

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
