%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/texlive.infra.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/texlive.infra.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/texlive.infra.doc.tar.xz

Name: texlive-texlive.infra
License: LPPL
Summary: basic TeX Live infrastructure
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19547%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-texlive.infra-bin = %{tl_version}

%description
This package contains the files needed to get the TeX Live
tools (notably tlmgr) running: perl modules, xz binaries, plus
(sometimes) tar and wget.  These files end up in the standalone
install packages, and in the tlcritical repository.

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
Summary: Documentation for texlive.infra
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19547%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for texlive.infra


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
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
rm -f %{buildroot}/%{_texdir}/texmf/doc/man/man1/tlmgr.1
rm -f %{buildroot}/%{_texdir}/texmf/scripts/texlive/tlmgr.pl
rm -f %{buildroot}/%{_texdir}/texmf/scripts/texlive/tlmgrgui.ico
rm -f %{buildroot}/%{_texdir}/texmf/scripts/texlive/tlmgrgui.pl
rm -f %{buildroot}/%{_texdir}/texmf/scripts/texlive/uninstall-win32.pl
mkdir -p %{buildroot}/%{_datadir}/
mv %{buildroot}/%{_texdir}/texmf/doc/man %{buildroot}/%{_datadir}/

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%{_texdir}/texmf/web2c/fmtutil-hdr.cnf
%{_texdir}/texmf/web2c/updmap-hdr.cfg
%{_texdir}/LICENSE.CTAN
%{_texdir}/LICENSE.TL
%{_texdir}/README
%{_texdir}/README.usergroups
%{_texdir}/index.html
%{_texdir}/release-texlive.txt
%{_texdir}/readme-html.dir/readme.cs.html
%{_texdir}/readme-html.dir/readme.de.html
%{_texdir}/readme-html.dir/readme.en.html
%{_texdir}/readme-html.dir/readme.fr.html
%{_texdir}/readme-html.dir/readme.it.html
%{_texdir}/readme-html.dir/readme.ja.html
%{_texdir}/readme-html.dir/readme.pl.html
%{_texdir}/readme-html.dir/readme.ru.html
%{_texdir}/readme-html.dir/readme.sr.html
%{_texdir}/readme-html.dir/readme.zh-cn.html
%{_texdir}/readme-txt.dir/README.CS
%{_texdir}/readme-txt.dir/README.DE
%{_texdir}/readme-txt.dir/README.EN
%{_texdir}/readme-txt.dir/README.FR
%{_texdir}/readme-txt.dir/README.IT
%{_texdir}/readme-txt.dir/README.JA
%{_texdir}/readme-txt.dir/README.PL
%{_texdir}/readme-txt.dir/README.RU
%{_texdir}/readme-txt.dir/README.RU-cp1251
%{_texdir}/readme-txt.dir/README.RU-koi8
%{_texdir}/readme-txt.dir/README.SK-ascii
%{_texdir}/readme-txt.dir/README.SK-cp1250
%{_texdir}/readme-txt.dir/README.SK-il2
%{_texdir}/readme-txt.dir/README.SR
%{_texdir}/readme-txt.dir/README.ZH-CN
%{_texdir}/tlpkg/TeXLive/Splashscreen.pm
%{_texdir}/tlpkg/TeXLive/TLConfFile.pm
%{_texdir}/tlpkg/TeXLive/TLConfig.pm
%{_texdir}/tlpkg/TeXLive/TLDownload.pm
#%{_texdir}/tlpkg/TeXLive/TLMedia.pm
%{_texdir}/tlpkg/TeXLive/TLPDB.pm
%{_texdir}/tlpkg/TeXLive/TLPOBJ.pm
%{_texdir}/tlpkg/TeXLive/TLPSRC.pm
%{_texdir}/tlpkg/TeXLive/TLPaper.pm
%{_texdir}/tlpkg/TeXLive/TLTREE.pm
%{_texdir}/tlpkg/TeXLive/TLUtils.pm
%{_texdir}/tlpkg/TeXLive/TLWinGoo.pm
%{_texdir}/tlpkg/TeXLive/TeXCatalogue.pm
%{_texdir}/tlpkg/TeXLive/trans.pl
%{_texdir}/tlpkg/TeXLive/waitVariableX.pm
%{_texdir}/tlpkg/installer/config.guess

%files doc
%defattr(-,root,root)
%{_texdir}/texmf/scripts/texlive/NEWS
%{_texdir}/tlpkg/README
%{_texdir}/tlpkg/installer/COPYING.MinGW-runtime.txt

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
