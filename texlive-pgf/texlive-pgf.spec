%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/pgf.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/pgf.doc.tar.xz

Name: texlive-pgf
License: LPPL
Summary: Create PostScript and PDF graphics in TeX
Version: %{tl_version}
Release: %{tl_noarch_release}.2.00.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-xkeyval = %{tl_version}
Provides: tex(pgf.sty)
Provides: tex(pgfbaseimage.sty)
Provides: tex(pgfbaselayers.sty)
Provides: tex(pgfbasematrix.sty)
Provides: tex(pgfbasepatterns.sty)
Provides: tex(pgfbaseplot.sty)
Provides: tex(pgfbaseshapes.sty)
Provides: tex(pgfbasesnakes.sty)
Provides: tex(pgfcore.sty)
Provides: tex(pgfarrows.sty)
Provides: tex(pgfautomata.sty)
Provides: tex(pgfcomp-version-0-65.sty)
Provides: tex(pgfcomp-version-1-18.sty)
Provides: tex(pgfheaps.sty)
Provides: tex(pgflibraryarrows.sty)
Provides: tex(pgflibraryautomata.sty)
Provides: tex(pgflibraryplothandlers.sty)
Provides: tex(pgflibraryplotmarks.sty)
Provides: tex(pgflibraryshapes.sty)
Provides: tex(pgflibrarysnakes.sty)
Provides: tex(pgflibrarytikzbackgrounds.sty)
Provides: tex(pgflibrarytikztrees.sty)
Provides: tex(pgfnodes.sty)
Provides: tex(pgfshade.sty)
Provides: tex(pgfpict2e.sty)
Provides: tex(tikz.sty)
Provides: tex(pgfmath.sty)
Provides: tex(pgfsys.sty)
Provides: tex(pgfcalendar.sty)
Provides: tex(pgffor.sty)
Provides: tex(pgfkeys.sty)
Provides: tex(pgfpages.sty)
Provides: tex(pgfrcs.sty)
Provides: tex(xxcolor.sty)
Requires: tex(graphicx.sty)
Requires: tex(keyval.sty)
Requires: tex(xcolor.sty)

%description
PGF is a macro package for creating graphics. It is platform-
and format-independent and works together with the most
important TeX backend drivers, including pdftex and dvips. It
comes with a user-friedly syntax layer called TikZ. Its usage
is similar to pstricks and the standard picture environment.
PGF works with plain (pdf-)TeX, (pdf-)LaTeX, and ConTeXt.
Unlike pstricks, it can produce either PostScript or PDF
output.

date: 2008-02-20 14:18:00 +0100

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
Summary: Documentation for pgf
Version: %{tl_version}
Release: %{tl_noarch_release}.2.00.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch
Requires: texlive-xkeyval-doc

%description doc
Documentation for pgf


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/lppl1.3.txt lppl1.3.txt
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

