%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/universa.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/universa.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/universa.source.tar.xz

Name: texlive-universa
License: GPL+
Summary: Herbert Bayer's 'universal' font
Version: %{tl_version}
Release: %{tl_noarch_release}.2.0.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(uni.sty)

%description
An implementation of the universal font by Herbert Bayer of the
Bauhaus school. The MetaFont sources of the fonts, and their
LaTeX support, are all supplied in a LaTeX documented source
(.dtx) file.

date: 2008-11-02 01:06:10 +0100

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
Summary: Documentation for universa
Version: %{tl_version}
Release: %{tl_noarch_release}.2.0.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for universa


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/gpl.txt gpl.txt
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
%doc gpl.txt
%{_texdir}/texmf-dist/fonts/source/public/universa/fulbc10.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulbc12.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulbc17.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulbc8.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulbc9.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulbo10.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulbo12.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulbo17.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulbo8.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulbo9.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulbr10.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulbr12.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulbr17.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulbr8.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulbr9.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulbst10.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulbst12.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulbst17.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulbst8.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulbst9.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulmc10.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulmc12.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulmc17.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulmc8.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulmc9.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulmo10.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulmo12.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulmo17.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulmo8.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulmo9.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulmr10.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulmr12.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulmr17.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulmr8.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulmr9.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulmst10.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulmst12.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulmst17.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulmst8.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/fulmst9.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/uniacc.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/unibase.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/unidig.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/uniext.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/unilig.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/unilow.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/unipun.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/unispe.mf
%{_texdir}/texmf-dist/fonts/source/public/universa/uniupp.mf
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulbc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulbc12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulbc17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulbc8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulbc9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulbo10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulbo12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulbo17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulbo8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulbo9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulbr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulbr12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulbr17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulbr8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulbr9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulbst10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulbst12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulbst17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulbst8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulbst9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulmc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulmc12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulmc17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulmc8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulmc9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulmo10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulmo12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulmo17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulmo8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulmo9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulmr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulmr12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulmr17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulmr8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulmr9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulmst10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulmst12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulmst17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulmst8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/universa/fulmst9.tfm
%{_texdir}/texmf-dist/tex/latex/universa/omluni.fd
%{_texdir}/texmf-dist/tex/latex/universa/omsuni.fd
%{_texdir}/texmf-dist/tex/latex/universa/ot1uni.fd
%{_texdir}/texmf-dist/tex/latex/universa/t1uni.fd
%{_texdir}/texmf-dist/tex/latex/universa/uni.sty
%{_texdir}/texmf-dist/tex/latex/universa/uuni.fd

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/fonts/universa/README.uni
%{_texdir}/texmf-dist/doc/fonts/universa/copyright.tex
%{_texdir}/texmf-dist/doc/fonts/universa/unidoc.sty


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
