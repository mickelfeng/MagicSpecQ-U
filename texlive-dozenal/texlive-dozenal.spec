%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/dozenal.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/dozenal.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/dozenal.source.tar.xz

Name: texlive-dozenal
License: LPPL
Summary: Typeset documents using base twelve numbering (also called "dozenal")
Version: %{tl_version}
Release: %{tl_noarch_release}.3.1.svn16193%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(dozenal.sty)
Requires: tex(fixltx2e.sty)
Requires: texlive-dozenal-fedora-fonts = %{tl_version}

%description
The package supports typesetting documents whose counters are
represented in base twelve, also called "dozenal". It includes
a macro by David Kastrup for converting positive whole numbers
to dozenal from decimal (base ten) representation. The package
also also includes a few other macros and redefines all the
standard counters to produce dozenal output. Fonts, in Roman,
italic, slanted, and boldface versions, provide ten and eleven
(the Pitman characters preferred by the Dozenal Society of
Great Britain). The fonts were designed to blend well with the
Computer Modern fonts, and are available both as MetaFont
source and in Adobe Type 1 format.

date: 2009-11-26 10:36:51 +0100

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
Summary: Documentation for dozenal
Version: %{tl_version}
Release: %{tl_noarch_release}.3.1.svn16193%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for dozenal

%package fedora-fonts
Summary: Fonts for dozenal
Version: %{tl_version}
Release: %{tl_noarch_release}.3.1.svn16193%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-dozenal = %{tl_version}
BuildArch: noarch

%description fedora-fonts
The package supports typesetting documents whose counters are
represented in base twelve, also called "dozenal". It includes
a macro by David Kastrup for converting positive whole numbers
to dozenal from decimal (base ten) representation. The package
also also includes a few other macros and redefines all the
standard counters to produce dozenal output. Fonts, in Roman,
italic, slanted, and boldface versions, provide ten and eleven
(the Pitman characters preferred by the Dozenal Society of
Great Britain). The fonts were designed to blend well with the
Computer Modern fonts, and are available both as MetaFont
source and in Adobe Type 1 format.

date: 2009-11-26 10:36:51 +0100


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/dozenal/fdzb8a.pfb .
ln -s %{_fontdir}/fdzb8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/dozenal/fdzb8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/dozenal/fdzbi8a.pfb .
ln -s %{_fontdir}/fdzbi8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/dozenal/fdzbi8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/dozenal/fdzbs8a.pfb .
ln -s %{_fontdir}/fdzbs8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/dozenal/fdzbs8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/dozenal/fdzi8a.pfb .
ln -s %{_fontdir}/fdzi8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/dozenal/fdzi8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/dozenal/fdzr8a.pfb .
ln -s %{_fontdir}/fdzr8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/dozenal/fdzr8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/dozenal/fdzs8a.pfb .
ln -s %{_fontdir}/fdzs8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/dozenal/fdzs8a.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/fonts/map/dvips/dozenal/fdz.map
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchars10.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchars12.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchars17.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchars6.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchars7.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchars8.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchars9.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchb10.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchbx10.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchbx12.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchbx5.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchbx6.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchbx7.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchbx8.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchbx9.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchbxi10.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchbxsl10.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchit10.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchit12.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchit7.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchit8.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchit9.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchsl10.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchsl12.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchsl8.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozchsl9.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozenal.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozenalb.mf
%{_texdir}/texmf-dist/fonts/source/public/dozenal/dozenali.mf
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchars10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchars12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchars17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchars6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchars7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchars8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchars9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchbx12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchbx5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchbx6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchbx7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchbx8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchbx9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchbxi10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchbxsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchit10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchit12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchit7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchit8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchit9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchsl12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchsl8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/dozchsl9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzb7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzb8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzb8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzb8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzb8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzbc7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzbc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzbi7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzbi8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzbi8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzbi8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzbi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzbo7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzbo8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzbo8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzbo8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzbs8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzi8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzr7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzr8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzr8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzr8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzr8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzrc7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzrc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzro7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzro8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzro8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzro8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzs7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzs8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzs8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzs8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzs8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzsc7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzsc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzso7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzso8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzso8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/fdzso8t.tfm
%{_texdir}/texmf-dist/fonts/type1/public/dozenal/fdzb8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/dozenal/fdzbi8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/dozenal/fdzbs8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/dozenal/fdzi8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/dozenal/fdzr8a.pfb
%{_texdir}/texmf-dist/fonts/type1/public/dozenal/fdzs8a.pfb
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzb7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzb8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzb8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzbc7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzbc8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzbi7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzbi8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzbi8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzbo7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzbo8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzbo8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzr7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzr8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzr8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzrc7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzrc8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzro7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzro8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzro8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzs7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzs8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzs8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzsc7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzsc8t.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzso7t.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzso8c.vf
%{_texdir}/texmf-dist/fonts/vf/public/dozenal/fdzso8t.vf
%{_texdir}/texmf-dist/tex/latex/dozenal/dozenal.sty

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/fonts/dozenal/README
%{_texdir}/texmf-dist/doc/fonts/dozenal/dozenal.pdf
%{_texdir}/texmf-dist/doc/fonts/dozenal/testdozchars.tex
%{_texdir}/texmf-dist/doc/fonts/dozenal/testfdzchars.tex

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/fdzb8a.pfb
%{_fontdir}/fdzbi8a.pfb
%{_fontdir}/fdzbs8a.pfb
%{_fontdir}/fdzi8a.pfb
%{_fontdir}/fdzr8a.pfb
%{_fontdir}/fdzs8a.pfb

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
