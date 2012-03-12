%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/epigrafica.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/epigrafica.doc.tar.xz

Name: texlive-epigrafica
License: GPL+
Summary: A Greek and Latin font
Version: %{tl_version}
Release: %{tl_noarch_release}.1.01.svn17210%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(epigrafica.sty)
Requires: tex(pxfonts.sty)
Requires: texlive-epigrafica-fedora-fonts = %{tl_version}

%description
Epigrafica is forked from the development of the MgOpen font
Cosmetica, which is a similar design to Optima and includes
Greek. Development has been supported by the Laboratory of
Digital Typography and Mathematical Software, of the Department
of Mathematics of the University of the Aegean, Greece.

date: 2010-02-24 20:55:02 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map epigrafica.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map epigrafica.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for epigrafica
Version: %{tl_version}
Release: %{tl_noarch_release}.1.01.svn17210%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for epigrafica

%package fedora-fonts
Summary: Fonts for epigrafica
Version: %{tl_version}
Release: %{tl_noarch_release}.1.01.svn17210%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-epigrafica = %{tl_version}
BuildArch: noarch

%description fedora-fonts
Epigrafica is forked from the development of the MgOpen font
Cosmetica, which is a similar design to Optima and includes
Greek. Development has been supported by the Laboratory of
Digital Typography and Mathematical Software, of the Department
of Mathematics of the University of the Aegean, Greece.

date: 2010-02-24 20:55:02 +0100


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/epigrafica/Epigrafica-Entona.pfb .
ln -s %{_fontdir}/Epigrafica-Entona.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/epigrafica/Epigrafica-Entona.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/epigrafica/Epigrafica-EntonaReonta.pfb .
ln -s %{_fontdir}/Epigrafica-EntonaReonta.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/epigrafica/Epigrafica-EntonaReonta.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/epigrafica/Epigrafica-Ortha.pfb .
ln -s %{_fontdir}/Epigrafica-Ortha.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/epigrafica/Epigrafica-Ortha.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/epigrafica/Epigrafica-Pezokefalaia.pfb .
ln -s %{_fontdir}/Epigrafica-Pezokefalaia.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/epigrafica/Epigrafica-Pezokefalaia.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/epigrafica/Epigrafica-Reonta.pfb .
ln -s %{_fontdir}/Epigrafica-Reonta.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/epigrafica/Epigrafica-Reonta.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/fonts/afm/public/epigrafica/Epigrafica-Entona.afm
%{_texdir}/texmf-dist/fonts/afm/public/epigrafica/Epigrafica-EntonaReonta.afm
%{_texdir}/texmf-dist/fonts/afm/public/epigrafica/Epigrafica-Ortha.afm
%{_texdir}/texmf-dist/fonts/afm/public/epigrafica/Epigrafica-Pezokefalaia.afm
%{_texdir}/texmf-dist/fonts/afm/public/epigrafica/Epigrafica-Reonta.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/epigrafica/epigraficahellenic.enc
%{_texdir}/texmf-dist/fonts/map/dvips/epigrafica/epigrafica.map
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficab8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficab8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficabi8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficabi8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficabo8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficabo8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficac8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficac8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficahb7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficahb7r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficahbi7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficahbi7r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficahbo7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficahbo7r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficahc7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficahc7r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficahi7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficahi7r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficahn7r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficaho7a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficaho7r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficai8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficai8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigrafican8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigrafican8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficao8a.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/epigraficao8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/gepigraficahn7a.tfm
%{_texdir}/texmf-dist/fonts/type1/public/epigrafica/Epigrafica-Entona.pfb
%{_texdir}/texmf-dist/fonts/type1/public/epigrafica/Epigrafica-EntonaReonta.pfb
%{_texdir}/texmf-dist/fonts/type1/public/epigrafica/Epigrafica-Ortha.pfb
%{_texdir}/texmf-dist/fonts/type1/public/epigrafica/Epigrafica-Pezokefalaia.pfb
%{_texdir}/texmf-dist/fonts/type1/public/epigrafica/Epigrafica-Reonta.pfb
%{_texdir}/texmf-dist/fonts/vf/public/epigrafica/epigraficab8r.vf
%{_texdir}/texmf-dist/fonts/vf/public/epigrafica/epigraficabi8r.vf
%{_texdir}/texmf-dist/fonts/vf/public/epigrafica/epigraficabo8r.vf
%{_texdir}/texmf-dist/fonts/vf/public/epigrafica/epigraficac8r.vf
%{_texdir}/texmf-dist/fonts/vf/public/epigrafica/epigraficahb7r.vf
%{_texdir}/texmf-dist/fonts/vf/public/epigrafica/epigraficahbi7r.vf
%{_texdir}/texmf-dist/fonts/vf/public/epigrafica/epigraficahbo7r.vf
%{_texdir}/texmf-dist/fonts/vf/public/epigrafica/epigraficahc7r.vf
%{_texdir}/texmf-dist/fonts/vf/public/epigrafica/epigraficahi7r.vf
%{_texdir}/texmf-dist/fonts/vf/public/epigrafica/epigraficahn7r.vf
%{_texdir}/texmf-dist/fonts/vf/public/epigrafica/epigraficaho7r.vf
%{_texdir}/texmf-dist/fonts/vf/public/epigrafica/epigraficai8r.vf
%{_texdir}/texmf-dist/fonts/vf/public/epigrafica/epigrafican8r.vf
%{_texdir}/texmf-dist/fonts/vf/public/epigrafica/epigraficao8r.vf
%{_texdir}/texmf-dist/tex/latex/epigrafica/epigrafica.sty
%{_texdir}/texmf-dist/tex/latex/epigrafica/lgrepigrafica.fd
%{_texdir}/texmf-dist/tex/latex/epigrafica/ot1epigrafica.fd

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/fonts/epigrafica/README
%{_texdir}/texmf-dist/doc/fonts/epigrafica/doc.zip
%{_texdir}/texmf-dist/doc/fonts/epigrafica/epigrafica.pdf
%{_texdir}/texmf-dist/doc/fonts/epigrafica/epigrafica.tex

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/Epigrafica-Entona.pfb
%{_fontdir}/Epigrafica-EntonaReonta.pfb
%{_fontdir}/Epigrafica-Ortha.pfb
%{_fontdir}/Epigrafica-Pezokefalaia.pfb
%{_fontdir}/Epigrafica-Reonta.pfb

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
