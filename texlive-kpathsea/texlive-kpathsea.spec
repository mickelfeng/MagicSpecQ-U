%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/kpathsea.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/kpathsea.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/kpathsea.doc.tar.xz

Name: texlive-kpathsea
License: LGPLv2+
Summary: Path searching library for TeX-related files
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19287%{?dist}
BuildArch: noarch
Provides: kpathsea = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires(preun,post): /sbin/install-info
Requires: texlive-kpathsea-bin = %{tl_version}

%description
Kpathsea is a library and utility programs which provide path
searching facilities for TeX file types, including the self-
locating feature required for movable installations, layered on
top of a general search mechanism. It is not distributed
separately, but rather is released and maintained as part of
the TeX-live sources.

date: 2010-05-03 20:19:11 +0200

%preun
if [ "$1" = "0" ]; then
  /sbin/install-info --delete %{_infodir}/kpathsea.info %{_infodir}/dir 2>/dev/null || :
  /sbin/install-info --delete %{_infodir}/tds.info %{_infodir}/dir 2>/dev/null || :
  /sbin/install-info --delete %{_infodir}/web2c.info %{_infodir}/dir 2>/dev/null || :
fi

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
/sbin/install-info %{_infodir}/kpathsea.info %{_infodir}/dir 2>/dev/null
/sbin/install-info %{_infodir}/tds.info %{_infodir}/dir 2>/dev/null
/sbin/install-info %{_infodir}/web2c.info %{_infodir}/dir 2>/dev/null
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
Summary: Documentation for kpathsea
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19287%{?dist}
Obsoletes: kpathsea < %{tl_version}
BuildArch: noarch

%description doc
Documentation for kpathsea


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/lgpl.txt lgpl.txt
xz -dc %{SOURCE0} | tar x -C %{buildroot}%{_texdir}
xz -dc %{SOURCE1} | tar x -C %{buildroot}%{_texdir}

# add reference to support old texmf tree
sed -i 's|TEXMFLOCAL = $SELFAUTOPARENT/../texmf-local|TEXMFLOCAL = $SELFAUTOPARENT/../texmf|g' %{buildroot}%{_texdir}/texmf/web2c/texmf.cnf

xz -dc %{SOURCE2} | tar x -C %{buildroot}%{_texdir}
# nuke useless tlmgr packaging stuff and doc droppings
rm -rf %{buildroot}%{_texdir}/tlpkg/tlpobj/
rm -rf %{buildroot}%{_texdir}/texmf-dist/tlpkg/tlpobj/
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/man*/*.pdf
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/Makefile
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/man*/Makefile
rm -rf %{buildroot}%{_texdir}/texmf/doc/info/dir
rm -f %{buildroot}/%{_texdir}/texmf/doc/info/kpathsea.info

# disable all formats
sed -i '/^[a-z]/s/^/\#\!\ /' %{buildroot}%{_texdir}/texmf/web2c/fmtutil.cnf
mkdir -p %{buildroot}/%{_datadir}/
mv %{buildroot}/%{_texdir}/texmf/doc/man %{buildroot}/%{_datadir}/
mkdir -p %{buildroot}/%{_infodir}/
mv %{buildroot}/%{_texdir}/texmf/doc/info/* %{buildroot}/%{_infodir}/

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lgpl.txt
%{_mandir}/man1/kpseaccess.1*
%{_mandir}/man1/kpsepath.1*
%{_mandir}/man1/kpsereadlink.1*
%{_mandir}/man1/kpsestat.1*
%{_mandir}/man1/kpsetool.1*
%{_mandir}/man1/kpsewhere.1*
%{_mandir}/man1/kpsewhich.1*
%{_mandir}/man1/kpsexpand.1*
%{_mandir}/man1/mkocp.1*
%{_mandir}/man1/mkofm.1*
%{_mandir}/man1/mktexfmt.1*
%{_mandir}/man1/mktexlsr.1*
%{_mandir}/man1/mktexmf.1*
%{_mandir}/man1/mktexpk.1*
%{_mandir}/man1/mktextfm.1*
%{_mandir}/man1/texhash.1*
%{_infodir}/tds.info*
%{_infodir}/web2c.info*
%{_texdir}/texmf/web2c/amiga-pl.tcx
#%config(noreplace) %{_texdir}/texmf/web2c/context.cnf
%{_texdir}/texmf/web2c/cp1250cs.tcx
%{_texdir}/texmf/web2c/cp1250pl.tcx
%{_texdir}/texmf/web2c/cp1250t1.tcx
%{_texdir}/texmf/web2c/cp227.tcx
%{_texdir}/texmf/web2c/cp852-cs.tcx
%{_texdir}/texmf/web2c/cp852-pl.tcx
%{_texdir}/texmf/web2c/cp8bit.tcx
%{_texdir}/texmf/web2c/empty.tcx
%config(noreplace) %{_texdir}/texmf/web2c/fmtutil.cnf
%{_texdir}/texmf/web2c/il1-t1.tcx
%{_texdir}/texmf/web2c/il2-cs.tcx
%{_texdir}/texmf/web2c/il2-pl.tcx
%{_texdir}/texmf/web2c/il2-t1.tcx
%{_texdir}/texmf/web2c/kam-cs.tcx
%{_texdir}/texmf/web2c/kam-t1.tcx
%{_texdir}/texmf/web2c/macce-pl.tcx
%{_texdir}/texmf/web2c/macce-t1.tcx
%{_texdir}/texmf/web2c/maz-pl.tcx
%config(noreplace) %{_texdir}/texmf/web2c/mktex.cnf
%{_texdir}/texmf/web2c/mktex.opt
%{_texdir}/texmf/web2c/mktexdir
%{_texdir}/texmf/web2c/mktexdir.opt
%{_texdir}/texmf/web2c/mktexnam
%{_texdir}/texmf/web2c/mktexnam.opt
%{_texdir}/texmf/web2c/mktexupd
%{_texdir}/texmf/web2c/natural.tcx
%{_texdir}/texmf/web2c/tcvn-t5.tcx
%config(noreplace) %{_texdir}/texmf/web2c/texmf.cnf
%{_texdir}/texmf/web2c/viscii-t5.tcx

%files doc
%defattr(-,root,root)
%doc lgpl.txt
%{_texdir}/texmf/doc/kpathsea/kpathsea.html
%{_texdir}/texmf/doc/kpathsea/kpathsea.pdf
%{_texdir}/texmf/doc/web2c/web2c.html
%{_texdir}/texmf/doc/web2c/web2c.pdf


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
