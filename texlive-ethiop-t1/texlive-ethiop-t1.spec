%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/ethiop-t1.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/ethiop-t1.doc.tar.xz

Name: texlive-ethiop-t1
License: GPL+
Summary: Type 1 versions of Amharic fonts
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-ethiop-t1-fedora-fonts = %{tl_version}

%description
These fonts are drop-in Adobe type 1 replacements for the fonts
of the ethiop package.

date: 2007-02-14 08:57:40 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "MixedMap ethiop.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^MixedMap ethiop.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for ethiop-t1
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for ethiop-t1

%package fedora-fonts
Summary: Fonts for ethiop-t1
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-ethiop-t1 = %{tl_version}
BuildArch: noarch

%description fedora-fonts
These fonts are drop-in Adobe type 1 replacements for the fonts
of the ethiop package.

date: 2007-02-14 08:57:40 +0100


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/etha10.pfb .
ln -s %{_fontdir}/etha10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/etha10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/etha6.pfb .
ln -s %{_fontdir}/etha6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/etha6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/etha7.pfb .
ln -s %{_fontdir}/etha7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/etha7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/etha8.pfb .
ln -s %{_fontdir}/etha8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/etha8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethab10.pfb .
ln -s %{_fontdir}/ethab10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethab10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethab11.pfb .
ln -s %{_fontdir}/ethab11.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethab11.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethab12.pfb .
ln -s %{_fontdir}/ethab12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethab12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethab14.pfb .
ln -s %{_fontdir}/ethab14.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethab14.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethab18.pfb .
ln -s %{_fontdir}/ethab18.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethab18.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethab24.pfb .
ln -s %{_fontdir}/ethab24.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethab24.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethab36.pfb .
ln -s %{_fontdir}/ethab36.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethab36.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethab9.pfb .
ln -s %{_fontdir}/ethab9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethab9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethas10.pfb .
ln -s %{_fontdir}/ethas10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethas10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethasb10.pfb .
ln -s %{_fontdir}/ethasb10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethasb10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethasb11.pfb .
ln -s %{_fontdir}/ethasb11.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethasb11.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethasb12.pfb .
ln -s %{_fontdir}/ethasb12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethasb12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethasb14.pfb .
ln -s %{_fontdir}/ethasb14.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethasb14.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethasb18.pfb .
ln -s %{_fontdir}/ethasb18.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethasb18.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethasb24.pfb .
ln -s %{_fontdir}/ethasb24.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethasb24.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethasb36.pfb .
ln -s %{_fontdir}/ethasb36.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethasb36.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethasb9.pfb .
ln -s %{_fontdir}/ethasb9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethasb9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethatt10.pfb .
ln -s %{_fontdir}/ethatt10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethatt10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethb10.pfb .
ln -s %{_fontdir}/ethb10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethb10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethb6.pfb .
ln -s %{_fontdir}/ethb6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethb6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethb7.pfb .
ln -s %{_fontdir}/ethb7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethb7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethb8.pfb .
ln -s %{_fontdir}/ethb8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethb8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbb10.pfb .
ln -s %{_fontdir}/ethbb10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbb10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbb11.pfb .
ln -s %{_fontdir}/ethbb11.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbb11.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbb12.pfb .
ln -s %{_fontdir}/ethbb12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbb12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbb14.pfb .
ln -s %{_fontdir}/ethbb14.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbb14.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbb18.pfb .
ln -s %{_fontdir}/ethbb18.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbb18.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbb24.pfb .
ln -s %{_fontdir}/ethbb24.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbb24.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbb36.pfb .
ln -s %{_fontdir}/ethbb36.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbb36.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbb9.pfb .
ln -s %{_fontdir}/ethbb9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbb9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbs10.pfb .
ln -s %{_fontdir}/ethbs10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbs10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbsb10.pfb .
ln -s %{_fontdir}/ethbsb10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbsb10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbsb11.pfb .
ln -s %{_fontdir}/ethbsb11.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbsb11.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbsb12.pfb .
ln -s %{_fontdir}/ethbsb12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbsb12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbsb14.pfb .
ln -s %{_fontdir}/ethbsb14.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbsb14.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbsb18.pfb .
ln -s %{_fontdir}/ethbsb18.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbsb18.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbsb24.pfb .
ln -s %{_fontdir}/ethbsb24.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbsb24.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbsb36.pfb .
ln -s %{_fontdir}/ethbsb36.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbsb36.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbsb9.pfb .
ln -s %{_fontdir}/ethbsb9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbsb9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbtt10.pfb .
ln -s %{_fontdir}/ethbtt10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbtt10.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/fonts/map/dvips/ethiop-t1/ethiop.map
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/etha10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/etha6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/etha7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/etha8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethab10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethab11.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethab12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethab14.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethab18.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethab24.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethab36.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethab9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethas10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethasb10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethasb11.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethasb12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethasb14.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethasb18.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethasb24.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethasb36.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethasb9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethatt10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethb10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethb6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethb7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethb8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbb10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbb11.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbb12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbb14.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbb18.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbb24.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbb36.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbb9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbs10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbsb10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbsb11.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbsb12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbsb14.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbsb18.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbsb24.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbsb36.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbsb9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/ethbtt10.pfb

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/latex/ethiop-t1/COPYING
%{_texdir}/texmf-dist/doc/latex/ethiop-t1/README

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/etha10.pfb
%{_fontdir}/etha6.pfb
%{_fontdir}/etha7.pfb
%{_fontdir}/etha8.pfb
%{_fontdir}/ethab10.pfb
%{_fontdir}/ethab11.pfb
%{_fontdir}/ethab12.pfb
%{_fontdir}/ethab14.pfb
%{_fontdir}/ethab18.pfb
%{_fontdir}/ethab24.pfb
%{_fontdir}/ethab36.pfb
%{_fontdir}/ethab9.pfb
%{_fontdir}/ethas10.pfb
%{_fontdir}/ethasb10.pfb
%{_fontdir}/ethasb11.pfb
%{_fontdir}/ethasb12.pfb
%{_fontdir}/ethasb14.pfb
%{_fontdir}/ethasb18.pfb
%{_fontdir}/ethasb24.pfb
%{_fontdir}/ethasb36.pfb
%{_fontdir}/ethasb9.pfb
%{_fontdir}/ethatt10.pfb
%{_fontdir}/ethb10.pfb
%{_fontdir}/ethb6.pfb
%{_fontdir}/ethb7.pfb
%{_fontdir}/ethb8.pfb
%{_fontdir}/ethbb10.pfb
%{_fontdir}/ethbb11.pfb
%{_fontdir}/ethbb12.pfb
%{_fontdir}/ethbb14.pfb
%{_fontdir}/ethbb18.pfb
%{_fontdir}/ethbb24.pfb
%{_fontdir}/ethbb36.pfb
%{_fontdir}/ethbb9.pfb
%{_fontdir}/ethbs10.pfb
%{_fontdir}/ethbsb10.pfb
%{_fontdir}/ethbsb11.pfb
%{_fontdir}/ethbsb12.pfb
%{_fontdir}/ethbsb14.pfb
%{_fontdir}/ethbsb18.pfb
%{_fontdir}/ethbsb24.pfb
%{_fontdir}/ethbsb36.pfb
%{_fontdir}/ethbsb9.pfb
%{_fontdir}/ethbtt10.pfb

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
