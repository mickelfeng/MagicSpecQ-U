%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/koma-script.tar.xz

Name: texlive-koma-script
License: LPPL
Summary: A bundle of versatile classes and packages
Version: %{tl_version}
Release: %{tl_noarch_release}.3.06.svn19027%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(scrguide.sty)
Provides: tex(scraddr.sty)
Provides: tex(scrartcl.sty)
Provides: tex(scrbase.sty)
Provides: tex(scrbook.sty)
Provides: tex(scrdate.sty)
Provides: tex(scrdoc.sty)
Provides: tex(scrextend.sty)
Provides: tex(scrhack.sty)
Provides: tex(scrjura.sty)
Provides: tex(scrkbase.sty)
Provides: tex(scrlettr.sty)
Provides: tex(scrlfile.sty)
Provides: tex(scrlttr2.sty)
Provides: tex(scrpage.sty)
Provides: tex(scrpage2.sty)
Provides: tex(scrreprt.sty)
Provides: tex(scrtime.sty)
Provides: tex(tocbasic.sty)
Provides: tex(tocstyle.sty)
Provides: tex(typearea.sty)
Requires: tex(inputenc.sty)
Requires: tex(fontenc.sty)
Requires: tex(babelbib.sty)
Requires: tex(afterpage.sty)
Requires: tex(makeidx.sty)
Requires: tex(graphicx.sty)
Requires: tex(booktabs.sty)
Requires: tex(longtable.sty)
Requires: tex(amsmath.sty)
Requires: tex(listings.sty)
Requires: tex(multicol.sty)
Requires: tex(marginnote.sty)
Requires: tex(xcolor.sty)
Requires: tex(hyperref.sty)
Requires: tex(bookmark.sty)
Requires: tex(geometry.sty)
Requires: tex(textcomp.sty)
Requires: tex(keyval.sty)

%description
The KOMA-Script bundle provides drop-in replacements for the
article/report/book classes with emphasis on typography and
versatility. There is also a letter class, different from all
other letter classes. It also offers e.g. a package for
calculated type areas in the way laid down by the typographer
Jan Tschichold, a package for easily changing and defining of
page styles, a package for getting not only the current date
but also the name of day and a package for getting current
time. All these packages may be used not only with KOMA-Script
classes but also with standard classes. Since every package has
its own version number, the number below is only the version of
scrbook, scrreprt, scrartcl, scrlttr2 and typearea. These are
the main parts of the bundle.

