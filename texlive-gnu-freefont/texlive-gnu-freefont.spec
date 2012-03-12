%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/gnu-freefont.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/gnu-freefont.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/gnu-freefont.source.tar.xz

Name: texlive-gnu-freefont
License: GPLv3+
Summary: A Unicode font, with rather wide coverage
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19511%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-gnu-freefont-fedora-fonts = %{tl_version}

%description
The package provides a set of outline (i.e. OpenType) fonts
covering as much as possible of the Unicode character set. The
set consists of three typefaces: one monospaced and two
proportional (one with uniform and one with modulated stroke).

date: 2010-01-08 23:56:56 +0100

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
Summary: Documentation for gnu-freefont
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19511%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for gnu-freefont

%package fedora-fonts
Summary: Fonts for gnu-freefont
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19511%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-gnu-freefont = %{tl_version}
BuildArch: noarch

%description fedora-fonts
The package provides a set of outline (i.e. OpenType) fonts
covering as much as possible of the Unicode character set. The
set consists of three typefaces: one monospaced and two
proportional (one with uniform and one with modulated stroke).

date: 2010-01-08 23:56:56 +0100


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/gpl3.txt gpl3.txt
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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeMono.otf .
ln -s %{_fontdir}/FreeMono.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeMono.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeMonoBold.otf .
ln -s %{_fontdir}/FreeMonoBold.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeMonoBold.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeMonoBoldOblique.otf .
ln -s %{_fontdir}/FreeMonoBoldOblique.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeMonoBoldOblique.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeMonoOblique.otf .
ln -s %{_fontdir}/FreeMonoOblique.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeMonoOblique.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeSans.otf .
ln -s %{_fontdir}/FreeSans.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeSans.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeSansBold.otf .
ln -s %{_fontdir}/FreeSansBold.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeSansBold.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeSansBoldOblique.otf .
ln -s %{_fontdir}/FreeSansBoldOblique.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeSansBoldOblique.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeSansOblique.otf .
ln -s %{_fontdir}/FreeSansOblique.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeSansOblique.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeSerif.otf .
ln -s %{_fontdir}/FreeSerif.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeSerif.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeSerifBold.otf .
ln -s %{_fontdir}/FreeSerifBold.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeSerifBold.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeSerifBoldItalic.otf .
ln -s %{_fontdir}/FreeSerifBoldItalic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeSerifBoldItalic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeSerifItalic.otf .
ln -s %{_fontdir}/FreeSerifItalic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeSerifItalic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeMono.ttf .
ln -s %{_fontdir}/FreeMono.ttf %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeMono.ttf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeMonoBold.ttf .
ln -s %{_fontdir}/FreeMonoBold.ttf %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeMonoBold.ttf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeMonoBoldOblique.ttf .
ln -s %{_fontdir}/FreeMonoBoldOblique.ttf %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeMonoBoldOblique.ttf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeMonoOblique.ttf .
ln -s %{_fontdir}/FreeMonoOblique.ttf %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeMonoOblique.ttf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeSans.ttf .
ln -s %{_fontdir}/FreeSans.ttf %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeSans.ttf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeSansBold.ttf .
ln -s %{_fontdir}/FreeSansBold.ttf %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeSansBold.ttf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeSansBoldOblique.ttf .
ln -s %{_fontdir}/FreeSansBoldOblique.ttf %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeSansBoldOblique.ttf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeSansOblique.ttf .
ln -s %{_fontdir}/FreeSansOblique.ttf %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeSansOblique.ttf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeSerif.ttf .
ln -s %{_fontdir}/FreeSerif.ttf %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeSerif.ttf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeSerifBold.ttf .
ln -s %{_fontdir}/FreeSerifBold.ttf %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeSerifBold.ttf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeSerifBoldItalic.ttf .
ln -s %{_fontdir}/FreeSerifBoldItalic.ttf %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeSerifBoldItalic.ttf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeSerifItalic.ttf .
ln -s %{_fontdir}/FreeSerifItalic.ttf %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeSerifItalic.ttf
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gpl3.txt
%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeMono.otf
%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeMonoBold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeMonoBoldOblique.otf
%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeMonoOblique.otf
%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeSans.otf
%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeSansBold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeSansBoldOblique.otf
%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeSansOblique.otf
%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeSerif.otf
%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeSerifBold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeSerifBoldItalic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/FreeSerifItalic.otf
%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeMono.ttf
%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeMonoBold.ttf
%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeMonoBoldOblique.ttf
%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeMonoOblique.ttf
%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeSans.ttf
%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeSansBold.ttf
%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeSansBoldOblique.ttf
%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeSansOblique.ttf
%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeSerif.ttf
%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeSerifBold.ttf
%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeSerifBoldItalic.ttf
%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/FreeSerifItalic.ttf

%files doc
%defattr(-,root,root)
%doc gpl3.txt
%{_texdir}/texmf-dist/doc/fonts/gnu-freefont/AUTHORS
%{_texdir}/texmf-dist/doc/fonts/gnu-freefont/COPYING
%{_texdir}/texmf-dist/doc/fonts/gnu-freefont/CREDITS
%{_texdir}/texmf-dist/doc/fonts/gnu-freefont/ChangeLog
%{_texdir}/texmf-dist/doc/fonts/gnu-freefont/INSTALL
%{_texdir}/texmf-dist/doc/fonts/gnu-freefont/README

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/FreeMono.otf
%{_fontdir}/FreeMonoBold.otf
%{_fontdir}/FreeMonoBoldOblique.otf
%{_fontdir}/FreeMonoOblique.otf
%{_fontdir}/FreeSans.otf
%{_fontdir}/FreeSansBold.otf
%{_fontdir}/FreeSansBoldOblique.otf
%{_fontdir}/FreeSansOblique.otf
%{_fontdir}/FreeSerif.otf
%{_fontdir}/FreeSerifBold.otf
%{_fontdir}/FreeSerifBoldItalic.otf
%{_fontdir}/FreeSerifItalic.otf
%{_fontdir}/FreeMono.ttf
%{_fontdir}/FreeMonoBold.ttf
%{_fontdir}/FreeMonoBoldOblique.ttf
%{_fontdir}/FreeMonoOblique.ttf
%{_fontdir}/FreeSans.ttf
%{_fontdir}/FreeSansBold.ttf
%{_fontdir}/FreeSansBoldOblique.ttf
%{_fontdir}/FreeSansOblique.ttf
%{_fontdir}/FreeSerif.ttf
%{_fontdir}/FreeSerifBold.ttf
%{_fontdir}/FreeSerifBoldItalic.ttf
%{_fontdir}/FreeSerifItalic.ttf

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
