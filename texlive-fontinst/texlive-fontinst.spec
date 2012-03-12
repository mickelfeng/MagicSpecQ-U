%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/fontinst.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/fontinst.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/fontinst.doc.tar.xz
Source3: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/fontinst.source.tar.xz

Name: texlive-fontinst
License: LPPL
Summary: Help with installing fonts for TeX and LaTeX
Version: %{tl_version}
Release: %{tl_noarch_release}.1.933.svn18835%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-fontinst-bin = %{tl_version}
Provides: tex(bbox.sty)
Provides: tex(cfntinst.sty)
Provides: tex(fontinst.sty)
Provides: tex(finstmsc.sty)
Provides: tex(multislot.sty)
Provides: tex(xfntinst.sty)
Provides: tex(fontdoc.sty)
Requires: tex(color.sty)
Requires: tex(amstext.sty)

%description
TeX macros for converting Adobe Font Metric files to TeX metric
and virtual font format. Fontinst helps mainly with the number
crunching and shovelling parts of font installation. This means
in practice that it creates a number of files which give the
TeX metrics (and related information) for a font family that
(La)TeX needs to do any typesetting in these fonts. Fontinst
furthermore makes it easy to create fonts containing glyphs
from more than one base font, taking advantage of (e.g.)
"expert" font sets. Fontinst cannot examine files to see if
they contain any useful information, nor automatically search
for files or work with binary file formats; those tasks must
normally be done manually or with the help of some other tool,
such as the pltotf and vptovf programs.

