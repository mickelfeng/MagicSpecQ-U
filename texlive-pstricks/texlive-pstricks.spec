%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/pstricks.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/pstricks.doc.tar.xz

Name: texlive-pstricks
License: LPPL
Summary: PostScript macros for TeX
Version: %{tl_version}
Release: %{tl_noarch_release}.2.08.svn19020%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(pst-all.sty)
Provides: tex(pst-key.sty)
Provides: tex(pstcol.sty)
Provides: tex(pstricks.sty)
Requires: tex(pst-plot.sty)
Requires: tex(pst-node.sty)
Requires: tex(pst-tree.sty)
Requires: tex(pst-grad.sty)
Requires: tex(pst-coil.sty)
Requires: tex(pst-text.sty)
Requires: tex(pst-3d.sty)
Requires: tex(pst-eps.sty)
Requires: tex(pst-fill.sty)
Requires: tex(pstricks-add.sty)
Requires: tex(multido.sty)
Requires: tex(auto-pst-pdf.sty)

%description
An extensive collection of PostScript macros that is compatible
with most TeX macro formats, including Plain TeX, LaTeX, AMS-
TeX, and AMS-LaTeX. Included are macros for colour, graphics,
pie charts, rotation, trees and overlays. It has many special
features, including a wide variety of graphics (picture
drawing) macros, with a flexible interface and with colour
support. There are macros for colouring or shading the cells of
tables. The package pstricks-add contains bug-fixes and
additions for pstricks (among other things). PSTricks uses
PostScript \special commands, which are not supported by
PDF(La)TeX. This limitation may be overcome by using either the
pst-pdf or the pdftricks package, to generate a PDF inclusion
from a PSTricks diagram.

