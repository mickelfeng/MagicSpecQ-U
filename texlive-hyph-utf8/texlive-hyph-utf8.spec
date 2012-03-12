%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/hyph-utf8.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/hyph-utf8.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/hyph-utf8.source.tar.xz

Name: texlive-hyph-utf8
License: Freely redistributable without restriction
Summary: Hyphenation patterns expressed in UTF-8
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18895%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: lua

%description
Modern native UTF-8 engines such as XeTeX and LuaTeX need
hyphenation patterns in UTF-8 format, whereas older systems
require hyphenation patterns in the 8-bit encoding of the font
in use (such encodings are codified in the LaTeX scheme with
names like OT1, T2A, TS1, OML, LY1, etc). The present package
offers a collection of conversions of existing patterns to UTF-
8 format, together with converters for use with 8-bit fonts in
older systems. Since hyphenation patterns for TeX are only read
at iniTeX time, it is hoped that the UTF-8 patterns, with their
converters, will completely supplant the older patterns.

date: 2010-06-01 11:48:39 +0200

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
Summary: Documentation for hyph-utf8
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18895%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for hyph-utf8


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/other-free.txt other-free.txt
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
%doc other-free.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/conversions/conv-utf8-ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/conversions/conv-utf8-il2.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/conversions/conv-utf8-il3.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/conversions/conv-utf8-l7x.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/conversions/conv-utf8-lmc.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/conversions/conv-utf8-qx.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/conversions/conv-utf8-t2a.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-as.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-bg.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-bn.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-ca.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-cop.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-cs.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-cy.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-da.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-de-1901.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-de-1996.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-de-ch-1901.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-el-monoton.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-el-polyton.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-en-gb.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-en-us.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-eo.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-es.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-et.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-eu.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-fi.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-fr.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-ga.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-gl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-grc.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-gu.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-hi.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-hr.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-hsb.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-hu.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-hy.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-ia.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-id.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-is.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-it.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-kmr.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-kn.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-la.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-lo.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-lt.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-lv.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-ml.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-mn-cyrl-x-lmc.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-mn-cyrl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-mr.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-nb.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-nl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-nn.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-or.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-pa.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-pl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-pt.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-ro.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-ru.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-sa.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-sk.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-sl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-sr-cyrl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-sr-latn.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-sv.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-ta.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-te.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-tk.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-tr.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-uk.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-as.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-bg.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-bn.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-ca.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-cop.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-cs.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-cy.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-da.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-de-1901.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-de-1996.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-de-ch-1901.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-el-monoton.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-el-polyton.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-en-gb.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-en-us.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-eo.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-es.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-et.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-eu.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-fi.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-fr.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-ga.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-gl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-grc.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-gu.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-hi.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-hr.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-hsb.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-hu.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-hy.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-ia.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-id.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-is.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-it.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-kmr.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-kn.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-la.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-lo.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-lt.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-lv.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-ml.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-mn-cyrl-x-lmc.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-mn-cyrl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-mr.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-nb.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-nl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-nn.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-no.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-or.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-pa.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-pl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-pt.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-ro.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-ru.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-sa.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-sh-cyrl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-sh-latn.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-sk.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-sl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-sr-cyrl.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-sv.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-ta.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-te.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-tk.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-tr.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-uk.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-as.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-as.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-as.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-as.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-bg.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-bg.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-bg.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-bg.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-bn.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-bn.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-bn.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-bn.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ca.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ca.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ca.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ca.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cop.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cop.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cop.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cop.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cs.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cs.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cs.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cs.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cy.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cy.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cy.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-cy.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-da.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-da.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-da.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-da.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-de-1901.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-de-1901.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-de-1901.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-de-1901.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-de-1996.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-de-1996.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-de-1996.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-de-1996.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-de-ch-1901.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-de-ch-1901.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-de-ch-1901.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-de-ch-1901.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-el-monoton.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-el-monoton.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-el-monoton.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-el-monoton.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-el-polyton.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-el-polyton.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-el-polyton.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-el-polyton.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-en-gb.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-en-gb.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-en-gb.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-en-gb.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-en-us.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-en-us.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-en-us.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-en-us.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-eo.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-eo.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-eo.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-eo.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-es.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-es.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-es.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-es.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-et.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-et.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-et.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-et.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-eu.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-eu.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-eu.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-eu.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-fi.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-fi.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-fi.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-fi.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-fr.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-fr.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-fr.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-fr.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ga.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ga.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ga.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ga.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-gl.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-gl.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-gl.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-gl.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-grc.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-grc.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-grc.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-grc.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-gu.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-gu.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-gu.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-gu.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hi.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hi.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hi.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hi.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hr.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hr.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hr.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hr.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hsb.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hsb.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hsb.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hsb.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hu.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hu.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hu.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hu.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hy.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hy.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hy.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-hy.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ia.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ia.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ia.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ia.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-id.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-id.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-id.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-id.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-is.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-is.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-is.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-is.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-it.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-it.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-it.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-it.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-kmr.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-kmr.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-kmr.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-kmr.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-kn.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-kn.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-kn.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-kn.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-la.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-la.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-la.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-la.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-lo.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-lo.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-lo.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-lo.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-lt.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-lt.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-lt.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-lt.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-lv.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-lv.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-lv.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-lv.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ml.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ml.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ml.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ml.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-mn-cyrl.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-mn-cyrl.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-mn-cyrl.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-mn-cyrl.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-mr.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-mr.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-mr.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-mr.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-nb.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-nb.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-nb.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-nb.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-nl.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-nl.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-nl.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-nl.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-nn.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-nn.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-nn.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-nn.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-or.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-or.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-or.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-or.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pa.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pa.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pa.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pa.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pl.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pl.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pl.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pl.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pt.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pt.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pt.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-pt.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ro.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ro.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ro.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ro.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ru.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ru.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ru.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ru.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sa.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sa.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sa.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sa.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sk.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sk.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sk.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sk.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sl.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sl.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sl.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sl.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sr-cyrl.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sr-cyrl.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sr-cyrl.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sr-cyrl.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sv.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sv.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sv.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sv.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ta.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ta.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ta.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-ta.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-te.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-te.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-te.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-te.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-tk.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-tk.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-tk.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-tk.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-tr.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-tr.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-tr.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-tr.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-uk.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-uk.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-uk.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-uk.pat.txt
%{_texdir}/texmf-dist/tex/luatex/hyph-utf8/etex.src
%{_texdir}/texmf-dist/tex/luatex/hyph-utf8/hyphen.cfg
%{_texdir}/texmf-dist/tex/luatex/hyph-utf8/luatex-hyphen.lua
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-af.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-mul-ethi.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph/loadhyph-zh-latn-pinyin.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-af.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-bg.t2a.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-ca.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-cs.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-cy.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-da.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-de-1901.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-de-1996.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-de-ch-1901.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-eo.il3.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-es.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-et.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-eu.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-fi.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-fr.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-ga.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-gl.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-hr.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-hsb.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-hu.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-is.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-kmr.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-la.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-lt.l7x.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-lv.l7x.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-mn-cyrl-x-lmc.lmc.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-mn-cyrl.t2a.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-nb.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-nl.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-nn.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-pl.qx.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-pt.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-ro.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-ru.t2a.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-sh-cyrl.t2a.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-sh-latn.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-sk.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-sl.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-sv.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-tk.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-tr.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-uk.t2a.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/hyph-zh-latn-pinyin.ec.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/quote/hyph-quote-af.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/quote/hyph-quote-fr.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/quote/hyph-quote-it.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/quote/hyph-quote-uk.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/quote/hyph-quote-zh-latn-pinyin.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex-8bit/copthyph.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-af.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-mul-ethi.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex/hyph-zh-latn-pinyin.tex
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-af.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-af.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-af.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-af.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-mul-ethi.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-mul-ethi.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-mul-ethi.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-mul-ethi.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sh-cyrl.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sh-cyrl.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sh-cyrl.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sh-cyrl.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sh-latn.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sh-latn.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sh-latn.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-sh-latn.pat.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-zh-latn-pinyin.chr.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-zh-latn-pinyin.hyp.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-zh-latn-pinyin.lic.txt
%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt/hyph-zh-latn-pinyin.pat.txt

