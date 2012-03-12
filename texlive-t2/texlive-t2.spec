%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/t2.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/t2.doc.tar.xz

Name: texlive-t2
License: LPPL
Summary: Support for using T2 encoding
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(citehack.sty)
Provides: tex(mathtext.sty)
Provides: tex(misccorr.sty)
Requires: tex(amssymb.sty)
Requires: tex(enumerate.sty)

%description
The T2 bundle provides a variety of separate support functions,
for using Cyrillic characters in LaTeX: - the mathtext package,
for using Cyrillic letters 'transparently' in formulae - the
citehack package, for using Cyrillic (or indeed any non-ascii)
characters in citation keys; - support for Cyrillic in BibTeX;
- support for Cyrillic in Makeindex; and - various items of
font support.

date: 2008-01-05 14:46:43 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
sed -i 's/^\#\!\ cyramstex/cyramstex pdftex language.dat -translate-file=cp227.tcx *cyramstx.ini/' %{_texdir}/texmf/web2c/fmtutil.cnf
sed -i 's/^\#\!\ cyrtex/cyrtex pdftex language.dat -translate-file=cp227.tcx *cyrtex.ini/' %{_texdir}/texmf/web2c/fmtutil.cnf
sed -i 's/^\#\!\ cyrtexinfo/cyrtexinfo pdftex language.dat -translate-file=cp227.tcx *cyrtxinf.ini/' %{_texdir}/texmf/web2c/fmtutil.cnf
touch /var/run/texlive/run-fmtutil
:

%postun
if [ $1 == 0 ]; then
  sed -i 's/^cyramstex/\#\!\ cyramstex/' %{_texdir}/texmf/web2c/fmtutil.cnf
  sed -i 's/^cyrtex/\#\!\ cyrtex/' %{_texdir}/texmf/web2c/fmtutil.cnf
  sed -i 's/^cyrtexinfo/\#\!\ cyrtexinfo/' %{_texdir}/texmf/web2c/fmtutil.cnf
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
Summary: Documentation for t2
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for t2


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
%{_texdir}/texmf-dist/fonts/enc/t2/t2a-mod1.enc
%{_texdir}/texmf-dist/fonts/enc/t2/t2a-mod2.enc
%{_texdir}/texmf-dist/fonts/enc/t2/t2a.enc
%{_texdir}/texmf-dist/fonts/enc/t2/t2b.enc
%{_texdir}/texmf-dist/fonts/enc/t2/t2c.enc
%{_texdir}/texmf-dist/fonts/enc/t2/x2.enc
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/6r.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/README
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/cyrillic.mtx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/lcy-hi.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/lcy.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/ot2.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/t2a.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/t2b.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/t2c.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/x2.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/lcyc.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/lcyci.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/lcycij.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/lcycj.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/lcyctt.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/lcyi.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/lcyij.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/lcyitt.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/lcyj.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/lcytt.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/ot2c.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/ot2cj.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/ot2i.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/ot2ij.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/ot2j.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/t2ac.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/t2acj.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/t2ai.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/t2aij.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/t2aj.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/t2bc.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/t2bcj.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/t2bi.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/t2bij.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/t2bj.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/t2cc.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/t2ccj.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/t2ci.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/t2cij.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/t2cj.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/x2c.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/x2cj.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/x2i.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/x2ij.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives/x2j.etx
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/etc/alias-cmc.tex
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/etc/alias-wncy.tex
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/etc/cyralias.tex
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/etc/fnstcorr.tex
%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/etc/showenc
%{_texdir}/texmf-dist/tex/latex/t2/citehack.sty
%{_texdir}/texmf-dist/tex/latex/t2/mathtext.sty
%{_texdir}/texmf-dist/tex/latex/t2/misccorr.sty

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/generic/t2/Makefile
%{_texdir}/texmf-dist/doc/generic/t2/OT2uni.map
%{_texdir}/texmf-dist/doc/generic/t2/README
%{_texdir}/texmf-dist/doc/generic/t2/T2Auni.map
%{_texdir}/texmf-dist/doc/generic/t2/T2Buni.map
%{_texdir}/texmf-dist/doc/generic/t2/T2Cuni.map
%{_texdir}/texmf-dist/doc/generic/t2/X2uni.map
%{_texdir}/texmf-dist/doc/generic/t2/amscyr.txt
%{_texdir}/texmf-dist/doc/generic/t2/broken1.txt
%{_texdir}/texmf-dist/doc/generic/t2/broken2.txt
%{_texdir}/texmf-dist/doc/generic/t2/cyrcset7.txt
%{_texdir}/texmf-dist/doc/generic/t2/cyrcset8.txt
%{_texdir}/texmf-dist/doc/generic/t2/cyrcsets.ind
%{_texdir}/texmf-dist/doc/generic/t2/make-enc.pl
%{_texdir}/texmf-dist/doc/generic/t2/mkencs.sh
%{_texdir}/texmf-dist/doc/generic/t2/mtcyr.txt
%{_texdir}/texmf-dist/doc/generic/t2/t2cyr.txt
%{_texdir}/texmf-dist/doc/generic/t2/t2lat.txt
%{_texdir}/texmf-dist/doc/generic/t2/urwcyr.txt
%{_texdir}/texmf-dist/doc/generic/t2/etc/amsppt.diff
%{_texdir}/texmf-dist/doc/generic/t2/etc/mathtext.dtx
%{_texdir}/texmf-dist/doc/generic/t2/etc/mathtext.ins
%{_texdir}/texmf-dist/doc/generic/t2/etc/ruinpenc
%{_texdir}/texmf-dist/doc/generic/t2/etc/t2filter.c
%{_texdir}/texmf-dist/doc/generic/t2/etc/rubibtex/README
%{_texdir}/texmf-dist/doc/generic/t2/etc/rubibtex/rubibtex
%{_texdir}/texmf-dist/doc/generic/t2/etc/rubibtex/rubibtex.bat
%{_texdir}/texmf-dist/doc/generic/t2/etc/rubibtex/rubibtex.old
%{_texdir}/texmf-dist/doc/generic/t2/etc/rubibtex/rubibtex.sed
%{_texdir}/texmf-dist/doc/generic/t2/etc/rumkidx/README
%{_texdir}/texmf-dist/doc/generic/t2/etc/rumkidx/rumakeindex
%{_texdir}/texmf-dist/doc/generic/t2/etc/rumkidx/rumkidx1.sed
%{_texdir}/texmf-dist/doc/generic/t2/etc/rumkidx/rumkidx2.sed
%{_texdir}/texmf-dist/doc/generic/t2/etc/rumkidx/rumkidx3.sed
%{_texdir}/texmf-dist/doc/generic/t2/etc/rumkidx/rumkidxd.bat
%{_texdir}/texmf-dist/doc/generic/t2/etc/rumkidx/rumkidxw.bat
%{_texdir}/texmf-dist/doc/generic/t2/etc/utf-8/test-utf8.tex
%{_texdir}/texmf-dist/doc/generic/t2/etc/utf-8/utf-8.def
%{_texdir}/texmf-dist/doc/generic/t2/etc/utf-8/utfcyr.def
%{_texdir}/texmf-dist/doc/generic/t2/etc/utf-8/utflat.def
%{_texdir}/texmf-dist/doc/generic/t2/examples/example1.tex
%{_texdir}/texmf-dist/doc/generic/t2/examples/example2.tex
%{_texdir}/texmf-dist/doc/generic/t2/examples/example3.tex
%{_texdir}/texmf-dist/doc/generic/t2/examples/example4.tex
%{_texdir}/texmf-dist/doc/generic/t2/examples/example5.tex


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
