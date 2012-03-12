%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/ctex.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/ctex.doc.tar.xz

Name: texlive-ctex
License: LPPL
Summary: LaTeX classes and packages for Chinese typesetting
Version: %{tl_version}
Release: %{tl_noarch_release}.0.97.svn16809%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-ttfutils = %{tl_version}
Provides: tex(ctexartutf8.sty)
Provides: tex(ctexbookutf8.sty)
Provides: tex(ctexcaputf8.sty)
Provides: tex(ctexreputf8.sty)
Provides: tex(ctexutf8.sty)
Provides: tex(ctex.sty)
Provides: tex(ctexart.sty)
Provides: tex(ctexbook.sty)
Provides: tex(ctexcap.sty)
Provides: tex(ctexrep.sty)

%description
ctex package

date: 2010-01-22 18:08:42 +0100

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
Summary: Documentation for ctex
Version: %{tl_version}
Release: %{tl_noarch_release}.0.97.svn16809%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch
Requires: texlive-ttfutils-doc

%description doc
Documentation for ctex


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
%{_texdir}/texmf-dist/tex/latex/ctex/back/ctexartutf8.cls
%{_texdir}/texmf-dist/tex/latex/ctex/back/ctexbookutf8.cls
%{_texdir}/texmf-dist/tex/latex/ctex/back/ctexcaputf8.sty
%{_texdir}/texmf-dist/tex/latex/ctex/back/ctexreputf8.cls
%{_texdir}/texmf-dist/tex/latex/ctex/back/ctexutf8.sty
%{_texdir}/texmf-dist/tex/latex/ctex/cfg/ctex.cfg
%{_texdir}/texmf-dist/tex/latex/ctex/cfg/ctexcap-gbk.cfg
%{_texdir}/texmf-dist/tex/latex/ctex/cfg/ctexcap-utf8.cfg
%{_texdir}/texmf-dist/tex/latex/ctex/cfg/ctexcap.cfg
%{_texdir}/texmf-dist/tex/latex/ctex/cfg/ctexopts.cfg.template
%{_texdir}/texmf-dist/tex/latex/ctex/ctex.sty
%{_texdir}/texmf-dist/tex/latex/ctex/ctexart.cls
%{_texdir}/texmf-dist/tex/latex/ctex/ctexbook.cls
%{_texdir}/texmf-dist/tex/latex/ctex/ctexcap.sty
%{_texdir}/texmf-dist/tex/latex/ctex/ctexrep.cls
%{_texdir}/texmf-dist/tex/latex/ctex/def/ctex-article.def
%{_texdir}/texmf-dist/tex/latex/ctex/def/ctex-book.def
%{_texdir}/texmf-dist/tex/latex/ctex/def/ctex-caption.def
%{_texdir}/texmf-dist/tex/latex/ctex/def/ctex-class.def
%{_texdir}/texmf-dist/tex/latex/ctex/def/ctex-common.def
%{_texdir}/texmf-dist/tex/latex/ctex/def/ctex-gbk.def
%{_texdir}/texmf-dist/tex/latex/ctex/def/ctex-loadclass.def
%{_texdir}/texmf-dist/tex/latex/ctex/def/ctex-report.def
%{_texdir}/texmf-dist/tex/latex/ctex/def/ctex-utf8.def
%{_texdir}/texmf-dist/tex/latex/ctex/engine/ctex-cct-engine.def
%{_texdir}/texmf-dist/tex/latex/ctex/engine/ctex-cjk-common.def
%{_texdir}/texmf-dist/tex/latex/ctex/engine/ctex-cjk-engine.def
%{_texdir}/texmf-dist/tex/latex/ctex/engine/ctex-xecjk-engine.def
%{_texdir}/texmf-dist/tex/latex/ctex/fd/c19gbsn.fd
%{_texdir}/texmf-dist/tex/latex/ctex/fd/c19gbsn.fdx
%{_texdir}/texmf-dist/tex/latex/ctex/fd/c19gkai.fd
%{_texdir}/texmf-dist/tex/latex/ctex/fd/c19gkai.fdx
%{_texdir}/texmf-dist/tex/latex/ctex/fd/c19rm.fd
%{_texdir}/texmf-dist/tex/latex/ctex/fd/c19sf.fd
%{_texdir}/texmf-dist/tex/latex/ctex/fd/c19tt.fd
%{_texdir}/texmf-dist/tex/latex/ctex/fd/c70rm.fd
%{_texdir}/texmf-dist/tex/latex/ctex/fd/c70sf.fd
%{_texdir}/texmf-dist/tex/latex/ctex/fd/c70tt.fd
%{_texdir}/texmf-dist/tex/latex/ctex/fontset/ctex-cjk-adobefonts.def
%{_texdir}/texmf-dist/tex/latex/ctex/fontset/ctex-cjk-winfonts.def
%{_texdir}/texmf-dist/tex/latex/ctex/fontset/ctex-xecjk-adobefonts.def
%{_texdir}/texmf-dist/tex/latex/ctex/fontset/ctex-xecjk-winfonts.def
%{_texdir}/texmf-dist/tex/latex/ctex/opt/ctex-caption-opts.def
%{_texdir}/texmf-dist/tex/latex/ctex/opt/ctex-class-opts.def
%{_texdir}/texmf-dist/tex/latex/ctex/opt/ctex-common-opts.def

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/ctex/README
%{_texdir}/texmf-dist/doc/latex/ctex/ctex.pdf
%{_texdir}/texmf-dist/doc/latex/ctex/ctex.tex
%{_texdir}/texmf-dist/doc/latex/ctex/test/test-cjk.tex
%{_texdir}/texmf-dist/doc/latex/ctex/test/test-cjkutf8.tex
%{_texdir}/texmf-dist/doc/latex/ctex/test/test-xetex.tex
%{_texdir}/texmf-dist/doc/latex/ctex/test/test-xetexgbk.tex


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
