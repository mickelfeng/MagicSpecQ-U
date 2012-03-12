%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/boisik.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/boisik.doc.tar.xz

Name: texlive-boisik
License: GPLv2+
Summary: A font inspired by Baskerville design
Version: %{tl_version}
Release: %{tl_noarch_release}.0.5.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(boisik.sty)

%description
Boisik is a serif font (inspired by the Baskerville typeface),
written in MetaFont. It comprises roman and italic text fonts
and maths fonts. LaTeX support is offered for use with OT1, IL2
and OM* encodings.

date: 2009-08-23 18:29:20 +0200

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
Summary: Documentation for boisik
Version: %{tl_version}
Release: %{tl_noarch_release}.0.5.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for boisik


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/gpl2.txt gpl2.txt
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
%doc gpl2.txt
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskarr10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskarrows.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskbase.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskex10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskext.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskhc10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bski10-TS1.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bski10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskib10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskiol10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskital.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskiu10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskiub10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskletters-i.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskletters-o.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskletters-r.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskligtab-i.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskligtab-sc.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskligtab.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bsklist-T1.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bsklist-TS1.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bsklist-ar.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bsklist-bb.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bsklist-ex.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bsklist-lc.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bsklist-ma.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bsklist-mi-up.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bsklist-mi.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bsklist-ms.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bsklist-sc.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bsklist-sy.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bsklist-uc.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskma10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskmab10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskmath.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskmathma.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskmathms.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskmathsy.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskmi10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskmib10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskms10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskmsb10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskmsbsl10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskmssl10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskr10-T1.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskr10-TS1.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskr10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskrb10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskrc10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskrcb10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskrf10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskrl10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskrol10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskroman.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskrsb10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskrsl10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bskrw10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bsksc.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bsksc10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bsksy10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bsksyb10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bsksybsl10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bsksymbols.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bsksyol10.mf
%{_texdir}/texmf-dist/fonts/source/public/boisik/bsksysl10.mf
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskarr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskex10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskhc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bski10-TS1.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bski10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskib10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskiol10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskiu10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskiub10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskma10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskmab10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskmi10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskmib10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskms10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskmsb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskmsbsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskmssl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskr10-T1.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskr10-TS1.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskrb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskrc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskrcb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskrf10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskrl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskrol10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskrsb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskrsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bskrw10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bsksc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bsksy10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bsksyol10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/bsksysl10.tfm
%{_texdir}/texmf-dist/tex/latex/boisik/boisik.sty
%{_texdir}/texmf-dist/tex/latex/boisik/il2bsk.fd
%{_texdir}/texmf-dist/tex/latex/boisik/il2bskf.fd
%{_texdir}/texmf-dist/tex/latex/boisik/lblbskm.fd
%{_texdir}/texmf-dist/tex/latex/boisik/lblcmr.fd
%{_texdir}/texmf-dist/tex/latex/boisik/lblenc.def
%{_texdir}/texmf-dist/tex/latex/boisik/lbmbsk.fd
%{_texdir}/texmf-dist/tex/latex/boisik/lbmbskms.fd
%{_texdir}/texmf-dist/tex/latex/boisik/lbmcmr.fd
%{_texdir}/texmf-dist/tex/latex/boisik/lbmenc.def
%{_texdir}/texmf-dist/tex/latex/boisik/lbsbsk.fd
%{_texdir}/texmf-dist/tex/latex/boisik/lbsbsksy.fd
%{_texdir}/texmf-dist/tex/latex/boisik/lbscmr.fd
%{_texdir}/texmf-dist/tex/latex/boisik/lbsenc.def
%{_texdir}/texmf-dist/tex/latex/boisik/ot1bsk.fd
%{_texdir}/texmf-dist/tex/latex/boisik/ot1bskf.fd
%{_texdir}/texmf-dist/tex/latex/boisik/ts1bsk.fd
%{_texdir}/texmf-dist/tex/latex/boisik/ubskex.fd

%files doc
%defattr(-,root,root)
%doc gpl2.txt
%{_texdir}/texmf-dist/doc/fonts/boisik/README
%{_texdir}/texmf-dist/doc/fonts/boisik/example/boisik-idiot.pdf
%{_texdir}/texmf-dist/doc/fonts/boisik/example/boisik-idiot.tex
%{_texdir}/texmf-dist/doc/fonts/boisik/example/boisik.pdf
%{_texdir}/texmf-dist/doc/fonts/boisik/example/boisik.tex
%{_texdir}/texmf-dist/doc/fonts/boisik/example/bskrlogo10.mf
%{_texdir}/texmf-dist/doc/fonts/boisik/example/table.pdf
%{_texdir}/texmf-dist/doc/fonts/boisik/example/table.tex
%{_texdir}/texmf-dist/doc/fonts/boisik/example/testfont.pdf
%{_texdir}/texmf-dist/doc/fonts/boisik/example/testfont.tex


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
