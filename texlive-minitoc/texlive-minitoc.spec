%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/minitoc.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/minitoc.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/minitoc.source.tar.xz

Name: texlive-minitoc
License: LPPL
Summary: Produce a table of contents for each chapter, part or section
Version: %{tl_version}
Release: %{tl_noarch_release}.60.svn16836%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(boldsc.sty)
Provides: tex(dblaccnt.sty)
Provides: tex(franc.sty)
Provides: tex(frbib.sty)
Provides: tex(frnew.sty)
Provides: tex(minitoc.sty)
Provides: tex(mtcmess.sty)
Provides: tex(mtcoff.sty)
Provides: tex(mtcpatchmem.sty)
Provides: tex(mypatches.sty)
Requires: tex(flafter.sty)
Requires: tex(placeins.sty)
Requires: tex(notoccite.sty)
Requires: tex(cmsd.sty)

%description
The minitoc package allows you to add mini-tables-of-contents
(minitocs) at the beginning of every chapter, part or section.
There is also provision for mini-lists of figures and of
tables. At the part level, they are parttocs, partlofs and
partlots. If the type of document does not use chapters, the
basic provision is section level secttocs, sectlofs and
sectlots. The package has provision for language-specific
configuration of its own "fixed names", using .mld files
(analagous to babel .ldf files that do that job for LaTeX"s own
fixed names).

