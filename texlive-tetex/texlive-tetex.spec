%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/tetex.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/tetex.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/tetex.doc.tar.xz

Name: texlive-tetex
License: Freely redistributable without restriction
Summary: scripts and files originally written for or included in teTeX
Version: %{tl_version}
Release: %{tl_noarch_release}.3.0.svn19496%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}

%description
teTeX was a comprehensive distribution of TeX, LaTeX and
family, designed to for ease of compilation, installation and
customisation. In 2006, Thomas Esser announced he would no
longer be able to support, or to produce new versions of,
teTeX. With the appearance of TeX live 2007 (whose Unix-system
TeX support originally derived from teTeX), no-one should be
using teTeX at all, in new applications. One of the "schemes"
available when installing TeX live provides a configuration
very close to that of the old teTeX, but using modern versions
of programs and packages.

date: 2009-11-10 12:26:23 +0100

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
Summary: Documentation for tetex
Version: %{tl_version}
Release: %{tl_noarch_release}.3.0.svn19496%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for tetex


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/other-free.txt other-free.txt
xz -dc %{SOURCE0} | tar x -C %{buildroot}%{_texdir}
xz -dc %{SOURCE1} | tar x -C %{buildroot}%{_texdir}
xz -dc %{SOURCE2} | tar x -C %{buildroot}%{_texdir}
# nuke useless tlmgr packaging stuff and doc droppings
rm -rf %{buildroot}%{_texdir}/tlpkg/tlpobj/
rm -rf %{buildroot}%{_texdir}/texmf-dist/tlpkg/tlpobj/
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/man*/*.pdf
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/Makefile
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/man*/Makefile
rm -rf %{buildroot}%{_texdir}/texmf/doc/info/dir

# disable all Maps/MixedMaps we add them by scriptlets
sed -i '/^M/d' %{buildroot}%{_texdir}/texmf/web2c/updmap.cfg
mkdir -p %{buildroot}/%{_datadir}/
mv %{buildroot}/%{_texdir}/texmf/doc/man %{buildroot}/%{_datadir}/

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc other-free.txt
%{_mandir}/man1/allcm.1*
%{_mandir}/man1/allec.1*
%{_mandir}/man1/allneeded.1*
%{_mandir}/man1/dvi2fax.1*
%{_mandir}/man1/dvired.1*
%{_mandir}/man1/fmtutil-sys.1*
%{_mandir}/man1/fmtutil.1*
%{_mandir}/man1/texlinks.1*
%{_mandir}/man1/updmap-sys.1*
%{_mandir}/man1/updmap.1*
%config(noreplace) %{_texdir}/texmf/web2c/updmap.cfg
%{_texdir}/texmf/scripts/tetex/updmap.pl
%{_mandir}/man5/fmtutil.cnf.5*
%{_mandir}/man5/updmap.cfg.5*
%{_texdir}/texmf/dvips/tetex/config.builtin35
%{_texdir}/texmf/dvips/tetex/config.dfaxhigh
%{_texdir}/texmf/dvips/tetex/config.dfaxlo
%{_texdir}/texmf/dvips/tetex/config.download35
%{_texdir}/texmf/dvips/tetex/config.gsftopk
%{_texdir}/texmf/dvips/tetex/config.outline
%{_texdir}/texmf/dvips/tetex/config.pdf
%{_texdir}/texmf/dvips/tetex/config.pk
%{_texdir}/texmf/dvips/tetex/config.www
%{_texdir}/texmf/fonts/enc/dvips/tetex/09fbbfac.enc
%{_texdir}/texmf/fonts/enc/dvips/tetex/0ef0afca.enc
%{_texdir}/texmf/fonts/enc/dvips/tetex/10037936.enc
%{_texdir}/texmf/fonts/enc/dvips/tetex/1b6d048e.enc
%{_texdir}/texmf/fonts/enc/dvips/tetex/71414f53.enc
%{_texdir}/texmf/fonts/enc/dvips/tetex/74afc74c.enc
%{_texdir}/texmf/fonts/enc/dvips/tetex/aae443f0.enc
%{_texdir}/texmf/fonts/enc/dvips/tetex/b6a4d7c7.enc
%{_texdir}/texmf/fonts/enc/dvips/tetex/bbad153f.enc
%{_texdir}/texmf/fonts/enc/dvips/tetex/d9b29452.enc
%{_texdir}/texmf/fonts/enc/dvips/tetex/f7b6d320.enc
%{_texdir}/texmf/fonts/enc/dvips/tetex/mtex.enc
%{_texdir}/texmf/fonts/map/dvips/tetex/dvipdfm35.map
%{_texdir}/texmf/fonts/map/dvips/tetex/dvips35.map
%{_texdir}/texmf/fonts/map/dvips/tetex/mathpple.map
%{_texdir}/texmf/fonts/map/dvips/tetex/pdftex35.map
%{_texdir}/texmf/fonts/map/dvips/tetex/ps2pk35.map
%{_texdir}/texmf/fonts/map/dvips/tetex/README
%{_texdir}/texmf/scripts/tetex/updmap-sys.sh

%files doc
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf/doc/tetex/TETEXDOC.pdf
%{_texdir}/texmf/doc/tetex/teTeX-FAQ


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
