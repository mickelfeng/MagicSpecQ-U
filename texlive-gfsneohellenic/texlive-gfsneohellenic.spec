%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/gfsneohellenic.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/gfsneohellenic.doc.tar.xz

Name: texlive-gfsneohellenic
License: Freely redistributable without restriction
Summary: A Greek font in the Neo-Hellenic style
Version: %{tl_version}
Release: %{tl_noarch_release}.1.0_rev.svn19440%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(gfsneohellenic.sty)
Requires: texlive-gfsneohellenic-fedora-fonts = %{tl_version}

%description
The NeoHellenic style evolved in academic circles in the 19th
and 20th century; the present font follows a cut commissioned
from Monotype in 1927. The present version was provided by the
Greek Font Society. The font supports both Greek and Latin
characters, and has been adjusted to work well with the
cmbright fonts for mathematics support. LaTeX support of the
fonts is provided, offering OT1, T1 and LGR encodings.

date: 2009-01-15 17:25:25 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map gfsneohellenic.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map gfsneohellenic.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for gfsneohellenic
Version: %{tl_version}
Release: %{tl_noarch_release}.1.0_rev.svn19440%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for gfsneohellenic

%package fedora-fonts
Summary: Fonts for gfsneohellenic
Version: %{tl_version}
Release: %{tl_noarch_release}.1.0_rev.svn19440%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-gfsneohellenic = %{tl_version}
BuildArch: noarch

%description fedora-fonts
The NeoHellenic style evolved in academic circles in the 19th
and 20th century; the present font follows a cut commissioned
from Monotype in 1927. The present version was provided by the
Greek Font Society. The font supports both Greek and Latin
characters, and has been adjusted to work well with the
cmbright fonts for mathematics support. LaTeX support of the
fonts is provided, offering OT1, T1 and LGR encodings.

