%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/iso10303.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/iso10303.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/iso10303.source.tar.xz

Name: texlive-iso10303
License: LPPL
Summary: Typesetting the STEP standards
Version: %{tl_version}
Release: %{tl_noarch_release}.1.5.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(aicv1.sty)
Provides: tex(apv12.sty)
Provides: tex(atsv11.sty)
Provides: tex(irv12.sty)
Provides: tex(stepv13.sty)

%description
Class and package files building on iso for typesetting the ISO
10303 (STEP) standards. Standard documents prepared using these
packages have been published by ISO.

date: 2007-01-09 14:09:22 +0100

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
Summary: Documentation for iso10303
Version: %{tl_version}
Release: %{tl_noarch_release}.1.5.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for iso10303


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/lppl.txt lppl.txt
xz -dc %{SOURCE0} | tar x -C %{buildroot}%{_texdir}/texmf-dist
xz -dc %{SOURCE1} | tar x -C %{buildroot}%{_texdir}/texmf-dist
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
%{_texdir}/texmf-dist/tex/latex/iso10303/aicv1.sty
%{_texdir}/texmf-dist/tex/latex/iso10303/apendint.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/apmpspec.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/apmptbl.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/apmptempl.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/apsstempl.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/apv12.sty
%{_texdir}/texmf-dist/tex/latex/iso10303/atsv11.sty
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfap1.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfap10.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfap11.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfap12.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfap13.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfap14.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfap15.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfap16.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfap2.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfap3.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfap4.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfap5.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfap6.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfap7.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfap8.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfap9.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfats1.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfats10.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfats11.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfats12.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfats14.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfats2.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfats3.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfats4.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfats5.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfats6.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfats7.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfats8.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfats9.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfir1.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfir2.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfir3.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfs1.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfs2.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/bpfs3.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/irv12.sty
%{_texdir}/texmf-dist/tex/latex/iso10303/stepman.tex
%{_texdir}/texmf-dist/tex/latex/iso10303/stepv13.4ht
%{_texdir}/texmf-dist/tex/latex/iso10303/stepv13.sty
%{_texdir}/texmf-dist/tex/latex/iso10303/stppdlst.tex

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/iso10303/README
%{_texdir}/texmf-dist/doc/latex/iso10303/step4ht.pdf
%{_texdir}/texmf-dist/doc/latex/iso10303/stepe.pdf
%{_texdir}/texmf-dist/doc/latex/iso10303/stepman.pdf


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
