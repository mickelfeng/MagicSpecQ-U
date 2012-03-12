%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/bera.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/bera.doc.tar.xz

Name: texlive-bera
License: Freely redistributable without restriction
Summary: Bera fonts
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(bera.sty)
Provides: tex(beramono.sty)
Provides: tex(berasans.sty)
Provides: tex(beraserif.sty)
Requires: tex(fontenc.sty)
Requires: tex(textcomp.sty)
Requires: tex(keyval.sty)
Requires: texlive-bera-fedora-fonts = %{tl_version}

%description
The package contains the Bera Type 1 fonts, and a zip archive
containing files to use the fonts with LaTeX. Bera is a set of
three font families: Bera Serif (a slab-serif Roman), Bera Sans
(a Frutiger descendant), and Bera Mono (monospaced/typewriter).
Support for use in LaTeX is also provided. The Bera family is a
repackaging, for use with TeX, of the Bitstream Vera family.

date: 2008-01-28 20:53:41 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map bera.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map bera.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for bera
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for bera

%package fedora-fonts
Summary: Fonts for bera
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-bera = %{tl_version}
BuildArch: noarch

%description fedora-fonts
The package contains the Bera Type 1 fonts, and a zip archive
containing files to use the fonts with LaTeX. Bera is a set of
three font families: Bera Serif (a slab-serif Roman), Bera Sans
(a Frutiger descendant), and Bera Mono (monospaced/typewriter).
Support for use in LaTeX is also provided. The Bera family is a
repackaging, for use with TeX, of the Bitstream Vera family.

date: 2008-01-28 20:53:41 +0100


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/bera/fveb8a.pfb .
ln -s %{_fontdir}/fveb8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/bera/fveb8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/bera/fver8a.pfb .
ln -s %{_fontdir}/fver8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/bera/fver8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/bera/fvmb8a.pfb .
ln -s %{_fontdir}/fvmb8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/bera/fvmb8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/bera/fvmbo8a.pfb .
ln -s %{_fontdir}/fvmbo8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/bera/fvmbo8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/bera/fvmr8a.pfb .
ln -s %{_fontdir}/fvmr8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/bera/fvmr8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/bera/fvmro8a.pfb .
ln -s %{_fontdir}/fvmro8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/bera/fvmro8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/bera/fvsb8a.pfb .
ln -s %{_fontdir}/fvsb8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/bera/fvsb8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/bera/fvsbo8a.pfb .
ln -s %{_fontdir}/fvsbo8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/bera/fvsbo8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/bera/fvsr8a.pfb .
ln -s %{_fontdir}/fvsr8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/bera/fvsr8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/bera/fvsro8a.pfb .
ln -s %{_fontdir}/fvsro8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/bera/fvsro8a.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/fonts/afm/public/bera/fveb8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/bera/fver8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/bera/fvmb8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/bera/fvmbo8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/bera/fvmr8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/bera/fvmro8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/bera/fvsb8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/bera/fvsbo8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/bera/fvsr8a.afm
%{_texdir}/texmf-dist/fonts/afm/public/bera/fvsro8a.afm
%{_texdir}/texmf-dist/fonts/map/dvips/bera/bera.map
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fveb8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fveb8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fveb8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fveb8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvebo8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvebo8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvebo8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fver8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fver8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fver8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fver8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvero8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvero8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvero8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvmb8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvmb8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvmb8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvmb8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvmbo8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvmbo8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvmbo8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvmbo8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvmr8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvmr8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvmr8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvmr8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvmro8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvmro8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvmro8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvmro8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvsb8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvsb8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvsb8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvsb8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvsbo8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvsbo8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvsbo8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvsbo8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvsr8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvsr8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvsr8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvsr8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvsro8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvsro8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvsro8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bera/fvsro8t.tfm
%{_texdir}/texmf-dist/fonts/type1/public/bera/fveb8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/bera/fver8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/bera/fvmb8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/bera/fvmbo8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/bera/fvmr8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/bera/fvmro8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/bera/fvsb8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/bera/fvsbo8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/bera/fvsr8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/bera/fvsro8a.pfb
%{_texdir}/texmf-dist/fonts/vf/public/bera/fveb8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/bera/fveb8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/bera/fvebo8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/bera/fvebo8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/bera/fver8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/bera/fver8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/bera/fvero8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/bera/fvero8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/bera/fvmb8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/bera/fvmb8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/bera/fvmbo8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/bera/fvmbo8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/bera/fvmr8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/bera/fvmr8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/bera/fvmro8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/bera/fvmro8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/bera/fvsb8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/bera/fvsb8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/bera/fvsbo8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/bera/fvsbo8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/bera/fvsr8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/bera/fvsr8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/bera/fvsro8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/bera/fvsro8t.vf
%{_texdir}/texmf-dist/tex/latex/bera/bera.sty
%{_texdir}/texmf-dist/tex/latex/bera/beramono.sty
%{_texdir}/texmf-dist/tex/latex/bera/berasans.sty
%{_texdir}/texmf-dist/tex/latex/bera/beraserif.sty
%{_texdir}/texmf-dist/tex/latex/bera/t1fve.fd
%{_texdir}/texmf-dist/tex/latex/bera/t1fvm.fd
%{_texdir}/texmf-dist/tex/latex/bera/t1fvs.fd
%{_texdir}/texmf-dist/tex/latex/bera/ts1fve.fd
%{_texdir}/texmf-dist/tex/latex/bera/ts1fvm.fd
%{_texdir}/texmf-dist/tex/latex/bera/ts1fvs.fd

%files doc
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/doc/fonts/bera/LICENSE
%{_texdir}/texmf-dist/doc/fonts/bera/README
%{_texdir}/texmf-dist/doc/fonts/bera/bera.pdf
%{_texdir}/texmf-dist/doc/fonts/bera/bera.txt

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/fveb8a.pfb
%{_fontdir}/fver8a.pfb
%{_fontdir}/fvmb8a.pfb
%{_fontdir}/fvmbo8a.pfb
%{_fontdir}/fvmr8a.pfb
%{_fontdir}/fvmro8a.pfb
%{_fontdir}/fvsb8a.pfb
%{_fontdir}/fvsbo8a.pfb
%{_fontdir}/fvsr8a.pfb
%{_fontdir}/fvsro8a.pfb

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