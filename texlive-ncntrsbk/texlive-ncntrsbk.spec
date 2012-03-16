%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/ncntrsbk.tar.xz

Name: texlive-ncntrsbk
License: LPPL
Summary: ncntrsbk package
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-ncntrsbk-fedora-fonts = %{tl_version}

%description
ncntrsbk package

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
Summary: Fonts for ncntrsbk
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-ncntrsbk = %{tl_version}
BuildArch: noarch

%description fedora-fonts
Fonts for ncntrsbk package.


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/ncntrsbk/uncb8a.pfb .
ln -s %{_fontdir}/uncb8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/ncntrsbk/uncb8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/ncntrsbk/uncbi8a.pfb .
ln -s %{_fontdir}/uncbi8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/ncntrsbk/uncbi8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/ncntrsbk/uncr8a.pfb .
ln -s %{_fontdir}/uncr8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/ncntrsbk/uncr8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/ncntrsbk/uncri8a.pfb .
ln -s %{_fontdir}/uncri8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/ncntrsbk/uncri8a.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%{_texdir}/texmf-dist/dvips/ncntrsbk/config.unc
%{_texdir}/texmf-dist/fonts/afm/adobe/ncntrsbk/pncb8a.afm
%{_texdir}/texmf-dist/fonts/afm/adobe/ncntrsbk/pncbi8a.afm
%{_texdir}/texmf-dist/fonts/afm/adobe/ncntrsbk/pncr8a.afm
%{_texdir}/texmf-dist/fonts/afm/adobe/ncntrsbk/pncri8a.afm
%{_texdir}/texmf-dist/fonts/afm/urw/ncntrsbk/uncb8a.afm
%{_texdir}/texmf-dist/fonts/afm/urw/ncntrsbk/uncbi8a.afm
%{_texdir}/texmf-dist/fonts/afm/urw/ncntrsbk/uncr8a.afm
%{_texdir}/texmf-dist/fonts/afm/urw/ncntrsbk/uncri8a.afm
%{_texdir}/texmf-dist/fonts/map/dvips/ncntrsbk/unc.map
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncb.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncb7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncb8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncb8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncb8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncbc.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncbc7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncbc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncbi7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncbi8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncbi8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncbi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncbo.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncbo7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncbo8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncbo8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncbo8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncr.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncr7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncr8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncr8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncr8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncrc.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncrc7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncrc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncri.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncri7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncri8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncri8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncri8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncro.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncro7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncro8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncro8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/pncro8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/ncntrsbk/pncb8z.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/ncntrsbk/pncbc8z.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/ncntrsbk/pncbi8z.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/ncntrsbk/pncr8z.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/ncntrsbk/pncrc8z.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/ncntrsbk/pncri8z.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/ncntrsbk/pncrv8z.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/ncntrsbk/rpncb.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/ncntrsbk/rpncbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/ncntrsbk/rpncr.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/ncntrsbk/rpncri.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncb7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncb8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncb8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncb8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncbc7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncbc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncbi7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncbi8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncbi8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncbi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncbo7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncbo8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncbo8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncbo8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncr7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncr8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncr8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncr8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncrc7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncrc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncri7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncri8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncri8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncri8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncro7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncro8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncro8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/uncro8t.tfm
%{_texdir}/texmf-dist/fonts/type1/urw/ncntrsbk/uncb8a.pfb
%{_texdir}/texmf-dist/fonts/type1/urw/ncntrsbk/uncb8a.pfm
%{_texdir}/texmf-dist/fonts/type1/urw/ncntrsbk/uncbi8a.pfb
%{_texdir}/texmf-dist/fonts/type1/urw/ncntrsbk/uncbi8a.pfm
%{_texdir}/texmf-dist/fonts/type1/urw/ncntrsbk/uncr8a.pfb
%{_texdir}/texmf-dist/fonts/type1/urw/ncntrsbk/uncr8a.pfm
%{_texdir}/texmf-dist/fonts/type1/urw/ncntrsbk/uncri8a.pfb
%{_texdir}/texmf-dist/fonts/type1/urw/ncntrsbk/uncri8a.pfm
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncb.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncb7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncb8c.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncb8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncbc.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncbc7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncbc8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncbi.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncbi7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncbi8c.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncbi8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncbo.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncbo7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncbo8c.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncbo8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncr.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncr7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncr8c.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncr8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncrc.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncrc7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncrc8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncri.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncri7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncri8c.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncri8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncro.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncro7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncro8c.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/pncro8t.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/ncntrsbk/pncb8z.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/ncntrsbk/pncbc8z.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/ncntrsbk/pncbi8z.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/ncntrsbk/pncr8z.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/ncntrsbk/pncrc8z.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/ncntrsbk/pncri8z.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/ncntrsbk/pncrv8z.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk/uncb7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk/uncb8c.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk/uncb8t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk/uncbc7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk/uncbc8t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk/uncbi7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk/uncbi8c.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk/uncbi8t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk/uncbo7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk/uncbo8c.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk/uncbo8t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk/uncr7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk/uncr8c.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk/uncr8t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk/uncrc7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk/uncrc8t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk/uncri7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk/uncri8c.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk/uncri8t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk/uncro7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk/uncro8c.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk/uncro8t.vf
%{_texdir}/texmf-dist/tex/latex/ncntrsbk/8runc.fd
%{_texdir}/texmf-dist/tex/latex/ncntrsbk/omlunc.fd
%{_texdir}/texmf-dist/tex/latex/ncntrsbk/omsunc.fd
%{_texdir}/texmf-dist/tex/latex/ncntrsbk/ot1unc.fd
%{_texdir}/texmf-dist/tex/latex/ncntrsbk/t1unc.fd
%{_texdir}/texmf-dist/tex/latex/ncntrsbk/ts1unc.fd

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/uncb8a.pfb
%{_fontdir}/uncbi8a.pfb
%{_fontdir}/uncr8a.pfb
%{_fontdir}/uncri8a.pfb

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
