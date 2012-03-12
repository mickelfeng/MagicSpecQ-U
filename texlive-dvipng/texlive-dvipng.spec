%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/dvipng.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/dvipng.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/dvipng.doc.tar.xz

Name: texlive-dvipng
License: LGPLv2+
Summary: A fast DVI to PNG/GIF converter
Version: %{tl_version}
Release: %{tl_noarch_release}.1.13.svn19010%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires(preun,post): /sbin/install-info
Requires: texlive-dvipng-bin = %{tl_version}

%description
This program makes PNG and/or GIF graphics from DVI files as
obtained from TeX and its relatives. Its benefits include: -
Speed. It offers very fast rendering of DVI as bitmap files,
which makes it suitable for generating large amounts of images
on-the-fly, as needed in preview-latex, WeBWorK and others; -
It does not read the postamble, so it can be started before TeX
finishes. There is a --follow switch that makes dvipng wait at
end-of-file for further output, unless it finds the POST marker
that indicates the end of the DVI; - Interactive query of
options. dvipng can read options interactively through stdin,
and all options are usable. It is even possible to change the
input file through this interface. - Support for PK, VF,
PostScript Type1, and TrueType fonts, colour specials, and
inclusion of PostScript, PNG, JPEG or GIF images.

date: 2010-03-18 08:38:46 +0100

%preun
if [ "$1" = "0" ]; then
  /sbin/install-info --delete %{_infodir}/dvipng.info %{_infodir}/dir 2>/dev/null || :
fi

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
/sbin/install-info %{_infodir}/dvipng.info %{_infodir}/dir 2>/dev/null
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
Summary: Documentation for dvipng
Version: %{tl_version}
Release: %{tl_noarch_release}.1.13.svn19010%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for dvipng


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/lgpl.txt lgpl.txt
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
mkdir -p %{buildroot}/%{_infodir}/
mv %{buildroot}/%{_texdir}/texmf/doc/info/* %{buildroot}/%{_infodir}/

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lgpl.txt
%{_mandir}/man1/dvigif.1*
%{_mandir}/man1/dvipng.1*
%{_infodir}/dvipng.info*

%files doc
%defattr(-,root,root)
%doc lgpl.txt
%{_texdir}/texmf/doc/dvipng/dvipng.html
%{_texdir}/texmf/doc/dvipng/dvipng.pdf


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
