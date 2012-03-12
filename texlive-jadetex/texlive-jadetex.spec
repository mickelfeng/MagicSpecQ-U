%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/jadetex.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/jadetex.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/jadetex.source.tar.xz

Name: texlive-jadetex
License: Freely redistributable without restriction
Summary: Macros supporting Jade DSSSL output
Version: %{tl_version}
Release: %{tl_noarch_release}.3.13.svn18835%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-pdftex = %{tl_version}
Requires: texlive-tex = %{tl_version}
Requires: texlive-jadetex-bin = %{tl_version}
Provides: tex(uentities.sty)

%description
Macro package on top of LaTeX to typeset TeX output of the Jade
DSSSL implementation.

date: 2008-04-20 19:53:04 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
sed -i 's/^\#\!\ jadetex/jadetex pdftex language.dat *jadetex.ini/' %{_texdir}/texmf/web2c/fmtutil.cnf
sed -i 's/^\#\!\ pdfjadetex/pdfjadetex pdftex language.dat *pdfjadetex.ini/' %{_texdir}/texmf/web2c/fmtutil.cnf
touch /var/run/texlive/run-fmtutil
:

%postun
if [ $1 == 0 ]; then
  sed -i 's/^jadetex/\#\!\ jadetex/' %{_texdir}/texmf/web2c/fmtutil.cnf
  sed -i 's/^pdfjadetex/\#\!\ pdfjadetex/' %{_texdir}/texmf/web2c/fmtutil.cnf
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
Summary: Documentation for jadetex
Version: %{tl_version}
Release: %{tl_noarch_release}.3.13.svn18835%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch
Requires: texlive-pdftex-doc

%description doc
Documentation for jadetex


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/other-free.txt other-free.txt
xz -dc %{SOURCE0} | tar x -C %{buildroot}%{_texdir}
xz -dc %{SOURCE1} | tar x -C %{buildroot}%{_texdir}
# nuke useless tlmgr packaging stuff and doc droppings
rm -rf %{buildroot}%{_texdir}/tlpkg/tlpobj/
rm -rf %{buildroot}%{_texdir}/texmf-dist/tlpkg/tlpobj/
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/man*/*.pdf
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/Makefile
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/man*/Makefile
rm -rf %{buildroot}%{_texdir}/texmf/doc/info/dir

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/tex/jadetex/base/dsssl.def
%{_texdir}/texmf-dist/tex/jadetex/base/jadetex.ini
%{_texdir}/texmf-dist/tex/jadetex/base/jadetex.ltx
%{_texdir}/texmf-dist/tex/jadetex/base/pdfjadetex.ini
%{_texdir}/texmf-dist/tex/jadetex/base/uentities.sty
%{_texdir}/texmf-dist/tex/jadetex/base/ut1omlgc.fd

%files doc
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/doc/otherformats/jadetex/base/ChangeLog
%{_texdir}/texmf-dist/doc/otherformats/jadetex/base/ChangeLog-old
%{_texdir}/texmf-dist/doc/otherformats/jadetex/base/Makefile
%{_texdir}/texmf-dist/doc/otherformats/jadetex/base/demo.sgm
%{_texdir}/texmf-dist/doc/otherformats/jadetex/base/docbook.dsl
%{_texdir}/texmf-dist/doc/otherformats/jadetex/base/index.html
%{_texdir}/texmf-dist/doc/otherformats/jadetex/base/index.xml
%{_texdir}/texmf-dist/doc/otherformats/jadetex/base/index.xsl
%{_texdir}/texmf-dist/doc/otherformats/jadetex/base/jadetex.1
%{_texdir}/texmf-dist/doc/otherformats/jadetex/base/jadetex.cfg
%{_texdir}/texmf-dist/doc/otherformats/jadetex/base/logo.png
%{_texdir}/texmf-dist/doc/otherformats/jadetex/base/pdfjadetex.1
%{_texdir}/texmf-dist/doc/otherformats/jadetex/base/releasenotes.dsl
%{_texdir}/texmf-dist/doc/otherformats/jadetex/base/releasenotes.xml


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
