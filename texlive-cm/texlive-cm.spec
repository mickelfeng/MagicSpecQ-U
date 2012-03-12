%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cm.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cm.doc.tar.xz

Name: texlive-cm
License: Knuth
Summary: Computer Modern fonts
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}

%description
Knuth's final iteration of his re-interpretation of a c.19
Modern-style font from Monotype. The family is comprehensive,
offering both sans and roman styles, and a monospaced font,
together with mathematics fonts closely integrated with the
mathematical facilities of TeX itself. The base fonts are
distributed as MetaFont source, but autotraced PostScript Type
1 versions are available (one version in the AMS fonts
distribution, and also the BaKoMa distribution). The Computer
Modern fonts have inspired many later families, notably the
European Computer Modern and the Latin Modern families.

date: 2009-07-03 18:23:26 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "MixedMap cmtext-bsr-interpolated.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^MixedMap cmtext-bsr-interpolated.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for cm
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for cm


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/knuth.txt knuth.txt
xz -dc %{SOURCE0} | tar x -C %{buildroot}%{_texdir}/texmf-dist
xz -dc %{SOURCE1} | tar x -C %{buildroot}%{_texdir}/texmf-dist
# nuke useless tlmgr packaging stuff and doc droppings
rm -rf %{buildroot}%{_texdir}/tlpkg/tlpobj/
rm -rf %{buildroot}%{_texdir}/texmf-dist/tlpkg/tlpobj/
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/man*/*.pdf
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/Makefile
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/man*/Makefile
rm -rf %{buildroot}%{_texdir}/texmf/doc/info/dir

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc knuth.txt
%{_texdir}/texmf-dist/fonts/map/dvips/cm/cmtext-bsr-interpolated.map
%{_texdir}/texmf-dist/fonts/pk/ljfour/public/cm/dpi600/cmbx10.pk
%{_texdir}/texmf-dist/fonts/pk/ljfour/public/cm/dpi600/cmex10.pk
%{_texdir}/texmf-dist/fonts/pk/ljfour/public/cm/dpi600/cmmi10.pk
%{_texdir}/texmf-dist/fonts/pk/ljfour/public/cm/dpi600/cmmi7.pk
%{_texdir}/texmf-dist/fonts/pk/ljfour/public/cm/dpi600/cmr10.pk
%{_texdir}/texmf-dist/fonts/pk/ljfour/public/cm/dpi600/cmr12.pk
%{_texdir}/texmf-dist/fonts/pk/ljfour/public/cm/dpi600/cmr17.pk
%{_texdir}/texmf-dist/fonts/pk/ljfour/public/cm/dpi600/cmr6.pk
%{_texdir}/texmf-dist/fonts/pk/ljfour/public/cm/dpi600/cmr7.pk
%{_texdir}/texmf-dist/fonts/pk/ljfour/public/cm/dpi600/cmr8.pk
%{_texdir}/texmf-dist/fonts/pk/ljfour/public/cm/dpi600/cmsl10.pk
%{_texdir}/texmf-dist/fonts/pk/ljfour/public/cm/dpi600/cmsy10.pk
%{_texdir}/texmf-dist/fonts/pk/ljfour/public/cm/dpi600/cmsy7.pk
%{_texdir}/texmf-dist/fonts/pk/ljfour/public/cm/dpi600/cmti10.pk
%{_texdir}/texmf-dist/fonts/source/public/cm/accent.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/bigacc.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/bigdel.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/bigop.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/calu.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmb10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmbase.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmbcsc10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmbsy10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmbtex10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmbtt10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmbtt8.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmbtt9.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmbx10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmbx12.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmbx5.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmbx6.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmbx7.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmbx8.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmbx9.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmbxsl10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmbxti10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmcsc10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmdunh10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmex10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmexb10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmff10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmfi10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmfib8.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cminch.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmitt10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmmi10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmmi12.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmmi5.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmmi6.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmmi7.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmmi8.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmmi9.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmmib10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmplain.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmr10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmr12.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmr17.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmr5.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmr6.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmr7.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmr8.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmr9.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmsl10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmsl12.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmsl8.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmsl9.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmsltt10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmss10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmss12.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmss17.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmss8.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmss9.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmssbx10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmssdc10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmssi10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmssi12.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmssi17.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmssi8.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmssi9.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmssq8.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmssqi8.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmsy10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmsy5.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmsy6.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmsy7.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmsy8.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmsy9.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmtcsc10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmtex10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmtex8.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmtex9.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmti10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmti12.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmti7.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmti8.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmti9.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmtt10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmtt12.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmtt8.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmtt9.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmttb10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmu10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cmvtt10.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/comlig.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/csc.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/cscspu.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/greekl.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/greeku.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/itald.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/italig.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/itall.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/italms.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/italp.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/italsp.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/mathex.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/mathit.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/mathsy.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/olddig.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/punct.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/roman.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/romand.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/romanl.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/romanp.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/romanu.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/romlig.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/romms.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/romspl.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/romspu.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/romsub.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/sym.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/symbol.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/texset.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/textit.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/title.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/tset.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/tsetsl.mf
%{_texdir}/texmf-dist/fonts/source/public/cm/white_setup.mf
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmbcsc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmbsy10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmbx12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmbx5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmbx6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmbx7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmbx8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmbx9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmbxsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmbxti10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmcsc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmdunh10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmex10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmff10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmfi10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmfib8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cminch.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmitt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmmi10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmmi12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmmi5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmmi6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmmi7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmmi8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmmi9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmmib10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmr12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmr17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmr5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmr6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmr7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmr8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmr9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmsl12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmsl8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmsl9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmsltt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmss10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmss12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmss17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmss8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmss9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmssbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmssdc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmssi10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmssi12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmssi17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmssi8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmssi9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmssq8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmssqi8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmsy10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmsy5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmsy6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmsy7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmsy8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmsy9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmtcsc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmtex10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmtex8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmtex9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmti10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmti12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmti7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmti8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmti9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmtt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmtt12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmtt8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmtt9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmu10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cm/cmvtt10.tfm
%{_texdir}/texmf-dist/fonts/pk/ljfour/public/cm/dpi600/black.pk
%{_texdir}/texmf-dist/fonts/pk/ljfour/public/cm/dpi600/gray.pk

%files doc
%defattr(-,root,root)
%doc knuth.txt
%{_texdir}/texmf-dist/doc/fonts/cm/README
%{_texdir}/texmf-dist/doc/fonts/cm/README-cmps.txt


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
