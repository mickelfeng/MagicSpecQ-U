%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/ae.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/ae.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/ae.source.tar.xz

Name: texlive-ae
License: LPPL
Summary: Virtual fonts for T1 encoded CMR-fonts
Version: %{tl_version}
Release: %{tl_noarch_release}.1.4.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(ae.sty)
Provides: tex(aecompl.sty)
Requires: tex(fontenc.sty)

%description
A set of virtual fonts which emulates T1 coded fonts using the
standard CM fonts. The package name, AE fonts, supposedly
stands for "Almost European". The main use of the package was
to produce PDF files using Adobe Type 1 versions of the CM
fonts instead of bitmapped EC fonts. Note that direct
substitutes for the bitmapped EC fonts are now available, via
the CM-super, Latin Modern and (in a restricted way) CM-LGC
font sets.

date: 2009-06-30 11:37:01 +0200

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
Summary: Documentation for ae
Version: %{tl_version}
Release: %{tl_noarch_release}.1.4.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for ae


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
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aeb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aebx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aebx12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aebx5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aebx6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aebx7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aebx8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aebx9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aebxsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aebxti10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aecsc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aeitt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aer10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aer12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aer17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aer5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aer6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aer7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aer8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aer9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aesl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aesl12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aesl8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aesl9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aesltt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aess10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aess12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aess17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aess8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aess9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aessbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aessdc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aessi10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aessi12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aessi17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aessi8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aessi9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aetcsc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aeti10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aeti12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aeti7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aeti8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aeti9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aett10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aett12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aett8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/aett9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/laess8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/laessb8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ae/laessi8.tfm
%{_texdir}/texmf-dist/fonts/vf/public/ae/aeb10.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aebx10.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aebx12.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aebx5.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aebx6.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aebx7.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aebx8.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aebx9.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aebxsl10.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aebxti10.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aecsc10.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aeitt10.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aer10.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aer12.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aer17.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aer5.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aer6.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aer7.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aer8.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aer9.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aesl10.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aesl12.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aesl8.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aesl9.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aesltt10.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aess10.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aess12.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aess17.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aess8.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aess9.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aessbx10.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aessdc10.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aessi10.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aessi12.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aessi17.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aessi8.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aessi9.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aetcsc10.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aeti10.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aeti12.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aeti7.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aeti8.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aeti9.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aett10.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aett12.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aett8.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/aett9.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/laess8.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/laessb8.vf
%{_texdir}/texmf-dist/fonts/vf/public/ae/laessi8.vf
%{_texdir}/texmf-dist/tex/latex/ae/ae.sty
%{_texdir}/texmf-dist/tex/latex/ae/aecompl.sty
%{_texdir}/texmf-dist/tex/latex/ae/omlaer.fd
%{_texdir}/texmf-dist/tex/latex/ae/omsaer.fd
%{_texdir}/texmf-dist/tex/latex/ae/ot1aer.fd
%{_texdir}/texmf-dist/tex/latex/ae/ot1aess.fd
%{_texdir}/texmf-dist/tex/latex/ae/ot1aett.fd
%{_texdir}/texmf-dist/tex/latex/ae/ot1laess.fd
%{_texdir}/texmf-dist/tex/latex/ae/ot1laett.fd
%{_texdir}/texmf-dist/tex/latex/ae/t1aer.fd
%{_texdir}/texmf-dist/tex/latex/ae/t1aess.fd
%{_texdir}/texmf-dist/tex/latex/ae/t1aett.fd
%{_texdir}/texmf-dist/tex/latex/ae/t1laess.fd
%{_texdir}/texmf-dist/tex/latex/ae/t1laett.fd

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/fonts/ae/COPYING
%{_texdir}/texmf-dist/doc/fonts/ae/MANIFEST
%{_texdir}/texmf-dist/doc/fonts/ae/README


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