date: 2009-01-15 17:25:25 +0100


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsneohellenic/GFSNeohellenic.otf .
ln -s %{_fontdir}/GFSNeohellenic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsneohellenic/GFSNeohellenic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsneohellenic/GFSNeohellenicBold.otf .
ln -s %{_fontdir}/GFSNeohellenicBold.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsneohellenic/GFSNeohellenicBold.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsneohellenic/GFSNeohellenicBoldIt.otf .
ln -s %{_fontdir}/GFSNeohellenicBoldIt.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsneohellenic/GFSNeohellenicBoldIt.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsneohellenic/GFSNeohellenicIt.otf .
ln -s %{_fontdir}/GFSNeohellenicIt.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsneohellenic/GFSNeohellenicIt.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsneohellenic/GFSNeohellenic-Bold.pfb .
ln -s %{_fontdir}/GFSNeohellenic-Bold.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsneohellenic/GFSNeohellenic-Bold.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsneohellenic/GFSNeohellenic-BoldItalic.pfb .
ln -s %{_fontdir}/GFSNeohellenic-BoldItalic.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsneohellenic/GFSNeohellenic-BoldItalic.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsneohellenic/GFSNeohellenic-Italic.pfb .
ln -s %{_fontdir}/GFSNeohellenic-Italic.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsneohellenic/GFSNeohellenic-Italic.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsneohellenic/GFSNeohellenic-Regular.pfb .
ln -s %{_fontdir}/GFSNeohellenic-Regular.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsneohellenic/GFSNeohellenic-Regular.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/fonts/afm/public/gfsneohellenic/GFSNeohellenic-Bold.afm
%{_texdir}/texmf-dist/fonts/afm/public/gfsneohellenic/GFSNeohellenic-BoldItalic.afm
%{_texdir}/texmf-dist/fonts/afm/public/gfsneohellenic/GFSNeohellenic-Italic.afm
%{_texdir}/texmf-dist/fonts/afm/public/gfsneohellenic/GFSNeohellenic-Regular.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsneohellenic/neohellenic.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsneohellenic/neohellenicdenomnums.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsneohellenic/neohellenicec.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsneohellenic/neohellenicecsc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsneohellenic/neohellenicel.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsneohellenic/neohellenicelsc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsneohellenic/neohellenicmath.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsneohellenic/neohellenicnumnums.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsneohellenic/neohellenicsc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsneohellenic/neohellenictabnums.enc
%{_texdir}/texmf-dist/fonts/map/dvips/gfsneohellenic/gfsneohellenic.map
%{_texdir}/texmf-dist/fonts/opentype/public/gfsneohellenic/GFSNeohellenic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/gfsneohellenic/GFSNeohellenicBold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/gfsneohellenic/GFSNeohellenicBoldIt.otf
%{_texdir}/texmf-dist/fonts/opentype/public/gfsneohellenic/GFSNeohellenicIt.otf
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/gfsneohellenicmath8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/gfsneohellenicmath8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/gneohellenicb6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/gneohellenicb6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/gneohellenicbi6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/gneohellenicbi6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/gneohellenicbo6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/gneohellenicbo6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/gneohellenici6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/gneohellenici6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/gneohellenico6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/gneohellenico6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/gneohellenicrg6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/gneohellenicrg6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/gneohellenicsc6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/gneohellenicsc6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/gneohellenicsco6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/gneohellenicsco6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicb8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicb8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicb9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicb9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicbi8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicbi8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicbi9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicbi9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicbo8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicbo8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicbo9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicbo9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicdenomnums8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicdenomnums8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenici8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenici8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenici9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenici9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicnumnums8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicnumnums8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenico8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenico8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenico9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenico9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicrg8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicrg8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicrg9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicrg9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicsc8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicsc8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicsc9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicsc9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicsco8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicsco8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicsco9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenicsco9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenictabnums8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/neohellenictabnums8r.tfm
%{_texdir}/texmf-dist/fonts/type1/public/gfsneohellenic/GFSNeohellenic-Bold.pfb
%{_texdir}/texmf-dist/fonts/type1/public/gfsneohellenic/GFSNeohellenic-BoldItalic.pfb
%{_texdir}/texmf-dist/fonts/type1/public/gfsneohellenic/GFSNeohellenic-Italic.pfb
%{_texdir}/texmf-dist/fonts/type1/public/gfsneohellenic/GFSNeohellenic-Regular.pfb
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/gfsneohellenicmath8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/gneohellenicb6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/gneohellenicbi6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/gneohellenicbo6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/gneohellenici6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/gneohellenico6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/gneohellenicrg6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/gneohellenicsc6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/gneohellenicsco6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/neohellenicb8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/neohellenicb9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/neohellenicbi8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/neohellenicbi9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/neohellenicbo8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/neohellenicbo9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/neohellenicdenomnums8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/neohellenici8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/neohellenici9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/neohellenicnumnums8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/neohellenico8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/neohellenico9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/neohellenicrg8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/neohellenicrg9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/neohellenicsc8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/neohellenicsc9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/neohellenicsco8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/neohellenicsco9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/neohellenictabnums8a.vf
%{_texdir}/texmf-dist/tex/latex/gfsneohellenic/gfsneohellenic.sty
%{_texdir}/texmf-dist/tex/latex/gfsneohellenic/lgrneohellenic.fd
%{_texdir}/texmf-dist/tex/latex/gfsneohellenic/omlneohellenic.fd
%{_texdir}/texmf-dist/tex/latex/gfsneohellenic/ot1neohellenic.fd
%{_texdir}/texmf-dist/tex/latex/gfsneohellenic/t1neohellenic.fd
%{_texdir}/texmf-dist/tex/latex/gfsneohellenic/uneohellenicnums.fd

%files doc
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/doc/fonts/gfsneohellenic/OFL-FAQ.txt
%{_texdir}/texmf-dist/doc/fonts/gfsneohellenic/OFL.txt
%{_texdir}/texmf-dist/doc/fonts/gfsneohellenic/README
%{_texdir}/texmf-dist/doc/fonts/gfsneohellenic/README.TEXLIVE
%{_texdir}/texmf-dist/doc/fonts/gfsneohellenic/gfsneohellenic.pdf
%{_texdir}/texmf-dist/doc/fonts/gfsneohellenic/gfsneohellenic.tex

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/GFSNeohellenic.otf
%{_fontdir}/GFSNeohellenicBold.otf
%{_fontdir}/GFSNeohellenicBoldIt.otf
%{_fontdir}/GFSNeohellenicIt.otf
%{_fontdir}/GFSNeohellenic-Bold.pfb
%{_fontdir}/GFSNeohellenic-BoldItalic.pfb
%{_fontdir}/GFSNeohellenic-Italic.pfb
%{_fontdir}/GFSNeohellenic-Regular.pfb

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
