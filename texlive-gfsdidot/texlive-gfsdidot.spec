%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/gfsdidot.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/gfsdidot.doc.tar.xz

Name: texlive-gfsdidot
License: Freely redistributable without restriction
Summary: A Greek font based on Didot's work
Version: %{tl_version}
Release: %{tl_noarch_release}.1.0.svn19469%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(gfsdidot.sty)
Requires: tex(pxfonts.sty)
Requires: texlive-gfsdidot-fedora-fonts = %{tl_version}

%description
The design of Didot's 1805 Greek typeface was influenced by the
neoclassical ideals of the late 18th century. The font was
brought to Greece at the time of the 1821 Greek Revolution, by
Didot's son, and was very widely used. The present version is
provided by the Greek Font Society. The font supports the Greek
alphabet, and is accompanied by a matching Latin alphabet based
on Zapf's Palatino. LaTeX support is provided, using the OT1,
T1 and LGR encodings.

date: 2008-08-19 21:00:04 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map gfsdidot.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map gfsdidot.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for gfsdidot
Version: %{tl_version}
Release: %{tl_noarch_release}.1.0.svn19469%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for gfsdidot

%package fedora-fonts
Summary: Fonts for gfsdidot
Version: %{tl_version}
Release: %{tl_noarch_release}.1.0.svn19469%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-gfsdidot = %{tl_version}
BuildArch: noarch

