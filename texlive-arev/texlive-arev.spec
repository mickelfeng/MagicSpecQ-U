%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/arev.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/arev.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/arev.source.tar.xz

Name: texlive-arev
License: LPPL
Summary: Fonts and LaTeX support files for Arev Sans
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(ams-mdbch.sty)
Provides: tex(arev.sty)
Provides: tex(arevmath.sty)
Provides: tex(arevtext.sty)
Requires: tex(amssymb.sty)
Requires: tex(amsfonts.sty)
Requires: tex(beramono.sty)
Requires: tex(ifthen.sty)
Requires: tex(fontenc.sty)
Requires: tex(textcomp.sty)
Requires: texlive-arev-fedora-fonts = %{tl_version}

%description
The package arev provides type 1 and virtual fonts, together
with LaTeX packages for using Arev Sans in both text and
mathematics. Arev Sans is a derivative of Bitstream Vera Sans
created by Tavmjong Bah, adding support for Greek and Cyrillic
characters. Bah also added a few variant letters that are more
appropriate for mathematics. The primary purpose for using Arev
Sans in LaTeX is presentations, particularly when using a
computer projector. In such a context, Arev Sans is quite
readable, with large x-height, "open letters", wide spacing,
and thick stems. The style is very similar to the SliTeX font
lcmss, but heavier. Arev is one of a very small number of sans-
font mathematics support packages. Others are cmbright, hvmath
and kerkis.

date: 2007-02-25 15:08:52 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map arev.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map arev.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for arev
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for arev

%package fedora-fonts
Summary: Fonts for arev
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-arev = %{tl_version}
BuildArch: noarch

%description fedora-fonts
The package arev provides type 1 and virtual fonts, together
with LaTeX packages for using Arev Sans in both text and
mathematics. Arev Sans is a derivative of Bitstream Vera Sans
created by Tavmjong Bah, adding support for Greek and Cyrillic
characters. Bah also added a few variant letters that are more
appropriate for mathematics. The primary purpose for using Arev
Sans in LaTeX is presentations, particularly when using a
computer projector. In such a context, Arev Sans is quite
readable, with large x-height, "open letters", wide spacing,
and thick stems. The style is very similar to the SliTeX font
lcmss, but heavier. Arev is one of a very small number of sans-
font mathematics support packages. Others are cmbright, hvmath
and kerkis.

