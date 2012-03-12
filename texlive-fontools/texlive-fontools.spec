%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/fontools.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/fontools.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/fontools.doc.tar.xz

Name: texlive-fontools
License: GPL+
Summary: Tools to simplify using fonts (especially TT/OTF ones)
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19534%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-fontools-bin = %{tl_version}

%description
This package provides a few tools to ease using fonts
(especially Truetype/Opentype ones) with Latex and fontinst:
AFM2AFM - reencode .afm files; designed to replace fontinst's
\reencodefont for big .afm files; AUTOINST - simplify the use
of the LCDF TypeTools by creating a command file for otftotfm,
plus .fd and .sty files; CMAP2ENC - convert glyph indices in
TrueType fonts without glyph names (such as Linotype Palatino)
to Adobe glyph names; FONT2AFM - create font metrics; this is
just a wrapper script around tools such as pf2afm, ttf2afm,
pfm2kpx and ot2kpx; OT2KPX - extract all kerning pairs from an
OpenType font; PFM2KPX - extract all kerning pairs from buggy
.pfm files (the ones where pf2afm complains ".notdef character
occurred among kern pairs"); and SHOWGLYPHS - create a pdf file
that shows all glyphs in a font. Please see the documentation
of the individual programs for further information.

date: 2010-07-19 16:45:16 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
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
Summary: Documentation for fontools
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19534%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for fontools


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/gpl.txt gpl.txt
xz -dc %{SOURCE0} | tar x -C %{buildroot}%{_texdir}
xz -dc %{SOURCE1} | tar x -C %{buildroot}%{_texdir}
xz -dc %{SOURCE2} | tar x -C %{buildroot}%{_texdir}
# nuke useless tlmgr packaging stuff and doc droppings
rm -rf %{buildroot}%{_texdir}/tlpkg/tlpobj/
rm -rf %{buildroot}%{_texdir}/texmf-dist/tlpkg/tlpobj/
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/man*/*.pdf
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/Makefile
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/man*/Makefile
rm -rf %{buildroot}%{_texdir}/texmf/doc/info/dir
mkdir -p %{buildroot}/%{_datadir}/
mv %{buildroot}/%{_texdir}/texmf/doc/man %{buildroot}/%{_datadir}/

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gpl.txt
%{_mandir}/man1/afm2afm.1*
%{_mandir}/man1/autoinst.1*
%{_mandir}/man1/cmap2enc.1*
%{_mandir}/man1/font2afm.1*
%{_mandir}/man1/ot2kpx.1*
%{_mandir}/man1/pfm2kpx.1*
%{_mandir}/man1/showglyphs.1*
%{_texdir}/texmf-dist/fonts/enc/dvips/fontools/fontools_ly1.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/fontools/fontools_ot1.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/fontools/fontools_t1.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/fontools/fontools_ts1.enc
%{_texdir}/texmf-dist/scripts/fontools/afm2afm
%{_texdir}/texmf-dist/scripts/fontools/autoinst
%{_texdir}/texmf-dist/scripts/fontools/cmap2enc
%{_texdir}/texmf-dist/scripts/fontools/font2afm
%{_texdir}/texmf-dist/scripts/fontools/ot2kpx
%{_texdir}/texmf-dist/scripts/fontools/pfm2kpx
%{_texdir}/texmf-dist/scripts/fontools/showglyphs

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/support/fontools/GPLv2.txt
%{_texdir}/texmf-dist/doc/support/fontools/README
%{_texdir}/texmf-dist/doc/support/fontools/examples/berling/berling.sty
%{_texdir}/texmf-dist/doc/support/fontools/examples/berling/berling.sub
%{_texdir}/texmf-dist/doc/support/fontools/examples/berling/makeberling
%{_texdir}/texmf-dist/doc/support/fontools/examples/berling/mbr_fnst.tex
%{_texdir}/texmf-dist/doc/support/fontools/examples/frutiger/frutiger.sty
%{_texdir}/texmf-dist/doc/support/fontools/examples/frutiger/frutiger.sub
%{_texdir}/texmf-dist/doc/support/fontools/examples/frutiger/lfr_fnst.tex
%{_texdir}/texmf-dist/doc/support/fontools/examples/frutiger/makefrutiger
%{_texdir}/texmf-dist/doc/support/fontools/examples/palatinox/Palatino_fnst.tex
%{_texdir}/texmf-dist/doc/support/fontools/examples/palatinox/make_Palatino
%{_texdir}/texmf-dist/doc/support/fontools/examples/palatinox/pala.sub
%{_texdir}/texmf-dist/doc/support/fontools/examples/palatinox/palatinox.sty
%{_texdir}/texmf-dist/doc/support/fontools/examples/palatinox/unsetSCaps.mtx


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