date: 2009-09-26 11:43:36 +0200

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
Summary: Documentation for fontinst
Version: %{tl_version}
Release: %{tl_noarch_release}.1.933.svn18835%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for fontinst


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/lppl.txt lppl.txt
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
mkdir -p %{buildroot}/%{_datadir}/
mv %{buildroot}/%{_texdir}/texmf/doc/man %{buildroot}/%{_datadir}/

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lppl.txt
%{_mandir}/man1/fontinst.1*
%{_texdir}/texmf-dist/tex/fontinst/base/bbox.sty
%{_texdir}/texmf-dist/tex/fontinst/base/cfntinst.sty
%{_texdir}/texmf-dist/tex/fontinst/base/finstmsc.sty
%{_texdir}/texmf-dist/tex/fontinst/base/fontinst.ini
%{_texdir}/texmf-dist/tex/fontinst/base/fontinst.sty
%{_texdir}/texmf-dist/tex/fontinst/base/multislot.sty
%{_texdir}/texmf-dist/tex/fontinst/base/xfntinst.sty
%{_texdir}/texmf-dist/tex/fontinst/latinetx/8r.etx
%{_texdir}/texmf-dist/tex/fontinst/latinetx/8y.etx
%{_texdir}/texmf-dist/tex/fontinst/latinetx/ot1.etx
%{_texdir}/texmf-dist/tex/fontinst/latinetx/ot1c.etx
%{_texdir}/texmf-dist/tex/fontinst/latinetx/ot1cj.etx
%{_texdir}/texmf-dist/tex/fontinst/latinetx/ot1ctt.etx
%{_texdir}/texmf-dist/tex/fontinst/latinetx/ot1i.etx
%{_texdir}/texmf-dist/tex/fontinst/latinetx/ot1ij.etx
%{_texdir}/texmf-dist/tex/fontinst/latinetx/ot1itt.etx
%{_texdir}/texmf-dist/tex/fontinst/latinetx/ot1j.etx
%{_texdir}/texmf-dist/tex/fontinst/latinetx/ot1tt.etx
%{_texdir}/texmf-dist/tex/fontinst/latinetx/t1.etx
%{_texdir}/texmf-dist/tex/fontinst/latinetx/t1c.etx
%{_texdir}/texmf-dist/tex/fontinst/latinetx/t1cj.etx
%{_texdir}/texmf-dist/tex/fontinst/latinetx/t1i.etx
%{_texdir}/texmf-dist/tex/fontinst/latinetx/t1ij.etx
%{_texdir}/texmf-dist/tex/fontinst/latinetx/t1j.etx
%{_texdir}/texmf-dist/tex/fontinst/latinetx/txtfdmns.etx
%{_texdir}/texmf-dist/tex/fontinst/latinmtx/8r.mtx
%{_texdir}/texmf-dist/tex/fontinst/latinmtx/8y.mtx
%{_texdir}/texmf-dist/tex/fontinst/latinmtx/latin.mtx
%{_texdir}/texmf-dist/tex/fontinst/latinmtx/latinsc.mtx
%{_texdir}/texmf-dist/tex/fontinst/latinmtx/llbuild.mtx
%{_texdir}/texmf-dist/tex/fontinst/latinmtx/lsbuild.mtx
%{_texdir}/texmf-dist/tex/fontinst/latinmtx/lsfake.mtx
%{_texdir}/texmf-dist/tex/fontinst/latinmtx/lsmisc.mtx
%{_texdir}/texmf-dist/tex/fontinst/latinmtx/ltcmds.mtx
%{_texdir}/texmf-dist/tex/fontinst/latinmtx/ltpunct.mtx
%{_texdir}/texmf-dist/tex/fontinst/latinmtx/lubuild.mtx
%{_texdir}/texmf-dist/tex/fontinst/latinmtx/newlatin.mtx
%{_texdir}/texmf-dist/tex/fontinst/latinmtx/resetsc.mtx
%{_texdir}/texmf-dist/tex/fontinst/latinmtx/unsetalf.mtx
%{_texdir}/texmf-dist/tex/fontinst/mathetx/euex.etx
%{_texdir}/texmf-dist/tex/fontinst/mathetx/eufrak.etx
%{_texdir}/texmf-dist/tex/fontinst/mathetx/eurm.etx
%{_texdir}/texmf-dist/tex/fontinst/mathetx/euscr.etx
%{_texdir}/texmf-dist/tex/fontinst/mathetx/msam.etx
%{_texdir}/texmf-dist/tex/fontinst/mathetx/msbm.etx
%{_texdir}/texmf-dist/tex/fontinst/mathetx/oml.etx
%{_texdir}/texmf-dist/tex/fontinst/mathetx/oms.etx
%{_texdir}/texmf-dist/tex/fontinst/mathetx/omx.etx
%{_texdir}/texmf-dist/tex/fontinst/mathetx/rsfs.etx
%{_texdir}/texmf-dist/tex/fontinst/mathmtx/mathex.mtx
%{_texdir}/texmf-dist/tex/fontinst/mathmtx/mathit.mtx
%{_texdir}/texmf-dist/tex/fontinst/mathmtx/mathsy.mtx
%{_texdir}/texmf-dist/tex/fontinst/misc/csc2x.tex
%{_texdir}/texmf-dist/tex/fontinst/misc/csckrn2x.tex
%{_texdir}/texmf-dist/tex/fontinst/misc/glyphbox.mtx
%{_texdir}/texmf-dist/tex/fontinst/misc/glyphoff.mtx
%{_texdir}/texmf-dist/tex/fontinst/misc/glyphon.mtx
%{_texdir}/texmf-dist/tex/fontinst/misc/kernoff.mtx
%{_texdir}/texmf-dist/tex/fontinst/misc/kernon.mtx
%{_texdir}/texmf-dist/tex/fontinst/misc/osf2x.tex
%{_texdir}/texmf-dist/tex/fontinst/smbletx/digit2.etx
%{_texdir}/texmf-dist/tex/fontinst/smbletx/ts1.etx
%{_texdir}/texmf-dist/tex/fontinst/smbletx/ts1i.etx
%{_texdir}/texmf-dist/tex/fontinst/smbletx/ts1ij.etx
%{_texdir}/texmf-dist/tex/fontinst/smbletx/ts1j.etx
%{_texdir}/texmf-dist/tex/fontinst/smblmtx/resetosf.mtx
%{_texdir}/texmf-dist/tex/fontinst/smblmtx/textcomp.mtx
%{_texdir}/texmf-dist/tex/fontinst/smblmtx/unsetnum.mtx
%{_texdir}/texmf-dist/tex/latex/fontinst/fontdoc.sty

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/fonts/fontinst/README
%{_texdir}/texmf-dist/doc/fonts/fontinst/encspecs/encspecs.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/encspecs/omxdraft.etx
%{_texdir}/texmf-dist/doc/fonts/fontinst/encspecs/ot1draft.etx
%{_texdir}/texmf-dist/doc/fonts/fontinst/encspecs/t1draft.etx
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/basic/basicex.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/basic/basicex2.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/eurofont/Makefile
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/eurofont/eurofont.map
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/eurofont/eurofont.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptm/Makefile
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptm/fontptcm.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptm/mathtest.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptm/resetsy.mtx
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptm/unsetmu.mtx
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptm/zrhax.mtx
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptm/zrmhax.mtx
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptm/zrmkern.mtx
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptm/zrvhax.mtx
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptm/zryhax.mtx
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptmx/Makefile
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptmx/fontptcmx.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptmx/mathptmx.sty
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptmx/mathtestx.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptmx/resetsy.mtx
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptmx/unsetmu.mtx
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptmx/zrhax.mtx
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptmx/zrmhax.mtx
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptmx/zrmkernx.mtx
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptmx/zrvhax.mtx
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptmx/zryhax.mtx
%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptmx/zrykernx.mtx
%{_texdir}/texmf-dist/doc/fonts/fontinst/manual/fontinst.pdf
%{_texdir}/texmf-dist/doc/fonts/fontinst/manual/fontinst.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/manual/intro98.pdf
%{_texdir}/texmf-dist/doc/fonts/fontinst/manual/intro98.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/manual/roadmap.eps
%{_texdir}/texmf-dist/doc/fonts/fontinst/talks/et99-font-tables.pdf
%{_texdir}/texmf-dist/doc/fonts/fontinst/talks/et99-font-tutorial.pdf
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/cc-pl.enc
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/comparemetrics.sty
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/comparepls.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/fadrr.mtx
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/multislot-test.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/multislot.etx
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/omsdraft.etx
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/testsc.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/v1901test.mtx
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/v1901test.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/v1902test.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/v1905test.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/v1906test.etx
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/v1906test.mtx
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/v1906test.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/v1913test.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/v1914test.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/v1914testmap.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/v1914testshow.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/v1915test.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/v1915testmap.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/v1916test.mtx
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/v1916test.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/v1916test2.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/v1923test.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/v1927test.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/v1928test.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/v1928test2.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/v1930test.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/v1931test0.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/v1931test1.tex
%{_texdir}/texmf-dist/doc/fonts/fontinst/test/v1931test2.tex


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
