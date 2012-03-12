%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/gfsbodoni.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/gfsbodoni.doc.tar.xz

Name: texlive-gfsbodoni
License: OFSFLD
Summary: A Greek and Latin font based on Bodoni
Version: %{tl_version}
Release: %{tl_noarch_release}.1.01.svn19440%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(gfsbodoni.sty)
Requires: texlive-gfsbodoni-fedora-fonts = %{tl_version}

%description
Bodoni's Greek fonts in the 18th century broke, for the first
time, with the Byzantine cursive tradition of Greek fonts. GFS
Bodoni resurrects his work for general use. The font family
supports both Greek and Latin letters. LaTeX support of the
fonts is provided, offering OT1, T1 and LGR encodings. The
fonts themselves are provided in Adobe Type 1 and OpenType
formats.

date: 2010-01-18 14:29:22 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map gfsbodoni.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map gfsbodoni.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for gfsbodoni
Version: %{tl_version}
Release: %{tl_noarch_release}.1.01.svn19440%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for gfsbodoni

%package fedora-fonts
Summary: Fonts for gfsbodoni
Version: %{tl_version}
Release: %{tl_noarch_release}.1.01.svn19440%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-gfsbodoni = %{tl_version}
BuildArch: noarch

%description fedora-fonts
Bodoni's Greek fonts in the 18th century broke, for the first
time, with the Byzantine cursive tradition of Greek fonts. GFS
Bodoni resurrects his work for general use. The font family
supports both Greek and Latin letters. LaTeX support of the
fonts is provided, offering OT1, T1 and LGR encodings. The
fonts themselves are provided in Adobe Type 1 and OpenType
formats.

