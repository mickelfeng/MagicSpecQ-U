%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/romande.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/romande.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/romande.source.tar.xz

Name: texlive-romande
License: LPPL
Summary: Romande ADF fonts and LaTeX support
Version: %{tl_version}
Release: %{tl_noarch_release}.1.008_v7.svn19537%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(romande.sty)
Requires: tex(xkeyval.sty)
Requires: tex(fontenc.sty)
Requires: tex(textcomp.sty)
Requires: tex(nfssext-cfr.sty)
Requires: texlive-romande-fedora-fonts = %{tl_version}

%description
Romande ADF is a serif font family with oldstyle figures,
designed as a substitute for Times, Tiffany or Caslon. The
family currently includes upright, italic and small-caps shapes
in each of regular and demi-bold weights and an italic script
in regular. The support package renames the fonts according to
the Karl Berry fontname scheme and defines four families. Two
of these primarily provide access to the "standard" or default
characters while the "alternate" families support alternate
characters, additional ligatures and the long s. The included
package files provide access to these features in LaTeX as
explained in the documentation. The LaTeX support requires the
nfssext-cfr and the xkeyval packages.

date: 2010-07-14 23:31:19 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map yrd.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map yrd.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for romande
Version: %{tl_version}
Release: %{tl_noarch_release}.1.008_v7.svn19537%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for romande

%package fedora-fonts
Summary: Fonts for romande
Version: %{tl_version}
Release: %{tl_noarch_release}.1.008_v7.svn19537%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-romande = %{tl_version}
BuildArch: noarch

%description fedora-fonts
Romande ADF is a serif font family with oldstyle figures,
designed as a substitute for Times, Tiffany or Caslon. The
family currently includes upright, italic and small-caps shapes
in each of regular and demi-bold weights and an italic script
in regular. The support package renames the fonts according to
the Karl Berry fontname scheme and defines four families. Two
of these primarily provide access to the "standard" or default
characters while the "alternate" families support alternate
characters, additional ligatures and the long s. The included
package files provide access to these features in LaTeX as
explained in the documentation. The LaTeX support requires the
nfssext-cfr and the xkeyval packages.

date: 2010-07-14 23:31:19 +0200


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrdd8a.pfb .
ln -s %{_fontdir}/yrdd8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrdd8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrddc8a.pfb .
ln -s %{_fontdir}/yrddc8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrddc8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrddi8a.pfb .
ln -s %{_fontdir}/yrddi8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrddi8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrdr8a.pfb .
ln -s %{_fontdir}/yrdr8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrdr8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrdrc8a.pfb .
ln -s %{_fontdir}/yrdrc8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrdrc8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrdri8a.pfb .
ln -s %{_fontdir}/yrdri8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrdri8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrdriw8a.pfb .
ln -s %{_fontdir}/yrdriw8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrdriw8a.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/fonts/afm/arkandis/romande/yrdd8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/romande/yrddc8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/romande/yrddi8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/romande/yrdr8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/romande/yrdrc8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/romande/yrdri8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/romande/yrdriw8a.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/romande/romande-supp.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/romande/t1-romandeadf-alt.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/romande/t1-romandeadf.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/romande/ts1-euro-yrd.enc
%{_texdir}/texmf-dist/fonts/map/dvips/romande/yrd.map
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/s-yrdd.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/s-yrddi.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/s-yrdr.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/s-yrdri.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/s-yrdriw.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/t1-romandeadf-alt-yrdd.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/t1-romandeadf-alt-yrddi.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/t1-romandeadf-alt-yrdr.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/t1-romandeadf-alt-yrdri.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/t1-romandeadf-alt-yrdriw.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/t1-romandeadf-yrdd.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/t1-romandeadf-yrddc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/t1-romandeadf-yrddi.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/t1-romandeadf-yrdr.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/t1-romandeadf-yrdrc.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/t1-romandeadf-yrdri.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/t1-romandeadf-yrdriw.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/ts1-yrdd.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/ts1-yrddi.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/ts1-yrdr.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/ts1-yrdri.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/ts1-yrdriw.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/yrdd8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/yrdd8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/yrdda8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/yrddai8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/yrddc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/yrddi8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/yrddi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/yrdr8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/yrdr8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/yrdra8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/yrdrai8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/yrdraiw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/yrdrc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/yrdri8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/yrdri8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/yrdriw8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/yrdriw8t.tfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrdd8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrdd8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrddc8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrddc8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrddi8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrddi8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrdr8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrdr8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrdrc8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrdrc8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrdri8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrdri8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrdriw8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/yrdriw8a.pfm
%{_texdir}/texmf-dist/fonts/vf/arkandis/romande/yrdd8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/romande/yrdd8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/romande/yrdda8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/romande/yrddai8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/romande/yrddc8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/romande/yrddi8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/romande/yrddi8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/romande/yrdr8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/romande/yrdr8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/romande/yrdra8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/romande/yrdrai8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/romande/yrdraiw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/romande/yrdrc8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/romande/yrdri8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/romande/yrdri8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/romande/yrdriw8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/romande/yrdriw8t.vf
%{_texdir}/texmf-dist/tex/latex/romande/romande.sty
%{_texdir}/texmf-dist/tex/latex/romande/t1yrd.fd
%{_texdir}/texmf-dist/tex/latex/romande/t1yrda.fd
%{_texdir}/texmf-dist/tex/latex/romande/t1yrdaw.fd
%{_texdir}/texmf-dist/tex/latex/romande/t1yrdw.fd
%{_texdir}/texmf-dist/tex/latex/romande/ts1yrd.fd
%{_texdir}/texmf-dist/tex/latex/romande/ts1yrda.fd
%{_texdir}/texmf-dist/tex/latex/romande/ts1yrdaw.fd
%{_texdir}/texmf-dist/tex/latex/romande/ts1yrdw.fd

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/fonts/romande/COPYING
%{_texdir}/texmf-dist/doc/fonts/romande/NOTICE.txt
%{_texdir}/texmf-dist/doc/fonts/romande/README
%{_texdir}/texmf-dist/doc/fonts/romande/manifest.txt
%{_texdir}/texmf-dist/doc/fonts/romande/romandeadf.pdf
%{_texdir}/texmf-dist/doc/fonts/romande/romandeadf.tex

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/yrdd8a.pfb
%{_fontdir}/yrddc8a.pfb
%{_fontdir}/yrddi8a.pfb
%{_fontdir}/yrdr8a.pfb
%{_fontdir}/yrdrc8a.pfb
%{_fontdir}/yrdri8a.pfb
%{_fontdir}/yrdriw8a.pfb

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
