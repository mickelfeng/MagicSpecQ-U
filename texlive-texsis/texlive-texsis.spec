%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/texsis.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/texsis.doc.tar.xz

Name: texlive-texsis
License: LPPL
Summary: Plain TeX macros for Physicists
Version: %{tl_version}
Release: %{tl_noarch_release}.2.18.svn18835%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tex = %{tl_version}
Requires: texlive-texsis-bin = %{tl_version}

%description
TeXsis is a TeX macro package which provides useful features
for typesetting research papers and related documents. For
example, it includes support specifically for: Automatic
numbering of equations, figures, tables and references;
Simplified control of type sizes, line spacing, footnotes,
running headlines and footlines, and tables of contents,
figures and tables; Specialized document formats for research
papers, preprints and ``e-prints,'' conference proceedings,
theses, books, referee reports, letters, and memoranda;
Simplified means of constructing an index for a book or thesis;
Easy to use double column formatting; Specialized environments
for lists, theorems and proofs, centered or non-justified text,
and listing computer code; Specialized macros for easily
constructing ruled tables. TeXsis was originally developed for
physicists, but others may also find it useful. It is
completely compatible with Plain TeX.

date: 2006-12-11 00:37:24 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
sed -i 's/^\#\!\ texsis/texsis pdftex - -translate-file=cp227.tcx texsis.ini/' %{_texdir}/texmf/web2c/fmtutil.cnf
touch /var/run/texlive/run-fmtutil
:

%postun
if [ $1 == 0 ]; then
  sed -i 's/^texsis/\#\!\ texsis/' %{_texdir}/texmf/web2c/fmtutil.cnf
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
Summary: Documentation for texsis
Version: %{tl_version}
Release: %{tl_noarch_release}.2.18.svn18835%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for texsis


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/lppl.txt lppl.txt
xz -dc %{SOURCE0} | tar x -C %{buildroot}%{_texdir}
xz -dc %{SOURCE1} | tar x -C %{buildroot}%{_texdir}
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
%{_texdir}/texmf-dist/bibtex/bst/texsis/texsis.bst
%{_texdir}/texmf-dist/tex/texsis/base/AIP.txs
%{_texdir}/texmf-dist/tex/texsis/base/CVformat.txs
%{_texdir}/texmf-dist/tex/texsis/base/Elsevier.txs
%{_texdir}/texmf-dist/tex/texsis/base/Exam.txs
%{_texdir}/texmf-dist/tex/texsis/base/Formletr.txs
%{_texdir}/texmf-dist/tex/texsis/base/IEEE.txs
%{_texdir}/texmf-dist/tex/texsis/base/PhysRev.txs
%{_texdir}/texmf-dist/tex/texsis/base/Spanish.txs
%{_texdir}/texmf-dist/tex/texsis/base/Swedish.txs
%{_texdir}/texmf-dist/tex/texsis/base/TXSconts.tex
%{_texdir}/texmf-dist/tex/texsis/base/TXSdcol.tex
%{_texdir}/texmf-dist/tex/texsis/base/TXSenvmt.tex
%{_texdir}/texmf-dist/tex/texsis/base/TXSeqns.tex
%{_texdir}/texmf-dist/tex/texsis/base/TXSfigs.tex
%{_texdir}/texmf-dist/tex/texsis/base/TXSfmts.tex
%{_texdir}/texmf-dist/tex/texsis/base/TXSfonts.tex
%{_texdir}/texmf-dist/tex/texsis/base/TXShead.tex
%{_texdir}/texmf-dist/tex/texsis/base/TXSinit.tex
%{_texdir}/texmf-dist/tex/texsis/base/TXSletr.tex
%{_texdir}/texmf-dist/tex/texsis/base/TXSmacs.tex
%{_texdir}/texmf-dist/tex/texsis/base/TXSmemo.tex
%{_texdir}/texmf-dist/tex/texsis/base/TXSprns.tex
%{_texdir}/texmf-dist/tex/texsis/base/TXSrefs.tex
%{_texdir}/texmf-dist/tex/texsis/base/TXSruled.tex
%{_texdir}/texmf-dist/tex/texsis/base/TXSsects.tex
%{_texdir}/texmf-dist/tex/texsis/base/TXSsite.tex
%{_texdir}/texmf-dist/tex/texsis/base/TXSsymb.tex
%{_texdir}/texmf-dist/tex/texsis/base/TXStags.tex
%{_texdir}/texmf-dist/tex/texsis/base/TXStitle.tex
%{_texdir}/texmf-dist/tex/texsis/base/Tablebod.txs
%{_texdir}/texmf-dist/tex/texsis/base/WorldSci.txs
%{_texdir}/texmf-dist/tex/texsis/base/color.txs
%{_texdir}/texmf-dist/tex/texsis/base/nuclproc.txs
%{_texdir}/texmf-dist/tex/texsis/base/printfont.txs
%{_texdir}/texmf-dist/tex/texsis/base/spine.txs
%{_texdir}/texmf-dist/tex/texsis/base/texsis.tex
%{_texdir}/texmf-dist/tex/texsis/base/thesis.txs
%{_texdir}/texmf-dist/tex/texsis/base/twin.txs
%{_texdir}/texmf-dist/tex/texsis/config/texsis.ini

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/COPYING
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/Example.tex
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/Fonts.tex
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/INSTALL
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/Install.tex
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/MANIFEST
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/Manual.fgl
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/Manual.ref
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/Manual.tbl
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/Manual.tex
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/NEWS
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/README
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/TXSapxF.doc
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/TXScover.doc
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/TXSdcol.doc
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/TXSdoc.doc
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/TXSdoc0.doc
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/TXSdocM.doc
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/TXSend.doc
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/TXSenvmt.doc
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/TXSeqns.doc
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/TXSfigs.doc
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/TXSfmts.doc
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/TXSfonts.doc
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/TXSinstl.doc
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/TXSintro.doc
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/TXSletr.doc
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/TXSmisc.doc
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/TXSprns.doc
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/TXSrefs.doc
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/TXSrevs.doc
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/TXSruled.doc
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/TXSsects.doc
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/TXSsite.000
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/TXSsymb.doc
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/TXStags.doc
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/index.tex
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/letr
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/penguin.eps
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/penguin2.eps
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/texsis.1
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/texsis.el
%{_texdir}/texmf-dist/doc/otherformats/texsis/base/texsis.lsm


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