%files doc
%defattr(-,root,root)
%doc lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/pgf/AUTHORS
%{_texdir}/texmf-dist/doc/generic/pgf/ChangeLog
%{_texdir}/texmf-dist/doc/generic/pgf/FILES
%{_texdir}/texmf-dist/doc/generic/pgf/INSTALL
%{_texdir}/texmf-dist/doc/generic/pgf/README
%{_texdir}/texmf-dist/doc/generic/pgf/TODO
%{_texdir}/texmf-dist/doc/generic/pgf/images/brave-gnu-world-logo-mask.bb
%{_texdir}/texmf-dist/doc/generic/pgf/images/brave-gnu-world-logo-mask.jpg
%{_texdir}/texmf-dist/doc/generic/pgf/images/brave-gnu-world-logo.25.bb
%{_texdir}/texmf-dist/doc/generic/pgf/images/brave-gnu-world-logo.25.eps
%{_texdir}/texmf-dist/doc/generic/pgf/images/brave-gnu-world-logo.25.jpg
%{_texdir}/texmf-dist/doc/generic/pgf/images/brave-gnu-world-logo.bb
%{_texdir}/texmf-dist/doc/generic/pgf/images/brave-gnu-world-logo.eps
%{_texdir}/texmf-dist/doc/generic/pgf/images/brave-gnu-world-logo.jpg
%{_texdir}/texmf-dist/doc/generic/pgf/images/pgfmanual-mindmap-1.pdf
%{_texdir}/texmf-dist/doc/generic/pgf/images/pgfmanual-mindmap-2.pdf
%{_texdir}/texmf-dist/doc/generic/pgf/licenses/LICENSE
%{_texdir}/texmf-dist/doc/generic/pgf/licenses/gnu-free-documentation-license-1.2.txt
%{_texdir}/texmf-dist/doc/generic/pgf/licenses/gnu-public-license-2.txt
%{_texdir}/texmf-dist/doc/generic/pgf/licenses/latex-project-public-license-1.3c.txt
%{_texdir}/texmf-dist/doc/generic/pgf/licenses/manifest-code.txt
%{_texdir}/texmf-dist/doc/generic/pgf/licenses/manifest-documentation.txt
%{_texdir}/texmf-dist/doc/generic/pgf/macros/pgfmanual-en-macros.tex
%{_texdir}/texmf-dist/doc/generic/pgf/pgfmanual.pdf
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-base-actions.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-base-arrows.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-base-decorations.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-base-design.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-base-external.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-base-images.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-base-internalregisters.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-base-layers.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-base-matrices.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-base-nodes.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-base-paths.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-base-patterns.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-base-plots.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-base-points.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-base-quick.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-base-scopes.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-base-shadings.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-base-transformations.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-base-transparency.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-drivers.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-dv-axes.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-dv-backend.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-dv-examples.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-dv-formats.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-dv-introduction.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-dv-main.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-dv-stylesheets.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-dv-visualizers.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-guidelines.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-installation.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-introduction.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-3d.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-arrows.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-automata.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-backgrounds.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-calc.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-calendar.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-chains.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-circuits.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-decorations.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-edges.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-er.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-external.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-fadings.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-fit.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-fixedpoint.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-folding.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-fpu.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-lsystems.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-matrices.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-mindmaps.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-patterns.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-petri.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-plot-handlers.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-plot-marks.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-profiler.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-shadings.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-shadows.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-shapes.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-spy.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-svg-path.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-through.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-trees.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-library-turtle.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-license.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-main.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-math-algorithms.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-math-commands.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-math-design.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-math-numberprinting.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-math-parsing.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-module-parser.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-oo.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-pages.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-pgfcalendar.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-pgffor.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-pgfkeys.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-pgfkeysfiltered.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-pgfsys-commands.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-pgfsys-overview.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-pgfsys-paths.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-pgfsys-protocol.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-tikz-actions.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-tikz-coordinates.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-tikz-decorations.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-tikz-design.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-tikz-matrices.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-tikz-paths.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-tikz-plots.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-tikz-scopes.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-tikz-shapes.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-tikz-transformations.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-tikz-transparency.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-tikz-trees.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-tutorial-Euclid.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-tutorial-chains.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-tutorial-map.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-tutorial-nodes.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-tutorial-nodes.tex.orig
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-tutorial.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/pgfmanual-en-xxcolor.tex
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/plots/pgf-asymptotic-example.gnuplot
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/plots/pgf-asymptotic-example.table
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/plots/pgf-exp.gnuplot
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/plots/pgf-exp.table
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/plots/pgf-parametric-example.gnuplot
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/plots/pgf-parametric-example.table
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/plots/pgf-sin.gnuplot
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/plots/pgf-sin.table
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/plots/pgf-x.gnuplot
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/plots/pgf-x.table
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/plots/pgfmanual-sine.gnuplot
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/plots/pgfmanual-sine.table
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/plots/pgfplotgnuplot-example.gnuplot
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/plots/pgfplotgnuplot-example.table
%{_texdir}/texmf-dist/doc/generic/pgf/text-en/texmf.cnf
%{_texdir}/texmf-dist/doc/generic/pgf/version-for-dvipdfm/en/Makefile
%{_texdir}/texmf-dist/doc/generic/pgf/version-for-dvipdfm/en/pgfmanual.tex
%{_texdir}/texmf-dist/doc/generic/pgf/version-for-dvipdfm/pgfmanual-dvipdfm.cfg
%{_texdir}/texmf-dist/doc/generic/pgf/version-for-dvipdfmx/en/Makefile
%{_texdir}/texmf-dist/doc/generic/pgf/version-for-dvipdfmx/en/pgfmanual.tex
%{_texdir}/texmf-dist/doc/generic/pgf/version-for-dvipdfmx/pgfmanual-dvipdfmx.cfg
%{_texdir}/texmf-dist/doc/generic/pgf/version-for-dvips/en/Makefile
%{_texdir}/texmf-dist/doc/generic/pgf/version-for-dvips/en/pgfmanual.tex
%{_texdir}/texmf-dist/doc/generic/pgf/version-for-dvips/pgfmanual-dvips.cfg
%{_texdir}/texmf-dist/doc/generic/pgf/version-for-pdftex/en/Makefile
%{_texdir}/texmf-dist/doc/generic/pgf/version-for-pdftex/en/pgfmanual.figlist
%{_texdir}/texmf-dist/doc/generic/pgf/version-for-pdftex/en/pgfmanual.tex
%{_texdir}/texmf-dist/doc/generic/pgf/version-for-pdftex/pgfmanual-pdftex.cfg
%{_texdir}/texmf-dist/doc/generic/pgf/version-for-tex4ht/en/Makefile
%{_texdir}/texmf-dist/doc/generic/pgf/version-for-tex4ht/en/pgfmanual.tex
%{_texdir}/texmf-dist/doc/generic/pgf/version-for-tex4ht/pgfmanual-tex4ht.cfg
%{_texdir}/texmf-dist/doc/generic/pgf/version-for-vtex/en/Makefile
%{_texdir}/texmf-dist/doc/generic/pgf/version-for-vtex/en/pgfmanual.tex
%{_texdir}/texmf-dist/doc/generic/pgf/version-for-vtex/pgfmanual-vtex.cfg
%{_texdir}/texmf-dist/doc/generic/pgf/version-for-xetex/en/Makefile
%{_texdir}/texmf-dist/doc/generic/pgf/version-for-xetex/en/pgfmanual.tex
%{_texdir}/texmf-dist/doc/generic/pgf/version-for-xetex/pgfmanual-xetex.cfg
%{_texdir}/texmf-dist/doc/latex/pgf/README

