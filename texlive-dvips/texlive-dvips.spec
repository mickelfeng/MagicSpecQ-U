%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/dvips.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/dvips.doc.tar.xz

Name: texlive-dvips
License: GPL+
Summary: A DVI to PostScript driver
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19496%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires(preun,post): /sbin/install-info
Requires: texlive-dvips-bin = %{tl_version}
Provides: tex(blackdvi.sty)
Provides: tex(colordvi.sty)
Provides: tex(rotate.sty)
Provides: tex(dvips) = %{tl_version}, tetex-dvips = 3.1-99, texlive-dvips = %{tl_version}, texlive-texmf-dvips = %{tl_version}
Obsoletes: tetex-dvips < 3.1-99, texlive-dvips < %{tl_version}, texlive-texmf-dvips < %{tl_version}

%description
This package has been withdrawn from CTAN. The current sources
of dvips may be found in the distribution of dvipsk which forms
part of the TeX-live sources.

date: 2009-11-09 17:50:29 +0100

%preun
if [ "$1" = "0" ]; then
  /sbin/install-info --delete %{_infodir}/dvips.info %{_infodir}/dir 2>/dev/null || :
fi

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
/sbin/install-info %{_infodir}/dvips.info %{_infodir}/dir 2>/dev/null
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
Summary: Documentation for dvips
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19496%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for dvips


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/gpl.txt gpl.txt
xz -dc %{SOURCE0} | tar x -C %{buildroot}%{_texdir}
xz -dc %{SOURCE1} | tar x -C %{buildroot}%{_texdir}
# nuke useless tlmgr packaging stuff and doc droppings
rm -rf %{buildroot}%{_texdir}/tlpkg/tlpobj/
rm -rf %{buildroot}%{_texdir}/texmf-dist/tlpkg/tlpobj/
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/man*/*.pdf
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/Makefile
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/man*/Makefile
rm -rf %{buildroot}%{_texdir}/texmf/doc/info/dir
mkdir -p %{buildroot}/%{_datadir}/
mv %{buildroot}/%{_texdir}/texmf/doc/man %{buildroot}/%{_datadir}/
mkdir -p %{buildroot}/%{_infodir}/
mv %{buildroot}/%{_texdir}/texmf/doc/info/* %{buildroot}/%{_infodir}/

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gpl.txt
%{_mandir}/man1/afm2tfm.1*
%{_mandir}/man1/dvips.1*
%{_infodir}/dvips.info*
%{_texdir}/texmf-dist/dvips/base/ehandler.ps
%{_texdir}/texmf-dist/dvips/base/resolution400.ps
%{_texdir}/texmf-dist/fonts/enc/dvips/base/6w.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/7t.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/8a.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/8r.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/ad.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/ansinew.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/asex.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/asexp.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/dc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/dvips.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/ec.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/extex.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/funky.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/odvips.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/q-cs-uni.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/q-ec-uni.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/q-l7x-uni.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/q-qx-uni.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/q-rm-uni.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/q-t2a-uni.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/q-t2b-uni.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/q-t2c-uni.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/q-t5-uni.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/q-texnansi-uni.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/q-ts1-uni.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/qx.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/stormex.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/tex256.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/texmext.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/texmital.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/texmsym.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/texnansx.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/xl2.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/base/xt2.enc
%{_texdir}/texmf-dist/tex/generic/dvips/blackdvi.sty
%{_texdir}/texmf-dist/tex/generic/dvips/blackdvi.tex
%{_texdir}/texmf-dist/tex/generic/dvips/colordvi.sty
%{_texdir}/texmf-dist/tex/generic/dvips/colordvi.tex
%{_texdir}/texmf-dist/tex/generic/dvips/rotate.sty
%{_texdir}/texmf-dist/tex/generic/dvips/rotate.tex
%{_texdir}/texmf/dvips/base/color.pro
%{_texdir}/texmf/dvips/base/crop.pro
%{_texdir}/texmf/dvips/base/finclude.pro
%{_texdir}/texmf/dvips/base/hps.pro
%{_texdir}/texmf/dvips/base/special.pro
%{_texdir}/texmf/dvips/base/tex.pro
%{_texdir}/texmf/dvips/base/texc.pro
%{_texdir}/texmf/dvips/base/texps.pro
%{_texdir}/texmf/dvips/config/alt-rule.pro
%{_texdir}/texmf/dvips/config/canonex.cfg
%{_texdir}/texmf/dvips/config/config.bakoma
%{_texdir}/texmf/dvips/config/config.canonex
%{_texdir}/texmf/dvips/config/config.cx
%{_texdir}/texmf/dvips/config/config.deskjet
%{_texdir}/texmf/dvips/config/config.dvired
%{_texdir}/texmf/dvips/config/config.epson
%{_texdir}/texmf/dvips/config/config.ibmvga
%{_texdir}/texmf/dvips/config/config.ljfour
%{_texdir}/texmf/dvips/config/config.luc
%{_texdir}/texmf/dvips/config/config.mbn
%{_texdir}/texmf/dvips/config/config.mga
%{_texdir}/texmf/dvips/config/config.mirrorprint
%{_texdir}/texmf/dvips/config/config.ot2
%{_texdir}/texmf/dvips/config/config.ps
%{_texdir}/texmf/dvips/config/config.qms
%{_texdir}/texmf/dvips/config/config.toshiba
%{_texdir}/texmf/dvips/config/config.unms
%{_texdir}/texmf/dvips/config/config.xyp
%{_texdir}/texmf/dvips/config/cx.cfg
%{_texdir}/texmf/dvips/config/deskjet.cfg
%{_texdir}/texmf/dvips/config/dfaxhigh.cfg
%{_texdir}/texmf/dvips/config/dvired.cfg
%{_texdir}/texmf/dvips/config/epson.cfg
%{_texdir}/texmf/dvips/config/ibmvga.cfg
%{_texdir}/texmf/dvips/config/ljfour.cfg
%{_texdir}/texmf/dvips/config/qms.cfg
%{_texdir}/texmf/dvips/config/toshiba.cfg
%{_texdir}/texmf/fonts/map/dvips/updmap/builtin35.map
%{_texdir}/texmf/fonts/map/dvips/updmap/download35.map
%{_texdir}/texmf/fonts/map/dvips/updmap/ps2pk.map
%{_texdir}/texmf/fonts/map/dvips/updmap/psfonts.map
%{_texdir}/texmf/fonts/map/dvips/updmap/psfonts_pk.map
%{_texdir}/texmf/fonts/map/dvips/updmap/psfonts_t1.map

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf/doc/dvips/dvips.html
%{_texdir}/texmf/doc/dvips/dvips.pdf


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