date: 2007-02-25 15:08:52 +0100


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/arev/ArevSans-Bold.pfb .
ln -s %{_fontdir}/ArevSans-Bold.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/arev/ArevSans-Bold.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/arev/ArevSans-BoldOblique.pfb .
ln -s %{_fontdir}/ArevSans-BoldOblique.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/arev/ArevSans-BoldOblique.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/arev/ArevSans-Oblique.pfb .
ln -s %{_fontdir}/ArevSans-Oblique.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/arev/ArevSans-Oblique.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/arev/ArevSans-Roman.pfb .
ln -s %{_fontdir}/ArevSans-Roman.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/arev/ArevSans-Roman.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/fonts/afm/public/arev/ArevSans-Bold.afm
%{_texdir}/texmf-dist/fonts/afm/public/arev/ArevSans-BoldOblique.afm
%{_texdir}/texmf-dist/fonts/afm/public/arev/ArevSans-Oblique.afm
%{_texdir}/texmf-dist/fonts/afm/public/arev/ArevSans-Roman.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/arev/arevoml.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/arev/arevoms.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/arev/arevot1.enc
%{_texdir}/texmf-dist/fonts/map/dvips/arev/arev.map
%{_texdir}/texmf-dist/fonts/tfm/public/arev/ArevSans-Bold.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arev/ArevSans-BoldOblique.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arev/ArevSans-Oblique.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arev/ArevSans-Roman.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arev/favb8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arev/favb8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arev/favbi8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arev/favbi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arev/favmb7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arev/favmbi7m.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arev/favmr7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arev/favmr7y.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arev/favmri7m.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arev/favr8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arev/favr8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arev/favri8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arev/favri8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arev/zavmb7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arev/zavmbi7m.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arev/zavmr7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arev/zavmr7y.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arev/zavmri7m.tfm
%{_texdir}/texmf-dist/fonts/type1/public/arev/ArevSans-Bold.pfb
%{_texdir}/texmf-dist/fonts/type1/public/arev/ArevSans-BoldOblique.pfb
%{_texdir}/texmf-dist/fonts/type1/public/arev/ArevSans-Oblique.pfb
%{_texdir}/texmf-dist/fonts/type1/public/arev/ArevSans-Roman.pfb
%{_texdir}/texmf-dist/fonts/vf/public/arev/favb8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/arev/favbi8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/arev/favr8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/arev/favri8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/arev/zavmb7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/arev/zavmbi7m.vf
%{_texdir}/texmf-dist/fonts/vf/public/arev/zavmr7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/arev/zavmr7y.vf
%{_texdir}/texmf-dist/fonts/vf/public/arev/zavmri7m.vf
%{_texdir}/texmf-dist/tex/latex/arev/ams-mdbch.sty
%{_texdir}/texmf-dist/tex/latex/arev/arev.sty
%{_texdir}/texmf-dist/tex/latex/arev/arevmath.sty
%{_texdir}/texmf-dist/tex/latex/arev/arevsymbols.tex
%{_texdir}/texmf-dist/tex/latex/arev/arevtext.sty
%{_texdir}/texmf-dist/tex/latex/arev/omlzavm.fd
%{_texdir}/texmf-dist/tex/latex/arev/omszavm.fd
%{_texdir}/texmf-dist/tex/latex/arev/ot1zavm.fd
%{_texdir}/texmf-dist/tex/latex/arev/t1fav.fd
%{_texdir}/texmf-dist/tex/latex/arev/uzavm.fd

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/fonts/arev/ArevSansLicense.txt
%{_texdir}/texmf-dist/doc/fonts/arev/BitstreamVeraLicense.txt
%{_texdir}/texmf-dist/doc/fonts/arev/ChangeLog
%{_texdir}/texmf-dist/doc/fonts/arev/GPLv2.txt
%{_texdir}/texmf-dist/doc/fonts/arev/LPPLv1-3a.txt
%{_texdir}/texmf-dist/doc/fonts/arev/Makefile
%{_texdir}/texmf-dist/doc/fonts/arev/README
%{_texdir}/texmf-dist/doc/fonts/arev/arevdoc.lyx
%{_texdir}/texmf-dist/doc/fonts/arev/arevdoc.pdf
%{_texdir}/texmf-dist/doc/fonts/arev/arevdoc.tex
%{_texdir}/texmf-dist/doc/fonts/arev/fontsample.tex
%{_texdir}/texmf-dist/doc/fonts/arev/mathtesty.pdf
%{_texdir}/texmf-dist/doc/fonts/arev/mathtesty.tex
%{_texdir}/texmf-dist/doc/fonts/arev/prosper-arev.tex
%{_texdir}/texmf-dist/doc/fonts/arev/prosper-cmbright.tex
%{_texdir}/texmf-dist/doc/fonts/arev/prosper-cmss.tex
%{_texdir}/texmf-dist/doc/fonts/arev/prosper-header.tex
%{_texdir}/texmf-dist/doc/fonts/arev/prosper-helvetica.tex
%{_texdir}/texmf-dist/doc/fonts/arev/prosper-kerkis.tex
%{_texdir}/texmf-dist/doc/fonts/arev/prosper-lcmss.tex
%{_texdir}/texmf-dist/doc/fonts/arev/prosper-text.tex

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/ArevSans-Bold.pfb
%{_fontdir}/ArevSans-BoldOblique.pfb
%{_fontdir}/ArevSans-Oblique.pfb
%{_fontdir}/ArevSans-Roman.pfb

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
