%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/doublestroke.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/doublestroke.doc.tar.xz

Name: texlive-doublestroke
License: Freely redistributable without restriction
Summary: Typeset mathematical double stroke symbols
Version: %{tl_version}
Release: %{tl_noarch_release}.1.111.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(dsfont.sty)
Requires: texlive-doublestroke-fedora-fonts = %{tl_version}

%description
A font based on Computer Modern Roman useful for typesetting
the mathematical symbols for the natural numbers (N), whole
numbers (Z), rational numbers (Q), real numbers (R) and complex
numbers (C); coverage includes all Roman capital letters, '1',
'h' and 'k'. The font is available both as MetaFont source and
in Adobe Type 1 format, and LaTeX macros for its use are
provided. The fonts appear in the blackboard bold sampler.

date: 2009-11-19 15:03:53 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map dstroke.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map dstroke.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for doublestroke
Version: %{tl_version}
Release: %{tl_noarch_release}.1.111.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for doublestroke

%package fedora-fonts
Summary: Fonts for doublestroke
Version: %{tl_version}
Release: %{tl_noarch_release}.1.111.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-doublestroke = %{tl_version}
BuildArch: noarch

%description fedora-fonts
A font based on Computer Modern Roman useful for typesetting
the mathematical symbols for the natural numbers (N), whole
numbers (Z), rational numbers (Q), real numbers (R) and complex
numbers (C); coverage includes all Roman capital letters, '1',
'h' and 'k'. The font is available both as MetaFont source and
in Adobe Type 1 format, and LaTeX macros for its use are
provided. The fonts appear in the blackboard bold sampler.

date: 2009-11-19 15:03:53 +0100


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/doublestroke/dsrom10.pfb .
ln -s %{_fontdir}/dsrom10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/doublestroke/dsrom10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/doublestroke/dsrom12.pfb .
ln -s %{_fontdir}/dsrom12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/doublestroke/dsrom12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/doublestroke/dsrom8.pfb .
ln -s %{_fontdir}/dsrom8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/doublestroke/dsrom8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/doublestroke/dsss10.pfb .
ln -s %{_fontdir}/dsss10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/doublestroke/dsss10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/doublestroke/dsss12.pfb .
ln -s %{_fontdir}/dsss12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/doublestroke/dsss12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/doublestroke/dsss8.pfb .
ln -s %{_fontdir}/dsss8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/doublestroke/dsss8.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/fonts/map/dvips/doublestroke/dstroke.map
%{_texdir}/texmf-dist/fonts/source/public/doublestroke/dsrom.mf
%{_texdir}/texmf-dist/fonts/source/public/doublestroke/dsrom10.mf
%{_texdir}/texmf-dist/fonts/source/public/doublestroke/dsrom12.mf
%{_texdir}/texmf-dist/fonts/source/public/doublestroke/dsrom8.mf
%{_texdir}/texmf-dist/fonts/source/public/doublestroke/dsromo.mf
%{_texdir}/texmf-dist/fonts/source/public/doublestroke/dsromu.mf
%{_texdir}/texmf-dist/fonts/source/public/doublestroke/dsss10.mf
%{_texdir}/texmf-dist/fonts/source/public/doublestroke/dsss12.mf
%{_texdir}/texmf-dist/fonts/source/public/doublestroke/dsss8.mf
%{_texdir}/texmf-dist/fonts/tfm/public/doublestroke/dsrom10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/doublestroke/dsrom12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/doublestroke/dsrom8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/doublestroke/dsss10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/doublestroke/dsss12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/doublestroke/dsss8.tfm
%{_texdir}/texmf-dist/fonts/type1/public/doublestroke/dsrom10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/doublestroke/dsrom12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/doublestroke/dsrom8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/doublestroke/dsss10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/doublestroke/dsss12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/doublestroke/dsss8.pfb
%{_texdir}/texmf-dist/tex/latex/doublestroke/Udsrom.fd
%{_texdir}/texmf-dist/tex/latex/doublestroke/Udsss.fd
%{_texdir}/texmf-dist/tex/latex/doublestroke/dsfont.sty

%files doc
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/doc/fonts/doublestroke/README
%{_texdir}/texmf-dist/doc/fonts/doublestroke/dsdoc.pdf
%{_texdir}/texmf-dist/doc/fonts/doublestroke/dsdoc.tex

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/dsrom10.pfb
%{_fontdir}/dsrom12.pfb
%{_fontdir}/dsrom8.pfb
%{_fontdir}/dsss10.pfb
%{_fontdir}/dsss12.pfb
%{_fontdir}/dsss8.pfb

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
