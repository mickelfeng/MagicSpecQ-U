%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/aleph.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/aleph.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/aleph.doc.tar.xz

Name: texlive-aleph
License: GPL+
Summary: Extended TeX
Version: %{tl_version}
Release: %{tl_noarch_release}.RC2.svn18835%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-aleph-bin = %{tl_version}

%description
An development of omega, using most of the extensions of TeX
itself developed for e-TeX.

date: 2009-11-09 13:03:38 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
sed -i 's/^\#\!\ aleph/aleph aleph - *aleph.ini/' %{_texdir}/texmf/web2c/fmtutil.cnf
sed -i 's/^\#\!\ lamed/lamed aleph language.dat *lambda.ini/' %{_texdir}/texmf/web2c/fmtutil.cnf
touch /var/run/texlive/run-fmtutil
:

%postun
if [ $1 == 0 ]; then
  sed -i 's/^aleph/\#\!\ aleph/' %{_texdir}/texmf/web2c/fmtutil.cnf
  sed -i 's/^lamed/\#\!\ lamed/' %{_texdir}/texmf/web2c/fmtutil.cnf
  %{_bindir}/texhash 2> /dev/null
  %{_bindir}/fmtutil-sys --missing &> /dev/null
else
  mkdir -p /var/run/texlive
  touch /var/run/texlive/run-texhash
  touch /var/run/texlive/run-fmtutil
fi
:

%posttrans
[ -e /var/run/texlive/run-texhash ] && %{_bindir}/texhash 2> /dev/null && rm -f /var/run/texlive/run-texhash
[ -e /var/run/texlive/run-fmtutil ] && %{_bindir}/fmtutil-sys --missing &> /dev/null && rm -f /var/run/texlive/run-fmtutil
[ -e /var/run/texlive ] && rm -rf /var/run/texlive
:

%package doc
Summary: Documentation for aleph
Version: %{tl_version}
Release: %{tl_noarch_release}.RC2.svn18835%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for aleph


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/gpl.txt gpl.txt
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
mkdir -p %{buildroot}/%{_datadir}/
mv %{buildroot}/%{_texdir}/texmf/doc/man %{buildroot}/%{_datadir}/

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gpl.txt
%{_mandir}/man1/aleph.1*
%{_mandir}/man1/lamed.1*

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/aleph/base/News
%{_texdir}/texmf-dist/doc/aleph/base/readme.txt


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
