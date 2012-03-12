%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/auncial-new.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/auncial-new.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/auncial-new.source.tar.xz

Name: texlive-auncial-new
License: LPPL
Summary: Artificial Uncial font and LaTeX support macros
Version: %{tl_version}
Release: %{tl_noarch_release}.2.0.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(allauncl.sty)
Provides: tex(auncial.sty)
Requires: texlive-auncial-new-fedora-fonts = %{tl_version}

%description
The auncial-new bundle provides packages and fonts for a script
based on the Artificial Uncial manuscript book-hand used
between the 6th & 10th century AD. The script consists of
minuscules and digits, with some appropriate period punctuation
marks. Both normal and bold versions are provided, and the font
is distributed in Adobe Type 1 format. This is an experimental
new version of the auncial bundle, which is one of a series of
bookhand fonts. The font follows the B1 encoding developed for
bookhands. Access to the encoding is essential. The encoding
mainly follows the standard T1 encoding.

date: 2008-08-16 20:32:59 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map auncial.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map auncial.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for auncial-new
Version: %{tl_version}
Release: %{tl_noarch_release}.2.0.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for auncial-new

%package fedora-fonts
Summary: Fonts for auncial-new
Version: %{tl_version}
Release: %{tl_noarch_release}.2.0.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-auncial-new = %{tl_version}
BuildArch: noarch

%description fedora-fonts
The auncial-new bundle provides packages and fonts for a script
based on the Artificial Uncial manuscript book-hand used
between the 6th & 10th century AD. The script consists of
minuscules and digits, with some appropriate period punctuation
marks. Both normal and bold versions are provided, and the font
is distributed in Adobe Type 1 format. This is an experimental
new version of the auncial bundle, which is one of a series of
bookhand fonts. The font follows the B1 encoding developed for
bookhands. Access to the encoding is essential. The encoding
mainly follows the standard T1 encoding.

date: 2008-08-16 20:32:59 +0200


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/auncial-new/auncl10.pfb .
ln -s %{_fontdir}/auncl10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/auncial-new/auncl10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/auncial-new/aunclb10.pfb .
ln -s %{_fontdir}/aunclb10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/auncial-new/aunclb10.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/fonts/afm/public/auncial-new/auncl10.afm
%{_texdir}/texmf-dist/fonts/afm/public/auncial-new/aunclb10.afm
%{_texdir}/texmf-dist/fonts/map/dvips/auncial-new/auncial.map
%{_texdir}/texmf-dist/fonts/tfm/public/auncial-new/auncl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/auncial-new/aunclb10.tfm
%{_texdir}/texmf-dist/fonts/type1/public/auncial-new/auncl10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/auncial-new/aunclb10.pfb
%{_texdir}/texmf-dist/tex/latex/auncial-new/allauncl.sty
%{_texdir}/texmf-dist/tex/latex/auncial-new/auncial.sty
%{_texdir}/texmf-dist/tex/latex/auncial-new/b1auncl.fd

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/fonts/auncial-new/README
%{_texdir}/texmf-dist/doc/fonts/auncial-new/auncial.pdf
%{_texdir}/texmf-dist/doc/fonts/auncial-new/tryauncial.pdf
%{_texdir}/texmf-dist/doc/fonts/auncial-new/tryauncial.tex

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/auncl10.pfb
%{_fontdir}/aunclb10.pfb

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