%files doc
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/doc/generic/hyph-utf8/CHANGES
%{_texdir}/texmf-dist/doc/generic/hyph-utf8/README
%{_texdir}/texmf-dist/doc/generic/hyph-utf8/hyphenation.pdf
%{_texdir}/texmf-dist/doc/generic/hyph-utf8/hyphenation.tex
%{_texdir}/texmf-dist/doc/generic/hyph-utf8/bg/azbukaExtended.pdf
%{_texdir}/texmf-dist/doc/generic/hyph-utf8/bg/azbukaExtended.tex
%{_texdir}/texmf-dist/doc/generic/hyph-utf8/es/README
%{_texdir}/texmf-dist/doc/generic/hyph-utf8/es/division.pdf
%{_texdir}/texmf-dist/doc/generic/hyph-utf8/hu/huhyphn.pdf
%{_texdir}/texmf-dist/doc/generic/hyph-utf8/sa/hyphenmin.txt
%{_texdir}/texmf-dist/doc/luatex/hyph-utf8/README
%{_texdir}/texmf-dist/doc/luatex/hyph-utf8/luatex-hyphen.pdf
%{_texdir}/texmf-dist/doc/generic/hyph-utf8/hyphenation-distribution.pdf
%{_texdir}/texmf-dist/doc/generic/hyph-utf8/hyphenation-distribution.tex
%{_texdir}/texmf-dist/doc/generic/hyph-utf8/img/miktex-languages.png
%{_texdir}/texmf-dist/doc/generic/hyph-utf8/img/texlive-collection-lang.png

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
