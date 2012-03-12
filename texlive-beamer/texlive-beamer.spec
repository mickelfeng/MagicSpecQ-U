%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/beamer.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/beamer.doc.tar.xz

Name: texlive-beamer
License: GPL+
Summary: A LaTeX class for producing presentations and slides
Version: %{tl_version}
Release: %{tl_noarch_release}.3.10.svn19443%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-pgf = %{tl_version}
Requires: texlive-xcolor = %{tl_version}
Provides: tex(beamer.sty)
Provides: tex(beamerarticle.sty)
Provides: tex(beamerbasearticle.sty)
Provides: tex(beamerbaseauxtemplates.sty)
Provides: tex(beamerbaseboxes.sty)
Provides: tex(beamerbasecolor.sty)
Provides: tex(beamerbasecompatibility.sty)
Provides: tex(beamerbasedecode.sty)
Provides: tex(beamerbaseexercise.sty)
Provides: tex(beamerbasefont.sty)
Provides: tex(beamerbaseframe.sty)
Provides: tex(beamerbaseframecomponents.sty)
Provides: tex(beamerbaseframesize.sty)
Provides: tex(beamerbaselocalstructure.sty)
Provides: tex(beamerbasemisc.sty)
Provides: tex(beamerbasemodes.sty)
Provides: tex(beamerbasenavigation.sty)
Provides: tex(beamerbasenotes.sty)
Provides: tex(beamerbaseoptions.sty)
Provides: tex(beamerbaseoverlay.sty)
Provides: tex(beamerbasercs.sty)
Provides: tex(beamerbaserequires.sty)
Provides: tex(beamerbasesection.sty)
Provides: tex(beamerbasetemplates.sty)
Provides: tex(beamerbasethemes.sty)
Provides: tex(beamerbasetheorems.sty)
Provides: tex(beamerbasetitle.sty)
Provides: tex(beamerbasetoc.sty)
Provides: tex(beamerbasetranslator.sty)
Provides: tex(beamerbasetwoscreens.sty)
Provides: tex(beamerbaseverbatim.sty)
Provides: tex(beamerfoils.sty)
Provides: tex(beamerprosper.sty)
Provides: tex(beamerseminar.sty)
Provides: tex(beamertexpower.sty)
Provides: tex(multimedia.sty)
Provides: tex(multimediasymbols.sty)
Provides: tex(xmpmulti.sty)
Provides: tex(beamercolorthemealbatross.sty)
Provides: tex(beamercolorthemebeaver.sty)
Provides: tex(beamercolorthemebeetle.sty)
Provides: tex(beamercolorthemecrane.sty)
Provides: tex(beamercolorthemedefault.sty)
Provides: tex(beamercolorthemedolphin.sty)
Provides: tex(beamercolorthemedove.sty)
Provides: tex(beamercolorthemefly.sty)
Provides: tex(beamercolorthemelily.sty)
Provides: tex(beamercolorthemeorchid.sty)
Provides: tex(beamercolorthemerose.sty)
Provides: tex(beamercolorthemeseagull.sty)
Provides: tex(beamercolorthemeseahorse.sty)
Provides: tex(beamercolorthemesidebartab.sty)
Provides: tex(beamercolorthemestructure.sty)
Provides: tex(beamercolorthemewhale.sty)
Provides: tex(beamercolorthemewolverine.sty)
Provides: tex(beamerfontthemedefault.sty)
Provides: tex(beamerfontthemeprofessionalfonts.sty)
Provides: tex(beamerfontthemeserif.sty)
Provides: tex(beamerfontthemestructurebold.sty)
Provides: tex(beamerfontthemestructureitalicserif.sty)
Provides: tex(beamerfontthemestructuresmallcapsserif.sty)
Provides: tex(beamerinnerthemecircles.sty)
Provides: tex(beamerinnerthemedefault.sty)
Provides: tex(beamerinnerthemeinmargin.sty)
Provides: tex(beamerinnerthemerectangles.sty)
Provides: tex(beamerinnerthemerounded.sty)
Provides: tex(beamerouterthemedefault.sty)
Provides: tex(beamerouterthemeinfolines.sty)
Provides: tex(beamerouterthememiniframes.sty)
Provides: tex(beamerouterthemeshadow.sty)
Provides: tex(beamerouterthemesidebar.sty)
Provides: tex(beamerouterthemesmoothbars.sty)
Provides: tex(beamerouterthemesmoothtree.sty)
Provides: tex(beamerouterthemesplit.sty)
Provides: tex(beamerouterthemetree.sty)
Provides: tex(beamerthemeAnnArbor.sty)
Provides: tex(beamerthemeAntibes.sty)
Provides: tex(beamerthemeBergen.sty)
Provides: tex(beamerthemeBerkeley.sty)
Provides: tex(beamerthemeBerlin.sty)
Provides: tex(beamerthemeBoadilla.sty)
Provides: tex(beamerthemeCambridgeUS.sty)
Provides: tex(beamerthemeCopenhagen.sty)
Provides: tex(beamerthemeDarmstadt.sty)
Provides: tex(beamerthemeDresden.sty)
Provides: tex(beamerthemeFrankfurt.sty)
Provides: tex(beamerthemeGoettingen.sty)
Provides: tex(beamerthemeHannover.sty)
Provides: tex(beamerthemeIlmenau.sty)
Provides: tex(beamerthemeJuanLesPins.sty)
Provides: tex(beamerthemeLuebeck.sty)
Provides: tex(beamerthemeMadrid.sty)
Provides: tex(beamerthemeMalmoe.sty)
Provides: tex(beamerthemeMarburg.sty)
Provides: tex(beamerthemeMontpellier.sty)
Provides: tex(beamerthemePaloAlto.sty)
Provides: tex(beamerthemePittsburgh.sty)
Provides: tex(beamerthemeRochester.sty)
Provides: tex(beamerthemeSingapore.sty)
Provides: tex(beamerthemeSzeged.sty)
Provides: tex(beamerthemeWarsaw.sty)
Provides: tex(beamerthemeboxes.sty)
Provides: tex(beamerthemedefault.sty)
Provides: tex(beamerthemebars.sty)
Provides: tex(beamerthemeclassic.sty)
Provides: tex(beamerthemecompatibility.sty)
Provides: tex(beamerthemelined.sty)
Provides: tex(beamerthemeplain.sty)
Provides: tex(beamerthemeshadow.sty)
Provides: tex(beamerthemesidebar.sty)
Provides: tex(beamerthemesplit.sty)
Provides: tex(beamerthemetree.sty)
Provides: tex(translator.sty)
Requires: tex(ucs.sty)
Requires: tex(inputenc.sty)
Requires: tex(geometry.sty)
Requires: tex(pgfcore.sty)
Requires: tex(xxcolor.sty)
Requires: tex(hyperref.sty)
Requires: tex(xcolor.sty)
Requires: tex(amssymb.sty)
Requires: tex(enumerate.sty)
Requires: tex(keyval.sty)
Requires: tex(amsmath.sty)
Requires: tex(amsthm.sty)
Requires: tex(pgf.sty)

