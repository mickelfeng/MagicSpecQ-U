%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/misc.tar.xz

Name: texlive-misc
License: LPPL
Summary: misc package
Version: %{tl_version}
Release: %{tl_noarch_release}.svn17497%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(bibnames.sty)
Provides: tex(texnames.sty)

%description
misc package

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


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
xz -dc %{SOURCE0} | tar x -C %{buildroot}%{_texdir}/texmf-dist
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
%{_texdir}/texmf-dist/fonts/source/public/misc/black.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/blackaps.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/blackcx.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/blackimagen.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/blacklino.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/blacklj.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/cmman.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/gray.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/grayaps.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/graycx.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/grayf.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/grayimagen.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/grayimagen3.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/grayimagenlight.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/graylj.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/manfnt.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/mfman.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/oneone.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/random.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/slant.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/slantaps4.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/slantcx4.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/slantcx6.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/slantimagen4.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/slantimagen6.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/slantlino4.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/slantlj4.mf
%{_texdir}/texmf-dist/fonts/source/public/misc/slantlj6.mf
%{_texdir}/texmf-dist/fonts/tfm/public/misc/black.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/misc/blackcx.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/misc/cmman.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/misc/gray.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/misc/graycx.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/misc/grayimagen3.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/misc/manfnt.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/misc/oneone.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/misc/slantcx4.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/misc/slantcx6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/misc/slantlj4.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/misc/slantlj6.tfm
%{_texdir}/texmf-dist/omega/ocp/misc/ebcdic.ocp
%{_texdir}/texmf-dist/omega/ocp/misc/id.ocp
%{_texdir}/texmf-dist/omega/otp/misc/ebcdic.otp
%{_texdir}/texmf-dist/omega/otp/misc/id.otp
%{_texdir}/texmf-dist/tex/generic/misc/bibnames.sty
%{_texdir}/texmf-dist/tex/generic/misc/null.tex
%{_texdir}/texmf-dist/tex/generic/misc/texnames.sty
%{_texdir}/texmf-dist/tex/plain/misc/idxmac.tex
%{_texdir}/texmf-dist/tex/plain/misc/pdfcolor.tex
%{_texdir}/texmf-dist/tex/plain/misc/tugboat.def
%{_texdir}/texmf-dist/tex/plain/misc/xepsf.tex


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
