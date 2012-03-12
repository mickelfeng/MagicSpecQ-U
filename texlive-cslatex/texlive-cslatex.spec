%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cslatex.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cslatex.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cslatex.source.tar.xz

Name: texlive-cslatex
License: GPL+
Summary: LaTeX support for Czech/Slovak typesetting
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18835%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-latex = %{tl_version}
Requires: texlive-cslatex-bin = %{tl_version}
Provides: tex(nhelvet.sty)
Provides: tex(ntimes.sty)

%description
cslatex package

date: 2009-09-24 20:53:04 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
sed -i 's/^\#\!\ cslatex/cslatex pdftex - -etex -translate-file=cp227.tcx cslatex.ini/' %{_texdir}/texmf/web2c/fmtutil.cnf
sed -i 's/^\#\!\ pdfcslatex/pdfcslatex pdftex - -etex -translate-file=cp227.tcx cslatex.ini/' %{_texdir}/texmf/web2c/fmtutil.cnf
touch /var/run/texlive/run-fmtutil
:

%postun
if [ $1 == 0 ]; then
  sed -i 's/^cslatex/\#\!\ cslatex/' %{_texdir}/texmf/web2c/fmtutil.cnf
  sed -i 's/^pdfcslatex/\#\!\ pdfcslatex/' %{_texdir}/texmf/web2c/fmtutil.cnf
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
Summary: Documentation for cslatex
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18835%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch
Requires: texlive-latex-doc

%description doc
Documentation for cslatex


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/gpl.txt gpl.txt
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
%doc gpl.txt
%{_texdir}/texmf-dist/tex/cslatex/base/cslatex-utf8.ini
%{_texdir}/texmf-dist/tex/cslatex/base/cslatex.ini
%{_texdir}/texmf-dist/tex/cslatex/base/cspsfont.il2
%{_texdir}/texmf-dist/tex/cslatex/base/cspsfont.tex
%{_texdir}/texmf-dist/tex/cslatex/base/cspsfont.xl2
%{_texdir}/texmf-dist/tex/cslatex/base/fonttext.cfg
%{_texdir}/texmf-dist/tex/cslatex/base/hyphen.cfg
%{_texdir}/texmf-dist/tex/cslatex/base/il2pag.fd
%{_texdir}/texmf-dist/tex/cslatex/base/il2pbk.fd
%{_texdir}/texmf-dist/tex/cslatex/base/il2pcr.fd
%{_texdir}/texmf-dist/tex/cslatex/base/il2phv.fd
%{_texdir}/texmf-dist/tex/cslatex/base/il2phvn.fd
%{_texdir}/texmf-dist/tex/cslatex/base/il2pnc.fd
%{_texdir}/texmf-dist/tex/cslatex/base/il2ppl.fd
%{_texdir}/texmf-dist/tex/cslatex/base/il2ptm.fd
%{_texdir}/texmf-dist/tex/cslatex/base/il2pzc.fd
%{_texdir}/texmf-dist/tex/cslatex/base/nhelvet.sty
%{_texdir}/texmf-dist/tex/cslatex/base/ntimes.sty
%{_texdir}/texmf-dist/tex/cslatex/base/xl2pag.fd
%{_texdir}/texmf-dist/tex/cslatex/base/xl2pbk.fd
%{_texdir}/texmf-dist/tex/cslatex/base/xl2pcr.fd
%{_texdir}/texmf-dist/tex/cslatex/base/xl2phv.fd
%{_texdir}/texmf-dist/tex/cslatex/base/xl2phvn.fd
%{_texdir}/texmf-dist/tex/cslatex/base/xl2pnc.fd
%{_texdir}/texmf-dist/tex/cslatex/base/xl2ppl.fd
%{_texdir}/texmf-dist/tex/cslatex/base/xl2ptm.fd
%{_texdir}/texmf-dist/tex/cslatex/base/xl2pzc.fd
%{_texdir}/texmf-dist/tex/latex/cslatex/il2cmdh.fd
%{_texdir}/texmf-dist/tex/latex/cslatex/il2cmfib.fd
%{_texdir}/texmf-dist/tex/latex/cslatex/il2cmfr.fd
%{_texdir}/texmf-dist/tex/latex/cslatex/il2cmr.fd
%{_texdir}/texmf-dist/tex/latex/cslatex/il2cmss.fd
%{_texdir}/texmf-dist/tex/latex/cslatex/il2cmtt.fd
%{_texdir}/texmf-dist/tex/latex/cslatex/il2cmvtt.fd
%{_texdir}/texmf-dist/tex/latex/cslatex/il2enc.def
%{_texdir}/texmf-dist/tex/latex/cslatex/il2lcmss.fd
%{_texdir}/texmf-dist/tex/latex/cslatex/il2lcmtt.fd

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/cslatex/base/INSTALL.cslatex
%{_texdir}/texmf-dist/doc/cslatex/base/README-cspsfont
%{_texdir}/texmf-dist/doc/cslatex/base/README.cslatex
%{_texdir}/texmf-dist/doc/cslatex/base/cs-fonts.doc
%{_texdir}/texmf-dist/doc/cslatex/base/cscorr.tab
%{_texdir}/texmf-dist/doc/cslatex/base/csplain.doc
%{_texdir}/texmf-dist/doc/cslatex/base/license.eng
%{_texdir}/texmf-dist/doc/cslatex/base/mklinks
%{_texdir}/texmf-dist/doc/cslatex/base/parpozn.tex
%{_texdir}/texmf-dist/doc/cslatex/base/prvni.tex
%{_texdir}/texmf-dist/doc/cslatex/base/test8z.tex
%{_texdir}/texmf-dist/doc/cslatex/base/testlat.tex
%{_texdir}/texmf-dist/doc/cslatex/base/zmeny.txt


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