%description fedora-fonts
The design of Didot's 1805 Greek typeface was influenced by the
neoclassical ideals of the late 18th century. The font was
brought to Greece at the time of the 1821 Greek Revolution, by
Didot's son, and was very widely used. The present version is
provided by the Greek Font Society. The font supports the Greek
alphabet, and is accompanied by a matching Latin alphabet based
on Zapf's Palatino. LaTeX support is provided, using the OT1,
T1 and LGR encodings.

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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsdidot/GFSDidot.otf .
ln -s %{_fontdir}/GFSDidot.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsdidot/GFSDidot.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsdidot/GFSDidotBold.otf .
ln -s %{_fontdir}/GFSDidotBold.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsdidot/GFSDidotBold.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsdidot/GFSDidotBoldItalic.otf .
ln -s %{_fontdir}/GFSDidotBoldItalic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsdidot/GFSDidotBoldItalic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsdidot/GFSDidotItalic.otf .
ln -s %{_fontdir}/GFSDidotItalic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsdidot/GFSDidotItalic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsdidot/GFSOlga.otf .
ln -s %{_fontdir}/GFSOlga.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsdidot/GFSOlga.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsdidot/GFSDidot-Bold.pfb .
ln -s %{_fontdir}/GFSDidot-Bold.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsdidot/GFSDidot-Bold.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsdidot/GFSDidot-BoldItalic.pfb .
ln -s %{_fontdir}/GFSDidot-BoldItalic.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsdidot/GFSDidot-BoldItalic.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsdidot/GFSDidot-Italic.pfb .
ln -s %{_fontdir}/GFSDidot-Italic.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsdidot/GFSDidot-Italic.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsdidot/GFSDidot.pfb .
ln -s %{_fontdir}/GFSDidot.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsdidot/GFSDidot.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsdidot/GFSOlga.pfb .
ln -s %{_fontdir}/GFSOlga.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsdidot/GFSOlga.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/fonts/afm/public/gfsdidot/GFSDidot-Bold.afm
%{_texdir}/texmf-dist/fonts/afm/public/gfsdidot/GFSDidot-BoldItalic.afm
%{_texdir}/texmf-dist/fonts/afm/public/gfsdidot/GFSDidot-Italic.afm
%{_texdir}/texmf-dist/fonts/afm/public/gfsdidot/GFSDidot.afm
%{_texdir}/texmf-dist/fonts/afm/public/gfsdidot/GFSOlga.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsdidot/didot.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsdidot/didotdenomnums.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsdidot/didotec.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsdidot/didotnumnums.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsdidot/didottabnums.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsdidot/didotuecsc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsdidot/didotusc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsdidot/gfsudidotmath.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsdidot/gpdidot.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsdidot/gpdidoti.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsdidot/gpdidotusc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsdidot/gpolga.enc
%{_texdir}/texmf-dist/fonts/map/dvips/gfsdidot/gfsdidot.map
%{_texdir}/texmf-dist/fonts/opentype/public/gfsdidot/GFSDidot.otf
%{_texdir}/texmf-dist/fonts/opentype/public/gfsdidot/GFSDidotBold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/gfsdidot/GFSDidotBoldItalic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/gfsdidot/GFSDidotItalic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/gfsdidot/GFSOlga.otf
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotb8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotb8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotb9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotb9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotbi8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotbi8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotbi9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotbi9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotbo8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotbo8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotbo9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotbo9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotdenomnums8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotdenomnums8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didoti8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didoti8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didoti9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didoti9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotnumnums8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotnumnums8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didoto8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didoto8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didoto9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didoto9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotrg8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotrg8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotrg9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotrg9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotsc8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotsc8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotsc9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotsc9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotsco8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotsco8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotsco9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotsco9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didottabnums8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didottabnums8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotui8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotui8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotui9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/didotui9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/gdidotb6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/gdidotb6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/gdidotbi6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/gdidotbi6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/gdidoti6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/gdidoti6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/gdidotrg6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/gdidotrg6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/gdidotsc6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/gdidotsc6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/gdidotsco6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/gdidotsco6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/gfsudidotmath8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/gfsudidotmath8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/golgai6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/golgai6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/golgaui6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/golgaui6r.tfm
%{_texdir}/texmf-dist/fonts/type1/public/gfsdidot/GFSDidot-Bold.pfb
%{_texdir}/texmf-dist/fonts/type1/public/gfsdidot/GFSDidot-BoldItalic.pfb
%{_texdir}/texmf-dist/fonts/type1/public/gfsdidot/GFSDidot-Italic.pfb
%{_texdir}/texmf-dist/fonts/type1/public/gfsdidot/GFSDidot.pfb
%{_texdir}/texmf-dist/fonts/type1/public/gfsdidot/GFSOlga.pfb
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/didotb8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/didotb9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/didotbi8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/didotbi9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/didotbo8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/didotbo9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/didotdenomnums8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/didoti8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/didoti9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/didotnumnums8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/didoto8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/didoto9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/didotrg8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/didotrg9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/didotsc8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/didotsc9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/didotsco8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/didotsco9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/didottabnums8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/didotui8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/didotui9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/gdidotb6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/gdidotbi6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/gdidoti6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/gdidotrg6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/gdidotsc6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/gdidotsco6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/gfsudidotmath8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/golgai6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/golgaui6a.vf
%{_texdir}/texmf-dist/tex/latex/gfsdidot/gfsdidot.sty
%{_texdir}/texmf-dist/tex/latex/gfsdidot/lgrudidot.fd
%{_texdir}/texmf-dist/tex/latex/gfsdidot/omludidot.fd
%{_texdir}/texmf-dist/tex/latex/gfsdidot/ot1udidot.fd
%{_texdir}/texmf-dist/tex/latex/gfsdidot/t1udidot.fd
%{_texdir}/texmf-dist/tex/latex/gfsdidot/uudidotnums.fd

%files doc
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/doc/fonts/gfsdidot/OFL-FAQ.txt
%{_texdir}/texmf-dist/doc/fonts/gfsdidot/OFL.txt
%{_texdir}/texmf-dist/doc/fonts/gfsdidot/README
%{_texdir}/texmf-dist/doc/fonts/gfsdidot/README.TEXLIVE
%{_texdir}/texmf-dist/doc/fonts/gfsdidot/gfsdidot.pdf
%{_texdir}/texmf-dist/doc/fonts/gfsdidot/gfsdidot.tex

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/GFSDidot.otf
%{_fontdir}/GFSDidotBold.otf
%{_fontdir}/GFSDidotBoldItalic.otf
%{_fontdir}/GFSDidotItalic.otf
%{_fontdir}/GFSOlga.otf
%{_fontdir}/GFSDidot-Bold.pfb
%{_fontdir}/GFSDidot-BoldItalic.pfb
%{_fontdir}/GFSDidot-Italic.pfb
%{_fontdir}/GFSDidot.pfb
%{_fontdir}/GFSOlga.pfb

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
