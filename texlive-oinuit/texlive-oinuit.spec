%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/oinuit.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/oinuit.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/oinuit.source.tar.xz

Name: texlive-oinuit
License: LPPL
Summary: LaTeX Support for the Inuktitut Language
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(oinuit.sty)
Requires: texlive-oinuit-fedora-fonts = %{tl_version}

%description
The oinuit system is a set of Lambda (Omega LaTeX) typesetting
tools for the Inuktitut language. The oinuit package supports
five different input methods and is bundled with the necessary
fonts.

date: 2007-02-23 22:01:12 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map oinuit.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map oinuit.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for oinuit
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for oinuit

%package fedora-fonts
Summary: Fonts for oinuit
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-oinuit = %{tl_version}
BuildArch: noarch

%description fedora-fonts
The oinuit system is a set of Lambda (Omega LaTeX) typesetting
tools for the Inuktitut language. The oinuit package supports
five different input methods and is bundled with the necessary
fonts.

date: 2007-02-23 22:01:12 +0100


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/oinuit/Inuit.pfb .
ln -s %{_fontdir}/Inuit.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/oinuit/Inuit.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/oinuit/Inuitb.pfb .
ln -s %{_fontdir}/Inuitb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/oinuit/Inuitb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/oinuit/Inuitbo.pfb .
ln -s %{_fontdir}/Inuitbo.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/oinuit/Inuitbo.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/oinuit/Inuito.pfb .
ln -s %{_fontdir}/Inuito.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/oinuit/Inuito.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/oinuit/cmssbxo10.pfb .
ln -s %{_fontdir}/cmssbxo10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/oinuit/cmssbxo10.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/fonts/map/dvips/oinuit/oinuit.map
%{_texdir}/texmf-dist/fonts/ofm/public/oinuit/OInuit.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/oinuit/OInuitb.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/oinuit/OInuitbo.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/oinuit/OInuito.ofm
%{_texdir}/texmf-dist/fonts/ovf/public/oinuit/OInuit.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/oinuit/OInuitb.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/oinuit/OInuitbo.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/oinuit/OInuito.ovf
%{_texdir}/texmf-dist/fonts/tfm/public/oinuit/Inuit.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oinuit/Inuitb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oinuit/Inuitbo.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oinuit/Inuito.tfm
%{_texdir}/texmf-dist/fonts/type1/public/oinuit/Inuit.pfb
%{_texdir}/texmf-dist/fonts/type1/public/oinuit/Inuitb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/oinuit/Inuitbo.pfb
%{_texdir}/texmf-dist/fonts/type1/public/oinuit/Inuito.pfb
%{_texdir}/texmf-dist/fonts/type1/public/oinuit/cmssbxo10.pfb
%{_texdir}/texmf-dist/omega/ocp/oinuit/Ninuit2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/oinuit/Qinuit2uni.ocp
%{_texdir}/texmf-dist/omega/ocp/oinuit/inuitscii.ocp
%{_texdir}/texmf-dist/tex/lambda/oinuit/oinuit.sty

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/fonts/oinuit/README.1ST
%{_texdir}/texmf-dist/doc/fonts/oinuit/examples/book.tex
%{_texdir}/texmf-dist/doc/fonts/oinuit/examples/taqtu.tex

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/Inuit.pfb
%{_fontdir}/Inuitb.pfb
%{_fontdir}/Inuitbo.pfb
%{_fontdir}/Inuito.pfb
%{_fontdir}/cmssbxo10.pfb

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
