%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cyklop.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cyklop.doc.tar.xz

Name: texlive-cyklop
License: LPPL
Summary: The Cyclop typeface
Version: %{tl_version}
Release: %{tl_noarch_release}.0.915.svn18651%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(cyklop.sty)
Requires: texlive-cyklop-fedora-fonts = %{tl_version}

%description
The Cyclop typeface was designed in the 1920s at the workshop
of Warsaw type foundry "Odlewnia Czcionek J. Idzkowski i S-ka".
This sans serif typeface has a highly modulated stroke so it
has high typographic contrast. The vertical stems are much
heavier then horizontal ones. Most characters have thin
rectangles as additional counters giving the unique shape of
the characters. The lead types of Cyclop typeface were produced
in slanted variant at sizes 8-48 pt. It was heavily used for
heads in newspapers and accidents prints. Typesetters used
Cyclop in the inter-war period, during the occupation in the
underground press. The typeface was used until the beginnings
of the offset print and computer typesetting era. Nowadays it
is hard to find the metal types of this typeface. The font was
generated using the Metatype1 package. Then the original set of
characters was completed by adding the full set of accented
letters and characters of the modern Latin alphabets (including
Vietnamese). The upright variant was generated and it was more
complicated task than it appeared at the beginning. 11 upright
letters of the Cyclop typeface were presented in the book by
Filip Trzaska, "Podstawy techniki wydawniczej" ("Foundation of
the publishing techonology"), Warsaw 1967. But even the author
of the book does not know what was the source of the presented
examples. The fonts are distributed in the Type1 and OpenType
formats along with the files necessary for use these fonts in
TeX and LaTeX including encoding definition files: T1 (ec), T5
(Vietnamese), OT4, QX, texnansi and nonstandard ones (IL2 for
Czech fonts).

date: 2008-12-15 08:58:20 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map cyklop.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map cyklop.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for cyklop
Version: %{tl_version}
Release: %{tl_noarch_release}.0.915.svn18651%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for cyklop

%package fedora-fonts
Summary: Fonts for cyklop
Version: %{tl_version}
Release: %{tl_noarch_release}.0.915.svn18651%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-cyklop = %{tl_version}
BuildArch: noarch

%description fedora-fonts
The Cyclop typeface was designed in the 1920s at the workshop
of Warsaw type foundry "Odlewnia Czcionek J. Idzkowski i S-ka".
This sans serif typeface has a highly modulated stroke so it
has high typographic contrast. The vertical stems are much
heavier then horizontal ones. Most characters have thin
rectangles as additional counters giving the unique shape of
the characters. The lead types of Cyclop typeface were produced
in slanted variant at sizes 8-48 pt. It was heavily used for
heads in newspapers and accidents prints. Typesetters used
Cyclop in the inter-war period, during the occupation in the
underground press. The typeface was used until the beginnings
of the offset print and computer typesetting era. Nowadays it
is hard to find the metal types of this typeface. The font was
generated using the Metatype1 package. Then the original set of
characters was completed by adding the full set of accented
letters and characters of the modern Latin alphabets (including
Vietnamese). The upright variant was generated and it was more
complicated task than it appeared at the beginning. 11 upright
letters of the Cyclop typeface were presented in the book by
Filip Trzaska, "Podstawy techniki wydawniczej" ("Foundation of
the publishing techonology"), Warsaw 1967. But even the author
of the book does not know what was the source of the presented
examples. The fonts are distributed in the Type1 and OpenType
formats along with the files necessary for use these fonts in
TeX and LaTeX including encoding definition files: T1 (ec), T5
(Vietnamese), OT4, QX, texnansi and nonstandard ones (IL2 for
Czech fonts).

date: 2008-12-15 08:58:20 +0100


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/gfl.txt gfl.txt
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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cyklop/cyklop-italic.otf .
ln -s %{_fontdir}/cyklop-italic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cyklop/cyklop-italic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cyklop/cyklop-regular.otf .
ln -s %{_fontdir}/cyklop-regular.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cyklop/cyklop-regular.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cyklop/cyklopi.pfb .
ln -s %{_fontdir}/cyklopi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cyklop/cyklopi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cyklop/cyklopr.pfb .
ln -s %{_fontdir}/cyklopr.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cyklop/cyklopr.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gfl.txt
%{_texdir}/texmf-dist/fonts/afm/public/cyklop/cyklopi.afm
%{_texdir}/texmf-dist/fonts/afm/public/cyklop/cyklopr.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/cyklop/cs-cyklop-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cyklop/cs-cyklop.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cyklop/ec-cyklop-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cyklop/ec-cyklop.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cyklop/l7x-cyklop-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cyklop/l7x-cyklop.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cyklop/ly1-cyklop-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cyklop/ly1-cyklop.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cyklop/qx-cyklop-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cyklop/qx-cyklop.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cyklop/t5-cyklop-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cyklop/t5-cyklop.enc
%{_texdir}/texmf-dist/fonts/map/dvips/cyklop/cyklop-cs.map
%{_texdir}/texmf-dist/fonts/map/dvips/cyklop/cyklop-ec.map
%{_texdir}/texmf-dist/fonts/map/dvips/cyklop/cyklop-l7x.map
%{_texdir}/texmf-dist/fonts/map/dvips/cyklop/cyklop-ly1.map
%{_texdir}/texmf-dist/fonts/map/dvips/cyklop/cyklop-qx.map
%{_texdir}/texmf-dist/fonts/map/dvips/cyklop/cyklop-t5.map
%{_texdir}/texmf-dist/fonts/map/dvips/cyklop/cyklop.map
%{_texdir}/texmf-dist/fonts/opentype/public/cyklop/cyklop-italic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/cyklop/cyklop-regular.otf
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/cs-cyklopi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/cs-cyklopi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/cs-cyklopr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/cs-cyklopr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/ec-cyklopi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/ec-cyklopi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/ec-cyklopr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/ec-cyklopr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/l7x-cyklopi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/l7x-cyklopi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/l7x-cyklopr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/l7x-cyklopr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/ly1-cyklopi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/ly1-cyklopi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/ly1-cyklopr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/ly1-cyklopr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/qx-cyklopi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/qx-cyklopi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/qx-cyklopr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/qx-cyklopr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/t5-cyklopi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/t5-cyklopi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/t5-cyklopr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cyklop/t5-cyklopr.tfm
%{_texdir}/texmf-dist/fonts/type1/public/cyklop/cyklopi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cyklop/cyklopr.pfb
%{_texdir}/texmf-dist/tex/latex/cyklop/cyklop.sty
%{_texdir}/texmf-dist/tex/latex/cyklop/il2cyklop.fd
%{_texdir}/texmf-dist/tex/latex/cyklop/l7xcyklop.fd
%{_texdir}/texmf-dist/tex/latex/cyklop/ly1cyklop.fd
%{_texdir}/texmf-dist/tex/latex/cyklop/ot1cyklop.fd
%{_texdir}/texmf-dist/tex/latex/cyklop/ot4cyklop.fd
%{_texdir}/texmf-dist/tex/latex/cyklop/qxcyklop.fd
%{_texdir}/texmf-dist/tex/latex/cyklop/t1cyklop.fd
%{_texdir}/texmf-dist/tex/latex/cyklop/t5cyklop.fd

%files doc
%defattr(-,root,root)
%doc gfl.txt
%{_texdir}/texmf-dist/doc/fonts/cyklop/00readme
%{_texdir}/texmf-dist/doc/fonts/cyklop/00readme-pl
%{_texdir}/texmf-dist/doc/fonts/cyklop/GUST-FONT-LICENSE.txt
%{_texdir}/texmf-dist/doc/fonts/cyklop/MANIFEST.txt
%{_texdir}/texmf-dist/doc/fonts/cyklop/cyklop-info.pdf

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/cyklop-italic.otf
%{_fontdir}/cyklop-regular.otf
%{_fontdir}/cyklopi.pfb
%{_fontdir}/cyklopr.pfb

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
