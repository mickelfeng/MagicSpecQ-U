%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/psnfss.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/psnfss.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/psnfss.source.tar.xz

Name: texlive-psnfss
License: LPPL
Summary: Font support for common PostScript fonts
Version: %{tl_version}
Release: %{tl_noarch_release}.9.2a.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-graphics = %{tl_version}
Provides: tex(avant.sty)
Provides: tex(bookman.sty)
Provides: tex(chancery.sty)
Provides: tex(charter.sty)
Provides: tex(courier.sty)
Provides: tex(helvet.sty)
Provides: tex(mathpazo.sty)
Provides: tex(mathpple.sty)
Provides: tex(mathptm.sty)
Provides: tex(mathptmx.sty)
Provides: tex(newcent.sty)
Provides: tex(palatino.sty)
Provides: tex(pifont.sty)
Provides: tex(times.sty)
Provides: tex(utopia.sty)
Requires: tex(keyval.sty)

%description
Font definition files, macros and font metrics for freely-
available Adobe Type 1 fonts. The font set consists of the
'LaserWriter 35' set (originally 'freely available' because
embedded in PostScript printers), and a variety of other free
fonts such as Bitstream Charter, Adobe Utopia (both donated to
the public domain by their commercial foundries) and Pazo Math
(optionally extended with the fpl small-caps and old-style
figures fonts). The bundle is part of the LaTeX 'required' set
of packages.

date: 2009-10-07 22:25:55 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map charter.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map fpls.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map pazo.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map utopia.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map charter.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map fpls.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map pazo.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map utopia.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  %{_bindir}/texhash 2> /dev/null
  %{_bindir}/updmap-sys --nohash --quiet &> /dev/null
else
  mkdir -p /var/run/texlive
  touch /var/run/texlive/run-texhash
  touch /var/run/texlive/run-updmap
fi
:

%posttrans
[ -e /var/run/texlive/run-texhash ] && %{_bindir}/texhash 2> /dev/null && rm -f /var/run/texlive/run-texhash
[ -e /var/run/texlive/run-updmap ] && %{_bindir}/updmap-sys --nohash --quiet &> /dev/null && rm -f /var/run/texlive/run-updmap
[ -e /var/run/texlive ] && rm -rf /var/run/texlive
:

%package doc
Summary: Documentation for psnfss
Version: %{tl_version}
Release: %{tl_noarch_release}.9.2a.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch
Requires: texlive-graphics-doc

%description doc
Documentation for psnfss


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
%{_texdir}/texmf-dist/fonts/map/dvips/psnfss/charter.map
%{_texdir}/texmf-dist/fonts/map/dvips/psnfss/fpls.map
%{_texdir}/texmf-dist/fonts/map/dvips/psnfss/pazo.map
%{_texdir}/texmf-dist/fonts/map/dvips/psnfss/psnfss.map
%{_texdir}/texmf-dist/fonts/map/dvips/psnfss/utopia.map
%{_texdir}/texmf-dist/tex/latex/psnfss/8rbch.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/8rpag.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/8rpbk.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/8rpcr.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/8rphv.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/8rpnc.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/8rppl.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/8rptm.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/8rput.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/8rpzc.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/avant.sty
%{_texdir}/texmf-dist/tex/latex/psnfss/bookman.sty
%{_texdir}/texmf-dist/tex/latex/psnfss/chancery.sty
%{_texdir}/texmf-dist/tex/latex/psnfss/charter.sty
%{_texdir}/texmf-dist/tex/latex/psnfss/courier.sty
%{_texdir}/texmf-dist/tex/latex/psnfss/helvet.sty
%{_texdir}/texmf-dist/tex/latex/psnfss/mathpazo.sty
%{_texdir}/texmf-dist/tex/latex/psnfss/mathpple.sty
%{_texdir}/texmf-dist/tex/latex/psnfss/mathptm.sty
%{_texdir}/texmf-dist/tex/latex/psnfss/mathptmx.sty
%{_texdir}/texmf-dist/tex/latex/psnfss/newcent.sty
%{_texdir}/texmf-dist/tex/latex/psnfss/omlbch.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omlpag.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omlpbk.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omlpcr.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omlphv.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omlpnc.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omlppl.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omlptm.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omlptmcm.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omlput.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omlpzc.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omlzplm.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omlzpple.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omlztmcm.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omsbch.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omspag.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omspbk.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omspcr.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omsphv.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omspnc.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omsppl.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omsptm.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omsput.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omspzc.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omspzccm.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omszplm.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omszpple.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omsztmcm.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omxpsycm.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omxzplm.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omxzpple.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/omxztmcm.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ot1bch.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ot1pag.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ot1pbk.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ot1pcr.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ot1phv.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ot1pnc.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ot1ppl.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ot1pplj.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ot1pplx.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ot1ptm.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ot1ptmcm.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ot1put.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ot1pzc.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ot1zplm.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ot1zpple.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ot1ztmcm.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/palatino.sty
%{_texdir}/texmf-dist/tex/latex/psnfss/pifont.sty
%{_texdir}/texmf-dist/tex/latex/psnfss/t1bch.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/t1pag.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/t1pbk.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/t1pcr.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/t1phv.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/t1pnc.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/t1ppl.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/t1pplj.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/t1pplx.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/t1ptm.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/t1put.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/t1pzc.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/times.sty
%{_texdir}/texmf-dist/tex/latex/psnfss/ts1bch.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ts1pag.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ts1pbk.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ts1pcr.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ts1phv.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ts1pnc.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ts1ppl.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ts1pplj.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ts1pplx.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ts1ptm.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ts1put.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ts1pzc.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ufplm.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/ufplmbb.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/upsy.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/upzd.fd
%{_texdir}/texmf-dist/tex/latex/psnfss/utopia.sty

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/psnfss/00readme.txt
%{_texdir}/texmf-dist/doc/latex/psnfss/changes.txt
%{_texdir}/texmf-dist/doc/latex/psnfss/manifest.txt
%{_texdir}/texmf-dist/doc/latex/psnfss/psfonts.pdf
%{_texdir}/texmf-dist/doc/latex/psnfss/psnfss2e.pdf
%{_texdir}/texmf-dist/doc/latex/psnfss/test/mathtest.tex
%{_texdir}/texmf-dist/doc/latex/psnfss/test/pitest.tex
%{_texdir}/texmf-dist/doc/latex/psnfss/test/test0.tex
%{_texdir}/texmf-dist/doc/latex/psnfss/test/test1.tex
%{_texdir}/texmf-dist/doc/latex/psnfss/test/test2.tex
%{_texdir}/texmf-dist/doc/latex/psnfss/test/test3.tex


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
