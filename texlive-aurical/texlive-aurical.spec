%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/aurical.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/aurical.doc.tar.xz

Name: texlive-aurical
License: LPPL
Summary: Calligraphic fonts for use with LaTeX in T1 encoding
Version: %{tl_version}
Release: %{tl_noarch_release}.1.5.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(aurical.sty)
Requires: texlive-aurical-fedora-fonts = %{tl_version}

%description
The package that implements a set (AuriocusKalligraphicus) of
three calligraphic fonts derived from the author's handwriting
in Adobe Type 1 Format, T1 (Cork) encoding for use with LaTeX:
- Auriocus Kalligraphicus; - Lukas Svatba; and - Jana Skrivana.
Each font features oldstyle digits and (machine-generated)
boldface and slanted versions. A variant of Lukas Svatba offers
a 'long s'.

date: 2008-07-27 23:11:56 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map aurical.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map aurical.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for aurical
Version: %{tl_version}
Release: %{tl_noarch_release}.1.5.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for aurical

%package fedora-fonts
Summary: Fonts for aurical
Version: %{tl_version}
Release: %{tl_noarch_release}.1.5.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-aurical = %{tl_version}
BuildArch: noarch

%description fedora-fonts
The package that implements a set (AuriocusKalligraphicus) of
three calligraphic fonts derived from the author's handwriting
in Adobe Type 1 Format, T1 (Cork) encoding for use with LaTeX:
- Auriocus Kalligraphicus; - Lukas Svatba; and - Jana Skrivana.
Each font features oldstyle digits and (machine-generated)
boldface and slanted versions. A variant of Lukas Svatba offers
a 'long s'.

