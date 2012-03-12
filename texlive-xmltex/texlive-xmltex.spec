%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/xmltex.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/xmltex.doc.tar.xz

Name: texlive-xmltex
License: LPPL
Summary: Support for parsing XML documents
Version: %{tl_version}
Release: %{tl_noarch_release}.0.8.svn18835%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-pdftex = %{tl_version}
Requires: texlive-tex = %{tl_version}
Requires: texlive-xmltex-bin = %{tl_version}

%description
This package provides an implementation of a parser for
documents matching the XML 1.0 and XML Namespace
Recommendations. In addition to parsing commands are provided
to attatch TeX typesetting instructions to the various markup
elemenets as they are encounted. Sample files for typesetting a
subset of TEI, MathML, are included. Element and Attribute
names, as well as character data, may use any characters
allowed in XML, using UTF-8 or a suitable 8-bit encoding.

date: 2006-12-16 17:11:43 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
sed -i 's/^\#\!\ xmltex/xmltex pdftex language.dat *xmltex.ini/' %{_texdir}/texmf/web2c/fmtutil.cnf
sed -i 's/^\#\!\ pdfxmltex/pdfxmltex pdftex language.dat *pdfxmltex.ini/' %{_texdir}/texmf/web2c/fmtutil.cnf
touch /var/run/texlive/run-fmtutil
:

%postun
if [ $1 == 0 ]; then
  sed -i 's/^xmltex/\#\!\ xmltex/' %{_texdir}/texmf/web2c/fmtutil.cnf
  sed -i 's/^pdfxmltex/\#\!\ pdfxmltex/' %{_texdir}/texmf/web2c/fmtutil.cnf
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
Summary: Documentation for xmltex
Version: %{tl_version}
Release: %{tl_noarch_release}.0.8.svn18835%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch
Requires: texlive-pdftex-doc

%description doc
Documentation for xmltex


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/lppl.txt lppl.txt
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
%doc lppl.txt
%{_texdir}/texmf-dist/tex/xmltex/base/iso-8859-1.xmt
%{_texdir}/texmf-dist/tex/xmltex/base/iso-8859-2.xmt
%{_texdir}/texmf-dist/tex/xmltex/base/koi8-r.xmt
%{_texdir}/texmf-dist/tex/xmltex/base/langtest.xmt
%{_texdir}/texmf-dist/tex/xmltex/base/mathml2.xmt
%{_texdir}/texmf-dist/tex/xmltex/base/sec.xmt
%{_texdir}/texmf-dist/tex/xmltex/base/utf-16.xmt
%{_texdir}/texmf-dist/tex/xmltex/base/windows-1250.xmt
%{_texdir}/texmf-dist/tex/xmltex/base/xmltex.cfg
%{_texdir}/texmf-dist/tex/xmltex/base/xmltex.tex
%{_texdir}/texmf-dist/tex/xmltex/config/pdfxmltex.ini
%{_texdir}/texmf-dist/tex/xmltex/config/xmltex.ini

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/otherformats/xmltex/base/englishutf16.xml
%{_texdir}/texmf-dist/doc/otherformats/xmltex/base/englishutf8.xml
%{_texdir}/texmf-dist/doc/otherformats/xmltex/base/langtest.xml
%{_texdir}/texmf-dist/doc/otherformats/xmltex/base/manual.html
%{_texdir}/texmf-dist/doc/otherformats/xmltex/base/manual.tex
%{_texdir}/texmf-dist/doc/otherformats/xmltex/base/manual.xml
%{_texdir}/texmf-dist/doc/otherformats/xmltex/base/manual.xsl
%{_texdir}/texmf-dist/doc/otherformats/xmltex/base/portugeselatin1.xml
%{_texdir}/texmf-dist/doc/otherformats/xmltex/base/readme.txt
%{_texdir}/texmf-dist/doc/otherformats/xmltex/base/russiankoi8.xml
%{_texdir}/texmf-dist/doc/otherformats/xmltex/base/russianutf8.xml
%{_texdir}/texmf-dist/doc/otherformats/xmltex/base/testascii.cfg
%{_texdir}/texmf-dist/doc/otherformats/xmltex/base/testascii.tex
%{_texdir}/texmf-dist/doc/otherformats/xmltex/base/testascii.xml
%{_texdir}/texmf-dist/doc/otherformats/xmltex/base/testsec.tex
%{_texdir}/texmf-dist/doc/otherformats/xmltex/base/testsec.xml


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
