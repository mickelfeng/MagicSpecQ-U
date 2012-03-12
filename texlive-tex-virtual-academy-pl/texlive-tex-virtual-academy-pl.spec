%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/tex-virtual-academy-pl.doc.tar.xz

Name: texlive-tex-virtual-academy-pl-doc
License: LPPL
Summary: Documentation for tex-virtual-academy-pl
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description
Documentation for tex-virtual-academy-pl


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
xz -dc %{SOURCE0} | tar x -C %{buildroot}%{_texdir}/texmf-dist
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
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/TeX-pub.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/cototex.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/index.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/manifest.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/context/cont-ins.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/context/context.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/context/tytuly.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/fonty/back.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/fonty/font-abc.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/fonty/fonts_inst.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/fonty/index.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/fonty/nfss.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/fonty/qx-info.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/fonty/qx-table1.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/fonty/qx-table2.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/fonty/tpstyle.css
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/gify/artykul.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/gify/context.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/gify/cop.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/gify/grupa.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/gify/gust.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/gify/gustloge.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/gify/indexowanie.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/gify/latex2e.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/gify/lew-7vs.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/gify/lew.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/gify/mail.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/gify/podpis.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/gify/prog.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/gify/tex.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/gify/texologia.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/gify/wa.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx/day.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx/decode.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx/dies.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx/fig1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx/flags.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx/id.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx/index.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx/jedn.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx/lang.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx/lower.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx/mil.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx/mon.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx/name.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx/order.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx/plmindex.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx/porzadek.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx/program.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx/setki.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx/spec.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx/tex-idx.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx/toascii.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx/typy.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx/tys.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx/upper.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/kuchnia/hist.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/kuchnia/tex.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/latex2e.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/listy/desc_p1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/listy/desc_p2.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/listy/desc_p3.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/listy/desc_p4.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/listy/description.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/listy/description.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/listy/enum_p1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/listy/enum_p2.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/listy/enumerate.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/listy/enumerate.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/listy/item_p1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/listy/item_p2.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/listy/itemize.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/listy/itemize.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/listy/klopoty.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/listy/list.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/listy/lista_p.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/listy/porzadek.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/listy/standard.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/3parttab.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/3parttable.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/BAhhline.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/accent.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/accents.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/acromake.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/acromake.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/afterpage.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/alltt.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/amsthm.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/amsthm1.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/amsthm2.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/arabic.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/array.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/balance.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/bar.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/bar1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/bar2.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/bbm.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/bbm1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/bbm2.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/bbm3.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/bbm4.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/bbm5.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/bbm6.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/bbma.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/bbmb.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/blk1.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/blk2.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/blk3.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/blk4.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/blk5.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/blk6.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/blk7.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/blk8.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/blk9.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/blkarray.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/bm.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/bophook.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/boxedminipage.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/boxm.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/calc.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/calc1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/calc2.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/capt-of.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/caption.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/caption2.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/case1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/case2.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/cases.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/ccapt1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/ccaption.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/changebar.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/chapterbib.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/cite.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/color.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/color.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/colortbl.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/comma.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/cute1.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/cuted.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/dblcol.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/dblfnote.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/dcolumn.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/delarray.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/delarray.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/deleq.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/deleq1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/deleq10.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/deleq11.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/deleq12.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/deleq13.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/deleq14.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/deleq15.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/deleq2.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/deleq3.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/deleq4.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/deleq5.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/deleq6.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/deleq7.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/deleq8.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/deleq9.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/diam.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/dotseqn.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/dotseqn.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/dow.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/drftcite.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/dropp1.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/dropping.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/easyeqn.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/easyeqn1.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/easyeqn10.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/easyeqn11.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/easyeqn12.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/easyeqn13.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/easyeqn14.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/easyeqn15.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/easyeqn16.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/easyeqn17.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/easyeqn2.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/easyeqn3.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/easyeqn4.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/easyeqn5.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/easyeqn6.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/easyeqn7.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/easyeqn8.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/easyeqn9.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/endfloat.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/enum.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/enumerate.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/enumitem.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/epsfig.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/everyship.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/expdlist.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/exscale.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/extmath.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/extramarks.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/fancb1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/fancb2.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/fancb3.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/fancb4.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/fancb5.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/fancb6.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/fancb7.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/fancb8.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/fancybox.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/fancyhdr.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/fancyheading.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/filecontents.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/flafter.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/float.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/floatflt.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/floatpag.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/flt1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/flt2.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/fltpage.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/flushend.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/fn2end.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/fnpara.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/fnpara.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/fnpos.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/footmisc.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/footmisc1.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/footmisc2.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/footnpag.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/fp.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/ftnright.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/geom1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/geom1.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/geom2.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/geometry.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/graphicx.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/graphpaper.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/harp1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/harp2.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/harp3.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/harp4.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/harp5.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/harp6.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/harp7.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/harp8.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/harpoon.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/heart.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/here.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/hhline.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/hhline.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/hyperref.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/ifthen.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/ifthen1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/ifthen2.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/indentfirst.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/index.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/labeldeb.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/lastpage.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/lcg.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/legend.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/letter.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/letterspace.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/listpart.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/localloc.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/longtable.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/lscape.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/lt1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/ltablex.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/ltabptch.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/ltxtable.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/macro.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/macro_t.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/manyfoot.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/manyfoot1.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/minitoc.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/moje_typy.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/moreverb.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/mparhack.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/multfoot.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/multfoot1.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/multfoot2.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/multibox.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/multibox.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/multicol.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/multirow.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/multirow1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/multirow2.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/multirow3.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/multirow4.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/multirow5.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/mycss.css
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/num.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/numprint.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/nut.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/oldst1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/oldstyle.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/oubraces.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/overbrace.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/overbrace1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/pdfscreen.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/pfnote.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/plain.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/printtim.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/pstcol.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/q1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/qobitree.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/ragged2e.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/regcount.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/relsize.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/remreset.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/rotate.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/rotating.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/rotbox.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/selectpage.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/shadepar.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/shadetheorem.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/shadethm.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/shadethm.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/shadow.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/shapepar.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/shedbox.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/shortvrb.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/showkeys.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/sidecap.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/squa.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/stm1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/stm2.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/stm3.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/stm4.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/stmaryrd.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/sube1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/subeqn-1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/subeqn-2.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/subeqn-3.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/subeqn.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/subeqna.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/subeqnarray.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/subfig.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/subfigure.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/subfloat.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/sublabel.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/sublabel.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/subscript.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/supertabular.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/sverb.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/sverb_n.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/sverb_w.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/tabularx.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/tabularx.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/theorem.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/theorem.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/threeparttable.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/time.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/ulem.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/ulem.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/ulem1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/umoline.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/undertilde-1.png
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/undertilde.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/url.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/verbatim.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/verbdef.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/verbt.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/verbt1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/verbt2.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/version.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/vfrlocal.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/vmargin.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/vrbexin.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/vrflocal.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/wiggly.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/wmcropmark.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/wrapf.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/wrapfig.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/xr.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/xspace.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/xspace1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/xspace2.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro/xtab.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/pagina/pagina.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/spisy/chap.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/spisy/l_chap.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/spisy/l_sec.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/spisy/spis.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/spisy/spis.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/chapter.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/count.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/liczniki.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/num.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/p1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/p2.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/p3.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/p3.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/p4.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/p4.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/p5.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/p5.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/p6.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/p6.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/p7.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/p7.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/part.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/poziom.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/s.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/sect.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/tc.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/tc.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/tca.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/tl.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/tl.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/tr.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/tr.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/tx.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/tx.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/txx.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly/txx.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/poczatki/cont-pl.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/poczatki/emtex.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/poczatki/implementacje.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/poczatki/index.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/poczatki/inst-mik.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/poczatki/latex-pl.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/poczatki/mex.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/poczatki/miktex.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/poczatki/spw.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/poczatki/tetex.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/poczatki/web2c.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/podstawy/2-0wst1.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/podstawy/2-1coto.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/podstawy/2-1kazio.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/podstawy/2-1przyg.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/podstawy/2-1zece.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/podstawy/bib.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/podstawy/spis.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/podstawy/tex.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/podstawy/title.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/prog/auctex.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/prog/dvidvi.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/prog/dvistro1.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/prog/dvistro2.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/prog/hyph.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/prog/prog.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/prog/bibtex/bibtex-1.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/prog/bibtex/bibtex-2.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/prog/bibtex/bibtex-3.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/prog/bibtex/bibtex-4.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/prog/bibtex/bibtex-5.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/prog/bibtex/bibtex-6.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/prog/bibtex/bibtex-7.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/prog/bibtex/bibtex-8.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/prog/bibtex/bibtex.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/tex/fermat.gif
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/tex/odsylacze.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/tex/tex.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/tex/tex_key.html
%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/tex/tryby.html


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