date: 2010-01-18 14:29:22 +0100


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/ofl.txt ofl.txt
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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsbodoni/GFSBodoni.otf .
ln -s %{_fontdir}/GFSBodoni.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsbodoni/GFSBodoni.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsbodoni/GFSBodoniBold.otf .
ln -s %{_fontdir}/GFSBodoniBold.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsbodoni/GFSBodoniBold.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsbodoni/GFSBodoniBoldIt.otf .
ln -s %{_fontdir}/GFSBodoniBoldIt.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsbodoni/GFSBodoniBoldIt.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsbodoni/GFSBodoniIt.otf .
ln -s %{_fontdir}/GFSBodoniIt.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsbodoni/GFSBodoniIt.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsbodoni/GFSBodoni-Bold.pfb .
ln -s %{_fontdir}/GFSBodoni-Bold.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsbodoni/GFSBodoni-Bold.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsbodoni/GFSBodoni-BoldItalic.pfb .
ln -s %{_fontdir}/GFSBodoni-BoldItalic.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsbodoni/GFSBodoni-BoldItalic.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsbodoni/GFSBodoni-Italic.pfb .
ln -s %{_fontdir}/GFSBodoni-Italic.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsbodoni/GFSBodoni-Italic.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsbodoni/GFSBodoni-Regular.pfb .
ln -s %{_fontdir}/GFSBodoni-Regular.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsbodoni/GFSBodoni-Regular.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc ofl.txt
%{_texdir}/texmf-dist/fonts/afm/public/gfsbodoni/GFSBodoni-Bold.afm
%{_texdir}/texmf-dist/fonts/afm/public/gfsbodoni/GFSBodoni-BoldItalic.afm
%{_texdir}/texmf-dist/fonts/afm/public/gfsbodoni/GFSBodoni-Italic.afm
%{_texdir}/texmf-dist/fonts/afm/public/gfsbodoni/GFSBodoni-Regular.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsbodoni/bodoni.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsbodoni/bodonidenomnums.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsbodoni/bodoniec.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsbodoni/bodoniecsc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsbodoni/bodoniel.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsbodoni/bodonielsc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsbodoni/bodoninumnums.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsbodoni/bodonisc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsbodoni/bodonitabnums.enc
%{_texdir}/texmf-dist/fonts/map/dvips/gfsbodoni/gfsbodoni.map
%{_texdir}/texmf-dist/fonts/opentype/public/gfsbodoni/GFSBodoni.otf
%{_texdir}/texmf-dist/fonts/opentype/public/gfsbodoni/GFSBodoniBold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/gfsbodoni/GFSBodoniBoldIt.otf
%{_texdir}/texmf-dist/fonts/opentype/public/gfsbodoni/GFSBodoniIt.otf
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonib8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonib8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonib9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonib9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonibi8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonibi8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonibi9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonibi9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonibo8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonibo8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonibo9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonibo9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonidenomnums8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonidenomnums8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonii8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonii8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonii9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonii9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodoninumnums8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodoninumnums8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonio8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonio8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonio9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonio9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonirg8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonirg8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonirg9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonirg9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonisc8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonisc8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonisc9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonisc9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonisco8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonisco8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonisco9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonisco9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonitabnums8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/bodonitabnums8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/gbodonib6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/gbodonib6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/gbodonibi6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/gbodonibi6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/gbodonibo6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/gbodonibo6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/gbodonii6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/gbodonii6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/gbodonio6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/gbodonio6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/gbodonio9a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/gbodonio9r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/gbodonirg6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/gbodonirg6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/gbodonisc6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/gbodonisc6r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/gbodonisco6a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/gbodonisco6r.tfm
%{_texdir}/texmf-dist/fonts/type1/public/gfsbodoni/GFSBodoni-Bold.pfb
%{_texdir}/texmf-dist/fonts/type1/public/gfsbodoni/GFSBodoni-BoldItalic.pfb
%{_texdir}/texmf-dist/fonts/type1/public/gfsbodoni/GFSBodoni-Italic.pfb
%{_texdir}/texmf-dist/fonts/type1/public/gfsbodoni/GFSBodoni-Regular.pfb
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/bodonib8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/bodonib9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/bodonibi8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/bodonibi9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/bodonibo8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/bodonibo9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/bodonidenomnums8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/bodonii8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/bodonii9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/bodoninumnums8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/bodonio8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/bodonio9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/bodonirg8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/bodonirg9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/bodonisc8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/bodonisc9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/bodonisco8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/bodonisco9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/bodonitabnums8a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/gbodonib6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/gbodonibi6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/gbodonibo6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/gbodonii6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/gbodonio6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/gbodonio9a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/gbodonirg6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/gbodonisc6a.vf
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/gbodonisco6a.vf
%{_texdir}/texmf-dist/tex/latex/gfsbodoni/gfsbodoni.sty
%{_texdir}/texmf-dist/tex/latex/gfsbodoni/lgrbodoni.fd
%{_texdir}/texmf-dist/tex/latex/gfsbodoni/ot1bodoni.fd
%{_texdir}/texmf-dist/tex/latex/gfsbodoni/t1bodoni.fd
%{_texdir}/texmf-dist/tex/latex/gfsbodoni/ubodoninums.fd

%files doc
%defattr(-,root,root)
%doc ofl.txt
%{_texdir}/texmf-dist/doc/fonts/gfsbodoni/OFL-FAQ.txt
%{_texdir}/texmf-dist/doc/fonts/gfsbodoni/OFL.txt
%{_texdir}/texmf-dist/doc/fonts/gfsbodoni/README
%{_texdir}/texmf-dist/doc/fonts/gfsbodoni/README.TEXLIVE
%{_texdir}/texmf-dist/doc/fonts/gfsbodoni/gfsbodoni.pdf

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/GFSBodoni.otf
%{_fontdir}/GFSBodoniBold.otf
%{_fontdir}/GFSBodoniBoldIt.otf
%{_fontdir}/GFSBodoniIt.otf
%{_fontdir}/GFSBodoni-Bold.pfb
%{_fontdir}/GFSBodoni-BoldItalic.pfb
%{_fontdir}/GFSBodoni-Italic.pfb
%{_fontdir}/GFSBodoni-Regular.pfb

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
