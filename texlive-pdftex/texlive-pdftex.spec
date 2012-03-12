%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/pdftex.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/pdftex.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/pdftex.doc.tar.xz

Name: texlive-pdftex
License: GPL+
Summary: A TeX extension for direct creation of PDF
Version: %{tl_version}
Release: %{tl_noarch_release}.1.40.10.svn19496%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-kpathsea = %{tl_version}
Requires: texlive-pdftex-bin = %{tl_version}

%description
An extension of TeX which can be configured to directly
generate PDF documents instead of DVI. All current TeX
distributions including TeX live, MacTeX and MiKTeX include
pdfTeX (Plain TeX) and pdfLaTeX (LaTeX). ConTeXt is designed
around use of pdfTeX.

date: 2009-12-01 09:55:52 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
sed -i 's/^\#\!\ pdftex/pdftex pdftex language.def -translate-file=cp227.tcx *pdfetex.ini/' %{_texdir}/texmf/web2c/fmtutil.cnf
sed -i 's/^\#\!\ etex/etex pdftex language.def -translate-file=cp227.tcx *etex.ini/' %{_texdir}/texmf/web2c/fmtutil.cnf
sed -i 's/^\#\!\ pdfetex/pdfetex pdftex language.def -translate-file=cp227.tcx *pdfetex.ini/' %{_texdir}/texmf/web2c/fmtutil.cnf
touch /var/run/texlive/run-fmtutil
:

%postun
if [ $1 == 0 ]; then
  sed -i 's/^pdftex/\#\!\ pdftex/' %{_texdir}/texmf/web2c/fmtutil.cnf
  sed -i 's/^etex/\#\!\ etex/' %{_texdir}/texmf/web2c/fmtutil.cnf
  sed -i 's/^pdfetex/\#\!\ pdfetex/' %{_texdir}/texmf/web2c/fmtutil.cnf
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
Summary: Documentation for pdftex
Version: %{tl_version}
Release: %{tl_noarch_release}.1.40.10.svn19496%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch
Requires: texlive-kpathsea-doc

%description doc
Documentation for pdftex


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/gpl.txt gpl.txt
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
%doc gpl.txt
%{_mandir}/man1/pdfetex.1*
%{_mandir}/man1/pdftex.1*
%{_texdir}/texmf/tex/generic/config/pdftex-dvi.tex
%{_texdir}/texmf/tex/generic/config/pdftexconfig.tex
%{_texdir}/texmf/fonts/map/pdftex/updmap/pdftex.map
%{_texdir}/texmf/fonts/map/pdftex/updmap/pdftex_dl14.map
%{_texdir}/texmf/fonts/map/pdftex/updmap/pdftex_ndl14.map
%{_texdir}/texmf/scripts/simpdftex/simpdftex
%{_texdir}/texmf/tex/generic/pdftex/glyphtounicode.tex

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/pdftex/Announcement-1.40.2
%{_texdir}/texmf-dist/doc/pdftex/NEWS
%{_texdir}/texmf-dist/doc/pdftex/README
%{_texdir}/texmf-dist/doc/pdftex/manual/ChangeLog
%{_texdir}/texmf-dist/doc/pdftex/manual/Makefile
%{_texdir}/texmf-dist/doc/pdftex/manual/README
%{_texdir}/texmf-dist/doc/pdftex/manual/makefiles.cmd
%{_texdir}/texmf-dist/doc/pdftex/manual/pdftex-a.pdf
%{_texdir}/texmf-dist/doc/pdftex/manual/pdftex-i.tex
%{_texdir}/texmf-dist/doc/pdftex/manual/pdftex-l.pdf
%{_texdir}/texmf-dist/doc/pdftex/manual/pdftex-s.pdf
%{_texdir}/texmf-dist/doc/pdftex/manual/pdftex-syntax.txt
%{_texdir}/texmf-dist/doc/pdftex/manual/pdftex-t.tex
%{_texdir}/texmf-dist/doc/pdftex/manual/pdftex-t.txt
#%{_texdir}/texmf-dist/doc/pdftex/manual/pdftex-w.pdf
%{_texdir}/texmf-dist/doc/pdftex/manual/pdftex-w.tex
%{_texdir}/texmf-dist/doc/pdftex/manual/syntaxform.awk
%{_texdir}/texmf-dist/doc/pdftex/manual/samplepdf/cmr10.103
%{_texdir}/texmf-dist/doc/pdftex/manual/samplepdf/obj.dat
%{_texdir}/texmf-dist/doc/pdftex/manual/samplepdf/pdfcolor.tex
%{_texdir}/texmf-dist/doc/pdftex/manual/samplepdf/pic.eps
%{_texdir}/texmf-dist/doc/pdftex/manual/samplepdf/pic.jpg
%{_texdir}/texmf-dist/doc/pdftex/manual/samplepdf/pic.mps
%{_texdir}/texmf-dist/doc/pdftex/manual/samplepdf/pic.pdf
%{_texdir}/texmf-dist/doc/pdftex/manual/samplepdf/pic.png
%{_texdir}/texmf-dist/doc/pdftex/manual/samplepdf/pic16.png
%{_texdir}/texmf-dist/doc/pdftex/manual/samplepdf/rgb.icc
%{_texdir}/texmf-dist/doc/pdftex/manual/samplepdf/samplepdf.0
%{_texdir}/texmf-dist/doc/pdftex/manual/samplepdf/samplepdf.1
%{_texdir}/texmf-dist/doc/pdftex/manual/samplepdf/samplepdf.tex
%{_texdir}/texmf-dist/doc/pdftex/manual/samplepdf/supp-mis.tex
%{_texdir}/texmf-dist/doc/pdftex/manual/samplepdf/supp-pdf.tex
%{_texdir}/texmf-dist/doc/pdftex/manual/samplepdf/tmp.pdf
%{_texdir}/texmf-dist/doc/pdftex/pdftex-pdfkeys/Makefile
%{_texdir}/texmf-dist/doc/pdftex/pdftex-pdfkeys/fdl.tex
%{_texdir}/texmf-dist/doc/pdftex/pdftex-pdfkeys/pdftex-pdfkeys.bbl
%{_texdir}/texmf-dist/doc/pdftex/pdftex-pdfkeys/pdftex-pdfkeys.pdf
%{_texdir}/texmf-dist/doc/pdftex/pdftex-pdfkeys/pdftex-pdfkeys.tex
%{_texdir}/texmf-dist/doc/pdftex/thanh/ext/abbr.tex
%{_texdir}/texmf-dist/doc/pdftex/thanh/ext/efcode.tex
%{_texdir}/texmf-dist/doc/pdftex/thanh/ext/il2.etx
%{_texdir}/texmf-dist/doc/pdftex/thanh/ext/il2.mtx
%{_texdir}/texmf-dist/doc/pdftex/thanh/ext/il2protcode.tex
%{_texdir}/texmf-dist/doc/pdftex/thanh/ext/mktextfm
%{_texdir}/texmf-dist/doc/pdftex/thanh/ext/mktextfm.ext
%{_texdir}/texmf-dist/doc/pdftex/thanh/ext/mktfm8z
%{_texdir}/texmf-dist/doc/pdftex/thanh/ext/protcode.tex
%{_texdir}/texmf-dist/doc/pdftex/thanh/ext/ufntinst.sty


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
