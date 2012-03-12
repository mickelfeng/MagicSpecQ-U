%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/libris.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/libris.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/libris.source.tar.xz

Name: texlive-libris
License: GPL+
Summary: Libris ADF fonts, with LaTeX support
Version: %{tl_version}
Release: %{tl_noarch_release}.1.007.svn19409%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(libris.sty)
Requires: tex(fontenc.sty)
Requires: tex(textcomp.sty)
Requires: tex(nfssext-cfr.sty)
Requires: texlive-libris-fedora-fonts = %{tl_version}

%description
LibrisADF is a sans-serif family designed to mimic Lydian. The
bundle includes: - fonts, in Adobe Type 1, TrueType and
OpenType formats, and - LaTeX support macros, for use with the
Type 1 versions of the fonts. The LaTeX macros depend on the
nfssext-cfr bundle. GPL licensing applies the the fonts
themselves; the support macros are distributed under LPPL
licensing.

date: 2010-07-10 19:16:06 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map yly.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map yly.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for libris
Version: %{tl_version}
Release: %{tl_noarch_release}.1.007.svn19409%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for libris

%package fedora-fonts
Summary: Fonts for libris
Version: %{tl_version}
Release: %{tl_noarch_release}.1.007.svn19409%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-libris = %{tl_version}
BuildArch: noarch

%description fedora-fonts
LibrisADF is a sans-serif family designed to mimic Lydian. The
bundle includes: - fonts, in Adobe Type 1, TrueType and
OpenType formats, and - LaTeX support macros, for use with the
Type 1 versions of the fonts. The LaTeX macros depend on the
nfssext-cfr bundle. GPL licensing applies the the fonts
themselves; the support macros are distributed under LPPL
licensing.

date: 2010-07-10 19:16:06 +0200


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/libris/ylyb8a.pfb .
ln -s %{_fontdir}/ylyb8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/libris/ylyb8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/libris/ylybi8a.pfb .
ln -s %{_fontdir}/ylybi8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/libris/ylybi8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/libris/ylyr8a.pfb .
ln -s %{_fontdir}/ylyr8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/libris/ylyr8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/libris/ylyri8a.pfb .
ln -s %{_fontdir}/ylyri8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/libris/ylyri8a.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/fonts/afm/arkandis/libris/ylyb8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/libris/ylybi8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/libris/ylyr8a.afm
%{_texdir}/texmf-dist/fonts/afm/arkandis/libris/ylyri8a.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/libris/libris-supp.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/libris/t1-cfr-yly.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/libris/ts1-euro-yly.enc
%{_texdir}/texmf-dist/fonts/map/dvips/libris/yly.map
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/ylyb-t1.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/ylyb-ts1.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/ylyb8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/ylyb8s.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/ylyb8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/ylybi-t1.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/ylybi-ts1.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/ylybi8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/ylybi8s.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/ylybi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/ylybiw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/ylybw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/ylyr-t1.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/ylyr-ts1.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/ylyr8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/ylyr8s.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/ylyr8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/ylyri-t1.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/ylyri-ts1.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/ylyri8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/ylyri8s.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/ylyri8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/ylyriw8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/ylyrw8t.tfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/libris/ylyb8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/libris/ylyb8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/libris/ylybi8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/libris/ylybi8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/libris/ylyr8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/libris/ylyr8a.pfm
%{_texdir}/texmf-dist/fonts/type1/arkandis/libris/ylyri8a.pfb
%{_texdir}/texmf-dist/fonts/type1/arkandis/libris/ylyri8a.pfm
%{_texdir}/texmf-dist/fonts/vf/arkandis/libris/ylyb8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/libris/ylyb8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/libris/ylybi8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/libris/ylybi8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/libris/ylybiw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/libris/ylybw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/libris/ylyr8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/libris/ylyr8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/libris/ylyri8c.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/libris/ylyri8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/libris/ylyriw8t.vf
%{_texdir}/texmf-dist/fonts/vf/arkandis/libris/ylyrw8t.vf
%{_texdir}/texmf-dist/tex/latex/libris/libris.sty
%{_texdir}/texmf-dist/tex/latex/libris/t1yly.fd
%{_texdir}/texmf-dist/tex/latex/libris/t1ylyw.fd
%{_texdir}/texmf-dist/tex/latex/libris/ts1yly.fd
%{_texdir}/texmf-dist/tex/latex/libris/ts1ylyw.fd

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/fonts/libris/COPYING
%{_texdir}/texmf-dist/doc/fonts/libris/NOTICE.txt
%{_texdir}/texmf-dist/doc/fonts/libris/README
%{_texdir}/texmf-dist/doc/fonts/libris/librisadf.pdf
%{_texdir}/texmf-dist/doc/fonts/libris/librisadf.tex
%{_texdir}/texmf-dist/doc/fonts/libris/manifest.txt

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/ylyb8a.pfb
%{_fontdir}/ylybi8a.pfb
%{_fontdir}/ylyr8a.pfb
%{_fontdir}/ylyri8a.pfb

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