date: 2008-07-27 23:11:56 +0200


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/AmiciLogo.pfb .
ln -s %{_fontdir}/AmiciLogo.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/AmiciLogo.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/AmiciLogoBold.pfb .
ln -s %{_fontdir}/AmiciLogoBold.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/AmiciLogoBold.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/AmiciLogoBoldRslant.pfb .
ln -s %{_fontdir}/AmiciLogoBoldRslant.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/AmiciLogoBoldRslant.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/AmiciLogoBoldSlant.pfb .
ln -s %{_fontdir}/AmiciLogoBoldSlant.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/AmiciLogoBoldSlant.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/AmiciLogoRslant.pfb .
ln -s %{_fontdir}/AmiciLogoRslant.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/AmiciLogoRslant.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/AmiciLogoSlant.pfb .
ln -s %{_fontdir}/AmiciLogoSlant.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/AmiciLogoSlant.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/AuriocusKalligraphicus.pfb .
ln -s %{_fontdir}/AuriocusKalligraphicus.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/AuriocusKalligraphicus.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/AuriocusKalligraphicusBold.pfb .
ln -s %{_fontdir}/AuriocusKalligraphicusBold.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/AuriocusKalligraphicusBold.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/AuriocusKalligraphicusBoldRslant.pfb .
ln -s %{_fontdir}/AuriocusKalligraphicusBoldRslant.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/AuriocusKalligraphicusBoldRslant.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/AuriocusKalligraphicusBoldSlant.pfb .
ln -s %{_fontdir}/AuriocusKalligraphicusBoldSlant.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/AuriocusKalligraphicusBoldSlant.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/AuriocusKalligraphicusRslant.pfb .
ln -s %{_fontdir}/AuriocusKalligraphicusRslant.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/AuriocusKalligraphicusRslant.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/AuriocusKalligraphicusSlant.pfb .
ln -s %{_fontdir}/AuriocusKalligraphicusSlant.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/AuriocusKalligraphicusSlant.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/JanaSkrivana.pfb .
ln -s %{_fontdir}/JanaSkrivana.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/JanaSkrivana.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/JanaSkrivanaBold.pfb .
ln -s %{_fontdir}/JanaSkrivanaBold.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/JanaSkrivanaBold.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/JanaSkrivanaBoldRslant.pfb .
ln -s %{_fontdir}/JanaSkrivanaBoldRslant.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/JanaSkrivanaBoldRslant.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/JanaSkrivanaBoldSlant.pfb .
ln -s %{_fontdir}/JanaSkrivanaBoldSlant.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/JanaSkrivanaBoldSlant.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/JanaSkrivanaRslant.pfb .
ln -s %{_fontdir}/JanaSkrivanaRslant.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/JanaSkrivanaRslant.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/JanaSkrivanaSlant.pfb .
ln -s %{_fontdir}/JanaSkrivanaSlant.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/JanaSkrivanaSlant.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/LukasSvatba.pfb .
ln -s %{_fontdir}/LukasSvatba.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/LukasSvatba.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/LukasSvatbaBold.pfb .
ln -s %{_fontdir}/LukasSvatbaBold.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/LukasSvatbaBold.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/LukasSvatbaBoldRslant.pfb .
ln -s %{_fontdir}/LukasSvatbaBoldRslant.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/LukasSvatbaBoldRslant.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/LukasSvatbaBoldSlant.pfb .
ln -s %{_fontdir}/LukasSvatbaBoldSlant.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/LukasSvatbaBoldSlant.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/LukasSvatbaRslant.pfb .
ln -s %{_fontdir}/LukasSvatbaRslant.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/LukasSvatbaRslant.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/LukasSvatbaSlant.pfb .
ln -s %{_fontdir}/LukasSvatbaSlant.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical/LukasSvatbaSlant.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/fonts/afm/public/aurical/AmiciLogo.afm
%{_texdir}/texmf-dist/fonts/afm/public/aurical/AmiciLogoBold.afm
%{_texdir}/texmf-dist/fonts/afm/public/aurical/AmiciLogoBoldRslant.afm
%{_texdir}/texmf-dist/fonts/afm/public/aurical/AmiciLogoBoldSlant.afm
%{_texdir}/texmf-dist/fonts/afm/public/aurical/AmiciLogoRslant.afm
%{_texdir}/texmf-dist/fonts/afm/public/aurical/AmiciLogoSlant.afm
%{_texdir}/texmf-dist/fonts/afm/public/aurical/AuriocusKalligraphicus.afm
%{_texdir}/texmf-dist/fonts/afm/public/aurical/AuriocusKalligraphicusBold.afm
%{_texdir}/texmf-dist/fonts/afm/public/aurical/AuriocusKalligraphicusBoldRslant.afm
%{_texdir}/texmf-dist/fonts/afm/public/aurical/AuriocusKalligraphicusBoldSlant.afm
%{_texdir}/texmf-dist/fonts/afm/public/aurical/AuriocusKalligraphicusRslant.afm
%{_texdir}/texmf-dist/fonts/afm/public/aurical/AuriocusKalligraphicusSlant.afm
%{_texdir}/texmf-dist/fonts/afm/public/aurical/JanaSkrivana.afm
%{_texdir}/texmf-dist/fonts/afm/public/aurical/JanaSkrivanaBold.afm
%{_texdir}/texmf-dist/fonts/afm/public/aurical/JanaSkrivanaBoldRslant.afm
%{_texdir}/texmf-dist/fonts/afm/public/aurical/JanaSkrivanaBoldSlant.afm
%{_texdir}/texmf-dist/fonts/afm/public/aurical/JanaSkrivanaRslant.afm
%{_texdir}/texmf-dist/fonts/afm/public/aurical/JanaSkrivanaSlant.afm
%{_texdir}/texmf-dist/fonts/afm/public/aurical/LukasSvatba.afm
%{_texdir}/texmf-dist/fonts/afm/public/aurical/LukasSvatbaBold.afm
%{_texdir}/texmf-dist/fonts/afm/public/aurical/LukasSvatbaBoldRslant.afm
%{_texdir}/texmf-dist/fonts/afm/public/aurical/LukasSvatbaBoldSlant.afm
%{_texdir}/texmf-dist/fonts/afm/public/aurical/LukasSvatbaRslant.afm
%{_texdir}/texmf-dist/fonts/afm/public/aurical/LukasSvatbaSlant.afm
%{_texdir}/texmf-dist/fonts/map/dvips/aurical/aurical.map
%{_texdir}/texmf-dist/fonts/source/public/aurical/aurical_source.zip
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/AmiciLogo.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/AmiciLogoBold.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/AmiciLogoBoldRslant.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/AmiciLogoBoldSlant.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/AmiciLogoRslant.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/AmiciLogoSlant.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/AuriocusKalligraphicus.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/AuriocusKalligraphicusBold.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/AuriocusKalligraphicusBoldRslant.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/AuriocusKalligraphicusBoldSlant.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/AuriocusKalligraphicusRslant.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/AuriocusKalligraphicusSlant.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/JanaSkrivana.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/JanaSkrivanaBold.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/JanaSkrivanaBoldRslant.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/JanaSkrivanaBoldSlant.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/JanaSkrivanaRslant.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/JanaSkrivanaSlant.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/LukasSvatba.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/LukasSvatbaBold.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/LukasSvatbaBoldRslant.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/LukasSvatbaBoldSlant.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/LukasSvatbaRslant.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/LukasSvatbaSlant.tfm
%{_texdir}/texmf-dist/fonts/type1/public/aurical/AmiciLogo.pfb
%{_texdir}/texmf-dist/fonts/type1/public/aurical/AmiciLogoBold.pfb
%{_texdir}/texmf-dist/fonts/type1/public/aurical/AmiciLogoBoldRslant.pfb
%{_texdir}/texmf-dist/fonts/type1/public/aurical/AmiciLogoBoldSlant.pfb
%{_texdir}/texmf-dist/fonts/type1/public/aurical/AmiciLogoRslant.pfb
%{_texdir}/texmf-dist/fonts/type1/public/aurical/AmiciLogoSlant.pfb
%{_texdir}/texmf-dist/fonts/type1/public/aurical/AuriocusKalligraphicus.pfb
%{_texdir}/texmf-dist/fonts/type1/public/aurical/AuriocusKalligraphicusBold.pfb
%{_texdir}/texmf-dist/fonts/type1/public/aurical/AuriocusKalligraphicusBoldRslant.pfb
%{_texdir}/texmf-dist/fonts/type1/public/aurical/AuriocusKalligraphicusBoldSlant.pfb
%{_texdir}/texmf-dist/fonts/type1/public/aurical/AuriocusKalligraphicusRslant.pfb
%{_texdir}/texmf-dist/fonts/type1/public/aurical/AuriocusKalligraphicusSlant.pfb
%{_texdir}/texmf-dist/fonts/type1/public/aurical/JanaSkrivana.pfb
%{_texdir}/texmf-dist/fonts/type1/public/aurical/JanaSkrivanaBold.pfb
%{_texdir}/texmf-dist/fonts/type1/public/aurical/JanaSkrivanaBoldRslant.pfb
%{_texdir}/texmf-dist/fonts/type1/public/aurical/JanaSkrivanaBoldSlant.pfb
%{_texdir}/texmf-dist/fonts/type1/public/aurical/JanaSkrivanaRslant.pfb
%{_texdir}/texmf-dist/fonts/type1/public/aurical/JanaSkrivanaSlant.pfb
%{_texdir}/texmf-dist/fonts/type1/public/aurical/LukasSvatba.pfb
%{_texdir}/texmf-dist/fonts/type1/public/aurical/LukasSvatbaBold.pfb
%{_texdir}/texmf-dist/fonts/type1/public/aurical/LukasSvatbaBoldRslant.pfb
%{_texdir}/texmf-dist/fonts/type1/public/aurical/LukasSvatbaBoldSlant.pfb
%{_texdir}/texmf-dist/fonts/type1/public/aurical/LukasSvatbaRslant.pfb
%{_texdir}/texmf-dist/fonts/type1/public/aurical/LukasSvatbaSlant.pfb
%{_texdir}/texmf-dist/tex/latex/aurical/T1AmiciLogo.fd
%{_texdir}/texmf-dist/tex/latex/aurical/T1AuriocusKalligraphicus.fd
%{_texdir}/texmf-dist/tex/latex/aurical/T1JanaSkrivana.fd
%{_texdir}/texmf-dist/tex/latex/aurical/T1LukasSvatba.fd
%{_texdir}/texmf-dist/tex/latex/aurical/aurical.sty

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/aurical/aurical.pdf
%{_texdir}/texmf-dist/doc/latex/aurical/aurical.tex

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/AmiciLogo.pfb
%{_fontdir}/AmiciLogoBold.pfb
%{_fontdir}/AmiciLogoBoldRslant.pfb
%{_fontdir}/AmiciLogoBoldSlant.pfb
%{_fontdir}/AmiciLogoRslant.pfb
%{_fontdir}/AmiciLogoSlant.pfb
%{_fontdir}/AuriocusKalligraphicus.pfb
%{_fontdir}/AuriocusKalligraphicusBold.pfb
%{_fontdir}/AuriocusKalligraphicusBoldRslant.pfb
%{_fontdir}/AuriocusKalligraphicusBoldSlant.pfb
%{_fontdir}/AuriocusKalligraphicusRslant.pfb
%{_fontdir}/AuriocusKalligraphicusSlant.pfb
%{_fontdir}/JanaSkrivana.pfb
%{_fontdir}/JanaSkrivanaBold.pfb
%{_fontdir}/JanaSkrivanaBoldRslant.pfb
%{_fontdir}/JanaSkrivanaBoldSlant.pfb
%{_fontdir}/JanaSkrivanaRslant.pfb
%{_fontdir}/JanaSkrivanaSlant.pfb
%{_fontdir}/LukasSvatba.pfb
%{_fontdir}/LukasSvatbaBold.pfb
%{_fontdir}/LukasSvatbaBoldRslant.pfb
%{_fontdir}/LukasSvatbaBoldSlant.pfb
%{_fontdir}/LukasSvatbaRslant.pfb
%{_fontdir}/LukasSvatbaSlant.pfb

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