date: 2009-05-26 00:38:29 +0200

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
Summary: Documentation for minitoc
Version: %{tl_version}
Release: %{tl_noarch_release}.60.svn16836%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for minitoc


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
%{_texdir}/texmf-dist/bibtex/bst/minitoc/en-mtc.bst
%{_texdir}/texmf-dist/bibtex/bst/minitoc/fr-mtc.bst
%{_texdir}/texmf-dist/makeindex/minitoc/minitoc-fr.ist
%{_texdir}/texmf-dist/makeindex/minitoc/minitoc.ist
%{_texdir}/texmf-dist/tex/latex/minitoc/UKenglish.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/USenglish.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/acadian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/acadien.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/afrikaan.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/afrikaans.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/albanian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/american.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/arab.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/arab2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/arabi.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/arabic.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/armenian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/australian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/austrian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/bahasa.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/bahasai.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/bahasam.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/bangla.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/basque.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/bengali.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/bicig.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/bicig2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/bicig3.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/bithe.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/boldsc.sty
%{_texdir}/texmf-dist/tex/latex/minitoc/brazil.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/brazilian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/breton.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/british.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/bulgarian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/bulgarianb.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/buryat.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/buryat2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/canadian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/canadien.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/castillan.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/castillian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/catalan.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/chinese1.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/chinese1.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/chinese2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/chinese2.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/croatian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/czech.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/danish.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/dblaccnt.sty
%{_texdir}/texmf-dist/tex/latex/minitoc/devanagari.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/dutch.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/english.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/english1.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/english2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/esperant.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/esperanto.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/estonian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/ethiopia.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/ethiopian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/ethiopian2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/farsi1.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/farsi1.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/farsi2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/farsi2.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/farsi3.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/finnish.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/finnish2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/franc.sty
%{_texdir}/texmf-dist/tex/latex/minitoc/francais.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/frbib.sty
%{_texdir}/texmf-dist/tex/latex/minitoc/french.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/french1.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/french2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/frenchb.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/frenchle.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/frenchpro.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/frnew.sty
%{_texdir}/texmf-dist/tex/latex/minitoc/galician.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/german.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/germanb.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/germanb2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/greek-mono.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/greek-polydemo.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/greek-polykatha.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/greek.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/guarani.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/hangul-u8.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/hangul-u8.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/hangul1.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/hangul1.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/hangul2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/hangul2.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/hangul3.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/hangul3.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/hangul4.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/hangul4.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/hanja-u8.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/hanja-u8.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/hanja1.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/hanja1.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/hanja2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/hanja2.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/hebrew.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/hebrew2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/hindi-modern.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/hindi.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/hungarian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/icelandic.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/indon.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/indonesian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/interlingua.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/irish.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/italian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/italian2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/japanese.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/japanese.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/japanese2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/japanese2.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/japanese3.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/japanese3.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/japanese4.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/japanese4.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/japanese5.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/japanese5.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/japanese6.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/japanese6.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/kannada.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/khalkha.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/latin.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/latin2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/latinc.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/latinc2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/latvian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/latvian2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/letton.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/letton2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/lithuanian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/lithuanian2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/lowersorbian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/lsorbian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/magyar.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/magyar2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/magyar3.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/malay.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/malayalam-b.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/malayalam-keli.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/malayalam-keli2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/malayalam-mr.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/malayalam-omega.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/malayalam-omega.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/malayalam-rachana.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/malayalam-rachana2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/malayalam-rachana3.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/manju.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/mexican.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/meyalu.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/minitoc.sty
%{_texdir}/texmf-dist/tex/latex/minitoc/mongol.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/mongolb.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/mongolian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/mtcmess.sty
%{_texdir}/texmf-dist/tex/latex/minitoc/mtcoff.sty
%{_texdir}/texmf-dist/tex/latex/minitoc/mtcpatchmem.sty
%{_texdir}/texmf-dist/tex/latex/minitoc/mypatches.sty
%{_texdir}/texmf-dist/tex/latex/minitoc/naustrian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/newzealand.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/ngerman.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/ngermanb.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/ngermanb2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/norsk.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/norsk2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/nynorsk.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/nynorsk2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/occitan.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/occitan2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/polish.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/polish2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/polski.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/portuges.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/portuguese.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/romanian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/romanian2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/romanian3.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/russian-cca.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/russian-cca.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/russian-cca1.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/russian-cca1.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/russian-lh.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/russian-lh.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/russian-lhcyralt.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/russian-lhcyralt.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/russian-lhcyrkoi.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/russian-lhcyrkoi.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/russian-lhcyrwin.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/russian-lhcyrwin.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/russian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/russian2m.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/russian2o.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/russianb.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/russianc.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/samin.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/scottish.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/serbian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/serbianc.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/slovak.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/slovene.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/spanish.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/spanish2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/spanish3.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/spanish4.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/swahili.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/swedish.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/swedish2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/thai.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/thai.mlo
%{_texdir}/texmf-dist/tex/latex/minitoc/turkish.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/uighur.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/uighur2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/uighur3.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/ukraineb.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/ukrainian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/uppersorbian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/usorbian.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/vietnam.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/vietnamese.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/welsh.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/xalx.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/xalx2.mld
%{_texdir}/texmf-dist/tex/latex/minitoc/xalx3.mld

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/minitoc/CATALOG
%{_texdir}/texmf-dist/doc/latex/minitoc/INSTALL
%{_texdir}/texmf-dist/doc/latex/minitoc/README
%{_texdir}/texmf-dist/doc/latex/minitoc/TODO
%{_texdir}/texmf-dist/doc/latex/minitoc/aaland-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/acadian-m.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/acadie-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/acadien-m.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/afghan-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/africa-lf.png
%{_texdir}/texmf-dist/doc/latex/minitoc/africa-lo.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/afrsud-l.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/afrsud-p.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/alb2.png
%{_texdir}/texmf-dist/doc/latex/minitoc/alba-eth.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/albania-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/albania.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/algeria-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/allemand.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/alsace-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/andorra-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/anglo1.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/angola-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/arab-l.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/arabw.png
%{_texdir}/texmf-dist/doc/latex/minitoc/argentina-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/armenia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/armeniad.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/armenian-l.png
%{_texdir}/texmf-dist/doc/latex/minitoc/armeniar.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/aruba-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/australia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/austria-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/azerbaijan-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/bahamas-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/bahrain-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/baltes.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/bangla.png
%{_texdir}/texmf-dist/doc/latex/minitoc/bangla1.png
%{_texdir}/texmf-dist/doc/latex/minitoc/bangla2.png
%{_texdir}/texmf-dist/doc/latex/minitoc/bangladesh-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/barbados-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/basque-de.png
%{_texdir}/texmf-dist/doc/latex/minitoc/basque-df.png
%{_texdir}/texmf-dist/doc/latex/minitoc/basque1.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/basque2.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/be-dg-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/belarus-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/belgique.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/belgium-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/belize-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/bengali-m.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/benin-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/bolivia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/bolzano-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/bosnia-hz-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/bosnia.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/bozen-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/brazil-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/brazil.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/brazilp.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/bretagne.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/brussels-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/bulgaria-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/bulgariar.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/bulgarski.png
%{_texdir}/texmf-dist/doc/latex/minitoc/bulgmap.png
%{_texdir}/texmf-dist/doc/latex/minitoc/bur-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/burkina-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/burundi-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/buryatia-l.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/buryatia.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/california-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/cambodia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/cameroon-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/canada-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/canada-l.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/canada-pe.png
%{_texdir}/texmf-dist/doc/latex/minitoc/canada-pf.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/canada.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/canada1.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/cap-verde-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/castille-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/catalan-d.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/catalan-p.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/catalonia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/caucasus.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/central-africa-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/chad-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/chile-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/china-ae.png
%{_texdir}/texmf-dist/doc/latex/minitoc/china-af.png
%{_texdir}/texmf-dist/doc/latex/minitoc/china-ch.png
%{_texdir}/texmf-dist/doc/latex/minitoc/china-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/china-l.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/china-w.png
%{_texdir}/texmf-dist/doc/latex/minitoc/chine1.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/chine2.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/cis-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/cmk
%{_texdir}/texmf-dist/doc/latex/minitoc/colombia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/comoros-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/congo-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/corsica-f.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/costa-rica-f.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/cplp-0.png
%{_texdir}/texmf-dist/doc/latex/minitoc/cplpmap.png
%{_texdir}/texmf-dist/doc/latex/minitoc/croatia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/croatia-un.png
%{_texdir}/texmf-dist/doc/latex/minitoc/croatie2.png
%{_texdir}/texmf-dist/doc/latex/minitoc/cuba-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/cyprus-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/cyr-alf.png
%{_texdir}/texmf-dist/doc/latex/minitoc/cz1.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/cz3.png
%{_texdir}/texmf-dist/doc/latex/minitoc/czech-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/czechd.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/dane-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/danemark.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/danishd.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/danishg.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/devanagari.png
%{_texdir}/texmf-dist/doc/latex/minitoc/djibouti-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/dominica-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/dominican-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/dutchw.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/east-timor-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/ecosse1.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/ecosse2.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/ecosse3.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/ecuador-f.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/egypt-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/el-salvador-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/emk
%{_texdir}/texmf-dist/doc/latex/minitoc/england-f.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/equa-guinea-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/eritrea-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/espa-l.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/espa-o.png
%{_texdir}/texmf-dist/doc/latex/minitoc/esperanto-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/estonia-a.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/estonia-b.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/estonia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/eth2.png
%{_texdir}/texmf-dist/doc/latex/minitoc/ethiolang.png
%{_texdir}/texmf-dist/doc/latex/minitoc/ethiopia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/ethiopia-p.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/ethiopia.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/euro-lan.png
%{_texdir}/texmf-dist/doc/latex/minitoc/euro-lan1.png
%{_texdir}/texmf-dist/doc/latex/minitoc/euro-lan2.png
%{_texdir}/texmf-dist/doc/latex/minitoc/eusk-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/euskara.png
%{_texdir}/texmf-dist/doc/latex/minitoc/faroe-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/farsi-logo.png
%{_texdir}/texmf-dist/doc/latex/minitoc/farsi.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/feroe.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/fiji-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/finland-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/finlande1.png
%{_texdir}/texmf-dist/doc/latex/minitoc/finlande2.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/finnishd.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/finnishl.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/flanders-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/fmk
%{_texdir}/texmf-dist/doc/latex/minitoc/france-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/france-lr.png
%{_texdir}/texmf-dist/doc/latex/minitoc/franco.png
%{_texdir}/texmf-dist/doc/latex/minitoc/francophonie-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/fswahili.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/gabon-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/gael-ft.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/gaid.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/galicia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/galicia-m.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/galicia-mp.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/galician-l.png
%{_texdir}/texmf-dist/doc/latex/minitoc/galles1.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/galles2.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/georgia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/germ-w.png
%{_texdir}/texmf-dist/doc/latex/minitoc/german-c.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/german-d.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/german-m.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/germany-f.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/ghana-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/gibraltar-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/grece1.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/grece2.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/greece-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/greeka.png
%{_texdir}/texmf-dist/doc/latex/minitoc/greekm.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/greenland-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/guatemala-f.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/guinea-bissau-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/guinea-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/gwenn-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/haiti-f.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/hangul.png
%{_texdir}/texmf-dist/doc/latex/minitoc/hanja.png
%{_texdir}/texmf-dist/doc/latex/minitoc/hanzi.png
%{_texdir}/texmf-dist/doc/latex/minitoc/hin.png
%{_texdir}/texmf-dist/doc/latex/minitoc/hindi-b.png
%{_texdir}/texmf-dist/doc/latex/minitoc/hindi-p.png
%{_texdir}/texmf-dist/doc/latex/minitoc/hispano.png
%{_texdir}/texmf-dist/doc/latex/minitoc/honduras-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/hrv.png
%{_texdir}/texmf-dist/doc/latex/minitoc/hun1.png
%{_texdir}/texmf-dist/doc/latex/minitoc/hun2.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/hungary-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/iceland-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/imk
%{_texdir}/texmf-dist/doc/latex/minitoc/imongolia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/inde1.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/inde2.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/india-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/indonesia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/indonesia1.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/indonesia2.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/iran-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/iranian.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/iraq-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/ireland-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/irish.png
%{_texdir}/texmf-dist/doc/latex/minitoc/irlande.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/islam-pbc.png
%{_texdir}/texmf-dist/doc/latex/minitoc/islam-sw.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/islande.png
%{_texdir}/texmf-dist/doc/latex/minitoc/islandep.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/isr1.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/isr2.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/israel-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/italian.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/italo1.png
%{_texdir}/texmf-dist/doc/latex/minitoc/italy-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/italysm.png
%{_texdir}/texmf-dist/doc/latex/minitoc/ivory-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/ivrit.png
%{_texdir}/texmf-dist/doc/latex/minitoc/jamaica-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/japan-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/japon1.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/japon2.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/jordan-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/jutland-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/kannada-n.png
%{_texdir}/texmf-dist/doc/latex/minitoc/karnad1.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/karnataka-f.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/karnataka.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/kazakhstan-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/kenya-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/kerala-f.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/kerala.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/khalkha.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/kiribati-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/korea-n-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/korea-s-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/korean1.png
%{_texdir}/texmf-dist/doc/latex/minitoc/korean2.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/kos-alb.png
%{_texdir}/texmf-dist/doc/latex/minitoc/kos-ml.png
%{_texdir}/texmf-dist/doc/latex/minitoc/kosovo-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/kuwait-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/kyrgyzstan-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/lamed3.png
%{_texdir}/texmf-dist/doc/latex/minitoc/lang-g.png
%{_texdir}/texmf-dist/doc/latex/minitoc/laos-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/latvia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/latvian-d.png
%{_texdir}/texmf-dist/doc/latex/minitoc/latvian-r1.png
%{_texdir}/texmf-dist/doc/latex/minitoc/lebanon-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/lettonie.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/leur.png
%{_texdir}/texmf-dist/doc/latex/minitoc/liberia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/libya-f.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/liech-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/lithuania-f.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/lituanie.png
%{_texdir}/texmf-dist/doc/latex/minitoc/lorraine-f.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/louisiana-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/ls-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/luso1.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/luso2.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/lux-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/macau-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/macedonia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/madagascar-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/maine-f.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/malawi-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/malayalam.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/malayalam.png
%{_texdir}/texmf-dist/doc/latex/minitoc/malaysia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/malaysia1.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/malaysia2.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mali-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/malta1-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/manchu.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/manchuria.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/manjuc.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/manjui.png
%{_texdir}/texmf-dist/doc/latex/minitoc/mauritania-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/mauritius-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/mex1.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mex2.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mex3.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mexico-f.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/mexip.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/meyalu.png
%{_texdir}/texmf-dist/doc/latex/minitoc/minitoc-fr.bib
%{_texdir}/texmf-dist/doc/latex/minitoc/minitoc-fr.lan
%{_texdir}/texmf-dist/doc/latex/minitoc/minitoc-fr.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/minitoc.bib
%{_texdir}/texmf-dist/doc/latex/minitoc/minitoc.bug
%{_texdir}/texmf-dist/doc/latex/minitoc/minitoc.l
%{_texdir}/texmf-dist/doc/latex/minitoc/minitoc.lan
%{_texdir}/texmf-dist/doc/latex/minitoc/minitoc.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/minitoc.pre
%{_texdir}/texmf-dist/doc/latex/minitoc/minitoc.sum
%{_texdir}/texmf-dist/doc/latex/minitoc/moldova-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/monaco-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/mondep.png
%{_texdir}/texmf-dist/doc/latex/minitoc/mongasie.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mongolcy.png
%{_texdir}/texmf-dist/doc/latex/minitoc/mongolia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/mongolian.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mongols.png
%{_texdir}/texmf-dist/doc/latex/minitoc/mongoltr.png
%{_texdir}/texmf-dist/doc/latex/minitoc/montenegro-f.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/morocco-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/mozambique-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-2c.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-2c.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-2nd.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-2nd.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-3co.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-3co.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-add.bib
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-add.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-add.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-ads.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-ads.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-amm.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-amm.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-apx.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-apx.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-art.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-art.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-bk.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-bk.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-bo.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-bo.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-ch0.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-ch0.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-cri.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-cri.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-fko.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-fko.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-fo1.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-fo1.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-fo2.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-fo2.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-gap.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-gap.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-hi1.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-hi1.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-hi2.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-hi2.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-hia.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-hia.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-hir.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-hir.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-hop.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-hop.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-liv.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-liv.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-mem.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-mem.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-mm1.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-mm1.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-mu.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-mu.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-nom.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-nom.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-ocf.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-ocf.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-ofs.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-ofs.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-sbf.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-sbf.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-scr.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-scr.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-syn.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-syn.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-tbi.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-tbi.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-tlc.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-tlc.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-tlo.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-tlo.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-tsf.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-tsf.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-vti.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/mtc-vti.tex
%{_texdir}/texmf-dist/doc/latex/minitoc/namibia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/nbrunswick-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/ncyprus-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/neder.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/netherlands-antilles-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/netherlands-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/new-york-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/newzealand-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/nicaragua-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/nice-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/niger-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/nigeria-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/nihongo.png
%{_texdir}/texmf-dist/doc/latex/minitoc/norvege-c.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/norvege-t.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/norway-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/norway-p.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/occ-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/occdial1.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/occdial2.png
%{_texdir}/texmf-dist/doc/latex/minitoc/occitanie.png
%{_texdir}/texmf-dist/doc/latex/minitoc/occtaur.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/oman-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/opole-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/pakistan-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/palestine-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/panama-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/paraguay-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/paraguay.png
%{_texdir}/texmf-dist/doc/latex/minitoc/paraguayp.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/peru-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/philippines-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/pmk
%{_texdir}/texmf-dist/doc/latex/minitoc/poland-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/polish-d.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/polmin.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/pologne.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/polski-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/portu-a.png
%{_texdir}/texmf-dist/doc/latex/minitoc/portu-b.png
%{_texdir}/texmf-dist/doc/latex/minitoc/portu-p.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/portu-r.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/portugal-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/portugal.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/puerto-rico-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/qatar-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/quebec-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/rdcongo-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/rmk
%{_texdir}/texmf-dist/doc/latex/minitoc/romania-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/romanian.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/rus-cyr.png
%{_texdir}/texmf-dist/doc/latex/minitoc/rus-re.png
%{_texdir}/texmf-dist/doc/latex/minitoc/rus-su.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/russia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/russian-e.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/russian-n.png
%{_texdir}/texmf-dist/doc/latex/minitoc/russian-w.png
%{_texdir}/texmf-dist/doc/latex/minitoc/russian.png
%{_texdir}/texmf-dist/doc/latex/minitoc/rwanda-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/saint-lucia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/same-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/same.png
%{_texdir}/texmf-dist/doc/latex/minitoc/sami-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/samoa-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/san-marino-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/sao-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/saudi-arabia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/scotland-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/senegal-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/serb-a.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/serbia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/serbia-f2.png
%{_texdir}/texmf-dist/doc/latex/minitoc/serbia1.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/seychelles-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/singapore-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/slovak-ok.png
%{_texdir}/texmf-dist/doc/latex/minitoc/slovakia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/slovakia.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/slovenia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/slovenian.png
%{_texdir}/texmf-dist/doc/latex/minitoc/slovenie.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/solomon-islands-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/somalia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/sorabe-1.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/sorabe-2.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/sorben.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/sorbian.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/south-africa-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/spain-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/spain.png
%{_texdir}/texmf-dist/doc/latex/minitoc/spilhennig.png
%{_texdir}/texmf-dist/doc/latex/minitoc/start.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/stop.png
%{_texdir}/texmf-dist/doc/latex/minitoc/sudan-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/suede-a.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/suede-fin.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/suisse-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/suriname-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/svenska.png
%{_texdir}/texmf-dist/doc/latex/minitoc/swahili-m.png
%{_texdir}/texmf-dist/doc/latex/minitoc/swahili.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/sweden-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/sweden.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/syria-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/taiwan-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/tajikistan-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/tanzania-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/thai.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/thai.png
%{_texdir}/texmf-dist/doc/latex/minitoc/thailand-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/tmk
%{_texdir}/texmf-dist/doc/latex/minitoc/togo-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/tonga-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/tunisia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/turkey-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/turkish.png
%{_texdir}/texmf-dist/doc/latex/minitoc/turkmenistan-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/turquie.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/tuvalu-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/uae-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/uganda-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/uighur-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/uighur.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/uk-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/ukra.png
%{_texdir}/texmf-dist/doc/latex/minitoc/ukraine-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/ukraine.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/ukrainep.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/uruguay-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/us-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/usa-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/uzbekistan-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/vanuatu-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/vatican-f.jpg
%{_texdir}/texmf-dist/doc/latex/minitoc/venezuela-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/vermont-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/viet-w.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/viet2.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/viet3.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/viet4.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/vietnam-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/vojvodina-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/wales-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/wallonia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/wallonie.pdf
%{_texdir}/texmf-dist/doc/latex/minitoc/wiki.png
%{_texdir}/texmf-dist/doc/latex/minitoc/wikif.png
%{_texdir}/texmf-dist/doc/latex/minitoc/wrs-a.png
%{_texdir}/texmf-dist/doc/latex/minitoc/wrs-c.png
%{_texdir}/texmf-dist/doc/latex/minitoc/xinjiang.png
%{_texdir}/texmf-dist/doc/latex/minitoc/xinjiangc.png
%{_texdir}/texmf-dist/doc/latex/minitoc/xmk
%{_texdir}/texmf-dist/doc/latex/minitoc/xyugo.png
%{_texdir}/texmf-dist/doc/latex/minitoc/yemen-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/zambia-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/zanzibar-f.png
%{_texdir}/texmf-dist/doc/latex/minitoc/zimbabwe-f.png


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