%description
The beamer LaTeX class can be used for producing slides. Its
functionality is similar to Prosper but does not need any
external programs and can directly produce a presentation using
pdflatex. Beamer uses pgf for pdf/ps independent graphics.
Frames are created using \frame{...}, and a frame can build
multiple slides through a simple notation for specifying
material for each slide within a frame. Beamer supports
bibliographies, appendicies and transitions. Short versions of
title, authors, institute can also be specified as optional
parameters. A \plainframe{} allows a picture, for example, to
fill the whole frame. Support figure and table environments,
transparency effects, a \transduration command, animation
commands, a pauses environment. Beamer also provides
compatibility with other packages like prosper. The package now
incorporates the functionality of the former translator
package, which is used for customising the package for use in
other language environments.

date: 2010-07-12 22:23:23 +0200

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
Summary: Documentation for beamer
Version: %{tl_version}
Release: %{tl_noarch_release}.3.10.svn19443%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch
Requires: texlive-pgf-doc
Requires: texlive-xcolor-doc

%description doc
Documentation for beamer


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/gpl.txt gpl.txt
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
%doc gpl.txt
%{_texdir}/texmf-dist/tex/latex/beamer/art/beamericonarticle.20.eps
%{_texdir}/texmf-dist/tex/latex/beamer/art/beamericonarticle.20.pdf
%{_texdir}/texmf-dist/tex/latex/beamer/art/beamericonarticle.eps
%{_texdir}/texmf-dist/tex/latex/beamer/art/beamericonarticle.pdf
%{_texdir}/texmf-dist/tex/latex/beamer/art/beamericonarticle.tex
%{_texdir}/texmf-dist/tex/latex/beamer/art/beamericonbook.20.eps
%{_texdir}/texmf-dist/tex/latex/beamer/art/beamericonbook.20.pdf
%{_texdir}/texmf-dist/tex/latex/beamer/art/beamericonbook.eps
%{_texdir}/texmf-dist/tex/latex/beamer/art/beamericonbook.pdf
%{_texdir}/texmf-dist/tex/latex/beamer/art/beamericonbook.tex
%{_texdir}/texmf-dist/tex/latex/beamer/beamer.cls
%{_texdir}/texmf-dist/tex/latex/beamer/beamerarticle.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbasearticle.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbaseauxtemplates.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbaseboxes.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbasecolor.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbasecompatibility.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbasedecode.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbaseexercise.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbasefont.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbaseframe.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbaseframecomponents.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbaseframesize.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbaselocalstructure.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbasemisc.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbasemodes.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbasenavigation.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbasenotes.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbaseoptions.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbaseoverlay.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbasercs.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbaserequires.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbasesection.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbasetemplates.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbasethemes.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbasetheorems.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbasetitle.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbasetoc.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbasetranslator.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbasetwoscreens.sty
%{_texdir}/texmf-dist/tex/latex/beamer/beamerbaseverbatim.sty
%{_texdir}/texmf-dist/tex/latex/beamer/emulation/beamerfoils.sty
%{_texdir}/texmf-dist/tex/latex/beamer/emulation/beamerprosper.sty
%{_texdir}/texmf-dist/tex/latex/beamer/emulation/beamerseminar.sty
%{_texdir}/texmf-dist/tex/latex/beamer/emulation/beamertexpower.sty
%{_texdir}/texmf-dist/tex/latex/beamer/emulation/examples/beamerexample-foils.tex
%{_texdir}/texmf-dist/tex/latex/beamer/emulation/examples/beamerexample-prosper.tex
%{_texdir}/texmf-dist/tex/latex/beamer/emulation/examples/beamerexample-seminar.tex
%{_texdir}/texmf-dist/tex/latex/beamer/emulation/examples/beamerexample-texpower.tex
%{_texdir}/texmf-dist/tex/latex/beamer/multimedia/multimedia.sty
%{_texdir}/texmf-dist/tex/latex/beamer/multimedia/multimediasymbols.sty
%{_texdir}/texmf-dist/tex/latex/beamer/multimedia/xmpmulti.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/color/beamercolorthemealbatross.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/color/beamercolorthemebeaver.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/color/beamercolorthemebeetle.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/color/beamercolorthemecrane.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/color/beamercolorthemedefault.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/color/beamercolorthemedolphin.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/color/beamercolorthemedove.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/color/beamercolorthemefly.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/color/beamercolorthemelily.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/color/beamercolorthemeorchid.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/color/beamercolorthemerose.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/color/beamercolorthemeseagull.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/color/beamercolorthemeseahorse.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/color/beamercolorthemesidebartab.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/color/beamercolorthemestructure.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/color/beamercolorthemewhale.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/color/beamercolorthemewolverine.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/font/beamerfontthemedefault.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/font/beamerfontthemeprofessionalfonts.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/font/beamerfontthemeserif.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/font/beamerfontthemestructurebold.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/font/beamerfontthemestructureitalicserif.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/font/beamerfontthemestructuresmallcapsserif.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/inner/beamerinnerthemecircles.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/inner/beamerinnerthemedefault.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/inner/beamerinnerthemeinmargin.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/inner/beamerinnerthemerectangles.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/inner/beamerinnerthemerounded.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/outer/beamerouterthemedefault.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/outer/beamerouterthemeinfolines.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/outer/beamerouterthememiniframes.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/outer/beamerouterthemeshadow.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/outer/beamerouterthemesidebar.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/outer/beamerouterthemesmoothbars.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/outer/beamerouterthemesmoothtree.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/outer/beamerouterthemesplit.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/outer/beamerouterthemetree.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeAnnArbor.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeAntibes.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeBergen.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeBerkeley.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeBerlin.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeBoadilla.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeCambridgeUS.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeCopenhagen.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeDarmstadt.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeDresden.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeFrankfurt.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeGoettingen.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeHannover.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeIlmenau.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeJuanLesPins.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeLuebeck.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeMadrid.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeMalmoe.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeMarburg.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeMontpellier.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemePaloAlto.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemePittsburgh.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeRochester.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeSingapore.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeSzeged.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeWarsaw.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeboxes.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemedefault.sty
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-basic-dictionary/translator-basic-dictionary-Croatian.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-basic-dictionary/translator-basic-dictionary-English.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-basic-dictionary/translator-basic-dictionary-French.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-basic-dictionary/translator-basic-dictionary-German.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-basic-dictionary/translator-basic-dictionary-Polish.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-basic-dictionary/translator-basic-dictionary-Serbian.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-bibliography-dictionary/translator-bibliography-dictionary-Croatian.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-bibliography-dictionary/translator-bibliography-dictionary-English.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-bibliography-dictionary/translator-bibliography-dictionary-French.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-bibliography-dictionary/translator-bibliography-dictionary-German.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-bibliography-dictionary/translator-bibliography-dictionary-Polish.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-bibliography-dictionary/translator-bibliography-dictionary-Serbian.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-environment-dictionary/translator-environment-dictionary-Croatian.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-environment-dictionary/translator-environment-dictionary-English.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-environment-dictionary/translator-environment-dictionary-French.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-environment-dictionary/translator-environment-dictionary-German.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-environment-dictionary/translator-environment-dictionary-Polish.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-environment-dictionary/translator-environment-dictionary-Serbian.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-months-dictionary/translator-months-dictionary-Croatian.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-months-dictionary/translator-months-dictionary-English.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-months-dictionary/translator-months-dictionary-French.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-months-dictionary/translator-months-dictionary-German.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-months-dictionary/translator-months-dictionary-Polish.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-months-dictionary/translator-months-dictionary-Serbian.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-numbers-dictionary/translator-numbers-dictionary-Croatian.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-numbers-dictionary/translator-numbers-dictionary-English.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-numbers-dictionary/translator-numbers-dictionary-French.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-numbers-dictionary/translator-numbers-dictionary-German.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-numbers-dictionary/translator-numbers-dictionary-Polish.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-numbers-dictionary/translator-numbers-dictionary-Serbian.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-theorem-dictionary/translator-theorem-dictionary-Croatian.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-theorem-dictionary/translator-theorem-dictionary-English.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-theorem-dictionary/translator-theorem-dictionary-French.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-theorem-dictionary/translator-theorem-dictionary-German.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-theorem-dictionary/translator-theorem-dictionary-Polish.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-theorem-dictionary/translator-theorem-dictionary-Serbian.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/translator-language-mappings.tex
%{_texdir}/texmf-dist/tex/latex/beamer/translator/translator.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/color/beamercolorthemespruce.sty
%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/beamerthemeEastLansing.sty
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-basic-dictionary/translator-basic-dictionary-Brazilian.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-basic-dictionary/translator-basic-dictionary-Greek.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-basic-dictionary/translator-basic-dictionary-Norsk.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-bibliography-dictionary/translator-bibliography-dictionary-Brazilian.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-bibliography-dictionary/translator-bibliography-dictionary-Greek.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-environment-dictionary/translator-environment-dictionary-Brazilian.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-environment-dictionary/translator-environment-dictionary-Greek.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-months-dictionary/translator-months-dictionary-Brazilian.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-months-dictionary/translator-months-dictionary-Greek.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-months-dictionary/translator-months-dictionary-Norsk.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-numbers-dictionary/translator-numbers-dictionary-Brazilian.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-numbers-dictionary/translator-numbers-dictionary-Greek.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-numbers-dictionary/translator-numbers-dictionary-Norsk.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-theorem-dictionary/translator-theorem-dictionary-Brazilian.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-theorem-dictionary/translator-theorem-dictionary-Greek.dict
%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-theorem-dictionary/translator-theorem-dictionary-Norsk.dict

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/latex/beamer/AUTHORS
%{_texdir}/texmf-dist/doc/latex/beamer/ChangeLog
%{_texdir}/texmf-dist/doc/latex/beamer/FILES
%{_texdir}/texmf-dist/doc/latex/beamer/INSTALL
%{_texdir}/texmf-dist/doc/latex/beamer/README
%{_texdir}/texmf-dist/doc/latex/beamer/TODO
%{_texdir}/texmf-dist/doc/latex/beamer/doc/Makefile
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamercolorthemeexample.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerfontthemeexample.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerinnerthemeexample.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerlogo.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerouterthemeexample.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerthemeexample.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerthemeexamplebase.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-animations.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-color.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-compatibility.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-elements.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-emulation.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-fonts.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-frames.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-globalstructure.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-graphics.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-guidelines.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-installation.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-interaction.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-introduction.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-license.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-localstructure.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-macros.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-nonpresentation.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-notes.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-overlays.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-solutions.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-themes.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-translator.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-transparencies.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-tricks.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-tutorial.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-twoscreens.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerug-workflow.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beameruserguide.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beameruserguide.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/licenses/LICENSE
%{_texdir}/texmf-dist/doc/latex/beamer/doc/themeexamples/beamerthemeexample.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/themeexamples/beamerthememakeexamples.sh
%{_texdir}/texmf-dist/doc/latex/beamer/emacs/beamer.el
%{_texdir}/texmf-dist/doc/latex/beamer/examples/Makefile
%{_texdir}/texmf-dist/doc/latex/beamer/examples/beamerexample-conference-talk.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/examples/beamerexample-lecture-beamer-version.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/examples/beamerexample-lecture-print-version.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/examples/a-conference-talk/beamerexample-conference-talk.tex
%{_texdir}/texmf-dist/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-beamer-version.tex
%{_texdir}/texmf-dist/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-body.tex
%{_texdir}/texmf-dist/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-logo.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-pic1.jpg
%{_texdir}/texmf-dist/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-pic2.jpg
%{_texdir}/texmf-dist/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-pic3.jpg
%{_texdir}/texmf-dist/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-pic4.jpg
%{_texdir}/texmf-dist/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-pic5.jpg
%{_texdir}/texmf-dist/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-pic6.jpg
%{_texdir}/texmf-dist/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-print-version.tex
%{_texdir}/texmf-dist/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-style.tex
%{_texdir}/texmf-dist/doc/latex/beamer/examples/lyx-based-presentation/beamerexample-lyx.lyx
%{_texdir}/texmf-dist/doc/latex/beamer/solutions/conference-talks/conference-ornate-20min.de.lyx
%{_texdir}/texmf-dist/doc/latex/beamer/solutions/conference-talks/conference-ornate-20min.de.tex
%{_texdir}/texmf-dist/doc/latex/beamer/solutions/conference-talks/conference-ornate-20min.en.lyx
%{_texdir}/texmf-dist/doc/latex/beamer/solutions/conference-talks/conference-ornate-20min.en.tex
%{_texdir}/texmf-dist/doc/latex/beamer/solutions/conference-talks/conference-ornate-20min.fr.tex
%{_texdir}/texmf-dist/doc/latex/beamer/solutions/generic-talks/generic-ornate-15min-45min.de.lyx
%{_texdir}/texmf-dist/doc/latex/beamer/solutions/generic-talks/generic-ornate-15min-45min.de.tex
%{_texdir}/texmf-dist/doc/latex/beamer/solutions/generic-talks/generic-ornate-15min-45min.en.lyx
%{_texdir}/texmf-dist/doc/latex/beamer/solutions/generic-talks/generic-ornate-15min-45min.en.tex
%{_texdir}/texmf-dist/doc/latex/beamer/solutions/generic-talks/generic-ornate-15min-45min.fr.tex
%{_texdir}/texmf-dist/doc/latex/beamer/solutions/short-talks/speaker_introduction-ornate-2min.de.lyx
%{_texdir}/texmf-dist/doc/latex/beamer/solutions/short-talks/speaker_introduction-ornate-2min.de.tex
%{_texdir}/texmf-dist/doc/latex/beamer/solutions/short-talks/speaker_introduction-ornate-2min.en.lyx
%{_texdir}/texmf-dist/doc/latex/beamer/solutions/short-talks/speaker_introduction-ornate-2min.en.tex
%{_texdir}/texmf-dist/doc/latex/beamer/solutions/short-talks/speaker_introduction-ornate-2min.fr.tex
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugcolorthemealbatross.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugcolorthemealbatrossstylish.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugcolorthemebeaver.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugcolorthemebeetle.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugcolorthemecrane.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugcolorthemedefault.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugcolorthemedolphin.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugcolorthemedove.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugcolorthemefly.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugcolorthemelily.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugcolorthemeorchid.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugcolorthemerose.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugcolorthemeseagull.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugcolorthemeseahorse.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugcolorthemesidebartab.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugcolorthemespruce.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugcolorthemestructure.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugcolorthemewhale.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugcolorthemewolverine.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugfontthemedefault.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugfontthemeserif.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugfontthemestructurebold.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugfontthemestructureitalicserif.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugfontthemestructuresmallcapsserif.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beameruginnerthemecircles.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beameruginnerthemedefault.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beameruginnerthemeinmargin.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beameruginnerthemerectangles.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beameruginnerthemerounded.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugouterthemedefault.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugouterthemeinfolines.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugouterthememiniframes.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugouterthemeshadow.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugouterthemesidebar.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugouterthemesmoothbars.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugouterthemesmoothtree.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugouterthemesplit.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugouterthemetree.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeAnnArbor.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeAntibes.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeBergen.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeBerkeley.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeBerlin.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeBoadilla.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeCambridgeUS.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeCopenhagen.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeDarmstadt.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeDresden.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeEastLansing.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeFrankfurt.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeGoettingen.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeHannover.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeIlmenau.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeJuanLesPins.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeLuebeck.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeMadrid.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeMalmoe.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeMarburg.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeMontpellier.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemePaloAlto.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemePittsburgh.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeRochester.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeSingapore.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeSzeged.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeWarsaw.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemeboxes.pdf
%{_texdir}/texmf-dist/doc/latex/beamer/doc/beamerugthemedefault.pdf

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
