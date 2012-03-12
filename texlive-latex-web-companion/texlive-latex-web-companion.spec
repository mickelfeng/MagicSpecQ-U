%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/latex-web-companion.doc.tar.xz

Name: texlive-latex-web-companion-doc
License: LPPL
Summary: Documentation for latex-web-companion
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description
Documentation for latex-web-companion


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

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apa/README.apa
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apa/latexexa-raw.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apa/latexexa.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apa/latexexa.ltx
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apa/latexexa.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apa/latexexa.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apa/phys332-1.eps
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apa/phys332-2.eps
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apa/teched.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apa/teched.java
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apb/InvitationSAX.class
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apb/InvitationSAX.java
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apb/MySAXApp.class
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apb/MySAXApp.java
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apb/README.apb
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apb/bibliotest1.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apb/bibliotest2.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apb/biblioxml1.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apb/biblioxml2.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apb/colorcir.eps
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apb/inv2.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apb/invitation.sty
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apb/invitation2.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apb/invitation2.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apb/latexmath.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apb/latexmml.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apb/minilatex.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apb/minilatex.xsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apb/minilatexexa.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apb/minilatexexa.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apb/mybiblio.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apb/utf82latin1.sh
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apc/ISOcyr1.pen
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apc/README.apc
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apc/invitation.sty
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apc/invitationfr.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apc/invitationfr.sty
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apc/invitationfr.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apc/invitationfr.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apc/invlat1fr.xsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apc/utf8.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apc/utf8.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apc/utf8.xsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apc/utf8tei.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/Makefile
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/Makefile.ex2
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/Makefile.ex3
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/README.ch3
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/colorcir.eps
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex20.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex21.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex22.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex2bib.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex30.dvi
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex30.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex31.ptr
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex31.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex32.ptr
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex32.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex3bib.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/l2hexa.dvi
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/l2hexa.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/myinit.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS.css
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS.dvi
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath.dvi
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathImages.dvi
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathImages.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathThumb.dvi
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathThumb.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/tac2dim.eps
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex30/contents.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex30/ex30.css
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex30/ex30.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex30/index.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex30/index.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex30/internals.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex30/labels.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex30/sections.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex31/Timg1.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex31/WARNINGS
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex31/contents.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex31/ex31.css
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex31/ex31.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex31/figure.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex31/images.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex31/images.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex31/img1.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex31/index.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex31/internals.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex31/labels.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex31/sections.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex32/contents.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex32/ex32.css
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex32/ex32.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex32/index.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex32/internals.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex32/labels.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex32/sections.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex32/table.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/l2hexa/images.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/l2hexa/images.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/l2hexa/img1.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/l2hexa/img2.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/l2hexa/index.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/l2hexa/internals.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/l2hexa/l2hexa.css
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/l2hexa/l2hexa.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/l2hexa/labels.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/l2hexa/node1.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/l2hexa/node2.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/l2hexa/node3.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/l2hexa/node4.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/l2hexa/node5.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/l2hexa/node6.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/l2hexa/node7.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/l2hexa/node8.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/WARNINGS
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/images.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/images.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/img1.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/img10.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/img11.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/img12.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/img13.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/img14.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/img15.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/img16.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/img17.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/img18.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/img19.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/img2.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/img20.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/img21.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/img3.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/img4.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/img5.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/img6.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/img7.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/img8.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/img9.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/index.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/internals.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/labels.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/node1.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/sampleAMS.css
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS/sampleAMS.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/WARNINGS
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/images.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/images.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/img1.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/img10.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/img11.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/img12.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/img13.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/img14.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/img15.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/img16.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/img17.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/img18.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/img19.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/img2.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/img20.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/img3.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/img4.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/img5.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/img6.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/img7.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/img8.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/img9.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/index.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/internals.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/labels.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/node1.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/sampleMath.css
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath/sampleMath.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathImages/WARNINGS
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathImages/images.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathImages/images.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathImages/img1.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathImages/img2.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathImages/img3.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathImages/img4.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathImages/img5.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathImages/img6.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathImages/img7.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathImages/img8.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathImages/img9.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathImages/index.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathImages/internals.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathImages/labels.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathImages/node1.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathImages/sampleMathImages.css
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathImages/sampleMathImages.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/Timg8.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/Timg9.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/WARNINGS
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/images.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/images.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/img1.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/img2.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/img3.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/img4.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/img5.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/img6.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/img7.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/img8.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/img9.gif
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/index.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/internals.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/labels.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/node1.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/sampleMathThumb.css
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathThumb/sampleMathThumb.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/intro/lwc.eepic
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/intro/lwc.fig
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2html/Makefile.ex2
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2html/Makefile.ex3
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2html/README.ch3
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2html/colorcir.eps
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2html/ex20.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2html/ex21.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2html/ex22.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2html/ex2bib.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2html/ex30.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2html/ex31.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2html/ex32.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2html/ex3bib.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2html/l2hexa.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2html/myinit.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2html/sampleAMS.css
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2html/sampleAMS.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2html/sampleMath.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2html/sampleMathImages.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2html/sampleMathThumb.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2html/tac2dim.eps
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/amaya.mml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/isoamsae.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/isoamsbe.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/isoamsce.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/isoamsne.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/isoamsoe.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/isoamsre.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/isogrk3e.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/isomfrke.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/isomopfe.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/isomscre.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/isonume.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/isoteche.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/l2xdemo.cfg
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/l2xdemo.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/l2xdemo.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/l2xmath.cfg
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/mathml.dsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/mathml.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/mathmltools.dsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/mathmlx.dsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/mmaliase.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/mmlent.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/mtdemo.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/stix.mml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/techexpl.mml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/test.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/test.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/tmp.tmp
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/try.cfg
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/try2.cfg
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/try3.cfg
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/try4.cfg
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/try5.cfg
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/webeq.mml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml/xml.dcl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xml/README.ch6
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xml/catalog
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xml/emptyexample.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xml/invitation.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xml/invitation.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xml/wrong.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xml/xml.dcl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/README.ch7
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/SGMLS.pm
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/catalog
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/catalog.dsssl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/catalog.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/dsssl.cat
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/dsssl.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/empty.dsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/empty.xsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/emptyexample.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/entable-alt.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/entable.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/fot.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/frisotab1exa1.xsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/frisotab1exa2.xsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/inv1html.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/inv2css.html.save
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/inv2html.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/inv2lat.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/inv3.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/invcss.html.save
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/invfo1.fo
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/invfo1.xsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/invfop.pdf
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/invhtml.dsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/invhtml2.xsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/invit.css
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/invitation.dsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/invitation.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/invitation.out
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/invitation.sty
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/invitation.tex.save
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/invitation.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/invitation1.tex
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/invitation2.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/invitation2.html
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/invitation2.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/invitationfr.sty
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/invlat1.xsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/invtab1.dsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/invtab2.dsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/isotab1to2-bis.xsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/isotab1to2.xsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/isotabexa1.xsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/isotabexa2.xsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/sectionexa.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/sectionexa.xsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/sgmlspl.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/skel.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/style-sheet.dtd
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/templatest.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/templatest.xsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/templatestnok.xsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/templatestok.xsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/test-SGMLS.pl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/writefiles.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/wrong.xml
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/xml.dcl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/xslexa1.xsl
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/SGMLS/Output.pm
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/SGMLS/Refs.pm
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/SGMLS/SGMLS.pm


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