date: 2010-06-12 20:05:05 +0200

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
Summary: Documentation for pstricks
Version: %{tl_version}
Release: %{tl_noarch_release}.2.08.svn19020%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for pstricks


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
%{_texdir}/texmf-dist/dvips/pstricks/pst-algparser.pro
%{_texdir}/texmf-dist/dvips/pstricks/pst-dots.pro
%{_texdir}/texmf-dist/dvips/pstricks/pstricks.pro
%{_texdir}/texmf-dist/dvips/pstricks/pstricks97.pro
%{_texdir}/texmf-dist/tex/generic/pstricks/config/README
%{_texdir}/texmf-dist/tex/generic/pstricks/config/distiller.cfg
%{_texdir}/texmf-dist/tex/generic/pstricks/config/dvips.cfg
%{_texdir}/texmf-dist/tex/generic/pstricks/config/dvipsone.cfg
%{_texdir}/texmf-dist/tex/generic/pstricks/config/textures.cfg
%{_texdir}/texmf-dist/tex/generic/pstricks/config/vtex.cfg
%{_texdir}/texmf-dist/tex/generic/pstricks/config/xdvipdfmx.cfg
%{_texdir}/texmf-dist/tex/generic/pstricks/pst-fp.tex
%{_texdir}/texmf-dist/tex/generic/pstricks/pst-key.tex
%{_texdir}/texmf-dist/tex/generic/pstricks/pstricks.con
%{_texdir}/texmf-dist/tex/generic/pstricks/pstricks.tex
%{_texdir}/texmf-dist/tex/generic/pstricks/pstricks97.tex
%{_texdir}/texmf-dist/tex/latex/pstricks/pst-all.sty
%{_texdir}/texmf-dist/tex/latex/pstricks/pst-key.sty
%{_texdir}/texmf-dist/tex/latex/pstricks/pstcol.sty
%{_texdir}/texmf-dist/tex/latex/pstricks/pstricks.sty
%{_texdir}/texmf-dist/dvips/pstricks/pst-dots97.pro
%{_texdir}/texmf-dist/dvips/pstricks/pst-tools.pro
%{_texdir}/texmf-dist/tex/generic/pstricks/config/Changes
%{_texdir}/texmf-dist/tex/generic/pstricks/pstPlain.tex

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/generic/pstricks/Changes
%{_texdir}/texmf-dist/doc/generic/pstricks/Changes.dvips
%{_texdir}/texmf-dist/doc/generic/pstricks/Changes.generic
%{_texdir}/texmf-dist/doc/generic/pstricks/Changes.latex
%{_texdir}/texmf-dist/doc/generic/pstricks/PSTricks.bib
%{_texdir}/texmf-dist/doc/generic/pstricks/pst-doc.cls
%{_texdir}/texmf-dist/doc/generic/pstricks/pst-doc.ist
%{_texdir}/texmf-dist/doc/generic/pstricks/pst-doc.pdf
#%{_texdir}/texmf-dist/doc/generic/pstricks/pst-docfull.pdf
%{_texdir}/texmf-dist/doc/generic/pstricks/pst-news.sty
%{_texdir}/texmf-dist/doc/generic/pstricks/pst-news05.pdf
%{_texdir}/texmf-dist/doc/generic/pstricks/pst-news05.tex
%{_texdir}/texmf-dist/doc/generic/pstricks/pst-news06.pdf
%{_texdir}/texmf-dist/doc/generic/pstricks/pst-news06.tex
%{_texdir}/texmf-dist/doc/generic/pstricks/pst-news08.pdf
%{_texdir}/texmf-dist/doc/generic/pstricks/pst-news08.tex
%{_texdir}/texmf-dist/doc/generic/pstricks/pst-news09.pdf
%{_texdir}/texmf-dist/doc/generic/pstricks/pst-news09.tex
%{_texdir}/texmf-dist/doc/generic/pstricks/pst-news10.pdf
%{_texdir}/texmf-dist/doc/generic/pstricks/pst-news10.tex
%{_texdir}/texmf-dist/doc/generic/pstricks/pst-quickref.pdf
%{_texdir}/texmf-dist/doc/generic/pstricks/pst-user.pdf
%{_texdir}/texmf-dist/doc/generic/pstricks/pst-user.tgz
%{_texdir}/texmf-dist/doc/generic/pstricks/pst-usrfull.pdf
%{_texdir}/texmf-dist/doc/generic/pstricks/pstnews1-10.pdf
%{_texdir}/texmf-dist/doc/generic/pstricks/pstnews1-10.tex
%{_texdir}/texmf-dist/doc/generic/pstricks/pstnews1-11.pdf
%{_texdir}/texmf-dist/doc/generic/pstricks/pstnews1-11.tex
%{_texdir}/texmf-dist/doc/generic/pstricks/pstnews1-12.pdf
%{_texdir}/texmf-dist/doc/generic/pstricks/pstnews1-12.tex
%{_texdir}/texmf-dist/doc/generic/pstricks/pstnews97-15.pdf
%{_texdir}/texmf-dist/doc/generic/pstricks/pstnews97-15.tex
%{_texdir}/texmf-dist/doc/generic/pstricks/pstricks-bug.tex
%{_texdir}/texmf-dist/doc/generic/pstricks/pstricks-doc.pdf
%{_texdir}/texmf-dist/doc/generic/pstricks/test-pst.pdf
%{_texdir}/texmf-dist/doc/generic/pstricks/test-pst.tex
%{_texdir}/texmf-dist/doc/generic/pstricks/images/flowers.eps
%{_texdir}/texmf-dist/doc/generic/pstricks/images/tiger.eps
%{_texdir}/texmf-dist/doc/generic/pstricks/Makefile
%{_texdir}/texmf-dist/doc/generic/pstricks/README
%{_texdir}/texmf-dist/doc/generic/pstricks/ctandir.sty
%{_texdir}/texmf-dist/doc/generic/pstricks/images/tiger.pdf
%{_texdir}/texmf-dist/doc/generic/pstricks/pst-news.tex
%{_texdir}/texmf-dist/doc/generic/pstricks/pst-news11.pdf
%{_texdir}/texmf-dist/doc/generic/pstricks/pst-news11.tex
%{_texdir}/texmf-dist/doc/generic/pstricks/pst-news12.pdf
%{_texdir}/texmf-dist/doc/generic/pstricks/pst-news12.tex
%{_texdir}/texmf-dist/doc/generic/pstricks/pstricks-add-data9.data

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
