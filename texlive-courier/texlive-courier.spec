%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/courier.tar.xz

Name: texlive-courier
License: Freely redistributable without restriction
Summary: Adobe Type 1 "free" copies of Courier
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-courier-fedora-fonts = %{tl_version}

%description
These fonts are available under the IBM/MIT X Consortium
Courier Typefont agreement. The distribution contains PFA
outline fonts (ASCII-encoded Type 1), and AFM files.

date: 2007-03-20 00:06:44 +0100

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

%package fedora-fonts
Summary: Fonts for courier
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-courier = %{tl_version}
BuildArch: noarch

%description fedora-fonts
These fonts are available under the IBM/MIT X Consortium
Courier Typefont agreement. The distribution contains PFA
outline fonts (ASCII-encoded Type 1), and AFM files.

date: 2007-03-20 00:06:44 +0100


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/other-free.txt other-free.txt
xz -dc %{SOURCE0} | tar x -C %{buildroot}%{_texdir}/texmf-dist
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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/adobe/courier/pcrb8a.pfb .
ln -s %{_fontdir}/pcrb8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/adobe/courier/pcrb8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/adobe/courier/pcrbi8a.pfb .
ln -s %{_fontdir}/pcrbi8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/adobe/courier/pcrbi8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/adobe/courier/pcrbo8a.pfb .
ln -s %{_fontdir}/pcrbo8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/adobe/courier/pcrbo8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/adobe/courier/pcri8a.pfb .
ln -s %{_fontdir}/pcri8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/adobe/courier/pcri8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/adobe/courier/pcrr8a.pfb .
ln -s %{_fontdir}/pcrr8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/adobe/courier/pcrr8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/adobe/courier/pcrro8a.pfb .
ln -s %{_fontdir}/pcrro8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/adobe/courier/pcrro8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/courier/ucrb8a.pfb .
ln -s %{_fontdir}/ucrb8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/courier/ucrb8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/courier/ucrbo8a.pfb .
ln -s %{_fontdir}/ucrbo8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/courier/ucrbo8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb .
ln -s %{_fontdir}/ucrr8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/courier/ucrro8a.pfb .
ln -s %{_fontdir}/ucrro8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/courier/ucrro8a.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/dvips/courier/config.ucr
%{_texdir}/texmf-dist/fonts/afm/adobe/courier/pcrb8a.afm
%{_texdir}/texmf-dist/fonts/afm/adobe/courier/pcrbo8a.afm
%{_texdir}/texmf-dist/fonts/afm/adobe/courier/pcrr8a.afm
%{_texdir}/texmf-dist/fonts/afm/adobe/courier/pcrro8a.afm
%{_texdir}/texmf-dist/fonts/afm/ibm/courier/cour.afm
%{_texdir}/texmf-dist/fonts/afm/ibm/courier/courb.afm
%{_texdir}/texmf-dist/fonts/afm/ibm/courier/courbi.afm
%{_texdir}/texmf-dist/fonts/afm/ibm/courier/couri.afm
%{_texdir}/texmf-dist/fonts/afm/ibm/courier/cr-pc8.afm
%{_texdir}/texmf-dist/fonts/afm/ibm/courier/crb-pc8.afm
%{_texdir}/texmf-dist/fonts/afm/ibm/courier/crbi-pc8.afm
%{_texdir}/texmf-dist/fonts/afm/ibm/courier/cri-pc8.afm
%{_texdir}/texmf-dist/fonts/afm/urw/courier/ucrb8a.afm
%{_texdir}/texmf-dist/fonts/afm/urw/courier/ucrbo8a.afm
%{_texdir}/texmf-dist/fonts/afm/urw/courier/ucrr8a.afm
%{_texdir}/texmf-dist/fonts/afm/urw/courier/ucrro8a.afm
%{_texdir}/texmf-dist/fonts/map/dvips/courier/ucr.map
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrb.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrb7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrb8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrb8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrb8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrbc.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrbc7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrbc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrbo.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrbo7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrbo8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrbo8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrbo8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrr.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrr7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrr8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrr8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrr8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrrc.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrrc7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrrc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrro.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrro7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrro8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrro8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/pcrro8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/ccrb.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/ccrb8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/ccrbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/ccrbi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/ccrr.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/ccrr8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/ccrri.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/ccrri8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/crb10u.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/crb2n.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/crb6j.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/crb7j.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/crb8u.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/crb9t.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/cri10u.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/cri2n.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/cri6j.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/cri7j.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/cri8u.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/cri9t.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/crj10u.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/crj2n.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/crj6j.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/crj7j.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/crj8u.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/crj9t.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/crr10u.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/crr2n.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/crr6j.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/crr7j.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/crr8u.tfm
%{_texdir}/texmf-dist/fonts/tfm/cg/courier/crr9t.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/courier/pcrb8u.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/courier/pcrbc8u.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/courier/pcrbo8u.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/courier/pcrr8u.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/courier/pcrrc8u.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/courier/pcrro8u.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/courier/rpcrb.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/courier/rpcrbo.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/courier/rpcrr.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/courier/rpcrro.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/courier/ucrb7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/courier/ucrb8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/courier/ucrb8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/courier/ucrb8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/courier/ucrbc7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/courier/ucrbc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/courier/ucrbo7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/courier/ucrbo8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/courier/ucrbo8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/courier/ucrbo8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/courier/ucrr7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/courier/ucrr8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/courier/ucrr8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/courier/ucrr8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/courier/ucrrc7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/courier/ucrrc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/courier/ucrro7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/courier/ucrro8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/courier/ucrro8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/courier/ucrro8t.tfm
%{_texdir}/texmf-dist/fonts/type1/adobe/courier/pcrb8a.pfb
%{_texdir}/texmf-dist/fonts/type1/adobe/courier/pcrbi8a.pfb
%{_texdir}/texmf-dist/fonts/type1/adobe/courier/pcrbo8a.pfb
%{_texdir}/texmf-dist/fonts/type1/adobe/courier/pcri8a.pfb
%{_texdir}/texmf-dist/fonts/type1/adobe/courier/pcrr8a.pfb
%{_texdir}/texmf-dist/fonts/type1/adobe/courier/pcrro8a.pfb
%{_texdir}/texmf-dist/fonts/type1/urw/courier/ucrb8a.pfb
%{_texdir}/texmf-dist/fonts/type1/urw/courier/ucrb8a.pfm
%{_texdir}/texmf-dist/fonts/type1/urw/courier/ucrbo8a.pfb
%{_texdir}/texmf-dist/fonts/type1/urw/courier/ucrbo8a.pfm
%{_texdir}/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb
%{_texdir}/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfm
%{_texdir}/texmf-dist/fonts/type1/urw/courier/ucrro8a.pfb
%{_texdir}/texmf-dist/fonts/type1/urw/courier/ucrro8a.pfm
%{_texdir}/texmf-dist/fonts/vf/adobe/courier/pcrb.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/courier/pcrb7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/courier/pcrb8c.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/courier/pcrb8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/courier/pcrbc.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/courier/pcrbc7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/courier/pcrbc8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/courier/pcrbo.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/courier/pcrbo7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/courier/pcrbo8c.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/courier/pcrbo8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/courier/pcrr.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/courier/pcrr7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/courier/pcrr8c.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/courier/pcrr8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/courier/pcrrc.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/courier/pcrrc7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/courier/pcrrc8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/courier/pcrro.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/courier/pcrro7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/courier/pcrro8c.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/courier/pcrro8t.vf
%{_texdir}/texmf-dist/fonts/vf/cg/courier/ccrb.vf
%{_texdir}/texmf-dist/fonts/vf/cg/courier/ccrb8t.vf
%{_texdir}/texmf-dist/fonts/vf/cg/courier/ccrbi.vf
%{_texdir}/texmf-dist/fonts/vf/cg/courier/ccrbi8t.vf
%{_texdir}/texmf-dist/fonts/vf/cg/courier/ccrr.vf
%{_texdir}/texmf-dist/fonts/vf/cg/courier/ccrr8t.vf
%{_texdir}/texmf-dist/fonts/vf/cg/courier/ccrri.vf
%{_texdir}/texmf-dist/fonts/vf/cg/courier/ccrri8t.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/courier/pcrb8u.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/courier/pcrbc8u.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/courier/pcrbo8u.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/courier/pcrr8u.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/courier/pcrrc8u.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/courier/pcrro8u.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/courier/ucrb7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/courier/ucrb8c.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/courier/ucrb8t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/courier/ucrbc7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/courier/ucrbc8t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/courier/ucrbo7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/courier/ucrbo8c.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/courier/ucrbo8t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/courier/ucrr7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/courier/ucrr8c.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/courier/ucrr8t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/courier/ucrrc7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/courier/ucrrc8t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/courier/ucrro7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/courier/ucrro8c.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/courier/ucrro8t.vf
%{_texdir}/texmf-dist/tex/latex/courier/8rucr.fd
%{_texdir}/texmf-dist/tex/latex/courier/omlucr.fd
%{_texdir}/texmf-dist/tex/latex/courier/omsucr.fd
%{_texdir}/texmf-dist/tex/latex/courier/ot1ucr.fd
%{_texdir}/texmf-dist/tex/latex/courier/t1ucr.fd
%{_texdir}/texmf-dist/tex/latex/courier/ts1ucr.fd

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/pcrb8a.pfb
%{_fontdir}/pcrbi8a.pfb
%{_fontdir}/pcrbo8a.pfb
%{_fontdir}/pcri8a.pfb
%{_fontdir}/pcrr8a.pfb
%{_fontdir}/pcrro8a.pfb
%{_fontdir}/ucrb8a.pfb
%{_fontdir}/ucrbo8a.pfb
%{_fontdir}/ucrr8a.pfb
%{_fontdir}/ucrro8a.pfb

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
