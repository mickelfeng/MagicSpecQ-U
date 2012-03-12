%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/fontname.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/fontname.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/fontname.doc.tar.xz

Name: texlive-fontname
License: GPL+
Summary: Scheme for naming fonts in TeX
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19515%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires(preun,post): /sbin/install-info

%description
The scheme for assigning names is described (in the
documentation part of the package), and map files giving the
relation between foundry name and 'TeX-name' are also provided.

date: 2010-07-18 10:12:55 +0200

%preun
if [ "$1" = "0" ]; then
  /sbin/install-info --delete %{_infodir}/fontname.info %{_infodir}/dir 2>/dev/null || :
fi

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
/sbin/install-info %{_infodir}/fontname.info %{_infodir}/dir 2>/dev/null
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
Summary: Documentation for fontname
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19515%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for fontname


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
mkdir -p %{buildroot}/%{_infodir}/
mv %{buildroot}/%{_texdir}/texmf/doc/info/* %{buildroot}/%{_infodir}/

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gpl.txt
%{_infodir}/fontname.info*
%{_texdir}/texmf-dist/fonts/map/fontname/adobe.map
%{_texdir}/texmf-dist/fonts/map/fontname/apple.map
%{_texdir}/texmf-dist/fonts/map/fontname/bitstrea.map
%{_texdir}/texmf-dist/fonts/map/fontname/dtc.map
%{_texdir}/texmf-dist/fonts/map/fontname/itc.map
%{_texdir}/texmf-dist/fonts/map/fontname/linot-cd.map
%{_texdir}/texmf-dist/fonts/map/fontname/linotype-cd.map
%{_texdir}/texmf-dist/fonts/map/fontname/linotype.map
%{_texdir}/texmf-dist/fonts/map/fontname/monotype.map
%{_texdir}/texmf-dist/fonts/map/fontname/skey1250.map
%{_texdir}/texmf-dist/fonts/map/fontname/skey1555.map
%{_texdir}/texmf-dist/fonts/map/fontname/softkey-1250.map
%{_texdir}/texmf-dist/fonts/map/fontname/softkey-1555.map
%{_texdir}/texmf-dist/fonts/map/fontname/softkey.map
%{_texdir}/texmf-dist/fonts/map/fontname/special.map
%{_texdir}/texmf-dist/fonts/map/fontname/supplier.map
%{_texdir}/texmf-dist/fonts/map/fontname/texfonts.map
%{_texdir}/texmf-dist/fonts/map/fontname/typeface.map
%{_texdir}/texmf-dist/fonts/map/fontname/urw.map
%{_texdir}/texmf-dist/fonts/map/fontname/variant.map
%{_texdir}/texmf-dist/fonts/map/fontname/weight.map
%{_texdir}/texmf-dist/fonts/map/fontname/width.map
%{_texdir}/texmf-dist/fonts/map/fontname/yandy.map

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/fonts/fontname/8a.html
%{_texdir}/texmf-dist/doc/fonts/fontname/8r.html
%{_texdir}/texmf-dist/doc/fonts/fontname/Adobe-fonts.html
%{_texdir}/texmf-dist/doc/fonts/fontname/Apple-fonts.html
%{_texdir}/texmf-dist/doc/fonts/fontname/Bitstream-fonts.html
%{_texdir}/texmf-dist/doc/fonts/fontname/ChangeLog
%{_texdir}/texmf-dist/doc/fonts/fontname/DTC-fonts.html
%{_texdir}/texmf-dist/doc/fonts/fontname/Encodings.html
%{_texdir}/texmf-dist/doc/fonts/fontname/Filenames-for-fonts.html
%{_texdir}/texmf-dist/doc/fonts/fontname/Font-legalities.html
%{_texdir}/texmf-dist/doc/fonts/fontname/Font-name-lists.html
%{_texdir}/texmf-dist/doc/fonts/fontname/History.html
%{_texdir}/texmf-dist/doc/fonts/fontname/ITC-fonts.html
%{_texdir}/texmf-dist/doc/fonts/fontname/Introduction.html
%{_texdir}/texmf-dist/doc/fonts/fontname/Linotype-fonts.html
%{_texdir}/texmf-dist/doc/fonts/fontname/Long-names.html
%{_texdir}/texmf-dist/doc/fonts/fontname/Long-naming-scheme.html
%{_texdir}/texmf-dist/doc/fonts/fontname/Makefile
%{_texdir}/texmf-dist/doc/fonts/fontname/Monotype-fonts.html
%{_texdir}/texmf-dist/doc/fonts/fontname/Name-mapping-file.html
%{_texdir}/texmf-dist/doc/fonts/fontname/References.html
%{_texdir}/texmf-dist/doc/fonts/fontname/Standard-PostScript-fonts.html
%{_texdir}/texmf-dist/doc/fonts/fontname/Suppliers.html
%{_texdir}/texmf-dist/doc/fonts/fontname/Typefaces.html
%{_texdir}/texmf-dist/doc/fonts/fontname/URW-fonts.html
%{_texdir}/texmf-dist/doc/fonts/fontname/Variants.html
%{_texdir}/texmf-dist/doc/fonts/fontname/Weights.html
%{_texdir}/texmf-dist/doc/fonts/fontname/Widths.html
%{_texdir}/texmf-dist/doc/fonts/fontname/bitstrea.aka
%{_texdir}/texmf-dist/doc/fonts/fontname/cork.html
%{_texdir}/texmf-dist/doc/fonts/fontname/dvips.html
%{_texdir}/texmf-dist/doc/fonts/fontname/fontname.aux
%{_texdir}/texmf-dist/doc/fonts/fontname/fontname.cp
%{_texdir}/texmf-dist/doc/fonts/fontname/fontname.html
%{_texdir}/texmf-dist/doc/fonts/fontname/fontname.pdf
%{_texdir}/texmf-dist/doc/fonts/fontname/fontname.texi
%{_texdir}/texmf-dist/doc/fonts/fontname/fontname.toc
%{_texdir}/texmf-dist/doc/fonts/fontname/index.html
%{_texdir}/texmf-dist/doc/fonts/fontname/texmext.html
%{_texdir}/texmf-dist/doc/fonts/fontname/texmital.html
%{_texdir}/texmf-dist/doc/fonts/fontname/texmsym.html
%{_texdir}/texmf-dist/doc/fonts/fontname/texnansi.html
%{_texdir}/texmf-dist/doc/fonts/fontname/texnansx.html
%{_texdir}/texmf-dist/doc/fonts/fontname/xl2.html
%{_texdir}/texmf-dist/doc/fonts/fontname/xt2.html


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