%files
%defattr(-,root,root)
%{_texdir}/texmf-dist/tex/context/third/pgf/basiclayer/t-pgf.tex
%{_texdir}/texmf-dist/tex/context/third/pgf/basiclayer/t-pgfbim.tex
%{_texdir}/texmf-dist/tex/context/third/pgf/basiclayer/t-pgfbla.tex
%{_texdir}/texmf-dist/tex/context/third/pgf/basiclayer/t-pgfbma.tex
%{_texdir}/texmf-dist/tex/context/third/pgf/basiclayer/t-pgfbpl.tex
%{_texdir}/texmf-dist/tex/context/third/pgf/basiclayer/t-pgfbpt.tex
%{_texdir}/texmf-dist/tex/context/third/pgf/basiclayer/t-pgfbsh.tex
%{_texdir}/texmf-dist/tex/context/third/pgf/basiclayer/t-pgfbsn.tex
%{_texdir}/texmf-dist/tex/context/third/pgf/basiclayer/t-pgfcor.tex
%{_texdir}/texmf-dist/tex/context/third/pgf/frontendlayer/t-tikz.tex
%{_texdir}/texmf-dist/tex/context/third/pgf/math/t-pgfmat.tex
%{_texdir}/texmf-dist/tex/context/third/pgf/systemlayer/t-pgfsys.tex
%{_texdir}/texmf-dist/tex/context/third/pgf/utilities/t-pgfcal.tex
%{_texdir}/texmf-dist/tex/context/third/pgf/utilities/t-pgffor.tex
%{_texdir}/texmf-dist/tex/context/third/pgf/utilities/t-pgfkey.tex
%{_texdir}/texmf-dist/tex/context/third/pgf/utilities/t-pgfmod.tex
%{_texdir}/texmf-dist/tex/context/third/pgf/utilities/t-pgfrcs.tex
%{_texdir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcore.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcorearrows.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreexternal.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcoregraphicstate.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreimage.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcorelayers.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreobjects.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepathconstruct.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepathprocessing.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepathusage.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepatterns.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepoints.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcorequick.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcorescopes.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreshade.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcoretransformations.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/basiclayer/pgfcoretransparency.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/svg/svgpgf.cfg
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/svg/svgpgf.xmt
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/svg/svgtest.cfg
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/svg/svgtest.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/svg/svgtest.xml
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.ee.IEC.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.ee.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.logic.CDH.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.logic.IEC.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.logic.US.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.logic.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/tikzlibrarydatavisualization.3d.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/tikzlibrarydatavisualization.barcharts.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/tikzlibrarydatavisualization.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/tikzlibrarydatavisualization.formats.functions.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/tikzlibrarydatavisualization.polar.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/tikzlibrarydatavisualization.sparklines.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/graphs/tikzlibrarygraphs.basic.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/graphs/tikzlibrarygraphs.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzexternalshared.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrary3d.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryarrows.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryautomata.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarybackgrounds.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarycalc.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarycalendar.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarychains.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.footprints.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.fractals.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.markings.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.pathmorphing.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.pathreplacing.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.shapes.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.text.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryer.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryfadings.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryfit.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryfixedpointarithmetic.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryfolding.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryfpu.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryintersections.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarylindenmayersystems.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarymatrix.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarymindmap.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarypatterns.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarypetri.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryplothandlers.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryplotmarks.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarypositioning.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryscopes.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshadings.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshadows.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.arrows.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.callouts.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.gates.logic.IEC.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.gates.logic.US.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.geometric.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.misc.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.multipart.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.symbols.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarysnakes.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryspy.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarysvg.path.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarythrough.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarytopaths.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarytrees.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryturtle.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/tikz.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/datavisualization/pgflibrarydatavisualization.barcharts.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/datavisualization/pgflibrarydatavisualization.formats.functions.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/datavisualization/pgflibrarydatavisualization.polar.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.footprints.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.fractals.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.markings.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.pathmorphing.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.pathreplacing.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.shapes.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.text.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/pgflibraryarrows.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/pgflibraryfadings.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/pgflibraryfixedpointarithmetic.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/pgflibraryfpu.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/pgflibraryintersections.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/pgflibrarylindenmayersystems.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/pgflibrarypatterns.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/pgflibraryplothandlers.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/pgflibraryplotmarks.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/pgflibraryprofiler.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/pgflibraryshadings.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/pgflibrarysnakes.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/pgflibrarysvg.path.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/shapes/circuits/pgflibraryshapes.gates.ee.IEC.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/shapes/circuits/pgflibraryshapes.gates.ee.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/shapes/circuits/pgflibraryshapes.gates.logic.IEC.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/shapes/circuits/pgflibraryshapes.gates.logic.US.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/shapes/circuits/pgflibraryshapes.gates.logic.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/shapes/pgflibraryshapes.arrows.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/shapes/pgflibraryshapes.callouts.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/shapes/pgflibraryshapes.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/shapes/pgflibraryshapes.geometric.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/shapes/pgflibraryshapes.misc.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/shapes/pgflibraryshapes.multipart.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/libraries/shapes/pgflibraryshapes.symbols.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/math/pgfmath.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/math/pgfmathcalc.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/math/pgfmathfloat.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.base.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.basic.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.comparison.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.misc.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.random.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.round.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.trigonometric.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/math/pgfmathparser.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/math/pgfmathutil.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/modules/pgfmoduledatavisualization.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/modules/pgfmoduledecorations.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/modules/pgfmodulematrix.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/modules/pgfmoduleoo.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/modules/pgfmoduleparser.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/modules/pgfmoduleplot.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/modules/pgfmoduleshapes.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/modules/pgfmodulesnakes.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/modules/pgfmodulesorting.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/rendering/pgfrenderpoints.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/rendering/pgfrendertransform.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/systemlayer/pgf.cfg
%{_texdir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-common-pdf-via-dvi.def
%{_texdir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-common-pdf.def
%{_texdir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-common-postscript.def
%{_texdir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-common-svg.def
%{_texdir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-dvi.def
%{_texdir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-dvipdfm.def
%{_texdir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-dvipdfmx.def
%{_texdir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-dvips.def
%{_texdir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-pdftex.def
%{_texdir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-tex4ht.def
%{_texdir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-textures.def
%{_texdir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-vtex.def
%{_texdir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-xetex.def
%{_texdir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsys.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsysprotocol.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/systemlayer/pgfsyssoftpath.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/utilities/pgfcalendar.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/utilities/pgfexternal.tex
%{_texdir}/texmf-dist/tex/generic/pgf/utilities/pgfexternalwithdepth.tex
%{_texdir}/texmf-dist/tex/generic/pgf/utilities/pgffor.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/utilities/pgfkeys.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/utilities/pgfkeysfiltered.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/utilities/pgfrcs.code.tex
%{_texdir}/texmf-dist/tex/generic/pgf/utilities/pgfutil-common.tex
%{_texdir}/texmf-dist/tex/generic/pgf/utilities/pgfutil-context.def
%{_texdir}/texmf-dist/tex/generic/pgf/utilities/pgfutil-latex.def
%{_texdir}/texmf-dist/tex/generic/pgf/utilities/pgfutil-plain.def
%{_texdir}/texmf-dist/tex/latex/pgf/basiclayer/pgf.sty
%{_texdir}/texmf-dist/tex/latex/pgf/basiclayer/pgfbaseimage.sty
%{_texdir}/texmf-dist/tex/latex/pgf/basiclayer/pgfbaselayers.sty
%{_texdir}/texmf-dist/tex/latex/pgf/basiclayer/pgfbasematrix.sty
%{_texdir}/texmf-dist/tex/latex/pgf/basiclayer/pgfbasepatterns.sty
%{_texdir}/texmf-dist/tex/latex/pgf/basiclayer/pgfbaseplot.sty
%{_texdir}/texmf-dist/tex/latex/pgf/basiclayer/pgfbaseshapes.sty
%{_texdir}/texmf-dist/tex/latex/pgf/basiclayer/pgfbasesnakes.sty
%{_texdir}/texmf-dist/tex/latex/pgf/basiclayer/pgfcore.sty
%{_texdir}/texmf-dist/tex/latex/pgf/compatibility/pgfarrows.sty
%{_texdir}/texmf-dist/tex/latex/pgf/compatibility/pgfautomata.sty
%{_texdir}/texmf-dist/tex/latex/pgf/compatibility/pgfcomp-version-0-65.sty
%{_texdir}/texmf-dist/tex/latex/pgf/compatibility/pgfcomp-version-1-18.sty
%{_texdir}/texmf-dist/tex/latex/pgf/compatibility/pgfheaps.sty
%{_texdir}/texmf-dist/tex/latex/pgf/compatibility/pgflibraryarrows.sty
%{_texdir}/texmf-dist/tex/latex/pgf/compatibility/pgflibraryautomata.sty
%{_texdir}/texmf-dist/tex/latex/pgf/compatibility/pgflibraryplothandlers.sty
%{_texdir}/texmf-dist/tex/latex/pgf/compatibility/pgflibraryplotmarks.sty
%{_texdir}/texmf-dist/tex/latex/pgf/compatibility/pgflibraryshapes.sty
%{_texdir}/texmf-dist/tex/latex/pgf/compatibility/pgflibrarysnakes.sty
%{_texdir}/texmf-dist/tex/latex/pgf/compatibility/pgflibrarytikzbackgrounds.sty
%{_texdir}/texmf-dist/tex/latex/pgf/compatibility/pgflibrarytikztrees.sty
%{_texdir}/texmf-dist/tex/latex/pgf/compatibility/pgfnodes.sty
%{_texdir}/texmf-dist/tex/latex/pgf/compatibility/pgfshade.sty
%{_texdir}/texmf-dist/tex/latex/pgf/doc/pgfmanual.code.tex
%{_texdir}/texmf-dist/tex/latex/pgf/doc/pgfmanual.pdflinks.code.tex
%{_texdir}/texmf-dist/tex/latex/pgf/doc/pgfmanual.prettyprinter.code.tex
%{_texdir}/texmf-dist/tex/latex/pgf/doc/pgfmanual.sty
%{_texdir}/texmf-dist/tex/latex/pgf/frontendlayer/libraries/tikzlibraryexternal.code.tex
%{_texdir}/texmf-dist/tex/latex/pgf/frontendlayer/pgfpict2e.sty
%{_texdir}/texmf-dist/tex/latex/pgf/frontendlayer/tikz.sty
%{_texdir}/texmf-dist/tex/latex/pgf/math/pgfmath.sty
%{_texdir}/texmf-dist/tex/latex/pgf/systemlayer/pgfsys.sty
%{_texdir}/texmf-dist/tex/latex/pgf/utilities/pgfcalendar.sty
%{_texdir}/texmf-dist/tex/latex/pgf/utilities/pgffor.sty
%{_texdir}/texmf-dist/tex/latex/pgf/utilities/pgfkeys.sty
%{_texdir}/texmf-dist/tex/latex/pgf/utilities/pgfpages.sty
%{_texdir}/texmf-dist/tex/latex/pgf/utilities/pgfrcs.sty
%{_texdir}/texmf-dist/tex/latex/pgf/utilities/tikzexternal.sty
%{_texdir}/texmf-dist/tex/latex/pgf/utilities/xxcolor.sty
%{_texdir}/texmf-dist/tex/plain/pgf/basiclayer/pgf.tex
%{_texdir}/texmf-dist/tex/plain/pgf/basiclayer/pgfbaseimage.tex
%{_texdir}/texmf-dist/tex/plain/pgf/basiclayer/pgfbaselayers.tex
%{_texdir}/texmf-dist/tex/plain/pgf/basiclayer/pgfbasematrix.tex
%{_texdir}/texmf-dist/tex/plain/pgf/basiclayer/pgfbasepatterns.tex
%{_texdir}/texmf-dist/tex/plain/pgf/basiclayer/pgfbaseplot.tex
%{_texdir}/texmf-dist/tex/plain/pgf/basiclayer/pgfbaseshapes.tex
%{_texdir}/texmf-dist/tex/plain/pgf/basiclayer/pgfbasesnakes.tex
%{_texdir}/texmf-dist/tex/plain/pgf/basiclayer/pgfcore.tex
%{_texdir}/texmf-dist/tex/plain/pgf/frontendlayer/tikz.tex
%{_texdir}/texmf-dist/tex/plain/pgf/math/pgfmath.tex
%{_texdir}/texmf-dist/tex/plain/pgf/systemlayer/pgfsys.tex
%{_texdir}/texmf-dist/tex/plain/pgf/utilities/pgfcalendar.tex
%{_texdir}/texmf-dist/tex/plain/pgf/utilities/pgffor.tex
%{_texdir}/texmf-dist/tex/plain/pgf/utilities/pgfkeys.tex
%{_texdir}/texmf-dist/tex/plain/pgf/utilities/pgfrcs.tex