date: 2010-06-17 12:10:47 +0200

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


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/lppl.txt lppl.txt
xz -dc %{SOURCE0} | tar x -C %{buildroot}%{_texdir}/texmf-dist
# nuke useless tlmgr packaging stuff and doc droppings
rm -rf %{buildroot}%{_texdir}/tlpkg/tlpobj/
rm -rf %{buildroot}%{_texdir}/texmf-dist/tlpkg/tlpobj/
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/man*/*.pdf
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/Makefile
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/man*/Makefile
rm -rf %{buildroot}%{_texdir}/texmf/doc/info/dir
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/ChangeLog
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/ChangeLog.2
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/Makefile
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/Makefile.baseinit
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/Makefile.baserules
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/japanlco.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scraddr.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scraddr.ins
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrbeta.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrdoc.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrextend.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrhack.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrjura.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrkbase.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrkbib.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrkcile.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrkcomp.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrkfloa.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrkfont.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrkftn.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrkidx.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrklang.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrklco.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrkliof.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrklist.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrkmisc.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrknpap.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrkpage.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrkpar.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrkplen.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrksect.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrktare.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrktitl.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrkvars.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrkvers.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrlettr.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrlettr.ins
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrlfile.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrlfile.ins
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrlogo.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrmain.ins
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrpage.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrpage.ins
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrsource.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrstrip.inc
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrstrop.inc
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/scrtime.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/tocbasic.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/tocstyle.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/Makefile
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/Makefile.guide
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/Makefile.latexinit
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/guide.bib
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/guide.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/koma-script.html
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/komascr.html
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/komascript.html
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/plength.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/scraddr.html
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/scrartcl.html
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/scrbook.html
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/scrdate.html
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/scrguide.cls
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/scrguide.gst
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/scrguide.html
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/scrguide.ist
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/scrguide.pdf
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/scrguien.html
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/scrguien.pdf
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/scrlfile.html
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/scrlttr2.html
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/scrpage2.html
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/scrreprt.html
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/scrtime.html
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/typearea.html
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/bin/genhtmlidx.pl
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/bin/genindex.pl
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/Makefile
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/adrconvnote.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/common-0.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/common-1.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/common-10.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/common-11.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/common-12.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/common-13.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/common-14.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/common-15.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/common-2.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/common-3.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/common-4.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/common-5.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/common-6.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/common-7.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/common-8.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/common-9.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/guide-english.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/htmlsetup
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/introduction.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/japanlco.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/scraddr.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/scrbookreportarticle.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/scrdatetime.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/scrlfile.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/scrlttr2.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/scrpage2.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/tocbasic.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/typearea.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/Makefile
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/Makefile.guide
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/adrconvnote.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/authorpart.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/common-0.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/common-1.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/common-10.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/common-11.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/common-12.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/common-13.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/common-14.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/common-15.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/common-2.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/common-3.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/common-4.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/common-5.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/common-6.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/common-7.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/common-8.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/common-9.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/expertpart.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/guide-ngerman.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/guide.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/htmlsetup
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/introduction.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/labelbasic.lco
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/linkalias.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/preface.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/scraddr.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/scrbase.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/scrbookreportarticle-experts.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/scrbookreportarticle.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/scrdatetime.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/scrextend.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/scrlfile.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/scrlttr2-experts.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/scrlttr2.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/scrlttr2examples.dtx
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/scrpage2.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/settleford600label.lco
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/tocbasic.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/typearea-experts.tex
rm -f %{buildroot}/%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/typearea.tex

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/koma-script/INSTALL.txt
%{_texdir}/texmf-dist/doc/latex/koma-script/INSTALLD.txt
%{_texdir}/texmf-dist/doc/latex/koma-script/README
%{_texdir}/texmf-dist/doc/latex/koma-script/koma-script.html
%{_texdir}/texmf-dist/doc/latex/koma-script/komabug.tex
%{_texdir}/texmf-dist/doc/latex/koma-script/komascr.html
%{_texdir}/texmf-dist/doc/latex/koma-script/komascript.html
%{_texdir}/texmf-dist/doc/latex/koma-script/lppl-de.txt
%{_texdir}/texmf-dist/doc/latex/koma-script/lppl.txt
%{_texdir}/texmf-dist/doc/latex/koma-script/manifest.txt
%{_texdir}/texmf-dist/doc/latex/koma-script/scraddr.html
%{_texdir}/texmf-dist/doc/latex/koma-script/scrartcl.html
%{_texdir}/texmf-dist/doc/latex/koma-script/scrbook.html
%{_texdir}/texmf-dist/doc/latex/koma-script/scrdate.html
%{_texdir}/texmf-dist/doc/latex/koma-script/scrguide.html
%{_texdir}/texmf-dist/doc/latex/koma-script/scrguide.pdf
%{_texdir}/texmf-dist/doc/latex/koma-script/scrguien.html
%{_texdir}/texmf-dist/doc/latex/koma-script/scrguien.pdf
%{_texdir}/texmf-dist/doc/latex/koma-script/scrhack.pdf
%{_texdir}/texmf-dist/doc/latex/koma-script/scrjura.pdf
%{_texdir}/texmf-dist/doc/latex/koma-script/scrlfile.html
%{_texdir}/texmf-dist/doc/latex/koma-script/scrlttr2.html
%{_texdir}/texmf-dist/doc/latex/koma-script/scrpage2.html
%{_texdir}/texmf-dist/doc/latex/koma-script/scrreprt.html
%{_texdir}/texmf-dist/doc/latex/koma-script/scrtime.html
%{_texdir}/texmf-dist/doc/latex/koma-script/tocstyle.pdf
%{_texdir}/texmf-dist/doc/latex/koma-script/typearea.html
%{_texdir}/texmf-dist/tex/latex/koma-script/DIN.lco
%{_texdir}/texmf-dist/tex/latex/koma-script/DINmtext.lco
%{_texdir}/texmf-dist/tex/latex/koma-script/KOMAold.lco
%{_texdir}/texmf-dist/tex/latex/koma-script/KakuLL.lco
%{_texdir}/texmf-dist/tex/latex/koma-script/NF.lco
%{_texdir}/texmf-dist/tex/latex/koma-script/NipponEH.lco
%{_texdir}/texmf-dist/tex/latex/koma-script/NipponEL.lco
%{_texdir}/texmf-dist/tex/latex/koma-script/NipponLH.lco
%{_texdir}/texmf-dist/tex/latex/koma-script/NipponLL.lco
%{_texdir}/texmf-dist/tex/latex/koma-script/NipponRL.lco
%{_texdir}/texmf-dist/tex/latex/koma-script/SN.lco
%{_texdir}/texmf-dist/tex/latex/koma-script/SNleft.lco
%{_texdir}/texmf-dist/tex/latex/koma-script/UScommercial9.lco
%{_texdir}/texmf-dist/tex/latex/koma-script/UScommercial9DW.lco
%{_texdir}/texmf-dist/tex/latex/koma-script/float.hak
%{_texdir}/texmf-dist/tex/latex/koma-script/hyperref.hak
%{_texdir}/texmf-dist/tex/latex/koma-script/listings.hak
%{_texdir}/texmf-dist/tex/latex/koma-script/scraddr.sty
%{_texdir}/texmf-dist/tex/latex/koma-script/scrartcl.cls
%{_texdir}/texmf-dist/tex/latex/koma-script/scrbase.sty
%{_texdir}/texmf-dist/tex/latex/koma-script/scrbook.cls
%{_texdir}/texmf-dist/tex/latex/koma-script/scrdate.sty
%{_texdir}/texmf-dist/tex/latex/koma-script/scrdoc.cls
%{_texdir}/texmf-dist/tex/latex/koma-script/scrextend.sty
%{_texdir}/texmf-dist/tex/latex/koma-script/scrhack.sty
%{_texdir}/texmf-dist/tex/latex/koma-script/scrjura.sty
%{_texdir}/texmf-dist/tex/latex/koma-script/scrkbase.sty
%{_texdir}/texmf-dist/tex/latex/koma-script/scrlettr.cls
%{_texdir}/texmf-dist/tex/latex/koma-script/scrlfile.sty
%{_texdir}/texmf-dist/tex/latex/koma-script/scrlttr2.cls
%{_texdir}/texmf-dist/tex/latex/koma-script/scrpage.sty
%{_texdir}/texmf-dist/tex/latex/koma-script/scrpage2.sty
%{_texdir}/texmf-dist/tex/latex/koma-script/scrreprt.cls
%{_texdir}/texmf-dist/tex/latex/koma-script/scrsize10pt.clo
%{_texdir}/texmf-dist/tex/latex/koma-script/scrsize11pt.clo
%{_texdir}/texmf-dist/tex/latex/koma-script/scrsize12pt.clo
%{_texdir}/texmf-dist/tex/latex/koma-script/scrtime.sty
%{_texdir}/texmf-dist/tex/latex/koma-script/tocbasic.sty
%{_texdir}/texmf-dist/tex/latex/koma-script/tocstyle.sty
%{_texdir}/texmf-dist/tex/latex/koma-script/typearea.sty
%{_texdir}/texmf-dist/tex/latex/koma-script/visualize.lco
%{_texdir}/texmf-dist/doc/latex/koma-script/scrbase.html
%{_texdir}/texmf-dist/doc/latex/koma-script/scrwfile.html
%{_texdir}/texmf-dist/doc/latex/koma-script/tocbasic.html
%{_texdir}/texmf-dist/source/latex/koma-script/doc/english/scrwfile.tex
%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/scrhack.tex
%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman/scrwfile.tex
%{_texdir}/texmf-dist/source/latex/koma-script/scrwfile.dtx
%{_texdir}/texmf-dist/tex/latex/koma-script/floatrow.hak
%{_texdir}/texmf-dist/tex/latex/koma-script/scrfontsizes.sty
%{_texdir}/texmf-dist/tex/latex/koma-script/scrwfile.sty


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
