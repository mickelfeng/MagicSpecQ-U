%define source_date 20100814
%define tl_version 2010
%define tl_release 9.%{source_date}
%define tl_noarch_release 7
%define _binary_payload w6.xzdio
%define source_name texlive-%{source_date}-source

%{!?_texdir: %global _texdir %{_datadir}/%{name}}
%{!?_texmf_var: %global _texmf_var  %{_var}/lib/texmf}

# don't figure any perl requires
%define __perl_requires %{nil}

Name: texlive
Version: %{tl_version}
Release: %{tl_release}%{?dist}
Summary: TeX formatting system
Group: Applications/Publishing
License: Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL: http://tug.org/texlive/
BuildRequires: xz libXaw-devel ncurses-devel byacc
BuildRequires: gd-devel teckit-devel freetype-devel t1lib-devel libpng-devel zlib-devel poppler-devel t1utils
#BuildRequires: clisp-devel
Requires: %{name}-base
Obsoletes: texlive < %{tl_version}, texlive-texmf < %{tl_version}
Obsoletes: texlive-texmf-afm < %{tl_version}
Obsoletes: texlive-texmf-fonts < %{tl_version}, texlive-afm < %{tl_version}
Obsoletes: texlive-dviutils < %{tl_version}, texlive-utils < %{tl_version}
Obsoletes: texlive-texmf-errata < %{tl_version}
Obsoletes: texlive-texmf-errata-afm < %{tl_version}, texlive-texmf-errata-context < %{tl_version}
Obsoletes: texlive-texmf-errata-doc < %{tl_version}, texlive-texmf-errata-dvips < %{tl_version}
Obsoletes: texlive-texmf-errata-east-asian < %{tl_version}, texlive-texmf-errata-fonts < %{tl_version}
Obsoletes: texlive-texmf-errata-latex < %{tl_version}, texlive-texmf-errata-xetex < %{tl_version}
Patch1: tl-kpfix.patch
#Patch2: tl-poppler.patch
Source0: %{source_name}.tar.xz
Source1: tl2rpm.c
Source2: texlive.tlpdb
Source3: texlive-licenses.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package scheme-basic
Summary: basic scheme (plain and LaTeX)
Version: %{tl_version}
Release: %{tl_noarch_release}.svn17228%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}
Requires: texlive-collection-latex = %{tl_version}

%description scheme-basic
This is the basic TeX Live scheme: it is a small set of files
sufficient to typeset plain TeX or LaTeX documents in
PostScript or PDF, using the Computer Modern fonts.  This
scheme corresponds to collection-basic and collection-latex.

%package collection-basic
Summary: Essential programs and files
Version: %{tl_version}
Release: %{tl_noarch_release}.svn17228%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}
Requires: texlive-amsfonts = %{tl_version}
Requires: texlive-apalike = %{tl_version}
Requires: texlive-bibtex = %{tl_version}
Requires: texlive-cm = %{tl_version}
Requires: texlive-dvipdfm = %{tl_version}
Requires: texlive-dvipdfmx = %{tl_version}
Requires: texlive-dvipdfmx-def = %{tl_version}
Requires: texlive-dvips = %{tl_version}
Requires: texlive-enctex = %{tl_version}
Requires: texlive-etex = %{tl_version}
Requires: texlive-etex-pkg = %{tl_version}
Requires: texlive-glyphlist = %{tl_version}
Requires: texlive-gsftopk = %{tl_version}
Requires: texlive-hyph-utf8 = %{tl_version}
Requires: texlive-hyphen-base = %{tl_version}
Requires: texlive-ifluatex = %{tl_version}
Requires: texlive-ifxetex = %{tl_version}
Requires: texlive-kpathsea = %{tl_version}
Requires: texlive-lua-alt-getopt = %{tl_version}
Requires: texlive-luatex = %{tl_version}
Requires: texlive-makeindex = %{tl_version}
Requires: texlive-metafont = %{tl_version}
Requires: texlive-mflogo = %{tl_version}
Requires: texlive-mfware = %{tl_version}
Requires: texlive-misc = %{tl_version}
Requires: texlive-pdftex = %{tl_version}
Requires: texlive-plain = %{tl_version}
Requires: texlive-tcdialog = %{tl_version}
Requires: texlive-tetex = %{tl_version}
Requires: texlive-tex = %{tl_version}
Requires: texlive-texconfig = %{tl_version}
Requires: texlive-texlive-msg-translations = %{tl_version}
Requires: texlive-texlive-scripts = %{tl_version}
Requires: texlive-texlive.infra = %{tl_version}
Requires: texlive-xdvi = %{tl_version}
Provides: tex(tex) = %{tl_version}, tex = %{tl_version}
Requires: dvipdfm, dvipdfmx, xdvik

%description collection-basic
These files are regarded as basic for any TeX system, covering
plain TeX macros, Computer Modern fonts, and configuration for
common drivers; no LaTeX.

%package collection-documentation-base
Summary: TeX Live documentation
Version: %{tl_version}
Release: %{tl_noarch_release}.svn17091%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-texlive-common-doc = %{tl_version}
Requires: texlive-texlive-en-doc = %{tl_version}
Provides: texlive-texmf-doc = %{tl_version}
Obsoletes: texlive-texmf-doc < %{tl_version}

%description collection-documentation-base
collection-documentation-base package

%package kpathsea-bin
Summary: Binaries for kpathsea
Version: %{tl_version}
Release: %{tl_release}.svn18765%{?dist}
Requires: texlive-kpathsea  = %{tl_version}

%description kpathsea-bin
Binaries for kpathsea

%package bibtex-bin
Summary: Binaries for bibtex
Version: %{tl_version}
Release: %{tl_release}.svn18765%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-bibtex  = %{tl_version}

%description bibtex-bin
Binaries for bibtex

%package dvipdfm-bin
Summary: Binaries for dvipdfm
Version: %{tl_version}
Release: %{tl_release}.svn13663%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-dvipdfm  = %{tl_version}
Provides: dvipdfm = %{tl_version}
Obsoletes: dvipdfm < %{tl_version}

%description dvipdfm-bin
Binaries for dvipdfm

%package dvipdfmx-bin
Summary: Binaries for dvipdfmx
Version: %{tl_version}
Release: %{tl_release}.svn19008%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-dvipdfmx  = %{tl_version}
Provides: dvipdfmx = %{tl_version}
Obsoletes: dvipdfmx < %{tl_version}

%description dvipdfmx-bin
Binaries for dvipdfmx

%package dvips-bin
Summary: Binaries for dvips
Version: %{tl_version}
Release: %{tl_release}.svn19233%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-dvips  = %{tl_version}

%description dvips-bin
Binaries for dvips

%package gsftopk-bin
Summary: Binaries for gsftopk
Version: %{tl_version}
Release: %{tl_release}.svn18765%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-gsftopk  = %{tl_version}

%description gsftopk-bin
Binaries for gsftopk

%package luatex-bin
Summary: Binaries for luatex
Version: %{tl_version}
Release: %{tl_release}.svn19405%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-luatex  = %{tl_version}

%description luatex-bin
Binaries for luatex

%package makeindex-bin
Summary: Binaries for makeindex
Version: %{tl_version}
Release: %{tl_release}.svn19405%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-makeindex  = %{tl_version}

%description makeindex-bin
Binaries for makeindex

%package metafont-bin
Summary: Binaries for metafont
Version: %{tl_version}
Release: %{tl_release}.svn19008%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-metafont  = %{tl_version}

%description metafont-bin
Binaries for metafont

%package mfware-bin
Summary: Binaries for mfware
Version: %{tl_version}
Release: %{tl_release}.svn18765%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-mfware  = %{tl_version}

%description mfware-bin
Binaries for mfware

%package pdftex-bin
Summary: Binaries for pdftex
Version: %{tl_version}
Release: %{tl_release}.svn19008%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-pdftex  = %{tl_version}

%description pdftex-bin
Binaries for pdftex

%package tcdialog-bin
Summary: Binaries for tcdialog
Version: %{tl_version}
Release: %{tl_release}.svn18336%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-tcdialog  = %{tl_version}

%description tcdialog-bin
Binaries for tcdialog

%package tetex-bin
Summary: Binaries for tetex
Version: %{tl_version}
Release: %{tl_release}.svn19226%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-tetex  = %{tl_version}

%description tetex-bin
Binaries for tetex

%package tex-bin
Summary: Binaries for tex
Version: %{tl_version}
Release: %{tl_release}.svn19008%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-tex  = %{tl_version}

%description tex-bin
Binaries for tex

%package texconfig-bin
Summary: Binaries for texconfig
Version: %{tl_version}
Release: %{tl_release}.svn18336%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-texconfig  = %{tl_version}

%description texconfig-bin
Binaries for texconfig

%package texlive.infra-bin
Summary: Binaries for texlive.infra
Version: %{tl_version}
Release: %{tl_release}.svn18958%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-texlive.infra  = %{tl_version}

%description texlive.infra-bin
Binaries for texlive.infra

%package texlive-scripts-bin
Summary: Binaries for texlive-scripts
Version: %{tl_version}
Release: %{tl_release}.svn13663%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-texlive-scripts  = %{tl_version}

%description texlive-scripts-bin
Binaries for texlive-scripts

%package xdvi-bin
Summary: Binaries for xdvi
Version: %{tl_version}
Release: %{tl_release}.svn18765%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-xdvi  = %{tl_version}
Provides: xdvi = %{tl_version}, xdvik = %{tl_version}, tetex-xdvi = 3.1-99
Obsoletes: xdvi < %{tl_version}, xdvik < %{tl_version}, tetex-xdvi < 3.1-99

%description xdvi-bin
Binaries for xdvi

%package collection-latex
Summary: Basic LaTeX packages
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18674%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-ae = %{tl_version}
Requires: texlive-amscls = %{tl_version}
Requires: texlive-amsmath = %{tl_version}
Requires: texlive-babel = %{tl_version}
Requires: texlive-babelbib = %{tl_version}
Requires: texlive-carlisle = %{tl_version}
Requires: texlive-colortbl = %{tl_version}
Requires: texlive-fancyhdr = %{tl_version}
Requires: texlive-fix2col = %{tl_version}
Requires: texlive-geometry = %{tl_version}
Requires: texlive-graphics = %{tl_version}
Requires: texlive-hyperref = %{tl_version}
Requires: texlive-latex = %{tl_version}
Requires: texlive-latex-bin = %{tl_version}
Requires: texlive-latex-fonts = %{tl_version}
Requires: texlive-latexconfig = %{tl_version}
Requires: texlive-ltxmisc = %{tl_version}
Requires: texlive-mfnfss = %{tl_version}
Requires: texlive-mptopdf = %{tl_version}
Requires: texlive-natbib = %{tl_version}
Requires: texlive-oberdiek = %{tl_version}
Requires: texlive-pdftex-def = %{tl_version}
Requires: texlive-pslatex = %{tl_version}
Requires: texlive-psnfss = %{tl_version}
Requires: texlive-pspicture = %{tl_version}
Requires: texlive-tools = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}
Provides: tex(latex) = %{tl_version}

%description collection-latex
These packages are mandated by the core LaTeX team, or at least
very strongly recommended.

%package latex-bin-bin
Summary: Binaries for latex-bin
Version: %{tl_version}
Release: %{tl_release}.svn14050%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-latex-bin  = %{tl_version}

%description latex-bin-bin
Binaries for latex-bin

%package mptopdf-bin
Summary: Binaries for mptopdf
Version: %{tl_version}
Release: %{tl_release}.svn18674%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-mptopdf  = %{tl_version}

%description mptopdf-bin
Binaries for mptopdf

%package scheme-context
Summary: ConTeXt scheme
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18797%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-collection-context = %{tl_version}
Requires: texlive-collection-metapost = %{tl_version}
Requires: texlive-tex-gyre = %{tl_version}
Requires: texlive-antt = %{tl_version}
Requires: texlive-antp = %{tl_version}
Requires: texlive-iwona = %{tl_version}
Requires: texlive-kurier = %{tl_version}
Requires: texlive-txfonts = %{tl_version}
Requires: texlive-pxfonts = %{tl_version}
Requires: texlive-mptopdf = %{tl_version}
Requires: texlive-xetex = %{tl_version}
Provides: tex(context) = %{tl_version}
Obsoletes: texlive-context < %{tl_version}
Obsoletes: texlive-texmf-context < %{tl_version}

%description scheme-context
This is the TeX Live scheme for installing ConTeXt.

%package collection-context
Summary: ConTeXt format
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18549%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-context = %{tl_version}
Requires: texlive-jmn = %{tl_version}
Requires: texlive-lmextra = %{tl_version}
Requires: texlive-context-account = %{tl_version}
Requires: texlive-context-algorithmic = %{tl_version}
Requires: texlive-context-bnf = %{tl_version}
Requires: texlive-context-chromato = %{tl_version}
Requires: texlive-context-construction-plan = %{tl_version}
Requires: texlive-context-degrade = %{tl_version}
Requires: texlive-context-fixme = %{tl_version}
Requires: texlive-context-french = %{tl_version}
Requires: texlive-context-fullpage = %{tl_version}
Requires: texlive-context-games = %{tl_version}
Requires: texlive-context-gnuplot = %{tl_version}
Requires: texlive-context-letter = %{tl_version}
Requires: texlive-context-lettrine = %{tl_version}
Requires: texlive-context-lilypond = %{tl_version}
Requires: texlive-context-notes-zh-cn-doc = %{tl_version}
Requires: texlive-context-ruby = %{tl_version}
Requires: texlive-context-simplefonts = %{tl_version}
Requires: texlive-context-simpleslides = %{tl_version}
Requires: texlive-context-top-ten-doc = %{tl_version}
Requires: texlive-context-typearea = %{tl_version}
Requires: texlive-context-typescripts = %{tl_version}
Requires: texlive-context-vim = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-context
Hans Hagen's powerful ConTeXt system, http://pragma-ade.com.
Also includes third-party ConTeXt packages.

%package metapost-bin
Summary: Binaries for metapost
Version: %{tl_version}
Release: %{tl_release}.svn18765%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-metapost  = %{tl_version}

%description metapost-bin
Binaries for metapost

%package xetex-bin
Summary: Binaries for xetex
Version: %{tl_version}
Release: %{tl_release}.svn19405%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-xetex  = %{tl_version}
Requires: teckit
Provides: xdvipdfmx = %{version}-%{release}
Obsoletes: xdvipdfmx < %{version}-%{release}

%description xetex-bin
Binaries for xetex

%package context-bin
Summary: Binaries for context
Version: %{tl_version}
Release: %{tl_release}.svn18902%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-context  = %{tl_version}

%description context-bin
Binaries for context

%package collection-metapost
Summary: MetaPost (and Metafont) drawing packages
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15388%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-automata = %{tl_version}
Requires: texlive-bbcard = %{tl_version}
Requires: texlive-blockdraw_mp = %{tl_version}
Requires: texlive-bpolynomial = %{tl_version}
Requires: texlive-cmarrows = %{tl_version}
Requires: texlive-drv = %{tl_version}
Requires: texlive-dviincl = %{tl_version}
Requires: texlive-emp = %{tl_version}
Requires: texlive-epsincl = %{tl_version}
Requires: texlive-expressg = %{tl_version}
Requires: texlive-exteps = %{tl_version}
Requires: texlive-featpost = %{tl_version}
Requires: texlive-feynmf = %{tl_version}
Requires: texlive-garrigues = %{tl_version}
Requires: texlive-hatching = %{tl_version}
Requires: texlive-latexmp = %{tl_version}
Requires: texlive-metago = %{tl_version}
Requires: texlive-metaobj = %{tl_version}
Requires: texlive-metaplot = %{tl_version}
Requires: texlive-metapost = %{tl_version}
Requires: texlive-metauml = %{tl_version}
Requires: texlive-mfpic = %{tl_version}
Requires: texlive-mfpic4ode = %{tl_version}
Requires: texlive-mpattern = %{tl_version}
Requires: texlive-piechartmp = %{tl_version}
Requires: texlive-roex = %{tl_version}
Requires: texlive-slideshow = %{tl_version}
Requires: texlive-splines = %{tl_version}
Requires: texlive-suanpan = %{tl_version}
Requires: texlive-textpath = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-metapost
collection-metapost package

%package scheme-full
Summary: full scheme (everything)
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19112%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}
Requires: texlive-collection-bibtexextra = %{tl_version}
Requires: texlive-collection-binextra = %{tl_version}
Requires: texlive-collection-context = %{tl_version}
Requires: texlive-collection-documentation-arabic = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}
Requires: texlive-collection-documentation-bulgarian = %{tl_version}
Requires: texlive-collection-documentation-chinese = %{tl_version}
Requires: texlive-collection-documentation-czechslovak = %{tl_version}
Requires: texlive-collection-documentation-dutch = %{tl_version}
Requires: texlive-collection-documentation-english = %{tl_version}
Requires: texlive-collection-documentation-finnish = %{tl_version}
Requires: texlive-collection-documentation-french = %{tl_version}
Requires: texlive-collection-documentation-german = %{tl_version}
Requires: texlive-collection-documentation-italian = %{tl_version}
Requires: texlive-collection-documentation-japanese = %{tl_version}
Requires: texlive-collection-documentation-korean = %{tl_version}
Requires: texlive-collection-documentation-mongolian = %{tl_version}
Requires: texlive-collection-documentation-polish = %{tl_version}
Requires: texlive-collection-documentation-portuguese = %{tl_version}
Requires: texlive-collection-documentation-russian = %{tl_version}
Requires: texlive-collection-documentation-serbian = %{tl_version}
Requires: texlive-collection-documentation-slovenian = %{tl_version}
Requires: texlive-collection-documentation-spanish = %{tl_version}
Requires: texlive-collection-documentation-thai = %{tl_version}
Requires: texlive-collection-documentation-turkish = %{tl_version}
Requires: texlive-collection-documentation-ukrainian = %{tl_version}
Requires: texlive-collection-documentation-vietnamese = %{tl_version}
Requires: texlive-collection-fontsextra = %{tl_version}
Requires: texlive-collection-fontsrecommended = %{tl_version}
Requires: texlive-collection-fontutils = %{tl_version}
Requires: texlive-collection-formatsextra = %{tl_version}
Requires: texlive-collection-games = %{tl_version}
Requires: texlive-collection-genericextra = %{tl_version}
Requires: texlive-collection-genericrecommended = %{tl_version}
Requires: texlive-collection-htmlxml = %{tl_version}
Requires: texlive-collection-humanities = %{tl_version}
Requires: texlive-collection-langafrican = %{tl_version}
Requires: texlive-collection-langarabic = %{tl_version}
Requires: texlive-collection-langarmenian = %{tl_version}
Requires: texlive-collection-langcjk = %{tl_version}
Requires: texlive-collection-langcroatian = %{tl_version}
Requires: texlive-collection-langcyrillic = %{tl_version}
Requires: texlive-collection-langczechslovak = %{tl_version}
Requires: texlive-collection-langdanish = %{tl_version}
Requires: texlive-collection-langdutch = %{tl_version}
Requires: texlive-collection-langfinnish = %{tl_version}
Requires: texlive-collection-langfrench = %{tl_version}
Requires: texlive-collection-langgerman = %{tl_version}
Requires: texlive-collection-langgreek = %{tl_version}
Requires: texlive-collection-langhebrew = %{tl_version}
Requires: texlive-collection-langhungarian = %{tl_version}
Requires: texlive-collection-langindic = %{tl_version}
Requires: texlive-collection-langitalian = %{tl_version}
Requires: texlive-collection-langlatin = %{tl_version}
Requires: texlive-collection-langlatvian = %{tl_version}
Requires: texlive-collection-langlithuanian = %{tl_version}
Requires: texlive-collection-langmongolian = %{tl_version}
Requires: texlive-collection-langnorwegian = %{tl_version}
Requires: texlive-collection-langother = %{tl_version}
Requires: texlive-collection-langpolish = %{tl_version}
Requires: texlive-collection-langportuguese = %{tl_version}
Requires: texlive-collection-langspanish = %{tl_version}
Requires: texlive-collection-langswedish = %{tl_version}
Requires: texlive-collection-langtibetan = %{tl_version}
Requires: texlive-collection-langturkmen = %{tl_version}
Requires: texlive-collection-langenglish = %{tl_version}
Requires: texlive-collection-langvietnamese = %{tl_version}
Requires: texlive-collection-latex = %{tl_version}
Requires: texlive-collection-latex3 = %{tl_version}
Requires: texlive-collection-latexextra = %{tl_version}
Requires: texlive-collection-latexrecommended = %{tl_version}
Requires: texlive-collection-luatex = %{tl_version}
Requires: texlive-collection-mathextra = %{tl_version}
Requires: texlive-collection-metapost = %{tl_version}
Requires: texlive-collection-music = %{tl_version}
Requires: texlive-collection-omega = %{tl_version}
Requires: texlive-collection-pictures = %{tl_version}
Requires: texlive-collection-plainextra = %{tl_version}
Requires: texlive-collection-pstricks = %{tl_version}
Requires: texlive-collection-publishers = %{tl_version}
Requires: texlive-collection-science = %{tl_version}
Requires: texlive-collection-texinfo = %{tl_version}
Requires: texlive-collection-xetex = %{tl_version}

%description scheme-full
This is the full TeX Live scheme: it installs everything
available.

%package collection-bibtexextra
Summary: Extra BibTeX styles
Version: %{tl_version}
Release: %{tl_noarch_release}.svn17995%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-aichej = %{tl_version}
Requires: texlive-amsrefs = %{tl_version}
Requires: texlive-apacite = %{tl_version}
Requires: texlive-apalike2 = %{tl_version}
Requires: texlive-beebe = %{tl_version}
Requires: texlive-bibarts = %{tl_version}
Requires: texlive-bibexport = %{tl_version}
Requires: texlive-bibhtml = %{tl_version}
Requires: texlive-biblatex = %{tl_version}
Requires: texlive-biblatex-apa = %{tl_version}
Requires: texlive-biblatex-chem = %{tl_version}
Requires: texlive-biblatex-chicago-notes-df = %{tl_version}
Requires: texlive-biblatex-dw = %{tl_version}
Requires: texlive-biblatex-historian = %{tl_version}
Requires: texlive-biblatex-nature = %{tl_version}
Requires: texlive-biblatex-philosophy = %{tl_version}
Requires: texlive-biblatex-science = %{tl_version}
Requires: texlive-biblist = %{tl_version}
Requires: texlive-bibtopic = %{tl_version}
Requires: texlive-bibtopicprefix = %{tl_version}
Requires: texlive-bibunits = %{tl_version}
Requires: texlive-cell = %{tl_version}
Requires: texlive-chbibref = %{tl_version}
Requires: texlive-chicago = %{tl_version}
Requires: texlive-chicago-annote = %{tl_version}
Requires: texlive-chembst = %{tl_version}
Requires: texlive-collref = %{tl_version}
Requires: texlive-compactbib = %{tl_version}
Requires: texlive-custom-bib = %{tl_version}
Requires: texlive-din1505 = %{tl_version}
Requires: texlive-dk-bib = %{tl_version}
Requires: texlive-doipubmed = %{tl_version}
Requires: texlive-elsevier-bib = %{tl_version}
Requires: texlive-fbs = %{tl_version}
Requires: texlive-figbib = %{tl_version}
Requires: texlive-footbib = %{tl_version}
Requires: texlive-harvard = %{tl_version}
Requires: texlive-harvmac = %{tl_version}
Requires: texlive-historische-zeitschrift = %{tl_version}
Requires: texlive-ijqc = %{tl_version}
Requires: texlive-inlinebib = %{tl_version}
Requires: texlive-iopart-num = %{tl_version}
Requires: texlive-jneurosci = %{tl_version}
Requires: texlive-jurabib = %{tl_version}
Requires: texlive-listbib = %{tl_version}
Requires: texlive-margbib = %{tl_version}
Requires: texlive-multibib = %{tl_version}
Requires: texlive-munich = %{tl_version}
Requires: texlive-notes2bib = %{tl_version}
Requires: texlive-perception = %{tl_version}
Requires: texlive-pnas2009 = %{tl_version}
Requires: texlive-rsc = %{tl_version}
Requires: texlive-sort-by-letters = %{tl_version}
Requires: texlive-splitbib = %{tl_version}
Requires: texlive-urlbst = %{tl_version}
Requires: texlive-collection-latex = %{tl_version}

%description collection-bibtexextra
Additional BibTeX styles and bibliography databases, including
BibLaTeX.

%package bibexport-bin
Summary: Binaries for bibexport
Version: %{tl_version}
Release: %{tl_release}.svn16219%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-bibexport  = %{tl_version}

%description bibexport-bin
Binaries for bibexport

%package collection-binextra
Summary: TeX auxiliary programs
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18336%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}
Requires: texlive-a2ping = %{tl_version}
Requires: texlive-bibtex8 = %{tl_version}
Requires: texlive-bibtexu = %{tl_version}
Requires: texlive-bundledoc = %{tl_version}
Requires: texlive-chktex = %{tl_version}
Requires: texlive-ctie = %{tl_version}
Requires: texlive-cweb = %{tl_version}
Requires: texlive-de-macro = %{tl_version}
Requires: texlive-detex = %{tl_version}
Requires: texlive-dtl = %{tl_version}
Requires: texlive-dvi2tty = %{tl_version}
Requires: texlive-dviasm = %{tl_version}
Requires: texlive-dvicopy = %{tl_version}
Requires: texlive-dviljk = %{tl_version}
Requires: texlive-dvipng = %{tl_version}
Requires: texlive-dvipos = %{tl_version}
Requires: texlive-dvisvgm = %{tl_version}
Requires: texlive-findhyph = %{tl_version}
Requires: texlive-fragmaster = %{tl_version}
Requires: texlive-hyphenex = %{tl_version}
Requires: texlive-latex2man = %{tl_version}
Requires: texlive-latexdiff = %{tl_version}
Requires: texlive-latexmk = %{tl_version}
Requires: texlive-listings-ext = %{tl_version}
Requires: texlive-patgen = %{tl_version}
Requires: texlive-pdfcrop = %{tl_version}
Requires: texlive-pdfjam = %{tl_version}
Requires: texlive-pdftools = %{tl_version}
Requires: texlive-pkfix = %{tl_version}
Requires: texlive-pkfix-helper = %{tl_version}
Requires: texlive-purifyeps = %{tl_version}
Requires: texlive-seetexk = %{tl_version}
Requires: texlive-synctex = %{tl_version}
Requires: texlive-texcount = %{tl_version}
Requires: texlive-texdoc = %{tl_version}
Requires: texlive-texloganalyser = %{tl_version}
Requires: texlive-texware = %{tl_version}
Requires: texlive-tie = %{tl_version}
Requires: texlive-tpic2pdftex = %{tl_version}
Requires: texlive-web = %{tl_version}
Obsoletes: texlive-utils < %{tl_version}
Requires: dvipng

%description collection-binextra
Various useful, but non-essential, support programs. Includes
programs and macros for DVI file manipulation, literate
programming, patgen, and the TeX Works Editor.

%package a2ping-bin
Summary: Binaries for a2ping
Version: %{tl_version}
Release: %{tl_release}.svn6834%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-a2ping  = %{tl_version}

%description a2ping-bin
Binaries for a2ping

%package bibtex8-bin
Summary: Binaries for bibtex8
Version: %{tl_version}
Release: %{tl_release}.svn18765%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-bibtex8  = %{tl_version}

%description bibtex8-bin
Binaries for bibtex8

%package bibtexu-bin
Summary: Binaries for bibtexu
Version: %{tl_version}
Release: %{tl_release}.svn18765%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-bibtexu  = %{tl_version}

%description bibtexu-bin
Binaries for bibtexu

%package bundledoc-bin
Summary: Binaries for bundledoc
Version: %{tl_version}
Release: %{tl_release}.svn17794%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-bundledoc  = %{tl_version}

%description bundledoc-bin
Binaries for bundledoc

%package chktex-bin
Summary: Binaries for chktex
Version: %{tl_version}
Release: %{tl_release}.svn19008%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-chktex  = %{tl_version}

%description chktex-bin
Binaries for chktex

%package ctie-bin
Summary: Binaries for ctie
Version: %{tl_version}
Release: %{tl_release}.svn18765%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-ctie  = %{tl_version}

%description ctie-bin
Binaries for ctie

%package cweb-bin
Summary: Binaries for cweb
Version: %{tl_version}
Release: %{tl_release}.svn18765%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-cweb  = %{tl_version}

%description cweb-bin
Binaries for cweb

%package de-macro-bin
Summary: Binaries for de-macro
Version: %{tl_version}
Release: %{tl_release}.svn17399%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-de-macro  = %{tl_version}

%description de-macro-bin
Binaries for de-macro

%package detex-bin
Summary: Binaries for detex
Version: %{tl_version}
Release: %{tl_release}.svn19008%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-detex  = %{tl_version}

%description detex-bin
Binaries for detex

%package dtl-bin
Summary: Binaries for dtl
Version: %{tl_version}
Release: %{tl_release}.svn18336%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-dtl  = %{tl_version}

%description dtl-bin
Binaries for dtl

%package dvi2tty-bin
Summary: Binaries for dvi2tty
Version: %{tl_version}
Release: %{tl_release}.svn18336%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-dvi2tty  = %{tl_version}

%description dvi2tty-bin
Binaries for dvi2tty

%package dviasm-bin
Summary: Binaries for dviasm
Version: %{tl_version}
Release: %{tl_release}.svn8329%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-dviasm  = %{tl_version}

%description dviasm-bin
Binaries for dviasm

%package dvicopy-bin
Summary: Binaries for dvicopy
Version: %{tl_version}
Release: %{tl_release}.svn18765%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-dvicopy  = %{tl_version}

%description dvicopy-bin
Binaries for dvicopy

%package dviljk-bin
Summary: Binaries for dviljk
Version: %{tl_version}
Release: %{tl_release}.svn18765%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-dviljk  = %{tl_version}

%description dviljk-bin
Binaries for dviljk

%package dvipng-bin
Summary: Binaries for dvipng
Version: %{tl_version}
Release: %{tl_release}.svn18765%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-dvipng  = %{tl_version}
Provides: dvipng = %{tl_version}
Obsoletes: dvipng < %{tl_version}

%description dvipng-bin
Binaries for dvipng

%package dvipos-bin
Summary: Binaries for dvipos
Version: %{tl_version}
Release: %{tl_release}.svn18765%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-dvipos  = %{tl_version}

%description dvipos-bin
Binaries for dvipos

%package dvisvgm-bin
Summary: Binaries for dvisvgm
Version: %{tl_version}
Release: %{tl_release}.svn19405%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-dvisvgm  = %{tl_version}

%description dvisvgm-bin
Binaries for dvisvgm

%package findhyph-bin
Summary: Binaries for findhyph
Version: %{tl_version}
Release: %{tl_release}.svn14758%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-findhyph  = %{tl_version}

%description findhyph-bin
Binaries for findhyph

%package fragmaster-bin
Summary: Binaries for fragmaster
Version: %{tl_version}
Release: %{tl_release}.svn13663%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-fragmaster  = %{tl_version}

%description fragmaster-bin
Binaries for fragmaster

%package latex2man-bin
Summary: Binaries for latex2man
Version: %{tl_version}
Release: %{tl_release}.svn13663%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-latex2man  = %{tl_version}

%description latex2man-bin
Binaries for latex2man

%package latexdiff-bin
Summary: Binaries for latexdiff
Version: %{tl_version}
Release: %{tl_release}.svn16420%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-latexdiff  = %{tl_version}

%description latexdiff-bin
Binaries for latexdiff

%package latexmk-bin
Summary: Binaries for latexmk
Version: %{tl_version}
Release: %{tl_release}.svn10937%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-latexmk  = %{tl_version}

%description latexmk-bin
Binaries for latexmk

%package listings-ext-bin
Summary: Binaries for listings-ext
Version: %{tl_version}
Release: %{tl_release}.svn15093%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-listings-ext  = %{tl_version}

%description listings-ext-bin
Binaries for listings-ext

%package patgen-bin
Summary: Binaries for patgen
Version: %{tl_version}
Release: %{tl_release}.svn18765%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-patgen  = %{tl_version}

%description patgen-bin
Binaries for patgen

%package pdfcrop-bin
Summary: Binaries for pdfcrop
Version: %{tl_version}
Release: %{tl_release}.svn14387%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-pdfcrop  = %{tl_version}

%description pdfcrop-bin
Binaries for pdfcrop

%package pdfjam-bin
Summary: Binaries for pdfjam
Version: %{tl_version}
Release: %{tl_release}.svn17868%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-pdfjam  = %{tl_version}

%description pdfjam-bin
Binaries for pdfjam

%package pdftools-bin
Summary: Binaries for pdftools
Version: %{tl_version}
Release: %{tl_release}.svn18336%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-pdftools  = %{tl_version}

%description pdftools-bin
Binaries for pdftools

%package pkfix-bin
Summary: Binaries for pkfix
Version: %{tl_version}
Release: %{tl_release}.svn13364%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-pkfix  = %{tl_version}

%description pkfix-bin
Binaries for pkfix

%package pkfix-helper-bin
Summary: Binaries for pkfix-helper
Version: %{tl_version}
Release: %{tl_release}.svn13663%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-pkfix-helper  = %{tl_version}

%description pkfix-helper-bin
Binaries for pkfix-helper

%package purifyeps-bin
Summary: Binaries for purifyeps
Version: %{tl_version}
Release: %{tl_release}.svn13663%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-purifyeps  = %{tl_version}

%description purifyeps-bin
Binaries for purifyeps

%package seetexk-bin
Summary: Binaries for seetexk
Version: %{tl_version}
Release: %{tl_release}.svn18336%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-seetexk  = %{tl_version}

%description seetexk-bin
Binaries for seetexk

%package synctex-bin
Summary: Binaries for synctex
Version: %{tl_version}
Release: %{tl_release}.svn18336%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-synctex  = %{tl_version}

%description synctex-bin
Binaries for synctex

%package texcount-bin
Summary: Binaries for texcount
Version: %{tl_version}
Release: %{tl_release}.svn13013%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-texcount  = %{tl_version}

%description texcount-bin
Binaries for texcount

%package texdoc-bin
Summary: Binaries for texdoc
Version: %{tl_version}
Release: %{tl_release}.svn12518%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-texdoc  = %{tl_version}

%description texdoc-bin
Binaries for texdoc

%package texloganalyser-bin
Summary: Binaries for texloganalyser
Version: %{tl_version}
Release: %{tl_release}.svn13663%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-texloganalyser  = %{tl_version}

%description texloganalyser-bin
Binaries for texloganalyser

%package texware-bin
Summary: Binaries for texware
Version: %{tl_version}
Release: %{tl_release}.svn18765%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-texware  = %{tl_version}

%description texware-bin
Binaries for texware

%package tie-bin
Summary: Binaries for tie
Version: %{tl_version}
Release: %{tl_release}.svn18765%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-tie  = %{tl_version}

%description tie-bin
Binaries for tie

%package tpic2pdftex-bin
Summary: Binaries for tpic2pdftex
Version: %{tl_version}
Release: %{tl_release}.svn18336%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-tpic2pdftex  = %{tl_version}

%description tpic2pdftex-bin
Binaries for tpic2pdftex

%package web-bin
Summary: Binaries for web
Version: %{tl_version}
Release: %{tl_release}.svn18765%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-web  = %{tl_version}

%description web-bin
Binaries for web

%package collection-documentation-arabic
Summary: Arabic documentation
Version: %{tl_version}
Release: %{tl_noarch_release}.svn14327%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-lshort-persian-doc = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}

%description collection-documentation-arabic
collection-documentation-arabic package

%package collection-documentation-bulgarian
Summary: Bulgarian documentation
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19296%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-lshort-bulgarian-doc = %{tl_version}
Requires: texlive-pst-eucl-translation-bg-doc = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}

%description collection-documentation-bulgarian
collection-documentation-bulgarian package

%package collection-documentation-chinese
Summary: Chinese documentation
Version: %{tl_version}
Release: %{tl_noarch_release}.svn14384%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-asymptote-faq-zh-cn-doc = %{tl_version}
Requires: texlive-asymptote-by-example-zh-cn-doc = %{tl_version}
Requires: texlive-asymptote-manual-zh-cn-doc = %{tl_version}
Requires: texlive-ctex-faq-doc = %{tl_version}
Requires: texlive-latex-notes-zh-cn-doc = %{tl_version}
Requires: texlive-lshort-chinese-doc = %{tl_version}
Requires: texlive-texlive-zh-cn-doc = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}

%description collection-documentation-chinese
collection-documentation-chinese package

%package collection-documentation-czechslovak
Summary: Czech/Slovak documentation
Version: %{tl_version}
Release: %{tl_noarch_release}.svn14740%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-lshort-slovak-doc = %{tl_version}
Requires: texlive-texlive-cz-doc = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}

%description collection-documentation-czechslovak
collection-documentation-czechslovak package

%package collection-documentation-dutch
Summary: Dutch documentation
Version: %{tl_version}
Release: %{tl_noarch_release}.svn13822%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-lshort-dutch-doc = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}

%description collection-documentation-dutch
collection-documentation-dutch package

%package collection-documentation-english
Summary: English documentation
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18881%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-FAQ-en-doc = %{tl_version}
Requires: texlive-MemoirChapStyles-doc = %{tl_version}
Requires: texlive-Type1fonts-doc = %{tl_version}
Requires: texlive-amslatex-primer-doc = %{tl_version}
Requires: texlive-around-the-bend-doc = %{tl_version}
Requires: texlive-components-of-TeX-doc = %{tl_version}
Requires: texlive-comprehensive-doc = %{tl_version}
Requires: texlive-dtxtut-doc = %{tl_version}
Requires: texlive-first-latex-doc-doc = %{tl_version}
Requires: texlive-free-math-font-survey-doc = %{tl_version}
Requires: texlive-gentle-doc = %{tl_version}
Requires: texlive-guide-to-latex-doc = %{tl_version}
Requires: texlive-impatient-doc = %{tl_version}
Requires: texlive-intro-scientific-doc = %{tl_version}
Requires: texlive-knuth-doc = %{tl_version}
Requires: texlive-l2tabu-english-doc = %{tl_version}
Requires: texlive-latex2e-help-texinfo = %{tl_version}
Requires: texlive-latex-course-doc = %{tl_version}
Requires: texlive-latex-doc-ptr-doc = %{tl_version}
Requires: texlive-latex-graphics-companion-doc = %{tl_version}
Requires: texlive-latex-veryshortguide-doc = %{tl_version}
Requires: texlive-latex-web-companion-doc = %{tl_version}
Requires: texlive-latexcheat-doc = %{tl_version}
Requires: texlive-lshort-english-doc = %{tl_version}
Requires: texlive-mathmode-doc = %{tl_version}
Requires: texlive-memdesign-doc = %{tl_version}
Requires: texlive-metafont-beginners-doc = %{tl_version}
Requires: texlive-metapost-examples-doc = %{tl_version}
Requires: texlive-patgen2-tutorial-doc = %{tl_version}
Requires: texlive-pdf-forms-tutorial-en-doc = %{tl_version}
Requires: texlive-pstricks-tutorial-doc = %{tl_version}
Requires: texlive-svg-inkscape-doc = %{tl_version}
Requires: texlive-tamethebeast-doc = %{tl_version}
Requires: texlive-tds-doc = %{tl_version}
Requires: texlive-tex-font-errors-cheatsheet-doc = %{tl_version}
Requires: texlive-tex-refs-doc = %{tl_version}
Requires: texlive-texbytopic-doc = %{tl_version}
Requires: texlive-titlepages-doc = %{tl_version}
Requires: texlive-tlc2-doc = %{tl_version}
Requires: texlive-visualfaq-doc = %{tl_version}
Requires: texlive-webguide-doc = %{tl_version}
Requires: texlive-xetexref-doc = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}

%description collection-documentation-english
collection-documentation-english package

%package collection-documentation-finnish
Summary: Finnish documentation
Version: %{tl_version}
Release: %{tl_noarch_release}.svn13822%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-lshort-finnish-doc = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}

%description collection-documentation-finnish
collection-documentation-finnish package

%package collection-documentation-french
Summary: French documentation
Version: %{tl_version}
Release: %{tl_noarch_release}.svn17322%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-apprends-latex-doc = %{tl_version}
Requires: texlive-epslatex-fr-doc = %{tl_version}
Requires: texlive-impatient-fr-doc = %{tl_version}
Requires: texlive-l2tabu-french-doc = %{tl_version}
Requires: texlive-lshort-french-doc = %{tl_version}
Requires: texlive-texlive-fr-doc = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}

%description collection-documentation-french
collection-documentation-french package

%package collection-documentation-german
Summary: German documentation
Version: %{tl_version}
Release: %{tl_noarch_release}.svn16981%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kopka-doc = %{tl_version}
Requires: texlive-l2picfaq-doc = %{tl_version}
Requires: texlive-l2tabu-doc = %{tl_version}
Requires: texlive-latex-referenz-doc = %{tl_version}
Requires: texlive-latex-tabellen-doc = %{tl_version}
Requires: texlive-latex-tipps-und-tricks-doc = %{tl_version}
Requires: texlive-lshort-german-doc = %{tl_version}
Requires: texlive-pdf-forms-tutorial-de-doc = %{tl_version}
Requires: texlive-presentations-doc = %{tl_version}
Requires: texlive-templates-fenn-doc = %{tl_version}
Requires: texlive-templates-sommer-doc = %{tl_version}
Requires: texlive-texlive-de-doc = %{tl_version}
Requires: texlive-voss-de-doc = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}

%description collection-documentation-german
collection-documentation-german package

%package collection-documentation-italian
Summary: Italian documentation
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15708%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-amsldoc-it-doc = %{tl_version}
Requires: texlive-amsmath-it-doc = %{tl_version}
Requires: texlive-amsthdoc-it-doc = %{tl_version}
Requires: texlive-fancyhdr-it-doc = %{tl_version}
Requires: texlive-l2tabu-it-doc = %{tl_version}
Requires: texlive-lshort-italian-doc = %{tl_version}
Requires: texlive-psfrag-italian-doc = %{tl_version}
Requires: texlive-texlive-it-doc = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}

%description collection-documentation-italian
collection-documentation-italian package

%package collection-documentation-japanese
Summary: Japanese documentation
Version: %{tl_version}
Release: %{tl_noarch_release}.svn13822%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-lshort-japanese-doc = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}

%description collection-documentation-japanese
collection-documentation-japanese package

%package collection-documentation-korean
Summary: Korean documentation
Version: %{tl_version}
Release: %{tl_noarch_release}.svn13822%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-lshort-korean-doc = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}

%description collection-documentation-korean
collection-documentation-korean package

%package collection-documentation-mongolian
Summary: Mongolian documentation
Version: %{tl_version}
Release: %{tl_noarch_release}.svn13822%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-lshort-mongol-doc = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}

%description collection-documentation-mongolian
collection-documentation-mongolian package

%package collection-documentation-polish
Summary: Polish documentation
Version: %{tl_version}
Release: %{tl_noarch_release}.svn13822%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-lshort-polish-doc = %{tl_version}
Requires: texlive-tex-virtual-academy-pl-doc = %{tl_version}
Requires: texlive-texlive-pl-doc = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}

%description collection-documentation-polish
collection-documentation-polish package

%package collection-documentation-portuguese
Summary: Portuguese documentation
Version: %{tl_version}
Release: %{tl_noarch_release}.svn13822%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-beamer-tut-pt-doc = %{tl_version}
Requires: texlive-cursolatex-doc = %{tl_version}
Requires: texlive-latexcheat-ptbr-doc = %{tl_version}
Requires: texlive-lshort-portuguese-doc = %{tl_version}
Requires: texlive-xypic-tut-pt-doc = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}

%description collection-documentation-portuguese
collection-documentation-portuguese package

%package collection-documentation-russian
Summary: Russian documentation
Version: %{tl_version}
Release: %{tl_noarch_release}.svn13822%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-lshort-russian-doc = %{tl_version}
Requires: texlive-mpman-ru-doc = %{tl_version}
Requires: texlive-texlive-ru-doc = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}

%description collection-documentation-russian
collection-documentation-russian package

%package collection-documentation-serbian
Summary: Serbian documentation
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19112%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-texlive-sr-doc = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}

%description collection-documentation-serbian
collection-documentation-serbian package

%package collection-documentation-slovenian
Summary: Slovenian documentation
Version: %{tl_version}
Release: %{tl_noarch_release}.svn13822%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-lshort-slovenian-doc = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}

%description collection-documentation-slovenian
collection-documentation-slovenian package

%package collection-documentation-spanish
Summary: Spanish documentation
Version: %{tl_version}
Release: %{tl_noarch_release}.svn16564%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-es-tex-faq-doc = %{tl_version}
Requires: texlive-l2tabu-spanish-doc = %{tl_version}
Requires: texlive-latexcheat-esmx-doc = %{tl_version}
Requires: texlive-lshort-spanish-doc = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}

%description collection-documentation-spanish
collection-documentation-spanish package

%package collection-documentation-thai
Summary: Thai documentation
Version: %{tl_version}
Release: %{tl_noarch_release}.svn13822%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-lshort-thai-doc = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}

%description collection-documentation-thai
collection-documentation-thai package

%package collection-documentation-turkish
Summary: Turkish documentation
Version: %{tl_version}
Release: %{tl_noarch_release}.svn13822%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-lshort-turkish-doc = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}

%description collection-documentation-turkish
collection-documentation-turkish package

%package collection-documentation-ukrainian
Summary: Ukrainian documentation
Version: %{tl_version}
Release: %{tl_noarch_release}.svn13822%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-lshort-ukr-doc = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}

%description collection-documentation-ukrainian
collection-documentation-ukrainian package

%package collection-documentation-vietnamese
Summary: Vietnamese documentation
Version: %{tl_version}
Release: %{tl_noarch_release}.svn13822%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-amsldoc-vn-doc = %{tl_version}
Requires: texlive-lshort-vietnamese-doc = %{tl_version}
Requires: texlive-ntheorem-vn-doc = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}

%description collection-documentation-vietnamese
collection-documentation-vietnamese package

%package collection-fontsextra
Summary: Extra fonts
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19491%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-asana-math = %{tl_version}
Requires: texlive-allrunes = %{tl_version}
Requires: texlive-antiqua = %{tl_version}
Requires: texlive-antp = %{tl_version}
Requires: texlive-antt = %{tl_version}
Requires: texlive-ar = %{tl_version}
Requires: texlive-archaic = %{tl_version}
Requires: texlive-arev = %{tl_version}
Requires: texlive-ascii = %{tl_version}
Requires: texlive-astro = %{tl_version}
Requires: texlive-augie = %{tl_version}
Requires: texlive-auncial-new = %{tl_version}
Requires: texlive-aurical = %{tl_version}
Requires: texlive-barcodes = %{tl_version}
Requires: texlive-baskervald = %{tl_version}
Requires: texlive-bayer = %{tl_version}
Requires: texlive-bbding = %{tl_version}
Requires: texlive-bbm = %{tl_version}
Requires: texlive-bbm-macros = %{tl_version}
Requires: texlive-bbold = %{tl_version}
Requires: texlive-belleek = %{tl_version}
Requires: texlive-bera = %{tl_version}
Requires: texlive-blacklettert1 = %{tl_version}
Requires: texlive-boisik = %{tl_version}
Requires: texlive-bookhands = %{tl_version}
Requires: texlive-braille = %{tl_version}
Requires: texlive-brushscr = %{tl_version}
Requires: texlive-calligra = %{tl_version}
Requires: texlive-carolmin-ps = %{tl_version}
Requires: texlive-ccicons = %{tl_version}
Requires: texlive-cfr-lm = %{tl_version}
Requires: texlive-cm-lgc = %{tl_version}
Requires: texlive-cm-unicode = %{tl_version}
Requires: texlive-cmbright = %{tl_version}
Requires: texlive-cmll = %{tl_version}
Requires: texlive-cmpica = %{tl_version}
Requires: texlive-concmath-fonts = %{tl_version}
Requires: texlive-courier-scaled = %{tl_version}
Requires: texlive-cryst = %{tl_version}
Requires: texlive-cyklop = %{tl_version}
Requires: texlive-dancers = %{tl_version}
Requires: texlive-dice = %{tl_version}
Requires: texlive-dictsym = %{tl_version}
Requires: texlive-dingbat = %{tl_version}
Requires: texlive-doublestroke = %{tl_version}
Requires: texlive-dozenal = %{tl_version}
Requires: texlive-duerer-latex = %{tl_version}
Requires: texlive-ean = %{tl_version}
Requires: texlive-ecc = %{tl_version}
Requires: texlive-eco = %{tl_version}
Requires: texlive-eiad-ltx = %{tl_version}
Requires: texlive-elvish = %{tl_version}
Requires: texlive-epigrafica = %{tl_version}
Requires: texlive-epsdice = %{tl_version}
Requires: texlive-esvect = %{tl_version}
Requires: texlive-eulervm = %{tl_version}
Requires: texlive-euxm = %{tl_version}
Requires: texlive-feyn = %{tl_version}
Requires: texlive-fge = %{tl_version}
Requires: texlive-foekfont = %{tl_version}
Requires: texlive-fonetika = %{tl_version}
Requires: texlive-fourier = %{tl_version}
Requires: texlive-fouriernc = %{tl_version}
Requires: texlive-frcursive = %{tl_version}
Requires: texlive-genealogy = %{tl_version}
Requires: texlive-gentium = %{tl_version}
Requires: texlive-gfsartemisia = %{tl_version}
Requires: texlive-gfsbodoni = %{tl_version}
Requires: texlive-gfscomplutum = %{tl_version}
Requires: texlive-gfsdidot = %{tl_version}
Requires: texlive-gfsneohellenic = %{tl_version}
Requires: texlive-gfssolomos = %{tl_version}
Requires: texlive-gnu-freefont = %{tl_version}
Requires: texlive-gothic = %{tl_version}
Requires: texlive-greenpoint = %{tl_version}
Requires: texlive-groff = %{tl_version}
Requires: texlive-grotesq = %{tl_version}
Requires: texlive-hands = %{tl_version}
Requires: texlive-hfbright = %{tl_version}
Requires: texlive-hfoldsty = %{tl_version}
Requires: texlive-ifsym = %{tl_version}
Requires: texlive-inconsolata = %{tl_version}
Requires: texlive-initials = %{tl_version}
Requires: texlive-iwona = %{tl_version}
Requires: texlive-jablantile = %{tl_version}
Requires: texlive-junicode = %{tl_version}
Requires: texlive-kixfont = %{tl_version}
Requires: texlive-knuthotherfonts = %{tl_version}
Requires: texlive-kpfonts = %{tl_version}
Requires: texlive-kurier = %{tl_version}
Requires: texlive-lfb = %{tl_version}
Requires: texlive-libertine = %{tl_version}
Requires: texlive-libris = %{tl_version}
Requires: texlive-lineara = %{tl_version}
Requires: texlive-lxfonts = %{tl_version}
Requires: texlive-ly1 = %{tl_version}
Requires: texlive-mathabx = %{tl_version}
Requires: texlive-mathdesign = %{tl_version}
Requires: texlive-mnsymbol = %{tl_version}
Requires: texlive-nkarta = %{tl_version}
Requires: texlive-ocherokee = %{tl_version}
Requires: texlive-ogham = %{tl_version}
Requires: texlive-oinuit = %{tl_version}
Requires: texlive-oldlatin = %{tl_version}
Requires: texlive-oldstandard = %{tl_version}
Requires: texlive-orkhun = %{tl_version}
Requires: texlive-pacioli = %{tl_version}
Requires: texlive-pclnfss = %{tl_version}
Requires: texlive-phaistos = %{tl_version}
Requires: texlive-pigpen = %{tl_version}
Requires: texlive-psafm = %{tl_version}
Requires: texlive-punk = %{tl_version}
Requires: texlive-recycle = %{tl_version}
Requires: texlive-romande = %{tl_version}
Requires: texlive-sauter = %{tl_version}
Requires: texlive-sauterfonts = %{tl_version}
Requires: texlive-semaphor = %{tl_version}
Requires: texlive-skull = %{tl_version}
Requires: texlive-staves = %{tl_version}
Requires: texlive-stix = %{tl_version}
Requires: texlive-tapir = %{tl_version}
Requires: texlive-tengwarscript = %{tl_version}
Requires: texlive-tpslifonts = %{tl_version}
Requires: texlive-trajan = %{tl_version}
Requires: texlive-txfontsb = %{tl_version}
Requires: texlive-umtypewriter = %{tl_version}
Requires: texlive-universa = %{tl_version}
Requires: texlive-venturisadf = %{tl_version}
Requires: texlive-wsuipa = %{tl_version}
Requires: texlive-xits = %{tl_version}
Requires: texlive-yfonts = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-fontsextra
collection-fontsextra package

%package collection-fontsrecommended
Summary: Recommended fonts
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19478%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-avantgar = %{tl_version}
Requires: texlive-bookman = %{tl_version}
Requires: texlive-charter = %{tl_version}
Requires: texlive-cm-super = %{tl_version}
Requires: texlive-cmextra = %{tl_version}
Requires: texlive-courier = %{tl_version}
Requires: texlive-euro = %{tl_version}
Requires: texlive-euro-ce = %{tl_version}
Requires: texlive-eurofont = %{tl_version}
Requires: texlive-eurosans = %{tl_version}
Requires: texlive-eurosym = %{tl_version}
Requires: texlive-fpl = %{tl_version}
Requires: texlive-helvetic = %{tl_version}
Requires: texlive-lm = %{tl_version}
Requires: texlive-marvosym = %{tl_version}
Requires: texlive-mathpazo = %{tl_version}
Requires: texlive-ncntrsbk = %{tl_version}
Requires: texlive-palatino = %{tl_version}
Requires: texlive-pxfonts = %{tl_version}
Requires: texlive-rsfs = %{tl_version}
Requires: texlive-symbol = %{tl_version}
Requires: texlive-tex-gyre = %{tl_version}
Requires: texlive-times = %{tl_version}
Requires: texlive-tipa = %{tl_version}
Requires: texlive-txfonts = %{tl_version}
Requires: texlive-utopia = %{tl_version}
Requires: texlive-wasy = %{tl_version}
Requires: texlive-wasysym = %{tl_version}
Requires: texlive-zapfchan = %{tl_version}
Requires: texlive-zapfding = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}
Provides: tetex-fonts = 3.1-99
Obsoletes: tetex-fonts < 3.1-99
Provides: texlive-texmf-fonts = %{tl_version}
Obsoletes: texlive-texmf-fonts < %{tl_version}

%description collection-fontsrecommended
Recommended fonts, including the base 35 PostScript fonts,
Latin Modern, TeX Gyre, and T1 and other encoding support for
Computer Modern, in outline form.

%package collection-fontutils
Summary: TeX and Outline font utilities
Version: %{tl_version}
Release: %{tl_noarch_release}.svn16392%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}
Requires: texlive-accfonts = %{tl_version}
Requires: texlive-afm2pl = %{tl_version}
Requires: texlive-epstopdf = %{tl_version}
Requires: texlive-fontware = %{tl_version}
Requires: texlive-lcdftypetools = %{tl_version}
Requires: texlive-pstools = %{tl_version}
Requires: texlive-dvipsconfig = %{tl_version}
Requires: texlive-fontinst = %{tl_version}
Requires: texlive-fontools = %{tl_version}
Requires: texlive-ttfutils = %{tl_version}
Requires: t1utils, psutils, lcdf-typetools

%description collection-fontutils
Programs for conversion between font formats, testing fonts,
virtual fonts, .gf and .pk manipulation, mft, fontinst, etc.
Manipulating OpenType, TrueType, PostScript Type 1, etc.

%package accfonts-bin
Summary: Binaries for accfonts
Version: %{tl_version}
Release: %{tl_release}.svn12688%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-accfonts  = %{tl_version}

%description accfonts-bin
Binaries for accfonts

%package afm2pl-bin
Summary: Binaries for afm2pl
Version: %{tl_version}
Release: %{tl_release}.svn18765%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-afm2pl  = %{tl_version}

%description afm2pl-bin
Binaries for afm2pl

%package epstopdf-bin
Summary: Binaries for epstopdf
Version: %{tl_version}
Release: %{tl_release}.svn18336%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-epstopdf  = %{tl_version}

%description epstopdf-bin
Binaries for epstopdf

%package fontware-bin
Summary: Binaries for fontware
Version: %{tl_version}
Release: %{tl_release}.svn18765%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-fontware  = %{tl_version}

%description fontware-bin
Binaries for fontware

%package lcdftypetools-bin
Summary: Binaries for lcdftypetools
Version: %{tl_version}
Release: %{tl_release}.svn18765%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-lcdftypetools  = %{tl_version}
Provides: lcdf-typetools = %{tl_version}
Obsoletes: lcdf-typetools < %{tl_version}

%description lcdftypetools-bin
Binaries for lcdftypetools

%package pstools-bin
Summary: Binaries for pstools
Version: %{tl_version}
Release: %{tl_release}.svn14164%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-pstools  = %{tl_version}

%description pstools-bin
Binaries for pstools

%package fontinst-bin
Summary: Binaries for fontinst
Version: %{tl_version}
Release: %{tl_release}.svn10%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-fontinst  = %{tl_version}

%description fontinst-bin
Binaries for fontinst

%package fontools-bin
Summary: Binaries for fontools
Version: %{tl_version}
Release: %{tl_release}.svn12687%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-fontools  = %{tl_version}

%description fontools-bin
Binaries for fontools

%package ttfutils-bin
Summary: Binaries for ttfutils
Version: %{tl_version}
Release: %{tl_release}.svn18765%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-ttfutils  = %{tl_version}

%description ttfutils-bin
Binaries for ttfutils

%package collection-formatsextra
Summary: Extra formats
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18686%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-alatex = %{tl_version}
Requires: texlive-edmac = %{tl_version}
Requires: texlive-eplain = %{tl_version}
Requires: texlive-mltex = %{tl_version}
Requires: texlive-psizzl = %{tl_version}
Requires: texlive-startex = %{tl_version}
Requires: texlive-texsis = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-formatsextra
Collected TeX `formats', i.e., large-scale macro packages
designed to be dumped into .fmt files, other than most common
ones, such as latex and context.

%package eplain-bin
Summary: Binaries for eplain
Version: %{tl_version}
Release: %{tl_release}.svn3006%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-eplain  = %{tl_version}

%description eplain-bin
Binaries for eplain

%package mltex-bin
Summary: Binaries for mltex
Version: %{tl_version}
Release: %{tl_release}.svn3006%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-mltex  = %{tl_version}

%description mltex-bin
Binaries for mltex

%package texsis-bin
Summary: Binaries for texsis
Version: %{tl_version}
Release: %{tl_release}.svn3006%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-texsis  = %{tl_version}

%description texsis-bin
Binaries for texsis

%package collection-games
Summary: Games typesetting
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15166%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-chess = %{tl_version}
Requires: texlive-chess-problem-diagrams = %{tl_version}
Requires: texlive-chessboard = %{tl_version}
Requires: texlive-chessfss = %{tl_version}
Requires: texlive-crossword = %{tl_version}
Requires: texlive-crosswrd = %{tl_version}
Requires: texlive-egameps = %{tl_version}
Requires: texlive-go = %{tl_version}
Requires: texlive-hexgame = %{tl_version}
Requires: texlive-jeopardy = %{tl_version}
Requires: texlive-othello = %{tl_version}
Requires: texlive-psgo = %{tl_version}
Requires: texlive-sgame = %{tl_version}
Requires: texlive-skak = %{tl_version}
Requires: texlive-skaknew = %{tl_version}
Requires: texlive-sudoku = %{tl_version}
Requires: texlive-sudokubundle = %{tl_version}
Requires: texlive-xq = %{tl_version}
Requires: texlive-xskak = %{tl_version}
Requires: texlive-collection-latex = %{tl_version}

%description collection-games
Setups for typesetting various games, including chess.

%package collection-genericextra
Summary: Extra generic packages
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19036%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-abbr = %{tl_version}
Requires: texlive-abstyles = %{tl_version}
Requires: texlive-barr = %{tl_version}
Requires: texlive-c-pascal = %{tl_version}
Requires: texlive-colorsep = %{tl_version}
Requires: texlive-dinat = %{tl_version}
Requires: texlive-dirtree = %{tl_version}
Requires: texlive-eijkhout = %{tl_version}
Requires: texlive-encxvlna = %{tl_version}
Requires: texlive-fenixpar = %{tl_version}
Requires: texlive-fltpoint = %{tl_version}
Requires: texlive-iftex = %{tl_version}
Requires: texlive-insbox = %{tl_version}
Requires: texlive-librarian = %{tl_version}
Requires: texlive-mathdots = %{tl_version}
Requires: texlive-metatex = %{tl_version}
Requires: texlive-mftoeps = %{tl_version}
Requires: texlive-midnight = %{tl_version}
Requires: texlive-multi = %{tl_version}
Requires: texlive-ofs = %{tl_version}
Requires: texlive-pdf-trans = %{tl_version}
Requires: texlive-tabto-generic = %{tl_version}
Requires: texlive-texapi = %{tl_version}
Requires: texlive-vtex = %{tl_version}
Requires: texlive-xlop = %{tl_version}
Requires: texlive-yax = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-genericextra
Extra packages that work with multiple formats, typically both
TeX and LaTeX.

%package collection-genericrecommended
Summary: Recommended generic packages
Version: %{tl_version}
Release: %{tl_noarch_release}.svn16866%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-epsf = %{tl_version}
Requires: texlive-fontname = %{tl_version}
Requires: texlive-genmisc = %{tl_version}
Requires: texlive-multido = %{tl_version}
Requires: texlive-tex-ps = %{tl_version}
Requires: texlive-ulem = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-genericrecommended
Recommended packages that work with multiple formats.

%package collection-htmlxml
Summary: HTML/SGML/XML support
Version: %{tl_version}
Release: %{tl_noarch_release}.svn13822%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-jadetex = %{tl_version}
Requires: texlive-passivetex = %{tl_version}
Requires: texlive-tex4ht = %{tl_version}
Requires: texlive-xmlplay = %{tl_version}
Requires: texlive-xmltex = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}
Requires: texlive-collection-fontsrecommended = %{tl_version}
Requires: texlive-collection-latex = %{tl_version}

%description collection-htmlxml
Packages to convert LaTeX to XML/HTML, and typset XML/SGML

%package jadetex-bin
Summary: Binaries for jadetex
Version: %{tl_version}
Release: %{tl_release}.svn3006%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-jadetex  = %{tl_version}

%description jadetex-bin
Binaries for jadetex

%package tex4ht-bin
Summary: Binaries for tex4ht
Version: %{tl_version}
Release: %{tl_release}.svn18765%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-tex4ht  = %{tl_version}

%description tex4ht-bin
Binaries for tex4ht

%package xmltex-bin
Summary: Binaries for xmltex
Version: %{tl_version}
Release: %{tl_release}.svn3006%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-xmltex  = %{tl_version}
Provides: xmltex = %{tl_version}
Obsoletes: xmltex < %{tl_version}

%description xmltex-bin
Binaries for xmltex

%package collection-humanities
Summary: Humanities packages
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19344%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-alnumsec = %{tl_version}
Requires: texlive-arydshln = %{tl_version}
Requires: texlive-bibleref = %{tl_version}
Requires: texlive-covington = %{tl_version}
Requires: texlive-dramatist = %{tl_version}
Requires: texlive-ecltree = %{tl_version}
Requires: texlive-ednotes = %{tl_version}
Requires: texlive-gb4e = %{tl_version}
Requires: texlive-gmverse = %{tl_version}
Requires: texlive-jura = %{tl_version}
Requires: texlive-juraabbrev = %{tl_version}
Requires: texlive-juramisc = %{tl_version}
Requires: texlive-jurarsp = %{tl_version}
Requires: texlive-ledmac = %{tl_version}
Requires: texlive-lexikon = %{tl_version}
Requires: texlive-lineno = %{tl_version}
Requires: texlive-linguex = %{tl_version}
Requires: texlive-liturg = %{tl_version}
Requires: texlive-parallel = %{tl_version}
Requires: texlive-parrun = %{tl_version}
Requires: texlive-plari = %{tl_version}
Requires: texlive-play = %{tl_version}
Requires: texlive-poemscol = %{tl_version}
Requires: texlive-qobitree = %{tl_version}
Requires: texlive-qtree = %{tl_version}
Requires: texlive-rtklage = %{tl_version}
Requires: texlive-screenplay = %{tl_version}
Requires: texlive-sides = %{tl_version}
Requires: texlive-stage = %{tl_version}
Requires: texlive-verse = %{tl_version}
Requires: texlive-xyling = %{tl_version}
Requires: texlive-collection-latex = %{tl_version}

%description collection-humanities
Packages for law, linguistics, the social sciences, the
humanities, etc.

%package collection-langafrican
Summary: African scripts
Version: %{tl_version}
Release: %{tl_noarch_release}.svn14727%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-ethiop = %{tl_version}
Requires: texlive-ethiop-t1 = %{tl_version}
Requires: texlive-fc = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langafrican
Support for typesetting some African scripts

%package collection-langarabic
Summary: Arabic
Version: %{tl_version}
Release: %{tl_noarch_release}.svn17780%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-arabi = %{tl_version}
Requires: texlive-arabtex = %{tl_version}
Requires: texlive-bidi = %{tl_version}
Requires: texlive-hyphen-arabic = %{tl_version}
Requires: texlive-hyphen-farsi = %{tl_version}
Requires: texlive-persian-bib = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langarabic
Support for typesetting Arabic.

%package collection-langarmenian
Summary: Armenian
Version: %{tl_version}
Release: %{tl_noarch_release}.svn14727%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-armenian = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langarmenian
Support for typesetting Armenian.

%package collection-langcjk
Summary: Chinese, Japanese, Korean
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18686%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-adobemapping = %{tl_version}
Requires: texlive-arphic = %{tl_version}
Requires: texlive-c90 = %{tl_version}
Requires: texlive-cjk = %{tl_version}
Requires: texlive-cjkpunct = %{tl_version}
Requires: texlive-cjkutils = %{tl_version}
Requires: texlive-cns = %{tl_version}
Requires: texlive-ctex = %{tl_version}
Requires: texlive-dnp = %{tl_version}
Requires: texlive-garuda-c90 = %{tl_version}
Requires: texlive-hyphen-chinese = %{tl_version}
Requires: texlive-jsclasses = %{tl_version}
Requires: texlive-norasi-c90 = %{tl_version}
Requires: texlive-ptex = %{tl_version}
Requires: texlive-uhc = %{tl_version}
Requires: texlive-zhmetrics = %{tl_version}
Requires: texlive-zhspacing = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}
Requires: texlive-collection-documentation-chinese = %{tl_version}
Provides: tex(japanese) = %{tl_version}
Provides: tex(east-asian) = %{tl_version}
Obsoletes: texlive-east-asian < %{tl_version}
Obsoletes: texlive-texmf-east-asian < %{tl_version}

%description collection-langcjk
CJK (Chinese, Japanese, Korean) macros, fonts, documentation,
also Thai since there is some overlap in the fonts.

%package cjkutils-bin
Summary: Binaries for cjkutils
Version: %{tl_version}
Release: %{tl_release}.svn18765%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-cjkutils  = %{tl_version}

%description cjkutils-bin
Binaries for cjkutils

%package ptex-bin
Summary: Binaries for ptex
Version: %{tl_version}
Release: %{tl_release}.svn19008%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-ptex  = %{tl_version}

%description ptex-bin
Binaries for ptex

%package collection-langcroatian
Summary: Croatian
Version: %{tl_version}
Release: %{tl_noarch_release}.svn14727%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-hrlatex = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langcroatian
Support for typesetting Croatian.

%package collection-langcyrillic
Summary: Cyrillic
Version: %{tl_version}
Release: %{tl_noarch_release}.svn16705%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-cmcyr = %{tl_version}
Requires: texlive-cyrillic = %{tl_version}
Requires: texlive-cyrillic-bin = %{tl_version}
Requires: texlive-cyrplain = %{tl_version}
Requires: texlive-disser = %{tl_version}
Requires: texlive-eskd = %{tl_version}
Requires: texlive-eskdx = %{tl_version}
Requires: texlive-gost = %{tl_version}
Requires: texlive-lcyw = %{tl_version}
Requires: texlive-lh = %{tl_version}
Requires: texlive-lhcyr = %{tl_version}
Requires: texlive-ruhyphen = %{tl_version}
Requires: texlive-t2 = %{tl_version}
Requires: texlive-ukrhyph = %{tl_version}
Requires: texlive-hyphen-bulgarian = %{tl_version}
Requires: texlive-hyphen-russian = %{tl_version}
Requires: texlive-hyphen-ukrainian = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}
Requires: texlive-collection-latex = %{tl_version}

%description collection-langcyrillic
Support for typesetting Cyrillic.

%package cyrillic-bin-bin
Summary: Binaries for cyrillic-bin
Version: %{tl_version}
Release: %{tl_release}.svn10%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-cyrillic-bin  = %{tl_version}

%description cyrillic-bin-bin
Binaries for cyrillic-bin

%package collection-langczechslovak
Summary: Czech/Slovak
Version: %{tl_version}
Release: %{tl_noarch_release}.svn14727%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-cs = %{tl_version}
Requires: texlive-csbulletin = %{tl_version}
Requires: texlive-cslatex = %{tl_version}
Requires: texlive-csplain = %{tl_version}
Requires: texlive-vlna = %{tl_version}
Requires: texlive-hyphen-czech = %{tl_version}
Requires: texlive-hyphen-slovak = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}
Requires: texlive-collection-latex = %{tl_version}

%description collection-langczechslovak
Support for typesetting Czech/Slovak.

%package cslatex-bin
Summary: Binaries for cslatex
Version: %{tl_version}
Release: %{tl_release}.svn3006%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-cslatex  = %{tl_version}

%description cslatex-bin
Binaries for cslatex

%package csplain-bin
Summary: Binaries for csplain
Version: %{tl_version}
Release: %{tl_release}.svn3006%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-csplain  = %{tl_version}

%description csplain-bin
Binaries for csplain

%package vlna-bin
Summary: Binaries for vlna
Version: %{tl_version}
Release: %{tl_release}.svn18336%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-vlna  = %{tl_version}

%description vlna-bin
Binaries for vlna

%package collection-langdanish
Summary: Danish
Version: %{tl_version}
Release: %{tl_noarch_release}.svn14727%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-hyphen-danish = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langdanish
Support for typesetting Danish.

%package collection-langdutch
Summary: Dutch
Version: %{tl_version}
Release: %{tl_noarch_release}.svn14727%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-hyphen-dutch = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langdutch
Support for typesetting Dutch.

%package collection-langfinnish
Summary: Finnish
Version: %{tl_version}
Release: %{tl_noarch_release}.svn14727%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-finbib = %{tl_version}
Requires: texlive-hyphen-finnish = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langfinnish
Support for typesetting Finnish.

%package collection-langfrench
Summary: French
Version: %{tl_version}
Release: %{tl_noarch_release}.svn14727%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-aeguill = %{tl_version}
Requires: texlive-bib-fr = %{tl_version}
Requires: texlive-frenchle = %{tl_version}
Requires: texlive-frletter = %{tl_version}
Requires: texlive-mafr = %{tl_version}
Requires: texlive-tabvar = %{tl_version}
Requires: texlive-tdsfrmath = %{tl_version}
Requires: texlive-variations = %{tl_version}
Requires: texlive-hyphen-basque = %{tl_version}
Requires: texlive-hyphen-french = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langfrench
Support for typesetting French.

%package collection-langgerman
Summary: German
Version: %{tl_version}
Release: %{tl_noarch_release}.svn16731%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-dehyph-exptl = %{tl_version}
Requires: texlive-german = %{tl_version}
Requires: texlive-germkorr = %{tl_version}
Requires: texlive-kalender = %{tl_version}
Requires: texlive-r_und_s = %{tl_version}
Requires: texlive-umlaute = %{tl_version}
Requires: texlive-hyphen-german = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langgerman
Support for typesetting German.

%package collection-langgreek
Summary: Greek
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15748%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-betababel = %{tl_version}
Requires: texlive-bgreek = %{tl_version}
Requires: texlive-cbfonts = %{tl_version}
Requires: texlive-gfsbaskerville = %{tl_version}
Requires: texlive-gfsporson = %{tl_version}
Requires: texlive-greek-inputenc = %{tl_version}
Requires: texlive-greekdates = %{tl_version}
Requires: texlive-greektex = %{tl_version}
Requires: texlive-grverb = %{tl_version}
Requires: texlive-ibycus-babel = %{tl_version}
Requires: texlive-ibygrk = %{tl_version}
Requires: texlive-kerkis = %{tl_version}
Requires: texlive-mkgrkindex = %{tl_version}
Requires: texlive-teubner = %{tl_version}
Requires: texlive-xgreek = %{tl_version}
Requires: texlive-hyphen-greek = %{tl_version}
Requires: texlive-hyphen-ancientgreek = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langgreek
Support for typesetting Greek.

%package mkgrkindex-bin
Summary: Binaries for mkgrkindex
Version: %{tl_version}
Release: %{tl_release}.svn14428%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-mkgrkindex  = %{tl_version}

%description mkgrkindex-bin
Binaries for mkgrkindex

%package collection-langhebrew
Summary: Hebrew
Version: %{tl_version}
Release: %{tl_noarch_release}.svn14727%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-cjhebrew = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langhebrew
Support for typesetting Hebrew.

%package collection-langhungarian
Summary: Hungarian
Version: %{tl_version}
Release: %{tl_noarch_release}.svn14727%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-magyar-doc = %{tl_version}
Requires: texlive-hyphen-hungarian = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langhungarian
Support for typesetting Hungarian.

%package collection-langindic
Summary: Indic scripts
Version: %{tl_version}
Release: %{tl_noarch_release}.svn17578%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-bangtex = %{tl_version}
Requires: texlive-burmese = %{tl_version}
Requires: texlive-ebong = %{tl_version}
Requires: texlive-hyphen-indic = %{tl_version}
Requires: texlive-hyphen-sanskrit = %{tl_version}
Requires: texlive-itrans = %{tl_version}
Requires: texlive-malayalam = %{tl_version}
Requires: texlive-sanskrit = %{tl_version}
Requires: texlive-velthuis = %{tl_version}
Requires: texlive-wnri = %{tl_version}
Requires: texlive-devnag = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langindic
Support for typesetting some Indic scripts.

%package ebong-bin
Summary: Binaries for ebong
Version: %{tl_version}
Release: %{tl_release}.svn8576%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-ebong  = %{tl_version}

%description ebong-bin
Binaries for ebong

%package devnag-bin
Summary: Binaries for devnag
Version: %{tl_version}
Release: %{tl_release}.svn18336%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-devnag  = %{tl_version}

%description devnag-bin
Binaries for devnag

%package collection-langitalian
Summary: Italian
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19087%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}
Requires: texlive-hyphen-italian = %{tl_version}
Requires: texlive-frontespizio = %{tl_version}
Requires: texlive-itnumpar = %{tl_version}
Requires: texlive-layaureo = %{tl_version}

%description collection-langitalian
collection-langitalian package

%package collection-langlatin
Summary: Latin
Version: %{tl_version}
Release: %{tl_noarch_release}.svn14727%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-hyphen-latin = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langlatin
Support for typesetting Latin.

%package collection-langlatvian
Summary: Latvian
Version: %{tl_version}
Release: %{tl_noarch_release}.svn14727%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-hyphen-latvian = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langlatvian
Support for typesetting Latvian.

%package collection-langlithuanian
Summary: Lithuanian
Version: %{tl_version}
Release: %{tl_noarch_release}.svn14727%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-lithuanian = %{tl_version}
Requires: texlive-hyphen-lithuanian = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langlithuanian
Support for typesetting Lithuanian.

%package collection-langmongolian
Summary: Mongolian
Version: %{tl_version}
Release: %{tl_noarch_release}.svn14727%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}
Requires: texlive-hyphen-mongolian = %{tl_version}
Requires: texlive-mongolian-babel = %{tl_version}
Requires: texlive-montex = %{tl_version}

%description collection-langmongolian
Support for typesetting Mongolian.

%package collection-langnorwegian
Summary: Norwegian
Version: %{tl_version}
Release: %{tl_noarch_release}.svn14727%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-hyphen-norwegian = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langnorwegian
Support for typesetting Norwegian.

%package collection-langother
Summary: Other hyphenation files
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18620%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-hyphen-coptic = %{tl_version}
Requires: texlive-hyphen-esperanto = %{tl_version}
Requires: texlive-hyphen-estonian = %{tl_version}
Requires: texlive-hyphen-icelandic = %{tl_version}
Requires: texlive-hyphen-indonesian = %{tl_version}
Requires: texlive-hyphen-interlingua = %{tl_version}
Requires: texlive-hyphen-irish = %{tl_version}
Requires: texlive-hyphen-kurmanji = %{tl_version}
Requires: texlive-hyphen-romanian = %{tl_version}
Requires: texlive-hyphen-serbian = %{tl_version}
Requires: texlive-hyphen-slovenian = %{tl_version}
Requires: texlive-hyphen-uppersorbian = %{tl_version}
Requires: texlive-hyphen-welsh = %{tl_version}
Requires: texlive-hyphen-lao = %{tl_version}
Requires: texlive-hyphen-armenian = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langother
Hyphenation patterns for languages with no other support.

%package collection-langpolish
Summary: Polish
Version: %{tl_version}
Release: %{tl_noarch_release}.svn14727%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-cc-pl = %{tl_version}
Requires: texlive-gustlib = %{tl_version}
Requires: texlive-gustprog-doc = %{tl_version}
Requires: texlive-mex = %{tl_version}
Requires: texlive-mwcls = %{tl_version}
Requires: texlive-pl = %{tl_version}
Requires: texlive-polski = %{tl_version}
Requires: texlive-qpxqtx = %{tl_version}
Requires: texlive-tap = %{tl_version}
Requires: texlive-utf8mex = %{tl_version}
Requires: texlive-hyphen-polish = %{tl_version}
Requires: texlive-collection-latex = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langpolish
Support for typesetting Polish.

%package mex-bin
Summary: Binaries for mex
Version: %{tl_version}
Release: %{tl_release}.svn3006%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-mex  = %{tl_version}

%description mex-bin
Binaries for mex

%package collection-langportuguese
Summary: Portuguese
Version: %{tl_version}
Release: %{tl_noarch_release}.svn13822%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-ordinalpt = %{tl_version}
Requires: texlive-hyphen-portuguese = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langportuguese
collection-langportuguese package

%package collection-langspanish
Summary: Spanish
Version: %{tl_version}
Release: %{tl_noarch_release}.svn13822%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-hyphen-spanish = %{tl_version}
Requires: texlive-hyphen-catalan = %{tl_version}
Requires: texlive-hyphen-galician = %{tl_version}
Requires: texlive-spanish-doc = %{tl_version}
Requires: texlive-spanish-mx = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langspanish
collection-langspanish package

%package collection-langswedish
Summary: Swedish
Version: %{tl_version}
Release: %{tl_noarch_release}.svn14727%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-swebib = %{tl_version}
Requires: texlive-hyphen-swedish = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langswedish
Support for typesetting Swedish.

%package collection-langtibetan
Summary: Tibetan
Version: %{tl_version}
Release: %{tl_noarch_release}.svn14727%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-ctib = %{tl_version}
Requires: texlive-otibet = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langtibetan
Support for typesetting Tibetan.

%package collection-langturkmen
Summary: Turkmen
Version: %{tl_version}
Release: %{tl_noarch_release}.svn17578%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-turkmen = %{tl_version}
Requires: texlive-hyphen-turkmen = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langturkmen
Support for typesetting Turkmen.

%package collection-langenglish
Summary: US and UK English
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18615%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-hyphen-english = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langenglish
Support for typesetting US and UK English.

%package collection-langvietnamese
Summary: Vietnamese
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15272%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-vntex = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-langvietnamese
Support for typesetting Vietnamese.

%package collection-latex3
Summary: LaTeX3 packages
Version: %{tl_version}
Release: %{tl_noarch_release}.svn16052%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-expl3 = %{tl_version}
Requires: texlive-mh = %{tl_version}
Requires: texlive-xpackages = %{tl_version}
Requires: texlive-collection-latex = %{tl_version}

%description collection-latex3
collection-latex3 package

%package collection-latexextra
Summary: LaTeX supplementary packages
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19538%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-collection-latex = %{tl_version}
Requires: texlive-collection-pictures = %{tl_version}
Requires: texlive-2up = %{tl_version}
Requires: texlive-AkkTeX = %{tl_version}
Requires: texlive-ESIEEcv = %{tl_version}
Requires: texlive-HA-prosper = %{tl_version}
Requires: texlive-Tabbing = %{tl_version}
Requires: texlive-a0poster = %{tl_version}
Requires: texlive-a5comb = %{tl_version}
Requires: texlive-abstract = %{tl_version}
Requires: texlive-achemso = %{tl_version}
Requires: texlive-acromake = %{tl_version}
Requires: texlive-acronym = %{tl_version}
Requires: texlive-addlines = %{tl_version}
Requires: texlive-adrconv = %{tl_version}
Requires: texlive-akletter = %{tl_version}
Requires: texlive-alterqcm = %{tl_version}
Requires: texlive-altfont = %{tl_version}
Requires: texlive-amsaddr = %{tl_version}
Requires: texlive-animate = %{tl_version}
Requires: texlive-anonchap = %{tl_version}
Requires: texlive-answers = %{tl_version}
Requires: texlive-anyfontsize = %{tl_version}
Requires: texlive-appendix = %{tl_version}
Requires: texlive-arcs = %{tl_version}
Requires: texlive-arrayjobx = %{tl_version}
Requires: texlive-assignment = %{tl_version}
Requires: texlive-attachfile = %{tl_version}
Requires: texlive-authoraftertitle = %{tl_version}
Requires: texlive-authorindex = %{tl_version}
Requires: texlive-background = %{tl_version}
Requires: texlive-beamer-contrib = %{tl_version}
Requires: texlive-beamerposter = %{tl_version}
Requires: texlive-begriff = %{tl_version}
Requires: texlive-beton = %{tl_version}
Requires: texlive-bez123 = %{tl_version}
Requires: texlive-bezos = %{tl_version}
Requires: texlive-bigfoot = %{tl_version}
Requires: texlive-bigints = %{tl_version}
Requires: texlive-bizcard = %{tl_version}
Requires: texlive-blindtext = %{tl_version}
Requires: texlive-blkarray = %{tl_version}
Requires: texlive-block = %{tl_version}
Requires: texlive-blowup = %{tl_version}
Requires: texlive-boites = %{tl_version}
Requires: texlive-bold-extra = %{tl_version}
Requires: texlive-bookest = %{tl_version}
Requires: texlive-booklet = %{tl_version}
Requires: texlive-boolexpr = %{tl_version}
Requires: texlive-bophook = %{tl_version}
Requires: texlive-boxedminipage = %{tl_version}
Requires: texlive-boxhandler = %{tl_version}
Requires: texlive-bracketkey = %{tl_version}
Requires: texlive-braket = %{tl_version}
Requires: texlive-breakurl = %{tl_version}
Requires: texlive-bullcntr = %{tl_version}
Requires: texlive-bussproofs = %{tl_version}
Requires: texlive-calctab = %{tl_version}
Requires: texlive-calrsfs = %{tl_version}
Requires: texlive-calxxxx = %{tl_version}
Requires: texlive-cancel = %{tl_version}
Requires: texlive-capt-of = %{tl_version}
Requires: texlive-captcont = %{tl_version}
Requires: texlive-captdef = %{tl_version}
Requires: texlive-cases = %{tl_version}
Requires: texlive-casyl = %{tl_version}
Requires: texlive-catechis = %{tl_version}
Requires: texlive-cbcoptic = %{tl_version}
Requires: texlive-ccaption = %{tl_version}
Requires: texlive-cclicenses = %{tl_version}
Requires: texlive-cd = %{tl_version}
Requires: texlive-cd-cover = %{tl_version}
Requires: texlive-cdpbundl = %{tl_version}
Requires: texlive-cellspace = %{tl_version}
Requires: texlive-changebar = %{tl_version}
Requires: texlive-changelayout = %{tl_version}
Requires: texlive-changepage = %{tl_version}
Requires: texlive-changes = %{tl_version}
Requires: texlive-chappg = %{tl_version}
Requires: texlive-chapterfolder = %{tl_version}
Requires: texlive-chletter = %{tl_version}
Requires: texlive-chngcntr = %{tl_version}
Requires: texlive-chronology = %{tl_version}
Requires: texlive-circ = %{tl_version}
Requires: texlive-clefval = %{tl_version}
Requires: texlive-cleveref = %{tl_version}
Requires: texlive-clock = %{tl_version}
Requires: texlive-cmdstring = %{tl_version}
Requires: texlive-cmdtrack = %{tl_version}
Requires: texlive-cmsd = %{tl_version}
Requires: texlive-codedoc = %{tl_version}
Requires: texlive-colordoc = %{tl_version}
Requires: texlive-colorinfo = %{tl_version}
Requires: texlive-colortab = %{tl_version}
Requires: texlive-colorwav = %{tl_version}
Requires: texlive-combelow = %{tl_version}
Requires: texlive-combine = %{tl_version}
Requires: texlive-comma = %{tl_version}
Requires: texlive-comment = %{tl_version}
Requires: texlive-concprog = %{tl_version}
Requires: texlive-constants = %{tl_version}
Requires: texlive-contour = %{tl_version}
Requires: texlive-cooking = %{tl_version}
Requires: texlive-cookybooky = %{tl_version}
Requires: texlive-cool = %{tl_version}
Requires: texlive-coollist = %{tl_version}
Requires: texlive-coolstr = %{tl_version}
Requires: texlive-cooltooltips = %{tl_version}
Requires: texlive-coordsys = %{tl_version}
Requires: texlive-courseoutline = %{tl_version}
Requires: texlive-coursepaper = %{tl_version}
Requires: texlive-coverpage = %{tl_version}
Requires: texlive-crossreference = %{tl_version}
Requires: texlive-csquotes = %{tl_version}
Requires: texlive-csvtools = %{tl_version}
Requires: texlive-cuisine = %{tl_version}
Requires: texlive-currfile = %{tl_version}
Requires: texlive-currvita = %{tl_version}
Requires: texlive-cv = %{tl_version}
Requires: texlive-cweb-latex = %{tl_version}
Requires: texlive-dashbox = %{tl_version}
Requires: texlive-dashrule = %{tl_version}
Requires: texlive-dashundergaps = %{tl_version}
Requires: texlive-datatool = %{tl_version}
Requires: texlive-dateiliste = %{tl_version}
Requires: texlive-datenumber = %{tl_version}
Requires: texlive-datetime = %{tl_version}
Requires: texlive-dblfloatfix = %{tl_version}
Requires: texlive-decimal = %{tl_version}
Requires: texlive-delimtxt = %{tl_version}
Requires: texlive-diagnose = %{tl_version}
Requires: texlive-dichokey = %{tl_version}
Requires: texlive-dinbrief = %{tl_version}
Requires: texlive-directory = %{tl_version}
Requires: texlive-dlfltxb = %{tl_version}
Requires: texlive-dnaseq = %{tl_version}
Requires: texlive-docmfp = %{tl_version}
Requires: texlive-docmute = %{tl_version}
Requires: texlive-doi = %{tl_version}
Requires: texlive-dotarrow = %{tl_version}
Requires: texlive-dotseqn = %{tl_version}
Requires: texlive-dox = %{tl_version}
Requires: texlive-dpfloat = %{tl_version}
Requires: texlive-dprogress = %{tl_version}
Requires: texlive-drac = %{tl_version}
Requires: texlive-draftcopy = %{tl_version}
Requires: texlive-draftwatermark = %{tl_version}
Requires: texlive-dtk = %{tl_version}
Requires: texlive-dtxgallery-doc = %{tl_version}
Requires: texlive-dvdcoll = %{tl_version}
Requires: texlive-easy = %{tl_version}
Requires: texlive-easylist = %{tl_version}
Requires: texlive-ean13isbn = %{tl_version}
Requires: texlive-ebezier = %{tl_version}
Requires: texlive-ecclesiastic = %{tl_version}
Requires: texlive-ecv = %{tl_version}
Requires: texlive-ed = %{tl_version}
Requires: texlive-edmargin = %{tl_version}
Requires: texlive-eemeir = %{tl_version}
Requires: texlive-egplot = %{tl_version}
Requires: texlive-ellipsis = %{tl_version}
Requires: texlive-elmath = %{tl_version}
Requires: texlive-elpres = %{tl_version}
Requires: texlive-elsarticle = %{tl_version}
Requires: texlive-em = %{tl_version}
Requires: texlive-emptypage = %{tl_version}
Requires: texlive-emulateapj = %{tl_version}
Requires: texlive-endfloat = %{tl_version}
Requires: texlive-endheads = %{tl_version}
Requires: texlive-endnotes = %{tl_version}
Requires: texlive-engpron = %{tl_version}
Requires: texlive-engrec = %{tl_version}
Requires: texlive-enumitem = %{tl_version}
Requires: texlive-envbig = %{tl_version}
Requires: texlive-environ = %{tl_version}
Requires: texlive-envlab = %{tl_version}
Requires: texlive-epigraph = %{tl_version}
Requires: texlive-epiolmec = %{tl_version}
Requires: texlive-eqell = %{tl_version}
Requires: texlive-eqlist = %{tl_version}
Requires: texlive-eqparbox = %{tl_version}
Requires: texlive-errata = %{tl_version}
Requires: texlive-esint = %{tl_version}
Requires: texlive-esint-type1 = %{tl_version}
Requires: texlive-etaremune = %{tl_version}
Requires: texlive-etextools = %{tl_version}
Requires: texlive-etoolbox = %{tl_version}
Requires: texlive-eukdate = %{tl_version}
Requires: texlive-europecv = %{tl_version}
Requires: texlive-everypage = %{tl_version}
Requires: texlive-exam = %{tl_version}
Requires: texlive-examdesign = %{tl_version}
Requires: texlive-examplep = %{tl_version}
Requires: texlive-excludeonly = %{tl_version}
Requires: texlive-exercise = %{tl_version}
Requires: texlive-exp-testopt = %{tl_version}
Requires: texlive-expdlist = %{tl_version}
Requires: texlive-export = %{tl_version}
Requires: texlive-extract = %{tl_version}
Requires: texlive-facsimile = %{tl_version}
Requires: texlive-fancynum = %{tl_version}
Requires: texlive-fancypar = %{tl_version}
Requires: texlive-fancytooltips = %{tl_version}
Requires: texlive-figsize = %{tl_version}
Requires: texlive-filecontents = %{tl_version}
Requires: texlive-filehook = %{tl_version}
Requires: texlive-fink = %{tl_version}
Requires: texlive-fixfoot = %{tl_version}
Requires: texlive-fixme = %{tl_version}
Requires: texlive-flabels = %{tl_version}
Requires: texlive-flacards = %{tl_version}
Requires: texlive-flagderiv = %{tl_version}
Requires: texlive-flashcards = %{tl_version}
Requires: texlive-flashmovie = %{tl_version}
Requires: texlive-flippdf = %{tl_version}
Requires: texlive-floatrow = %{tl_version}
Requires: texlive-flowfram = %{tl_version}
Requires: texlive-fltpage = %{tl_version}
Requires: texlive-fmp = %{tl_version}
Requires: texlive-fmtcount = %{tl_version}
Requires: texlive-fn2end = %{tl_version}
Requires: texlive-fnbreak = %{tl_version}
Requires: texlive-fncychap = %{tl_version}
Requires: texlive-fncylab = %{tl_version}
Requires: texlive-fnpara = %{tl_version}
Requires: texlive-foilhtml = %{tl_version}
Requires: texlive-fonttable = %{tl_version}
Requires: texlive-footmisc = %{tl_version}
Requires: texlive-footnpag = %{tl_version}
Requires: texlive-forarray = %{tl_version}
Requires: texlive-forloop = %{tl_version}
Requires: texlive-formular = %{tl_version}
Requires: texlive-fragments = %{tl_version}
Requires: texlive-frame = %{tl_version}
Requires: texlive-framed = %{tl_version}
Requires: texlive-frankenstein = %{tl_version}
Requires: texlive-ftcap = %{tl_version}
Requires: texlive-ftnxtra = %{tl_version}
Requires: texlive-fribrief = %{tl_version}
Requires: texlive-fullblck-doc = %{tl_version}
Requires: texlive-fundus = %{tl_version}
Requires: texlive-g-brief = %{tl_version}
Requires: texlive-gauss = %{tl_version}
Requires: texlive-gcard = %{tl_version}
Requires: texlive-gcite = %{tl_version}
Requires: texlive-genmpage = %{tl_version}
Requires: texlive-getfiledate = %{tl_version}
Requires: texlive-ginpenc = %{tl_version}
Requires: texlive-gloss = %{tl_version}
Requires: texlive-glossaries = %{tl_version}
Requires: texlive-gmdoc = %{tl_version}
Requires: texlive-gmdoc-enhance = %{tl_version}
Requires: texlive-gmeometric = %{tl_version}
Requires: texlive-gmiflink = %{tl_version}
Requires: texlive-gmutils = %{tl_version}
Requires: texlive-gmverb = %{tl_version}
Requires: texlive-graphicx-psmin = %{tl_version}
Requires: texlive-grfpaste = %{tl_version}
Requires: texlive-grid = %{tl_version}
Requires: texlive-gridset = %{tl_version}
Requires: texlive-guitlogo = %{tl_version}
Requires: texlive-hanging = %{tl_version}
Requires: texlive-harpoon = %{tl_version}
Requires: texlive-hc = %{tl_version}
Requires: texlive-hhtensor = %{tl_version}
Requires: texlive-histogr = %{tl_version}
Requires: texlive-hitec = %{tl_version}
Requires: texlive-hpsdiss = %{tl_version}
Requires: texlive-hrefhide = %{tl_version}
Requires: texlive-hvindex = %{tl_version}
Requires: texlive-hypdvips = %{tl_version}
Requires: texlive-hyper = %{tl_version}
Requires: texlive-hypernat = %{tl_version}
Requires: texlive-hyperref-docsrc-doc = %{tl_version}
Requires: texlive-hyperxmp = %{tl_version}
Requires: texlive-hyphenat = %{tl_version}
Requires: texlive-idxlayout = %{tl_version}
Requires: texlive-ifmslide = %{tl_version}
Requires: texlive-ifmtarg = %{tl_version}
Requires: texlive-ifplatform = %{tl_version}
Requires: texlive-image-gallery = %{tl_version}
Requires: texlive-imakeidx = %{tl_version}
Requires: texlive-import = %{tl_version}
Requires: texlive-inlinedef = %{tl_version}
Requires: texlive-interactiveworkbook = %{tl_version}
Requires: texlive-inversepath = %{tl_version}
Requires: texlive-iso = %{tl_version}
Requires: texlive-iso10303 = %{tl_version}
Requires: texlive-isodate = %{tl_version}
Requires: texlive-isonums = %{tl_version}
Requires: texlive-isodoc = %{tl_version}
Requires: texlive-isorot = %{tl_version}
Requires: texlive-isotope = %{tl_version}
Requires: texlive-kastrup = %{tl_version}
Requires: texlive-kerntest = %{tl_version}
Requires: texlive-keycommand = %{tl_version}
Requires: texlive-keystroke = %{tl_version}
Requires: texlive-labbook = %{tl_version}
Requires: texlive-labelcas = %{tl_version}
Requires: texlive-labels = %{tl_version}
Requires: texlive-lastpage = %{tl_version}
Requires: texlive-layouts = %{tl_version}
Requires: texlive-lazylist = %{tl_version}
Requires: texlive-lcd = %{tl_version}
Requires: texlive-lcg = %{tl_version}
Requires: texlive-leading = %{tl_version}
Requires: texlive-leaflet = %{tl_version}
Requires: texlive-leftidx = %{tl_version}
Requires: texlive-lettre = %{tl_version}
Requires: texlive-lettrine = %{tl_version}
Requires: texlive-lewis = %{tl_version}
Requires: texlive-lhelp = %{tl_version}
Requires: texlive-limap = %{tl_version}
Requires: texlive-linegoal = %{tl_version}
Requires: texlive-lipsum = %{tl_version}
Requires: texlive-listing = %{tl_version}
Requires: texlive-listofsymbols = %{tl_version}
Requires: texlive-listliketab = %{tl_version}
Requires: texlive-lkproof = %{tl_version}
Requires: texlive-locality = %{tl_version}
Requires: texlive-localloc = %{tl_version}
Requires: texlive-logical-markup-utils = %{tl_version}
Requires: texlive-logpap = %{tl_version}
Requires: texlive-lsc = %{tl_version}
Requires: texlive-ltabptch = %{tl_version}
Requires: texlive-ltxdockit = %{tl_version}
Requires: texlive-ltxindex = %{tl_version}
Requires: texlive-ltxnew = %{tl_version}
Requires: texlive-magaz = %{tl_version}
Requires: texlive-mailing = %{tl_version}
Requires: texlive-mailmerge = %{tl_version}
Requires: texlive-makebarcode = %{tl_version}
Requires: texlive-makebox = %{tl_version}
Requires: texlive-makecell = %{tl_version}
Requires: texlive-makecirc = %{tl_version}
Requires: texlive-makecmds = %{tl_version}
Requires: texlive-makedtx = %{tl_version}
Requires: texlive-makeglos = %{tl_version}
Requires: texlive-manfnt = %{tl_version}
Requires: texlive-manuscript = %{tl_version}
Requires: texlive-mapcodes = %{tl_version}
Requires: texlive-marginnote = %{tl_version}
Requires: texlive-mathexam = %{tl_version}
Requires: texlive-maybemath = %{tl_version}
Requires: texlive-mcaption = %{tl_version}
Requires: texlive-mceinleger = %{tl_version}
Requires: texlive-mcite = %{tl_version}
Requires: texlive-mciteplus = %{tl_version}
Requires: texlive-mdframed = %{tl_version}
Requires: texlive-memexsupp = %{tl_version}
Requires: texlive-menu = %{tl_version}
Requires: texlive-method = %{tl_version}
Requires: texlive-metre = %{tl_version}
Requires: texlive-mftinc = %{tl_version}
Requires: texlive-midpage = %{tl_version}
Requires: texlive-minibox = %{tl_version}
Requires: texlive-minipage-marginpar = %{tl_version}
Requires: texlive-minitoc = %{tl_version}
Requires: texlive-minted = %{tl_version}
Requires: texlive-minutes = %{tl_version}
Requires: texlive-misc209 = %{tl_version}
Requires: texlive-mla-paper = %{tl_version}
Requires: texlive-mlist = %{tl_version}
Requires: texlive-mmap = %{tl_version}
Requires: texlive-moderncv = %{tl_version}
Requires: texlive-modref = %{tl_version}
Requires: texlive-modroman = %{tl_version}
Requires: texlive-morefloats = %{tl_version}
Requires: texlive-moresize = %{tl_version}
Requires: texlive-moreverb = %{tl_version}
Requires: texlive-movie15 = %{tl_version}
Requires: texlive-mparhack = %{tl_version}
Requires: texlive-msc = %{tl_version}
Requires: texlive-msg = %{tl_version}
Requires: texlive-mslapa = %{tl_version}
Requires: texlive-mtgreek = %{tl_version}
Requires: texlive-multibbl = %{tl_version}
Requires: texlive-multicap = %{tl_version}
Requires: texlive-multirow = %{tl_version}
Requires: texlive-mylatexformat = %{tl_version}
Requires: texlive-nag = %{tl_version}
Requires: texlive-namespc = %{tl_version}
Requires: texlive-ncclatex = %{tl_version}
Requires: texlive-ncctools = %{tl_version}
Requires: texlive-needspace = %{tl_version}
Requires: texlive-newcommand-doc = %{tl_version}
Requires: texlive-newfile = %{tl_version}
Requires: texlive-newlfm = %{tl_version}
Requires: texlive-newspaper = %{tl_version}
Requires: texlive-newvbtm = %{tl_version}
Requires: texlive-newverbs = %{tl_version}
Requires: texlive-nextpage = %{tl_version}
Requires: texlive-nfssext-cfr = %{tl_version}
Requires: texlive-niceframe = %{tl_version}
Requires: texlive-nicetext = %{tl_version}
Requires: texlive-nlctdoc = %{tl_version}
Requires: texlive-noitcrul = %{tl_version}
Requires: texlive-nolbreaks = %{tl_version}
Requires: texlive-nomencl = %{tl_version}
Requires: texlive-nomentbl = %{tl_version}
Requires: texlive-nonfloat = %{tl_version}
Requires: texlive-nopageno = %{tl_version}
Requires: texlive-notes = %{tl_version}
Requires: texlive-notoccite = %{tl_version}
Requires: texlive-ntabbing = %{tl_version}
Requires: texlive-ntheorem = %{tl_version}
Requires: texlive-numname = %{tl_version}
Requires: texlive-numprint = %{tl_version}
Requires: texlive-ocgtools = %{tl_version}
Requires: texlive-ocr-latex = %{tl_version}
Requires: texlive-octavo = %{tl_version}
Requires: texlive-oldstyle = %{tl_version}
Requires: texlive-onlyamsmath = %{tl_version}
Requires: texlive-opcit = %{tl_version}
Requires: texlive-optional = %{tl_version}
Requires: texlive-outline = %{tl_version}
Requires: texlive-outliner = %{tl_version}
Requires: texlive-overpic = %{tl_version}
Requires: texlive-pagecont = %{tl_version}
Requires: texlive-pagenote = %{tl_version}
Requires: texlive-pagerange = %{tl_version}
Requires: texlive-pageslts = %{tl_version}
Requires: texlive-paper = %{tl_version}
Requires: texlive-papercdcase = %{tl_version}
Requires: texlive-papermas = %{tl_version}
Requires: texlive-papertex = %{tl_version}
Requires: texlive-paralist = %{tl_version}
Requires: texlive-paresse = %{tl_version}
Requires: texlive-patchcmd = %{tl_version}
Requires: texlive-pauldoc = %{tl_version}
Requires: texlive-pawpict = %{tl_version}
Requires: texlive-pax = %{tl_version}
Requires: texlive-pbox = %{tl_version}
Requires: texlive-pbsheet = %{tl_version}
Requires: texlive-pdf14 = %{tl_version}
Requires: texlive-pdfcomment = %{tl_version}
Requires: texlive-pdfcprot = %{tl_version}
Requires: texlive-pdfmarginpar = %{tl_version}
Requires: texlive-pdfscreen = %{tl_version}
Requires: texlive-pdfslide = %{tl_version}
Requires: texlive-pdfsync = %{tl_version}
Requires: texlive-pdfwin = %{tl_version}
Requires: texlive-pdfx = %{tl_version}
Requires: texlive-pecha = %{tl_version}
Requires: texlive-perltex = %{tl_version}
Requires: texlive-permute = %{tl_version}
Requires: texlive-petiteannonce = %{tl_version}
Requires: texlive-philex = %{tl_version}
Requires: texlive-photo = %{tl_version}
Requires: texlive-pittetd = %{tl_version}
Requires: texlive-placeins = %{tl_version}
Requires: texlive-plates = %{tl_version}
Requires: texlive-plantslabels = %{tl_version}
Requires: texlive-plweb = %{tl_version}
Requires: texlive-polyglot = %{tl_version}
Requires: texlive-polynom = %{tl_version}
Requires: texlive-polynomial = %{tl_version}
Requires: texlive-polytable = %{tl_version}
Requires: texlive-postcards = %{tl_version}
Requires: texlive-poster-mac = %{tl_version}
Requires: texlive-ppower4 = %{tl_version}
Requires: texlive-ppr-prv = %{tl_version}
Requires: texlive-preprint = %{tl_version}
Requires: texlive-prettyref = %{tl_version}
Requires: texlive-preview = %{tl_version}
Requires: texlive-printlen = %{tl_version}
Requires: texlive-probsoln = %{tl_version}
Requires: texlive-program = %{tl_version}
Requires: texlive-progress = %{tl_version}
Requires: texlive-properties = %{tl_version}
Requires: texlive-prosper = %{tl_version}
Requires: texlive-protex = %{tl_version}
Requires: texlive-protocol = %{tl_version}
Requires: texlive-psfragx = %{tl_version}
Requires: texlive-pst-pdf = %{tl_version}
Requires: texlive-pstool = %{tl_version}
Requires: texlive-qcm = %{tl_version}
Requires: texlive-qstest = %{tl_version}
Requires: texlive-qsymbols = %{tl_version}
Requires: texlive-quotchap = %{tl_version}
Requires: texlive-quotmark = %{tl_version}
Requires: texlive-randtext = %{tl_version}
Requires: texlive-rccol = %{tl_version}
Requires: texlive-rcs-multi = %{tl_version}
Requires: texlive-rcsinfo = %{tl_version}
Requires: texlive-recipe = %{tl_version}
Requires: texlive-recipecard = %{tl_version}
Requires: texlive-rectopma = %{tl_version}
Requires: texlive-refcheck = %{tl_version}
Requires: texlive-refman = %{tl_version}
Requires: texlive-refstyle = %{tl_version}
Requires: texlive-regcount = %{tl_version}
Requires: texlive-register = %{tl_version}
Requires: texlive-relsize = %{tl_version}
Requires: texlive-repeatindex = %{tl_version}
Requires: texlive-rjlparshap = %{tl_version}
Requires: texlive-rlepsf = %{tl_version}
Requires: texlive-rmpage = %{tl_version}
Requires: texlive-robustcommand = %{tl_version}
Requires: texlive-robustindex = %{tl_version}
Requires: texlive-romannum = %{tl_version}
Requires: texlive-rotfloat = %{tl_version}
Requires: texlive-rotpages = %{tl_version}
Requires: texlive-rtkinenc = %{tl_version}
Requires: texlive-sauerj = %{tl_version}
Requires: texlive-savefnmark = %{tl_version}
Requires: texlive-savesym = %{tl_version}
Requires: texlive-savetrees = %{tl_version}
Requires: texlive-scale = %{tl_version}
Requires: texlive-scalebar = %{tl_version}
Requires: texlive-sciwordconv = %{tl_version}
Requires: texlive-sdrt = %{tl_version}
Requires: texlive-sectionbox = %{tl_version}
Requires: texlive-sectsty = %{tl_version}
Requires: texlive-selectp = %{tl_version}
Requires: texlive-semantic = %{tl_version}
Requires: texlive-semioneside = %{tl_version}
Requires: texlive-seqsplit = %{tl_version}
Requires: texlive-sf298 = %{tl_version}
Requires: texlive-sffms = %{tl_version}
Requires: texlive-sfmath = %{tl_version}
Requires: texlive-shadethm = %{tl_version}
Requires: texlive-shapepar = %{tl_version}
Requires: texlive-shipunov = %{tl_version}
Requires: texlive-shorttoc = %{tl_version}
Requires: texlive-show2e = %{tl_version}
Requires: texlive-showexpl = %{tl_version}
Requires: texlive-showlabels = %{tl_version}
Requires: texlive-sidecap = %{tl_version}
Requires: texlive-silence = %{tl_version}
Requires: texlive-simplecd = %{tl_version}
Requires: texlive-simplecv = %{tl_version}
Requires: texlive-simplewick = %{tl_version}
Requires: texlive-skeycommand = %{tl_version}
Requires: texlive-skeyval = %{tl_version}
Requires: texlive-slantsc = %{tl_version}
Requires: texlive-smalltableof = %{tl_version}
Requires: texlive-smartref = %{tl_version}
Requires: texlive-snapshot = %{tl_version}
Requires: texlive-soul = %{tl_version}
Requires: texlive-sparklines = %{tl_version}
Requires: texlive-spreadtab = %{tl_version}
Requires: texlive-spverbatim = %{tl_version}
Requires: texlive-splitindex = %{tl_version}
Requires: texlive-spotcolor = %{tl_version}
Requires: texlive-srcltx = %{tl_version}
Requires: texlive-sseq = %{tl_version}
Requires: texlive-ssqquote = %{tl_version}
Requires: texlive-stack = %{tl_version}
Requires: texlive-standalone = %{tl_version}
Requires: texlive-statistik = %{tl_version}
Requires: texlive-stdclsdv = %{tl_version}
Requires: texlive-stdpage = %{tl_version}
Requires: texlive-stex = %{tl_version}
Requires: texlive-stringstrings = %{tl_version}
Requires: texlive-sttools = %{tl_version}
Requires: texlive-stubs = %{tl_version}
Requires: texlive-subdepth = %{tl_version}
Requires: texlive-subeqn = %{tl_version}
Requires: texlive-subeqnarray = %{tl_version}
Requires: texlive-subfigure = %{tl_version}
Requires: texlive-subfloat = %{tl_version}
Requires: texlive-substr = %{tl_version}
Requires: texlive-supertabular = %{tl_version}
Requires: texlive-svgcolor = %{tl_version}
Requires: texlive-svn = %{tl_version}
Requires: texlive-svn-multi = %{tl_version}
Requires: texlive-svn-prov = %{tl_version}
Requires: texlive-svninfo = %{tl_version}
Requires: texlive-syntax = %{tl_version}
Requires: texlive-syntrace = %{tl_version}
Requires: texlive-synttree = %{tl_version}
Requires: texlive-tableaux = %{tl_version}
Requires: texlive-tablenotes = %{tl_version}
Requires: texlive-tablists = %{tl_version}
Requires: texlive-tabls = %{tl_version}
Requires: texlive-tabto-ltx = %{tl_version}
Requires: texlive-tabularborder = %{tl_version}
Requires: texlive-tabularcalc = %{tl_version}
Requires: texlive-tabularew = %{tl_version}
Requires: texlive-tabulary = %{tl_version}
Requires: texlive-talk = %{tl_version}
Requires: texlive-taupin = %{tl_version}
Requires: texlive-tcldoc = %{tl_version}
Requires: texlive-tdclock = %{tl_version}
Requires: texlive-technics = %{tl_version}
Requires: texlive-ted = %{tl_version}
Requires: texlive-termlist = %{tl_version}
Requires: texlive-tex-label = %{tl_version}
Requires: texlive-texlogos = %{tl_version}
Requires: texlive-texmate = %{tl_version}
Requires: texlive-texments = %{tl_version}
Requires: texlive-texpower = %{tl_version}
Requires: texlive-texshade = %{tl_version}
Requires: texlive-textcase = %{tl_version}
Requires: texlive-textfit = %{tl_version}
Requires: texlive-textmerg = %{tl_version}
Requires: texlive-textpos = %{tl_version}
Requires: texlive-theoremref = %{tl_version}
Requires: texlive-threeparttable = %{tl_version}
Requires: texlive-threeparttablex = %{tl_version}
Requires: texlive-thinsp = %{tl_version}
Requires: texlive-thmtools = %{tl_version}
Requires: texlive-thumb = %{tl_version}
Requires: texlive-thumby = %{tl_version}
Requires: texlive-ticket = %{tl_version}
Requires: texlive-timesht = %{tl_version}
Requires: texlive-titlefoot = %{tl_version}
Requires: texlive-titlepic = %{tl_version}
Requires: texlive-titleref = %{tl_version}
Requires: texlive-titlesec = %{tl_version}
Requires: texlive-titling = %{tl_version}
Requires: texlive-tocbibind = %{tl_version}
Requires: texlive-tocloft = %{tl_version}
Requires: texlive-tocvsec2 = %{tl_version}
Requires: texlive-todo = %{tl_version}
Requires: texlive-todonotes = %{tl_version}
Requires: texlive-tokenizer = %{tl_version}
Requires: texlive-toolbox = %{tl_version}
Requires: texlive-topfloat = %{tl_version}
Requires: texlive-totcount = %{tl_version}
Requires: texlive-totpages = %{tl_version}
Requires: texlive-trfsigns = %{tl_version}
Requires: texlive-trimspaces = %{tl_version}
Requires: texlive-trsym = %{tl_version}
Requires: texlive-trivfloat = %{tl_version}
Requires: texlive-truncate = %{tl_version}
Requires: texlive-twoinone = %{tl_version}
Requires: texlive-twoup = %{tl_version}
Requires: texlive-type1cm = %{tl_version}
Requires: texlive-typedref = %{tl_version}
Requires: texlive-typogrid = %{tl_version}
Requires: texlive-ucs = %{tl_version}
Requires: texlive-uebungsblatt = %{tl_version}
Requires: texlive-umoline = %{tl_version}
Requires: texlive-underlin = %{tl_version}
Requires: texlive-undolabl = %{tl_version}
Requires: texlive-units = %{tl_version}
Requires: texlive-upmethodology = %{tl_version}
Requires: texlive-upquote = %{tl_version}
Requires: texlive-ushort = %{tl_version}
Requires: texlive-varindex = %{tl_version}
Requires: texlive-varsfromjobname = %{tl_version}
Requires: texlive-varwidth = %{tl_version}
Requires: texlive-verbatimbox = %{tl_version}
Requires: texlive-verbatimcopy = %{tl_version}
Requires: texlive-verbdef = %{tl_version}
Requires: texlive-version = %{tl_version}
Requires: texlive-versions = %{tl_version}
Requires: texlive-vertbars = %{tl_version}
Requires: texlive-vhistory = %{tl_version}
Requires: texlive-vita = %{tl_version}
Requires: texlive-vmargin = %{tl_version}
Requires: texlive-volumes = %{tl_version}
Requires: texlive-vpe = %{tl_version}
Requires: texlive-vrsion = %{tl_version}
Requires: texlive-vwcol = %{tl_version}
Requires: texlive-wallpaper = %{tl_version}
Requires: texlive-warning = %{tl_version}
Requires: texlive-warpcol = %{tl_version}
Requires: texlive-was = %{tl_version}
Requires: texlive-widetable = %{tl_version}
Requires: texlive-williams = %{tl_version}
Requires: texlive-wordlike = %{tl_version}
Requires: texlive-wrapfig = %{tl_version}
Requires: texlive-xargs = %{tl_version}
Requires: texlive-xbmc = %{tl_version}
Requires: texlive-xcomment = %{tl_version}
Requires: texlive-xtab = %{tl_version}
Requires: texlive-xdoc = %{tl_version}
Requires: texlive-xfor = %{tl_version}
Requires: texlive-xifthen = %{tl_version}
Requires: texlive-xmpincl = %{tl_version}
Requires: texlive-xnewcommand = %{tl_version}
Requires: texlive-xoptarg = %{tl_version}
Requires: texlive-xstring = %{tl_version}
Requires: texlive-xwatermark = %{tl_version}
Requires: texlive-xytree = %{tl_version}
Requires: texlive-yafoot = %{tl_version}
Requires: texlive-yagusylo = %{tl_version}
Requires: texlive-ydoc = %{tl_version}
Requires: texlive-yplan = %{tl_version}
Requires: texlive-zed-csp = %{tl_version}
Requires: texlive-ziffer = %{tl_version}
Requires: texlive-zwgetfdate = %{tl_version}
Requires: texlive-zwpagelayout = %{tl_version}

%description collection-latexextra
A large collection of add-on packages for LaTeX.

%package collection-pictures
Summary: Graphics packages and programs
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19330%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-asyfig = %{tl_version}
Requires: texlive-autoarea = %{tl_version}
Requires: texlive-bardiag = %{tl_version}
Requires: texlive-cachepic = %{tl_version}
Requires: texlive-chemfig = %{tl_version}
Requires: texlive-combinedgraphics = %{tl_version}
Requires: texlive-circuitikz = %{tl_version}
Requires: texlive-curve = %{tl_version}
Requires: texlive-curve2e = %{tl_version}
Requires: texlive-curves = %{tl_version}
Requires: texlive-dcpic = %{tl_version}
Requires: texlive-diagmac2 = %{tl_version}
Requires: texlive-doc-pictex-doc = %{tl_version}
Requires: texlive-dottex = %{tl_version}
Requires: texlive-dot2texi = %{tl_version}
Requires: texlive-dratex = %{tl_version}
Requires: texlive-drs = %{tl_version}
Requires: texlive-duotenzor = %{tl_version}
Requires: texlive-eepic = %{tl_version}
Requires: texlive-epspdf = %{tl_version}
Requires: texlive-epspdfconversion = %{tl_version}
Requires: texlive-esk = %{tl_version}
Requires: texlive-fig4latex = %{tl_version}
Requires: texlive-gnuplottex = %{tl_version}
Requires: texlive-here = %{tl_version}
Requires: texlive-hvfloat = %{tl_version}
Requires: texlive-knitting = %{tl_version}
Requires: texlive-knittingpattern = %{tl_version}
Requires: texlive-mathspic = %{tl_version}
Requires: texlive-miniplot = %{tl_version}
Requires: texlive-pb-diagram = %{tl_version}
Requires: texlive-petri-nets = %{tl_version}
Requires: texlive-pgf = %{tl_version}
Requires: texlive-pgf-soroban = %{tl_version}
Requires: texlive-pgf-umlsd = %{tl_version}
Requires: texlive-pgfopts = %{tl_version}
Requires: texlive-pgfplots = %{tl_version}
Requires: texlive-picinpar = %{tl_version}
Requires: texlive-pict2e = %{tl_version}
Requires: texlive-pictex2 = %{tl_version}
Requires: texlive-pinlabel = %{tl_version}
Requires: texlive-pmgraph = %{tl_version}
Requires: texlive-prerex = %{tl_version}
Requires: texlive-randbild = %{tl_version}
Requires: texlive-roundbox = %{tl_version}
Requires: texlive-schemabloc = %{tl_version}
Requires: texlive-swimgraf-doc = %{tl_version}
Requires: texlive-texdraw = %{tl_version}
Requires: texlive-tikz-3dplot = %{tl_version}
Requires: texlive-tikz-inet = %{tl_version}
Requires: texlive-tikz-qtree = %{tl_version}
Requires: texlive-tikz-timing = %{tl_version}
Requires: texlive-tkz-doc = %{tl_version}
Requires: texlive-tkz-linknodes = %{tl_version}
Requires: texlive-tkz-orm = %{tl_version}
Requires: texlive-tkz-tab = %{tl_version}
Requires: texlive-tufte-latex = %{tl_version}
Requires: texlive-xypdf = %{tl_version}
Requires: texlive-xypic = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-pictures
collection-pictures package

%package cachepic-bin
Summary: Binaries for cachepic
Version: %{tl_version}
Release: %{tl_release}.svn15543%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-cachepic  = %{tl_version}

%description cachepic-bin
Binaries for cachepic

%package epspdf-bin
Summary: Binaries for epspdf
Version: %{tl_version}
Release: %{tl_release}.svn9222%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-epspdf  = %{tl_version}

%description epspdf-bin
Binaries for epspdf

%package fig4latex-bin
Summary: Binaries for fig4latex
Version: %{tl_version}
Release: %{tl_release}.svn14752%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-fig4latex  = %{tl_version}

%description fig4latex-bin
Binaries for fig4latex

%package mathspic-bin
Summary: Binaries for mathspic
Version: %{tl_version}
Release: %{tl_release}.svn18868%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-mathspic  = %{tl_version}

%description mathspic-bin
Binaries for mathspic

%package authorindex-bin
Summary: Binaries for authorindex
Version: %{tl_version}
Release: %{tl_release}.svn18790%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-authorindex  = %{tl_version}

%description authorindex-bin
Binaries for authorindex

%package glossaries-bin
Summary: Binaries for glossaries
Version: %{tl_version}
Release: %{tl_release}.svn6881%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-glossaries  = %{tl_version}

%description glossaries-bin
Binaries for glossaries

%package pax-bin
Summary: Binaries for pax
Version: %{tl_version}
Release: %{tl_release}.svn10843%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-pax  = %{tl_version}

%description pax-bin
Binaries for pax

%package perltex-bin
Summary: Binaries for perltex
Version: %{tl_version}
Release: %{tl_release}.svn16181%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-perltex  = %{tl_version}

%description perltex-bin
Binaries for perltex

%package ppower4-bin
Summary: Binaries for ppower4
Version: %{tl_version}
Release: %{tl_release}.svn13097%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-ppower4  = %{tl_version}

%description ppower4-bin
Binaries for ppower4

%package splitindex-bin
Summary: Binaries for splitindex
Version: %{tl_version}
Release: %{tl_release}.svn12613%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-splitindex  = %{tl_version}

%description splitindex-bin
Binaries for splitindex

%package svn-multi-bin
Summary: Binaries for svn-multi
Version: %{tl_version}
Release: %{tl_release}.svn13663%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-svn-multi  = %{tl_version}

%description svn-multi-bin
Binaries for svn-multi

%package vpe-bin
Summary: Binaries for vpe
Version: %{tl_version}
Release: %{tl_release}.svn6897%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-vpe  = %{tl_version}

%description vpe-bin
Binaries for vpe

%package collection-latexrecommended
Summary: LaTeX recommended packages
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18261%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-anysize = %{tl_version}
Requires: texlive-beamer = %{tl_version}
Requires: texlive-booktabs = %{tl_version}
Requires: texlive-caption = %{tl_version}
Requires: texlive-cite = %{tl_version}
Requires: texlive-cmap = %{tl_version}
Requires: texlive-crop = %{tl_version}
Requires: texlive-ctable = %{tl_version}
Requires: texlive-ec = %{tl_version}
Requires: texlive-eso-pic = %{tl_version}
Requires: texlive-euler = %{tl_version}
Requires: texlive-extsizes = %{tl_version}
Requires: texlive-fancybox = %{tl_version}
Requires: texlive-fancyref = %{tl_version}
Requires: texlive-fancyvrb = %{tl_version}
Requires: texlive-float = %{tl_version}
Requires: texlive-fp = %{tl_version}
Requires: texlive-index = %{tl_version}
Requires: texlive-jknapltx = %{tl_version}
Requires: texlive-koma-script = %{tl_version}
Requires: texlive-listings = %{tl_version}
Requires: texlive-mdwtools = %{tl_version}
Requires: texlive-memoir = %{tl_version}
Requires: texlive-metalogo = %{tl_version}
Requires: texlive-microtype = %{tl_version}
Requires: texlive-ms = %{tl_version}
Requires: texlive-ntgclass = %{tl_version}
Requires: texlive-pdfpages = %{tl_version}
Requires: texlive-powerdot = %{tl_version}
Requires: texlive-psfrag = %{tl_version}
Requires: texlive-rcs = %{tl_version}
Requires: texlive-rotating = %{tl_version}
Requires: texlive-sansmath = %{tl_version}
Requires: texlive-seminar = %{tl_version}
Requires: texlive-setspace = %{tl_version}
Requires: texlive-subfig = %{tl_version}
Requires: texlive-thumbpdf = %{tl_version}
Requires: texlive-typehtml = %{tl_version}
Requires: texlive-underscore = %{tl_version}
Requires: texlive-url = %{tl_version}
Requires: texlive-xcolor = %{tl_version}
Requires: texlive-xkeyval = %{tl_version}
Requires: texlive-collection-latex = %{tl_version}

%description collection-latexrecommended
A collection of recommended add-on packages for LaTeX which
have widespread use

%package thumbpdf-bin
Summary: Binaries for thumbpdf
Version: %{tl_version}
Release: %{tl_release}.svn6898%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-thumbpdf  = %{tl_version}

%description thumbpdf-bin
Binaries for thumbpdf

%package collection-luatex
Summary: LuaTeX packages
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18256%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}
Requires: texlive-luainputenc = %{tl_version}
Requires: texlive-lualibs = %{tl_version}
Requires: texlive-luamplib = %{tl_version}
Requires: texlive-luaotfload = %{tl_version}
Requires: texlive-luatexbase = %{tl_version}
Requires: texlive-luatextra = %{tl_version}

%description collection-luatex
Packages for LuaTeX, a Unicode-aware extension of pdfTeX, using
Lua  as an embedded scripting and extension language.
http://luatex.org/

%package luaotfload-bin
Summary: Binaries for luaotfload
Version: %{tl_version}
Release: %{tl_release}.svn18579%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-luaotfload  = %{tl_version}

%description luaotfload-bin
Binaries for luaotfload

%package collection-mathextra
Summary: Advanced math typesetting
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19348%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-12many = %{tl_version}
Requires: texlive-amstex = %{tl_version}
Requires: texlive-binomexp = %{tl_version}
Requires: texlive-boldtensors = %{tl_version}
Requires: texlive-bosisio = %{tl_version}
Requires: texlive-ccfonts = %{tl_version}
Requires: texlive-commath = %{tl_version}
Requires: texlive-concmath = %{tl_version}
Requires: texlive-concrete = %{tl_version}
Requires: texlive-extarrows = %{tl_version}
Requires: texlive-extpfeil = %{tl_version}
Requires: texlive-faktor = %{tl_version}
Requires: texlive-ionumbers = %{tl_version}
Requires: texlive-isomath = %{tl_version}
Requires: texlive-mathcomp = %{tl_version}
Requires: texlive-mattens = %{tl_version}
Requires: texlive-mhequ = %{tl_version}
Requires: texlive-multiobjective = %{tl_version}
Requires: texlive-nath = %{tl_version}
Requires: texlive-ot-tableau = %{tl_version}
Requires: texlive-proba = %{tl_version}
Requires: texlive-shuffle = %{tl_version}
Requires: texlive-statex2 = %{tl_version}
Requires: texlive-stmaryrd = %{tl_version}
Requires: texlive-susy = %{tl_version}
Requires: texlive-syllogism = %{tl_version}
Requires: texlive-synproof = %{tl_version}
Requires: texlive-tablor = %{tl_version}
Requires: texlive-tensor = %{tl_version}
Requires: texlive-tex-ewd = %{tl_version}
Requires: texlive-thmbox = %{tl_version}
Requires: texlive-turnstile = %{tl_version}
Requires: texlive-unicode-math = %{tl_version}
Requires: texlive-venn = %{tl_version}
Requires: texlive-yhmath = %{tl_version}
Requires: texlive-collection-fontsrecommended = %{tl_version}
Requires: texlive-collection-latex = %{tl_version}

%description collection-mathextra
Extra math

%package amstex-bin
Summary: Binaries for amstex
Version: %{tl_version}
Release: %{tl_release}.svn3006%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-amstex  = %{tl_version}

%description amstex-bin
Binaries for amstex

%package collection-music
Summary: Music typesetting
Version: %{tl_version}
Release: %{tl_noarch_release}.svn13822%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-abc = %{tl_version}
Requires: texlive-figbas = %{tl_version}
Requires: texlive-gchords = %{tl_version}
Requires: texlive-guitar = %{tl_version}
Requires: texlive-harmony = %{tl_version}
Requires: texlive-musixlyr = %{tl_version}
Requires: texlive-musixps = %{tl_version}
Requires: texlive-musixtex = %{tl_version}
Requires: texlive-songbook = %{tl_version}
Requires: texlive-musixflx = %{tl_version}
Requires: texlive-collection-latex = %{tl_version}

%description collection-music
Music-related fonts and packages.

%package musixflx-bin
Summary: Binaries for musixflx
Version: %{tl_version}
Release: %{tl_release}.svn14164%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-musixflx  = %{tl_version}

%description musixflx-bin
Binaries for musixflx

%package collection-omega
Summary: Omega
Version: %{tl_version}
Release: %{tl_noarch_release}.svn13822%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-antomega = %{tl_version}
Requires: texlive-lambda = %{tl_version}
Requires: texlive-omega = %{tl_version}
Requires: texlive-aleph = %{tl_version}
Requires: texlive-omegaware = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}
Requires: texlive-collection-latex = %{tl_version}

%description collection-omega
Omega, a 16-bit extended TeX by John Plaice and Yannis
Haralambous

%package aleph-bin
Summary: Binaries for aleph
Version: %{tl_version}
Release: %{tl_release}.svn19008%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-aleph  = %{tl_version}

%description aleph-bin
Binaries for aleph

%package omegaware-bin
Summary: Binaries for omegaware
Version: %{tl_version}
Release: %{tl_release}.svn19008%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-omegaware  = %{tl_version}

%description omegaware-bin
Binaries for omegaware

%package collection-plainextra
Summary: Plain TeX supplementary packages
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19038%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-fixpdfmag = %{tl_version}
Requires: texlive-font-change = %{tl_version}
Requires: texlive-fontch = %{tl_version}
Requires: texlive-graphics-pln = %{tl_version}
Requires: texlive-hyplain = %{tl_version}
Requires: texlive-js-misc = %{tl_version}
Requires: texlive-mkpattern = %{tl_version}
Requires: texlive-newsletr = %{tl_version}
Requires: texlive-pitex = %{tl_version}
Requires: texlive-placeins-plain = %{tl_version}
Requires: texlive-plnfss = %{tl_version}
Requires: texlive-resumemac = %{tl_version}
Requires: texlive-timetable = %{tl_version}
Requires: texlive-treetex = %{tl_version}
Requires: texlive-varisize = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-plainextra
Add-on packages and macros that work with plain TeX.

%package collection-pstricks
Summary: PSTricks packages
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19037%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-auto-pst-pdf = %{tl_version}
Requires: texlive-bclogo = %{tl_version}
Requires: texlive-makeplot = %{tl_version}
Requires: texlive-pdftricks = %{tl_version}
Requires: texlive-psbao = %{tl_version}
Requires: texlive-pst-2dplot = %{tl_version}
Requires: texlive-pst-3d = %{tl_version}
Requires: texlive-pst-3dplot = %{tl_version}
Requires: texlive-pst-abspos = %{tl_version}
Requires: texlive-pst-am = %{tl_version}
Requires: texlive-pst-asr = %{tl_version}
Requires: texlive-pst-bar = %{tl_version}
Requires: texlive-pst-barcode = %{tl_version}
Requires: texlive-pst-bezier = %{tl_version}
Requires: texlive-pst-blur = %{tl_version}
Requires: texlive-pst-bspline = %{tl_version}
Requires: texlive-pst-calendar = %{tl_version}
Requires: texlive-pst-circ = %{tl_version}
Requires: texlive-pst-coil = %{tl_version}
Requires: texlive-pst-cox = %{tl_version}
Requires: texlive-pst-dbicons = %{tl_version}
Requires: texlive-pst-diffraction = %{tl_version}
Requires: texlive-pst-electricfield = %{tl_version}
Requires: texlive-pst-eps = %{tl_version}
Requires: texlive-pst-eucl = %{tl_version}
Requires: texlive-pst-exa = %{tl_version}
Requires: texlive-pst-fill = %{tl_version}
Requires: texlive-pst-fr3d = %{tl_version}
Requires: texlive-pst-fractal = %{tl_version}
Requires: texlive-pst-fun = %{tl_version}
Requires: texlive-pst-func = %{tl_version}
Requires: texlive-pst-gantt = %{tl_version}
Requires: texlive-pst-geo = %{tl_version}
Requires: texlive-pst-ghsb = %{tl_version}
Requires: texlive-pst-gr3d = %{tl_version}
Requires: texlive-pst-grad = %{tl_version}
Requires: texlive-pst-infixplot = %{tl_version}
Requires: texlive-pst-jtree = %{tl_version}
Requires: texlive-pst-knot = %{tl_version}
Requires: texlive-pst-labo = %{tl_version}
Requires: texlive-pst-lens = %{tl_version}
Requires: texlive-pst-light3d = %{tl_version}
Requires: texlive-pst-magneticfield = %{tl_version}
Requires: texlive-pst-math = %{tl_version}
Requires: texlive-pst-mirror = %{tl_version}
Requires: texlive-pst-node = %{tl_version}
Requires: texlive-pst-ob3d = %{tl_version}
Requires: texlive-pst-optexp = %{tl_version}
Requires: texlive-pst-optic = %{tl_version}
Requires: texlive-pst-osci = %{tl_version}
Requires: texlive-pst-pad = %{tl_version}
Requires: texlive-pst-pdgr = %{tl_version}
Requires: texlive-pst-platon = %{tl_version}
Requires: texlive-pst-plot = %{tl_version}
Requires: texlive-pst-poly = %{tl_version}
Requires: texlive-pst-qtree = %{tl_version}
Requires: texlive-pst-sigsys = %{tl_version}
Requires: texlive-pst-slpe = %{tl_version}
Requires: texlive-pst-spectra = %{tl_version}
Requires: texlive-pst-solides3d = %{tl_version}
Requires: texlive-pst-soroban = %{tl_version}
Requires: texlive-pst-stru = %{tl_version}
Requires: texlive-pst-support-doc = %{tl_version}
Requires: texlive-pst-text = %{tl_version}
Requires: texlive-pst-thick = %{tl_version}
Requires: texlive-pst-tree = %{tl_version}
Requires: texlive-pst-uml = %{tl_version}
Requires: texlive-pst-vowel = %{tl_version}
Requires: texlive-pst-vue3d = %{tl_version}
Requires: texlive-pst2pdf = %{tl_version}
Requires: texlive-pstricks = %{tl_version}
Requires: texlive-pstricks-add = %{tl_version}
Requires: texlive-pstricks_calcnotes-doc = %{tl_version}
Requires: texlive-uml = %{tl_version}
Requires: texlive-vaucanson-g = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}
Requires: texlive-collection-genericrecommended = %{tl_version}

%description collection-pstricks
collection-pstricks package

%package pst2pdf-bin
Summary: Binaries for pst2pdf
Version: %{tl_version}
Release: %{tl_release}.svn16622%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-pst2pdf  = %{tl_version}

%description pst2pdf-bin
Binaries for pst2pdf

%package collection-publishers
Summary: Support for publishers, theses, standards, conferences, etc
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19046%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-ANUfinalexam-doc = %{tl_version}
Requires: texlive-IEEEconf = %{tl_version}
Requires: texlive-IEEEtran = %{tl_version}
Requires: texlive-aastex = %{tl_version}
Requires: texlive-acmconf = %{tl_version}
Requires: texlive-active-conf = %{tl_version}
Requires: texlive-afthesis = %{tl_version}
Requires: texlive-aguplus = %{tl_version}
Requires: texlive-aiaa = %{tl_version}
Requires: texlive-ametsoc = %{tl_version}
Requires: texlive-apa = %{tl_version}
Requires: texlive-arsclassica = %{tl_version}
Requires: texlive-asaetr = %{tl_version}
Requires: texlive-ascelike = %{tl_version}
Requires: texlive-beamer-FUBerlin = %{tl_version}
Requires: texlive-chem-journal = %{tl_version}
Requires: texlive-classicthesis = %{tl_version}
Requires: texlive-confproc = %{tl_version}
Requires: texlive-ebsthesis = %{tl_version}
Requires: texlive-economic = %{tl_version}
Requires: texlive-elbioimp = %{tl_version}
Requires: texlive-elsevier = %{tl_version}
Requires: texlive-erdc = %{tl_version}
Requires: texlive-estcpmm = %{tl_version}
Requires: texlive-euproposal = %{tl_version}
Requires: texlive-gaceta = %{tl_version}
Requires: texlive-gatech-thesis = %{tl_version}
Requires: texlive-har2nat = %{tl_version}
Requires: texlive-icsv = %{tl_version}
Requires: texlive-ieeepes = %{tl_version}
Requires: texlive-ijmart = %{tl_version}
Requires: texlive-imac = %{tl_version}
Requires: texlive-imtekda = %{tl_version}
Requires: texlive-jmlr = %{tl_version}
Requires: texlive-jpsj = %{tl_version}
Requires: texlive-kluwer = %{tl_version}
Requires: texlive-lps = %{tl_version}
Requires: texlive-macqassign = %{tl_version}
Requires: texlive-mentis = %{tl_version}
Requires: texlive-muthesis = %{tl_version}
Requires: texlive-nddiss = %{tl_version}
Requires: texlive-nih = %{tl_version}
Requires: texlive-nostarch = %{tl_version}
Requires: texlive-nrc = %{tl_version}
Requires: texlive-onrannual = %{tl_version}
Requires: texlive-philosophersimprint = %{tl_version}
Requires: texlive-powerdot-FUBerlin = %{tl_version}
Requires: texlive-pracjourn = %{tl_version}
Requires: texlive-procIAGssymp = %{tl_version}
Requires: texlive-ptptex = %{tl_version}
Requires: texlive-psu-thesis = %{tl_version}
Requires: texlive-revtex = %{tl_version}
Requires: texlive-revtex4 = %{tl_version}
Requires: texlive-ryethesis = %{tl_version}
Requires: texlive-sageep = %{tl_version}
Requires: texlive-seuthesis = %{tl_version}
Requires: texlive-siggraph = %{tl_version}
Requires: texlive-soton = %{tl_version}
Requires: texlive-spie = %{tl_version}
Requires: texlive-stellenbosch = %{tl_version}
Requires: texlive-sugconf = %{tl_version}
Requires: texlive-texilikechaps = %{tl_version}
Requires: texlive-texilikecover = %{tl_version}
Requires: texlive-thesis-titlepage-fhac = %{tl_version}
Requires: texlive-thuthesis = %{tl_version}
Requires: texlive-toptesi = %{tl_version}
Requires: texlive-tugboat = %{tl_version}
Requires: texlive-tugboat-plain = %{tl_version}
Requires: texlive-uaclasses = %{tl_version}
Requires: texlive-ucdavisthesis = %{tl_version}
Requires: texlive-ucthesis = %{tl_version}
Requires: texlive-uiucthesis = %{tl_version}
Requires: texlive-umthesis = %{tl_version}
Requires: texlive-umich-thesis = %{tl_version}
Requires: texlive-ut-thesis = %{tl_version}
Requires: texlive-uwthesis = %{tl_version}
Requires: texlive-vancouver = %{tl_version}
Requires: texlive-vxu = %{tl_version}
Requires: texlive-york-thesis = %{tl_version}
Requires: texlive-collection-latex = %{tl_version}

%description collection-publishers
collection-publishers package

%package collection-science
Summary: Typesetting for natural and computer sciences
Version: %{tl_version}
Release: %{tl_noarch_release}.svn17277%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-SIstyle = %{tl_version}
Requires: texlive-SIunits = %{tl_version}
Requires: texlive-alg = %{tl_version}
Requires: texlive-algorithm2e = %{tl_version}
Requires: texlive-algorithmicx = %{tl_version}
Requires: texlive-algorithms = %{tl_version}
Requires: texlive-biocon = %{tl_version}
Requires: texlive-bpchem = %{tl_version}
Requires: texlive-bytefield = %{tl_version}
Requires: texlive-chemarrow = %{tl_version}
Requires: texlive-chemcompounds = %{tl_version}
Requires: texlive-chemcono = %{tl_version}
Requires: texlive-chemstyle = %{tl_version}
Requires: texlive-clrscode = %{tl_version}
Requires: texlive-complexity = %{tl_version}
Requires: texlive-computational-complexity = %{tl_version}
Requires: texlive-digiconfigs = %{tl_version}
Requires: texlive-dyntree = %{tl_version}
Requires: texlive-eltex = %{tl_version}
Requires: texlive-engtlc = %{tl_version}
Requires: texlive-fouridx = %{tl_version}
Requires: texlive-functan = %{tl_version}
Requires: texlive-galois = %{tl_version}
Requires: texlive-gastex = %{tl_version}
Requires: texlive-gene-logic = %{tl_version}
Requires: texlive-gu = %{tl_version}
Requires: texlive-hep = %{tl_version}
Requires: texlive-hepnames = %{tl_version}
Requires: texlive-hepparticles = %{tl_version}
Requires: texlive-hepthesis = %{tl_version}
Requires: texlive-hepunits = %{tl_version}
Requires: texlive-karnaugh = %{tl_version}
Requires: texlive-mhchem = %{tl_version}
Requires: texlive-mhs = %{tl_version}
Requires: texlive-miller = %{tl_version}
Requires: texlive-objectz = %{tl_version}
Requires: texlive-pseudocode = %{tl_version}
Requires: texlive-scientificpaper = %{tl_version}
Requires: texlive-sciposter = %{tl_version}
Requires: texlive-sfg = %{tl_version}
Requires: texlive-siunitx = %{tl_version}
Requires: texlive-steinmetz = %{tl_version}
Requires: texlive-struktex = %{tl_version}
Requires: texlive-t-angles = %{tl_version}
Requires: texlive-textopo = %{tl_version}
Requires: texlive-ulqda = %{tl_version}
Requires: texlive-unitsdef = %{tl_version}
Requires: texlive-youngtab = %{tl_version}
Requires: texlive-collection-latex = %{tl_version}

%description collection-science
Typesetting for natural and computer sciences

%package ulqda-bin
Summary: Binaries for ulqda
Version: %{tl_version}
Release: %{tl_release}.svn13663%{?dist}
Requires: texlive-base = %{tl_version}
Requires: texlive-ulqda  = %{tl_version}

%description ulqda-bin
Binaries for ulqda

%package collection-texinfo
Summary: GNU Texinfo
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15216%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-texinfo = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description collection-texinfo
TeX macros for the GNU Texinfo documentation system.  The
programs and documentation are no longer distributed with TeX
Live; get the original Texinfo package for your system.

%package collection-xetex
Summary: XeTeX packages
Version: %{tl_version}
Release: %{tl_noarch_release}.svn17780%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-arabxetex = %{tl_version}
Requires: texlive-euenc = %{tl_version}
Requires: texlive-fontspec = %{tl_version}
Requires: texlive-fontwrap = %{tl_version}
Requires: texlive-harvardkyoto = %{tl_version}
Requires: texlive-mathspec = %{tl_version}
Requires: texlive-philokalia = %{tl_version}
Requires: texlive-polyglossia = %{tl_version}
Requires: texlive-xecjk = %{tl_version}
Requires: texlive-xecolour = %{tl_version}
Requires: texlive-xecyr = %{tl_version}
Requires: texlive-xeindex = %{tl_version}
Requires: texlive-xepersian = %{tl_version}
Requires: texlive-xesearch = %{tl_version}
Requires: texlive-xetex = %{tl_version}
Requires: texlive-xetex-def = %{tl_version}
Requires: texlive-xetex-itrans = %{tl_version}
Requires: texlive-xetex-pstricks = %{tl_version}
Requires: texlive-xetexconfig = %{tl_version}
Requires: texlive-xetexfontinfo = %{tl_version}
Requires: texlive-xltxtra = %{tl_version}
Requires: texlive-xunicode = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}
Provides: tex(xetex) = %{tl_version}
Obsoletes: texlive-xetex < %{tl_version}
Obsoletes: texlive-texmf-xetex < %{tl_version}

%description collection-xetex
Packages for XeTeX, the Unicode/OpenType-enabled TeX by
Jonathan Kew, http://scripts.sil.org/xetex.

%package scheme-gust
Summary: GUST TeX Live scheme
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15728%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-FAQ-en-doc = %{tl_version}
Requires: texlive-Type1fonts-doc = %{tl_version}
Requires: texlive-amslatex-primer-doc = %{tl_version}
Requires: texlive-amstex = %{tl_version}
Requires: texlive-antp = %{tl_version}
Requires: texlive-antt = %{tl_version}
Requires: texlive-comment = %{tl_version}
Requires: texlive-comprehensive-doc = %{tl_version}
Requires: texlive-concrete = %{tl_version}
Requires: texlive-cyklop = %{tl_version}
Requires: texlive-gustprog-doc = %{tl_version}
Requires: texlive-impatient-doc = %{tl_version}
Requires: texlive-iwona = %{tl_version}
Requires: texlive-metafont-beginners-doc = %{tl_version}
Requires: texlive-metapost-examples-doc = %{tl_version}
Requires: texlive-pstricks-tutorial-doc = %{tl_version}
Requires: texlive-seminar = %{tl_version}
Requires: texlive-tds-doc = %{tl_version}
Requires: texlive-tex4ht = %{tl_version}
Requires: texlive-bibtex8 = %{tl_version}
Requires: texlive-dviljk = %{tl_version}
Requires: texlive-seetexk = %{tl_version}
Requires: texlive-texdoc = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}
Requires: texlive-collection-context = %{tl_version}
Requires: texlive-collection-documentation-polish = %{tl_version}
Requires: texlive-collection-fontutils = %{tl_version}
Requires: texlive-collection-fontsrecommended = %{tl_version}
Requires: texlive-collection-genericrecommended = %{tl_version}
Requires: texlive-collection-langpolish = %{tl_version}
Requires: texlive-collection-latex = %{tl_version}
Requires: texlive-collection-latexrecommended = %{tl_version}
Requires: texlive-collection-metapost = %{tl_version}
Requires: texlive-collection-xetex = %{tl_version}

%description scheme-gust
This is the GUST TeX Live scheme: it is a set of files
sufficient to typeset Polish plain TeX, LaTeX and ConTeXt
documents in PostScript or PDF.

%package scheme-medium
Summary: medium scheme (plain, latex, recommended packages, some languages)
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18615%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}
Requires: texlive-collection-binextra = %{tl_version}
Requires: texlive-collection-context = %{tl_version}
Requires: texlive-collection-documentation-english = %{tl_version}
Requires: texlive-collection-fontutils = %{tl_version}
Requires: texlive-collection-fontsrecommended = %{tl_version}
Requires: texlive-collection-langczechslovak = %{tl_version}
Requires: texlive-collection-langdutch = %{tl_version}
Requires: texlive-collection-langfrench = %{tl_version}
Requires: texlive-collection-langgerman = %{tl_version}
Requires: texlive-collection-langitalian = %{tl_version}
Requires: texlive-collection-langpolish = %{tl_version}
Requires: texlive-collection-langportuguese = %{tl_version}
Requires: texlive-collection-langspanish = %{tl_version}
Requires: texlive-collection-langenglish = %{tl_version}
Requires: texlive-collection-latex = %{tl_version}
Requires: texlive-collection-latexrecommended = %{tl_version}
Requires: texlive-collection-mathextra = %{tl_version}
Requires: texlive-collection-metapost = %{tl_version}
Requires: texlive-collection-texinfo = %{tl_version}
Requires: texlive-collection-xetex = %{tl_version}
Requires: texlive-collection-luatex = %{tl_version}
Requires: texlive-collection-genericrecommended = %{tl_version}

%description scheme-medium
This is the medium TeX Live collection: it contains plain TeX,
LaTeX, many recommended packages, and support for some widely-
used European languages.

%package scheme-minimal
Summary: minimal scheme (plain only)
Version: %{tl_version}
Release: %{tl_noarch_release}.svn13822%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}

%description scheme-minimal
This is the minimal TeX Live scheme, with support for only
plain TeX. (No LaTeX macros.)  LuaTeX is included because Lua
scripts are used in TeX Live infrastructure.  This scheme
corresponds exactly to collection-basic.

%package scheme-tetex
Summary: teTeX scheme (more than medium, but nowhere near full)
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18615%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-FAQ-en-doc = %{tl_version}
Requires: texlive-SIunits = %{tl_version}
Requires: texlive-acronym = %{tl_version}
Requires: texlive-amslatex-primer-doc = %{tl_version}
Requires: texlive-bbm = %{tl_version}
Requires: texlive-bbm-macros = %{tl_version}
Requires: texlive-bbold = %{tl_version}
Requires: texlive-bibtex8 = %{tl_version}
Requires: texlive-ctie = %{tl_version}
Requires: texlive-detex = %{tl_version}
Requires: texlive-dtl = %{tl_version}
Requires: texlive-dvi2tty = %{tl_version}
Requires: texlive-dvicopy = %{tl_version}
Requires: texlive-dviljk = %{tl_version}
Requires: texlive-patgen = %{tl_version}
Requires: texlive-pdftools = %{tl_version}
Requires: texlive-seetexk = %{tl_version}
Requires: texlive-tie = %{tl_version}
Requires: texlive-web = %{tl_version}
Requires: texlive-cmbright = %{tl_version}
Requires: texlive-cweb = %{tl_version}
Requires: texlive-eplain = %{tl_version}
Requires: texlive-eulervm = %{tl_version}
Requires: texlive-gentle-doc = %{tl_version}
Requires: texlive-lshort-english-doc = %{tl_version}
Requires: texlive-mathmode-doc = %{tl_version}
Requires: texlive-mltex = %{tl_version}
Requires: texlive-multirow = %{tl_version}
Requires: texlive-nomencl = %{tl_version}
Requires: texlive-pst-pdf = %{tl_version}
Requires: texlive-pstricks-tutorial-doc = %{tl_version}
Requires: texlive-rsfs = %{tl_version}
Requires: texlive-subfigure = %{tl_version}
Requires: texlive-supertabular = %{tl_version}
Requires: texlive-tamethebeast-doc = %{tl_version}
Requires: texlive-tds-doc = %{tl_version}
Requires: texlive-tex-refs-doc = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}
Requires: texlive-collection-context = %{tl_version}
Requires: texlive-collection-documentation-base = %{tl_version}
Requires: texlive-collection-fontutils = %{tl_version}
Requires: texlive-collection-fontsrecommended = %{tl_version}
Requires: texlive-collection-genericrecommended = %{tl_version}
Requires: texlive-collection-langcjk = %{tl_version}
Requires: texlive-collection-langcroatian = %{tl_version}
Requires: texlive-collection-langcyrillic = %{tl_version}
Requires: texlive-collection-langczechslovak = %{tl_version}
Requires: texlive-collection-langdanish = %{tl_version}
Requires: texlive-collection-langdutch = %{tl_version}
Requires: texlive-collection-langfinnish = %{tl_version}
Requires: texlive-collection-langfrench = %{tl_version}
Requires: texlive-collection-langgerman = %{tl_version}
Requires: texlive-collection-langgreek = %{tl_version}
Requires: texlive-collection-langhungarian = %{tl_version}
Requires: texlive-collection-langitalian = %{tl_version}
Requires: texlive-collection-langlatin = %{tl_version}
Requires: texlive-collection-langmongolian = %{tl_version}
Requires: texlive-collection-langnorwegian = %{tl_version}
Requires: texlive-collection-langother = %{tl_version}
Requires: texlive-collection-langpolish = %{tl_version}
Requires: texlive-collection-langportuguese = %{tl_version}
Requires: texlive-collection-langspanish = %{tl_version}
Requires: texlive-collection-langswedish = %{tl_version}
Requires: texlive-collection-langenglish = %{tl_version}
Requires: texlive-collection-langvietnamese = %{tl_version}
Requires: texlive-collection-latex = %{tl_version}
Requires: texlive-collection-latexrecommended = %{tl_version}
Requires: texlive-collection-mathextra = %{tl_version}
Requires: texlive-collection-metapost = %{tl_version}
Requires: texlive-collection-omega = %{tl_version}
Requires: texlive-collection-pictures = %{tl_version}
Requires: texlive-collection-pstricks = %{tl_version}
Requires: texlive-collection-texinfo = %{tl_version}
Provides: tetex = 3.1-99
Obsoletes: tetex < 3.1-99
Obsoletes: texlive-dviutils < %{tl_version}

%description scheme-tetex
TeX Live scheme nearly equivalent to the teTeX distribution
that was maintained by Thomas Esser.

%package scheme-xml
Summary: XML scheme
Version: %{tl_version}
Release: %{tl_noarch_release}.svn13822%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-context = %{tl_version}
Requires: texlive-jadetex = %{tl_version}
Requires: texlive-ltxmisc = %{tl_version}
Requires: texlive-marvosym = %{tl_version}
Requires: texlive-marvosym = %{tl_version}
Requires: texlive-metapost = %{tl_version}
Requires: texlive-passivetex = %{tl_version}
Requires: texlive-rotating = %{tl_version}
Requires: texlive-stmaryrd = %{tl_version}
Requires: texlive-tex4ht = %{tl_version}
Requires: texlive-tipa = %{tl_version}
Requires: texlive-ucs = %{tl_version}
Requires: texlive-wasy = %{tl_version}
Requires: texlive-wasysym = %{tl_version}
Requires: texlive-xmltex = %{tl_version}
Requires: texlive-collection-basic = %{tl_version}
Requires: texlive-collection-fontsrecommended = %{tl_version}
Requires: texlive-collection-latex = %{tl_version}
Requires: texlive-collection-omega = %{tl_version}

%description scheme-xml
This contains the things you need to do XML-related work,
including PassiveTeX, JadeTeX, ConTeXt and Omega.


%package base
Summary: TeX Live licenses shipped in text form
BuildArch: noarch
Requires: %{name} = %{version}
Requires: %{name}-scheme-basic
Requires: %{name}-collection-latexrecommended
#Requires(posttrans): %{name}-kpathsea, %{name}-tetex
Requires: %{name}-kpathsea, %{name}-tetex

%description base
TeX Live licenses shipped in text form.

%package kpathsea-lib
Summary: Path searching library for TeX-related files

%description kpathsea-lib
The library is at the centre of pretty much all Unix-based TeX
executable. It is no longer distributed separately, but rather
consititutes a central part of the sources of the TeX-live
distribution.

%package kpathsea-lib-devel
Summary: Path searching library for TeX-related files
Requires: %{name}-kpathsea-lib = %{version}
Provides: kpathsea-devel = %{version}
Obsoletes: kpathsea-devel < %{version}

%description kpathsea-lib-devel
The library is at the centre of pretty much all Unix-based TeX
executable. It is no longer distributed separately, but rather
consititutes a central part of the sources of the TeX-live
distribution.

%prep
%setup -q -c -T
xz -dc %{SOURCE0} | tar x
[ -e %{source_name} ] && mv %{source_name} source
%patch1 -p0
for l in `unxz -c %{SOURCE3} | tar t`; do
ln -s %{_texdir}/licenses/$l $l
done

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export CXXFLAGS="$RPM_OPT_FLAGS"
cd source
PREF=`pwd`/inst
mkdir -p work
cd work
../configure --prefix=$PREF --datadir=$PREF --libdir=$PREF/lib --with-system-xpdf --with-system-gd --with-system-t1lib --with-system-libpng --with-system-zlib --with-system-teckit --with-teckit-includes=/usr/include/teckit --with-system-freetype2 --with-pic --with-xdvi-x-toolkit=xaw --disable-xindy --disable-xindy-docs --disable-xindy-make-rules --enable-shared --disable-t1utils --disable-psutils --disable-lacheck --disable-ps2pkm --disable-dvidvi --enable-compiler-warnings=max --without-cxx-runtime-hack --disable-native-texlive-build --disable-ptexenc
#--disable-makejvf #--disable-mendexk
make world %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/../texmf
mkdir -p %{buildroot}%{_texmf_var}
mkdir -p %{buildroot}%{_texdir}/
mkdir -p %{buildroot}%{_texdir}/readme-html.dir
mkdir -p %{buildroot}%{_texdir}/readme-txt.dir
mkdir -p %{buildroot}%{_texdir}/texmf/chktex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bib/abstyles
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bib/amsrefs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bib/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bib/beebe
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bib/biblatex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bib/computational-complexity
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bib/directory
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bib/dk-bib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bib/frankenstein
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bib/gatech-thesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bib/gloss
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bib/gustlib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bib/harvard
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bib/IEEEtran
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bib/index
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bib/jurabib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bib/lsc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bib/msc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bib/nostarch
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bib/philosophersimprint
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bib/revtex4
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bib/spie
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bib/urlbst
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bib/vancouver
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/abstyles
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/achemso
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/adrconv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/afthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/aguplus
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/aiaa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/aichej
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/ametsoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/amscls
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/amsrefs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/apacite
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/apalike
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/apalike2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/arsclassica
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/asaetr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/ascelike
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/babelbib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/beebe
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/bibexport
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/bib-fr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/bibhtml
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/biblatex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/cell
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/chembst
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/chem-journal
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/chicago
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/chicago-annote
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/computational-complexity
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/confproc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/context
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/datatool
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/din1505
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/dinat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/directory
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/disser
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/dk-bib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/dlfltxb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/dtk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/dvdcoll
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/economic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/elsarticle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/elsevier-bib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/fbs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/figbib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/finbib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/frankenstein
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/gatech-thesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/gloss
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/gost
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/gustlib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/harvard
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/hc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/ieeepes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/IEEEtran
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/ijmart
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/ijqc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/imac
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/index
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/inlinebib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/iopart-num
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/jneurosci
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/jurabib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/jurarsp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/kluwer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/mciteplus
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/minitoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/mslapa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/multibib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/munich
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/natbib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/nddiss
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/opcit
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/perception
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/persian-bib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/pnas2009
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/psu-thesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/revtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/revtex4
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/rsc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/sageep
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/savetrees
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/seuthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/shipunov
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/sort-by-letters
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/spie
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/stellenbosch
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/swebib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/texsis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/thuthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/tugboat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/urlbst
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/bst/vancouver
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/csf/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/csf/biblatex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/csf/disser
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/csf/dk-bib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/csf/gost
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/csf/persian-bib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/bibtex/csf/polish-csf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/context/data/scite
mkdir -p %{buildroot}%{_texdir}/texmf-dist/context/data/texfont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/context/data/textadept
mkdir -p %{buildroot}%{_texdir}/texmf-dist/context/data/texworks
mkdir -p %{buildroot}%{_texdir}/texmf-dist/context/data/texworks/completion
mkdir -p %{buildroot}%{_texdir}/texmf-dist/context/data/texworks/configuration
mkdir -p %{buildroot}%{_texdir}/texmf-dist/context/data/texworks/TUG
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/aleph/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/amstex/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/bibtex/abstyles
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/bibtex/apalike
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/bibtex/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/bibtex/bib-fr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/bibtex/bibhtml
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/bibtex/chicago-annote
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/bibtex/dinat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/bibtex/economic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/bibtex/elsevier-bib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/bibtex/gost
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/bibtex/ijqc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/bibtex/iopart-num
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/bibtex/tamethebeast
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/bibtex/vancouver
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/bib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/document/general/manuals
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/manuals/allkind
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/manuals/reference
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/manuals/reference/en
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/manuals/reference/en/columns
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/manuals/reference/en/fonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/manuals/reference/en/pagedesign
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/manuals/reference/en/tables
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/manuals/reference/en/typography
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/scripts/perl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/account
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/bnf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/chromato
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/construction-plan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/context-notes-zh-cn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/context-notes-zh-cn/src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/context-notes-zh-cn/src/figures
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/context-top-ten
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/context-top-ten/src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/degrade
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/fixme
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/french
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/fullpage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/games
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/letter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/lettrine
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/lilypond
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/pgfplots
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/ruby
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/simplefonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/simpleslides
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/simpleslides/solutions
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/simpleslides/styles
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/typearea
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/typescripts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/context/third/vim
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/cslatex/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/eplain
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/eplain/demo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/eplain/doc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/eplain/util
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/etex/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/accfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/ae
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/allrunes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/amsfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/antiqua
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/antp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/antt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/archaic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/arev
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/armenian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/armenian/examples/latex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/armenian/examples/plain
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/arphic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/arphic/bkaiu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/arphic/bsmiu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/arphic/gbsnu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/arphic/gkaiu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/Asana-Math
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/ascii
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/astro
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/auncial-new
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/baskervald
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/bbm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/belleek
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/bera
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/blacklettert1
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/boisik
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/boisik/example
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/bookhands
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/burmese
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/carolmin-ps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/cbfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/cc-pl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/cfr-lm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/charter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/chemarrow
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/cjhebrew
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/cm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/cmcyr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/cmcyr/vf/cmcyr6i
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/cmcyr/vf/cmcyr6k
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/cmcyr/vf/cmcyr6w
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/cmll
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/cm-super
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/cm-unicode
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/cns/cns40-1
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/cns/cns40-2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/cns/cns40-3
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/cns/cns40-4
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/cns/cns40-5
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/cns/cns40-6
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/cns/cns40-7
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/cns/cns40-b5
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/concmath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/concmath-fonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/concrete
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/cyklop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/dice
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/dictsym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/dingbat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/doublestroke
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/dozenal
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/ean
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/ec
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/ecc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/eco
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/elvish
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/enc/c90
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/epigrafica
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/esint-type1
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/euro-ce
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/eurofont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/eurosym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/eurosym/c
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/eurosym/src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/fc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/feyn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/fge
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/fonetika
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/fontinst
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/fontinst/encspecs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/basic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/eurofont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptmx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/fontinst/manual
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/fontinst/talks
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/fontinst/test
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/fontname
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/fourier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/fouriernc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/fpl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/frcursive
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/frcursive/doc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/frcursive/latex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/frcursive/mf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/frcursive/test
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/free-math-font-survey
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/free-math-font-survey/images
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/free-math-font-survey/source
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/genealogy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/gentium
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/gentium/Gentium_1.02
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/gentium/Gentium_Basic_1.1
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/gfsartemisia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/gfsbaskerville
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/gfsbodoni
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/gfscomplutum
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/gfsdidot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/gfsneohellenic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/gfsporson
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/gfssolomos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/gnu-freefont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/gothic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/greenpoint
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/grotesq
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/hfbright
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/hfoldsty
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/ibygrk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/ifsym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/inconsolata
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/initials
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/itrans
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/iwona
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/jablantile
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/junicode
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/kdgreek
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/kixfont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/knitting
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/kpfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/kurier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/lfb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/lh
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/lh/beresta
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/lh/fonttest
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/lh/lhfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/lh/samples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/libertine
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/libertine/pdfs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/libris
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/linearA
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/lm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/lxfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/ly1
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/malayalam
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/malayalam/article
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/marvosym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/marvosym/mac
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/marvosym/mac/docs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/marvosym/mac/docs/obsolete
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/marvosym/mac/oztex/configs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/marvosym/mac/oztex/dvips/inputs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/marvosym/mac/oztex/ps-files
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/marvosym/mac/oztex/tex-font/misc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/marvosym/vtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/mathabx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/memdesign
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/metafont-beginners
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/metafont-for-beginners
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/nkarta
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/oinuit
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/oinuit/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/oldlatin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/oldstandard
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/orkhun
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/pacioli
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/pclnfss
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/phaistos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/pl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/pxfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/qpxqtx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/recycle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/romande
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/rsfs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/semaphor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/skaknew
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/staves
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/stix
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/stix/Glyphs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/stmaryrd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/tex-gyre
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/tipa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/txfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/txfontsb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/Type1fonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/uhc/umj
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/universa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/utopia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/venturisadf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/wasy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/xits
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/xq
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/fonts/zhmetrics
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/2up
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/abbr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/around-the-bend
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/arrayjobx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/babel
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/barr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/colortab
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/components-of-TeX
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/c-pascal
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/c-pascal/prog
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/dcpic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/dehyph-exptl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/dirtree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/doc-pictex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/dratex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/enctex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/encxvlna
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/epsf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/epsf/okay
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/es-tex-faq
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/FAQ-en
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/FAQ-en/html
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/fenixpar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/fltpoint
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/frame
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/german
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/german/betatest
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/hyph-utf8
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/hyph-utf8/bg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/hyph-utf8/es
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/hyph-utf8/hu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/hyph-utf8/sa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/iftex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/ifxetex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/insbox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/kastrup
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/knuth/errata
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/knuth/etc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/knuth/mf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/knuth/mfware
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/knuth/tex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/knuth/texware
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/knuth/web
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/latex-notes-zh-cn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/latex-notes-zh-cn/src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/latex-notes-zh-cn/src/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/librarian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/mathdots
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/mfpic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/mfpic/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/midnight
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/multido
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/musixps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/musixtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/musixtex/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/ofs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pdf-trans
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pgf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pgf/images
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pgf/licenses
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pgf/macros
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pgfplots
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pgf/text-en
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pgf/text-en/plots
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pgf/version-for-dvipdfm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pgf/version-for-dvipdfm/en
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pgf/version-for-dvips
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pgf/version-for-dvips/en
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pgf/version-for-pdftex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pgf/version-for-pdftex/en
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pgf/version-for-tex4ht
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pgf/version-for-tex4ht/en
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pgf/version-for-vtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pgf/version-for-vtex/en
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pgf/version-for-vtex/en/plots
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/poster-mac
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-2dplot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-3dplot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-abspos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-am
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-asr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-bar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-barcode
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-bezier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-blur
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-bspline
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-circ
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-circ/more_docs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-coil
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-cox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-cox/pst-coxcoor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-cox/pst-coxeterp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-dbicons
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-diffraction
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-electricfield
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-eps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-eucl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-eucl/Exemples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-fill
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-fr3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-fractal
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-fun
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-func
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-gantt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-geo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-ghsb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-gr3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-grad
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-infixplot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-jtree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-knot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-labo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-lens
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-light3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-magneticfield
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-math
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-mirror
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-node
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-node/more_docs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-ob3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-optexp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-optic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-osci
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-pad
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-pdgr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-platon
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-plot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-plot/more_docs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-poly
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-qtree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pstricks
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pstricks-add
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pstricks/images
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pstricks-tutorial
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-sigsys
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-slpe
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-solides3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-solides3d/doc-en
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-soroban
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-spectra
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-stru
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-support
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-text
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-thick
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-tree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-uml
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/pst-vue3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/rlepsf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/shapepar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/t2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/t2/etc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/t2/etc/rubibtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/t2/etc/rumkidx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/t2/etc/utf-8
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/t2/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/tap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/tds
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/tex4ht
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/texapi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/tex-ewd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/tex-ps/cmyk-hax
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/tex-ps/poligraf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/tex-refs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/textmerg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/context
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/fonty
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/gify
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/kuchnia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/listy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/pagina
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/spisy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/poczatki
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/podstawy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/prog
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/prog/bibtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/tex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/thumbpdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/ukrhyph
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/ulem
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/variations
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/vaucanson-g
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/vaucanson-g/VCManual-src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/velthuis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/vntex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/voss-de
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/voss-de/gauss
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/voss-de/InlineMath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/voss-de/mathCol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/wsuipa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/wsuipa/latex209
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/wsuipa/latex2e
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/wsuipa/text1
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/xcomment
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/xlop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/xstring
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/xypic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/xypic/support
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/xypic-tut-pt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/generic/yax
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/12many
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/a0poster
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/a5comb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/aastex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/abc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/abstract
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/achemso
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/acmconf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/acromake
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/acronym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/active-conf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/active-conf/example
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/addlines
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/adrconv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/adrconv/adrconv_pages08.pages
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/adrconv/adrconv_pages08.pages/Contents
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/adrconv/adrconv_pages08.pages/QuickLook
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/aeguill
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/afthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/aguplus
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/aiaa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/aiaa/pre2004
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/aiaa/pre2004/demos/paper
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/aiaa/pre2004/demos/refs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/aiaa/pre2004/demos/subfigs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/aiaa/pre2004/demos/talk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/AkkTeX
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/akletter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/alg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/algorithm2e
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/algorithmicx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/algorithms
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/alnumsec
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/alterqcm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/alterqcm/doc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/altfont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ametsoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ametsoc/bibliography
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ametsoc/figures
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/amsaddr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/amscls
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/amslatex-primer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/amsldoc-it
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/amsldoc-vn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/amsmath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/amsmath-it
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/amsrefs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/amsthdoc-it
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/animate
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/animate/files
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/anonchap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/answers
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/antt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ANUfinalexam
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/anyfontsize
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/anysize
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/apa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/apacite
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/appendix
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/apprends-latex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/apprends-latex/exemples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/arabi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/arabtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/arcs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/arsclassica
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/arsclassica/Chapters
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/arsclassica/FrontBackMatter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/arsclassica/Graphics
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/arsclassica/Italian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/arsclassica/Italian/Capitoli
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/arsclassica/Italian/Immagini
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/arsclassica/Italian/MaterialeInizialeFinale
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/arydshln
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/asaetr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ascelike
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/assignment
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/asyfig
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/asyfig/example
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/attachfile
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/augie
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/augie/other
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/augie/vtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/aurical
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/authoraftertitle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/authorindex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/autoarea
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/autoarea/autodemo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/auto-pst-pdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/babelbib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/background
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bangtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/barcodes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bardiag
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bardiag/example
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bardiag/example/src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bardiag/figs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bardiag/src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bayer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bbding
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bbm-macros
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bbold
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bclogo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/beamer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/beamer-contrib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/beamer/doc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/beamer/doc/licenses
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/beamer/doc/themeexamples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/beamer/emacs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/beamer/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/beamer/examples/a-conference-talk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/beamer/examples/a-lecture
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/beamer/examples/lyx-based-presentation
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/beamer-FUBerlin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/beamerposter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/beamer/solutions/conference-talks
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/beamer/solutions/generic-talks
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/beamer/solutions/short-talks
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/begriff
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/betababel
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/beton
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bez123
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bezos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bgreek
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bibarts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bibexport
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/biblatex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/biblatex-apa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/biblatex-chem
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/biblatex-chem/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/biblatex-chicago-notes-df
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/biblatex-dw
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/biblatex-dw/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/biblatex/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/biblatex-historian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/biblatex-nature
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/biblatex-philosophy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/biblatex/resources
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/biblatex-science
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bibleref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/biblist
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bibtopic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bibtopicprefix
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bibunits
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bidi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bigfoot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bigints
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/binomexp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/biocon
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bizcard
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/blindtext
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/blkarray
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/block
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/blowup
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/boites
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bold-extra
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/boldtensors
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bookest
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/booklet
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/booktabs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/boolexpr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bophook
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bosisio
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/boxedminipage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/boxhandler
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bpchem
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bracketkey
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/braille
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/braket
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/breakurl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/brushscr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bullcntr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bussproofs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/bytefield
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cachepic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/calctab
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/calligra
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/calrsfs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/calxxxx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cancel
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/captcont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/captdef
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/caption
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/capt-of
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/carlisle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cases
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/casyl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/catechis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cbcoptic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ccaption
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ccfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ccicons
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cclicenses
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cd-cover
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cdpbundl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cell
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cellspace
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/changebar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/changelayout
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/changepage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/changes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/chappg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/chapterfolder
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/chbibref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/chembst
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/chemcompounds
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/chemcono
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/chemfig
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/chemstyle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/chessboard
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/chessfss
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/chess-problem-diagrams
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/chletter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/chngcntr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/chronology
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/circ
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/circuitikz
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cite
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cjk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cjk/doc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cjk/doc/chinese
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cjk/doc/cjk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cjk/doc/japanese
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cjk/doc/pdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/examples/texinput/Bg5
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/examples/texinput/GB
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/examples/texinput/JIS
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/examples/texinput/SJIS
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cjk/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cjk/examples/cjk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cjk/examples/pdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cjkpunct
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cjkpunct/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cjkpunct/setpunct
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cjk/texlive
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cjk/utils/pyhyphen
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/classicthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/classicthesis/Chapters
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/classicthesis/Examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/classicthesis/FrontBackmatter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/classicthesis/gfx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/clefval
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cleveref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/clock
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/clrscode
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cmap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cmbright
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cmdstring
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cmdtrack
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cm-lgc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cmpica
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cmsd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/codedoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/collref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/colordoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/colorinfo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/colortbl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/colorwav
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/combelow
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/combine
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/combinedgraphics
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/combinedgraphics/test
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/comma
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/commath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/comment
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/complexity
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/comprehensive
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/comprehensive/source
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/computational-complexity
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/concprog
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/confproc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/confproc/example
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/confproc/example/papers
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/confproc/example/papers/sources_pdftex/p_001
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/confproc/example/papers/sources_pdftex/p_003
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/confproc/example/papers/sources_pdftex/p_005
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/confproc/example/papers/sources_pdftex/p_007
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/confproc/example/papers/sources_tex/p_009
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/confproc/example/pictures
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/constants
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/contour
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cooking
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cookybooky
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cookybooky/documentation
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cookybooky/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cookybooky/examples/graphics
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cool
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/coollist
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/coolstr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cooltooltips
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/coordsys
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/courier-scaled
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/courseoutline
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/coursepaper
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/coverpage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/covington
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/crop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/crossreference
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/crossword
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/crosswrd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cryst
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/csbulletin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/csquotes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/csvtools
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ctable
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ctex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ctex-faq
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ctex-faq/src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ctex/test
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ctib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cuisine
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/currfile
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/currvita
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cursolatex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cursolatex/src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/curve
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/curve2e
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/curves
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/custom-bib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cweb-latex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cweb-latex/contrib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cweb-latex/contrib/cweb-hy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cweb-latex/contrib/wagner
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cweb-latex/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cweb-latex/examples/compare
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cweb-latex/src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/style
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/cyrillic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dashrule
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dashundergaps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dashundergaps/doc/pdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dashundergaps/doc/tex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/datatool
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dateiliste
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/datenumber
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/datetime
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dblfloatfix
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/delimtxt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/diagmac2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/diagmac2/doc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/diagnose
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dichokey
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/digiconfigs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/din1505
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dinbrief
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/directory
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/disser
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/disser/include
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/disser/templates
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/disser/templates/bachelor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/disser/templates/bachelor/fig
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/disser/templates/candidate
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/disser/templates/candidate/fig
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/disser/templates/doctor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/disser/templates/doctor/fig
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/disser/templates/master
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/disser/templates/master/fig
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dk-bib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dlfltxb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dnaseq
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/docmfp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/docmute
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/doi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/doipubmed
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dot2texi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dot2texi/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dotarrow
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dotseqn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dottex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dpfloat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dprogress
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/drac
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/draftcopy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/draftwatermark
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dramatist
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/drs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dtk/doc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dtk/historical
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dtxgallery
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dtxtut
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/duerer-latex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/duotenzor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dvdcoll
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/dyntree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ean13isbn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/easy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/easy/for-latex2html
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/easylist
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ebezier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ebong
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ebsthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ecclesiastic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ecltree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ecv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ecv/template
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ed
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/edmac
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/edmargin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ednotes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/eemeir
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/eepic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/eepic/fig2eepic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/egameps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/egplot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/eiad-ltx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/elbioimp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ellipsis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/elmath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/elpres
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/elsarticle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/elsevier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/eltex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/em
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/emp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/emptypage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/emulateapj
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/endfloat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/endheads
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/endnotes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/engpron
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/engrec
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/engtlc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/enumitem
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/envbig
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/environ
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/envlab
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/epigraph
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/epiolmec
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/epsdice
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/epslatex-fr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/epspdfconversion
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/epspdfconversion/example
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/epstopdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/eqell
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/eqlist
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/eqparbox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/erdc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/errata
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ESIEEcv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/esint
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/esk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/eskd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/eskdx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/eskdx/manual
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/eskdx/source
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/eskdx/test
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/eso-pic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/estcpmm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/esvect
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/etaremune
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/etex-pkg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/etextools
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ethiop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ethiop-t1
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/etoolbox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/euenc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/eukdate
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/euler
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/eulervm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/euproposal
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/euro
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/europecv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/europecv/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/europecv/templates
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/eurosans
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/everypage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/exam
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/examdesign
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/examplep
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/excludeonly
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/exercise
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/expdlist
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/expl3
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/export
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/exp-testopt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/extarrows
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/extpfeil
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/extract
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/extsizes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/facsimile
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/faktor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fancybox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fancyhdr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fancyhdr-it
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fancynum
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fancypar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fancyref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fancytooltips
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fancytooltips/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fancytooltips/examples/fancy-preview
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fancytooltips/examples/tex4ht
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fancytooltips/examples/tex4ht/images
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fancyvrb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/feynmf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/figbib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/figsize
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/filecontents
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/filehook
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fink
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/first-latex-doc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fix2col
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fixfoot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fixme
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/flabels
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/flacards
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/flagderiv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/flashcards
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/flashmovie
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/flashmovie/flv-player-license
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/flippdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/float
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/floatrow
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/flowfram
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/flowfram/samples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fltpage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fmp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fmtcount
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fn2end
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fnbreak
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fncychap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fncylab
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fnpara
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/foekfont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fontspec
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fonttable
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/footbib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/footmisc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/footnpag
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/footnpag/test
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/forarray
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/forloop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/formular
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fouridx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fragments
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/framed
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/frankenstein
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/frankenstein/unsupported
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/frenchle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fribrief
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/frletter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/frontespizio
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ftcap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ftnxtra
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fullblck
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/functan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fundus
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/fundus/doc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gaceta
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/galois
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gastex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gatech-thesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gatech-thesis/julesverne
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gatech-thesis/julesverne/basic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gatech-thesis/julesverne/bellswhistles
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gatech-thesis/julesverne/bellswhistles/code
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gatech-thesis/julesverne/bellswhistles/fig
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gauss
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gb4e
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/g-brief
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gcard
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gchords
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gcite
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gene-logic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/genmpage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/geometry
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/germkorr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/getfiledate
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ginpenc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gloss
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/glossaries
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/glossaries/samples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gmdoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gmdoc/basedrivers
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gmdoc-enhance
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gmeometric
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gmiflink
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gmutils
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gmverb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gmverse
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gnuplottex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/graphics
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/graphicx-psmin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/greekdates
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/greek-inputenc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/greektex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/grfpaste
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/grfpaste/doc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/grid
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gridset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/grverb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/gu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/guide-to-latex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap10
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap11
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap15
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap3
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap4
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap5
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap6
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap7
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap8
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/guitar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/guitlogo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hanging
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/HA-prosper
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/har2nat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/harmony
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/harpoon
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/harvard
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hep
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hepnames
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hepparticles
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hepthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hepthesis/example
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hepunits
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/here
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hexgame
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hhtensor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/histogr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/historische-zeitschrift
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hitec
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hpsdiss
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hrlatex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hvfloat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hvindex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hypdvips
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hypdvips/images
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hyper
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hyper/contrib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hypernat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hyperref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hyperref-docsrc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hyper/scontrib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hyperxmp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/hyphenat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ibycus-babel
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/icsv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/idxlayout
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/IEEEconf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ieeepes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/IEEEtran
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ifmslide
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ifmtarg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ifplatform
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ijmart
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/imac
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/image-gallery
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/imakeidx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/import
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/imtekda
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/imtekda/figures
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/index
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/inlinebib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/inlinedef
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/documentation
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/samplefiles
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/intro-scientific
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/inversepath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ionumbers
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/iso
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/iso10303
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/isodate
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/isodoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/isomath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/isonums
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/isorot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/itnumpar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/jeopardy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/jeopardy/example
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/jknapltx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/jmlr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/jmlr/sample-books
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/jmlr/sample-books/paper1
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/jmlr/sample-books/paper2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/jmlr/sample-books/paper3
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/jmlr/sample-books/paper4
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/jmlr/sample-papers
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/jmlr/sample-papers/images
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/jneurosci
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/jpsj
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/jura
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/juraabbrev
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/jurabib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/jurabib/docs/english
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/jurabib/docs/german
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/juramisc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/juramisc/doc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/juramisc/doc/jbook
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/jurarsp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/karnaugh
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/kerkis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/kerntest
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/keycommand
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/keystroke
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/kluwer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/knittingpattern
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/koma-script
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel6
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel7
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel8
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/l2picfaq
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/l2tabu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/l2tabu-english
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/l2tabu-french
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/l2tabu-it
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/l2tabu-spanish
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/labbook
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/labelcas
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/labels
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/labels/test
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lastpage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex2e-help-texinfo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latexcheat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latexcheat-esmx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latexcheat-ptbr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-course
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-course/Graphics
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latexdiff
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latexdiff/contrib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latexdiff/example
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-doc-ptr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/inputs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-referenz
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-tabellen
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-tipps-und-tricks
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-veryshortguide
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-web-companion/apc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex30
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex31
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex32
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/l2hexa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathImages
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathThumb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-web-companion/intro
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2html
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xml
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/SGMLS
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/layaureo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/layouts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lazylist
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lcd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lcg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lcyw
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/leading
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/leaflet
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ledmac
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ledmac/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/leftidx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lettre
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lettrine
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lewis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lexikon
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lhelp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/linegoal
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lineno
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/linguex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lipsum
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/listbib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/listing
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/listings
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/listings-ext
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/listliketab
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/listofsymbols
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lithuanian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/liturg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lkproof
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/locality
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/localloc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/logical-markup-utils
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/logpap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lsc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-bulgarian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-bulgarian/src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-chinese
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-chinese/src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-dutch
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-english
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-finnish
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-finnish/src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-french
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-german
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-italian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-japanese
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-korean
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-mongol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-mongol/src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-persian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-polish
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-portuguese
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-russian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-slovak
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-slovenian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-slovenian/src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-spanish
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-spanish/fuente
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-spanish/fuente/src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-thai
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-turkish
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-ukr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-vietnamese
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/lshort-vietnamese/src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ltabptch
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ltxdockit
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ltxindex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ltxnew
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/macqassign
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mafr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/magaz
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/magyar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mailing
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mailmerge
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/makebarcode
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/makebox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/makecell
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/makecmds
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/makedtx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/makeglos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/makeplot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/manuscript
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/margbib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/marginnote
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mathcomp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mathdesign
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mathdesign/mdbch
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mathdesign/mdput
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mathdesign/mdugm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mathexam
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mathmode
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mathmode/images
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mathpazo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mathspic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mattens
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/maybemath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mcaption
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mceinleger
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mcite
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mciteplus
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mdframed
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mdwtools
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/memexsupp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/memoir
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/MemoirChapStyles
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mentis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/menu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/metalogo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/metaplot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/metaplot/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/method
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/metre
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mflogo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mfnfss
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mfpic4ode
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mfpic4ode/demo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mftinc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mh
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mhchem
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mhequ
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/microtype
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/midpage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/miller
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/minibox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/minipage-marginpar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/miniplot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/minitoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/minted
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/minutes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mla-paper
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mlist
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mltex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mmap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mnsymbol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/moderncv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/moderncv/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/modref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/modroman
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mongolian-babel
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/montex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/montex/mfinput/bithe
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/moresize
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/moreverb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/movie15
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mparhack
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ms
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/msc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/msg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mslapa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mtgreek
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/muench/hrefhide
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/multibbl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/multibib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/multicap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/multiobjective
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/multirow
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/munich
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/musixlyr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/muthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mwcls
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/mylatexformat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/nag
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/namespc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/natbib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/nath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ncclatex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ncctools
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/nddiss
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/nddiss/example-v1.3
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/needspace
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/newcommand
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/newfile
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/newlfm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/newspaper
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/newvbtm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/newverbs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/nfssext-cfr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/niceframe
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/nicetext
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/nicetext/demo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/nicetext/docsrc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/nih
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/nlctdoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/noitcrul
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/nolbreaks
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/nomencl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/nomentbl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/nonfloat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/nopageno
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/nostarch
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/notes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/notes2bib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/notoccite
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/nrc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ntabbing
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ntgclass
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ntheorem
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ntheorem-vn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ntheorem-vn/src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/numname
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/numprint
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/oberdiek
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/oberdiek/test
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/objectz
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ocgtools
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ocgtools/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ocr-latex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/octavo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ogham
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/oldstyle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/onlyamsmath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/onrannual
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/opcit
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/optional
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ordinalpt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/othello
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/otibet
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ot-tableau
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/outline
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/outliner
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/overpic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pagecont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pagenote
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pagerange
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pageslts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/paper
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/papercdcase
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/papermas
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/papertex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/papertex/example
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/papertex/example/img
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/papertex/example/img/weather
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/paralist
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/parallel
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/paresse
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/parrun
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/patchcmd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pauldoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pax
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pb-diagram
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pbox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pbsheet
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pbsheet/xpl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pbsheet/xpl/img
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pbsheet/xpl/pgm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pdf14
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pdfcomment
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pdfcprot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pdf-forms-tutorial-de
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pdf-forms-tutorial-de/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pdf-forms-tutorial-de/forms-src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pdf-forms-tutorial-en
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pdf-forms-tutorial-en/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pdf-forms-tutorial-en/forms-src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pdfjam
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pdfmarginpar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pdfpages
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pdfscreen
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pdfslide
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pdfsync
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pdftricks
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pdfwin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pdfx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pecha
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/perception
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/perltex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/permute
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/petiteannonce
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/petri-nets
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pgfopts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pgfplots
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pgfplots/figures
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pgfplots/gallery
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pgfplots/gnuplot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pgfplots/plotdata
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pgf-soroban
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pgf-umlsd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/philex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/philosophersimprint
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/photo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/picinpar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pict2e
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pigpen
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pinlabel
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pinlabel/src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pittetd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/placeins
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/plantslabels
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/plantslabels/doc/pdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/plantslabels/doc/tex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/plantslabels/example/pdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/plantslabels/example/tex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/plari
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/plates
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/play
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/plweb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pmgraph
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/poemscol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/polski
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/polyglot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/polynom
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/polynomial
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/polytable
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/postcards
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/powerdot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/powerdot-FUBerlin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ppower4
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ppower4/demo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ppower4/edemo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ppower4/exampled
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ppower4/examplee
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ppower4/leveldemo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ppr-prv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pracjourn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/preprint
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/prerex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/prerex/doc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/prerex/patches
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/presentations
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/presentations/images/beamer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/presentations/images/pd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/presentations/images/pdfscreen
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/prettyref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/preview
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/proba
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/probsoln
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/probsoln/samples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/procIAGssymp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/program
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/progress
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/properties
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/prosper
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/protex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/protocol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/psbao
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pseudocode
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/psfrag
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/psfrag-italian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/psfragx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/psgo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/psnfss
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/psnfss/test
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pspicture
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pst2pdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pst-calendar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pst-exa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pstool
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pstool/subdir
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pst-pdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pstricks_calcnotes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pstricks_calcnotes/Convert_PstricsCode_To_Pdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pstricks_calcnotes/For_Pdf_Output
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pstricks_calcnotes/For_Ps_Output
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/pst-vowel
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/psu-thesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ptptex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/qcm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/qobitree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/qstest
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/qsymbols
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/qtree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/quotchap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/quotmark
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/randbild
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/randtext
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/rccol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/rcs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/rcsinfo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/rcs-multi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/recipe
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/recipecard
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/rectopma
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/refcheck
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/refman
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/refstyle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/regcount
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/register
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/repeatindex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/revtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/revtex4
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/revtex/aip
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/revtex/aps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/revtex/auguide
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/revtex/sample/aip
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/revtex/sample/aps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/revtex/source
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/rjlparshap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/rmpage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/robustcommand
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/robustindex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/romannum
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/rotating
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/rotfloat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/rotpages
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/rotpages/Documentation
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/rotpages/Examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/roundbox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/rsc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/rst
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/rtkinenc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/rtklage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/r_und_s
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ryethesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sageep
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sanskrit
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sansmath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sauerj
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sauterfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/savefnmark
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/savetrees
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/scale
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/scalebar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/schemabloc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/scientificpaper
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sciposter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sciposter/sciposterexample
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sciposter/sciposterexample/auto
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sciwordconv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/screenplay
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sdrt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sectionbox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sectionbox/example
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sectsty
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/semantic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/seminar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/semioneside
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/seqsplit
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/seuthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/seuthesis/a3cover
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/seuthesis/figures
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/seuthesis/zharticle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sf298
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sffms
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sfg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sgame
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/shadethm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/shipunov
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/shorttoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/show2e
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/showexpl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/showlabels
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/shuffle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sidecap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sides
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/siggraph
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/silence
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/simplecd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/simplecv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/simplewick
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/SIstyle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/SIunits
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/siunitx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/skak
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/skeycommand
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/skeyval
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/slantsc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/smalltableof
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/smartref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/snapshot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/songbook
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/songbook/contrib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/songbook/contrib/CarolBook
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/songbook/contrib/crd2sb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sort-by-letters
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/soton
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/soul
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/spanish
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/spanish/doc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/spanish-mx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/spanish/source
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/spanish/tex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sparklines
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/spie
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/splitbib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/splitindex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/spotcolor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/spreadtab
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/spverbatim
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/srcltx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sseq
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ssqquote
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/standalone
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/statistik
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stdclsdv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stdpage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/steinmetz
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stellenbosch
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stellenbosch/templates
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stex/assignment
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stex/cmathml
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stex/cnx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stex/dcm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stex/example
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stex/example/background
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stex/example/paper
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stex/example/test
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stex/mikoslides
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stex/modules
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stex/omd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stex/omdoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stex/omtext
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stex/presentation
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stex/problem
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stex/reqdoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stex/sproof
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stex/sref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stex/statements
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stringstrings
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/struktex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sttools
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sttools/doc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/stubs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/subdepth
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/subeqn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/subeqnarray
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/subfig
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/subfigure
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/subfloat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/substr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sudoku
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sudokubundle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/sugconf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/supertabular
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/susy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/svgcolor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/svg-inkscape
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/svn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/svninfo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/svn-multi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/svn-prov
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/swebib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/swimgraf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/syllogism
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/synproof
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/syntax
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/syntrace
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/synttree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/Tabbing
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tableaux
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tablenotes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tablists
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tablor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tablor/Figures
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tabls
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tabto-ltx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tabularborder
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tabularcalc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tabularew
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tabulary
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tabvar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/talk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/t-angles
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tapir
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tcldoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tdclock
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tdsfrmath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/technics
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ted
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/templates-fenn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/templates-sommer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tengwarscript
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tensor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/termlist
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/teubner
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tex-font-errors-cheatsheet
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tex-label
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/texmate
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/texments
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/texpower
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/texpower/contrib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/texpower/tpslifonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/texshade
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/textcase
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/textfit
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/textopo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/textpos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/textpos/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/theoremref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/thesis-titlepage-fhac
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/thinsp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/thmbox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/thmtools
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/threeparttable
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/threeparttablex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/thumb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/thumby
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/thuthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/thuthesis/example
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/thuthesis/example/data
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/thuthesis/example/figures
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/thuthesis/example/ref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ticket
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tikz-3dplot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tikz-inet
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tikz-qtree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tikz-timing
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/timesht
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/titlepages
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/titlepic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/titleref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/titlesec
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/titling
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tkz-doc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tkz-linknodes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tkz-linknodes/doc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tkz-orm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tkz-tab
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tlc2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tocbibind
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tocloft
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tocvsec2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/todo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/todonotes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tokenizer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/toolbox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tools
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/topfloat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/toptesi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/totcount
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/totpages
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tpslifonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/trajan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/trfsigns
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/trimspaces
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/trivfloat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/trsym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/truncate
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tufte-latex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tufte-latex/graphics
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/tugboat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/turkmen
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/turnstile
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/twoinone
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/twoup
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/type1cm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/typedref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/typehtml
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/typogrid
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/uaclasses
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ucdavisthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ucdavisthesis/Example
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ucs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ucs/config
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ucthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/uebungsblatt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/uiucthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ulqda
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/umich-thesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/uml
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/umlaute
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/umoline
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/umthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/underlin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/underscore
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/undolabl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/unicode-math
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/units
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/unitsdef
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/upmethodology
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/url
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/urlbst
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ushort
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ut-thesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/uwthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/varindex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/varsfromjobname
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/verbatimbox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/verbatimcopy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/verbdef
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/verse
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/vhistory
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/visualfaq
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/visualfaq/source
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/vita
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/vmargin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/volumes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/vpe
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/vrsion
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/vwcol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/vxu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/wallpaper
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/wallpaper/example
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/wallpaper/example/auto
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/warpcol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/was
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/wasysym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/webguide
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/widetable
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/williams
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/wnri
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/wordlike
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/wrapfig
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/xargs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/xcolor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/xdoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/xfor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/xifthen
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/xkeyval
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/xmpincl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/xnewcommand
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/xoptarg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/xpackages
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/xpackages/xbase
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/xpackages/xtras
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/xskak
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/xtab
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/xwatermark
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/xwatermark/Graphics
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/xyling
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/xypdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/xytree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/yafoot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/yagusylo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ydoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/yfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/yhmath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/york-thesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/youngtab
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/yplan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/zed-csp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/ziffer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/zwgetfdate
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/latex/zwpagelayout
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/lualatex/luainputenc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/luatex/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/luatex/hyph-utf8
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/luatex/lualibs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/luatex/luamplib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/luatex/luaotfload
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/luatex/luatexbase
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/luatex/luatextra
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/automata
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/base/source-manual
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/base/source-tutorial
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/bbcard
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/blockdraw_mp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/bpolynomial
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/cmarrows
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/drv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/drv/doc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/drv/sample
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/drv/template
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/dviincl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/epsincl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/expressg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/exteps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/featpost
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/featpost/bashscript
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/featpost/doc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/featpost/example/bugtrack
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/featpost/example/highmemory
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/featpost/example/repeated
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/featpost/example/standard
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/featpost/example/tug04
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/featpost/galrey
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/featpost/jpeg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/featpost/latex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/featpost/macro
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/featpost/nontextualpng
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/featpost/png
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/featpost/typesetinspace
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/featpost/xcmd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/garrigues
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/hatching
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/latexmp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/makecirc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/metago
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/metaobj
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/metapost-examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/metauml
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/metauml/metauml_manual
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/metauml/metauml_manual/fig
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/mpattern
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/mpman-ru
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/piechartmp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/piechartmp/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/slideshow
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/splines
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/suanpan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/textpath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/metapost/venn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/mex/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/mex/utf8mex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/mex/utf8mex/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/omega/antomega
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/omega/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/omega/ocherokee
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/otherformats/alatex/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/otherformats/jadetex/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/otherformats/psizzl/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/otherformats/startex/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/otherformats/texsis/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/otherformats/xmltex/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/otherformats/xmltex/xmlplay
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/pdftex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/pdftex/manual
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/pdftex/manual/samplepdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/pdftex/pdftex-pdfkeys
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/pdftex/thanh/ext
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/plain/cweb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/plain/fontch
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/plain/font-change
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/plain/gentle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/plain/graphics-pln
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/plain/gustlib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/plain/harvmac
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/plain/hyplain
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/plain/impatient
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/plain/impatient-fr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/plain/js-misc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/plain/js-misc/xfig
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/plain/metatex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/plain/metatex/mtpaper
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/plain/mkpattern
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/plain/newsletr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/plain/pgfplots
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/plain/pitex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/plain/plnfss
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/plain/resumemac
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/plain/texbytopic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/plain/treetex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/plain/tugboat-plain
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/plain/varisize
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/ptex/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/ptex/jvf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/ptex/pbibtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/asymptote-by-example-zh-cn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/figure-src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/asymptote-faq-zh-cn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/asymptote-faq-zh-cn/src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/asymptote-faq-zh-cn/src/figures
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/bundledoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/de-macro
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/epspdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/epspdf/images
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/fig4latex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/fig4latex/figs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/findhyph
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/fontools
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/fontools/examples/berling
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/fontools/examples/frutiger
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/fontools/examples/palatinox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/fragmaster
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/fragmaster/example
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/gustprog
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/latex2man
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/latexmk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/latexmk/example_rcfiles
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/latexmk/extra-scripts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/lua-alt-getopt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/lua-alt-getopt/tests
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/makeindex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/mkgrkindex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/patgen2-tutorial
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/pdfcrop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/pkfix
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/pkfix-helper
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/purifyeps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/texcount
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/texdraw
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/support/texloganalyser
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/xelatex/arabxetex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/xelatex/arabxetex/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/xelatex/fontwrap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/xelatex/mathspec
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/xelatex/persian-bib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/xelatex/philokalia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/xelatex/polyglossia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/xelatex/xecjk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/xelatex/xecjk/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/xelatex/xecolour
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/xelatex/xecyr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/xelatex/xeindex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/xelatex/xepersian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/xelatex/xetex-itrans
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/xelatex/xgreek
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/xelatex/xltxtra
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/xelatex/xunicode
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/xetex/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/xetex/xesearch
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/xetex/xetexfontinfo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/xetex/xetex-pstricks
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/xetex/xetexref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/doc/xetex/zhspacing
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/antiqua
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/antp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/arphic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/avantgar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/bookman
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/brushscr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/cm-super
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/colorsep
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/courier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/cs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/dvipsconfig
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/esint-type1
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/garuda-c90
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/gastex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/gothic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/grotesq
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/helvetic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/hfbright
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/initials
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/libertine
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/mathdesign
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/multi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/musixps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/musixtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/ncntrsbk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/norasi-c90
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/omega
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/palatino
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/psfrag
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pspicture
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-3dplot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-bar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-barcode
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-bezier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-blur
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-circ
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-coil
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-cox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-electricfield
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-eucl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-fractal
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-fun
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-func
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-geo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-ghsb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-grad
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-knot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-light3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-magneticfield
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-math
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-mirror
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-node
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-optexp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pstricks
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pstricks-add
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-slpe
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-solides3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-spectra
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-text
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/pst-vue3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/symbol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/tex-ps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/times
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/uhc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/xcolor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/xypic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/zapfchan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/dvips/zapfding
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/adobe/avantgar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/adobe/bookman
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/adobe/courier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/adobe/helvetic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/adobe/ncntrsbk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/adobe/palatino
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/adobe/symbol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/adobe/times
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/adobe/utopia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/adobe/zapfchan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/adobe/zapfding
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/arabi/arabeyes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/arkandis/baskervald
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/arkandis/libris
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/arkandis/romande
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/arkandis/venturis2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/arkandis/venturisold
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/bitstrea/charter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/groff
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/hoekwater/context
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/hoekwater/manfnt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/hoekwater/mflogo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/hoekwater/stmaryrd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/ibm/courier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/ibm/times
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/itc/psafm/stonesan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/jmn/hans
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/mathdesign/mdbch
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/mathdesign/mdput
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/mathdesign/mdugm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cmextra
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cyrillic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/euler
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/latxfont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/amsfonts/symbols
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/antp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/antt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/archaic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/arev
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/augie
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/auncial-new
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/aurical
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/bera
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/brushscr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/carolmin-ps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/chemarrow
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/cjhebrew
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/cm-super
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/cryst
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/cyklop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/dictsym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/epigrafica
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/figbas
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/fonetika
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/fourier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/fouriernc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/fpl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/gentium
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/gfsartemisia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/gfsbaskerville
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/gfsbodoni
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/gfscomplutum
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/gfsdidot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/gfsneohellenic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/gfsporson
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/gfssolomos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/gothic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/grverb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/hfbright
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/ibygrk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/initials
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/itrans
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/iwona
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/kerkis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/knitting
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/kpfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/kurier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/libertine
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/linearA
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/lm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/marvosym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/mathpazo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/ocherokee
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/omega
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/phaistos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/pl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/pxfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/rsfs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/semaphor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/skaknew
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/tabvar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/thailatex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/trajan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/txfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/txfontsb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/velthuis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/wasy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/public/xypic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/uhc/umj
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/urw/antiqua
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/urw/avantgar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/urw/bookman
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/urw/courier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/urw/grotesq
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/urw/helvetic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/urw/ncntrsbk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/urw/palatino
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/urw/symbol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/urw/times
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/urw/zapfchan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/urw/zapfding
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/vntex/chartervn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/vntex/grotesqvn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/vntex/urwvn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/afm/vntex/vntopia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/cid/fontforge
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/cmap/adobemapping
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ai0/CMap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ToUnicode
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/antp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/antt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/arabi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/arev
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/baskervald
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/c90
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/cbfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/ccicons
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/cfr-lm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/chessfss
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/cjhebrew
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/cm-lgc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/cm-super
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/cm-unicode
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/context
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/cs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/cyklop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/epigrafica
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/fontools
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/gentium
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/gfsartemisia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/gfsbaskerville
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/gfsbodoni
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/gfscomplutum
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/gfsdidot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/gfsneohellenic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/gfsporson
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/gfssolomos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/groff
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/hfbright
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/ibygrk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/inconsolata
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/iwona
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/jmn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/kerkis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/kpfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/kurier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/libertine
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/libris
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/lithuanian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/lm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/ly1
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/mnsymbol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/pl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/romande
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/semaphor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/tengwarscript
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/txfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/txfontsb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/venturisadf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/vntex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/dvips/xypic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/pdftex/kpfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/pdftex/vntex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/enc/t2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/fea/context
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvipdfm/lm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/allrunes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/amsfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/antiqua
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/antp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/antt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/arabi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/arabtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/archaic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/arev
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/arphic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/ascii
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/augie
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/auncial-new
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/aurical
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/avantgar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/baskervald
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/belleek
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/bera
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/bookman
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/brushscr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/burmese
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/carolmin-ps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/cbfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/ccicons
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/cc-pl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/cfr-lm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/chemarrow
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/cjhebrew
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/cm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/cmcyr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/cm-lgc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/cmll
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/cm-super
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/cm-unicode
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/context
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/courier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/cs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/cyklop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/dictsym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/doublestroke
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/dozenal
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/epigrafica
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/epiolmec
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/esint-type1
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/esvect
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/ethiop-t1
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/eurofont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/eurosym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/fge
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/figbas
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/foekfont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/fonetika
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/fourier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/garuda-c90
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/gfsartemisia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/gfsbaskerville
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/gfsbodoni
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/gfscomplutum
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/gfsdidot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/gfsneohellenic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/gfsporson
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/gfssolomos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/gothic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/groff
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/grotesq
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/grverb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/helvetic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/hfbright
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/ibygrk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/inconsolata
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/initials
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/iwona
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/jmn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/kerkis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/knitting
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/kpfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/kurier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/libertine
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/libris
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/linearA
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/lithuanian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/lm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/lxfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/ly1
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/manfnt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/marvosym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/mathdesign
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/mflogo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/mnsymbol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/montex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/musixtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/ncntrsbk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/norasi-c90
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/ocherokee
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/oinuit
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/omega
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/palatino
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/phaistos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/pigpen
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/pl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/pslatex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/psnfss
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/pxfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/recycle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/romande
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/rsfs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/sanskrit
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/semaphor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/skaknew
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/staves
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/stmaryrd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/symbol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/tabvar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/tengwarscript
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/times
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/tipa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/trajan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/txfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/txfontsb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/uhc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/velthuis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/venturis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/venturis2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/venturisold
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/venturissans
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/venturissans2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/vntex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/wasy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/xypic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/yhmath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/zapfchan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/dvips/zapfding
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/fontname
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/glyphlist
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/luatex/context
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/pdftex/context
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/pdftex/gentium
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/vtex/bera
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/vtex/cm-super
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/vtex/dictsym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/vtex/mnsymbol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/map/vtex/skaknew
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/misc/cns
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/context
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/harvardkyoto
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/polyglossia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/velthuis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/xepersian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/xetex-itrans
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/ofm/public/cm-lgc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/ofm/public/ethiop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/ofm/public/ocherokee
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/ofm/public/oinuit
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/ofm/public/omega
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/ofm/public/otibet
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/antt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/Asana-Math
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/cyklop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsartemisia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsbaskerville
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsbodoni
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfscomplutum
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsdidot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsneohellenic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfsporson
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gfssolomos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/inconsolata
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/iwona
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/kurier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/libertine
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/lm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/oldstandard
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/phaistos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/philokalia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/semaphor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/skaknew
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/stix
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/umtypewriter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/xits
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/ovf/public/cm-lgc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/ovf/public/ethiop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/ovf/public/ocherokee
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/ovf/public/oinuit
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/ovf/public/omega
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/ovf/public/otibet
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/ovp/public/ethiop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/ovp/public/ocherokee
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/ovp/public/omega
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/ovp/public/otibet
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/pk/ljfour/public/cm/dpi600
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/pk/ljfour/public/cm/dpi720
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/sfd/dnp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/sfd/ttf2pk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/jknappen/ec
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/jknappen/fc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/lh/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/lh/lh-conc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/lh/lh-lcy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/lh/lh-ot2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/lh/lh-t2a
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/lh/lh-t2b
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/lh/lh-t2c
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/lh/lh-t2d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/lh/lh-x2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/lh/lh-XSlav
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/lh/nont2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/lh/specific
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/ptex/ascgrp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/ptex/jis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/ptex/nmin-ngoth
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/ptex/standard
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/allrunes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cmextra
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/amsfonts/dummy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/amsfonts/symbols
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/ar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/arabtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/archaic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/armenian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/astro
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/aurical
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/bangtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/barcodes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/bayer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/bbding
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/bbm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/bbold
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/boisik
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/bookhands
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/calligra
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/casyl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/cbcoptic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/cbfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/cc-pl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/chemarrow
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/chess
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/circ
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/clock
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/cm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/cmbright
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/cmcyr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/cmextra
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/cmll
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/cmpica
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/concmath-fonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/concrete
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/cryst
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/cs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/ctib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/dancers
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/dice
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/dingbat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/doublestroke
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/dozenal
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/ean
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/ecc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/eiad-ltx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/elvish
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/esint
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/esvect
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/ethiop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/euro-ce
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/eurosym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/euxm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/feyn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/fge
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/frcursive
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/genealogy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/go
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/gothic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/greenpoint
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/hands
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/ibygrk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/ifsym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/itrans
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/jablantile
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/kdgreek
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/kixfont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/knitting
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/knuthotherfonts/committee
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/knuthotherfonts/halftone
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/knuthotherfonts/mfbook
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/kpfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/latex-fonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/lfb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/lxfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/malayalam
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/malayalam/effects
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/mathabx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/mflogo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/misc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/mnsymbol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/montex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/musixps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/musixtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/niceframe
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/nkarta
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/ogham
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/oldlatin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/orkhun
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/othello
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/otibet
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/pacioli
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/pigpen
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/pl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/punk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/recycle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/rsfs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/sanskrit
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/sauter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/semaphor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/semaphor/metafont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/shuffle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/skak
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/skull
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/stmaryrd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/tapir
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/tipa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/trsym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/universa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/velthuis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/wasy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/wnri
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/wsuipa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/xbmc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/xq
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/xypic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/public/yhmath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/source/vntex/vnr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/adobe/avantgar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/adobe/bookman
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/adobe/courier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/adobe/ly1
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/adobe/palatino
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/adobe/symbol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/adobe/times
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/adobe/utopia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/adobe/zapfchan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/adobe/zapfding
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/arabi/farsiweb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/cg/courier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/cg/times
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/avantgar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/bookman
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/courier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/helvetic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/ncntrsbk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/palatino
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/symbol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/times
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/zapfchan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/zapfding
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/groff
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/groff/avantgar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/groff/bookman
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/groff/courier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/groff/helvetic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/groff/ncntrsbk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/groff/palatino
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/groff/times
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/groff/zapfchan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/hoekwater/context
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/jknappen/fc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/jmn/hans
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/mathdesign/mdbch
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/mathdesign/mdput
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/mathdesign/mdugm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/monotype/symbol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/ptex/ascgrp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/ptex/dvips
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/ptex/jis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/ptex/morisawa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/ptex/nmin-ngoth
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/ptex/standard
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/ae
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/allrunes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/dummy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/symbols
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/antp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/antt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/ar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/arabtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/archaic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/arev
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/armenian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/ascii
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/astro
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/augie
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/auncial-new
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/aurical
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/bangtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/barcodes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/bayer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/bbding
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/bbm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/bbold
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/bera
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/bgreek
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/blacklettert1
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/boisik
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/brushscr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/burmese
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/calligra
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/casyl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/cbcoptic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/ccicons
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/cc-pl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/chemarrow
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/circ
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/cjhebrew
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/clock
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/cm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/cmbright
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/cmcyr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/cmextra
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/cmll
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/cmpica
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/concmath-fonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/concrete
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/cryst
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/cs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/ctib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/cyklop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/dancers
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/dice
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/dictsym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/dingbat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/doublestroke
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/dozenal
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/ean
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/ecc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/eco
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/elvish
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/epiolmec
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/esint
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/esvect
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/ethiop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/eulervm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/euro-ce
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/eurosym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/euxm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/feyn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/fge
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/figbas
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/foekfont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/fonetika
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/fourier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/fouriernc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/frcursive
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/garuda-c90
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/genealogy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/gentium
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/gfsbaskerville
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/gfscomplutum
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/gfsporson
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/gfssolomos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/go
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/gothic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/greenpoint
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/grverb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/hands
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/hfoldsty
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/ibygrk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/ifsym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/inconsolata
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/initials
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/itrans
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/iwona
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/kdgreek
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/kerkis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/kixfont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/knitting
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/kpfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/kurier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/latex-fonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/lfb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/libertine
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/linearA
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/lithuanian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/lm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/lxfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/malayalam
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/marvosym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/mathabx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/mathpazo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/mflogo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/misc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/montex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/musixps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/musixtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/niceframe
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/nkarta
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/norasi-c90
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/ocherokee
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/ogham
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/oinuit
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/omega
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/orkhun
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/othello
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/otibet
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/pacioli
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/phaistos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/pigpen
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/pl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/pslatex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/punk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/pxfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/qpxqtx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/recycle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/rsfs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/sanskrit
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/semaphor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/shuffle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/skak
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/skaknew
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/staves
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/stmaryrd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/tabvar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/tipa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/trajan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/trsym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/txfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/txfontsb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/universa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/velthuis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/wasy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/wnri
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/wsuipa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/xbmc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/xq
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/xypic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/public/yhmath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/uhc/umj
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/uhc/uwmj
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/uhc/wmj
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/urw35vf/avantgar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/urw35vf/bookman
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/urw35vf/courier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/urw35vf/palatino
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/urw35vf/symbol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/urw35vf/times
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/urw35vf/zapfchan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/urw35vf/zapfding
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/urw/antiqua
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/urw/grotesq
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/vntex/arevvn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/vntex/chartervn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/vntex/cmbrightvn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/vntex/concretevn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/vntex/grotesqvn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/vntex/txttvn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/vntex/vnr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/vntex/vntopia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/zhmetrics/cyberb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/zhmetrics/gbk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/zhmetrics/gbkfs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/zhmetrics/gbkhei
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/zhmetrics/gbkkai
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/zhmetrics/gbkli
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/zhmetrics/gbksong
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/zhmetrics/gbkyou
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/zhmetrics/unifs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/zhmetrics/unihei
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/zhmetrics/unikai
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/zhmetrics/unili
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/zhmetrics/unisong
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/tfm/zhmetrics/uniyou
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/hoekwater/lmextra
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/Asana-Math
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/belleek
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gentium
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/itrans
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/truetype/public/junicode
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/adobe/courier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/adobe/utopia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arabi/farsiweb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/libris
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/romande
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturisold
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/bitstrea/charter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/groff
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/hoekwater/context
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/hoekwater/manfnt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/hoekwater/stmaryrd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/jmn/hans
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/mathdesign/mdbch
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/mathdesign/mdput
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/mathdesign/mdugm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/ptex/ascgrp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/allrunes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/antt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/arabtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/archaic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/arev
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ascii
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/augie
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/auncial-new
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/aurical
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/belleek
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/bera
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/brushscr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/burmese
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/carolmin-ps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbcoptic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cbfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ccicons
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cc-pl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/chemarrow
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cjhebrew
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmcyr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cmll
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-super
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cryst
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cyklop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/dictsym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/doublestroke
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/dozenal
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/epigrafica
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/epiolmec
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/esint-type1
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/esvect
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/eurosym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fge
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/figbas
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/foekfont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fonetika
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fourier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/fpl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsartemisia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsbaskerville
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsbodoni
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfscomplutum
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsdidot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsneohellenic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfsporson
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gfssolomos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/gothic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/grverb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/hfbright
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ibygrk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/inconsolata
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/initials
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/itrans
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/iwona
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kerkis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/knitting
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kpfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/kurier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/libertine
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/linearA
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/lxfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/marvosym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mathpazo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/mnsymbol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/montex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/musixtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/ocherokee
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/oinuit
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/omega
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/phaistos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pigpen
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/pxfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/recycle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/rsfs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/sanskrit
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/semaphor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/skaknew
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/staves
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tabvar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tapir
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/thailatex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tipa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/trajan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/txfontsb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/velthuis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/wasy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/xypic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/yhmath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/uhc/umj
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/antiqua
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/avantgar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/bookman
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/courier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/grotesq
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/ncntrsbk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/palatino
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/symbol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/times
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/zapfchan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/zapfding
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/arevvn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/chartervn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/concretevn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/grotesqvn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/txttvn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/urwvn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vnr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/type1/vntex/vntopia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/adobe/avantgar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/adobe/bookman
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/adobe/courier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/adobe/palatino
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/adobe/times
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/adobe/utopia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/adobe/zapfchan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/arkandis/baskervald
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/arkandis/libris
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/arkandis/romande
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/arkandis/venturisold
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/bitstrea/charter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/cg/courier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/cg/times
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/avantgar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/bookman
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/courier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/helvetic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/ncntrsbk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/palatino
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/times
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/zapfchan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/mathdesign/mdbch
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/mathdesign/mdput
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/mathdesign/mdugm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/monotype/helvetic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/ptex/jis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/ptex/morisawa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/ptex/nmin-ngoth
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/ptex/standard
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/ae
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/arev
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/augie
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/bera
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/bgreek
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/blacklettert1
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/brushscr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/cjhebrew
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/cmcyr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/dozenal
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/eco
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/epigrafica
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/eulervm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/fourier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/fouriernc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/gfsbaskerville
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/gfscomplutum
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/gfsporson
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/gfssolomos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/gothic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/grverb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/hfoldsty
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/kerkis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/kpfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/libertine
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/mathpazo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/pslatex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/pxfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/qpxqtx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/tengwarscript
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/txfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/txfontsb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/public/yhmath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/uhc/uwmj
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/uhc/wmj
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/urw35vf/avantgar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/urw35vf/bookman
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/urw35vf/courier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/urw35vf/palatino
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/urw35vf/times
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/urw35vf/zapfchan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/urw/antiqua
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/urw/grotesq
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/vntex/chartervn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/vntex/urwvn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/fonts/vf/vntex/vntopia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/arsclassica
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/babel
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/bibarts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/confproc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/disser
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/dtk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/expl3
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/gatech-thesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/gmdoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/index
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/iso
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/juraabbrev
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/latex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/memoir
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/minitoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/mkgrkindex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/multibib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/nomencl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/nomentbl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/nostarch
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/plain
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/repeatindex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/songbook
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/startex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/makeindex/xdoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metafont/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metafont/config
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metafont/feynmf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metafont/mfpic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metafont/mftoeps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metafont/misc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metafont/roex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/automata
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/bbcard
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/blockdraw_mp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/bpolynomial
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/cmarrows
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/config
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/context/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/context/font
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/context/third/gnuplot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/drv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/dviincl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/epsincl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/expressg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/exteps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/featpost
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/feynmf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/frcursive
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/garrigues
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/hatching
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/latexmp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/makecirc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/metago
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/metaobj
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/metaplot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/metauml
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/mfpic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/misc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/mpattern
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/nkarta
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/piechartmp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/slideshow
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/splines
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/suanpan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/support
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/support/charlib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/tabvar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/textpath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/metapost/venn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/mft/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/omega/ocp/antomega
mkdir -p %{buildroot}%{_texdir}/texmf-dist/omega/ocp/antomega/latin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/omega/ocp/char2uni
mkdir -p %{buildroot}%{_texdir}/texmf-dist/omega/ocp/ethiop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/omega/ocp/misc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/omega/ocp/ocherokee
mkdir -p %{buildroot}%{_texdir}/texmf-dist/omega/ocp/oinuit
mkdir -p %{buildroot}%{_texdir}/texmf-dist/omega/ocp/omega
mkdir -p %{buildroot}%{_texdir}/texmf-dist/omega/ocp/otibet
mkdir -p %{buildroot}%{_texdir}/texmf-dist/omega/ocp/uni2char
mkdir -p %{buildroot}%{_texdir}/texmf-dist/omega/otp/antomega
mkdir -p %{buildroot}%{_texdir}/texmf-dist/omega/otp/antomega/latin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/omega/otp/char2uni
mkdir -p %{buildroot}%{_texdir}/texmf-dist/omega/otp/ethiop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/omega/otp/misc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/omega/otp/ocherokee
mkdir -p %{buildroot}%{_texdir}/texmf-dist/omega/otp/omega
mkdir -p %{buildroot}%{_texdir}/texmf-dist/omega/otp/otibet
mkdir -p %{buildroot}%{_texdir}/texmf-dist/omega/otp/uni2char
mkdir -p %{buildroot}%{_texdir}/texmf-dist/pbibtex/bib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/pbibtex/bst
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/accfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/authorindex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/bibexport
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/bundledoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/cachepic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/context/lua
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/context/perl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/context/ruby
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/context/ruby/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/context/ruby/base/kpse
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/context/ruby/graphics
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/context/stubs/mswin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/context/stubs/source
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/context/stubs/unix
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/de-macro
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/dviasm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/epspdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/epstopdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/fig4latex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/findhyph
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/fontools
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/fragmaster
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/glossaries
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/jmlr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/latex2man
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/latexdiff
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/latexmk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/listings-ext
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/lua-alt-getopt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/luaotfload
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/mathspic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/mkgrkindex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/oberdiek
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/pax
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/pdfcrop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/pdfjam
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/perltex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/pgfplots
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/pkfix
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/pkfix-helper
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/ppower4
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/pst2pdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/pst-pdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/purifyeps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/shipunov
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/splitindex/perl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/svn-multi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/tex4ht
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/texcount
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/texloganalyser
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/thumbpdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/ulqda
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/vpe
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/xetex/perl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/xetex/perl/lib/PDF
mkdir -p %{buildroot}%{_texdir}/texmf-dist/scripts/xetex/perl/lib/PDF/Reuse
mkdir -p %{buildroot}%{_texdir}/texmf-dist/source/latex/koma-script
mkdir -p %{buildroot}%{_texdir}/texmf-dist/source/latex/koma-script/doc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/source/latex/koma-script/doc/bin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/source/latex/koma-script/doc/english
mkdir -p %{buildroot}%{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/base/unix
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/bin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/avantgar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/bookman
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/courier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/helvetic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/mathppl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/mathptmx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/ncntrsbk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/palatino
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/ppalatino
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/pslatex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/symbol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/times
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/utopia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/zapfchan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/zapfding
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/ae
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/ams/euler
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/antt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/arabi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/arev
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/bitstrea
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/bitstrea/charter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/cc-pl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/chartervn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/chess
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/cjk/b5ka
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/cm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/cm/sauter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/concrete
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/cs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/currency
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/cyklop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/cyrillic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/cyrillic/cmcyr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/ec
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/aliase/mathtime
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/eulervm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/euro
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk/gbkcy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk/gbkfs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk/gbkhei
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk/gbkkai
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk/gbkli
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk/gbkshu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk/gbksu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk/gbkxh
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk/gbkxk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk/gbkxw
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk/gbkyao
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk/gbkyou
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/greek/ibygrk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/hebrew
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/iwona
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/iwona/cs-iwonacap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/iwona/ec-iwonacap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/iwona/qx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/iwona/t5-iwonacap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/iwona/texnansi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/jknappen/tc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/cs-iwona
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/cs-iwonacap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/ec
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/ex-iwona
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/exp-iwona
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/greek-iwona
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/mi-iwona
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/qx-iwona
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/qx-iwonacap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/rm-iwona
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/sy-iwona
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/t2a-iwona
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/t2b-iwona
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/t2c-iwona
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/t5-iwona
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/t5-iwonacap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/texnansi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/wncy-iwona
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/latex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lh/lh-t2a
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/libertine
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lm/lm-ec
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lm/lm-qx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lm/lm-rep-cmin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lm/lm-rep-cmrm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lm/lm-rep-cmsc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lm/lm-rep-csin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lm/lm-rep-csrm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lm/lm-rep-cstt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lm/lm-rep-plrm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lm/lm-rep-t5psn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lm/pre2005
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/marvosym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/mathdesign
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/mathpple
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/mathtime
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/pazo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/pl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/pxfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/qfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/sw
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/times
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/tipa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/txfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex/arevvn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex/chartervn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex/classicovn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex/cmbrightvn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex/comicsansvn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex/concretevn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex/garamondvn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex/grotesqvn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex/mscorevn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex/urwvn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex/utopiavn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex/vnr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/ascii/manfnt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/cp1256/charset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/css/emacspeak/cm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/dbcs/cjk/b5ka
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/gb2312/charset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/gbk/charset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/html-speech/charset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/charset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/charset/uni
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/chess
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/cm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/devanagari
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/euro
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/go
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/html/charset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/ipa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/mathtime
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/mongolian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/ps2mf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/sw
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/tibetan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/xypic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/2/charset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/2/html/charset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/5/charset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/5/cm/sauter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/5/cyrillic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/5/cyrillic/cmcyr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/5/html/charset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/5/lh/lh-t2a
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/6/charset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/6/html/charset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/7/charset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/8/hebrew
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/jsml/charset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/koi/8r/charset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/koi/8r/lh/lh-t2a
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/mozilla/charset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/mozilla/charset/mnemonic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/mozilla/charset/native
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/ooffice/charset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/share/adobe/helvetic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/symbol/charset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/symbol/cyrillic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/symbol/hebrew
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/symbol/mathtime
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/adobe/courier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/adobe/helvetic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/adobe/mathptm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/adobe/palatino
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/adobe/symbol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/adobe/times
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/adobe/zapfding
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/ae
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/ams/cyrillic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/ams/euler
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/ams/symbols
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/antt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/arabi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/arev
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/bbold
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/bitstrea/charter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/cbgreek
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/charset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/chess
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/cjk/b5ka
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/cjk/gbksong
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/cjk/gbksong/long
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/cjk/utf8
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/cm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/concrete
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/cs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/currency
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/cyklop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/cyrillic/cmcyr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/dstroke
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/greek/ibygrk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/hebrew
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/html/charset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/iwona
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/jknappen/tc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/latex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/lh/lh-t2a
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/libertine
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/lm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/lm/pre2005
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/marvosym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/math
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/mathdesign
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/mathtime
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/mflogo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/misc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/pl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/public
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/pxfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/stmaryrd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/tibetan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/tipa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/txfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/utf8/charset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/viqr/charset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/viscii/charset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/win/1251/charset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/win/1251/cm/sauter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/win/1251/cyrillic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/win/1251/cyrillic/cmcyr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/ht-fonts/win/1251/lh/lh-t2a
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex4ht/xtpipes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/alatex/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/amstex/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/amstex/config
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/bib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/config
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/extra
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/fonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/foxet
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/interface
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/interface/third
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/patterns
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/pgf/basiclayer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/pgf/frontendlayer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/pgf/math
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/pgf/systemlayer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/pgf/utilities
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/sample
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/test
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/account
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/algorithmic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/bnf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/chromato
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/construction-plan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/degrade
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/fixme
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/french
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/fullpage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/games
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/gentium
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/gnuplot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/letter/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/letter/extension
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/letter/interface
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/letter/style
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/lettrine
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/lilypond
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/pgfplots
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/ruby
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/semaphor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/simplefonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/simpleslides
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/typearea
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/typescripts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/third/vim
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/context/user
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/cslatex/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/csplain/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/eplain
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/fontinst/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/fontinst/latinetx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/fontinst/latinmtx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/fontinst/mathetx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/fontinst/mathmtx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/fontinst/misc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/fontinst/smbletx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/fontinst/smblmtx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/2up
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/abbr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/abstyles
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/arrayjobx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/babel
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/barr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/colortab
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/context
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/c-pascal
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/dcpic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/dehyph-exptl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/dirtree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/dratex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/dvips
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/ean
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/edmac
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/eijkhout
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/encodings
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/enctex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/epsf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/fenixpar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/fltpoint
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/frame
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/genmisc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/german
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/hyphenex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/hyph-utf8/conversions
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex-special
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/ibygrk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/iftex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/ifxetex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/insbox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/kastrup
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/librarian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/mathabx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/mathdots
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/metapost
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/mfpic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/midnight
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/misc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/multido
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/musixlyr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/musixps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/musixtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/oberdiek
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/ofs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/omegahyph
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pdf-trans
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pgf/basiclayer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pgf/libraries
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pgf/math
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pgf/modules
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pgfplots
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pgfplots/libs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pgfplots/liststructure
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pgfplots/numtable
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pgfplots/oldpgfcompatib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pgfplots/oldpgfplotscompatib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pgfplots/sys
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pgfplots/util
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pgf/systemlayer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pgf/utilities
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/poster-mac
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-3dplot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-abspos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-asr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-bar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-barcode
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-bezier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-blur
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-bspline
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-circ
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-coil
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-cox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-diffraction
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-electricfield
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-eps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-eucl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-fill
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-fr3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-fractal
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-fun
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-func
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-gantt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-geo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-geo/data
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-geo/dataII
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-ghsb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-gr3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-grad
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-infixplot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-jtree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-knot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-labo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-lens
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-light3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-magneticfield
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-math
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-mirror
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-node
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-ob3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-optexp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-optic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-osci
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-pad
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-pdgr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-plot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-poly
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-qtree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pstricks
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pstricks-add
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pstricks/config
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-sigsys
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-slpe
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-solides3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-spectra
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-stru
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-text
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-thick
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-tree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/pst-vue3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/qpxqtx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/rlepsf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/ruhyphen
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/shapepar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/etc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/tabto-generic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/tap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/tex4ht
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/texapi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/texdraw
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/tex-ewd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/tex-ps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/textmerg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/thumbpdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/ukrhyph
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/ulem
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/variations
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/vaucanson-g
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/velthuis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/xcomment
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/xecyr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/xetexconfig
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/xkeyval
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/xlop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/xstring
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/xypic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/yax
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/generic/zhmetrics
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/jadetex/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/lambda/antomega
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/lambda/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/lambda/config
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/lambda/oinuit
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/12many
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/a0poster
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/a5comb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/aastex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/abc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/abstract
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/accfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/achemso
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/achemso/config
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/acmconf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/acromake
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/acronym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/active-conf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/addlines
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/adrconv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ae
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/aeguill
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/afthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/aguplus
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/aiaa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/AkkTeX
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/akletter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/alg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/algorithm2e
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/algorithmicx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/algorithms
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/allrunes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/alnumsec
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/alterqcm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/altfont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ametsoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/amsaddr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/amscls
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/amsfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/amsmath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/amsrefs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/animate
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/anonchap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/answers
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/antiqua
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/antp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/antt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/anyfontsize
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/anysize
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/apa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/apacite
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/apalike
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/appendix
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/arabi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/arabtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/archaic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/arcs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/arev
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/armenian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/arsclassica
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/arydshln
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/asaetr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ascelike
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ascii
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/assignment
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/asyfig
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/attachfile
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/augie
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/auncial-new
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/aurical
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/authoraftertitle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/authorindex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/autoarea
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/auto-pst-pdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/avantgar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/babelbib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/background
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bangtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/barcodes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bardiag
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/baskervald
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bayer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bbding
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bbm-macros
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bbold
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bclogo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/beamer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/beamer/art
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/beamer-contrib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/beamer/emulation
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/beamer/emulation/examples
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/beamer-FUBerlin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/beamer/multimedia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/beamerposter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/beamer/themes/color
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/beamer/themes/font
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/beamer/themes/inner
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/beamer/themes/outer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/compatibility
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/beamer/translator
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-basic-dictionary
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-bibliography-dictionary
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-environment-dictionary
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-months-dictionary
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-numbers-dictionary
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-theorem-dictionary
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/begriff
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bera
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/betababel
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/beton
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bez123
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bezos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bgreek
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bibarts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/biblatex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/biblatex-apa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/biblatex/bbx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/biblatex/cbx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/biblatex-chem/bbx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/biblatex-chem/cbx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/biblatex-chicago-notes-df
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/biblatex-dw/bbx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/biblatex-dw/cbx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/biblatex-dw/lbx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/biblatex-historian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/biblatex/lbx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/biblatex-nature/bbx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/biblatex-nature/cbx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/biblatex-philosophy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/biblatex-science/bbx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/biblatex-science/cbx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bibleref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/biblist
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bibtopic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bibtopicprefix
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bibunits
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bidi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bigfoot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bigints
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/binomexp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/biocon
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bizcard
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/blacklettert1
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/blindtext
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/blkarray
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/block
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/blowup
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/boisik
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/boites
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bold-extra
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/boldtensors
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bookest
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bookhands
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/booklet
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bookman
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/booktabs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/boolexpr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bophook
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bosisio
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/boxedminipage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/boxhandler
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bpchem
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bracketkey
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/braille
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/braket
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/breakurl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/brushscr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bullcntr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bundledoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/burmese
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bussproofs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/bytefield
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cachepic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/calctab
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/calrsfs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/calxxxx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cancel
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/captcont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/captdef
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/caption
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/capt-of
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/carlisle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cases
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/casyl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/catechis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cbcoptic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ccaption
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ccfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ccicons
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cclicenses
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cd-cover
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cdpbundl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cell
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cellspace
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cfr-lm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/changebar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/changelayout
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/changepage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/changes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/chappg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/chapterfolder
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/chbibref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/chemarrow
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/chemcompounds
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/chemcono
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/chemfig
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/chemstyle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/chemstyle/config
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/chess
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/chessboard
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/chessfss
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/chess-problem-diagrams
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/chicago
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/chletter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/chngcntr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/chronology
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/circ
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/circuitikz
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cite
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cjhebrew
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cjk/contrib/wadalab
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cjkpunct
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cjk/texinput
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cjk/texinput/Bg5
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cjk/texinput/CEF
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cjk/texinput/CNS
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cjk/texinput/GB
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cjk/texinput/JIS
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cjk/texinput/mule
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cjk/texinput/SJIS
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cjk/texinput/thai
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cjk/texinput/UTF8
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cjk/utils/pyhyphen
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/classicthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/clefval
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cleveref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/clock
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/clrscode
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cmap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cmbright
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cmdstring
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cmdtrack
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cm-lgc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cmll
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cmsd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cm-super
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/codedoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/collref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/colordoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/colorinfo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/colortbl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/colorwav
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/combelow
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/combine
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/combinedgraphics
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/comma
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/commath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/comment
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/compactbib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/complexity
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/computational-complexity
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/concmath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/concprog
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/confproc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/constants
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/context
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/contour
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cooking
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cookybooky
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cool
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/coollist
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/coolstr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cooltooltips
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/coordsys
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/courier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/courier-scaled
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/courseoutline
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/coursepaper
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/coverpage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/covington
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/crop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/crossreference
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/crossword
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/crosswrd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/csbulletin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cslatex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/csquotes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/csvtools
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ctable
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ctex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ctex/back
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ctex/cfg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ctex/def
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ctex/engine
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ctex/fd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ctex/fontset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ctex/opt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ctib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cuisine
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/currfile
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/currvita
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/curve
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/curve2e
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/curves
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/custom-bib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cweb-latex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cyklop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/cyrillic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dashbox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dashrule
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dashundergaps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/datatool
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dateiliste
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/datenumber
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/datetime
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dblfloatfix
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/decimal
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/delimtxt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/diagmac2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/diagnose
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dichokey
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dictsym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/digiconfigs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dinbrief
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dingbat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/directory
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/disser
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dk-bib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dlfltxb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dnaseq
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/docmfp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/docmute
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/doi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/doipubmed
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dot2texi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dotarrow
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dotseqn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dottex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/doublestroke
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dozenal
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dpfloat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dprogress
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/drac
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/draftcopy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/draftwatermark
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dramatist
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/drs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dtk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/duerer-latex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/duotenzor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dvdcoll
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dvipdfmx-def
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/dyntree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ean13isbn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/easy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/easylist
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ebezier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ebsthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ecclesiastic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ecltree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/eco
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/economic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ecv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ed
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/edmargin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ednotes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/eemeir
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/eepic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/egameps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/egplot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/eiad-ltx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/elbioimp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ellipsis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/elmath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/elpres
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/elsarticle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/elsevier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/eltex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/em
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/emp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/emptypage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/emulateapj
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/encxvlna
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/endfloat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/endheads
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/endnotes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/engpron
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/engrec
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/engtlc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/enumitem
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/envbig
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/environ
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/envlab
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/epigrafica
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/epigraph
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/epiolmec
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/epsdice
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/epspdfconversion
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/eqell
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/eqlist
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/eqparbox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/erdc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/errata
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ESIEEcv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/esint
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/esk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/eskd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/eskdx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/eso-pic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/estcpmm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/esvect
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/etaremune
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/etex-pkg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/etextools
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ethiop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/etoolbox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/euenc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/eukdate
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/euler
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/eulervm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/euproposal
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/euro
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/eurofont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/europecv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/eurosans
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/eurosym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/everypage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/exam
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/examdesign
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/examplep
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/excludeonly
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/exercise
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/expdlist
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/expl3
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/export
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/exp-testopt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/extarrows
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/extpfeil
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/extract
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/extsizes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/facsimile
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/faktor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fancybox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fancyhdr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fancynum
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fancypar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fancyref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fancytooltips
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fancyvrb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/feyn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/feynmf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fge
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/figbib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/figsize
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/filecontents
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/filehook
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fink
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fix2col
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fixfoot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fixme
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fixme/layouts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fixme/layouts/env
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fixme/layouts/target
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fixme/themes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/flabels
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/flacards
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/flagderiv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/flashcards
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/flashmovie
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/flippdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/float
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/floatrow
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/flowfram
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fltpage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fmp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fmtcount
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fn2end
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fnbreak
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fncychap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fncylab
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fnpara
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/foekfont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/foilhtml
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fonetika
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fontinst
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fontspec
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fonttable
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/footbib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/footmisc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/footnpag
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/forarray
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/forloop
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/formular
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fouridx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fourier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fouriernc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fragments
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/framed
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/frankenstein
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/frcursive
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/frenchle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fribrief
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/frletter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/frontespizio
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ftcap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ftnxtra
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/functan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/fundus
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gaceta
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/galois
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gastex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gatech-thesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gauss
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gb4e
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/g-brief
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gcard
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gchords
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gcite
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gene-logic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/genmpage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/geometry
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/germkorr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/getfiledate
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gfsartemisia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gfsbaskerville
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gfsbodoni
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gfscomplutum
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gfsdidot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gfsneohellenic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gfsporson
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gfssolomos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ginpenc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gloss
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/glossaries/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/glossaries/dict
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/glossaries/expl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/glossaries/styles
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gmdoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gmdoc-enhance
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gmeometric
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gmiflink
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gmutils
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gmverb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gmverse
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gnuplottex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/go
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/graphics
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/graphicx-psmin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/greekdates
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/greek-inputenc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/greektex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/grfpaste
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/grid
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gridset
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/grotesq
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/grverb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/gu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/guitar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/guitlogo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/hanging
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/HA-prosper
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/HA-prosper/Styles/Aggie
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/HA-prosper/Styles/Capsules
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/HA-prosper/Styles/Ciment
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/HA-prosper/Styles/Fyma
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/HA-prosper/Styles/HA
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/HA-prosper/Styles/Lakar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/HA-prosper/Styles/Simple
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/HA-prosper/Styles/TCS
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/HA-prosper/Styles/Tycja
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/har2nat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/harmony
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/harpoon
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/harvard
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/hc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/helvetic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/hep
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/hepnames
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/hepparticles
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/hepthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/hepunits
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/here
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/hexgame
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/hfoldsty
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/hhtensor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/histogr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/historische-zeitschrift/bbx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/historische-zeitschrift/cbx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/historische-zeitschrift/lbx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/hitec
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/hpsdiss
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/hrlatex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/hvfloat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/hvindex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/hypdvips
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/hyper
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/hypernat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/hyperref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/hyperxmp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/hyphenat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ibycus-babel
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/icsv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/idxlayout
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/IEEEconf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ieeepes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/IEEEtran
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ifmslide
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ifmtarg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ifplatform
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ifsym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ijmart
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/imac
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/image-gallery
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/imakeidx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/import
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/imtekda
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/inconsolata
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/index
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/initials
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/inlinebib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/inlinedef
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/interactiveworkbook
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/inversepath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ionumbers
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/iso
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/iso10303
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/isodate
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/isodoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/isomath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/isonums
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/isorot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/isotope
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/itnumpar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/itrans
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/iwona
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/jeopardy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/jknapltx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/jmlr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/jneurosci
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/jpsj
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/jura
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/juraabbrev
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/jurabib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/juramisc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/jurarsp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/kalender
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/karnaugh
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/kerkis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/kerntest
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/keycommand
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/keystroke
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/kluwer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/knitting
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/knittingpattern
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/koma-script
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/kpfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/kurier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/labbook
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/labelcas
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/labels
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/lastpage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/latex2man
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/latexconfig
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/layaureo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/layouts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/lazylist
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/lcd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/lcg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/lcyw
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/leading
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/leaflet
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ledmac
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/leftidx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/lettre
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/lettrine
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/lewis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/lexikon
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/lh
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/lhcyr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyralt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrkoi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrwin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/lhelp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/libertine
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/libris
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/limap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/linearA
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/linegoal
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/lineno
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/linguex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/lipsum
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/listbib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/listing
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/listings
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/listings-ext
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/listliketab
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/listofsymbols
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/lithuanian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/liturg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/lkproof
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/lm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/locality
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/localloc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/logical-markup-utils
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/logpap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/lps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/lsc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ltabptch
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ltxdockit
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ltxindex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ltxmisc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ltxnew
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/lxfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ly1
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/macqassign
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mafr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/magaz
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mailing
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mailmerge
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/makebarcode
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/makebox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/makecell
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/makecmds
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/makedtx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/makeglos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/makeplot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/manfnt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/manuscript
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mapcodes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/margbib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/marginnote
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/marvosym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mathcomp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mathdesign
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mathdesign/mdbch
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mathdesign/mdput
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mathdesign/mdugm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mathexam
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mathspic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mattens
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/maybemath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mcaption
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mceinleger
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mcite
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mciteplus
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mdframed
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mdwtools
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/memexsupp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/memoir
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mentis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/menu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/metalogo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/method
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/metre
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mflogo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mfnfss
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mfpic4ode
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mftinc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mh
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mhchem
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mhequ
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mhs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/microtype
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/midpage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/miller
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/minibox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/minipage-marginpar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/miniplot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/minitoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/minted
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/minutes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/misc209
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mla-paper
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mlist
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mltex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mmap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mnsymbol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/moderncv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/modref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/modroman
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mongolian-babel
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/montex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/morefloats
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/moresize
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/moreverb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/movie15
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mparhack
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ms
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/msc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/msg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mslapa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mtgreek
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/muench/hrefhide
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/multibbl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/multibib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/multicap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/multido
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/multiobjective
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/multirow
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/muthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mwcls
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/mylatexformat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/nag
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/namespc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/natbib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/nath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ncclatex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ncctools
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ncntrsbk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/nddiss
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/needspace
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/newfile
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/newlfm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/newspaper
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/newvbtm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/newverbs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/nextpage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/nfssext-cfr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/niceframe
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/nicetext
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/nih
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/nlctdoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/noitcrul
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/nolbreaks
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/nomencl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/nomentbl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/nonfloat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/nopageno
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/nostarch
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/notes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/notes2bib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/notoccite
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/nrc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ntabbing
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ntgclass
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ntheorem
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/numname
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/numprint
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/oberdiek
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/objectz
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ocgtools
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ocr-latex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/octavo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/oldstyle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/onlyamsmath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/onrannual
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/opcit
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/optional
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ordinalpt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/othello
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/otibet
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ot-tableau
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/outline
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/outliner
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/overpic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pacioli
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pagecont
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pagenote
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pagerange
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pageslts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/palatino
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/paper
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/papercdcase
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/papermas
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/papertex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/paralist
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/parallel
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/paresse
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/parrun
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/patchcmd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pauldoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pawpict
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pax
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pb-diagram
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pbox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pbsheet
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pclnfss
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pdf14
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pdfcomment
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pdfcprot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pdfmarginpar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pdfpages
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pdfscreen
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pdfslide
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pdfsync
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pdftex-def
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pdftricks
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pdfwin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pdfx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pecha
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/perltex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/permute
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/petiteannonce
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/petri-nets
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pgf/basiclayer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pgf/compatibility
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pgf/frontendlayer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pgf/math
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pgfopts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pgfplots
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pgfplots/libs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pgf-soroban
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pgf/systemlayer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pgf-umlsd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pgf/utilities
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/phaistos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/philex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/philosophersimprint
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/photo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/picinpar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pict2e
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pictex2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pigpen
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pinlabel
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pittetd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/placeins
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/plantslabels
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/plari
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/plates
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/play
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/plweb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pmgraph
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/poemscol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/polski
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/polyglot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/polynom
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/polynomial
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/polytable
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/postcards
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/powerdot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/powerdot-FUBerlin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ppower4
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ppr-prv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pracjourn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/preprint
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/prerex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/prettyref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/preview
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/printlen
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/proba
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/probsoln
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/procIAGssymp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/program
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/progress
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/properties
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/prosper
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/protex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/protocol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/psbao
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pseudocode
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/psfrag
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/psfragx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/psgo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pslatex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/psnfss
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pspicture
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-2dplot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-3dplot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-abspos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-am
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-asr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-bar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-barcode
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-bezier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-blur
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-bspline
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-calendar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-circ
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-coil
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-cox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-dbicons
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-diffraction
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-electricfield
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-eps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-eucl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-exa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-fill
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-fr3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-fractal
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-fun
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-func
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-gantt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-geo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-ghsb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-gr3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-grad
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-infixplot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-jtree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-knot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-labo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-lens
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-light3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-magneticfield
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-math
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-mirror
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-node
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-ob3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pstool
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-optexp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-optic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-osci
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-pad
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-pdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-pdgr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-platon
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-plot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-poly
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-qtree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pstricks
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pstricks-add
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-sigsys
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-slpe
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-solides3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-soroban
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-spectra
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-stru
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-text
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-thick
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-tree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-uml
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-vowel
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pst-vue3d
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/psu-thesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ptptex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/pxfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/qcm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/qobitree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/qstest
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/qsymbols
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/qtree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/quotchap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/quotmark
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/randbild
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/randtext
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/rccol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/rcs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/rcsinfo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/rcs-multi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/recipe
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/recipecard
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/rectopma
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/recycle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/refcheck
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/refman
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/refstyle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/regcount
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/register
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/relsize
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/repeatindex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/revtex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/revtex4
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/rjlparshap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/rmpage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/robustcommand
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/robustindex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/romande
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/romannum
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/rotating
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/rotfloat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/rotpages
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/roundbox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/rsc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/rst
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/rtkinenc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/rtklage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/r_und_s
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ryethesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/sageep
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/sanskrit
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/sansmath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/sauerj
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/sauterfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/savefnmark
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/savesym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/savetrees
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/scale
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/scalebar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/schemabloc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/scientificpaper
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/sciposter
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/sciwordconv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/screenplay
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/sdrt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/sectionbox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/sectsty
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/selectp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/semantic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/semaphor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/seminar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/semioneside
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/seqsplit
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/setspace
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/seuthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/sf298
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/sffms
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/sfg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/sfmath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/sgame
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/shadethm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/shipunov
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/shorttoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/show2e
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/showexpl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/showlabels
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/shuffle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/sidecap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/sides
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/siggraph
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/silence
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/simplecd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/simplecv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/simplewick
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/SIstyle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/SIunits
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/siunitx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/siunitx/config
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/skak
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/skeycommand
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/skeyval
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/skull
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/slantsc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/smalltableof
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/smartref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/snapshot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/songbook
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/soton
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/soul
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/spanish-mx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/sparklines
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/spie
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/splitbib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/splitindex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/spotcolor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/spreadtab
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/spverbatim
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/srcltx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/sseq
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ssqquote
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stack
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/standalone
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/statex2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/statistik
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/staves
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stdclsdv
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stdpage
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/steinmetz
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stellenbosch
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stellenbosch/logos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stex/assignment
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stex/cmathml
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stex/cnx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stex/dcm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stex/mikoslides
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stex/modules
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stex/omd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stex/omdoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stex/omtext
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stex/presentation
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stex/problem
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stex/reqdoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stex/sproof
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stex/sref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stex/statements
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stmaryrd
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stringstrings
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/struktex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/sttools
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/stubs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/subdepth
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/subeqn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/subeqnarray
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/subfig
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/subfigure
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/subfloat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/substr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/sudoku
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/sudokubundle
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/sugconf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/supertabular
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/susy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/svgcolor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/svn
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/svninfo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/svn-multi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/svn-prov
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/syllogism
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/symbol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/synproof
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/syntax
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/syntrace
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/synttree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/t2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/Tabbing
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tableaux
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tablenotes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tablists
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tablor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tabls
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tabto-ltx
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tabularborder
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tabularcalc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tabularew
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tabulary
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tabvar
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/talk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/t-angles
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/taupin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tcldoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tdclock
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tdsfrmath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/technics
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ted
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tengwarscript
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tensor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/termlist
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/teubner
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tex-gyre
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/texilikechaps
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/texilikecover
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tex-label
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/texlogos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/texmate
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/texments
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/texpower
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/texshade
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/textcase
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/textfit
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/textopo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/textpath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/textpos
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/theoremref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/thesis-titlepage-fhac
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/thinsp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/thmbox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/thmtools
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/threeparttable
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/threeparttablex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/thumb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/thumby
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/thuthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ticket
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tikz-3dplot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tikz-inet
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tikz-qtree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tikz-timing
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/times
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/timesht
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tipa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/titlefoot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/titlepic
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/titleref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/titlesec
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/titling
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tkz-doc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tkz-linknodes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tkz-orm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tkz-tab
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tocbibind
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tocloft
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tocvsec2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/todo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/todonotes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tokenizer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/toolbox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tools
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/topfloat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/toptesi
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/totcount
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/totpages
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tpslifonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/trajan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/trfsigns
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/trimspaces
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/trivfloat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/trsym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/truncate
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tufte-latex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/tugboat
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/turkmen
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/turnstile
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/twoinone
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/twoup
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/txfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/txfontsb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/type1cm
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/typedref
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/typehtml
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/typogrid
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/uaclasses
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ucdavisthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ucs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ucs/data
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ucthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/uebungsblatt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/uiucthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ulqda
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/umich-thesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/uml
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/umlaute
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/umoline
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/umthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/underlin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/underscore
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/undolabl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/unicode-math
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/units
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/unitsdef
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/universa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/upmethodology
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/upquote
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/url
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ushort
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ut-thesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/uwthesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/varindex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/varsfromjobname
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/varwidth
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/velthuis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/venturis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/venturis2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/venturisadf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/venturisold
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/venturissans
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/venturissans2
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/verbatimbox
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/verbatimcopy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/verbdef
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/verse
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/version
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/versions
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/vertbars
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/vhistory
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/vita
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/vmargin
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/vntex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/volumes
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/vpe
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/vrsion
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/vwcol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/vxu
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/wallpaper
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/warning
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/warpcol
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/was
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/wasysym
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/widetable
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/williams
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/wnri
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/wordlike
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/wrapfig
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/wsuipa
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/xargs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/xcolor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/xdoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/xfor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/xifthen
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/xkeyval
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/xmpincl
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/xnewcommand
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/xoptarg
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/xpackages/xbase
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/xpackages/xtras
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/xq
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/xskak
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/xtab
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/xwatermark
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/xyling
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/xypdf
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/xytree
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/yafoot
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/yagusylo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ydoc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/yfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/yhmath
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/york-thesis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/youngtab
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/yplan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/zapfchan
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/zapfding
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/zed-csp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/zhmetrics
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/ziffer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/zwgetfdate
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/latex/zwpagelayout
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/lualatex/luainputenc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/luatex/hyph-utf8
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/luatex/lualibs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/luatex/luamplib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/luatex/luaotfload
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/luatex/luatexbase
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/luatex/luatextra
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/mex/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/mex/config
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/mex/utf8mex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/mltex/config
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/mptopdf/config
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/amsfonts
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/antt
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/apalike
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/armenian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/config
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/cweb
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/cyrplain
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/encxvlna
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/esint-type1
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/etex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/fixpdfmag
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/fontch
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/font-change
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/fp
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/graphics-pln
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/gustlib
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/gustlib/biblotex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/gustlib/licz
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/gustlib/map
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/gustlib/plbtx993
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/gustlib/plmac218
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/harvmac
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/hyplain
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/iwona
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/js-misc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/kdgreek
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/knitting
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/kurier
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/lh
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/ly1
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/metatex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/misc
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/mkpattern
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/newsletr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/omega
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/pgf/basiclayer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/pgf/frontendlayer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/pgf/math
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/pgfplots
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/pgf/systemlayer
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/pgf/utilities
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/pitex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/placeins-plain
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/plnfss
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/resumemac
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/rsfs
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/semaphor
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/timetable
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/treetex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/tugboat-plain
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/varisize
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/velthuis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/vntex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/plain/wasy
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/platex/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/platex/config
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/platex/jsclasses
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/psizzl/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/psizzl/config
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/ptex/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/ptex/config
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/ptexgeneric/config
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/ptexgeneric/hyphen
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/ptexgeneric/ruhyphen
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/ptexgeneric/ukrhyph
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/startex/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/texinfo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/texsis/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/texsis/config
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xelatex/arabxetex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xelatex/fontwrap
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xelatex/mathspec
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xelatex/philokalia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xelatex/polyglossia
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xelatex/velthuis
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xelatex/xecjk
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xelatex/xecolour
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xelatex/xecyr
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xelatex/xeindex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xelatex/xepersian
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xelatex/xetexconfig
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xelatex/xetex-def
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xelatex/xetex-pstricks
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xelatex/xgreek
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xelatex/xltxtra
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xelatex/xunicode
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xetex/xesearch
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xetex/xetexfontinfo
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xetex/xetex-pstricks
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xetex/zhspacing/context
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xetex/zhspacing/latex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xetex/zhspacing/plain
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xmltex/base
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xmltex/config
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xmltex/passivetex
mkdir -p %{buildroot}%{_texdir}/texmf-dist/tex/xmltex/xmlplay
mkdir -p %{buildroot}%{_texdir}/texmf-dist/vtex/config
mkdir -p %{buildroot}%{_texdir}/texmf/doc/bg5conv
mkdir -p %{buildroot}%{_texdir}/texmf/doc/bibtex8
mkdir -p %{buildroot}%{_texdir}/texmf/doc/cef5conv
mkdir -p %{buildroot}%{_texdir}/texmf/doc/cefconv
mkdir -p %{buildroot}%{_texdir}/texmf/doc/cefsconv
mkdir -p %{buildroot}%{_texdir}/texmf/doc/chktex
mkdir -p %{buildroot}%{_texdir}/texmf/doc/dvipdfm
mkdir -p %{buildroot}%{_texdir}/texmf/doc/dvipng
mkdir -p %{buildroot}%{_texdir}/texmf/doc/dvips
mkdir -p %{buildroot}%{_texdir}/texmf/doc/extconv
mkdir -p %{buildroot}%{_texdir}/texmf/doc/generic/elhyphen
mkdir -p %{buildroot}%{_texdir}/texmf/doc/generic/huhyphen
mkdir -p %{buildroot}%{_texdir}/texmf/doc/hbf2gf
mkdir -p %{buildroot}%{_texdir}/texmf/doc/info
mkdir -p %{buildroot}%{_texdir}/texmf/doc/kpathsea
mkdir -p %{buildroot}%{_texdir}/texmf/doc/man/man1
mkdir -p %{buildroot}%{_texdir}/texmf/doc/man/man5
mkdir -p %{buildroot}%{_texdir}/texmf/doc/sjisconv
mkdir -p %{buildroot}%{_texdir}/texmf/doc/tetex
mkdir -p %{buildroot}%{_texdir}/texmf/doc/texdoc
mkdir -p %{buildroot}%{_texdir}/texmf/doc/texlive
mkdir -p %{buildroot}%{_texdir}/texmf/doc/texlive/texlive-common
mkdir -p %{buildroot}%{_texdir}/texmf/doc/texlive/texlive-common/examples
mkdir -p %{buildroot}%{_texdir}/texmf/doc/texlive/texlive-cz
mkdir -p %{buildroot}%{_texdir}/texmf/doc/texlive/texlive-de
mkdir -p %{buildroot}%{_texdir}/texmf/doc/texlive/texlive-en
mkdir -p %{buildroot}%{_texdir}/texmf/doc/texlive/texlive-en/archive
mkdir -p %{buildroot}%{_texdir}/texmf/doc/texlive/texlive-fr
mkdir -p %{buildroot}%{_texdir}/texmf/doc/texlive/texlive-it
mkdir -p %{buildroot}%{_texdir}/texmf/doc/texlive/texlive-pl
mkdir -p %{buildroot}%{_texdir}/texmf/doc/texlive/texlive-ru
mkdir -p %{buildroot}%{_texdir}/texmf/doc/texlive/texlive-sr
mkdir -p %{buildroot}%{_texdir}/texmf/doc/texlive/texlive-sr/images
mkdir -p %{buildroot}%{_texdir}/texmf/doc/texlive/texlive-zh-cn
mkdir -p %{buildroot}%{_texdir}/texmf/doc/tpic2pdftex
mkdir -p %{buildroot}%{_texdir}/texmf/doc/ttf2pk
mkdir -p %{buildroot}%{_texdir}/texmf/doc/vlna
mkdir -p %{buildroot}%{_texdir}/texmf/doc/web2c
mkdir -p %{buildroot}%{_texdir}/texmf/dvipdfm/config
mkdir -p %{buildroot}%{_texdir}/texmf/dvipdfmx
mkdir -p %{buildroot}%{_texdir}/texmf/dvips/base
mkdir -p %{buildroot}%{_texdir}/texmf/dvips/config
mkdir -p %{buildroot}%{_texdir}/texmf/dvips/gsftopk
mkdir -p %{buildroot}%{_texdir}/texmf/dvips/tetex
mkdir -p %{buildroot}%{_texdir}/texmf/fonts/cmap
mkdir -p %{buildroot}%{_texdir}/texmf/fonts/cmap/dvipdfmx
mkdir -p %{buildroot}%{_texdir}/texmf/fonts/enc/dvips/afm2pl
mkdir -p %{buildroot}%{_texdir}/texmf/fonts/enc/dvips/tetex
mkdir -p %{buildroot}%{_texdir}/texmf/fonts/enc/ttf2pk/base
mkdir -p %{buildroot}%{_texdir}/texmf/fonts/lig/afm2pl
mkdir -p %{buildroot}%{_texdir}/texmf/fonts/map/dvipdfm/tetex
mkdir -p %{buildroot}%{_texdir}/texmf/fonts/map/dvipdfm/updmap
mkdir -p %{buildroot}%{_texdir}/texmf/fonts/map/dvipdfmx
mkdir -p %{buildroot}%{_texdir}/texmf/fonts/map/dvips/tetex
mkdir -p %{buildroot}%{_texdir}/texmf/fonts/map/dvips/updmap
mkdir -p %{buildroot}%{_texdir}/texmf/fonts/map/pdftex/updmap
mkdir -p %{buildroot}%{_texdir}/texmf/fonts/map/ttf2pk/config
mkdir -p %{buildroot}%{_texdir}/texmf/hbf2gf
mkdir -p %{buildroot}%{_texdir}/texmf/scripts/a2ping
mkdir -p %{buildroot}%{_texdir}/texmf/scripts/simpdftex
mkdir -p %{buildroot}%{_texdir}/texmf/scripts/tetex
mkdir -p %{buildroot}%{_texdir}/texmf/scripts/tex4ht
mkdir -p %{buildroot}%{_texdir}/texmf/scripts/texdoc
mkdir -p %{buildroot}%{_texdir}/texmf/scripts/texlive
mkdir -p %{buildroot}%{_texdir}/texmf/scripts/texlive/lua/texlive
mkdir -p %{buildroot}%{_texdir}/texmf/texconfig
mkdir -p %{buildroot}%{_texdir}/texmf/texconfig/g
mkdir -p %{buildroot}%{_texdir}/texmf/texconfig/v
mkdir -p %{buildroot}%{_texdir}/texmf/texconfig/x
mkdir -p %{buildroot}%{_texdir}/texmf/texdoc
mkdir -p %{buildroot}%{_texdir}/texmf/texdoctk
mkdir -p %{buildroot}%{_texdir}/texmf/tex/fontinst/afm2pl
mkdir -p %{buildroot}%{_texdir}/texmf/tex/generic/config
mkdir -p %{buildroot}%{_texdir}/texmf/tex/generic/hyphen
mkdir -p %{buildroot}%{_texdir}/texmf/tex/generic/pdftex
mkdir -p %{buildroot}%{_texdir}/texmf/tex/latex/afm2pl
mkdir -p %{buildroot}%{_texdir}/texmf/tex/latex/dvipdfm
mkdir -p %{buildroot}%{_texdir}/texmf/ttf2pk
mkdir -p %{buildroot}%{_texdir}/texmf/web2c
mkdir -p %{buildroot}%{_texdir}/texmf/xdvi
mkdir -p %{buildroot}%{_texdir}/texmf/xdvi/pixmap
mkdir -p %{buildroot}%{_texdir}/tlpkg

#install licenses
mkdir -p %{buildroot}%{_texdir}/licenses
pushd %{buildroot}%{_texdir}/licenses
xz -dc %{SOURCE3} | tar x
popd

# install binaries
rm -rf %{buildroot}%{_texdir}/bin/
mkdir -p %{buildroot}%{_bindir}
rm -f source/inst/bin/man
cp source/inst/bin/* %{buildroot}%{_bindir}

# install kpathsea shared libs, nuke static ones
rm -rf %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_libdir}
cp -d source/inst/lib/* %{buildroot}%{_libdir}
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la

# install includes
rm -rf %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_includedir}
cp -r source/inst/include/* %{buildroot}%{_includedir}

# relocate binaries to %%{_bindir} and fix relative symlinks
pushd %{buildroot}%{_bindir}
for i in `find . -type l`; do
if [ "`readlink $i | grep '..' | wc -l`" == "1" ]; then
l=`readlink $i | sed s,../../,../share/texlive/,`
rm -f $i
ln -s $l $i
fi
done
popd

# sync built/distro binaries
pushd %{buildroot}%{_bindir}
rm -f man
[ ! -e mfplain ] && ln -s mpost mfplain
[ ! -e texlua ] && ln -s luatex texlua
[ ! -e texluac ] && ln -s luatex texluac
# invalid licenses (and texdirflatten doesn't exist)
#for i in mkjobtexmf physe phyzzx texdiff texdirflatten metatex dvisvgm; do
for i in mkjobtexmf physe phyzzx texdiff texdirflatten metatex; do
rm -f %{buildroot}%{_bindir}/$i
done
rm -rf %{buildroot}%{_includedir}/ptexenc
popd

# remove all unshipped stuff
rm -f %{buildroot}/%{_bindir}/tlmgr

# nuke useless tlmgr packaging stuff
rm -rf %{buildroot}%{_texdir}/tlpkg/tlpobj/

# link config dir to the main tree and var dir to root
pushd %{buildroot}%{_texdir}
[ ! -e texmf-config ] && ln -s texmf texmf-config
[ ! -h texmf-var ] && ln -s %{_texmf_var} texmf-var
popd

# touch ghosts
touch %{buildroot}%{_texdir}/texmf/ls-R
touch %{buildroot}%{_texdir}/texmf-dist/ls-R
touch %{buildroot}%{_texdir}/../texmf/ls-R

%clean
rm -rf %{buildroot}

%pre base
rm -rf %{_texdir}/texmf-var
rm -rf %{_texmf_var}/*
:

%posttrans base
%{_bindir}/texhash 2> /dev/null
%{_bindir}/updmap-sys &> /dev/null
%{_bindir}/fmtutil-sys --all &> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
[ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%files
%defattr(-,root,root)

%files base
%defattr(-,root,root)
%dir %{_texmf_var}
%dir %{_texdir}/texmf-config
%dir %{_texdir}/texmf-var
%dir %{_texdir}/../texmf
%dir %{_texdir}/licenses
%{_texdir}/licenses/*
%attr(0644, root, root) %verify(not md5 size mtime) %ghost %{_texdir}/texmf/ls-R
%attr(0644, root, root) %verify(not md5 size mtime) %ghost %{_texdir}/texmf-dist/ls-R
%attr(0644, root, root) %verify(not md5 size mtime) %ghost %{_texdir}/../texmf/ls-R
%dir %{_texdir}/
%dir %{_texdir}/readme-html.dir
%dir %{_texdir}/readme-txt.dir
%dir %{_texdir}/texmf
%dir %{_texdir}/texmf/chktex
%dir %{_texdir}/texmf-dist
%dir %{_texdir}/texmf-dist/bibtex
%dir %{_texdir}/texmf-dist/bibtex/bib
%dir %{_texdir}/texmf-dist/bibtex/bib/abstyles
%dir %{_texdir}/texmf-dist/bibtex/bib/amsrefs
%dir %{_texdir}/texmf-dist/bibtex/bib/base
%dir %{_texdir}/texmf-dist/bibtex/bib/beebe
%dir %{_texdir}/texmf-dist/bibtex/bib/biblatex
%dir %{_texdir}/texmf-dist/bibtex/bib/computational-complexity
%dir %{_texdir}/texmf-dist/bibtex/bib/directory
%dir %{_texdir}/texmf-dist/bibtex/bib/dk-bib
%dir %{_texdir}/texmf-dist/bibtex/bib/frankenstein
%dir %{_texdir}/texmf-dist/bibtex/bib/gatech-thesis
%dir %{_texdir}/texmf-dist/bibtex/bib/gloss
%dir %{_texdir}/texmf-dist/bibtex/bib/gustlib
%dir %{_texdir}/texmf-dist/bibtex/bib/harvard
%dir %{_texdir}/texmf-dist/bibtex/bib/IEEEtran
%dir %{_texdir}/texmf-dist/bibtex/bib/index
%dir %{_texdir}/texmf-dist/bibtex/bib/jurabib
%dir %{_texdir}/texmf-dist/bibtex/bib/lsc
%dir %{_texdir}/texmf-dist/bibtex/bib/msc
%dir %{_texdir}/texmf-dist/bibtex/bib/nostarch
%dir %{_texdir}/texmf-dist/bibtex/bib/philosophersimprint
%dir %{_texdir}/texmf-dist/bibtex/bib/revtex4
%dir %{_texdir}/texmf-dist/bibtex/bib/spie
%dir %{_texdir}/texmf-dist/bibtex/bib/urlbst
%dir %{_texdir}/texmf-dist/bibtex/bib/vancouver
%dir %{_texdir}/texmf-dist/bibtex/bst
%dir %{_texdir}/texmf-dist/bibtex/bst/abstyles
%dir %{_texdir}/texmf-dist/bibtex/bst/achemso
%dir %{_texdir}/texmf-dist/bibtex/bst/adrconv
%dir %{_texdir}/texmf-dist/bibtex/bst/afthesis
%dir %{_texdir}/texmf-dist/bibtex/bst/aguplus
%dir %{_texdir}/texmf-dist/bibtex/bst/aiaa
%dir %{_texdir}/texmf-dist/bibtex/bst/aichej
%dir %{_texdir}/texmf-dist/bibtex/bst/ametsoc
%dir %{_texdir}/texmf-dist/bibtex/bst/amscls
%dir %{_texdir}/texmf-dist/bibtex/bst/amsrefs
%dir %{_texdir}/texmf-dist/bibtex/bst/apacite
%dir %{_texdir}/texmf-dist/bibtex/bst/apalike
%dir %{_texdir}/texmf-dist/bibtex/bst/apalike2
%dir %{_texdir}/texmf-dist/bibtex/bst/arsclassica
%dir %{_texdir}/texmf-dist/bibtex/bst/asaetr
%dir %{_texdir}/texmf-dist/bibtex/bst/ascelike
%dir %{_texdir}/texmf-dist/bibtex/bst/babelbib
%dir %{_texdir}/texmf-dist/bibtex/bst/base
%dir %{_texdir}/texmf-dist/bibtex/bst/beebe
%dir %{_texdir}/texmf-dist/bibtex/bst/bibexport
%dir %{_texdir}/texmf-dist/bibtex/bst/bib-fr
%dir %{_texdir}/texmf-dist/bibtex/bst/bibhtml
%dir %{_texdir}/texmf-dist/bibtex/bst/biblatex
%dir %{_texdir}/texmf-dist/bibtex/bst/cell
%dir %{_texdir}/texmf-dist/bibtex/bst/chembst
%dir %{_texdir}/texmf-dist/bibtex/bst/chem-journal
%dir %{_texdir}/texmf-dist/bibtex/bst/chicago
%dir %{_texdir}/texmf-dist/bibtex/bst/chicago-annote
%dir %{_texdir}/texmf-dist/bibtex/bst/computational-complexity
%dir %{_texdir}/texmf-dist/bibtex/bst/confproc
%dir %{_texdir}/texmf-dist/bibtex/bst/context
%dir %{_texdir}/texmf-dist/bibtex/bst/datatool
%dir %{_texdir}/texmf-dist/bibtex/bst/din1505
%dir %{_texdir}/texmf-dist/bibtex/bst/dinat
%dir %{_texdir}/texmf-dist/bibtex/bst/directory
%dir %{_texdir}/texmf-dist/bibtex/bst/disser
%dir %{_texdir}/texmf-dist/bibtex/bst/dk-bib
%dir %{_texdir}/texmf-dist/bibtex/bst/dlfltxb
%dir %{_texdir}/texmf-dist/bibtex/bst/dtk
%dir %{_texdir}/texmf-dist/bibtex/bst/dvdcoll
%dir %{_texdir}/texmf-dist/bibtex/bst/economic
%dir %{_texdir}/texmf-dist/bibtex/bst/elsarticle
%dir %{_texdir}/texmf-dist/bibtex/bst/elsevier-bib
%dir %{_texdir}/texmf-dist/bibtex/bst/fbs
%dir %{_texdir}/texmf-dist/bibtex/bst/figbib
%dir %{_texdir}/texmf-dist/bibtex/bst/finbib
%dir %{_texdir}/texmf-dist/bibtex/bst/frankenstein
%dir %{_texdir}/texmf-dist/bibtex/bst/gatech-thesis
%dir %{_texdir}/texmf-dist/bibtex/bst/gloss
%dir %{_texdir}/texmf-dist/bibtex/bst/gost
%dir %{_texdir}/texmf-dist/bibtex/bst/gustlib
%dir %{_texdir}/texmf-dist/bibtex/bst/harvard
%dir %{_texdir}/texmf-dist/bibtex/bst/hc
%dir %{_texdir}/texmf-dist/bibtex/bst/ieeepes
%dir %{_texdir}/texmf-dist/bibtex/bst/IEEEtran
%dir %{_texdir}/texmf-dist/bibtex/bst/ijmart
%dir %{_texdir}/texmf-dist/bibtex/bst/ijqc
%dir %{_texdir}/texmf-dist/bibtex/bst/imac
%dir %{_texdir}/texmf-dist/bibtex/bst/index
%dir %{_texdir}/texmf-dist/bibtex/bst/inlinebib
%dir %{_texdir}/texmf-dist/bibtex/bst/iopart-num
%dir %{_texdir}/texmf-dist/bibtex/bst/jneurosci
%dir %{_texdir}/texmf-dist/bibtex/bst/jurabib
%dir %{_texdir}/texmf-dist/bibtex/bst/jurarsp
%dir %{_texdir}/texmf-dist/bibtex/bst/kluwer
%dir %{_texdir}/texmf-dist/bibtex/bst/mciteplus
%dir %{_texdir}/texmf-dist/bibtex/bst/minitoc
%dir %{_texdir}/texmf-dist/bibtex/bst/mslapa
%dir %{_texdir}/texmf-dist/bibtex/bst/multibib
%dir %{_texdir}/texmf-dist/bibtex/bst/munich
%dir %{_texdir}/texmf-dist/bibtex/bst/natbib
%dir %{_texdir}/texmf-dist/bibtex/bst/nddiss
%dir %{_texdir}/texmf-dist/bibtex/bst/opcit
%dir %{_texdir}/texmf-dist/bibtex/bst/perception
%dir %{_texdir}/texmf-dist/bibtex/bst/persian-bib
%dir %{_texdir}/texmf-dist/bibtex/bst/pnas2009
%dir %{_texdir}/texmf-dist/bibtex/bst/psu-thesis
%dir %{_texdir}/texmf-dist/bibtex/bst/revtex
%dir %{_texdir}/texmf-dist/bibtex/bst/revtex4
%dir %{_texdir}/texmf-dist/bibtex/bst/rsc
%dir %{_texdir}/texmf-dist/bibtex/bst/sageep
%dir %{_texdir}/texmf-dist/bibtex/bst/savetrees
%dir %{_texdir}/texmf-dist/bibtex/bst/seuthesis
%dir %{_texdir}/texmf-dist/bibtex/bst/shipunov
%dir %{_texdir}/texmf-dist/bibtex/bst/sort-by-letters
%dir %{_texdir}/texmf-dist/bibtex/bst/spie
%dir %{_texdir}/texmf-dist/bibtex/bst/stellenbosch
%dir %{_texdir}/texmf-dist/bibtex/bst/swebib
%dir %{_texdir}/texmf-dist/bibtex/bst/texsis
%dir %{_texdir}/texmf-dist/bibtex/bst/thuthesis
%dir %{_texdir}/texmf-dist/bibtex/bst/tugboat
%dir %{_texdir}/texmf-dist/bibtex/bst/urlbst
%dir %{_texdir}/texmf-dist/bibtex/bst/vancouver
%dir %{_texdir}/texmf-dist/bibtex/csf
%dir %{_texdir}/texmf-dist/bibtex/csf/base
%dir %{_texdir}/texmf-dist/bibtex/csf/biblatex
%dir %{_texdir}/texmf-dist/bibtex/csf/disser
%dir %{_texdir}/texmf-dist/bibtex/csf/dk-bib
%dir %{_texdir}/texmf-dist/bibtex/csf/gost
%dir %{_texdir}/texmf-dist/bibtex/csf/persian-bib
%dir %{_texdir}/texmf-dist/bibtex/csf/polish-csf
%dir %{_texdir}/texmf-dist/context
%dir %{_texdir}/texmf-dist/context/data
%dir %{_texdir}/texmf-dist/context/data/scite
%dir %{_texdir}/texmf-dist/context/data/texfont
%dir %{_texdir}/texmf-dist/context/data/textadept
%dir %{_texdir}/texmf-dist/context/data/texworks
%dir %{_texdir}/texmf-dist/context/data/texworks/completion
%dir %{_texdir}/texmf-dist/context/data/texworks/configuration
%dir %{_texdir}/texmf-dist/context/data/texworks/TUG
%dir %{_texdir}/texmf-dist/doc
%dir %{_texdir}/texmf-dist/doc/aleph
%dir %{_texdir}/texmf-dist/doc/aleph/base
%dir %{_texdir}/texmf-dist/doc/amstex
%dir %{_texdir}/texmf-dist/doc/amstex/base
%dir %{_texdir}/texmf-dist/doc/bibtex
%dir %{_texdir}/texmf-dist/doc/bibtex/abstyles
%dir %{_texdir}/texmf-dist/doc/bibtex/apalike
%dir %{_texdir}/texmf-dist/doc/bibtex/base
%dir %{_texdir}/texmf-dist/doc/bibtex/bib-fr
%dir %{_texdir}/texmf-dist/doc/bibtex/bibhtml
%dir %{_texdir}/texmf-dist/doc/bibtex/chicago-annote
%dir %{_texdir}/texmf-dist/doc/bibtex/dinat
%dir %{_texdir}/texmf-dist/doc/bibtex/economic
%dir %{_texdir}/texmf-dist/doc/bibtex/elsevier-bib
%dir %{_texdir}/texmf-dist/doc/bibtex/gost
%dir %{_texdir}/texmf-dist/doc/bibtex/ijqc
%dir %{_texdir}/texmf-dist/doc/bibtex/iopart-num
%dir %{_texdir}/texmf-dist/doc/bibtex/tamethebeast
%dir %{_texdir}/texmf-dist/doc/bibtex/vancouver
%dir %{_texdir}/texmf-dist/doc/context
%dir %{_texdir}/texmf-dist/doc/context/bib
%dir %{_texdir}/texmf-dist/doc/context/document
%dir %{_texdir}/texmf-dist/doc/context/document/general
%dir %{_texdir}/texmf-dist/doc/context/document/general/manuals
%dir %{_texdir}/texmf-dist/doc/context/manuals
%dir %{_texdir}/texmf-dist/doc/context/manuals/allkind
%dir %{_texdir}/texmf-dist/doc/context/manuals/reference
%dir %{_texdir}/texmf-dist/doc/context/manuals/reference/en
%dir %{_texdir}/texmf-dist/doc/context/manuals/reference/en/columns
%dir %{_texdir}/texmf-dist/doc/context/manuals/reference/en/fonts
%dir %{_texdir}/texmf-dist/doc/context/manuals/reference/en/pagedesign
%dir %{_texdir}/texmf-dist/doc/context/manuals/reference/en/tables
%dir %{_texdir}/texmf-dist/doc/context/manuals/reference/en/typography
%dir %{_texdir}/texmf-dist/doc/context/scripts
%dir %{_texdir}/texmf-dist/doc/context/scripts/perl
%dir %{_texdir}/texmf-dist/doc/context/third
%dir %{_texdir}/texmf-dist/doc/context/third/account
%dir %{_texdir}/texmf-dist/doc/context/third/bnf
%dir %{_texdir}/texmf-dist/doc/context/third/chromato
%dir %{_texdir}/texmf-dist/doc/context/third/construction-plan
%dir %{_texdir}/texmf-dist/doc/context/third/context-notes-zh-cn
%dir %{_texdir}/texmf-dist/doc/context/third/context-notes-zh-cn/src
%dir %{_texdir}/texmf-dist/doc/context/third/context-notes-zh-cn/src/figures
%dir %{_texdir}/texmf-dist/doc/context/third/context-top-ten
%dir %{_texdir}/texmf-dist/doc/context/third/context-top-ten/src
%dir %{_texdir}/texmf-dist/doc/context/third/degrade
%dir %{_texdir}/texmf-dist/doc/context/third/fixme
%dir %{_texdir}/texmf-dist/doc/context/third/french
%dir %{_texdir}/texmf-dist/doc/context/third/fullpage
%dir %{_texdir}/texmf-dist/doc/context/third/games
%dir %{_texdir}/texmf-dist/doc/context/third/letter
%dir %{_texdir}/texmf-dist/doc/context/third/lettrine
%dir %{_texdir}/texmf-dist/doc/context/third/lilypond
%dir %{_texdir}/texmf-dist/doc/context/third/pgfplots
%dir %{_texdir}/texmf-dist/doc/context/third/ruby
%dir %{_texdir}/texmf-dist/doc/context/third/simplefonts
%dir %{_texdir}/texmf-dist/doc/context/third/simpleslides
%dir %{_texdir}/texmf-dist/doc/context/third/simpleslides/solutions
%dir %{_texdir}/texmf-dist/doc/context/third/simpleslides/styles
%dir %{_texdir}/texmf-dist/doc/context/third/typearea
%dir %{_texdir}/texmf-dist/doc/context/third/typescripts
%dir %{_texdir}/texmf-dist/doc/context/third/vim
%dir %{_texdir}/texmf-dist/doc/cslatex
%dir %{_texdir}/texmf-dist/doc/cslatex/base
%dir %{_texdir}/texmf-dist/doc/eplain
%dir %{_texdir}/texmf-dist/doc/eplain/demo
%dir %{_texdir}/texmf-dist/doc/eplain/doc
%dir %{_texdir}/texmf-dist/doc/eplain/util
%dir %{_texdir}/texmf-dist/doc/etex
%dir %{_texdir}/texmf-dist/doc/etex/base
%dir %{_texdir}/texmf-dist/doc/fonts
%dir %{_texdir}/texmf-dist/doc/fonts/accfonts
%dir %{_texdir}/texmf-dist/doc/fonts/ae
%dir %{_texdir}/texmf-dist/doc/fonts/allrunes
%dir %{_texdir}/texmf-dist/doc/fonts/amsfonts
%dir %{_texdir}/texmf-dist/doc/fonts/antiqua
%dir %{_texdir}/texmf-dist/doc/fonts/antp
%dir %{_texdir}/texmf-dist/doc/fonts/antt
%dir %{_texdir}/texmf-dist/doc/fonts/archaic
%dir %{_texdir}/texmf-dist/doc/fonts/arev
%dir %{_texdir}/texmf-dist/doc/fonts/armenian
%dir %{_texdir}/texmf-dist/doc/fonts/armenian/examples
%dir %{_texdir}/texmf-dist/doc/fonts/armenian/examples/latex
%dir %{_texdir}/texmf-dist/doc/fonts/armenian/examples/plain
%dir %{_texdir}/texmf-dist/doc/fonts/arphic
%dir %{_texdir}/texmf-dist/doc/fonts/arphic/bkaiu
%dir %{_texdir}/texmf-dist/doc/fonts/arphic/bsmiu
%dir %{_texdir}/texmf-dist/doc/fonts/arphic/gbsnu
%dir %{_texdir}/texmf-dist/doc/fonts/arphic/gkaiu
%dir %{_texdir}/texmf-dist/doc/fonts/Asana-Math
%dir %{_texdir}/texmf-dist/doc/fonts/ascii
%dir %{_texdir}/texmf-dist/doc/fonts/astro
%dir %{_texdir}/texmf-dist/doc/fonts/auncial-new
%dir %{_texdir}/texmf-dist/doc/fonts/baskervald
%dir %{_texdir}/texmf-dist/doc/fonts/bbm
%dir %{_texdir}/texmf-dist/doc/fonts/belleek
%dir %{_texdir}/texmf-dist/doc/fonts/bera
%dir %{_texdir}/texmf-dist/doc/fonts/blacklettert1
%dir %{_texdir}/texmf-dist/doc/fonts/boisik
%dir %{_texdir}/texmf-dist/doc/fonts/boisik/example
%dir %{_texdir}/texmf-dist/doc/fonts/bookhands
%dir %{_texdir}/texmf-dist/doc/fonts/burmese
%dir %{_texdir}/texmf-dist/doc/fonts/carolmin-ps
%dir %{_texdir}/texmf-dist/doc/fonts/cbfonts
%dir %{_texdir}/texmf-dist/doc/fonts/cc-pl
%dir %{_texdir}/texmf-dist/doc/fonts/cfr-lm
%dir %{_texdir}/texmf-dist/doc/fonts/charter
%dir %{_texdir}/texmf-dist/doc/fonts/chemarrow
%dir %{_texdir}/texmf-dist/doc/fonts/cjhebrew
%dir %{_texdir}/texmf-dist/doc/fonts/cm
%dir %{_texdir}/texmf-dist/doc/fonts/cmcyr
%dir %{_texdir}/texmf-dist/doc/fonts/cmcyr/vf
%dir %{_texdir}/texmf-dist/doc/fonts/cmcyr/vf/cmcyr6i
%dir %{_texdir}/texmf-dist/doc/fonts/cmcyr/vf/cmcyr6k
%dir %{_texdir}/texmf-dist/doc/fonts/cmcyr/vf/cmcyr6w
%dir %{_texdir}/texmf-dist/doc/fonts/cmll
%dir %{_texdir}/texmf-dist/doc/fonts/cm-super
%dir %{_texdir}/texmf-dist/doc/fonts/cm-unicode
%dir %{_texdir}/texmf-dist/doc/fonts/cns
%dir %{_texdir}/texmf-dist/doc/fonts/cns/cns40-1
%dir %{_texdir}/texmf-dist/doc/fonts/cns/cns40-2
%dir %{_texdir}/texmf-dist/doc/fonts/cns/cns40-3
%dir %{_texdir}/texmf-dist/doc/fonts/cns/cns40-4
%dir %{_texdir}/texmf-dist/doc/fonts/cns/cns40-5
%dir %{_texdir}/texmf-dist/doc/fonts/cns/cns40-6
%dir %{_texdir}/texmf-dist/doc/fonts/cns/cns40-7
%dir %{_texdir}/texmf-dist/doc/fonts/cns/cns40-b5
%dir %{_texdir}/texmf-dist/doc/fonts/concmath
%dir %{_texdir}/texmf-dist/doc/fonts/concmath-fonts
%dir %{_texdir}/texmf-dist/doc/fonts/concrete
%dir %{_texdir}/texmf-dist/doc/fonts/cyklop
%dir %{_texdir}/texmf-dist/doc/fonts/dice
%dir %{_texdir}/texmf-dist/doc/fonts/dictsym
%dir %{_texdir}/texmf-dist/doc/fonts/dingbat
%dir %{_texdir}/texmf-dist/doc/fonts/doublestroke
%dir %{_texdir}/texmf-dist/doc/fonts/dozenal
%dir %{_texdir}/texmf-dist/doc/fonts/ean
%dir %{_texdir}/texmf-dist/doc/fonts/ec
%dir %{_texdir}/texmf-dist/doc/fonts/ecc
%dir %{_texdir}/texmf-dist/doc/fonts/eco
%dir %{_texdir}/texmf-dist/doc/fonts/elvish
%dir %{_texdir}/texmf-dist/doc/fonts/enc
%dir %{_texdir}/texmf-dist/doc/fonts/enc/c90
%dir %{_texdir}/texmf-dist/doc/fonts/epigrafica
%dir %{_texdir}/texmf-dist/doc/fonts/esint-type1
%dir %{_texdir}/texmf-dist/doc/fonts/euro-ce
%dir %{_texdir}/texmf-dist/doc/fonts/eurofont
%dir %{_texdir}/texmf-dist/doc/fonts/eurosym
%dir %{_texdir}/texmf-dist/doc/fonts/eurosym/c
%dir %{_texdir}/texmf-dist/doc/fonts/eurosym/src
%dir %{_texdir}/texmf-dist/doc/fonts/fc
%dir %{_texdir}/texmf-dist/doc/fonts/feyn
%dir %{_texdir}/texmf-dist/doc/fonts/fge
%dir %{_texdir}/texmf-dist/doc/fonts/fonetika
%dir %{_texdir}/texmf-dist/doc/fonts/fontinst
%dir %{_texdir}/texmf-dist/doc/fonts/fontinst/encspecs
%dir %{_texdir}/texmf-dist/doc/fonts/fontinst/examples
%dir %{_texdir}/texmf-dist/doc/fonts/fontinst/examples/basic
%dir %{_texdir}/texmf-dist/doc/fonts/fontinst/examples/eurofont
%dir %{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptm
%dir %{_texdir}/texmf-dist/doc/fonts/fontinst/examples/mathptmx
%dir %{_texdir}/texmf-dist/doc/fonts/fontinst/manual
%dir %{_texdir}/texmf-dist/doc/fonts/fontinst/talks
%dir %{_texdir}/texmf-dist/doc/fonts/fontinst/test
%dir %{_texdir}/texmf-dist/doc/fonts/fontname
%dir %{_texdir}/texmf-dist/doc/fonts/fourier
%dir %{_texdir}/texmf-dist/doc/fonts/fouriernc
%dir %{_texdir}/texmf-dist/doc/fonts/fpl
%dir %{_texdir}/texmf-dist/doc/fonts/frcursive
%dir %{_texdir}/texmf-dist/doc/fonts/frcursive/doc
%dir %{_texdir}/texmf-dist/doc/fonts/frcursive/latex
%dir %{_texdir}/texmf-dist/doc/fonts/frcursive/mf
%dir %{_texdir}/texmf-dist/doc/fonts/frcursive/test
%dir %{_texdir}/texmf-dist/doc/fonts/free-math-font-survey
%dir %{_texdir}/texmf-dist/doc/fonts/free-math-font-survey/images
%dir %{_texdir}/texmf-dist/doc/fonts/free-math-font-survey/source
%dir %{_texdir}/texmf-dist/doc/fonts/genealogy
%dir %{_texdir}/texmf-dist/doc/fonts/gentium
%dir %{_texdir}/texmf-dist/doc/fonts/gentium/Gentium_1.02
%dir %{_texdir}/texmf-dist/doc/fonts/gentium/Gentium_Basic_1.1
%dir %{_texdir}/texmf-dist/doc/fonts/gfsartemisia
%dir %{_texdir}/texmf-dist/doc/fonts/gfsbaskerville
%dir %{_texdir}/texmf-dist/doc/fonts/gfsbodoni
%dir %{_texdir}/texmf-dist/doc/fonts/gfscomplutum
%dir %{_texdir}/texmf-dist/doc/fonts/gfsdidot
%dir %{_texdir}/texmf-dist/doc/fonts/gfsneohellenic
%dir %{_texdir}/texmf-dist/doc/fonts/gfsporson
%dir %{_texdir}/texmf-dist/doc/fonts/gfssolomos
%dir %{_texdir}/texmf-dist/doc/fonts/gnu-freefont
%dir %{_texdir}/texmf-dist/doc/fonts/gothic
%dir %{_texdir}/texmf-dist/doc/fonts/greenpoint
%dir %{_texdir}/texmf-dist/doc/fonts/grotesq
%dir %{_texdir}/texmf-dist/doc/fonts/hfbright
%dir %{_texdir}/texmf-dist/doc/fonts/hfoldsty
%dir %{_texdir}/texmf-dist/doc/fonts/ibygrk
%dir %{_texdir}/texmf-dist/doc/fonts/ifsym
%dir %{_texdir}/texmf-dist/doc/fonts/inconsolata
%dir %{_texdir}/texmf-dist/doc/fonts/initials
%dir %{_texdir}/texmf-dist/doc/fonts/itrans
%dir %{_texdir}/texmf-dist/doc/fonts/iwona
%dir %{_texdir}/texmf-dist/doc/fonts/jablantile
%dir %{_texdir}/texmf-dist/doc/fonts/junicode
%dir %{_texdir}/texmf-dist/doc/fonts/kdgreek
%dir %{_texdir}/texmf-dist/doc/fonts/kixfont
%dir %{_texdir}/texmf-dist/doc/fonts/knitting
%dir %{_texdir}/texmf-dist/doc/fonts/kpfonts
%dir %{_texdir}/texmf-dist/doc/fonts/kurier
%dir %{_texdir}/texmf-dist/doc/fonts/lfb
%dir %{_texdir}/texmf-dist/doc/fonts/lh
%dir %{_texdir}/texmf-dist/doc/fonts/lh/beresta
%dir %{_texdir}/texmf-dist/doc/fonts/lh/fonttest
%dir %{_texdir}/texmf-dist/doc/fonts/lh/lhfonts
%dir %{_texdir}/texmf-dist/doc/fonts/lh/samples
%dir %{_texdir}/texmf-dist/doc/fonts/libertine
%dir %{_texdir}/texmf-dist/doc/fonts/libertine/pdfs
%dir %{_texdir}/texmf-dist/doc/fonts/libris
%dir %{_texdir}/texmf-dist/doc/fonts/linearA
%dir %{_texdir}/texmf-dist/doc/fonts/lm
%dir %{_texdir}/texmf-dist/doc/fonts/lxfonts
%dir %{_texdir}/texmf-dist/doc/fonts/ly1
%dir %{_texdir}/texmf-dist/doc/fonts/malayalam
%dir %{_texdir}/texmf-dist/doc/fonts/malayalam/article
%dir %{_texdir}/texmf-dist/doc/fonts/marvosym
%dir %{_texdir}/texmf-dist/doc/fonts/marvosym/mac
%dir %{_texdir}/texmf-dist/doc/fonts/marvosym/mac/docs
%dir %{_texdir}/texmf-dist/doc/fonts/marvosym/mac/docs/obsolete
%dir %{_texdir}/texmf-dist/doc/fonts/marvosym/mac/oztex
%dir %{_texdir}/texmf-dist/doc/fonts/marvosym/mac/oztex/configs
%dir %{_texdir}/texmf-dist/doc/fonts/marvosym/mac/oztex/dvips
%dir %{_texdir}/texmf-dist/doc/fonts/marvosym/mac/oztex/dvips/inputs
%dir %{_texdir}/texmf-dist/doc/fonts/marvosym/mac/oztex/ps-files
%dir %{_texdir}/texmf-dist/doc/fonts/marvosym/mac/oztex/tex-font
%dir %{_texdir}/texmf-dist/doc/fonts/marvosym/mac/oztex/tex-font/misc
%dir %{_texdir}/texmf-dist/doc/fonts/marvosym/vtex
%dir %{_texdir}/texmf-dist/doc/fonts/mathabx
%dir %{_texdir}/texmf-dist/doc/fonts/memdesign
%dir %{_texdir}/texmf-dist/doc/fonts/metafont-beginners
%dir %{_texdir}/texmf-dist/doc/fonts/metafont-for-beginners
%dir %{_texdir}/texmf-dist/doc/fonts/nkarta
%dir %{_texdir}/texmf-dist/doc/fonts/oinuit
%dir %{_texdir}/texmf-dist/doc/fonts/oinuit/examples
%dir %{_texdir}/texmf-dist/doc/fonts/oldlatin
%dir %{_texdir}/texmf-dist/doc/fonts/oldstandard
%dir %{_texdir}/texmf-dist/doc/fonts/orkhun
%dir %{_texdir}/texmf-dist/doc/fonts/pacioli
%dir %{_texdir}/texmf-dist/doc/fonts/pclnfss
%dir %{_texdir}/texmf-dist/doc/fonts/phaistos
%dir %{_texdir}/texmf-dist/doc/fonts/pl
%dir %{_texdir}/texmf-dist/doc/fonts/pxfonts
%dir %{_texdir}/texmf-dist/doc/fonts/qpxqtx
%dir %{_texdir}/texmf-dist/doc/fonts/recycle
%dir %{_texdir}/texmf-dist/doc/fonts/romande
%dir %{_texdir}/texmf-dist/doc/fonts/rsfs
%dir %{_texdir}/texmf-dist/doc/fonts/semaphor
%dir %{_texdir}/texmf-dist/doc/fonts/skaknew
%dir %{_texdir}/texmf-dist/doc/fonts/staves
%dir %{_texdir}/texmf-dist/doc/fonts/stix
%dir %{_texdir}/texmf-dist/doc/fonts/stix/Glyphs
%dir %{_texdir}/texmf-dist/doc/fonts/stmaryrd
%dir %{_texdir}/texmf-dist/doc/fonts/tex-gyre
%dir %{_texdir}/texmf-dist/doc/fonts/tipa
%dir %{_texdir}/texmf-dist/doc/fonts/txfonts
%dir %{_texdir}/texmf-dist/doc/fonts/txfontsb
%dir %{_texdir}/texmf-dist/doc/fonts/Type1fonts
%dir %{_texdir}/texmf-dist/doc/fonts/uhc
%dir %{_texdir}/texmf-dist/doc/fonts/uhc/umj
%dir %{_texdir}/texmf-dist/doc/fonts/universa
%dir %{_texdir}/texmf-dist/doc/fonts/utopia
%dir %{_texdir}/texmf-dist/doc/fonts/venturisadf
%dir %{_texdir}/texmf-dist/doc/fonts/wasy
%dir %{_texdir}/texmf-dist/doc/fonts/xits
%dir %{_texdir}/texmf-dist/doc/fonts/xq
%dir %{_texdir}/texmf-dist/doc/fonts/zhmetrics
%dir %{_texdir}/texmf-dist/doc/generic
%dir %{_texdir}/texmf-dist/doc/generic/2up
%dir %{_texdir}/texmf-dist/doc/generic/abbr
%dir %{_texdir}/texmf-dist/doc/generic/around-the-bend
%dir %{_texdir}/texmf-dist/doc/generic/arrayjobx
%dir %{_texdir}/texmf-dist/doc/generic/babel
%dir %{_texdir}/texmf-dist/doc/generic/barr
%dir %{_texdir}/texmf-dist/doc/generic/colortab
%dir %{_texdir}/texmf-dist/doc/generic/components-of-TeX
%dir %{_texdir}/texmf-dist/doc/generic/c-pascal
%dir %{_texdir}/texmf-dist/doc/generic/c-pascal/prog
%dir %{_texdir}/texmf-dist/doc/generic/dcpic
%dir %{_texdir}/texmf-dist/doc/generic/dehyph-exptl
%dir %{_texdir}/texmf-dist/doc/generic/dirtree
%dir %{_texdir}/texmf-dist/doc/generic/doc-pictex
%dir %{_texdir}/texmf-dist/doc/generic/dratex
%dir %{_texdir}/texmf-dist/doc/generic/enctex
%dir %{_texdir}/texmf-dist/doc/generic/encxvlna
%dir %{_texdir}/texmf-dist/doc/generic/epsf
%dir %{_texdir}/texmf-dist/doc/generic/epsf/okay
%dir %{_texdir}/texmf-dist/doc/generic/es-tex-faq
%dir %{_texdir}/texmf-dist/doc/generic/FAQ-en
%dir %{_texdir}/texmf-dist/doc/generic/FAQ-en/html
%dir %{_texdir}/texmf-dist/doc/generic/fenixpar
%dir %{_texdir}/texmf-dist/doc/generic/fltpoint
%dir %{_texdir}/texmf-dist/doc/generic/frame
%dir %{_texdir}/texmf-dist/doc/generic/german
%dir %{_texdir}/texmf-dist/doc/generic/german/betatest
%dir %{_texdir}/texmf-dist/doc/generic/hyph-utf8
%dir %{_texdir}/texmf-dist/doc/generic/hyph-utf8/bg
%dir %{_texdir}/texmf-dist/doc/generic/hyph-utf8/es
%dir %{_texdir}/texmf-dist/doc/generic/hyph-utf8/hu
%dir %{_texdir}/texmf-dist/doc/generic/hyph-utf8/sa
%dir %{_texdir}/texmf-dist/doc/generic/iftex
%dir %{_texdir}/texmf-dist/doc/generic/ifxetex
%dir %{_texdir}/texmf-dist/doc/generic/insbox
%dir %{_texdir}/texmf-dist/doc/generic/kastrup
%dir %{_texdir}/texmf-dist/doc/generic/knuth
%dir %{_texdir}/texmf-dist/doc/generic/knuth/errata
%dir %{_texdir}/texmf-dist/doc/generic/knuth/etc
%dir %{_texdir}/texmf-dist/doc/generic/knuth/mf
%dir %{_texdir}/texmf-dist/doc/generic/knuth/mfware
%dir %{_texdir}/texmf-dist/doc/generic/knuth/tex
%dir %{_texdir}/texmf-dist/doc/generic/knuth/texware
%dir %{_texdir}/texmf-dist/doc/generic/knuth/web
%dir %{_texdir}/texmf-dist/doc/generic/latex-notes-zh-cn
%dir %{_texdir}/texmf-dist/doc/generic/latex-notes-zh-cn/src
%dir %{_texdir}/texmf-dist/doc/generic/latex-notes-zh-cn/src/examples
%dir %{_texdir}/texmf-dist/doc/generic/librarian
%dir %{_texdir}/texmf-dist/doc/generic/mathdots
%dir %{_texdir}/texmf-dist/doc/generic/mfpic
%dir %{_texdir}/texmf-dist/doc/generic/mfpic/examples
%dir %{_texdir}/texmf-dist/doc/generic/midnight
%dir %{_texdir}/texmf-dist/doc/generic/multido
%dir %{_texdir}/texmf-dist/doc/generic/musixps
%dir %{_texdir}/texmf-dist/doc/generic/musixtex
%dir %{_texdir}/texmf-dist/doc/generic/musixtex/examples
%dir %{_texdir}/texmf-dist/doc/generic/ofs
%dir %{_texdir}/texmf-dist/doc/generic/pdf-trans
%dir %{_texdir}/texmf-dist/doc/generic/pgf
%dir %{_texdir}/texmf-dist/doc/generic/pgf/images
%dir %{_texdir}/texmf-dist/doc/generic/pgf/licenses
%dir %{_texdir}/texmf-dist/doc/generic/pgf/macros
%dir %{_texdir}/texmf-dist/doc/generic/pgfplots
%dir %{_texdir}/texmf-dist/doc/generic/pgf/text-en
%dir %{_texdir}/texmf-dist/doc/generic/pgf/text-en/plots
%dir %{_texdir}/texmf-dist/doc/generic/pgf/version-for-dvipdfm
%dir %{_texdir}/texmf-dist/doc/generic/pgf/version-for-dvipdfm/en
%dir %{_texdir}/texmf-dist/doc/generic/pgf/version-for-dvips
%dir %{_texdir}/texmf-dist/doc/generic/pgf/version-for-dvips/en
%dir %{_texdir}/texmf-dist/doc/generic/pgf/version-for-pdftex
%dir %{_texdir}/texmf-dist/doc/generic/pgf/version-for-pdftex/en
%dir %{_texdir}/texmf-dist/doc/generic/pgf/version-for-tex4ht
%dir %{_texdir}/texmf-dist/doc/generic/pgf/version-for-tex4ht/en
%dir %{_texdir}/texmf-dist/doc/generic/pgf/version-for-vtex
%dir %{_texdir}/texmf-dist/doc/generic/pgf/version-for-vtex/en
%dir %{_texdir}/texmf-dist/doc/generic/pgf/version-for-vtex/en/plots
%dir %{_texdir}/texmf-dist/doc/generic/poster-mac
%dir %{_texdir}/texmf-dist/doc/generic/pst-2dplot
%dir %{_texdir}/texmf-dist/doc/generic/pst-3d
%dir %{_texdir}/texmf-dist/doc/generic/pst-3dplot
%dir %{_texdir}/texmf-dist/doc/generic/pst-abspos
%dir %{_texdir}/texmf-dist/doc/generic/pst-am
%dir %{_texdir}/texmf-dist/doc/generic/pst-asr
%dir %{_texdir}/texmf-dist/doc/generic/pst-bar
%dir %{_texdir}/texmf-dist/doc/generic/pst-barcode
%dir %{_texdir}/texmf-dist/doc/generic/pst-bezier
%dir %{_texdir}/texmf-dist/doc/generic/pst-blur
%dir %{_texdir}/texmf-dist/doc/generic/pst-bspline
%dir %{_texdir}/texmf-dist/doc/generic/pst-circ
%dir %{_texdir}/texmf-dist/doc/generic/pst-circ/more_docs
%dir %{_texdir}/texmf-dist/doc/generic/pst-coil
%dir %{_texdir}/texmf-dist/doc/generic/pst-cox
%dir %{_texdir}/texmf-dist/doc/generic/pst-cox/pst-coxcoor
%dir %{_texdir}/texmf-dist/doc/generic/pst-cox/pst-coxeterp
%dir %{_texdir}/texmf-dist/doc/generic/pst-dbicons
%dir %{_texdir}/texmf-dist/doc/generic/pst-diffraction
%dir %{_texdir}/texmf-dist/doc/generic/pst-electricfield
%dir %{_texdir}/texmf-dist/doc/generic/pst-eps
%dir %{_texdir}/texmf-dist/doc/generic/pst-eucl
%dir %{_texdir}/texmf-dist/doc/generic/pst-eucl/Exemples
%dir %{_texdir}/texmf-dist/doc/generic/pst-fill
%dir %{_texdir}/texmf-dist/doc/generic/pst-fr3d
%dir %{_texdir}/texmf-dist/doc/generic/pst-fractal
%dir %{_texdir}/texmf-dist/doc/generic/pst-fun
%dir %{_texdir}/texmf-dist/doc/generic/pst-func
%dir %{_texdir}/texmf-dist/doc/generic/pst-gantt
%dir %{_texdir}/texmf-dist/doc/generic/pst-geo
%dir %{_texdir}/texmf-dist/doc/generic/pst-ghsb
%dir %{_texdir}/texmf-dist/doc/generic/pst-gr3d
%dir %{_texdir}/texmf-dist/doc/generic/pst-grad
%dir %{_texdir}/texmf-dist/doc/generic/pst-infixplot
%dir %{_texdir}/texmf-dist/doc/generic/pst-jtree
%dir %{_texdir}/texmf-dist/doc/generic/pst-knot
%dir %{_texdir}/texmf-dist/doc/generic/pst-labo
%dir %{_texdir}/texmf-dist/doc/generic/pst-lens
%dir %{_texdir}/texmf-dist/doc/generic/pst-light3d
%dir %{_texdir}/texmf-dist/doc/generic/pst-magneticfield
%dir %{_texdir}/texmf-dist/doc/generic/pst-math
%dir %{_texdir}/texmf-dist/doc/generic/pst-mirror
%dir %{_texdir}/texmf-dist/doc/generic/pst-node
%dir %{_texdir}/texmf-dist/doc/generic/pst-node/more_docs
%dir %{_texdir}/texmf-dist/doc/generic/pst-ob3d
%dir %{_texdir}/texmf-dist/doc/generic/pst-optexp
%dir %{_texdir}/texmf-dist/doc/generic/pst-optic
%dir %{_texdir}/texmf-dist/doc/generic/pst-osci
%dir %{_texdir}/texmf-dist/doc/generic/pst-pad
%dir %{_texdir}/texmf-dist/doc/generic/pst-pdgr
%dir %{_texdir}/texmf-dist/doc/generic/pst-platon
%dir %{_texdir}/texmf-dist/doc/generic/pst-plot
%dir %{_texdir}/texmf-dist/doc/generic/pst-plot/more_docs
%dir %{_texdir}/texmf-dist/doc/generic/pst-poly
%dir %{_texdir}/texmf-dist/doc/generic/pst-qtree
%dir %{_texdir}/texmf-dist/doc/generic/pstricks
%dir %{_texdir}/texmf-dist/doc/generic/pstricks-add
%dir %{_texdir}/texmf-dist/doc/generic/pstricks/images
%dir %{_texdir}/texmf-dist/doc/generic/pstricks-tutorial
%dir %{_texdir}/texmf-dist/doc/generic/pst-sigsys
%dir %{_texdir}/texmf-dist/doc/generic/pst-slpe
%dir %{_texdir}/texmf-dist/doc/generic/pst-solides3d
%dir %{_texdir}/texmf-dist/doc/generic/pst-solides3d/doc-en
%dir %{_texdir}/texmf-dist/doc/generic/pst-soroban
%dir %{_texdir}/texmf-dist/doc/generic/pst-spectra
%dir %{_texdir}/texmf-dist/doc/generic/pst-stru
%dir %{_texdir}/texmf-dist/doc/generic/pst-support
%dir %{_texdir}/texmf-dist/doc/generic/pst-text
%dir %{_texdir}/texmf-dist/doc/generic/pst-thick
%dir %{_texdir}/texmf-dist/doc/generic/pst-tree
%dir %{_texdir}/texmf-dist/doc/generic/pst-uml
%dir %{_texdir}/texmf-dist/doc/generic/pst-vue3d
%dir %{_texdir}/texmf-dist/doc/generic/rlepsf
%dir %{_texdir}/texmf-dist/doc/generic/shapepar
%dir %{_texdir}/texmf-dist/doc/generic/t2
%dir %{_texdir}/texmf-dist/doc/generic/t2/etc
%dir %{_texdir}/texmf-dist/doc/generic/t2/etc/rubibtex
%dir %{_texdir}/texmf-dist/doc/generic/t2/etc/rumkidx
%dir %{_texdir}/texmf-dist/doc/generic/t2/etc/utf-8
%dir %{_texdir}/texmf-dist/doc/generic/t2/examples
%dir %{_texdir}/texmf-dist/doc/generic/tap
%dir %{_texdir}/texmf-dist/doc/generic/tds
%dir %{_texdir}/texmf-dist/doc/generic/tex4ht
%dir %{_texdir}/texmf-dist/doc/generic/texapi
%dir %{_texdir}/texmf-dist/doc/generic/tex-ewd
%dir %{_texdir}/texmf-dist/doc/generic/tex-ps
%dir %{_texdir}/texmf-dist/doc/generic/tex-ps/cmyk-hax
%dir %{_texdir}/texmf-dist/doc/generic/tex-ps/poligraf
%dir %{_texdir}/texmf-dist/doc/generic/tex-refs
%dir %{_texdir}/texmf-dist/doc/generic/textmerg
%dir %{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl
%dir %{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/context
%dir %{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/fonty
%dir %{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/gify
%dir %{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/idx
%dir %{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/kuchnia
%dir %{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e
%dir %{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/listy
%dir %{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/macro
%dir %{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/pagina
%dir %{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/spisy
%dir %{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/latex2e/tytuly
%dir %{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/poczatki
%dir %{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/podstawy
%dir %{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/prog
%dir %{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/prog/bibtex
%dir %{_texdir}/texmf-dist/doc/generic/tex-virtual-academy-pl/tex
%dir %{_texdir}/texmf-dist/doc/generic/thumbpdf
%dir %{_texdir}/texmf-dist/doc/generic/ukrhyph
%dir %{_texdir}/texmf-dist/doc/generic/ulem
%dir %{_texdir}/texmf-dist/doc/generic/variations
%dir %{_texdir}/texmf-dist/doc/generic/vaucanson-g
%dir %{_texdir}/texmf-dist/doc/generic/vaucanson-g/VCManual-src
%dir %{_texdir}/texmf-dist/doc/generic/velthuis
%dir %{_texdir}/texmf-dist/doc/generic/vntex
%dir %{_texdir}/texmf-dist/doc/generic/voss-de
%dir %{_texdir}/texmf-dist/doc/generic/voss-de/gauss
%dir %{_texdir}/texmf-dist/doc/generic/voss-de/InlineMath
%dir %{_texdir}/texmf-dist/doc/generic/voss-de/mathCol
%dir %{_texdir}/texmf-dist/doc/generic/wsuipa
%dir %{_texdir}/texmf-dist/doc/generic/wsuipa/latex209
%dir %{_texdir}/texmf-dist/doc/generic/wsuipa/latex2e
%dir %{_texdir}/texmf-dist/doc/generic/wsuipa/text1
%dir %{_texdir}/texmf-dist/doc/generic/xcomment
%dir %{_texdir}/texmf-dist/doc/generic/xlop
%dir %{_texdir}/texmf-dist/doc/generic/xstring
%dir %{_texdir}/texmf-dist/doc/generic/xypic
%dir %{_texdir}/texmf-dist/doc/generic/xypic/support
%dir %{_texdir}/texmf-dist/doc/generic/xypic-tut-pt
%dir %{_texdir}/texmf-dist/doc/generic/yax
%dir %{_texdir}/texmf-dist/doc/latex
%dir %{_texdir}/texmf-dist/doc/latex/12many
%dir %{_texdir}/texmf-dist/doc/latex/a0poster
%dir %{_texdir}/texmf-dist/doc/latex/a5comb
%dir %{_texdir}/texmf-dist/doc/latex/aastex
%dir %{_texdir}/texmf-dist/doc/latex/abc
%dir %{_texdir}/texmf-dist/doc/latex/abstract
%dir %{_texdir}/texmf-dist/doc/latex/achemso
%dir %{_texdir}/texmf-dist/doc/latex/acmconf
%dir %{_texdir}/texmf-dist/doc/latex/acromake
%dir %{_texdir}/texmf-dist/doc/latex/acronym
%dir %{_texdir}/texmf-dist/doc/latex/active-conf
%dir %{_texdir}/texmf-dist/doc/latex/active-conf/example
%dir %{_texdir}/texmf-dist/doc/latex/addlines
%dir %{_texdir}/texmf-dist/doc/latex/adrconv
%dir %{_texdir}/texmf-dist/doc/latex/adrconv/adrconv_pages08.pages
%dir %{_texdir}/texmf-dist/doc/latex/adrconv/adrconv_pages08.pages/Contents
%dir %{_texdir}/texmf-dist/doc/latex/adrconv/adrconv_pages08.pages/QuickLook
%dir %{_texdir}/texmf-dist/doc/latex/aeguill
%dir %{_texdir}/texmf-dist/doc/latex/afthesis
%dir %{_texdir}/texmf-dist/doc/latex/aguplus
%dir %{_texdir}/texmf-dist/doc/latex/aiaa
%dir %{_texdir}/texmf-dist/doc/latex/aiaa/pre2004
%dir %{_texdir}/texmf-dist/doc/latex/aiaa/pre2004/demos
%dir %{_texdir}/texmf-dist/doc/latex/aiaa/pre2004/demos/paper
%dir %{_texdir}/texmf-dist/doc/latex/aiaa/pre2004/demos/refs
%dir %{_texdir}/texmf-dist/doc/latex/aiaa/pre2004/demos/subfigs
%dir %{_texdir}/texmf-dist/doc/latex/aiaa/pre2004/demos/talk
%dir %{_texdir}/texmf-dist/doc/latex/AkkTeX
%dir %{_texdir}/texmf-dist/doc/latex/akletter
%dir %{_texdir}/texmf-dist/doc/latex/alg
%dir %{_texdir}/texmf-dist/doc/latex/algorithm2e
%dir %{_texdir}/texmf-dist/doc/latex/algorithmicx
%dir %{_texdir}/texmf-dist/doc/latex/algorithms
%dir %{_texdir}/texmf-dist/doc/latex/alnumsec
%dir %{_texdir}/texmf-dist/doc/latex/alterqcm
%dir %{_texdir}/texmf-dist/doc/latex/alterqcm/doc
%dir %{_texdir}/texmf-dist/doc/latex/altfont
%dir %{_texdir}/texmf-dist/doc/latex/ametsoc
%dir %{_texdir}/texmf-dist/doc/latex/ametsoc/bibliography
%dir %{_texdir}/texmf-dist/doc/latex/ametsoc/figures
%dir %{_texdir}/texmf-dist/doc/latex/amsaddr
%dir %{_texdir}/texmf-dist/doc/latex/amscls
%dir %{_texdir}/texmf-dist/doc/latex/amslatex-primer
%dir %{_texdir}/texmf-dist/doc/latex/amsldoc-it
%dir %{_texdir}/texmf-dist/doc/latex/amsldoc-vn
%dir %{_texdir}/texmf-dist/doc/latex/amsmath
%dir %{_texdir}/texmf-dist/doc/latex/amsmath-it
%dir %{_texdir}/texmf-dist/doc/latex/amsrefs
%dir %{_texdir}/texmf-dist/doc/latex/amsthdoc-it
%dir %{_texdir}/texmf-dist/doc/latex/animate
%dir %{_texdir}/texmf-dist/doc/latex/animate/files
%dir %{_texdir}/texmf-dist/doc/latex/anonchap
%dir %{_texdir}/texmf-dist/doc/latex/answers
%dir %{_texdir}/texmf-dist/doc/latex/antt
%dir %{_texdir}/texmf-dist/doc/latex/ANUfinalexam
%dir %{_texdir}/texmf-dist/doc/latex/anyfontsize
%dir %{_texdir}/texmf-dist/doc/latex/anysize
%dir %{_texdir}/texmf-dist/doc/latex/apa
%dir %{_texdir}/texmf-dist/doc/latex/apacite
%dir %{_texdir}/texmf-dist/doc/latex/appendix
%dir %{_texdir}/texmf-dist/doc/latex/apprends-latex
%dir %{_texdir}/texmf-dist/doc/latex/apprends-latex/exemples
%dir %{_texdir}/texmf-dist/doc/latex/ar
%dir %{_texdir}/texmf-dist/doc/latex/arabi
%dir %{_texdir}/texmf-dist/doc/latex/arabtex
%dir %{_texdir}/texmf-dist/doc/latex/arcs
%dir %{_texdir}/texmf-dist/doc/latex/arsclassica
%dir %{_texdir}/texmf-dist/doc/latex/arsclassica/Chapters
%dir %{_texdir}/texmf-dist/doc/latex/arsclassica/FrontBackMatter
%dir %{_texdir}/texmf-dist/doc/latex/arsclassica/Graphics
%dir %{_texdir}/texmf-dist/doc/latex/arsclassica/Italian
%dir %{_texdir}/texmf-dist/doc/latex/arsclassica/Italian/Capitoli
%dir %{_texdir}/texmf-dist/doc/latex/arsclassica/Italian/Immagini
%dir %{_texdir}/texmf-dist/doc/latex/arsclassica/Italian/MaterialeInizialeFinale
%dir %{_texdir}/texmf-dist/doc/latex/arydshln
%dir %{_texdir}/texmf-dist/doc/latex/asaetr
%dir %{_texdir}/texmf-dist/doc/latex/ascelike
%dir %{_texdir}/texmf-dist/doc/latex/assignment
%dir %{_texdir}/texmf-dist/doc/latex/asyfig
%dir %{_texdir}/texmf-dist/doc/latex/asyfig/example
%dir %{_texdir}/texmf-dist/doc/latex/attachfile
%dir %{_texdir}/texmf-dist/doc/latex/augie
%dir %{_texdir}/texmf-dist/doc/latex/augie/other
%dir %{_texdir}/texmf-dist/doc/latex/augie/vtex
%dir %{_texdir}/texmf-dist/doc/latex/aurical
%dir %{_texdir}/texmf-dist/doc/latex/authoraftertitle
%dir %{_texdir}/texmf-dist/doc/latex/authorindex
%dir %{_texdir}/texmf-dist/doc/latex/autoarea
%dir %{_texdir}/texmf-dist/doc/latex/autoarea/autodemo
%dir %{_texdir}/texmf-dist/doc/latex/auto-pst-pdf
%dir %{_texdir}/texmf-dist/doc/latex/babelbib
%dir %{_texdir}/texmf-dist/doc/latex/background
%dir %{_texdir}/texmf-dist/doc/latex/bangtex
%dir %{_texdir}/texmf-dist/doc/latex/barcodes
%dir %{_texdir}/texmf-dist/doc/latex/bardiag
%dir %{_texdir}/texmf-dist/doc/latex/bardiag/example
%dir %{_texdir}/texmf-dist/doc/latex/bardiag/example/src
%dir %{_texdir}/texmf-dist/doc/latex/bardiag/figs
%dir %{_texdir}/texmf-dist/doc/latex/bardiag/src
%dir %{_texdir}/texmf-dist/doc/latex/base
%dir %{_texdir}/texmf-dist/doc/latex/bayer
%dir %{_texdir}/texmf-dist/doc/latex/bbding
%dir %{_texdir}/texmf-dist/doc/latex/bbm-macros
%dir %{_texdir}/texmf-dist/doc/latex/bbold
%dir %{_texdir}/texmf-dist/doc/latex/bclogo
%dir %{_texdir}/texmf-dist/doc/latex/beamer
%dir %{_texdir}/texmf-dist/doc/latex/beamer-contrib
%dir %{_texdir}/texmf-dist/doc/latex/beamer/doc
%dir %{_texdir}/texmf-dist/doc/latex/beamer/doc/licenses
%dir %{_texdir}/texmf-dist/doc/latex/beamer/doc/themeexamples
%dir %{_texdir}/texmf-dist/doc/latex/beamer/emacs
%dir %{_texdir}/texmf-dist/doc/latex/beamer/examples
%dir %{_texdir}/texmf-dist/doc/latex/beamer/examples/a-conference-talk
%dir %{_texdir}/texmf-dist/doc/latex/beamer/examples/a-lecture
%dir %{_texdir}/texmf-dist/doc/latex/beamer/examples/lyx-based-presentation
%dir %{_texdir}/texmf-dist/doc/latex/beamer-FUBerlin
%dir %{_texdir}/texmf-dist/doc/latex/beamerposter
%dir %{_texdir}/texmf-dist/doc/latex/beamer/solutions
%dir %{_texdir}/texmf-dist/doc/latex/beamer/solutions/conference-talks
%dir %{_texdir}/texmf-dist/doc/latex/beamer/solutions/generic-talks
%dir %{_texdir}/texmf-dist/doc/latex/beamer/solutions/short-talks
%dir %{_texdir}/texmf-dist/doc/latex/beamer-tut-pt
%dir %{_texdir}/texmf-dist/doc/latex/begriff
%dir %{_texdir}/texmf-dist/doc/latex/betababel
%dir %{_texdir}/texmf-dist/doc/latex/beton
%dir %{_texdir}/texmf-dist/doc/latex/bez123
%dir %{_texdir}/texmf-dist/doc/latex/bezos
%dir %{_texdir}/texmf-dist/doc/latex/bgreek
%dir %{_texdir}/texmf-dist/doc/latex/bibarts
%dir %{_texdir}/texmf-dist/doc/latex/bibexport
%dir %{_texdir}/texmf-dist/doc/latex/biblatex
%dir %{_texdir}/texmf-dist/doc/latex/biblatex-apa
%dir %{_texdir}/texmf-dist/doc/latex/biblatex-chem
%dir %{_texdir}/texmf-dist/doc/latex/biblatex-chem/examples
%dir %{_texdir}/texmf-dist/doc/latex/biblatex-chicago-notes-df
%dir %{_texdir}/texmf-dist/doc/latex/biblatex-dw
%dir %{_texdir}/texmf-dist/doc/latex/biblatex-dw/examples
%dir %{_texdir}/texmf-dist/doc/latex/biblatex/examples
%dir %{_texdir}/texmf-dist/doc/latex/biblatex-historian
%dir %{_texdir}/texmf-dist/doc/latex/biblatex-nature
%dir %{_texdir}/texmf-dist/doc/latex/biblatex-philosophy
%dir %{_texdir}/texmf-dist/doc/latex/biblatex/resources
%dir %{_texdir}/texmf-dist/doc/latex/biblatex-science
%dir %{_texdir}/texmf-dist/doc/latex/bibleref
%dir %{_texdir}/texmf-dist/doc/latex/biblist
%dir %{_texdir}/texmf-dist/doc/latex/bibtopic
%dir %{_texdir}/texmf-dist/doc/latex/bibtopicprefix
%dir %{_texdir}/texmf-dist/doc/latex/bibunits
%dir %{_texdir}/texmf-dist/doc/latex/bidi
%dir %{_texdir}/texmf-dist/doc/latex/bigfoot
%dir %{_texdir}/texmf-dist/doc/latex/bigints
%dir %{_texdir}/texmf-dist/doc/latex/binomexp
%dir %{_texdir}/texmf-dist/doc/latex/biocon
%dir %{_texdir}/texmf-dist/doc/latex/bizcard
%dir %{_texdir}/texmf-dist/doc/latex/blindtext
%dir %{_texdir}/texmf-dist/doc/latex/blkarray
%dir %{_texdir}/texmf-dist/doc/latex/block
%dir %{_texdir}/texmf-dist/doc/latex/blowup
%dir %{_texdir}/texmf-dist/doc/latex/boites
%dir %{_texdir}/texmf-dist/doc/latex/bold-extra
%dir %{_texdir}/texmf-dist/doc/latex/boldtensors
%dir %{_texdir}/texmf-dist/doc/latex/bookest
%dir %{_texdir}/texmf-dist/doc/latex/booklet
%dir %{_texdir}/texmf-dist/doc/latex/booktabs
%dir %{_texdir}/texmf-dist/doc/latex/boolexpr
%dir %{_texdir}/texmf-dist/doc/latex/bophook
%dir %{_texdir}/texmf-dist/doc/latex/bosisio
%dir %{_texdir}/texmf-dist/doc/latex/boxedminipage
%dir %{_texdir}/texmf-dist/doc/latex/boxhandler
%dir %{_texdir}/texmf-dist/doc/latex/bpchem
%dir %{_texdir}/texmf-dist/doc/latex/bracketkey
%dir %{_texdir}/texmf-dist/doc/latex/braille
%dir %{_texdir}/texmf-dist/doc/latex/braket
%dir %{_texdir}/texmf-dist/doc/latex/breakurl
%dir %{_texdir}/texmf-dist/doc/latex/brushscr
%dir %{_texdir}/texmf-dist/doc/latex/bullcntr
%dir %{_texdir}/texmf-dist/doc/latex/bussproofs
%dir %{_texdir}/texmf-dist/doc/latex/bytefield
%dir %{_texdir}/texmf-dist/doc/latex/cachepic
%dir %{_texdir}/texmf-dist/doc/latex/calctab
%dir %{_texdir}/texmf-dist/doc/latex/calligra
%dir %{_texdir}/texmf-dist/doc/latex/calrsfs
%dir %{_texdir}/texmf-dist/doc/latex/calxxxx
%dir %{_texdir}/texmf-dist/doc/latex/cancel
%dir %{_texdir}/texmf-dist/doc/latex/captcont
%dir %{_texdir}/texmf-dist/doc/latex/captdef
%dir %{_texdir}/texmf-dist/doc/latex/caption
%dir %{_texdir}/texmf-dist/doc/latex/capt-of
%dir %{_texdir}/texmf-dist/doc/latex/carlisle
%dir %{_texdir}/texmf-dist/doc/latex/cases
%dir %{_texdir}/texmf-dist/doc/latex/casyl
%dir %{_texdir}/texmf-dist/doc/latex/catechis
%dir %{_texdir}/texmf-dist/doc/latex/cbcoptic
%dir %{_texdir}/texmf-dist/doc/latex/ccaption
%dir %{_texdir}/texmf-dist/doc/latex/ccfonts
%dir %{_texdir}/texmf-dist/doc/latex/ccicons
%dir %{_texdir}/texmf-dist/doc/latex/cclicenses
%dir %{_texdir}/texmf-dist/doc/latex/cd
%dir %{_texdir}/texmf-dist/doc/latex/cd-cover
%dir %{_texdir}/texmf-dist/doc/latex/cdpbundl
%dir %{_texdir}/texmf-dist/doc/latex/cell
%dir %{_texdir}/texmf-dist/doc/latex/cellspace
%dir %{_texdir}/texmf-dist/doc/latex/changebar
%dir %{_texdir}/texmf-dist/doc/latex/changelayout
%dir %{_texdir}/texmf-dist/doc/latex/changepage
%dir %{_texdir}/texmf-dist/doc/latex/changes
%dir %{_texdir}/texmf-dist/doc/latex/chappg
%dir %{_texdir}/texmf-dist/doc/latex/chapterfolder
%dir %{_texdir}/texmf-dist/doc/latex/chbibref
%dir %{_texdir}/texmf-dist/doc/latex/chembst
%dir %{_texdir}/texmf-dist/doc/latex/chemcompounds
%dir %{_texdir}/texmf-dist/doc/latex/chemcono
%dir %{_texdir}/texmf-dist/doc/latex/chemfig
%dir %{_texdir}/texmf-dist/doc/latex/chemstyle
%dir %{_texdir}/texmf-dist/doc/latex/chessboard
%dir %{_texdir}/texmf-dist/doc/latex/chessfss
%dir %{_texdir}/texmf-dist/doc/latex/chess-problem-diagrams
%dir %{_texdir}/texmf-dist/doc/latex/chletter
%dir %{_texdir}/texmf-dist/doc/latex/chngcntr
%dir %{_texdir}/texmf-dist/doc/latex/chronology
%dir %{_texdir}/texmf-dist/doc/latex/circ
%dir %{_texdir}/texmf-dist/doc/latex/circuitikz
%dir %{_texdir}/texmf-dist/doc/latex/cite
%dir %{_texdir}/texmf-dist/doc/latex/cjk
%dir %{_texdir}/texmf-dist/doc/latex/cjk/doc
%dir %{_texdir}/texmf-dist/doc/latex/cjk/doc/chinese
%dir %{_texdir}/texmf-dist/doc/latex/cjk/doc/cjk
%dir %{_texdir}/texmf-dist/doc/latex/cjk/doc/japanese
%dir %{_texdir}/texmf-dist/doc/latex/cjk/doc/pdf
%dir %{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto
%dir %{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/examples
%dir %{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/examples/texinput
%dir %{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/examples/texinput/Bg5
%dir %{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/examples/texinput/GB
%dir %{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/examples/texinput/JIS
%dir %{_texdir}/texmf-dist/doc/latex/cjk/doc/pdfhowto/examples/texinput/SJIS
%dir %{_texdir}/texmf-dist/doc/latex/cjk/examples
%dir %{_texdir}/texmf-dist/doc/latex/cjk/examples/cjk
%dir %{_texdir}/texmf-dist/doc/latex/cjk/examples/pdf
%dir %{_texdir}/texmf-dist/doc/latex/cjkpunct
%dir %{_texdir}/texmf-dist/doc/latex/cjkpunct/examples
%dir %{_texdir}/texmf-dist/doc/latex/cjkpunct/setpunct
%dir %{_texdir}/texmf-dist/doc/latex/cjk/texlive
%dir %{_texdir}/texmf-dist/doc/latex/cjk/utils
%dir %{_texdir}/texmf-dist/doc/latex/cjk/utils/pyhyphen
%dir %{_texdir}/texmf-dist/doc/latex/classicthesis
%dir %{_texdir}/texmf-dist/doc/latex/classicthesis/Chapters
%dir %{_texdir}/texmf-dist/doc/latex/classicthesis/Examples
%dir %{_texdir}/texmf-dist/doc/latex/classicthesis/FrontBackmatter
%dir %{_texdir}/texmf-dist/doc/latex/classicthesis/gfx
%dir %{_texdir}/texmf-dist/doc/latex/clefval
%dir %{_texdir}/texmf-dist/doc/latex/cleveref
%dir %{_texdir}/texmf-dist/doc/latex/clock
%dir %{_texdir}/texmf-dist/doc/latex/clrscode
%dir %{_texdir}/texmf-dist/doc/latex/cmap
%dir %{_texdir}/texmf-dist/doc/latex/cmbright
%dir %{_texdir}/texmf-dist/doc/latex/cmdstring
%dir %{_texdir}/texmf-dist/doc/latex/cmdtrack
%dir %{_texdir}/texmf-dist/doc/latex/cm-lgc
%dir %{_texdir}/texmf-dist/doc/latex/cmpica
%dir %{_texdir}/texmf-dist/doc/latex/cmsd
%dir %{_texdir}/texmf-dist/doc/latex/codedoc
%dir %{_texdir}/texmf-dist/doc/latex/collref
%dir %{_texdir}/texmf-dist/doc/latex/colordoc
%dir %{_texdir}/texmf-dist/doc/latex/colorinfo
%dir %{_texdir}/texmf-dist/doc/latex/colortbl
%dir %{_texdir}/texmf-dist/doc/latex/colorwav
%dir %{_texdir}/texmf-dist/doc/latex/combelow
%dir %{_texdir}/texmf-dist/doc/latex/combine
%dir %{_texdir}/texmf-dist/doc/latex/combinedgraphics
%dir %{_texdir}/texmf-dist/doc/latex/combinedgraphics/test
%dir %{_texdir}/texmf-dist/doc/latex/comma
%dir %{_texdir}/texmf-dist/doc/latex/commath
%dir %{_texdir}/texmf-dist/doc/latex/comment
%dir %{_texdir}/texmf-dist/doc/latex/complexity
%dir %{_texdir}/texmf-dist/doc/latex/comprehensive
%dir %{_texdir}/texmf-dist/doc/latex/comprehensive/source
%dir %{_texdir}/texmf-dist/doc/latex/computational-complexity
%dir %{_texdir}/texmf-dist/doc/latex/concprog
%dir %{_texdir}/texmf-dist/doc/latex/confproc
%dir %{_texdir}/texmf-dist/doc/latex/confproc/example
%dir %{_texdir}/texmf-dist/doc/latex/confproc/example/papers
%dir %{_texdir}/texmf-dist/doc/latex/confproc/example/papers/sources_pdftex
%dir %{_texdir}/texmf-dist/doc/latex/confproc/example/papers/sources_pdftex/p_001
%dir %{_texdir}/texmf-dist/doc/latex/confproc/example/papers/sources_pdftex/p_003
%dir %{_texdir}/texmf-dist/doc/latex/confproc/example/papers/sources_pdftex/p_005
%dir %{_texdir}/texmf-dist/doc/latex/confproc/example/papers/sources_pdftex/p_007
%dir %{_texdir}/texmf-dist/doc/latex/confproc/example/papers/sources_tex
%dir %{_texdir}/texmf-dist/doc/latex/confproc/example/papers/sources_tex/p_009
%dir %{_texdir}/texmf-dist/doc/latex/confproc/example/pictures
%dir %{_texdir}/texmf-dist/doc/latex/constants
%dir %{_texdir}/texmf-dist/doc/latex/contour
%dir %{_texdir}/texmf-dist/doc/latex/cooking
%dir %{_texdir}/texmf-dist/doc/latex/cookybooky
%dir %{_texdir}/texmf-dist/doc/latex/cookybooky/documentation
%dir %{_texdir}/texmf-dist/doc/latex/cookybooky/examples
%dir %{_texdir}/texmf-dist/doc/latex/cookybooky/examples/graphics
%dir %{_texdir}/texmf-dist/doc/latex/cool
%dir %{_texdir}/texmf-dist/doc/latex/coollist
%dir %{_texdir}/texmf-dist/doc/latex/coolstr
%dir %{_texdir}/texmf-dist/doc/latex/cooltooltips
%dir %{_texdir}/texmf-dist/doc/latex/coordsys
%dir %{_texdir}/texmf-dist/doc/latex/courier-scaled
%dir %{_texdir}/texmf-dist/doc/latex/courseoutline
%dir %{_texdir}/texmf-dist/doc/latex/coursepaper
%dir %{_texdir}/texmf-dist/doc/latex/coverpage
%dir %{_texdir}/texmf-dist/doc/latex/covington
%dir %{_texdir}/texmf-dist/doc/latex/crop
%dir %{_texdir}/texmf-dist/doc/latex/crossreference
%dir %{_texdir}/texmf-dist/doc/latex/crossword
%dir %{_texdir}/texmf-dist/doc/latex/crosswrd
%dir %{_texdir}/texmf-dist/doc/latex/cryst
%dir %{_texdir}/texmf-dist/doc/latex/csbulletin
%dir %{_texdir}/texmf-dist/doc/latex/csquotes
%dir %{_texdir}/texmf-dist/doc/latex/csvtools
%dir %{_texdir}/texmf-dist/doc/latex/ctable
%dir %{_texdir}/texmf-dist/doc/latex/ctex
%dir %{_texdir}/texmf-dist/doc/latex/ctex-faq
%dir %{_texdir}/texmf-dist/doc/latex/ctex-faq/src
%dir %{_texdir}/texmf-dist/doc/latex/ctex/test
%dir %{_texdir}/texmf-dist/doc/latex/ctib
%dir %{_texdir}/texmf-dist/doc/latex/cuisine
%dir %{_texdir}/texmf-dist/doc/latex/currfile
%dir %{_texdir}/texmf-dist/doc/latex/currvita
%dir %{_texdir}/texmf-dist/doc/latex/cursolatex
%dir %{_texdir}/texmf-dist/doc/latex/cursolatex/src
%dir %{_texdir}/texmf-dist/doc/latex/curve
%dir %{_texdir}/texmf-dist/doc/latex/curve2e
%dir %{_texdir}/texmf-dist/doc/latex/curves
%dir %{_texdir}/texmf-dist/doc/latex/custom-bib
%dir %{_texdir}/texmf-dist/doc/latex/cv
%dir %{_texdir}/texmf-dist/doc/latex/cweb-latex
%dir %{_texdir}/texmf-dist/doc/latex/cweb-latex/contrib
%dir %{_texdir}/texmf-dist/doc/latex/cweb-latex/contrib/cweb-hy
%dir %{_texdir}/texmf-dist/doc/latex/cweb-latex/contrib/wagner
%dir %{_texdir}/texmf-dist/doc/latex/cweb-latex/examples
%dir %{_texdir}/texmf-dist/doc/latex/cweb-latex/examples/compare
%dir %{_texdir}/texmf-dist/doc/latex/cweb-latex/src
%dir %{_texdir}/texmf-dist/doc/latex/cweb-latex/src/style
%dir %{_texdir}/texmf-dist/doc/latex/cweb-latex/src/test
%dir %{_texdir}/texmf-dist/doc/latex/cyrillic
%dir %{_texdir}/texmf-dist/doc/latex/dashrule
%dir %{_texdir}/texmf-dist/doc/latex/dashundergaps
%dir %{_texdir}/texmf-dist/doc/latex/dashundergaps/doc
%dir %{_texdir}/texmf-dist/doc/latex/dashundergaps/doc/pdf
%dir %{_texdir}/texmf-dist/doc/latex/dashundergaps/doc/tex
%dir %{_texdir}/texmf-dist/doc/latex/datatool
%dir %{_texdir}/texmf-dist/doc/latex/dateiliste
%dir %{_texdir}/texmf-dist/doc/latex/datenumber
%dir %{_texdir}/texmf-dist/doc/latex/datetime
%dir %{_texdir}/texmf-dist/doc/latex/dblfloatfix
%dir %{_texdir}/texmf-dist/doc/latex/delimtxt
%dir %{_texdir}/texmf-dist/doc/latex/diagmac2
%dir %{_texdir}/texmf-dist/doc/latex/diagmac2/doc
%dir %{_texdir}/texmf-dist/doc/latex/diagnose
%dir %{_texdir}/texmf-dist/doc/latex/dichokey
%dir %{_texdir}/texmf-dist/doc/latex/digiconfigs
%dir %{_texdir}/texmf-dist/doc/latex/din1505
%dir %{_texdir}/texmf-dist/doc/latex/dinbrief
%dir %{_texdir}/texmf-dist/doc/latex/directory
%dir %{_texdir}/texmf-dist/doc/latex/disser
%dir %{_texdir}/texmf-dist/doc/latex/disser/include
%dir %{_texdir}/texmf-dist/doc/latex/disser/templates
%dir %{_texdir}/texmf-dist/doc/latex/disser/templates/bachelor
%dir %{_texdir}/texmf-dist/doc/latex/disser/templates/bachelor/fig
%dir %{_texdir}/texmf-dist/doc/latex/disser/templates/candidate
%dir %{_texdir}/texmf-dist/doc/latex/disser/templates/candidate/fig
%dir %{_texdir}/texmf-dist/doc/latex/disser/templates/doctor
%dir %{_texdir}/texmf-dist/doc/latex/disser/templates/doctor/fig
%dir %{_texdir}/texmf-dist/doc/latex/disser/templates/master
%dir %{_texdir}/texmf-dist/doc/latex/disser/templates/master/fig
%dir %{_texdir}/texmf-dist/doc/latex/dk-bib
%dir %{_texdir}/texmf-dist/doc/latex/dlfltxb
%dir %{_texdir}/texmf-dist/doc/latex/dnaseq
%dir %{_texdir}/texmf-dist/doc/latex/docmfp
%dir %{_texdir}/texmf-dist/doc/latex/docmute
%dir %{_texdir}/texmf-dist/doc/latex/doi
%dir %{_texdir}/texmf-dist/doc/latex/doipubmed
%dir %{_texdir}/texmf-dist/doc/latex/dot2texi
%dir %{_texdir}/texmf-dist/doc/latex/dot2texi/examples
%dir %{_texdir}/texmf-dist/doc/latex/dotarrow
%dir %{_texdir}/texmf-dist/doc/latex/dotseqn
%dir %{_texdir}/texmf-dist/doc/latex/dottex
%dir %{_texdir}/texmf-dist/doc/latex/dox
%dir %{_texdir}/texmf-dist/doc/latex/dpfloat
%dir %{_texdir}/texmf-dist/doc/latex/dprogress
%dir %{_texdir}/texmf-dist/doc/latex/drac
%dir %{_texdir}/texmf-dist/doc/latex/draftcopy
%dir %{_texdir}/texmf-dist/doc/latex/draftwatermark
%dir %{_texdir}/texmf-dist/doc/latex/dramatist
%dir %{_texdir}/texmf-dist/doc/latex/drs
%dir %{_texdir}/texmf-dist/doc/latex/dtk
%dir %{_texdir}/texmf-dist/doc/latex/dtk/doc
%dir %{_texdir}/texmf-dist/doc/latex/dtk/historical
%dir %{_texdir}/texmf-dist/doc/latex/dtxgallery
%dir %{_texdir}/texmf-dist/doc/latex/dtxtut
%dir %{_texdir}/texmf-dist/doc/latex/duerer-latex
%dir %{_texdir}/texmf-dist/doc/latex/duotenzor
%dir %{_texdir}/texmf-dist/doc/latex/dvdcoll
%dir %{_texdir}/texmf-dist/doc/latex/dyntree
%dir %{_texdir}/texmf-dist/doc/latex/ean13isbn
%dir %{_texdir}/texmf-dist/doc/latex/easy
%dir %{_texdir}/texmf-dist/doc/latex/easy/for-latex2html
%dir %{_texdir}/texmf-dist/doc/latex/easylist
%dir %{_texdir}/texmf-dist/doc/latex/ebezier
%dir %{_texdir}/texmf-dist/doc/latex/ebong
%dir %{_texdir}/texmf-dist/doc/latex/ebsthesis
%dir %{_texdir}/texmf-dist/doc/latex/ecclesiastic
%dir %{_texdir}/texmf-dist/doc/latex/ecltree
%dir %{_texdir}/texmf-dist/doc/latex/ecv
%dir %{_texdir}/texmf-dist/doc/latex/ecv/template
%dir %{_texdir}/texmf-dist/doc/latex/ed
%dir %{_texdir}/texmf-dist/doc/latex/edmac
%dir %{_texdir}/texmf-dist/doc/latex/edmargin
%dir %{_texdir}/texmf-dist/doc/latex/ednotes
%dir %{_texdir}/texmf-dist/doc/latex/eemeir
%dir %{_texdir}/texmf-dist/doc/latex/eepic
%dir %{_texdir}/texmf-dist/doc/latex/eepic/fig2eepic
%dir %{_texdir}/texmf-dist/doc/latex/egameps
%dir %{_texdir}/texmf-dist/doc/latex/egplot
%dir %{_texdir}/texmf-dist/doc/latex/eiad-ltx
%dir %{_texdir}/texmf-dist/doc/latex/elbioimp
%dir %{_texdir}/texmf-dist/doc/latex/ellipsis
%dir %{_texdir}/texmf-dist/doc/latex/elmath
%dir %{_texdir}/texmf-dist/doc/latex/elpres
%dir %{_texdir}/texmf-dist/doc/latex/elsarticle
%dir %{_texdir}/texmf-dist/doc/latex/elsevier
%dir %{_texdir}/texmf-dist/doc/latex/eltex
%dir %{_texdir}/texmf-dist/doc/latex/em
%dir %{_texdir}/texmf-dist/doc/latex/emp
%dir %{_texdir}/texmf-dist/doc/latex/emptypage
%dir %{_texdir}/texmf-dist/doc/latex/emulateapj
%dir %{_texdir}/texmf-dist/doc/latex/endfloat
%dir %{_texdir}/texmf-dist/doc/latex/endheads
%dir %{_texdir}/texmf-dist/doc/latex/endnotes
%dir %{_texdir}/texmf-dist/doc/latex/engpron
%dir %{_texdir}/texmf-dist/doc/latex/engrec
%dir %{_texdir}/texmf-dist/doc/latex/engtlc
%dir %{_texdir}/texmf-dist/doc/latex/enumitem
%dir %{_texdir}/texmf-dist/doc/latex/envbig
%dir %{_texdir}/texmf-dist/doc/latex/environ
%dir %{_texdir}/texmf-dist/doc/latex/envlab
%dir %{_texdir}/texmf-dist/doc/latex/epigraph
%dir %{_texdir}/texmf-dist/doc/latex/epiolmec
%dir %{_texdir}/texmf-dist/doc/latex/epsdice
%dir %{_texdir}/texmf-dist/doc/latex/epslatex-fr
%dir %{_texdir}/texmf-dist/doc/latex/epspdfconversion
%dir %{_texdir}/texmf-dist/doc/latex/epspdfconversion/example
%dir %{_texdir}/texmf-dist/doc/latex/epstopdf
%dir %{_texdir}/texmf-dist/doc/latex/eqell
%dir %{_texdir}/texmf-dist/doc/latex/eqlist
%dir %{_texdir}/texmf-dist/doc/latex/eqparbox
%dir %{_texdir}/texmf-dist/doc/latex/erdc
%dir %{_texdir}/texmf-dist/doc/latex/errata
%dir %{_texdir}/texmf-dist/doc/latex/ESIEEcv
%dir %{_texdir}/texmf-dist/doc/latex/esint
%dir %{_texdir}/texmf-dist/doc/latex/esk
%dir %{_texdir}/texmf-dist/doc/latex/eskd
%dir %{_texdir}/texmf-dist/doc/latex/eskdx
%dir %{_texdir}/texmf-dist/doc/latex/eskdx/manual
%dir %{_texdir}/texmf-dist/doc/latex/eskdx/source
%dir %{_texdir}/texmf-dist/doc/latex/eskdx/test
%dir %{_texdir}/texmf-dist/doc/latex/eso-pic
%dir %{_texdir}/texmf-dist/doc/latex/estcpmm
%dir %{_texdir}/texmf-dist/doc/latex/esvect
%dir %{_texdir}/texmf-dist/doc/latex/etaremune
%dir %{_texdir}/texmf-dist/doc/latex/etex-pkg
%dir %{_texdir}/texmf-dist/doc/latex/etextools
%dir %{_texdir}/texmf-dist/doc/latex/ethiop
%dir %{_texdir}/texmf-dist/doc/latex/ethiop-t1
%dir %{_texdir}/texmf-dist/doc/latex/etoolbox
%dir %{_texdir}/texmf-dist/doc/latex/euenc
%dir %{_texdir}/texmf-dist/doc/latex/eukdate
%dir %{_texdir}/texmf-dist/doc/latex/euler
%dir %{_texdir}/texmf-dist/doc/latex/eulervm
%dir %{_texdir}/texmf-dist/doc/latex/euproposal
%dir %{_texdir}/texmf-dist/doc/latex/euro
%dir %{_texdir}/texmf-dist/doc/latex/europecv
%dir %{_texdir}/texmf-dist/doc/latex/europecv/examples
%dir %{_texdir}/texmf-dist/doc/latex/europecv/templates
%dir %{_texdir}/texmf-dist/doc/latex/eurosans
%dir %{_texdir}/texmf-dist/doc/latex/everypage
%dir %{_texdir}/texmf-dist/doc/latex/exam
%dir %{_texdir}/texmf-dist/doc/latex/examdesign
%dir %{_texdir}/texmf-dist/doc/latex/examplep
%dir %{_texdir}/texmf-dist/doc/latex/excludeonly
%dir %{_texdir}/texmf-dist/doc/latex/exercise
%dir %{_texdir}/texmf-dist/doc/latex/expdlist
%dir %{_texdir}/texmf-dist/doc/latex/expl3
%dir %{_texdir}/texmf-dist/doc/latex/export
%dir %{_texdir}/texmf-dist/doc/latex/exp-testopt
%dir %{_texdir}/texmf-dist/doc/latex/extarrows
%dir %{_texdir}/texmf-dist/doc/latex/extpfeil
%dir %{_texdir}/texmf-dist/doc/latex/extract
%dir %{_texdir}/texmf-dist/doc/latex/extsizes
%dir %{_texdir}/texmf-dist/doc/latex/facsimile
%dir %{_texdir}/texmf-dist/doc/latex/faktor
%dir %{_texdir}/texmf-dist/doc/latex/fancybox
%dir %{_texdir}/texmf-dist/doc/latex/fancyhdr
%dir %{_texdir}/texmf-dist/doc/latex/fancyhdr-it
%dir %{_texdir}/texmf-dist/doc/latex/fancynum
%dir %{_texdir}/texmf-dist/doc/latex/fancypar
%dir %{_texdir}/texmf-dist/doc/latex/fancyref
%dir %{_texdir}/texmf-dist/doc/latex/fancytooltips
%dir %{_texdir}/texmf-dist/doc/latex/fancytooltips/examples
%dir %{_texdir}/texmf-dist/doc/latex/fancytooltips/examples/fancy-preview
%dir %{_texdir}/texmf-dist/doc/latex/fancytooltips/examples/tex4ht
%dir %{_texdir}/texmf-dist/doc/latex/fancytooltips/examples/tex4ht/images
%dir %{_texdir}/texmf-dist/doc/latex/fancyvrb
%dir %{_texdir}/texmf-dist/doc/latex/feynmf
%dir %{_texdir}/texmf-dist/doc/latex/figbib
%dir %{_texdir}/texmf-dist/doc/latex/figsize
%dir %{_texdir}/texmf-dist/doc/latex/filecontents
%dir %{_texdir}/texmf-dist/doc/latex/filehook
%dir %{_texdir}/texmf-dist/doc/latex/fink
%dir %{_texdir}/texmf-dist/doc/latex/first-latex-doc
%dir %{_texdir}/texmf-dist/doc/latex/fix2col
%dir %{_texdir}/texmf-dist/doc/latex/fixfoot
%dir %{_texdir}/texmf-dist/doc/latex/fixme
%dir %{_texdir}/texmf-dist/doc/latex/flabels
%dir %{_texdir}/texmf-dist/doc/latex/flacards
%dir %{_texdir}/texmf-dist/doc/latex/flagderiv
%dir %{_texdir}/texmf-dist/doc/latex/flashcards
%dir %{_texdir}/texmf-dist/doc/latex/flashmovie
%dir %{_texdir}/texmf-dist/doc/latex/flashmovie/flv-player-license
%dir %{_texdir}/texmf-dist/doc/latex/flippdf
%dir %{_texdir}/texmf-dist/doc/latex/float
%dir %{_texdir}/texmf-dist/doc/latex/floatrow
%dir %{_texdir}/texmf-dist/doc/latex/flowfram
%dir %{_texdir}/texmf-dist/doc/latex/flowfram/samples
%dir %{_texdir}/texmf-dist/doc/latex/fltpage
%dir %{_texdir}/texmf-dist/doc/latex/fmp
%dir %{_texdir}/texmf-dist/doc/latex/fmtcount
%dir %{_texdir}/texmf-dist/doc/latex/fn2end
%dir %{_texdir}/texmf-dist/doc/latex/fnbreak
%dir %{_texdir}/texmf-dist/doc/latex/fncychap
%dir %{_texdir}/texmf-dist/doc/latex/fncylab
%dir %{_texdir}/texmf-dist/doc/latex/fnpara
%dir %{_texdir}/texmf-dist/doc/latex/foekfont
%dir %{_texdir}/texmf-dist/doc/latex/fontspec
%dir %{_texdir}/texmf-dist/doc/latex/fonttable
%dir %{_texdir}/texmf-dist/doc/latex/footbib
%dir %{_texdir}/texmf-dist/doc/latex/footmisc
%dir %{_texdir}/texmf-dist/doc/latex/footnpag
%dir %{_texdir}/texmf-dist/doc/latex/footnpag/test
%dir %{_texdir}/texmf-dist/doc/latex/forarray
%dir %{_texdir}/texmf-dist/doc/latex/forloop
%dir %{_texdir}/texmf-dist/doc/latex/formular
%dir %{_texdir}/texmf-dist/doc/latex/fouridx
%dir %{_texdir}/texmf-dist/doc/latex/fp
%dir %{_texdir}/texmf-dist/doc/latex/fragments
%dir %{_texdir}/texmf-dist/doc/latex/framed
%dir %{_texdir}/texmf-dist/doc/latex/frankenstein
%dir %{_texdir}/texmf-dist/doc/latex/frankenstein/unsupported
%dir %{_texdir}/texmf-dist/doc/latex/frenchle
%dir %{_texdir}/texmf-dist/doc/latex/fribrief
%dir %{_texdir}/texmf-dist/doc/latex/frletter
%dir %{_texdir}/texmf-dist/doc/latex/frontespizio
%dir %{_texdir}/texmf-dist/doc/latex/ftcap
%dir %{_texdir}/texmf-dist/doc/latex/ftnxtra
%dir %{_texdir}/texmf-dist/doc/latex/fullblck
%dir %{_texdir}/texmf-dist/doc/latex/functan
%dir %{_texdir}/texmf-dist/doc/latex/fundus
%dir %{_texdir}/texmf-dist/doc/latex/fundus/doc
%dir %{_texdir}/texmf-dist/doc/latex/gaceta
%dir %{_texdir}/texmf-dist/doc/latex/galois
%dir %{_texdir}/texmf-dist/doc/latex/gastex
%dir %{_texdir}/texmf-dist/doc/latex/gatech-thesis
%dir %{_texdir}/texmf-dist/doc/latex/gatech-thesis/julesverne
%dir %{_texdir}/texmf-dist/doc/latex/gatech-thesis/julesverne/basic
%dir %{_texdir}/texmf-dist/doc/latex/gatech-thesis/julesverne/bellswhistles
%dir %{_texdir}/texmf-dist/doc/latex/gatech-thesis/julesverne/bellswhistles/code
%dir %{_texdir}/texmf-dist/doc/latex/gatech-thesis/julesverne/bellswhistles/fig
%dir %{_texdir}/texmf-dist/doc/latex/gauss
%dir %{_texdir}/texmf-dist/doc/latex/gb4e
%dir %{_texdir}/texmf-dist/doc/latex/g-brief
%dir %{_texdir}/texmf-dist/doc/latex/gcard
%dir %{_texdir}/texmf-dist/doc/latex/gchords
%dir %{_texdir}/texmf-dist/doc/latex/gcite
%dir %{_texdir}/texmf-dist/doc/latex/gene-logic
%dir %{_texdir}/texmf-dist/doc/latex/genmpage
%dir %{_texdir}/texmf-dist/doc/latex/geometry
%dir %{_texdir}/texmf-dist/doc/latex/germkorr
%dir %{_texdir}/texmf-dist/doc/latex/getfiledate
%dir %{_texdir}/texmf-dist/doc/latex/ginpenc
%dir %{_texdir}/texmf-dist/doc/latex/gloss
%dir %{_texdir}/texmf-dist/doc/latex/glossaries
%dir %{_texdir}/texmf-dist/doc/latex/glossaries/samples
%dir %{_texdir}/texmf-dist/doc/latex/gmdoc
%dir %{_texdir}/texmf-dist/doc/latex/gmdoc/basedrivers
%dir %{_texdir}/texmf-dist/doc/latex/gmdoc-enhance
%dir %{_texdir}/texmf-dist/doc/latex/gmeometric
%dir %{_texdir}/texmf-dist/doc/latex/gmiflink
%dir %{_texdir}/texmf-dist/doc/latex/gmutils
%dir %{_texdir}/texmf-dist/doc/latex/gmverb
%dir %{_texdir}/texmf-dist/doc/latex/gmverse
%dir %{_texdir}/texmf-dist/doc/latex/gnuplottex
%dir %{_texdir}/texmf-dist/doc/latex/graphics
%dir %{_texdir}/texmf-dist/doc/latex/graphicx-psmin
%dir %{_texdir}/texmf-dist/doc/latex/greekdates
%dir %{_texdir}/texmf-dist/doc/latex/greek-inputenc
%dir %{_texdir}/texmf-dist/doc/latex/greektex
%dir %{_texdir}/texmf-dist/doc/latex/grfpaste
%dir %{_texdir}/texmf-dist/doc/latex/grfpaste/doc
%dir %{_texdir}/texmf-dist/doc/latex/grid
%dir %{_texdir}/texmf-dist/doc/latex/gridset
%dir %{_texdir}/texmf-dist/doc/latex/grverb
%dir %{_texdir}/texmf-dist/doc/latex/gu
%dir %{_texdir}/texmf-dist/doc/latex/guide-to-latex
%dir %{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises
%dir %{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap10
%dir %{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap11
%dir %{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap15
%dir %{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap2
%dir %{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap3
%dir %{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap4
%dir %{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap5
%dir %{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap6
%dir %{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap7
%dir %{_texdir}/texmf-dist/doc/latex/guide-to-latex/exercises/chap8
%dir %{_texdir}/texmf-dist/doc/latex/guitar
%dir %{_texdir}/texmf-dist/doc/latex/guitlogo
%dir %{_texdir}/texmf-dist/doc/latex/hanging
%dir %{_texdir}/texmf-dist/doc/latex/HA-prosper
%dir %{_texdir}/texmf-dist/doc/latex/har2nat
%dir %{_texdir}/texmf-dist/doc/latex/harmony
%dir %{_texdir}/texmf-dist/doc/latex/harpoon
%dir %{_texdir}/texmf-dist/doc/latex/harvard
%dir %{_texdir}/texmf-dist/doc/latex/hc
%dir %{_texdir}/texmf-dist/doc/latex/hep
%dir %{_texdir}/texmf-dist/doc/latex/hepnames
%dir %{_texdir}/texmf-dist/doc/latex/hepparticles
%dir %{_texdir}/texmf-dist/doc/latex/hepthesis
%dir %{_texdir}/texmf-dist/doc/latex/hepthesis/example
%dir %{_texdir}/texmf-dist/doc/latex/hepunits
%dir %{_texdir}/texmf-dist/doc/latex/here
%dir %{_texdir}/texmf-dist/doc/latex/hexgame
%dir %{_texdir}/texmf-dist/doc/latex/hhtensor
%dir %{_texdir}/texmf-dist/doc/latex/histogr
%dir %{_texdir}/texmf-dist/doc/latex/historische-zeitschrift
%dir %{_texdir}/texmf-dist/doc/latex/hitec
%dir %{_texdir}/texmf-dist/doc/latex/hpsdiss
%dir %{_texdir}/texmf-dist/doc/latex/hrlatex
%dir %{_texdir}/texmf-dist/doc/latex/hvfloat
%dir %{_texdir}/texmf-dist/doc/latex/hvindex
%dir %{_texdir}/texmf-dist/doc/latex/hypdvips
%dir %{_texdir}/texmf-dist/doc/latex/hypdvips/images
%dir %{_texdir}/texmf-dist/doc/latex/hyper
%dir %{_texdir}/texmf-dist/doc/latex/hyper/contrib
%dir %{_texdir}/texmf-dist/doc/latex/hypernat
%dir %{_texdir}/texmf-dist/doc/latex/hyperref
%dir %{_texdir}/texmf-dist/doc/latex/hyperref-docsrc
%dir %{_texdir}/texmf-dist/doc/latex/hyper/scontrib
%dir %{_texdir}/texmf-dist/doc/latex/hyperxmp
%dir %{_texdir}/texmf-dist/doc/latex/hyphenat
%dir %{_texdir}/texmf-dist/doc/latex/ibycus-babel
%dir %{_texdir}/texmf-dist/doc/latex/icsv
%dir %{_texdir}/texmf-dist/doc/latex/idxlayout
%dir %{_texdir}/texmf-dist/doc/latex/IEEEconf
%dir %{_texdir}/texmf-dist/doc/latex/ieeepes
%dir %{_texdir}/texmf-dist/doc/latex/IEEEtran
%dir %{_texdir}/texmf-dist/doc/latex/ifmslide
%dir %{_texdir}/texmf-dist/doc/latex/ifmtarg
%dir %{_texdir}/texmf-dist/doc/latex/ifplatform
%dir %{_texdir}/texmf-dist/doc/latex/ijmart
%dir %{_texdir}/texmf-dist/doc/latex/imac
%dir %{_texdir}/texmf-dist/doc/latex/image-gallery
%dir %{_texdir}/texmf-dist/doc/latex/imakeidx
%dir %{_texdir}/texmf-dist/doc/latex/import
%dir %{_texdir}/texmf-dist/doc/latex/imtekda
%dir %{_texdir}/texmf-dist/doc/latex/imtekda/figures
%dir %{_texdir}/texmf-dist/doc/latex/index
%dir %{_texdir}/texmf-dist/doc/latex/inlinebib
%dir %{_texdir}/texmf-dist/doc/latex/inlinedef
%dir %{_texdir}/texmf-dist/doc/latex/interactiveworkbook
%dir %{_texdir}/texmf-dist/doc/latex/interactiveworkbook/documentation
%dir %{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles
%dir %{_texdir}/texmf-dist/doc/latex/interactiveworkbook/samplefiles
%dir %{_texdir}/texmf-dist/doc/latex/intro-scientific
%dir %{_texdir}/texmf-dist/doc/latex/inversepath
%dir %{_texdir}/texmf-dist/doc/latex/ionumbers
%dir %{_texdir}/texmf-dist/doc/latex/iso
%dir %{_texdir}/texmf-dist/doc/latex/iso10303
%dir %{_texdir}/texmf-dist/doc/latex/isodate
%dir %{_texdir}/texmf-dist/doc/latex/isodoc
%dir %{_texdir}/texmf-dist/doc/latex/isomath
%dir %{_texdir}/texmf-dist/doc/latex/isonums
%dir %{_texdir}/texmf-dist/doc/latex/isorot
%dir %{_texdir}/texmf-dist/doc/latex/itnumpar
%dir %{_texdir}/texmf-dist/doc/latex/jeopardy
%dir %{_texdir}/texmf-dist/doc/latex/jeopardy/example
%dir %{_texdir}/texmf-dist/doc/latex/jknapltx
%dir %{_texdir}/texmf-dist/doc/latex/jmlr
%dir %{_texdir}/texmf-dist/doc/latex/jmlr/sample-books
%dir %{_texdir}/texmf-dist/doc/latex/jmlr/sample-books/paper1
%dir %{_texdir}/texmf-dist/doc/latex/jmlr/sample-books/paper2
%dir %{_texdir}/texmf-dist/doc/latex/jmlr/sample-books/paper3
%dir %{_texdir}/texmf-dist/doc/latex/jmlr/sample-books/paper4
%dir %{_texdir}/texmf-dist/doc/latex/jmlr/sample-papers
%dir %{_texdir}/texmf-dist/doc/latex/jmlr/sample-papers/images
%dir %{_texdir}/texmf-dist/doc/latex/jneurosci
%dir %{_texdir}/texmf-dist/doc/latex/jpsj
%dir %{_texdir}/texmf-dist/doc/latex/jura
%dir %{_texdir}/texmf-dist/doc/latex/juraabbrev
%dir %{_texdir}/texmf-dist/doc/latex/jurabib
%dir %{_texdir}/texmf-dist/doc/latex/jurabib/docs
%dir %{_texdir}/texmf-dist/doc/latex/jurabib/docs/english
%dir %{_texdir}/texmf-dist/doc/latex/jurabib/docs/german
%dir %{_texdir}/texmf-dist/doc/latex/juramisc
%dir %{_texdir}/texmf-dist/doc/latex/juramisc/doc
%dir %{_texdir}/texmf-dist/doc/latex/juramisc/doc/jbook
%dir %{_texdir}/texmf-dist/doc/latex/jurarsp
%dir %{_texdir}/texmf-dist/doc/latex/karnaugh
%dir %{_texdir}/texmf-dist/doc/latex/kerkis
%dir %{_texdir}/texmf-dist/doc/latex/kerntest
%dir %{_texdir}/texmf-dist/doc/latex/keycommand
%dir %{_texdir}/texmf-dist/doc/latex/keystroke
%dir %{_texdir}/texmf-dist/doc/latex/kluwer
%dir %{_texdir}/texmf-dist/doc/latex/knittingpattern
%dir %{_texdir}/texmf-dist/doc/latex/koma-script
%dir %{_texdir}/texmf-dist/doc/latex/kopka
%dir %{_texdir}/texmf-dist/doc/latex/kopka/uebungen
%dir %{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel2
%dir %{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel3
%dir %{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel4
%dir %{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel5
%dir %{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel6
%dir %{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel7
%dir %{_texdir}/texmf-dist/doc/latex/kopka/uebungen/kapitel8
%dir %{_texdir}/texmf-dist/doc/latex/l2picfaq
%dir %{_texdir}/texmf-dist/doc/latex/l2tabu
%dir %{_texdir}/texmf-dist/doc/latex/l2tabu-english
%dir %{_texdir}/texmf-dist/doc/latex/l2tabu-french
%dir %{_texdir}/texmf-dist/doc/latex/l2tabu-it
%dir %{_texdir}/texmf-dist/doc/latex/l2tabu-spanish
%dir %{_texdir}/texmf-dist/doc/latex/labbook
%dir %{_texdir}/texmf-dist/doc/latex/labelcas
%dir %{_texdir}/texmf-dist/doc/latex/labels
%dir %{_texdir}/texmf-dist/doc/latex/labels/test
%dir %{_texdir}/texmf-dist/doc/latex/lastpage
%dir %{_texdir}/texmf-dist/doc/latex/latex2e-help-texinfo
%dir %{_texdir}/texmf-dist/doc/latex/latexcheat
%dir %{_texdir}/texmf-dist/doc/latex/latexcheat-esmx
%dir %{_texdir}/texmf-dist/doc/latex/latexcheat-ptbr
%dir %{_texdir}/texmf-dist/doc/latex/latex-course
%dir %{_texdir}/texmf-dist/doc/latex/latex-course/Graphics
%dir %{_texdir}/texmf-dist/doc/latex/latexdiff
%dir %{_texdir}/texmf-dist/doc/latex/latexdiff/contrib
%dir %{_texdir}/texmf-dist/doc/latex/latexdiff/example
%dir %{_texdir}/texmf-dist/doc/latex/latex-doc-ptr
%dir %{_texdir}/texmf-dist/doc/latex/latex-graphics-companion
%dir %{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/inputs
%dir %{_texdir}/texmf-dist/doc/latex/latex-referenz
%dir %{_texdir}/texmf-dist/doc/latex/latex-tabellen
%dir %{_texdir}/texmf-dist/doc/latex/latex-tipps-und-tricks
%dir %{_texdir}/texmf-dist/doc/latex/latex-veryshortguide
%dir %{_texdir}/texmf-dist/doc/latex/latex-web-companion
%dir %{_texdir}/texmf-dist/doc/latex/latex-web-companion/apa
%dir %{_texdir}/texmf-dist/doc/latex/latex-web-companion/apb
%dir %{_texdir}/texmf-dist/doc/latex/latex-web-companion/apc
%dir %{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis
%dir %{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex30
%dir %{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex31
%dir %{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/ex32
%dir %{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/l2hexa
%dir %{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleAMS
%dir %{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMath
%dir %{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathImages
%dir %{_texdir}/texmf-dist/doc/latex/latex-web-companion/ch3bis/sampleMathThumb
%dir %{_texdir}/texmf-dist/doc/latex/latex-web-companion/intro
%dir %{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2html
%dir %{_texdir}/texmf-dist/doc/latex/latex-web-companion/latex2xml
%dir %{_texdir}/texmf-dist/doc/latex/latex-web-companion/xml
%dir %{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle
%dir %{_texdir}/texmf-dist/doc/latex/latex-web-companion/xmlstyle/SGMLS
%dir %{_texdir}/texmf-dist/doc/latex/layaureo
%dir %{_texdir}/texmf-dist/doc/latex/layouts
%dir %{_texdir}/texmf-dist/doc/latex/lazylist
%dir %{_texdir}/texmf-dist/doc/latex/lcd
%dir %{_texdir}/texmf-dist/doc/latex/lcg
%dir %{_texdir}/texmf-dist/doc/latex/lcyw
%dir %{_texdir}/texmf-dist/doc/latex/leading
%dir %{_texdir}/texmf-dist/doc/latex/leaflet
%dir %{_texdir}/texmf-dist/doc/latex/ledmac
%dir %{_texdir}/texmf-dist/doc/latex/ledmac/examples
%dir %{_texdir}/texmf-dist/doc/latex/leftidx
%dir %{_texdir}/texmf-dist/doc/latex/lettre
%dir %{_texdir}/texmf-dist/doc/latex/lettrine
%dir %{_texdir}/texmf-dist/doc/latex/lewis
%dir %{_texdir}/texmf-dist/doc/latex/lexikon
%dir %{_texdir}/texmf-dist/doc/latex/lhelp
%dir %{_texdir}/texmf-dist/doc/latex/linegoal
%dir %{_texdir}/texmf-dist/doc/latex/lineno
%dir %{_texdir}/texmf-dist/doc/latex/linguex
%dir %{_texdir}/texmf-dist/doc/latex/lipsum
%dir %{_texdir}/texmf-dist/doc/latex/listbib
%dir %{_texdir}/texmf-dist/doc/latex/listing
%dir %{_texdir}/texmf-dist/doc/latex/listings
%dir %{_texdir}/texmf-dist/doc/latex/listings-ext
%dir %{_texdir}/texmf-dist/doc/latex/listliketab
%dir %{_texdir}/texmf-dist/doc/latex/listofsymbols
%dir %{_texdir}/texmf-dist/doc/latex/lithuanian
%dir %{_texdir}/texmf-dist/doc/latex/liturg
%dir %{_texdir}/texmf-dist/doc/latex/lkproof
%dir %{_texdir}/texmf-dist/doc/latex/locality
%dir %{_texdir}/texmf-dist/doc/latex/localloc
%dir %{_texdir}/texmf-dist/doc/latex/logical-markup-utils
%dir %{_texdir}/texmf-dist/doc/latex/logpap
%dir %{_texdir}/texmf-dist/doc/latex/lps
%dir %{_texdir}/texmf-dist/doc/latex/lsc
%dir %{_texdir}/texmf-dist/doc/latex/lshort-bulgarian
%dir %{_texdir}/texmf-dist/doc/latex/lshort-bulgarian/src
%dir %{_texdir}/texmf-dist/doc/latex/lshort-chinese
%dir %{_texdir}/texmf-dist/doc/latex/lshort-chinese/src
%dir %{_texdir}/texmf-dist/doc/latex/lshort-dutch
%dir %{_texdir}/texmf-dist/doc/latex/lshort-english
%dir %{_texdir}/texmf-dist/doc/latex/lshort-finnish
%dir %{_texdir}/texmf-dist/doc/latex/lshort-finnish/src
%dir %{_texdir}/texmf-dist/doc/latex/lshort-french
%dir %{_texdir}/texmf-dist/doc/latex/lshort-german
%dir %{_texdir}/texmf-dist/doc/latex/lshort-italian
%dir %{_texdir}/texmf-dist/doc/latex/lshort-japanese
%dir %{_texdir}/texmf-dist/doc/latex/lshort-korean
%dir %{_texdir}/texmf-dist/doc/latex/lshort-mongol
%dir %{_texdir}/texmf-dist/doc/latex/lshort-mongol/src
%dir %{_texdir}/texmf-dist/doc/latex/lshort-persian
%dir %{_texdir}/texmf-dist/doc/latex/lshort-polish
%dir %{_texdir}/texmf-dist/doc/latex/lshort-portuguese
%dir %{_texdir}/texmf-dist/doc/latex/lshort-russian
%dir %{_texdir}/texmf-dist/doc/latex/lshort-slovak
%dir %{_texdir}/texmf-dist/doc/latex/lshort-slovenian
%dir %{_texdir}/texmf-dist/doc/latex/lshort-slovenian/src
%dir %{_texdir}/texmf-dist/doc/latex/lshort-spanish
%dir %{_texdir}/texmf-dist/doc/latex/lshort-spanish/fuente
%dir %{_texdir}/texmf-dist/doc/latex/lshort-spanish/fuente/src
%dir %{_texdir}/texmf-dist/doc/latex/lshort-thai
%dir %{_texdir}/texmf-dist/doc/latex/lshort-turkish
%dir %{_texdir}/texmf-dist/doc/latex/lshort-ukr
%dir %{_texdir}/texmf-dist/doc/latex/lshort-vietnamese
%dir %{_texdir}/texmf-dist/doc/latex/lshort-vietnamese/src
%dir %{_texdir}/texmf-dist/doc/latex/ltabptch
%dir %{_texdir}/texmf-dist/doc/latex/ltxdockit
%dir %{_texdir}/texmf-dist/doc/latex/ltxindex
%dir %{_texdir}/texmf-dist/doc/latex/ltxnew
%dir %{_texdir}/texmf-dist/doc/latex/macqassign
%dir %{_texdir}/texmf-dist/doc/latex/mafr
%dir %{_texdir}/texmf-dist/doc/latex/magaz
%dir %{_texdir}/texmf-dist/doc/latex/magyar
%dir %{_texdir}/texmf-dist/doc/latex/mailing
%dir %{_texdir}/texmf-dist/doc/latex/mailmerge
%dir %{_texdir}/texmf-dist/doc/latex/makebarcode
%dir %{_texdir}/texmf-dist/doc/latex/makebox
%dir %{_texdir}/texmf-dist/doc/latex/makecell
%dir %{_texdir}/texmf-dist/doc/latex/makecmds
%dir %{_texdir}/texmf-dist/doc/latex/makedtx
%dir %{_texdir}/texmf-dist/doc/latex/makeglos
%dir %{_texdir}/texmf-dist/doc/latex/makeplot
%dir %{_texdir}/texmf-dist/doc/latex/manuscript
%dir %{_texdir}/texmf-dist/doc/latex/margbib
%dir %{_texdir}/texmf-dist/doc/latex/marginnote
%dir %{_texdir}/texmf-dist/doc/latex/mathcomp
%dir %{_texdir}/texmf-dist/doc/latex/mathdesign
%dir %{_texdir}/texmf-dist/doc/latex/mathdesign/mdbch
%dir %{_texdir}/texmf-dist/doc/latex/mathdesign/mdput
%dir %{_texdir}/texmf-dist/doc/latex/mathdesign/mdugm
%dir %{_texdir}/texmf-dist/doc/latex/mathexam
%dir %{_texdir}/texmf-dist/doc/latex/mathmode
%dir %{_texdir}/texmf-dist/doc/latex/mathmode/images
%dir %{_texdir}/texmf-dist/doc/latex/mathpazo
%dir %{_texdir}/texmf-dist/doc/latex/mathspic
%dir %{_texdir}/texmf-dist/doc/latex/mattens
%dir %{_texdir}/texmf-dist/doc/latex/maybemath
%dir %{_texdir}/texmf-dist/doc/latex/mcaption
%dir %{_texdir}/texmf-dist/doc/latex/mceinleger
%dir %{_texdir}/texmf-dist/doc/latex/mcite
%dir %{_texdir}/texmf-dist/doc/latex/mciteplus
%dir %{_texdir}/texmf-dist/doc/latex/mdframed
%dir %{_texdir}/texmf-dist/doc/latex/mdwtools
%dir %{_texdir}/texmf-dist/doc/latex/memexsupp
%dir %{_texdir}/texmf-dist/doc/latex/memoir
%dir %{_texdir}/texmf-dist/doc/latex/MemoirChapStyles
%dir %{_texdir}/texmf-dist/doc/latex/mentis
%dir %{_texdir}/texmf-dist/doc/latex/menu
%dir %{_texdir}/texmf-dist/doc/latex/metalogo
%dir %{_texdir}/texmf-dist/doc/latex/metaplot
%dir %{_texdir}/texmf-dist/doc/latex/metaplot/examples
%dir %{_texdir}/texmf-dist/doc/latex/method
%dir %{_texdir}/texmf-dist/doc/latex/metre
%dir %{_texdir}/texmf-dist/doc/latex/mflogo
%dir %{_texdir}/texmf-dist/doc/latex/mfnfss
%dir %{_texdir}/texmf-dist/doc/latex/mfpic4ode
%dir %{_texdir}/texmf-dist/doc/latex/mfpic4ode/demo
%dir %{_texdir}/texmf-dist/doc/latex/mftinc
%dir %{_texdir}/texmf-dist/doc/latex/mh
%dir %{_texdir}/texmf-dist/doc/latex/mhchem
%dir %{_texdir}/texmf-dist/doc/latex/mhequ
%dir %{_texdir}/texmf-dist/doc/latex/microtype
%dir %{_texdir}/texmf-dist/doc/latex/midpage
%dir %{_texdir}/texmf-dist/doc/latex/miller
%dir %{_texdir}/texmf-dist/doc/latex/minibox
%dir %{_texdir}/texmf-dist/doc/latex/minipage-marginpar
%dir %{_texdir}/texmf-dist/doc/latex/miniplot
%dir %{_texdir}/texmf-dist/doc/latex/minitoc
%dir %{_texdir}/texmf-dist/doc/latex/minted
%dir %{_texdir}/texmf-dist/doc/latex/minutes
%dir %{_texdir}/texmf-dist/doc/latex/mla-paper
%dir %{_texdir}/texmf-dist/doc/latex/mlist
%dir %{_texdir}/texmf-dist/doc/latex/mltex
%dir %{_texdir}/texmf-dist/doc/latex/mmap
%dir %{_texdir}/texmf-dist/doc/latex/mnsymbol
%dir %{_texdir}/texmf-dist/doc/latex/moderncv
%dir %{_texdir}/texmf-dist/doc/latex/moderncv/examples
%dir %{_texdir}/texmf-dist/doc/latex/modref
%dir %{_texdir}/texmf-dist/doc/latex/modroman
%dir %{_texdir}/texmf-dist/doc/latex/mongolian-babel
%dir %{_texdir}/texmf-dist/doc/latex/montex
%dir %{_texdir}/texmf-dist/doc/latex/montex/mfinput
%dir %{_texdir}/texmf-dist/doc/latex/montex/mfinput/bithe
%dir %{_texdir}/texmf-dist/doc/latex/moresize
%dir %{_texdir}/texmf-dist/doc/latex/moreverb
%dir %{_texdir}/texmf-dist/doc/latex/movie15
%dir %{_texdir}/texmf-dist/doc/latex/mparhack
%dir %{_texdir}/texmf-dist/doc/latex/ms
%dir %{_texdir}/texmf-dist/doc/latex/msc
%dir %{_texdir}/texmf-dist/doc/latex/msg
%dir %{_texdir}/texmf-dist/doc/latex/mslapa
%dir %{_texdir}/texmf-dist/doc/latex/mtgreek
%dir %{_texdir}/texmf-dist/doc/latex/muench
%dir %{_texdir}/texmf-dist/doc/latex/muench/hrefhide
%dir %{_texdir}/texmf-dist/doc/latex/multibbl
%dir %{_texdir}/texmf-dist/doc/latex/multibib
%dir %{_texdir}/texmf-dist/doc/latex/multicap
%dir %{_texdir}/texmf-dist/doc/latex/multiobjective
%dir %{_texdir}/texmf-dist/doc/latex/multirow
%dir %{_texdir}/texmf-dist/doc/latex/munich
%dir %{_texdir}/texmf-dist/doc/latex/musixlyr
%dir %{_texdir}/texmf-dist/doc/latex/muthesis
%dir %{_texdir}/texmf-dist/doc/latex/mwcls
%dir %{_texdir}/texmf-dist/doc/latex/mylatexformat
%dir %{_texdir}/texmf-dist/doc/latex/nag
%dir %{_texdir}/texmf-dist/doc/latex/namespc
%dir %{_texdir}/texmf-dist/doc/latex/natbib
%dir %{_texdir}/texmf-dist/doc/latex/nath
%dir %{_texdir}/texmf-dist/doc/latex/ncclatex
%dir %{_texdir}/texmf-dist/doc/latex/ncctools
%dir %{_texdir}/texmf-dist/doc/latex/nddiss
%dir %{_texdir}/texmf-dist/doc/latex/nddiss/example-v1.3
%dir %{_texdir}/texmf-dist/doc/latex/needspace
%dir %{_texdir}/texmf-dist/doc/latex/newcommand
%dir %{_texdir}/texmf-dist/doc/latex/newfile
%dir %{_texdir}/texmf-dist/doc/latex/newlfm
%dir %{_texdir}/texmf-dist/doc/latex/newspaper
%dir %{_texdir}/texmf-dist/doc/latex/newvbtm
%dir %{_texdir}/texmf-dist/doc/latex/newverbs
%dir %{_texdir}/texmf-dist/doc/latex/nfssext-cfr
%dir %{_texdir}/texmf-dist/doc/latex/niceframe
%dir %{_texdir}/texmf-dist/doc/latex/nicetext
%dir %{_texdir}/texmf-dist/doc/latex/nicetext/demo
%dir %{_texdir}/texmf-dist/doc/latex/nicetext/docsrc
%dir %{_texdir}/texmf-dist/doc/latex/nih
%dir %{_texdir}/texmf-dist/doc/latex/nlctdoc
%dir %{_texdir}/texmf-dist/doc/latex/noitcrul
%dir %{_texdir}/texmf-dist/doc/latex/nolbreaks
%dir %{_texdir}/texmf-dist/doc/latex/nomencl
%dir %{_texdir}/texmf-dist/doc/latex/nomentbl
%dir %{_texdir}/texmf-dist/doc/latex/nonfloat
%dir %{_texdir}/texmf-dist/doc/latex/nopageno
%dir %{_texdir}/texmf-dist/doc/latex/nostarch
%dir %{_texdir}/texmf-dist/doc/latex/notes
%dir %{_texdir}/texmf-dist/doc/latex/notes2bib
%dir %{_texdir}/texmf-dist/doc/latex/notoccite
%dir %{_texdir}/texmf-dist/doc/latex/nrc
%dir %{_texdir}/texmf-dist/doc/latex/ntabbing
%dir %{_texdir}/texmf-dist/doc/latex/ntgclass
%dir %{_texdir}/texmf-dist/doc/latex/ntheorem
%dir %{_texdir}/texmf-dist/doc/latex/ntheorem-vn
%dir %{_texdir}/texmf-dist/doc/latex/ntheorem-vn/src
%dir %{_texdir}/texmf-dist/doc/latex/numname
%dir %{_texdir}/texmf-dist/doc/latex/numprint
%dir %{_texdir}/texmf-dist/doc/latex/oberdiek
%dir %{_texdir}/texmf-dist/doc/latex/oberdiek/test
%dir %{_texdir}/texmf-dist/doc/latex/objectz
%dir %{_texdir}/texmf-dist/doc/latex/ocgtools
%dir %{_texdir}/texmf-dist/doc/latex/ocgtools/examples
%dir %{_texdir}/texmf-dist/doc/latex/ocr-latex
%dir %{_texdir}/texmf-dist/doc/latex/octavo
%dir %{_texdir}/texmf-dist/doc/latex/ogham
%dir %{_texdir}/texmf-dist/doc/latex/oldstyle
%dir %{_texdir}/texmf-dist/doc/latex/onlyamsmath
%dir %{_texdir}/texmf-dist/doc/latex/onrannual
%dir %{_texdir}/texmf-dist/doc/latex/opcit
%dir %{_texdir}/texmf-dist/doc/latex/optional
%dir %{_texdir}/texmf-dist/doc/latex/ordinalpt
%dir %{_texdir}/texmf-dist/doc/latex/othello
%dir %{_texdir}/texmf-dist/doc/latex/otibet
%dir %{_texdir}/texmf-dist/doc/latex/ot-tableau
%dir %{_texdir}/texmf-dist/doc/latex/outline
%dir %{_texdir}/texmf-dist/doc/latex/outliner
%dir %{_texdir}/texmf-dist/doc/latex/overpic
%dir %{_texdir}/texmf-dist/doc/latex/pagecont
%dir %{_texdir}/texmf-dist/doc/latex/pagenote
%dir %{_texdir}/texmf-dist/doc/latex/pagerange
%dir %{_texdir}/texmf-dist/doc/latex/pageslts
%dir %{_texdir}/texmf-dist/doc/latex/paper
%dir %{_texdir}/texmf-dist/doc/latex/papercdcase
%dir %{_texdir}/texmf-dist/doc/latex/papermas
%dir %{_texdir}/texmf-dist/doc/latex/papertex
%dir %{_texdir}/texmf-dist/doc/latex/papertex/example
%dir %{_texdir}/texmf-dist/doc/latex/papertex/example/img
%dir %{_texdir}/texmf-dist/doc/latex/papertex/example/img/weather
%dir %{_texdir}/texmf-dist/doc/latex/paralist
%dir %{_texdir}/texmf-dist/doc/latex/parallel
%dir %{_texdir}/texmf-dist/doc/latex/paresse
%dir %{_texdir}/texmf-dist/doc/latex/parrun
%dir %{_texdir}/texmf-dist/doc/latex/patchcmd
%dir %{_texdir}/texmf-dist/doc/latex/pauldoc
%dir %{_texdir}/texmf-dist/doc/latex/pax
%dir %{_texdir}/texmf-dist/doc/latex/pb-diagram
%dir %{_texdir}/texmf-dist/doc/latex/pbox
%dir %{_texdir}/texmf-dist/doc/latex/pbsheet
%dir %{_texdir}/texmf-dist/doc/latex/pbsheet/xpl
%dir %{_texdir}/texmf-dist/doc/latex/pbsheet/xpl/img
%dir %{_texdir}/texmf-dist/doc/latex/pbsheet/xpl/pgm
%dir %{_texdir}/texmf-dist/doc/latex/pdf14
%dir %{_texdir}/texmf-dist/doc/latex/pdfcomment
%dir %{_texdir}/texmf-dist/doc/latex/pdfcprot
%dir %{_texdir}/texmf-dist/doc/latex/pdf-forms-tutorial-de
%dir %{_texdir}/texmf-dist/doc/latex/pdf-forms-tutorial-de/examples
%dir %{_texdir}/texmf-dist/doc/latex/pdf-forms-tutorial-de/forms-src
%dir %{_texdir}/texmf-dist/doc/latex/pdf-forms-tutorial-en
%dir %{_texdir}/texmf-dist/doc/latex/pdf-forms-tutorial-en/examples
%dir %{_texdir}/texmf-dist/doc/latex/pdf-forms-tutorial-en/forms-src
%dir %{_texdir}/texmf-dist/doc/latex/pdfjam
%dir %{_texdir}/texmf-dist/doc/latex/pdfmarginpar
%dir %{_texdir}/texmf-dist/doc/latex/pdfpages
%dir %{_texdir}/texmf-dist/doc/latex/pdfscreen
%dir %{_texdir}/texmf-dist/doc/latex/pdfslide
%dir %{_texdir}/texmf-dist/doc/latex/pdfsync
%dir %{_texdir}/texmf-dist/doc/latex/pdftricks
%dir %{_texdir}/texmf-dist/doc/latex/pdfwin
%dir %{_texdir}/texmf-dist/doc/latex/pdfx
%dir %{_texdir}/texmf-dist/doc/latex/pecha
%dir %{_texdir}/texmf-dist/doc/latex/perception
%dir %{_texdir}/texmf-dist/doc/latex/perltex
%dir %{_texdir}/texmf-dist/doc/latex/permute
%dir %{_texdir}/texmf-dist/doc/latex/petiteannonce
%dir %{_texdir}/texmf-dist/doc/latex/petri-nets
%dir %{_texdir}/texmf-dist/doc/latex/pgfopts
%dir %{_texdir}/texmf-dist/doc/latex/pgfplots
%dir %{_texdir}/texmf-dist/doc/latex/pgfplots/figures
%dir %{_texdir}/texmf-dist/doc/latex/pgfplots/gallery
%dir %{_texdir}/texmf-dist/doc/latex/pgfplots/gnuplot
%dir %{_texdir}/texmf-dist/doc/latex/pgfplots/plotdata
%dir %{_texdir}/texmf-dist/doc/latex/pgf-soroban
%dir %{_texdir}/texmf-dist/doc/latex/pgf-umlsd
%dir %{_texdir}/texmf-dist/doc/latex/philex
%dir %{_texdir}/texmf-dist/doc/latex/philosophersimprint
%dir %{_texdir}/texmf-dist/doc/latex/photo
%dir %{_texdir}/texmf-dist/doc/latex/picinpar
%dir %{_texdir}/texmf-dist/doc/latex/pict2e
%dir %{_texdir}/texmf-dist/doc/latex/pigpen
%dir %{_texdir}/texmf-dist/doc/latex/pinlabel
%dir %{_texdir}/texmf-dist/doc/latex/pinlabel/src
%dir %{_texdir}/texmf-dist/doc/latex/pittetd
%dir %{_texdir}/texmf-dist/doc/latex/placeins
%dir %{_texdir}/texmf-dist/doc/latex/plantslabels
%dir %{_texdir}/texmf-dist/doc/latex/plantslabels/doc
%dir %{_texdir}/texmf-dist/doc/latex/plantslabels/doc/pdf
%dir %{_texdir}/texmf-dist/doc/latex/plantslabels/doc/tex
%dir %{_texdir}/texmf-dist/doc/latex/plantslabels/example
%dir %{_texdir}/texmf-dist/doc/latex/plantslabels/example/pdf
%dir %{_texdir}/texmf-dist/doc/latex/plantslabels/example/tex
%dir %{_texdir}/texmf-dist/doc/latex/plari
%dir %{_texdir}/texmf-dist/doc/latex/plates
%dir %{_texdir}/texmf-dist/doc/latex/play
%dir %{_texdir}/texmf-dist/doc/latex/plweb
%dir %{_texdir}/texmf-dist/doc/latex/pmgraph
%dir %{_texdir}/texmf-dist/doc/latex/poemscol
%dir %{_texdir}/texmf-dist/doc/latex/polski
%dir %{_texdir}/texmf-dist/doc/latex/polyglot
%dir %{_texdir}/texmf-dist/doc/latex/polynom
%dir %{_texdir}/texmf-dist/doc/latex/polynomial
%dir %{_texdir}/texmf-dist/doc/latex/polytable
%dir %{_texdir}/texmf-dist/doc/latex/postcards
%dir %{_texdir}/texmf-dist/doc/latex/powerdot
%dir %{_texdir}/texmf-dist/doc/latex/powerdot-FUBerlin
%dir %{_texdir}/texmf-dist/doc/latex/ppower4
%dir %{_texdir}/texmf-dist/doc/latex/ppower4/demo
%dir %{_texdir}/texmf-dist/doc/latex/ppower4/edemo
%dir %{_texdir}/texmf-dist/doc/latex/ppower4/exampled
%dir %{_texdir}/texmf-dist/doc/latex/ppower4/examplee
%dir %{_texdir}/texmf-dist/doc/latex/ppower4/leveldemo
%dir %{_texdir}/texmf-dist/doc/latex/ppr-prv
%dir %{_texdir}/texmf-dist/doc/latex/pracjourn
%dir %{_texdir}/texmf-dist/doc/latex/preprint
%dir %{_texdir}/texmf-dist/doc/latex/prerex
%dir %{_texdir}/texmf-dist/doc/latex/prerex/doc
%dir %{_texdir}/texmf-dist/doc/latex/prerex/patches
%dir %{_texdir}/texmf-dist/doc/latex/presentations
%dir %{_texdir}/texmf-dist/doc/latex/presentations/images
%dir %{_texdir}/texmf-dist/doc/latex/presentations/images/beamer
%dir %{_texdir}/texmf-dist/doc/latex/presentations/images/pd
%dir %{_texdir}/texmf-dist/doc/latex/presentations/images/pdfscreen
%dir %{_texdir}/texmf-dist/doc/latex/prettyref
%dir %{_texdir}/texmf-dist/doc/latex/preview
%dir %{_texdir}/texmf-dist/doc/latex/proba
%dir %{_texdir}/texmf-dist/doc/latex/probsoln
%dir %{_texdir}/texmf-dist/doc/latex/probsoln/samples
%dir %{_texdir}/texmf-dist/doc/latex/procIAGssymp
%dir %{_texdir}/texmf-dist/doc/latex/program
%dir %{_texdir}/texmf-dist/doc/latex/progress
%dir %{_texdir}/texmf-dist/doc/latex/properties
%dir %{_texdir}/texmf-dist/doc/latex/prosper
%dir %{_texdir}/texmf-dist/doc/latex/protex
%dir %{_texdir}/texmf-dist/doc/latex/protocol
%dir %{_texdir}/texmf-dist/doc/latex/psbao
%dir %{_texdir}/texmf-dist/doc/latex/pseudocode
%dir %{_texdir}/texmf-dist/doc/latex/psfrag
%dir %{_texdir}/texmf-dist/doc/latex/psfrag-italian
%dir %{_texdir}/texmf-dist/doc/latex/psfragx
%dir %{_texdir}/texmf-dist/doc/latex/psgo
%dir %{_texdir}/texmf-dist/doc/latex/psnfss
%dir %{_texdir}/texmf-dist/doc/latex/psnfss/test
%dir %{_texdir}/texmf-dist/doc/latex/pspicture
%dir %{_texdir}/texmf-dist/doc/latex/pst2pdf
%dir %{_texdir}/texmf-dist/doc/latex/pst-calendar
%dir %{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg
%dir %{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples
%dir %{_texdir}/texmf-dist/doc/latex/pst-exa
%dir %{_texdir}/texmf-dist/doc/latex/pstool
%dir %{_texdir}/texmf-dist/doc/latex/pstool/subdir
%dir %{_texdir}/texmf-dist/doc/latex/pst-pdf
%dir %{_texdir}/texmf-dist/doc/latex/pstricks_calcnotes
%dir %{_texdir}/texmf-dist/doc/latex/pstricks_calcnotes/Convert_PstricsCode_To_Pdf
%dir %{_texdir}/texmf-dist/doc/latex/pstricks_calcnotes/For_Pdf_Output
%dir %{_texdir}/texmf-dist/doc/latex/pstricks_calcnotes/For_Ps_Output
%dir %{_texdir}/texmf-dist/doc/latex/pst-vowel
%dir %{_texdir}/texmf-dist/doc/latex/psu-thesis
%dir %{_texdir}/texmf-dist/doc/latex/ptptex
%dir %{_texdir}/texmf-dist/doc/latex/qcm
%dir %{_texdir}/texmf-dist/doc/latex/qobitree
%dir %{_texdir}/texmf-dist/doc/latex/qstest
%dir %{_texdir}/texmf-dist/doc/latex/qsymbols
%dir %{_texdir}/texmf-dist/doc/latex/qtree
%dir %{_texdir}/texmf-dist/doc/latex/quotchap
%dir %{_texdir}/texmf-dist/doc/latex/quotmark
%dir %{_texdir}/texmf-dist/doc/latex/randbild
%dir %{_texdir}/texmf-dist/doc/latex/randtext
%dir %{_texdir}/texmf-dist/doc/latex/rccol
%dir %{_texdir}/texmf-dist/doc/latex/rcs
%dir %{_texdir}/texmf-dist/doc/latex/rcsinfo
%dir %{_texdir}/texmf-dist/doc/latex/rcs-multi
%dir %{_texdir}/texmf-dist/doc/latex/recipe
%dir %{_texdir}/texmf-dist/doc/latex/recipecard
%dir %{_texdir}/texmf-dist/doc/latex/rectopma
%dir %{_texdir}/texmf-dist/doc/latex/refcheck
%dir %{_texdir}/texmf-dist/doc/latex/refman
%dir %{_texdir}/texmf-dist/doc/latex/refstyle
%dir %{_texdir}/texmf-dist/doc/latex/regcount
%dir %{_texdir}/texmf-dist/doc/latex/register
%dir %{_texdir}/texmf-dist/doc/latex/repeatindex
%dir %{_texdir}/texmf-dist/doc/latex/revtex
%dir %{_texdir}/texmf-dist/doc/latex/revtex4
%dir %{_texdir}/texmf-dist/doc/latex/revtex/aip
%dir %{_texdir}/texmf-dist/doc/latex/revtex/aps
%dir %{_texdir}/texmf-dist/doc/latex/revtex/auguide
%dir %{_texdir}/texmf-dist/doc/latex/revtex/sample
%dir %{_texdir}/texmf-dist/doc/latex/revtex/sample/aip
%dir %{_texdir}/texmf-dist/doc/latex/revtex/sample/aps
%dir %{_texdir}/texmf-dist/doc/latex/revtex/source
%dir %{_texdir}/texmf-dist/doc/latex/rjlparshap
%dir %{_texdir}/texmf-dist/doc/latex/rmpage
%dir %{_texdir}/texmf-dist/doc/latex/robustcommand
%dir %{_texdir}/texmf-dist/doc/latex/robustindex
%dir %{_texdir}/texmf-dist/doc/latex/romannum
%dir %{_texdir}/texmf-dist/doc/latex/rotating
%dir %{_texdir}/texmf-dist/doc/latex/rotfloat
%dir %{_texdir}/texmf-dist/doc/latex/rotpages
%dir %{_texdir}/texmf-dist/doc/latex/rotpages/Documentation
%dir %{_texdir}/texmf-dist/doc/latex/rotpages/Examples
%dir %{_texdir}/texmf-dist/doc/latex/roundbox
%dir %{_texdir}/texmf-dist/doc/latex/rsc
%dir %{_texdir}/texmf-dist/doc/latex/rst
%dir %{_texdir}/texmf-dist/doc/latex/rtkinenc
%dir %{_texdir}/texmf-dist/doc/latex/rtklage
%dir %{_texdir}/texmf-dist/doc/latex/r_und_s
%dir %{_texdir}/texmf-dist/doc/latex/ryethesis
%dir %{_texdir}/texmf-dist/doc/latex/sageep
%dir %{_texdir}/texmf-dist/doc/latex/sanskrit
%dir %{_texdir}/texmf-dist/doc/latex/sansmath
%dir %{_texdir}/texmf-dist/doc/latex/sauerj
%dir %{_texdir}/texmf-dist/doc/latex/sauterfonts
%dir %{_texdir}/texmf-dist/doc/latex/savefnmark
%dir %{_texdir}/texmf-dist/doc/latex/savetrees
%dir %{_texdir}/texmf-dist/doc/latex/scale
%dir %{_texdir}/texmf-dist/doc/latex/scalebar
%dir %{_texdir}/texmf-dist/doc/latex/schemabloc
%dir %{_texdir}/texmf-dist/doc/latex/scientificpaper
%dir %{_texdir}/texmf-dist/doc/latex/sciposter
%dir %{_texdir}/texmf-dist/doc/latex/sciposter/sciposterexample
%dir %{_texdir}/texmf-dist/doc/latex/sciposter/sciposterexample/auto
%dir %{_texdir}/texmf-dist/doc/latex/sciwordconv
%dir %{_texdir}/texmf-dist/doc/latex/screenplay
%dir %{_texdir}/texmf-dist/doc/latex/sdrt
%dir %{_texdir}/texmf-dist/doc/latex/sectionbox
%dir %{_texdir}/texmf-dist/doc/latex/sectionbox/example
%dir %{_texdir}/texmf-dist/doc/latex/sectsty
%dir %{_texdir}/texmf-dist/doc/latex/semantic
%dir %{_texdir}/texmf-dist/doc/latex/seminar
%dir %{_texdir}/texmf-dist/doc/latex/semioneside
%dir %{_texdir}/texmf-dist/doc/latex/seqsplit
%dir %{_texdir}/texmf-dist/doc/latex/seuthesis
%dir %{_texdir}/texmf-dist/doc/latex/seuthesis/a3cover
%dir %{_texdir}/texmf-dist/doc/latex/seuthesis/figures
%dir %{_texdir}/texmf-dist/doc/latex/seuthesis/zharticle
%dir %{_texdir}/texmf-dist/doc/latex/sf298
%dir %{_texdir}/texmf-dist/doc/latex/sffms
%dir %{_texdir}/texmf-dist/doc/latex/sfg
%dir %{_texdir}/texmf-dist/doc/latex/sgame
%dir %{_texdir}/texmf-dist/doc/latex/shadethm
%dir %{_texdir}/texmf-dist/doc/latex/shipunov
%dir %{_texdir}/texmf-dist/doc/latex/shorttoc
%dir %{_texdir}/texmf-dist/doc/latex/show2e
%dir %{_texdir}/texmf-dist/doc/latex/showexpl
%dir %{_texdir}/texmf-dist/doc/latex/showlabels
%dir %{_texdir}/texmf-dist/doc/latex/shuffle
%dir %{_texdir}/texmf-dist/doc/latex/sidecap
%dir %{_texdir}/texmf-dist/doc/latex/sides
%dir %{_texdir}/texmf-dist/doc/latex/siggraph
%dir %{_texdir}/texmf-dist/doc/latex/silence
%dir %{_texdir}/texmf-dist/doc/latex/simplecd
%dir %{_texdir}/texmf-dist/doc/latex/simplecv
%dir %{_texdir}/texmf-dist/doc/latex/simplewick
%dir %{_texdir}/texmf-dist/doc/latex/SIstyle
%dir %{_texdir}/texmf-dist/doc/latex/SIunits
%dir %{_texdir}/texmf-dist/doc/latex/siunitx
%dir %{_texdir}/texmf-dist/doc/latex/skak
%dir %{_texdir}/texmf-dist/doc/latex/skeycommand
%dir %{_texdir}/texmf-dist/doc/latex/skeyval
%dir %{_texdir}/texmf-dist/doc/latex/slantsc
%dir %{_texdir}/texmf-dist/doc/latex/smalltableof
%dir %{_texdir}/texmf-dist/doc/latex/smartref
%dir %{_texdir}/texmf-dist/doc/latex/snapshot
%dir %{_texdir}/texmf-dist/doc/latex/songbook
%dir %{_texdir}/texmf-dist/doc/latex/songbook/contrib
%dir %{_texdir}/texmf-dist/doc/latex/songbook/contrib/CarolBook
%dir %{_texdir}/texmf-dist/doc/latex/songbook/contrib/crd2sb
%dir %{_texdir}/texmf-dist/doc/latex/sort-by-letters
%dir %{_texdir}/texmf-dist/doc/latex/soton
%dir %{_texdir}/texmf-dist/doc/latex/soul
%dir %{_texdir}/texmf-dist/doc/latex/spanish
%dir %{_texdir}/texmf-dist/doc/latex/spanish/doc
%dir %{_texdir}/texmf-dist/doc/latex/spanish-mx
%dir %{_texdir}/texmf-dist/doc/latex/spanish/source
%dir %{_texdir}/texmf-dist/doc/latex/spanish/tex
%dir %{_texdir}/texmf-dist/doc/latex/sparklines
%dir %{_texdir}/texmf-dist/doc/latex/spie
%dir %{_texdir}/texmf-dist/doc/latex/splitbib
%dir %{_texdir}/texmf-dist/doc/latex/splitindex
%dir %{_texdir}/texmf-dist/doc/latex/spotcolor
%dir %{_texdir}/texmf-dist/doc/latex/spreadtab
%dir %{_texdir}/texmf-dist/doc/latex/spverbatim
%dir %{_texdir}/texmf-dist/doc/latex/srcltx
%dir %{_texdir}/texmf-dist/doc/latex/sseq
%dir %{_texdir}/texmf-dist/doc/latex/ssqquote
%dir %{_texdir}/texmf-dist/doc/latex/stage
%dir %{_texdir}/texmf-dist/doc/latex/standalone
%dir %{_texdir}/texmf-dist/doc/latex/statistik
%dir %{_texdir}/texmf-dist/doc/latex/stdclsdv
%dir %{_texdir}/texmf-dist/doc/latex/stdpage
%dir %{_texdir}/texmf-dist/doc/latex/steinmetz
%dir %{_texdir}/texmf-dist/doc/latex/stellenbosch
%dir %{_texdir}/texmf-dist/doc/latex/stellenbosch/templates
%dir %{_texdir}/texmf-dist/doc/latex/stex
%dir %{_texdir}/texmf-dist/doc/latex/stex/assignment
%dir %{_texdir}/texmf-dist/doc/latex/stex/cmathml
%dir %{_texdir}/texmf-dist/doc/latex/stex/cnx
%dir %{_texdir}/texmf-dist/doc/latex/stex/dcm
%dir %{_texdir}/texmf-dist/doc/latex/stex/example
%dir %{_texdir}/texmf-dist/doc/latex/stex/example/background
%dir %{_texdir}/texmf-dist/doc/latex/stex/example/paper
%dir %{_texdir}/texmf-dist/doc/latex/stex/example/test
%dir %{_texdir}/texmf-dist/doc/latex/stex/mikoslides
%dir %{_texdir}/texmf-dist/doc/latex/stex/modules
%dir %{_texdir}/texmf-dist/doc/latex/stex/omd
%dir %{_texdir}/texmf-dist/doc/latex/stex/omdoc
%dir %{_texdir}/texmf-dist/doc/latex/stex/omtext
%dir %{_texdir}/texmf-dist/doc/latex/stex/presentation
%dir %{_texdir}/texmf-dist/doc/latex/stex/problem
%dir %{_texdir}/texmf-dist/doc/latex/stex/reqdoc
%dir %{_texdir}/texmf-dist/doc/latex/stex/sproof
%dir %{_texdir}/texmf-dist/doc/latex/stex/sref
%dir %{_texdir}/texmf-dist/doc/latex/stex/statements
%dir %{_texdir}/texmf-dist/doc/latex/stringstrings
%dir %{_texdir}/texmf-dist/doc/latex/struktex
%dir %{_texdir}/texmf-dist/doc/latex/sttools
%dir %{_texdir}/texmf-dist/doc/latex/sttools/doc
%dir %{_texdir}/texmf-dist/doc/latex/stubs
%dir %{_texdir}/texmf-dist/doc/latex/subdepth
%dir %{_texdir}/texmf-dist/doc/latex/subeqn
%dir %{_texdir}/texmf-dist/doc/latex/subeqnarray
%dir %{_texdir}/texmf-dist/doc/latex/subfig
%dir %{_texdir}/texmf-dist/doc/latex/subfigure
%dir %{_texdir}/texmf-dist/doc/latex/subfloat
%dir %{_texdir}/texmf-dist/doc/latex/substr
%dir %{_texdir}/texmf-dist/doc/latex/sudoku
%dir %{_texdir}/texmf-dist/doc/latex/sudokubundle
%dir %{_texdir}/texmf-dist/doc/latex/sugconf
%dir %{_texdir}/texmf-dist/doc/latex/supertabular
%dir %{_texdir}/texmf-dist/doc/latex/susy
%dir %{_texdir}/texmf-dist/doc/latex/svgcolor
%dir %{_texdir}/texmf-dist/doc/latex/svg-inkscape
%dir %{_texdir}/texmf-dist/doc/latex/svn
%dir %{_texdir}/texmf-dist/doc/latex/svninfo
%dir %{_texdir}/texmf-dist/doc/latex/svn-multi
%dir %{_texdir}/texmf-dist/doc/latex/svn-prov
%dir %{_texdir}/texmf-dist/doc/latex/swebib
%dir %{_texdir}/texmf-dist/doc/latex/swimgraf
%dir %{_texdir}/texmf-dist/doc/latex/syllogism
%dir %{_texdir}/texmf-dist/doc/latex/synproof
%dir %{_texdir}/texmf-dist/doc/latex/syntax
%dir %{_texdir}/texmf-dist/doc/latex/syntrace
%dir %{_texdir}/texmf-dist/doc/latex/synttree
%dir %{_texdir}/texmf-dist/doc/latex/Tabbing
%dir %{_texdir}/texmf-dist/doc/latex/tableaux
%dir %{_texdir}/texmf-dist/doc/latex/tablenotes
%dir %{_texdir}/texmf-dist/doc/latex/tablists
%dir %{_texdir}/texmf-dist/doc/latex/tablor
%dir %{_texdir}/texmf-dist/doc/latex/tablor/Figures
%dir %{_texdir}/texmf-dist/doc/latex/tabls
%dir %{_texdir}/texmf-dist/doc/latex/tabto-ltx
%dir %{_texdir}/texmf-dist/doc/latex/tabularborder
%dir %{_texdir}/texmf-dist/doc/latex/tabularcalc
%dir %{_texdir}/texmf-dist/doc/latex/tabularew
%dir %{_texdir}/texmf-dist/doc/latex/tabulary
%dir %{_texdir}/texmf-dist/doc/latex/tabvar
%dir %{_texdir}/texmf-dist/doc/latex/talk
%dir %{_texdir}/texmf-dist/doc/latex/t-angles
%dir %{_texdir}/texmf-dist/doc/latex/tapir
%dir %{_texdir}/texmf-dist/doc/latex/tcldoc
%dir %{_texdir}/texmf-dist/doc/latex/tdclock
%dir %{_texdir}/texmf-dist/doc/latex/tdsfrmath
%dir %{_texdir}/texmf-dist/doc/latex/technics
%dir %{_texdir}/texmf-dist/doc/latex/ted
%dir %{_texdir}/texmf-dist/doc/latex/templates-fenn
%dir %{_texdir}/texmf-dist/doc/latex/templates-sommer
%dir %{_texdir}/texmf-dist/doc/latex/tengwarscript
%dir %{_texdir}/texmf-dist/doc/latex/tensor
%dir %{_texdir}/texmf-dist/doc/latex/termlist
%dir %{_texdir}/texmf-dist/doc/latex/teubner
%dir %{_texdir}/texmf-dist/doc/latex/tex-font-errors-cheatsheet
%dir %{_texdir}/texmf-dist/doc/latex/tex-label
%dir %{_texdir}/texmf-dist/doc/latex/texmate
%dir %{_texdir}/texmf-dist/doc/latex/texments
%dir %{_texdir}/texmf-dist/doc/latex/texpower
%dir %{_texdir}/texmf-dist/doc/latex/texpower/contrib
%dir %{_texdir}/texmf-dist/doc/latex/texpower/tpslifonts
%dir %{_texdir}/texmf-dist/doc/latex/texshade
%dir %{_texdir}/texmf-dist/doc/latex/textcase
%dir %{_texdir}/texmf-dist/doc/latex/textfit
%dir %{_texdir}/texmf-dist/doc/latex/textopo
%dir %{_texdir}/texmf-dist/doc/latex/textpos
%dir %{_texdir}/texmf-dist/doc/latex/textpos/examples
%dir %{_texdir}/texmf-dist/doc/latex/theoremref
%dir %{_texdir}/texmf-dist/doc/latex/thesis-titlepage-fhac
%dir %{_texdir}/texmf-dist/doc/latex/thinsp
%dir %{_texdir}/texmf-dist/doc/latex/thmbox
%dir %{_texdir}/texmf-dist/doc/latex/thmtools
%dir %{_texdir}/texmf-dist/doc/latex/threeparttable
%dir %{_texdir}/texmf-dist/doc/latex/threeparttablex
%dir %{_texdir}/texmf-dist/doc/latex/thumb
%dir %{_texdir}/texmf-dist/doc/latex/thumby
%dir %{_texdir}/texmf-dist/doc/latex/thuthesis
%dir %{_texdir}/texmf-dist/doc/latex/thuthesis/example
%dir %{_texdir}/texmf-dist/doc/latex/thuthesis/example/data
%dir %{_texdir}/texmf-dist/doc/latex/thuthesis/example/figures
%dir %{_texdir}/texmf-dist/doc/latex/thuthesis/example/ref
%dir %{_texdir}/texmf-dist/doc/latex/ticket
%dir %{_texdir}/texmf-dist/doc/latex/tikz-3dplot
%dir %{_texdir}/texmf-dist/doc/latex/tikz-inet
%dir %{_texdir}/texmf-dist/doc/latex/tikz-qtree
%dir %{_texdir}/texmf-dist/doc/latex/tikz-timing
%dir %{_texdir}/texmf-dist/doc/latex/timesht
%dir %{_texdir}/texmf-dist/doc/latex/titlepages
%dir %{_texdir}/texmf-dist/doc/latex/titlepic
%dir %{_texdir}/texmf-dist/doc/latex/titleref
%dir %{_texdir}/texmf-dist/doc/latex/titlesec
%dir %{_texdir}/texmf-dist/doc/latex/titling
%dir %{_texdir}/texmf-dist/doc/latex/tkz-doc
%dir %{_texdir}/texmf-dist/doc/latex/tkz-linknodes
%dir %{_texdir}/texmf-dist/doc/latex/tkz-linknodes/doc
%dir %{_texdir}/texmf-dist/doc/latex/tkz-orm
%dir %{_texdir}/texmf-dist/doc/latex/tkz-tab
%dir %{_texdir}/texmf-dist/doc/latex/tlc2
%dir %{_texdir}/texmf-dist/doc/latex/tocbibind
%dir %{_texdir}/texmf-dist/doc/latex/tocloft
%dir %{_texdir}/texmf-dist/doc/latex/tocvsec2
%dir %{_texdir}/texmf-dist/doc/latex/todo
%dir %{_texdir}/texmf-dist/doc/latex/todonotes
%dir %{_texdir}/texmf-dist/doc/latex/tokenizer
%dir %{_texdir}/texmf-dist/doc/latex/toolbox
%dir %{_texdir}/texmf-dist/doc/latex/tools
%dir %{_texdir}/texmf-dist/doc/latex/topfloat
%dir %{_texdir}/texmf-dist/doc/latex/toptesi
%dir %{_texdir}/texmf-dist/doc/latex/totcount
%dir %{_texdir}/texmf-dist/doc/latex/totpages
%dir %{_texdir}/texmf-dist/doc/latex/tpslifonts
%dir %{_texdir}/texmf-dist/doc/latex/trajan
%dir %{_texdir}/texmf-dist/doc/latex/trfsigns
%dir %{_texdir}/texmf-dist/doc/latex/trimspaces
%dir %{_texdir}/texmf-dist/doc/latex/trivfloat
%dir %{_texdir}/texmf-dist/doc/latex/trsym
%dir %{_texdir}/texmf-dist/doc/latex/truncate
%dir %{_texdir}/texmf-dist/doc/latex/tufte-latex
%dir %{_texdir}/texmf-dist/doc/latex/tufte-latex/graphics
%dir %{_texdir}/texmf-dist/doc/latex/tugboat
%dir %{_texdir}/texmf-dist/doc/latex/turkmen
%dir %{_texdir}/texmf-dist/doc/latex/turnstile
%dir %{_texdir}/texmf-dist/doc/latex/twoinone
%dir %{_texdir}/texmf-dist/doc/latex/twoup
%dir %{_texdir}/texmf-dist/doc/latex/type1cm
%dir %{_texdir}/texmf-dist/doc/latex/typedref
%dir %{_texdir}/texmf-dist/doc/latex/typehtml
%dir %{_texdir}/texmf-dist/doc/latex/typogrid
%dir %{_texdir}/texmf-dist/doc/latex/uaclasses
%dir %{_texdir}/texmf-dist/doc/latex/ucdavisthesis
%dir %{_texdir}/texmf-dist/doc/latex/ucdavisthesis/Example
%dir %{_texdir}/texmf-dist/doc/latex/ucs
%dir %{_texdir}/texmf-dist/doc/latex/ucs/config
%dir %{_texdir}/texmf-dist/doc/latex/ucthesis
%dir %{_texdir}/texmf-dist/doc/latex/uebungsblatt
%dir %{_texdir}/texmf-dist/doc/latex/uiucthesis
%dir %{_texdir}/texmf-dist/doc/latex/ulqda
%dir %{_texdir}/texmf-dist/doc/latex/umich-thesis
%dir %{_texdir}/texmf-dist/doc/latex/uml
%dir %{_texdir}/texmf-dist/doc/latex/umlaute
%dir %{_texdir}/texmf-dist/doc/latex/umoline
%dir %{_texdir}/texmf-dist/doc/latex/umthesis
%dir %{_texdir}/texmf-dist/doc/latex/underlin
%dir %{_texdir}/texmf-dist/doc/latex/underscore
%dir %{_texdir}/texmf-dist/doc/latex/undolabl
%dir %{_texdir}/texmf-dist/doc/latex/unicode-math
%dir %{_texdir}/texmf-dist/doc/latex/units
%dir %{_texdir}/texmf-dist/doc/latex/unitsdef
%dir %{_texdir}/texmf-dist/doc/latex/upmethodology
%dir %{_texdir}/texmf-dist/doc/latex/url
%dir %{_texdir}/texmf-dist/doc/latex/urlbst
%dir %{_texdir}/texmf-dist/doc/latex/ushort
%dir %{_texdir}/texmf-dist/doc/latex/ut-thesis
%dir %{_texdir}/texmf-dist/doc/latex/uwthesis
%dir %{_texdir}/texmf-dist/doc/latex/varindex
%dir %{_texdir}/texmf-dist/doc/latex/varsfromjobname
%dir %{_texdir}/texmf-dist/doc/latex/verbatimbox
%dir %{_texdir}/texmf-dist/doc/latex/verbatimcopy
%dir %{_texdir}/texmf-dist/doc/latex/verbdef
%dir %{_texdir}/texmf-dist/doc/latex/verse
%dir %{_texdir}/texmf-dist/doc/latex/vhistory
%dir %{_texdir}/texmf-dist/doc/latex/visualfaq
%dir %{_texdir}/texmf-dist/doc/latex/visualfaq/source
%dir %{_texdir}/texmf-dist/doc/latex/vita
%dir %{_texdir}/texmf-dist/doc/latex/vmargin
%dir %{_texdir}/texmf-dist/doc/latex/volumes
%dir %{_texdir}/texmf-dist/doc/latex/vpe
%dir %{_texdir}/texmf-dist/doc/latex/vrsion
%dir %{_texdir}/texmf-dist/doc/latex/vwcol
%dir %{_texdir}/texmf-dist/doc/latex/vxu
%dir %{_texdir}/texmf-dist/doc/latex/wallpaper
%dir %{_texdir}/texmf-dist/doc/latex/wallpaper/example
%dir %{_texdir}/texmf-dist/doc/latex/wallpaper/example/auto
%dir %{_texdir}/texmf-dist/doc/latex/warpcol
%dir %{_texdir}/texmf-dist/doc/latex/was
%dir %{_texdir}/texmf-dist/doc/latex/wasysym
%dir %{_texdir}/texmf-dist/doc/latex/webguide
%dir %{_texdir}/texmf-dist/doc/latex/widetable
%dir %{_texdir}/texmf-dist/doc/latex/williams
%dir %{_texdir}/texmf-dist/doc/latex/wnri
%dir %{_texdir}/texmf-dist/doc/latex/wordlike
%dir %{_texdir}/texmf-dist/doc/latex/wrapfig
%dir %{_texdir}/texmf-dist/doc/latex/xargs
%dir %{_texdir}/texmf-dist/doc/latex/xcolor
%dir %{_texdir}/texmf-dist/doc/latex/xdoc
%dir %{_texdir}/texmf-dist/doc/latex/xfor
%dir %{_texdir}/texmf-dist/doc/latex/xifthen
%dir %{_texdir}/texmf-dist/doc/latex/xkeyval
%dir %{_texdir}/texmf-dist/doc/latex/xmpincl
%dir %{_texdir}/texmf-dist/doc/latex/xnewcommand
%dir %{_texdir}/texmf-dist/doc/latex/xoptarg
%dir %{_texdir}/texmf-dist/doc/latex/xpackages
%dir %{_texdir}/texmf-dist/doc/latex/xpackages/xbase
%dir %{_texdir}/texmf-dist/doc/latex/xpackages/xtras
%dir %{_texdir}/texmf-dist/doc/latex/xskak
%dir %{_texdir}/texmf-dist/doc/latex/xtab
%dir %{_texdir}/texmf-dist/doc/latex/xwatermark
%dir %{_texdir}/texmf-dist/doc/latex/xwatermark/Graphics
%dir %{_texdir}/texmf-dist/doc/latex/xyling
%dir %{_texdir}/texmf-dist/doc/latex/xypdf
%dir %{_texdir}/texmf-dist/doc/latex/xytree
%dir %{_texdir}/texmf-dist/doc/latex/yafoot
%dir %{_texdir}/texmf-dist/doc/latex/yagusylo
%dir %{_texdir}/texmf-dist/doc/latex/ydoc
%dir %{_texdir}/texmf-dist/doc/latex/yfonts
%dir %{_texdir}/texmf-dist/doc/latex/yhmath
%dir %{_texdir}/texmf-dist/doc/latex/york-thesis
%dir %{_texdir}/texmf-dist/doc/latex/youngtab
%dir %{_texdir}/texmf-dist/doc/latex/yplan
%dir %{_texdir}/texmf-dist/doc/latex/zed-csp
%dir %{_texdir}/texmf-dist/doc/latex/ziffer
%dir %{_texdir}/texmf-dist/doc/latex/zwgetfdate
%dir %{_texdir}/texmf-dist/doc/latex/zwpagelayout
%dir %{_texdir}/texmf-dist/doc/lualatex
%dir %{_texdir}/texmf-dist/doc/lualatex/luainputenc
%dir %{_texdir}/texmf-dist/doc/luatex
%dir %{_texdir}/texmf-dist/doc/luatex/base
%dir %{_texdir}/texmf-dist/doc/luatex/hyph-utf8
%dir %{_texdir}/texmf-dist/doc/luatex/lualibs
%dir %{_texdir}/texmf-dist/doc/luatex/luamplib
%dir %{_texdir}/texmf-dist/doc/luatex/luaotfload
%dir %{_texdir}/texmf-dist/doc/luatex/luatexbase
%dir %{_texdir}/texmf-dist/doc/luatex/luatextra
%dir %{_texdir}/texmf-dist/doc/metapost
%dir %{_texdir}/texmf-dist/doc/metapost/automata
%dir %{_texdir}/texmf-dist/doc/metapost/base
%dir %{_texdir}/texmf-dist/doc/metapost/base/source-manual
%dir %{_texdir}/texmf-dist/doc/metapost/base/source-tutorial
%dir %{_texdir}/texmf-dist/doc/metapost/bbcard
%dir %{_texdir}/texmf-dist/doc/metapost/blockdraw_mp
%dir %{_texdir}/texmf-dist/doc/metapost/bpolynomial
%dir %{_texdir}/texmf-dist/doc/metapost/cmarrows
%dir %{_texdir}/texmf-dist/doc/metapost/drv
%dir %{_texdir}/texmf-dist/doc/metapost/drv/doc
%dir %{_texdir}/texmf-dist/doc/metapost/drv/sample
%dir %{_texdir}/texmf-dist/doc/metapost/drv/template
%dir %{_texdir}/texmf-dist/doc/metapost/dviincl
%dir %{_texdir}/texmf-dist/doc/metapost/epsincl
%dir %{_texdir}/texmf-dist/doc/metapost/expressg
%dir %{_texdir}/texmf-dist/doc/metapost/exteps
%dir %{_texdir}/texmf-dist/doc/metapost/featpost
%dir %{_texdir}/texmf-dist/doc/metapost/featpost/bashscript
%dir %{_texdir}/texmf-dist/doc/metapost/featpost/doc
%dir %{_texdir}/texmf-dist/doc/metapost/featpost/example
%dir %{_texdir}/texmf-dist/doc/metapost/featpost/example/bugtrack
%dir %{_texdir}/texmf-dist/doc/metapost/featpost/example/highmemory
%dir %{_texdir}/texmf-dist/doc/metapost/featpost/example/repeated
%dir %{_texdir}/texmf-dist/doc/metapost/featpost/example/standard
%dir %{_texdir}/texmf-dist/doc/metapost/featpost/example/tug04
%dir %{_texdir}/texmf-dist/doc/metapost/featpost/galrey
%dir %{_texdir}/texmf-dist/doc/metapost/featpost/jpeg
%dir %{_texdir}/texmf-dist/doc/metapost/featpost/latex
%dir %{_texdir}/texmf-dist/doc/metapost/featpost/macro
%dir %{_texdir}/texmf-dist/doc/metapost/featpost/nontextualpng
%dir %{_texdir}/texmf-dist/doc/metapost/featpost/png
%dir %{_texdir}/texmf-dist/doc/metapost/featpost/typesetinspace
%dir %{_texdir}/texmf-dist/doc/metapost/featpost/xcmd
%dir %{_texdir}/texmf-dist/doc/metapost/garrigues
%dir %{_texdir}/texmf-dist/doc/metapost/hatching
%dir %{_texdir}/texmf-dist/doc/metapost/latexmp
%dir %{_texdir}/texmf-dist/doc/metapost/makecirc
%dir %{_texdir}/texmf-dist/doc/metapost/metago
%dir %{_texdir}/texmf-dist/doc/metapost/metaobj
%dir %{_texdir}/texmf-dist/doc/metapost/metapost-examples
%dir %{_texdir}/texmf-dist/doc/metapost/metauml
%dir %{_texdir}/texmf-dist/doc/metapost/metauml/metauml_manual
%dir %{_texdir}/texmf-dist/doc/metapost/metauml/metauml_manual/fig
%dir %{_texdir}/texmf-dist/doc/metapost/mpattern
%dir %{_texdir}/texmf-dist/doc/metapost/mpman-ru
%dir %{_texdir}/texmf-dist/doc/metapost/piechartmp
%dir %{_texdir}/texmf-dist/doc/metapost/piechartmp/examples
%dir %{_texdir}/texmf-dist/doc/metapost/slideshow
%dir %{_texdir}/texmf-dist/doc/metapost/splines
%dir %{_texdir}/texmf-dist/doc/metapost/suanpan
%dir %{_texdir}/texmf-dist/doc/metapost/textpath
%dir %{_texdir}/texmf-dist/doc/metapost/venn
%dir %{_texdir}/texmf-dist/doc/mex
%dir %{_texdir}/texmf-dist/doc/mex/base
%dir %{_texdir}/texmf-dist/doc/mex/utf8mex
%dir %{_texdir}/texmf-dist/doc/mex/utf8mex/examples
%dir %{_texdir}/texmf-dist/doc/omega
%dir %{_texdir}/texmf-dist/doc/omega/antomega
%dir %{_texdir}/texmf-dist/doc/omega/base
%dir %{_texdir}/texmf-dist/doc/omega/ocherokee
%dir %{_texdir}/texmf-dist/doc/otherformats
%dir %{_texdir}/texmf-dist/doc/otherformats/alatex
%dir %{_texdir}/texmf-dist/doc/otherformats/alatex/base
%dir %{_texdir}/texmf-dist/doc/otherformats/jadetex
%dir %{_texdir}/texmf-dist/doc/otherformats/jadetex/base
%dir %{_texdir}/texmf-dist/doc/otherformats/psizzl
%dir %{_texdir}/texmf-dist/doc/otherformats/psizzl/base
%dir %{_texdir}/texmf-dist/doc/otherformats/startex
%dir %{_texdir}/texmf-dist/doc/otherformats/startex/base
%dir %{_texdir}/texmf-dist/doc/otherformats/texsis
%dir %{_texdir}/texmf-dist/doc/otherformats/texsis/base
%dir %{_texdir}/texmf-dist/doc/otherformats/xmltex
%dir %{_texdir}/texmf-dist/doc/otherformats/xmltex/base
%dir %{_texdir}/texmf-dist/doc/otherformats/xmltex/xmlplay
%dir %{_texdir}/texmf-dist/doc/pdftex
%dir %{_texdir}/texmf-dist/doc/pdftex/manual
%dir %{_texdir}/texmf-dist/doc/pdftex/manual/samplepdf
%dir %{_texdir}/texmf-dist/doc/pdftex/pdftex-pdfkeys
%dir %{_texdir}/texmf-dist/doc/pdftex/thanh
%dir %{_texdir}/texmf-dist/doc/pdftex/thanh/ext
%dir %{_texdir}/texmf-dist/doc/plain
%dir %{_texdir}/texmf-dist/doc/plain/cweb
%dir %{_texdir}/texmf-dist/doc/plain/fontch
%dir %{_texdir}/texmf-dist/doc/plain/font-change
%dir %{_texdir}/texmf-dist/doc/plain/gentle
%dir %{_texdir}/texmf-dist/doc/plain/graphics-pln
%dir %{_texdir}/texmf-dist/doc/plain/gustlib
%dir %{_texdir}/texmf-dist/doc/plain/harvmac
%dir %{_texdir}/texmf-dist/doc/plain/hyplain
%dir %{_texdir}/texmf-dist/doc/plain/impatient
%dir %{_texdir}/texmf-dist/doc/plain/impatient-fr
%dir %{_texdir}/texmf-dist/doc/plain/js-misc
%dir %{_texdir}/texmf-dist/doc/plain/js-misc/xfig
%dir %{_texdir}/texmf-dist/doc/plain/metatex
%dir %{_texdir}/texmf-dist/doc/plain/metatex/mtpaper
%dir %{_texdir}/texmf-dist/doc/plain/mkpattern
%dir %{_texdir}/texmf-dist/doc/plain/newsletr
%dir %{_texdir}/texmf-dist/doc/plain/pgfplots
%dir %{_texdir}/texmf-dist/doc/plain/pitex
%dir %{_texdir}/texmf-dist/doc/plain/plnfss
%dir %{_texdir}/texmf-dist/doc/plain/resumemac
%dir %{_texdir}/texmf-dist/doc/plain/texbytopic
%dir %{_texdir}/texmf-dist/doc/plain/treetex
%dir %{_texdir}/texmf-dist/doc/plain/tugboat-plain
%dir %{_texdir}/texmf-dist/doc/plain/varisize
%dir %{_texdir}/texmf-dist/doc/ptex
%dir %{_texdir}/texmf-dist/doc/ptex/base
%dir %{_texdir}/texmf-dist/doc/ptex/jvf
%dir %{_texdir}/texmf-dist/doc/ptex/pbibtex
%dir %{_texdir}/texmf-dist/doc/support
%dir %{_texdir}/texmf-dist/doc/support/asymptote-by-example-zh-cn
%dir %{_texdir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src
%dir %{_texdir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/figure-src
%dir %{_texdir}/texmf-dist/doc/support/asymptote-faq-zh-cn
%dir %{_texdir}/texmf-dist/doc/support/asymptote-faq-zh-cn/src
%dir %{_texdir}/texmf-dist/doc/support/asymptote-faq-zh-cn/src/figures
%dir %{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn
%dir %{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src
%dir %{_texdir}/texmf-dist/doc/support/bundledoc
%dir %{_texdir}/texmf-dist/doc/support/de-macro
%dir %{_texdir}/texmf-dist/doc/support/epspdf
%dir %{_texdir}/texmf-dist/doc/support/epspdf/images
%dir %{_texdir}/texmf-dist/doc/support/fig4latex
%dir %{_texdir}/texmf-dist/doc/support/fig4latex/figs
%dir %{_texdir}/texmf-dist/doc/support/findhyph
%dir %{_texdir}/texmf-dist/doc/support/fontools
%dir %{_texdir}/texmf-dist/doc/support/fontools/examples
%dir %{_texdir}/texmf-dist/doc/support/fontools/examples/berling
%dir %{_texdir}/texmf-dist/doc/support/fontools/examples/frutiger
%dir %{_texdir}/texmf-dist/doc/support/fontools/examples/palatinox
%dir %{_texdir}/texmf-dist/doc/support/fragmaster
%dir %{_texdir}/texmf-dist/doc/support/fragmaster/example
%dir %{_texdir}/texmf-dist/doc/support/gustprog
%dir %{_texdir}/texmf-dist/doc/support/latex2man
%dir %{_texdir}/texmf-dist/doc/support/latexmk
%dir %{_texdir}/texmf-dist/doc/support/latexmk/example_rcfiles
%dir %{_texdir}/texmf-dist/doc/support/latexmk/extra-scripts
%dir %{_texdir}/texmf-dist/doc/support/lua-alt-getopt
%dir %{_texdir}/texmf-dist/doc/support/lua-alt-getopt/tests
%dir %{_texdir}/texmf-dist/doc/support/makeindex
%dir %{_texdir}/texmf-dist/doc/support/mkgrkindex
%dir %{_texdir}/texmf-dist/doc/support/patgen2-tutorial
%dir %{_texdir}/texmf-dist/doc/support/pdfcrop
%dir %{_texdir}/texmf-dist/doc/support/pkfix
%dir %{_texdir}/texmf-dist/doc/support/pkfix-helper
%dir %{_texdir}/texmf-dist/doc/support/purifyeps
%dir %{_texdir}/texmf-dist/doc/support/texcount
%dir %{_texdir}/texmf-dist/doc/support/texdraw
%dir %{_texdir}/texmf-dist/doc/support/texloganalyser
%dir %{_texdir}/texmf-dist/doc/xelatex
%dir %{_texdir}/texmf-dist/doc/xelatex/arabxetex
%dir %{_texdir}/texmf-dist/doc/xelatex/arabxetex/examples
%dir %{_texdir}/texmf-dist/doc/xelatex/fontwrap
%dir %{_texdir}/texmf-dist/doc/xelatex/mathspec
%dir %{_texdir}/texmf-dist/doc/xelatex/persian-bib
%dir %{_texdir}/texmf-dist/doc/xelatex/philokalia
%dir %{_texdir}/texmf-dist/doc/xelatex/polyglossia
%dir %{_texdir}/texmf-dist/doc/xelatex/xecjk
%dir %{_texdir}/texmf-dist/doc/xelatex/xecjk/examples
%dir %{_texdir}/texmf-dist/doc/xelatex/xecolour
%dir %{_texdir}/texmf-dist/doc/xelatex/xecyr
%dir %{_texdir}/texmf-dist/doc/xelatex/xeindex
%dir %{_texdir}/texmf-dist/doc/xelatex/xepersian
%dir %{_texdir}/texmf-dist/doc/xelatex/xetex-itrans
%dir %{_texdir}/texmf-dist/doc/xelatex/xgreek
%dir %{_texdir}/texmf-dist/doc/xelatex/xltxtra
%dir %{_texdir}/texmf-dist/doc/xelatex/xunicode
%dir %{_texdir}/texmf-dist/doc/xetex
%dir %{_texdir}/texmf-dist/doc/xetex/base
%dir %{_texdir}/texmf-dist/doc/xetex/xesearch
%dir %{_texdir}/texmf-dist/doc/xetex/xetexfontinfo
%dir %{_texdir}/texmf-dist/doc/xetex/xetex-pstricks
%dir %{_texdir}/texmf-dist/doc/xetex/xetexref
%dir %{_texdir}/texmf-dist/doc/xetex/zhspacing
%dir %{_texdir}/texmf-dist/dvips
%dir %{_texdir}/texmf-dist/dvips/antiqua
%dir %{_texdir}/texmf-dist/dvips/antp
%dir %{_texdir}/texmf-dist/dvips/arphic
%dir %{_texdir}/texmf-dist/dvips/avantgar
%dir %{_texdir}/texmf-dist/dvips/base
%dir %{_texdir}/texmf-dist/dvips/bookman
%dir %{_texdir}/texmf-dist/dvips/brushscr
%dir %{_texdir}/texmf-dist/dvips/cm-super
%dir %{_texdir}/texmf-dist/dvips/colorsep
%dir %{_texdir}/texmf-dist/dvips/courier
%dir %{_texdir}/texmf-dist/dvips/cs
%dir %{_texdir}/texmf-dist/dvips/dvipsconfig
%dir %{_texdir}/texmf-dist/dvips/esint-type1
%dir %{_texdir}/texmf-dist/dvips/garuda-c90
%dir %{_texdir}/texmf-dist/dvips/gastex
%dir %{_texdir}/texmf-dist/dvips/gothic
%dir %{_texdir}/texmf-dist/dvips/grotesq
%dir %{_texdir}/texmf-dist/dvips/helvetic
%dir %{_texdir}/texmf-dist/dvips/hfbright
%dir %{_texdir}/texmf-dist/dvips/initials
%dir %{_texdir}/texmf-dist/dvips/libertine
%dir %{_texdir}/texmf-dist/dvips/mathdesign
%dir %{_texdir}/texmf-dist/dvips/multi
%dir %{_texdir}/texmf-dist/dvips/musixps
%dir %{_texdir}/texmf-dist/dvips/musixtex
%dir %{_texdir}/texmf-dist/dvips/ncntrsbk
%dir %{_texdir}/texmf-dist/dvips/norasi-c90
%dir %{_texdir}/texmf-dist/dvips/omega
%dir %{_texdir}/texmf-dist/dvips/palatino
%dir %{_texdir}/texmf-dist/dvips/pl
%dir %{_texdir}/texmf-dist/dvips/psfrag
%dir %{_texdir}/texmf-dist/dvips/pspicture
%dir %{_texdir}/texmf-dist/dvips/pst-3d
%dir %{_texdir}/texmf-dist/dvips/pst-3dplot
%dir %{_texdir}/texmf-dist/dvips/pst-bar
%dir %{_texdir}/texmf-dist/dvips/pst-barcode
%dir %{_texdir}/texmf-dist/dvips/pst-bezier
%dir %{_texdir}/texmf-dist/dvips/pst-blur
%dir %{_texdir}/texmf-dist/dvips/pst-circ
%dir %{_texdir}/texmf-dist/dvips/pst-coil
%dir %{_texdir}/texmf-dist/dvips/pst-cox
%dir %{_texdir}/texmf-dist/dvips/pst-electricfield
%dir %{_texdir}/texmf-dist/dvips/pst-eucl
%dir %{_texdir}/texmf-dist/dvips/pst-fractal
%dir %{_texdir}/texmf-dist/dvips/pst-fun
%dir %{_texdir}/texmf-dist/dvips/pst-func
%dir %{_texdir}/texmf-dist/dvips/pst-geo
%dir %{_texdir}/texmf-dist/dvips/pst-ghsb
%dir %{_texdir}/texmf-dist/dvips/pst-grad
%dir %{_texdir}/texmf-dist/dvips/pst-knot
%dir %{_texdir}/texmf-dist/dvips/pst-light3d
%dir %{_texdir}/texmf-dist/dvips/pst-magneticfield
%dir %{_texdir}/texmf-dist/dvips/pst-math
%dir %{_texdir}/texmf-dist/dvips/pst-mirror
%dir %{_texdir}/texmf-dist/dvips/pst-node
%dir %{_texdir}/texmf-dist/dvips/pst-optexp
%dir %{_texdir}/texmf-dist/dvips/pstricks
%dir %{_texdir}/texmf-dist/dvips/pstricks-add
%dir %{_texdir}/texmf-dist/dvips/pst-slpe
%dir %{_texdir}/texmf-dist/dvips/pst-solides3d
%dir %{_texdir}/texmf-dist/dvips/pst-spectra
%dir %{_texdir}/texmf-dist/dvips/pst-text
%dir %{_texdir}/texmf-dist/dvips/pst-vue3d
%dir %{_texdir}/texmf-dist/dvips/symbol
%dir %{_texdir}/texmf-dist/dvips/tex-ps
%dir %{_texdir}/texmf-dist/dvips/times
%dir %{_texdir}/texmf-dist/dvips/uhc
%dir %{_texdir}/texmf-dist/dvips/xcolor
%dir %{_texdir}/texmf-dist/dvips/xypic
%dir %{_texdir}/texmf-dist/dvips/zapfchan
%dir %{_texdir}/texmf-dist/dvips/zapfding
%dir %{_texdir}/texmf-dist/fonts
%dir %{_texdir}/texmf-dist/fonts/afm
%dir %{_texdir}/texmf-dist/fonts/afm/adobe
%dir %{_texdir}/texmf-dist/fonts/afm/adobe/avantgar
%dir %{_texdir}/texmf-dist/fonts/afm/adobe/bookman
%dir %{_texdir}/texmf-dist/fonts/afm/adobe/courier
%dir %{_texdir}/texmf-dist/fonts/afm/adobe/helvetic
%dir %{_texdir}/texmf-dist/fonts/afm/adobe/ncntrsbk
%dir %{_texdir}/texmf-dist/fonts/afm/adobe/palatino
%dir %{_texdir}/texmf-dist/fonts/afm/adobe/symbol
%dir %{_texdir}/texmf-dist/fonts/afm/adobe/times
%dir %{_texdir}/texmf-dist/fonts/afm/adobe/utopia
%dir %{_texdir}/texmf-dist/fonts/afm/adobe/zapfchan
%dir %{_texdir}/texmf-dist/fonts/afm/adobe/zapfding
%dir %{_texdir}/texmf-dist/fonts/afm/arabi
%dir %{_texdir}/texmf-dist/fonts/afm/arabi/arabeyes
%dir %{_texdir}/texmf-dist/fonts/afm/arkandis
%dir %{_texdir}/texmf-dist/fonts/afm/arkandis/baskervald
%dir %{_texdir}/texmf-dist/fonts/afm/arkandis/libris
%dir %{_texdir}/texmf-dist/fonts/afm/arkandis/romande
%dir %{_texdir}/texmf-dist/fonts/afm/arkandis/venturis
%dir %{_texdir}/texmf-dist/fonts/afm/arkandis/venturis2
%dir %{_texdir}/texmf-dist/fonts/afm/arkandis/venturisold
%dir %{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans
%dir %{_texdir}/texmf-dist/fonts/afm/arkandis/venturissans2
%dir %{_texdir}/texmf-dist/fonts/afm/arphic
%dir %{_texdir}/texmf-dist/fonts/afm/arphic/bkaiu
%dir %{_texdir}/texmf-dist/fonts/afm/arphic/bsmiu
%dir %{_texdir}/texmf-dist/fonts/afm/arphic/gbsnu
%dir %{_texdir}/texmf-dist/fonts/afm/arphic/gkaiu
%dir %{_texdir}/texmf-dist/fonts/afm/bitstrea
%dir %{_texdir}/texmf-dist/fonts/afm/bitstrea/charter
%dir %{_texdir}/texmf-dist/fonts/afm/groff
%dir %{_texdir}/texmf-dist/fonts/afm/hoekwater
%dir %{_texdir}/texmf-dist/fonts/afm/hoekwater/context
%dir %{_texdir}/texmf-dist/fonts/afm/hoekwater/manfnt
%dir %{_texdir}/texmf-dist/fonts/afm/hoekwater/mflogo
%dir %{_texdir}/texmf-dist/fonts/afm/hoekwater/stmaryrd
%dir %{_texdir}/texmf-dist/fonts/afm/ibm
%dir %{_texdir}/texmf-dist/fonts/afm/ibm/courier
%dir %{_texdir}/texmf-dist/fonts/afm/ibm/times
%dir %{_texdir}/texmf-dist/fonts/afm/itc
%dir %{_texdir}/texmf-dist/fonts/afm/itc/psafm
%dir %{_texdir}/texmf-dist/fonts/afm/itc/psafm/stonesan
%dir %{_texdir}/texmf-dist/fonts/afm/jmn
%dir %{_texdir}/texmf-dist/fonts/afm/jmn/hans
%dir %{_texdir}/texmf-dist/fonts/afm/mathdesign
%dir %{_texdir}/texmf-dist/fonts/afm/mathdesign/mdbch
%dir %{_texdir}/texmf-dist/fonts/afm/mathdesign/mdput
%dir %{_texdir}/texmf-dist/fonts/afm/mathdesign/mdugm
%dir %{_texdir}/texmf-dist/fonts/afm/public
%dir %{_texdir}/texmf-dist/fonts/afm/public/amsfonts
%dir %{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cm
%dir %{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cmextra
%dir %{_texdir}/texmf-dist/fonts/afm/public/amsfonts/cyrillic
%dir %{_texdir}/texmf-dist/fonts/afm/public/amsfonts/euler
%dir %{_texdir}/texmf-dist/fonts/afm/public/amsfonts/latxfont
%dir %{_texdir}/texmf-dist/fonts/afm/public/amsfonts/symbols
%dir %{_texdir}/texmf-dist/fonts/afm/public/antp
%dir %{_texdir}/texmf-dist/fonts/afm/public/antt
%dir %{_texdir}/texmf-dist/fonts/afm/public/archaic
%dir %{_texdir}/texmf-dist/fonts/afm/public/arev
%dir %{_texdir}/texmf-dist/fonts/afm/public/augie
%dir %{_texdir}/texmf-dist/fonts/afm/public/auncial-new
%dir %{_texdir}/texmf-dist/fonts/afm/public/aurical
%dir %{_texdir}/texmf-dist/fonts/afm/public/bera
%dir %{_texdir}/texmf-dist/fonts/afm/public/brushscr
%dir %{_texdir}/texmf-dist/fonts/afm/public/carolmin-ps
%dir %{_texdir}/texmf-dist/fonts/afm/public/chemarrow
%dir %{_texdir}/texmf-dist/fonts/afm/public/cjhebrew
%dir %{_texdir}/texmf-dist/fonts/afm/public/cm-lgc
%dir %{_texdir}/texmf-dist/fonts/afm/public/cm-super
%dir %{_texdir}/texmf-dist/fonts/afm/public/cm-unicode
%dir %{_texdir}/texmf-dist/fonts/afm/public/cryst
%dir %{_texdir}/texmf-dist/fonts/afm/public/cyklop
%dir %{_texdir}/texmf-dist/fonts/afm/public/dictsym
%dir %{_texdir}/texmf-dist/fonts/afm/public/epigrafica
%dir %{_texdir}/texmf-dist/fonts/afm/public/figbas
%dir %{_texdir}/texmf-dist/fonts/afm/public/fonetika
%dir %{_texdir}/texmf-dist/fonts/afm/public/fourier
%dir %{_texdir}/texmf-dist/fonts/afm/public/fouriernc
%dir %{_texdir}/texmf-dist/fonts/afm/public/fpl
%dir %{_texdir}/texmf-dist/fonts/afm/public/gentium
%dir %{_texdir}/texmf-dist/fonts/afm/public/gfsartemisia
%dir %{_texdir}/texmf-dist/fonts/afm/public/gfsbaskerville
%dir %{_texdir}/texmf-dist/fonts/afm/public/gfsbodoni
%dir %{_texdir}/texmf-dist/fonts/afm/public/gfscomplutum
%dir %{_texdir}/texmf-dist/fonts/afm/public/gfsdidot
%dir %{_texdir}/texmf-dist/fonts/afm/public/gfsneohellenic
%dir %{_texdir}/texmf-dist/fonts/afm/public/gfsporson
%dir %{_texdir}/texmf-dist/fonts/afm/public/gfssolomos
%dir %{_texdir}/texmf-dist/fonts/afm/public/gothic
%dir %{_texdir}/texmf-dist/fonts/afm/public/grverb
%dir %{_texdir}/texmf-dist/fonts/afm/public/hfbright
%dir %{_texdir}/texmf-dist/fonts/afm/public/ibygrk
%dir %{_texdir}/texmf-dist/fonts/afm/public/initials
%dir %{_texdir}/texmf-dist/fonts/afm/public/itrans
%dir %{_texdir}/texmf-dist/fonts/afm/public/iwona
%dir %{_texdir}/texmf-dist/fonts/afm/public/kerkis
%dir %{_texdir}/texmf-dist/fonts/afm/public/knitting
%dir %{_texdir}/texmf-dist/fonts/afm/public/kpfonts
%dir %{_texdir}/texmf-dist/fonts/afm/public/kurier
%dir %{_texdir}/texmf-dist/fonts/afm/public/libertine
%dir %{_texdir}/texmf-dist/fonts/afm/public/linearA
%dir %{_texdir}/texmf-dist/fonts/afm/public/lm
%dir %{_texdir}/texmf-dist/fonts/afm/public/marvosym
%dir %{_texdir}/texmf-dist/fonts/afm/public/mathpazo
%dir %{_texdir}/texmf-dist/fonts/afm/public/ocherokee
%dir %{_texdir}/texmf-dist/fonts/afm/public/omega
%dir %{_texdir}/texmf-dist/fonts/afm/public/phaistos
%dir %{_texdir}/texmf-dist/fonts/afm/public/pl
%dir %{_texdir}/texmf-dist/fonts/afm/public/pxfonts
%dir %{_texdir}/texmf-dist/fonts/afm/public/rsfs
%dir %{_texdir}/texmf-dist/fonts/afm/public/semaphor
%dir %{_texdir}/texmf-dist/fonts/afm/public/skaknew
%dir %{_texdir}/texmf-dist/fonts/afm/public/tabvar
%dir %{_texdir}/texmf-dist/fonts/afm/public/tex-gyre
%dir %{_texdir}/texmf-dist/fonts/afm/public/thailatex
%dir %{_texdir}/texmf-dist/fonts/afm/public/trajan
%dir %{_texdir}/texmf-dist/fonts/afm/public/txfonts
%dir %{_texdir}/texmf-dist/fonts/afm/public/txfontsb
%dir %{_texdir}/texmf-dist/fonts/afm/public/velthuis
%dir %{_texdir}/texmf-dist/fonts/afm/public/wasy
%dir %{_texdir}/texmf-dist/fonts/afm/public/xypic
%dir %{_texdir}/texmf-dist/fonts/afm/uhc
%dir %{_texdir}/texmf-dist/fonts/afm/uhc/umj
%dir %{_texdir}/texmf-dist/fonts/afm/urw
%dir %{_texdir}/texmf-dist/fonts/afm/urw/antiqua
%dir %{_texdir}/texmf-dist/fonts/afm/urw/avantgar
%dir %{_texdir}/texmf-dist/fonts/afm/urw/bookman
%dir %{_texdir}/texmf-dist/fonts/afm/urw/courier
%dir %{_texdir}/texmf-dist/fonts/afm/urw/grotesq
%dir %{_texdir}/texmf-dist/fonts/afm/urw/helvetic
%dir %{_texdir}/texmf-dist/fonts/afm/urw/ncntrsbk
%dir %{_texdir}/texmf-dist/fonts/afm/urw/palatino
%dir %{_texdir}/texmf-dist/fonts/afm/urw/symbol
%dir %{_texdir}/texmf-dist/fonts/afm/urw/times
%dir %{_texdir}/texmf-dist/fonts/afm/urw/zapfchan
%dir %{_texdir}/texmf-dist/fonts/afm/urw/zapfding
%dir %{_texdir}/texmf-dist/fonts/afm/vntex
%dir %{_texdir}/texmf-dist/fonts/afm/vntex/chartervn
%dir %{_texdir}/texmf-dist/fonts/afm/vntex/grotesqvn
%dir %{_texdir}/texmf-dist/fonts/afm/vntex/urwvn
%dir %{_texdir}/texmf-dist/fonts/afm/vntex/vntopia
%dir %{_texdir}/texmf-dist/fonts/cid
%dir %{_texdir}/texmf-dist/fonts/cid/fontforge
%dir %{_texdir}/texmf-dist/fonts/cmap
%dir %{_texdir}/texmf-dist/fonts/cmap/adobemapping
%dir %{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16
%dir %{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap
%dir %{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15
%dir %{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap
%dir %{_texdir}/texmf-dist/fonts/cmap/adobemapping/ai0
%dir %{_texdir}/texmf-dist/fonts/cmap/adobemapping/ai0/CMap
%dir %{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16
%dir %{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap
%dir %{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12
%dir %{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap
%dir %{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther
%dir %{_texdir}/texmf-dist/fonts/cmap/adobemapping/ToUnicode
%dir %{_texdir}/texmf-dist/fonts/enc
%dir %{_texdir}/texmf-dist/fonts/enc/dvips
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/antp
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/antt
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/arabi
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/arev
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/base
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/baskervald
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/c90
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/cbfonts
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/ccicons
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/cfr-lm
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/chessfss
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/cjhebrew
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/cm-lgc
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/cm-super
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/cm-unicode
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/context
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/cs
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/cyklop
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/epigrafica
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/fontools
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/gentium
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/gfsartemisia
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/gfsbaskerville
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/gfsbodoni
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/gfscomplutum
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/gfsdidot
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/gfsneohellenic
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/gfsporson
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/gfssolomos
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/groff
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/hfbright
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/ibygrk
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/inconsolata
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/iwona
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/jmn
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/kerkis
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/kpfonts
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/kurier
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/libertine
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/libris
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/lithuanian
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/lm
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/ly1
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/mnsymbol
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/pl
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/romande
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/semaphor
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/tengwarscript
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/txfonts
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/txfontsb
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/venturisadf
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/vntex
%dir %{_texdir}/texmf-dist/fonts/enc/dvips/xypic
%dir %{_texdir}/texmf-dist/fonts/enc/pdftex
%dir %{_texdir}/texmf-dist/fonts/enc/pdftex/kpfonts
%dir %{_texdir}/texmf-dist/fonts/enc/pdftex/vntex
%dir %{_texdir}/texmf-dist/fonts/enc/t2
%dir %{_texdir}/texmf-dist/fonts/fea
%dir %{_texdir}/texmf-dist/fonts/fea/context
%dir %{_texdir}/texmf-dist/fonts/map
%dir %{_texdir}/texmf-dist/fonts/map/dvipdfm
%dir %{_texdir}/texmf-dist/fonts/map/dvipdfm/lm
%dir %{_texdir}/texmf-dist/fonts/map/dvips
%dir %{_texdir}/texmf-dist/fonts/map/dvips/allrunes
%dir %{_texdir}/texmf-dist/fonts/map/dvips/amsfonts
%dir %{_texdir}/texmf-dist/fonts/map/dvips/antiqua
%dir %{_texdir}/texmf-dist/fonts/map/dvips/antp
%dir %{_texdir}/texmf-dist/fonts/map/dvips/antt
%dir %{_texdir}/texmf-dist/fonts/map/dvips/arabi
%dir %{_texdir}/texmf-dist/fonts/map/dvips/arabtex
%dir %{_texdir}/texmf-dist/fonts/map/dvips/archaic
%dir %{_texdir}/texmf-dist/fonts/map/dvips/arev
%dir %{_texdir}/texmf-dist/fonts/map/dvips/arphic
%dir %{_texdir}/texmf-dist/fonts/map/dvips/ascii
%dir %{_texdir}/texmf-dist/fonts/map/dvips/augie
%dir %{_texdir}/texmf-dist/fonts/map/dvips/auncial-new
%dir %{_texdir}/texmf-dist/fonts/map/dvips/aurical
%dir %{_texdir}/texmf-dist/fonts/map/dvips/avantgar
%dir %{_texdir}/texmf-dist/fonts/map/dvips/baskervald
%dir %{_texdir}/texmf-dist/fonts/map/dvips/belleek
%dir %{_texdir}/texmf-dist/fonts/map/dvips/bera
%dir %{_texdir}/texmf-dist/fonts/map/dvips/bookman
%dir %{_texdir}/texmf-dist/fonts/map/dvips/brushscr
%dir %{_texdir}/texmf-dist/fonts/map/dvips/burmese
%dir %{_texdir}/texmf-dist/fonts/map/dvips/carolmin-ps
%dir %{_texdir}/texmf-dist/fonts/map/dvips/cbfonts
%dir %{_texdir}/texmf-dist/fonts/map/dvips/ccicons
%dir %{_texdir}/texmf-dist/fonts/map/dvips/cc-pl
%dir %{_texdir}/texmf-dist/fonts/map/dvips/cfr-lm
%dir %{_texdir}/texmf-dist/fonts/map/dvips/chemarrow
%dir %{_texdir}/texmf-dist/fonts/map/dvips/cjhebrew
%dir %{_texdir}/texmf-dist/fonts/map/dvips/cm
%dir %{_texdir}/texmf-dist/fonts/map/dvips/cmcyr
%dir %{_texdir}/texmf-dist/fonts/map/dvips/cm-lgc
%dir %{_texdir}/texmf-dist/fonts/map/dvips/cmll
%dir %{_texdir}/texmf-dist/fonts/map/dvips/cm-super
%dir %{_texdir}/texmf-dist/fonts/map/dvips/cm-unicode
%dir %{_texdir}/texmf-dist/fonts/map/dvips/context
%dir %{_texdir}/texmf-dist/fonts/map/dvips/courier
%dir %{_texdir}/texmf-dist/fonts/map/dvips/cs
%dir %{_texdir}/texmf-dist/fonts/map/dvips/cyklop
%dir %{_texdir}/texmf-dist/fonts/map/dvips/dictsym
%dir %{_texdir}/texmf-dist/fonts/map/dvips/doublestroke
%dir %{_texdir}/texmf-dist/fonts/map/dvips/dozenal
%dir %{_texdir}/texmf-dist/fonts/map/dvips/epigrafica
%dir %{_texdir}/texmf-dist/fonts/map/dvips/epiolmec
%dir %{_texdir}/texmf-dist/fonts/map/dvips/esint-type1
%dir %{_texdir}/texmf-dist/fonts/map/dvips/esvect
%dir %{_texdir}/texmf-dist/fonts/map/dvips/ethiop-t1
%dir %{_texdir}/texmf-dist/fonts/map/dvips/eurofont
%dir %{_texdir}/texmf-dist/fonts/map/dvips/eurosym
%dir %{_texdir}/texmf-dist/fonts/map/dvips/fge
%dir %{_texdir}/texmf-dist/fonts/map/dvips/figbas
%dir %{_texdir}/texmf-dist/fonts/map/dvips/foekfont
%dir %{_texdir}/texmf-dist/fonts/map/dvips/fonetika
%dir %{_texdir}/texmf-dist/fonts/map/dvips/fourier
%dir %{_texdir}/texmf-dist/fonts/map/dvips/garuda-c90
%dir %{_texdir}/texmf-dist/fonts/map/dvips/gfsartemisia
%dir %{_texdir}/texmf-dist/fonts/map/dvips/gfsbaskerville
%dir %{_texdir}/texmf-dist/fonts/map/dvips/gfsbodoni
%dir %{_texdir}/texmf-dist/fonts/map/dvips/gfscomplutum
%dir %{_texdir}/texmf-dist/fonts/map/dvips/gfsdidot
%dir %{_texdir}/texmf-dist/fonts/map/dvips/gfsneohellenic
%dir %{_texdir}/texmf-dist/fonts/map/dvips/gfsporson
%dir %{_texdir}/texmf-dist/fonts/map/dvips/gfssolomos
%dir %{_texdir}/texmf-dist/fonts/map/dvips/gothic
%dir %{_texdir}/texmf-dist/fonts/map/dvips/groff
%dir %{_texdir}/texmf-dist/fonts/map/dvips/grotesq
%dir %{_texdir}/texmf-dist/fonts/map/dvips/grverb
%dir %{_texdir}/texmf-dist/fonts/map/dvips/helvetic
%dir %{_texdir}/texmf-dist/fonts/map/dvips/hfbright
%dir %{_texdir}/texmf-dist/fonts/map/dvips/ibygrk
%dir %{_texdir}/texmf-dist/fonts/map/dvips/inconsolata
%dir %{_texdir}/texmf-dist/fonts/map/dvips/initials
%dir %{_texdir}/texmf-dist/fonts/map/dvips/iwona
%dir %{_texdir}/texmf-dist/fonts/map/dvips/jmn
%dir %{_texdir}/texmf-dist/fonts/map/dvips/kerkis
%dir %{_texdir}/texmf-dist/fonts/map/dvips/knitting
%dir %{_texdir}/texmf-dist/fonts/map/dvips/kpfonts
%dir %{_texdir}/texmf-dist/fonts/map/dvips/kurier
%dir %{_texdir}/texmf-dist/fonts/map/dvips/libertine
%dir %{_texdir}/texmf-dist/fonts/map/dvips/libris
%dir %{_texdir}/texmf-dist/fonts/map/dvips/linearA
%dir %{_texdir}/texmf-dist/fonts/map/dvips/lithuanian
%dir %{_texdir}/texmf-dist/fonts/map/dvips/lm
%dir %{_texdir}/texmf-dist/fonts/map/dvips/lxfonts
%dir %{_texdir}/texmf-dist/fonts/map/dvips/ly1
%dir %{_texdir}/texmf-dist/fonts/map/dvips/manfnt
%dir %{_texdir}/texmf-dist/fonts/map/dvips/marvosym
%dir %{_texdir}/texmf-dist/fonts/map/dvips/mathdesign
%dir %{_texdir}/texmf-dist/fonts/map/dvips/mflogo
%dir %{_texdir}/texmf-dist/fonts/map/dvips/mnsymbol
%dir %{_texdir}/texmf-dist/fonts/map/dvips/montex
%dir %{_texdir}/texmf-dist/fonts/map/dvips/musixtex
%dir %{_texdir}/texmf-dist/fonts/map/dvips/ncntrsbk
%dir %{_texdir}/texmf-dist/fonts/map/dvips/norasi-c90
%dir %{_texdir}/texmf-dist/fonts/map/dvips/ocherokee
%dir %{_texdir}/texmf-dist/fonts/map/dvips/oinuit
%dir %{_texdir}/texmf-dist/fonts/map/dvips/omega
%dir %{_texdir}/texmf-dist/fonts/map/dvips/palatino
%dir %{_texdir}/texmf-dist/fonts/map/dvips/phaistos
%dir %{_texdir}/texmf-dist/fonts/map/dvips/pigpen
%dir %{_texdir}/texmf-dist/fonts/map/dvips/pl
%dir %{_texdir}/texmf-dist/fonts/map/dvips/pslatex
%dir %{_texdir}/texmf-dist/fonts/map/dvips/psnfss
%dir %{_texdir}/texmf-dist/fonts/map/dvips/pxfonts
%dir %{_texdir}/texmf-dist/fonts/map/dvips/recycle
%dir %{_texdir}/texmf-dist/fonts/map/dvips/romande
%dir %{_texdir}/texmf-dist/fonts/map/dvips/rsfs
%dir %{_texdir}/texmf-dist/fonts/map/dvips/sanskrit
%dir %{_texdir}/texmf-dist/fonts/map/dvips/semaphor
%dir %{_texdir}/texmf-dist/fonts/map/dvips/skaknew
%dir %{_texdir}/texmf-dist/fonts/map/dvips/staves
%dir %{_texdir}/texmf-dist/fonts/map/dvips/stmaryrd
%dir %{_texdir}/texmf-dist/fonts/map/dvips/symbol
%dir %{_texdir}/texmf-dist/fonts/map/dvips/tabvar
%dir %{_texdir}/texmf-dist/fonts/map/dvips/tengwarscript
%dir %{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre
%dir %{_texdir}/texmf-dist/fonts/map/dvips/times
%dir %{_texdir}/texmf-dist/fonts/map/dvips/tipa
%dir %{_texdir}/texmf-dist/fonts/map/dvips/trajan
%dir %{_texdir}/texmf-dist/fonts/map/dvips/txfonts
%dir %{_texdir}/texmf-dist/fonts/map/dvips/txfontsb
%dir %{_texdir}/texmf-dist/fonts/map/dvips/uhc
%dir %{_texdir}/texmf-dist/fonts/map/dvips/velthuis
%dir %{_texdir}/texmf-dist/fonts/map/dvips/venturis
%dir %{_texdir}/texmf-dist/fonts/map/dvips/venturis2
%dir %{_texdir}/texmf-dist/fonts/map/dvips/venturisold
%dir %{_texdir}/texmf-dist/fonts/map/dvips/venturissans
%dir %{_texdir}/texmf-dist/fonts/map/dvips/venturissans2
%dir %{_texdir}/texmf-dist/fonts/map/dvips/vntex
%dir %{_texdir}/texmf-dist/fonts/map/dvips/wasy
%dir %{_texdir}/texmf-dist/fonts/map/dvips/xypic
%dir %{_texdir}/texmf-dist/fonts/map/dvips/yhmath
%dir %{_texdir}/texmf-dist/fonts/map/dvips/zapfchan
%dir %{_texdir}/texmf-dist/fonts/map/dvips/zapfding
%dir %{_texdir}/texmf-dist/fonts/map/fontname
%dir %{_texdir}/texmf-dist/fonts/map/glyphlist
%dir %{_texdir}/texmf-dist/fonts/map/luatex
%dir %{_texdir}/texmf-dist/fonts/map/luatex/context
%dir %{_texdir}/texmf-dist/fonts/map/pdftex
%dir %{_texdir}/texmf-dist/fonts/map/pdftex/context
%dir %{_texdir}/texmf-dist/fonts/map/pdftex/gentium
%dir %{_texdir}/texmf-dist/fonts/map/vtex
%dir %{_texdir}/texmf-dist/fonts/map/vtex/bera
%dir %{_texdir}/texmf-dist/fonts/map/vtex/cm-super
%dir %{_texdir}/texmf-dist/fonts/map/vtex/dictsym
%dir %{_texdir}/texmf-dist/fonts/map/vtex/mnsymbol
%dir %{_texdir}/texmf-dist/fonts/map/vtex/skaknew
%dir %{_texdir}/texmf-dist/fonts/misc
%dir %{_texdir}/texmf-dist/fonts/misc/cns
%dir %{_texdir}/texmf-dist/fonts/misc/xetex
%dir %{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping
%dir %{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex
%dir %{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/base
%dir %{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/context
%dir %{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/harvardkyoto
%dir %{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/polyglossia
%dir %{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/velthuis
%dir %{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/xepersian
%dir %{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/xetex-itrans
%dir %{_texdir}/texmf-dist/fonts/ofm
%dir %{_texdir}/texmf-dist/fonts/ofm/public
%dir %{_texdir}/texmf-dist/fonts/ofm/public/cm-lgc
%dir %{_texdir}/texmf-dist/fonts/ofm/public/ethiop
%dir %{_texdir}/texmf-dist/fonts/ofm/public/ocherokee
%dir %{_texdir}/texmf-dist/fonts/ofm/public/oinuit
%dir %{_texdir}/texmf-dist/fonts/ofm/public/omega
%dir %{_texdir}/texmf-dist/fonts/ofm/public/otibet
%dir %{_texdir}/texmf-dist/fonts/opentype
%dir %{_texdir}/texmf-dist/fonts/opentype/public
%dir %{_texdir}/texmf-dist/fonts/opentype/public/antt
%dir %{_texdir}/texmf-dist/fonts/opentype/public/Asana-Math
%dir %{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode
%dir %{_texdir}/texmf-dist/fonts/opentype/public/cyklop
%dir %{_texdir}/texmf-dist/fonts/opentype/public/gfsartemisia
%dir %{_texdir}/texmf-dist/fonts/opentype/public/gfsbaskerville
%dir %{_texdir}/texmf-dist/fonts/opentype/public/gfsbodoni
%dir %{_texdir}/texmf-dist/fonts/opentype/public/gfscomplutum
%dir %{_texdir}/texmf-dist/fonts/opentype/public/gfsdidot
%dir %{_texdir}/texmf-dist/fonts/opentype/public/gfsneohellenic
%dir %{_texdir}/texmf-dist/fonts/opentype/public/gfsporson
%dir %{_texdir}/texmf-dist/fonts/opentype/public/gfssolomos
%dir %{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont
%dir %{_texdir}/texmf-dist/fonts/opentype/public/inconsolata
%dir %{_texdir}/texmf-dist/fonts/opentype/public/iwona
%dir %{_texdir}/texmf-dist/fonts/opentype/public/kurier
%dir %{_texdir}/texmf-dist/fonts/opentype/public/libertine
%dir %{_texdir}/texmf-dist/fonts/opentype/public/lm
%dir %{_texdir}/texmf-dist/fonts/opentype/public/mnsymbol
%dir %{_texdir}/texmf-dist/fonts/opentype/public/oldstandard
%dir %{_texdir}/texmf-dist/fonts/opentype/public/phaistos
%dir %{_texdir}/texmf-dist/fonts/opentype/public/philokalia
%dir %{_texdir}/texmf-dist/fonts/opentype/public/semaphor
%dir %{_texdir}/texmf-dist/fonts/opentype/public/skaknew
%dir %{_texdir}/texmf-dist/fonts/opentype/public/stix
%dir %{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre
%dir %{_texdir}/texmf-dist/fonts/opentype/public/umtypewriter
%dir %{_texdir}/texmf-dist/fonts/opentype/public/xits
%dir %{_texdir}/texmf-dist/fonts/ovf
%dir %{_texdir}/texmf-dist/fonts/ovf/public
%dir %{_texdir}/texmf-dist/fonts/ovf/public/cm-lgc
%dir %{_texdir}/texmf-dist/fonts/ovf/public/ethiop
%dir %{_texdir}/texmf-dist/fonts/ovf/public/ocherokee
%dir %{_texdir}/texmf-dist/fonts/ovf/public/oinuit
%dir %{_texdir}/texmf-dist/fonts/ovf/public/omega
%dir %{_texdir}/texmf-dist/fonts/ovf/public/otibet
%dir %{_texdir}/texmf-dist/fonts/ovp
%dir %{_texdir}/texmf-dist/fonts/ovp/public
%dir %{_texdir}/texmf-dist/fonts/ovp/public/ethiop
%dir %{_texdir}/texmf-dist/fonts/ovp/public/ocherokee
%dir %{_texdir}/texmf-dist/fonts/ovp/public/omega
%dir %{_texdir}/texmf-dist/fonts/ovp/public/otibet
%dir %{_texdir}/texmf-dist/fonts/pk
%dir %{_texdir}/texmf-dist/fonts/pk/ljfour
%dir %{_texdir}/texmf-dist/fonts/pk/ljfour/public
%dir %{_texdir}/texmf-dist/fonts/pk/ljfour/public/cm
%dir %{_texdir}/texmf-dist/fonts/pk/ljfour/public/cm/dpi600
%dir %{_texdir}/texmf-dist/fonts/pk/ljfour/public/cm/dpi720
%dir %{_texdir}/texmf-dist/fonts/sfd
%dir %{_texdir}/texmf-dist/fonts/sfd/dnp
%dir %{_texdir}/texmf-dist/fonts/sfd/ttf2pk
%dir %{_texdir}/texmf-dist/fonts/source
%dir %{_texdir}/texmf-dist/fonts/source/jknappen
%dir %{_texdir}/texmf-dist/fonts/source/jknappen/ec
%dir %{_texdir}/texmf-dist/fonts/source/jknappen/fc
%dir %{_texdir}/texmf-dist/fonts/source/lh
%dir %{_texdir}/texmf-dist/fonts/source/lh/base
%dir %{_texdir}/texmf-dist/fonts/source/lh/lh-conc
%dir %{_texdir}/texmf-dist/fonts/source/lh/lh-lcy
%dir %{_texdir}/texmf-dist/fonts/source/lh/lh-ot2
%dir %{_texdir}/texmf-dist/fonts/source/lh/lh-t2a
%dir %{_texdir}/texmf-dist/fonts/source/lh/lh-t2b
%dir %{_texdir}/texmf-dist/fonts/source/lh/lh-t2c
%dir %{_texdir}/texmf-dist/fonts/source/lh/lh-t2d
%dir %{_texdir}/texmf-dist/fonts/source/lh/lh-x2
%dir %{_texdir}/texmf-dist/fonts/source/lh/lh-XSlav
%dir %{_texdir}/texmf-dist/fonts/source/lh/nont2
%dir %{_texdir}/texmf-dist/fonts/source/lh/specific
%dir %{_texdir}/texmf-dist/fonts/source/ptex
%dir %{_texdir}/texmf-dist/fonts/source/ptex/ascgrp
%dir %{_texdir}/texmf-dist/fonts/source/ptex/jis
%dir %{_texdir}/texmf-dist/fonts/source/ptex/nmin-ngoth
%dir %{_texdir}/texmf-dist/fonts/source/ptex/standard
%dir %{_texdir}/texmf-dist/fonts/source/public
%dir %{_texdir}/texmf-dist/fonts/source/public/allrunes
%dir %{_texdir}/texmf-dist/fonts/source/public/amsfonts
%dir %{_texdir}/texmf-dist/fonts/source/public/amsfonts/cmextra
%dir %{_texdir}/texmf-dist/fonts/source/public/amsfonts/cyrillic
%dir %{_texdir}/texmf-dist/fonts/source/public/amsfonts/dummy
%dir %{_texdir}/texmf-dist/fonts/source/public/amsfonts/symbols
%dir %{_texdir}/texmf-dist/fonts/source/public/ar
%dir %{_texdir}/texmf-dist/fonts/source/public/arabtex
%dir %{_texdir}/texmf-dist/fonts/source/public/archaic
%dir %{_texdir}/texmf-dist/fonts/source/public/armenian
%dir %{_texdir}/texmf-dist/fonts/source/public/astro
%dir %{_texdir}/texmf-dist/fonts/source/public/aurical
%dir %{_texdir}/texmf-dist/fonts/source/public/bangtex
%dir %{_texdir}/texmf-dist/fonts/source/public/barcodes
%dir %{_texdir}/texmf-dist/fonts/source/public/bayer
%dir %{_texdir}/texmf-dist/fonts/source/public/bbding
%dir %{_texdir}/texmf-dist/fonts/source/public/bbm
%dir %{_texdir}/texmf-dist/fonts/source/public/bbold
%dir %{_texdir}/texmf-dist/fonts/source/public/boisik
%dir %{_texdir}/texmf-dist/fonts/source/public/bookhands
%dir %{_texdir}/texmf-dist/fonts/source/public/calligra
%dir %{_texdir}/texmf-dist/fonts/source/public/casyl
%dir %{_texdir}/texmf-dist/fonts/source/public/cbcoptic
%dir %{_texdir}/texmf-dist/fonts/source/public/cbfonts
%dir %{_texdir}/texmf-dist/fonts/source/public/cc-pl
%dir %{_texdir}/texmf-dist/fonts/source/public/chemarrow
%dir %{_texdir}/texmf-dist/fonts/source/public/chess
%dir %{_texdir}/texmf-dist/fonts/source/public/circ
%dir %{_texdir}/texmf-dist/fonts/source/public/clock
%dir %{_texdir}/texmf-dist/fonts/source/public/cm
%dir %{_texdir}/texmf-dist/fonts/source/public/cmbright
%dir %{_texdir}/texmf-dist/fonts/source/public/cmcyr
%dir %{_texdir}/texmf-dist/fonts/source/public/cmextra
%dir %{_texdir}/texmf-dist/fonts/source/public/cmll
%dir %{_texdir}/texmf-dist/fonts/source/public/cmpica
%dir %{_texdir}/texmf-dist/fonts/source/public/concmath-fonts
%dir %{_texdir}/texmf-dist/fonts/source/public/concrete
%dir %{_texdir}/texmf-dist/fonts/source/public/cryst
%dir %{_texdir}/texmf-dist/fonts/source/public/cs
%dir %{_texdir}/texmf-dist/fonts/source/public/ctib
%dir %{_texdir}/texmf-dist/fonts/source/public/dancers
%dir %{_texdir}/texmf-dist/fonts/source/public/dice
%dir %{_texdir}/texmf-dist/fonts/source/public/dingbat
%dir %{_texdir}/texmf-dist/fonts/source/public/doublestroke
%dir %{_texdir}/texmf-dist/fonts/source/public/dozenal
%dir %{_texdir}/texmf-dist/fonts/source/public/ean
%dir %{_texdir}/texmf-dist/fonts/source/public/ecc
%dir %{_texdir}/texmf-dist/fonts/source/public/eiad-ltx
%dir %{_texdir}/texmf-dist/fonts/source/public/elvish
%dir %{_texdir}/texmf-dist/fonts/source/public/esint
%dir %{_texdir}/texmf-dist/fonts/source/public/esvect
%dir %{_texdir}/texmf-dist/fonts/source/public/ethiop
%dir %{_texdir}/texmf-dist/fonts/source/public/euro-ce
%dir %{_texdir}/texmf-dist/fonts/source/public/eurosym
%dir %{_texdir}/texmf-dist/fonts/source/public/euxm
%dir %{_texdir}/texmf-dist/fonts/source/public/feyn
%dir %{_texdir}/texmf-dist/fonts/source/public/fge
%dir %{_texdir}/texmf-dist/fonts/source/public/frcursive
%dir %{_texdir}/texmf-dist/fonts/source/public/genealogy
%dir %{_texdir}/texmf-dist/fonts/source/public/go
%dir %{_texdir}/texmf-dist/fonts/source/public/gothic
%dir %{_texdir}/texmf-dist/fonts/source/public/greenpoint
%dir %{_texdir}/texmf-dist/fonts/source/public/hands
%dir %{_texdir}/texmf-dist/fonts/source/public/ibygrk
%dir %{_texdir}/texmf-dist/fonts/source/public/ifsym
%dir %{_texdir}/texmf-dist/fonts/source/public/itrans
%dir %{_texdir}/texmf-dist/fonts/source/public/jablantile
%dir %{_texdir}/texmf-dist/fonts/source/public/kdgreek
%dir %{_texdir}/texmf-dist/fonts/source/public/kixfont
%dir %{_texdir}/texmf-dist/fonts/source/public/knitting
%dir %{_texdir}/texmf-dist/fonts/source/public/knuthotherfonts
%dir %{_texdir}/texmf-dist/fonts/source/public/knuthotherfonts/committee
%dir %{_texdir}/texmf-dist/fonts/source/public/knuthotherfonts/halftone
%dir %{_texdir}/texmf-dist/fonts/source/public/knuthotherfonts/mfbook
%dir %{_texdir}/texmf-dist/fonts/source/public/kpfonts
%dir %{_texdir}/texmf-dist/fonts/source/public/latex-fonts
%dir %{_texdir}/texmf-dist/fonts/source/public/lfb
%dir %{_texdir}/texmf-dist/fonts/source/public/lxfonts
%dir %{_texdir}/texmf-dist/fonts/source/public/malayalam
%dir %{_texdir}/texmf-dist/fonts/source/public/malayalam/effects
%dir %{_texdir}/texmf-dist/fonts/source/public/malayalam/styles
%dir %{_texdir}/texmf-dist/fonts/source/public/mathabx
%dir %{_texdir}/texmf-dist/fonts/source/public/mflogo
%dir %{_texdir}/texmf-dist/fonts/source/public/misc
%dir %{_texdir}/texmf-dist/fonts/source/public/mnsymbol
%dir %{_texdir}/texmf-dist/fonts/source/public/montex
%dir %{_texdir}/texmf-dist/fonts/source/public/musixps
%dir %{_texdir}/texmf-dist/fonts/source/public/musixtex
%dir %{_texdir}/texmf-dist/fonts/source/public/niceframe
%dir %{_texdir}/texmf-dist/fonts/source/public/nkarta
%dir %{_texdir}/texmf-dist/fonts/source/public/ogham
%dir %{_texdir}/texmf-dist/fonts/source/public/oldlatin
%dir %{_texdir}/texmf-dist/fonts/source/public/orkhun
%dir %{_texdir}/texmf-dist/fonts/source/public/othello
%dir %{_texdir}/texmf-dist/fonts/source/public/otibet
%dir %{_texdir}/texmf-dist/fonts/source/public/pacioli
%dir %{_texdir}/texmf-dist/fonts/source/public/pigpen
%dir %{_texdir}/texmf-dist/fonts/source/public/pl
%dir %{_texdir}/texmf-dist/fonts/source/public/punk
%dir %{_texdir}/texmf-dist/fonts/source/public/recycle
%dir %{_texdir}/texmf-dist/fonts/source/public/rsfs
%dir %{_texdir}/texmf-dist/fonts/source/public/sanskrit
%dir %{_texdir}/texmf-dist/fonts/source/public/sauter
%dir %{_texdir}/texmf-dist/fonts/source/public/semaphor
%dir %{_texdir}/texmf-dist/fonts/source/public/semaphor/metafont
%dir %{_texdir}/texmf-dist/fonts/source/public/shuffle
%dir %{_texdir}/texmf-dist/fonts/source/public/skak
%dir %{_texdir}/texmf-dist/fonts/source/public/skull
%dir %{_texdir}/texmf-dist/fonts/source/public/stmaryrd
%dir %{_texdir}/texmf-dist/fonts/source/public/tapir
%dir %{_texdir}/texmf-dist/fonts/source/public/tipa
%dir %{_texdir}/texmf-dist/fonts/source/public/trsym
%dir %{_texdir}/texmf-dist/fonts/source/public/universa
%dir %{_texdir}/texmf-dist/fonts/source/public/velthuis
%dir %{_texdir}/texmf-dist/fonts/source/public/wasy
%dir %{_texdir}/texmf-dist/fonts/source/public/wnri
%dir %{_texdir}/texmf-dist/fonts/source/public/wsuipa
%dir %{_texdir}/texmf-dist/fonts/source/public/xbmc
%dir %{_texdir}/texmf-dist/fonts/source/public/xq
%dir %{_texdir}/texmf-dist/fonts/source/public/xypic
%dir %{_texdir}/texmf-dist/fonts/source/public/yhmath
%dir %{_texdir}/texmf-dist/fonts/source/vntex
%dir %{_texdir}/texmf-dist/fonts/source/vntex/vnr
%dir %{_texdir}/texmf-dist/fonts/tfm
%dir %{_texdir}/texmf-dist/fonts/tfm/adobe
%dir %{_texdir}/texmf-dist/fonts/tfm/adobe/avantgar
%dir %{_texdir}/texmf-dist/fonts/tfm/adobe/bookman
%dir %{_texdir}/texmf-dist/fonts/tfm/adobe/courier
%dir %{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic
%dir %{_texdir}/texmf-dist/fonts/tfm/adobe/ly1
%dir %{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk
%dir %{_texdir}/texmf-dist/fonts/tfm/adobe/palatino
%dir %{_texdir}/texmf-dist/fonts/tfm/adobe/symbol
%dir %{_texdir}/texmf-dist/fonts/tfm/adobe/times
%dir %{_texdir}/texmf-dist/fonts/tfm/adobe/utopia
%dir %{_texdir}/texmf-dist/fonts/tfm/adobe/zapfchan
%dir %{_texdir}/texmf-dist/fonts/tfm/adobe/zapfding
%dir %{_texdir}/texmf-dist/fonts/tfm/arabi
%dir %{_texdir}/texmf-dist/fonts/tfm/arabi/arabeyes
%dir %{_texdir}/texmf-dist/fonts/tfm/arabi/farsiweb
%dir %{_texdir}/texmf-dist/fonts/tfm/arkandis
%dir %{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald
%dir %{_texdir}/texmf-dist/fonts/tfm/arkandis/libris
%dir %{_texdir}/texmf-dist/fonts/tfm/arkandis/romande
%dir %{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis
%dir %{_texdir}/texmf-dist/fonts/tfm/arkandis/venturis2
%dir %{_texdir}/texmf-dist/fonts/tfm/arkandis/venturisold
%dir %{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans
%dir %{_texdir}/texmf-dist/fonts/tfm/arkandis/venturissans2
%dir %{_texdir}/texmf-dist/fonts/tfm/arphic
%dir %{_texdir}/texmf-dist/fonts/tfm/arphic/bkaimp
%dir %{_texdir}/texmf-dist/fonts/tfm/arphic/bkaiu
%dir %{_texdir}/texmf-dist/fonts/tfm/arphic/bsmilp
%dir %{_texdir}/texmf-dist/fonts/tfm/arphic/bsmiu
%dir %{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnlp
%dir %{_texdir}/texmf-dist/fonts/tfm/arphic/gbsnu
%dir %{_texdir}/texmf-dist/fonts/tfm/arphic/gkaimp
%dir %{_texdir}/texmf-dist/fonts/tfm/arphic/gkaiu
%dir %{_texdir}/texmf-dist/fonts/tfm/bitstrea
%dir %{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter
%dir %{_texdir}/texmf-dist/fonts/tfm/cg
%dir %{_texdir}/texmf-dist/fonts/tfm/cg/courier
%dir %{_texdir}/texmf-dist/fonts/tfm/cg/times
%dir %{_texdir}/texmf-dist/fonts/tfm/cns
%dir %{_texdir}/texmf-dist/fonts/tfm/cns/c0so12
%dir %{_texdir}/texmf-dist/fonts/tfm/cns/c1so12
%dir %{_texdir}/texmf-dist/fonts/tfm/cns/c2so12
%dir %{_texdir}/texmf-dist/fonts/tfm/cns/c3so12
%dir %{_texdir}/texmf-dist/fonts/tfm/cns/c4so12
%dir %{_texdir}/texmf-dist/fonts/tfm/cns/c5so12
%dir %{_texdir}/texmf-dist/fonts/tfm/cns/c6so12
%dir %{_texdir}/texmf-dist/fonts/tfm/cns/c7so12
%dir %{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe
%dir %{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/avantgar
%dir %{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/bookman
%dir %{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/courier
%dir %{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/helvetic
%dir %{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/ncntrsbk
%dir %{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/palatino
%dir %{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/symbol
%dir %{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/times
%dir %{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/zapfchan
%dir %{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/zapfding
%dir %{_texdir}/texmf-dist/fonts/tfm/groff
%dir %{_texdir}/texmf-dist/fonts/tfm/groff/avantgar
%dir %{_texdir}/texmf-dist/fonts/tfm/groff/bookman
%dir %{_texdir}/texmf-dist/fonts/tfm/groff/courier
%dir %{_texdir}/texmf-dist/fonts/tfm/groff/helvetic
%dir %{_texdir}/texmf-dist/fonts/tfm/groff/ncntrsbk
%dir %{_texdir}/texmf-dist/fonts/tfm/groff/palatino
%dir %{_texdir}/texmf-dist/fonts/tfm/groff/times
%dir %{_texdir}/texmf-dist/fonts/tfm/groff/zapfchan
%dir %{_texdir}/texmf-dist/fonts/tfm/hoekwater
%dir %{_texdir}/texmf-dist/fonts/tfm/hoekwater/context
%dir %{_texdir}/texmf-dist/fonts/tfm/jknappen
%dir %{_texdir}/texmf-dist/fonts/tfm/jknappen/ec
%dir %{_texdir}/texmf-dist/fonts/tfm/jknappen/fc
%dir %{_texdir}/texmf-dist/fonts/tfm/jmn
%dir %{_texdir}/texmf-dist/fonts/tfm/jmn/hans
%dir %{_texdir}/texmf-dist/fonts/tfm/mathdesign
%dir %{_texdir}/texmf-dist/fonts/tfm/mathdesign/mdbch
%dir %{_texdir}/texmf-dist/fonts/tfm/mathdesign/mdput
%dir %{_texdir}/texmf-dist/fonts/tfm/mathdesign/mdugm
%dir %{_texdir}/texmf-dist/fonts/tfm/monotype
%dir %{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic
%dir %{_texdir}/texmf-dist/fonts/tfm/monotype/symbol
%dir %{_texdir}/texmf-dist/fonts/tfm/ptex
%dir %{_texdir}/texmf-dist/fonts/tfm/ptex/ascgrp
%dir %{_texdir}/texmf-dist/fonts/tfm/ptex/dvips
%dir %{_texdir}/texmf-dist/fonts/tfm/ptex/jis
%dir %{_texdir}/texmf-dist/fonts/tfm/ptex/morisawa
%dir %{_texdir}/texmf-dist/fonts/tfm/ptex/nmin-ngoth
%dir %{_texdir}/texmf-dist/fonts/tfm/ptex/standard
%dir %{_texdir}/texmf-dist/fonts/tfm/public
%dir %{_texdir}/texmf-dist/fonts/tfm/public/ae
%dir %{_texdir}/texmf-dist/fonts/tfm/public/allrunes
%dir %{_texdir}/texmf-dist/fonts/tfm/public/amsfonts
%dir %{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra
%dir %{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic
%dir %{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/dummy
%dir %{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/euler
%dir %{_texdir}/texmf-dist/fonts/tfm/public/amsfonts/symbols
%dir %{_texdir}/texmf-dist/fonts/tfm/public/antp
%dir %{_texdir}/texmf-dist/fonts/tfm/public/antt
%dir %{_texdir}/texmf-dist/fonts/tfm/public/ar
%dir %{_texdir}/texmf-dist/fonts/tfm/public/arabtex
%dir %{_texdir}/texmf-dist/fonts/tfm/public/archaic
%dir %{_texdir}/texmf-dist/fonts/tfm/public/arev
%dir %{_texdir}/texmf-dist/fonts/tfm/public/armenian
%dir %{_texdir}/texmf-dist/fonts/tfm/public/ascii
%dir %{_texdir}/texmf-dist/fonts/tfm/public/astro
%dir %{_texdir}/texmf-dist/fonts/tfm/public/augie
%dir %{_texdir}/texmf-dist/fonts/tfm/public/auncial-new
%dir %{_texdir}/texmf-dist/fonts/tfm/public/aurical
%dir %{_texdir}/texmf-dist/fonts/tfm/public/bangtex
%dir %{_texdir}/texmf-dist/fonts/tfm/public/barcodes
%dir %{_texdir}/texmf-dist/fonts/tfm/public/bayer
%dir %{_texdir}/texmf-dist/fonts/tfm/public/bbding
%dir %{_texdir}/texmf-dist/fonts/tfm/public/bbm
%dir %{_texdir}/texmf-dist/fonts/tfm/public/bbold
%dir %{_texdir}/texmf-dist/fonts/tfm/public/bera
%dir %{_texdir}/texmf-dist/fonts/tfm/public/bgreek
%dir %{_texdir}/texmf-dist/fonts/tfm/public/blacklettert1
%dir %{_texdir}/texmf-dist/fonts/tfm/public/boisik
%dir %{_texdir}/texmf-dist/fonts/tfm/public/brushscr
%dir %{_texdir}/texmf-dist/fonts/tfm/public/burmese
%dir %{_texdir}/texmf-dist/fonts/tfm/public/calligra
%dir %{_texdir}/texmf-dist/fonts/tfm/public/casyl
%dir %{_texdir}/texmf-dist/fonts/tfm/public/cbcoptic
%dir %{_texdir}/texmf-dist/fonts/tfm/public/cbfonts
%dir %{_texdir}/texmf-dist/fonts/tfm/public/ccicons
%dir %{_texdir}/texmf-dist/fonts/tfm/public/cc-pl
%dir %{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm
%dir %{_texdir}/texmf-dist/fonts/tfm/public/chemarrow
%dir %{_texdir}/texmf-dist/fonts/tfm/public/circ
%dir %{_texdir}/texmf-dist/fonts/tfm/public/cjhebrew
%dir %{_texdir}/texmf-dist/fonts/tfm/public/clock
%dir %{_texdir}/texmf-dist/fonts/tfm/public/cm
%dir %{_texdir}/texmf-dist/fonts/tfm/public/cmbright
%dir %{_texdir}/texmf-dist/fonts/tfm/public/cmcyr
%dir %{_texdir}/texmf-dist/fonts/tfm/public/cmextra
%dir %{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc
%dir %{_texdir}/texmf-dist/fonts/tfm/public/cmll
%dir %{_texdir}/texmf-dist/fonts/tfm/public/cmpica
%dir %{_texdir}/texmf-dist/fonts/tfm/public/concmath-fonts
%dir %{_texdir}/texmf-dist/fonts/tfm/public/concrete
%dir %{_texdir}/texmf-dist/fonts/tfm/public/cryst
%dir %{_texdir}/texmf-dist/fonts/tfm/public/cs
%dir %{_texdir}/texmf-dist/fonts/tfm/public/ctib
%dir %{_texdir}/texmf-dist/fonts/tfm/public/cyklop
%dir %{_texdir}/texmf-dist/fonts/tfm/public/dancers
%dir %{_texdir}/texmf-dist/fonts/tfm/public/dice
%dir %{_texdir}/texmf-dist/fonts/tfm/public/dictsym
%dir %{_texdir}/texmf-dist/fonts/tfm/public/dingbat
%dir %{_texdir}/texmf-dist/fonts/tfm/public/doublestroke
%dir %{_texdir}/texmf-dist/fonts/tfm/public/dozenal
%dir %{_texdir}/texmf-dist/fonts/tfm/public/ean
%dir %{_texdir}/texmf-dist/fonts/tfm/public/ecc
%dir %{_texdir}/texmf-dist/fonts/tfm/public/eco
%dir %{_texdir}/texmf-dist/fonts/tfm/public/elvish
%dir %{_texdir}/texmf-dist/fonts/tfm/public/epigrafica
%dir %{_texdir}/texmf-dist/fonts/tfm/public/epiolmec
%dir %{_texdir}/texmf-dist/fonts/tfm/public/esint
%dir %{_texdir}/texmf-dist/fonts/tfm/public/esvect
%dir %{_texdir}/texmf-dist/fonts/tfm/public/ethiop
%dir %{_texdir}/texmf-dist/fonts/tfm/public/eulervm
%dir %{_texdir}/texmf-dist/fonts/tfm/public/euro-ce
%dir %{_texdir}/texmf-dist/fonts/tfm/public/eurosym
%dir %{_texdir}/texmf-dist/fonts/tfm/public/euxm
%dir %{_texdir}/texmf-dist/fonts/tfm/public/feyn
%dir %{_texdir}/texmf-dist/fonts/tfm/public/fge
%dir %{_texdir}/texmf-dist/fonts/tfm/public/figbas
%dir %{_texdir}/texmf-dist/fonts/tfm/public/foekfont
%dir %{_texdir}/texmf-dist/fonts/tfm/public/fonetika
%dir %{_texdir}/texmf-dist/fonts/tfm/public/fourier
%dir %{_texdir}/texmf-dist/fonts/tfm/public/fouriernc
%dir %{_texdir}/texmf-dist/fonts/tfm/public/frcursive
%dir %{_texdir}/texmf-dist/fonts/tfm/public/garuda-c90
%dir %{_texdir}/texmf-dist/fonts/tfm/public/genealogy
%dir %{_texdir}/texmf-dist/fonts/tfm/public/gentium
%dir %{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia
%dir %{_texdir}/texmf-dist/fonts/tfm/public/gfsbaskerville
%dir %{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni
%dir %{_texdir}/texmf-dist/fonts/tfm/public/gfscomplutum
%dir %{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot
%dir %{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic
%dir %{_texdir}/texmf-dist/fonts/tfm/public/gfsporson
%dir %{_texdir}/texmf-dist/fonts/tfm/public/gfssolomos
%dir %{_texdir}/texmf-dist/fonts/tfm/public/go
%dir %{_texdir}/texmf-dist/fonts/tfm/public/gothic
%dir %{_texdir}/texmf-dist/fonts/tfm/public/greenpoint
%dir %{_texdir}/texmf-dist/fonts/tfm/public/grverb
%dir %{_texdir}/texmf-dist/fonts/tfm/public/hands
%dir %{_texdir}/texmf-dist/fonts/tfm/public/hfoldsty
%dir %{_texdir}/texmf-dist/fonts/tfm/public/ibygrk
%dir %{_texdir}/texmf-dist/fonts/tfm/public/ifsym
%dir %{_texdir}/texmf-dist/fonts/tfm/public/inconsolata
%dir %{_texdir}/texmf-dist/fonts/tfm/public/initials
%dir %{_texdir}/texmf-dist/fonts/tfm/public/itrans
%dir %{_texdir}/texmf-dist/fonts/tfm/public/iwona
%dir %{_texdir}/texmf-dist/fonts/tfm/public/kdgreek
%dir %{_texdir}/texmf-dist/fonts/tfm/public/kerkis
%dir %{_texdir}/texmf-dist/fonts/tfm/public/kixfont
%dir %{_texdir}/texmf-dist/fonts/tfm/public/knitting
%dir %{_texdir}/texmf-dist/fonts/tfm/public/kpfonts
%dir %{_texdir}/texmf-dist/fonts/tfm/public/kurier
%dir %{_texdir}/texmf-dist/fonts/tfm/public/latex-fonts
%dir %{_texdir}/texmf-dist/fonts/tfm/public/lfb
%dir %{_texdir}/texmf-dist/fonts/tfm/public/libertine
%dir %{_texdir}/texmf-dist/fonts/tfm/public/linearA
%dir %{_texdir}/texmf-dist/fonts/tfm/public/lithuanian
%dir %{_texdir}/texmf-dist/fonts/tfm/public/lm
%dir %{_texdir}/texmf-dist/fonts/tfm/public/lxfonts
%dir %{_texdir}/texmf-dist/fonts/tfm/public/malayalam
%dir %{_texdir}/texmf-dist/fonts/tfm/public/marvosym
%dir %{_texdir}/texmf-dist/fonts/tfm/public/mathabx
%dir %{_texdir}/texmf-dist/fonts/tfm/public/mathpazo
%dir %{_texdir}/texmf-dist/fonts/tfm/public/mflogo
%dir %{_texdir}/texmf-dist/fonts/tfm/public/misc
%dir %{_texdir}/texmf-dist/fonts/tfm/public/mnsymbol
%dir %{_texdir}/texmf-dist/fonts/tfm/public/montex
%dir %{_texdir}/texmf-dist/fonts/tfm/public/musixps
%dir %{_texdir}/texmf-dist/fonts/tfm/public/musixtex
%dir %{_texdir}/texmf-dist/fonts/tfm/public/niceframe
%dir %{_texdir}/texmf-dist/fonts/tfm/public/nkarta
%dir %{_texdir}/texmf-dist/fonts/tfm/public/norasi-c90
%dir %{_texdir}/texmf-dist/fonts/tfm/public/ocherokee
%dir %{_texdir}/texmf-dist/fonts/tfm/public/ogham
%dir %{_texdir}/texmf-dist/fonts/tfm/public/oinuit
%dir %{_texdir}/texmf-dist/fonts/tfm/public/oldlatin
%dir %{_texdir}/texmf-dist/fonts/tfm/public/omega
%dir %{_texdir}/texmf-dist/fonts/tfm/public/orkhun
%dir %{_texdir}/texmf-dist/fonts/tfm/public/othello
%dir %{_texdir}/texmf-dist/fonts/tfm/public/otibet
%dir %{_texdir}/texmf-dist/fonts/tfm/public/pacioli
%dir %{_texdir}/texmf-dist/fonts/tfm/public/phaistos
%dir %{_texdir}/texmf-dist/fonts/tfm/public/pigpen
%dir %{_texdir}/texmf-dist/fonts/tfm/public/pl
%dir %{_texdir}/texmf-dist/fonts/tfm/public/pslatex
%dir %{_texdir}/texmf-dist/fonts/tfm/public/punk
%dir %{_texdir}/texmf-dist/fonts/tfm/public/pxfonts
%dir %{_texdir}/texmf-dist/fonts/tfm/public/qpxqtx
%dir %{_texdir}/texmf-dist/fonts/tfm/public/recycle
%dir %{_texdir}/texmf-dist/fonts/tfm/public/rsfs
%dir %{_texdir}/texmf-dist/fonts/tfm/public/sanskrit
%dir %{_texdir}/texmf-dist/fonts/tfm/public/semaphor
%dir %{_texdir}/texmf-dist/fonts/tfm/public/shuffle
%dir %{_texdir}/texmf-dist/fonts/tfm/public/skak
%dir %{_texdir}/texmf-dist/fonts/tfm/public/skaknew
%dir %{_texdir}/texmf-dist/fonts/tfm/public/staves
%dir %{_texdir}/texmf-dist/fonts/tfm/public/stmaryrd
%dir %{_texdir}/texmf-dist/fonts/tfm/public/tabvar
%dir %{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript
%dir %{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre
%dir %{_texdir}/texmf-dist/fonts/tfm/public/tipa
%dir %{_texdir}/texmf-dist/fonts/tfm/public/trajan
%dir %{_texdir}/texmf-dist/fonts/tfm/public/trsym
%dir %{_texdir}/texmf-dist/fonts/tfm/public/txfonts
%dir %{_texdir}/texmf-dist/fonts/tfm/public/txfontsb
%dir %{_texdir}/texmf-dist/fonts/tfm/public/universa
%dir %{_texdir}/texmf-dist/fonts/tfm/public/velthuis
%dir %{_texdir}/texmf-dist/fonts/tfm/public/wasy
%dir %{_texdir}/texmf-dist/fonts/tfm/public/wnri
%dir %{_texdir}/texmf-dist/fonts/tfm/public/wsuipa
%dir %{_texdir}/texmf-dist/fonts/tfm/public/xbmc
%dir %{_texdir}/texmf-dist/fonts/tfm/public/xq
%dir %{_texdir}/texmf-dist/fonts/tfm/public/xypic
%dir %{_texdir}/texmf-dist/fonts/tfm/public/yhmath
%dir %{_texdir}/texmf-dist/fonts/tfm/uhc
%dir %{_texdir}/texmf-dist/fonts/tfm/uhc/umj
%dir %{_texdir}/texmf-dist/fonts/tfm/uhc/uwmj
%dir %{_texdir}/texmf-dist/fonts/tfm/uhc/wmj
%dir %{_texdir}/texmf-dist/fonts/tfm/urw
%dir %{_texdir}/texmf-dist/fonts/tfm/urw35vf
%dir %{_texdir}/texmf-dist/fonts/tfm/urw35vf/avantgar
%dir %{_texdir}/texmf-dist/fonts/tfm/urw35vf/bookman
%dir %{_texdir}/texmf-dist/fonts/tfm/urw35vf/courier
%dir %{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic
%dir %{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk
%dir %{_texdir}/texmf-dist/fonts/tfm/urw35vf/palatino
%dir %{_texdir}/texmf-dist/fonts/tfm/urw35vf/symbol
%dir %{_texdir}/texmf-dist/fonts/tfm/urw35vf/times
%dir %{_texdir}/texmf-dist/fonts/tfm/urw35vf/zapfchan
%dir %{_texdir}/texmf-dist/fonts/tfm/urw35vf/zapfding
%dir %{_texdir}/texmf-dist/fonts/tfm/urw/antiqua
%dir %{_texdir}/texmf-dist/fonts/tfm/urw/grotesq
%dir %{_texdir}/texmf-dist/fonts/tfm/vntex
%dir %{_texdir}/texmf-dist/fonts/tfm/vntex/arevvn
%dir %{_texdir}/texmf-dist/fonts/tfm/vntex/chartervn
%dir %{_texdir}/texmf-dist/fonts/tfm/vntex/cmbrightvn
%dir %{_texdir}/texmf-dist/fonts/tfm/vntex/concretevn
%dir %{_texdir}/texmf-dist/fonts/tfm/vntex/grotesqvn
%dir %{_texdir}/texmf-dist/fonts/tfm/vntex/txttvn
%dir %{_texdir}/texmf-dist/fonts/tfm/vntex/urwvn
%dir %{_texdir}/texmf-dist/fonts/tfm/vntex/vnr
%dir %{_texdir}/texmf-dist/fonts/tfm/vntex/vntopia
%dir %{_texdir}/texmf-dist/fonts/tfm/zhmetrics
%dir %{_texdir}/texmf-dist/fonts/tfm/zhmetrics/cyberb
%dir %{_texdir}/texmf-dist/fonts/tfm/zhmetrics/gbk
%dir %{_texdir}/texmf-dist/fonts/tfm/zhmetrics/gbkfs
%dir %{_texdir}/texmf-dist/fonts/tfm/zhmetrics/gbkhei
%dir %{_texdir}/texmf-dist/fonts/tfm/zhmetrics/gbkkai
%dir %{_texdir}/texmf-dist/fonts/tfm/zhmetrics/gbkli
%dir %{_texdir}/texmf-dist/fonts/tfm/zhmetrics/gbksong
%dir %{_texdir}/texmf-dist/fonts/tfm/zhmetrics/gbkyou
%dir %{_texdir}/texmf-dist/fonts/tfm/zhmetrics/unifs
%dir %{_texdir}/texmf-dist/fonts/tfm/zhmetrics/unihei
%dir %{_texdir}/texmf-dist/fonts/tfm/zhmetrics/unikai
%dir %{_texdir}/texmf-dist/fonts/tfm/zhmetrics/unili
%dir %{_texdir}/texmf-dist/fonts/tfm/zhmetrics/unisong
%dir %{_texdir}/texmf-dist/fonts/tfm/zhmetrics/uniyou
%dir %{_texdir}/texmf-dist/fonts/truetype
%dir %{_texdir}/texmf-dist/fonts/truetype/hoekwater
%dir %{_texdir}/texmf-dist/fonts/truetype/hoekwater/lmextra
%dir %{_texdir}/texmf-dist/fonts/truetype/public
%dir %{_texdir}/texmf-dist/fonts/truetype/public/Asana-Math
%dir %{_texdir}/texmf-dist/fonts/truetype/public/belleek
%dir %{_texdir}/texmf-dist/fonts/truetype/public/gentium
%dir %{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont
%dir %{_texdir}/texmf-dist/fonts/truetype/public/itrans
%dir %{_texdir}/texmf-dist/fonts/truetype/public/junicode
%dir %{_texdir}/texmf-dist/fonts/type1
%dir %{_texdir}/texmf-dist/fonts/type1/adobe
%dir %{_texdir}/texmf-dist/fonts/type1/adobe/courier
%dir %{_texdir}/texmf-dist/fonts/type1/adobe/utopia
%dir %{_texdir}/texmf-dist/fonts/type1/arabi
%dir %{_texdir}/texmf-dist/fonts/type1/arabi/arabeyes
%dir %{_texdir}/texmf-dist/fonts/type1/arabi/farsiweb
%dir %{_texdir}/texmf-dist/fonts/type1/arkandis
%dir %{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald
%dir %{_texdir}/texmf-dist/fonts/type1/arkandis/libris
%dir %{_texdir}/texmf-dist/fonts/type1/arkandis/romande
%dir %{_texdir}/texmf-dist/fonts/type1/arkandis/venturis
%dir %{_texdir}/texmf-dist/fonts/type1/arkandis/venturis2
%dir %{_texdir}/texmf-dist/fonts/type1/arkandis/venturisold
%dir %{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans
%dir %{_texdir}/texmf-dist/fonts/type1/arkandis/venturissans2
%dir %{_texdir}/texmf-dist/fonts/type1/arphic
%dir %{_texdir}/texmf-dist/fonts/type1/arphic/bkaiu
%dir %{_texdir}/texmf-dist/fonts/type1/arphic/bsmiu
%dir %{_texdir}/texmf-dist/fonts/type1/arphic/gbsnu
%dir %{_texdir}/texmf-dist/fonts/type1/arphic/gkaiu
%dir %{_texdir}/texmf-dist/fonts/type1/bitstrea
%dir %{_texdir}/texmf-dist/fonts/type1/bitstrea/charter
%dir %{_texdir}/texmf-dist/fonts/type1/groff
%dir %{_texdir}/texmf-dist/fonts/type1/hoekwater
%dir %{_texdir}/texmf-dist/fonts/type1/hoekwater/context
%dir %{_texdir}/texmf-dist/fonts/type1/hoekwater/manfnt
%dir %{_texdir}/texmf-dist/fonts/type1/hoekwater/mflogo
%dir %{_texdir}/texmf-dist/fonts/type1/hoekwater/stmaryrd
%dir %{_texdir}/texmf-dist/fonts/type1/jmn
%dir %{_texdir}/texmf-dist/fonts/type1/jmn/hans
%dir %{_texdir}/texmf-dist/fonts/type1/mathdesign
%dir %{_texdir}/texmf-dist/fonts/type1/mathdesign/mdbch
%dir %{_texdir}/texmf-dist/fonts/type1/mathdesign/mdput
%dir %{_texdir}/texmf-dist/fonts/type1/mathdesign/mdugm
%dir %{_texdir}/texmf-dist/fonts/type1/ptex
%dir %{_texdir}/texmf-dist/fonts/type1/ptex/ascgrp
%dir %{_texdir}/texmf-dist/fonts/type1/public
%dir %{_texdir}/texmf-dist/fonts/type1/public/allrunes
%dir %{_texdir}/texmf-dist/fonts/type1/public/amsfonts
%dir %{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cm
%dir %{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cmextra
%dir %{_texdir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic
%dir %{_texdir}/texmf-dist/fonts/type1/public/amsfonts/euler
%dir %{_texdir}/texmf-dist/fonts/type1/public/amsfonts/latxfont
%dir %{_texdir}/texmf-dist/fonts/type1/public/amsfonts/symbols
%dir %{_texdir}/texmf-dist/fonts/type1/public/antp
%dir %{_texdir}/texmf-dist/fonts/type1/public/antt
%dir %{_texdir}/texmf-dist/fonts/type1/public/arabtex
%dir %{_texdir}/texmf-dist/fonts/type1/public/archaic
%dir %{_texdir}/texmf-dist/fonts/type1/public/arev
%dir %{_texdir}/texmf-dist/fonts/type1/public/ascii
%dir %{_texdir}/texmf-dist/fonts/type1/public/augie
%dir %{_texdir}/texmf-dist/fonts/type1/public/auncial-new
%dir %{_texdir}/texmf-dist/fonts/type1/public/aurical
%dir %{_texdir}/texmf-dist/fonts/type1/public/belleek
%dir %{_texdir}/texmf-dist/fonts/type1/public/bera
%dir %{_texdir}/texmf-dist/fonts/type1/public/brushscr
%dir %{_texdir}/texmf-dist/fonts/type1/public/burmese
%dir %{_texdir}/texmf-dist/fonts/type1/public/carolmin-ps
%dir %{_texdir}/texmf-dist/fonts/type1/public/cbcoptic
%dir %{_texdir}/texmf-dist/fonts/type1/public/cbfonts
%dir %{_texdir}/texmf-dist/fonts/type1/public/ccicons
%dir %{_texdir}/texmf-dist/fonts/type1/public/cc-pl
%dir %{_texdir}/texmf-dist/fonts/type1/public/chemarrow
%dir %{_texdir}/texmf-dist/fonts/type1/public/cjhebrew
%dir %{_texdir}/texmf-dist/fonts/type1/public/cmcyr
%dir %{_texdir}/texmf-dist/fonts/type1/public/cm-lgc
%dir %{_texdir}/texmf-dist/fonts/type1/public/cmll
%dir %{_texdir}/texmf-dist/fonts/type1/public/cm-super
%dir %{_texdir}/texmf-dist/fonts/type1/public/cm-unicode
%dir %{_texdir}/texmf-dist/fonts/type1/public/cryst
%dir %{_texdir}/texmf-dist/fonts/type1/public/cs
%dir %{_texdir}/texmf-dist/fonts/type1/public/cyklop
%dir %{_texdir}/texmf-dist/fonts/type1/public/dictsym
%dir %{_texdir}/texmf-dist/fonts/type1/public/doublestroke
%dir %{_texdir}/texmf-dist/fonts/type1/public/dozenal
%dir %{_texdir}/texmf-dist/fonts/type1/public/epigrafica
%dir %{_texdir}/texmf-dist/fonts/type1/public/epiolmec
%dir %{_texdir}/texmf-dist/fonts/type1/public/esint-type1
%dir %{_texdir}/texmf-dist/fonts/type1/public/esvect
%dir %{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1
%dir %{_texdir}/texmf-dist/fonts/type1/public/eurosym
%dir %{_texdir}/texmf-dist/fonts/type1/public/fge
%dir %{_texdir}/texmf-dist/fonts/type1/public/figbas
%dir %{_texdir}/texmf-dist/fonts/type1/public/foekfont
%dir %{_texdir}/texmf-dist/fonts/type1/public/fonetika
%dir %{_texdir}/texmf-dist/fonts/type1/public/fourier
%dir %{_texdir}/texmf-dist/fonts/type1/public/fpl
%dir %{_texdir}/texmf-dist/fonts/type1/public/gfsartemisia
%dir %{_texdir}/texmf-dist/fonts/type1/public/gfsbaskerville
%dir %{_texdir}/texmf-dist/fonts/type1/public/gfsbodoni
%dir %{_texdir}/texmf-dist/fonts/type1/public/gfscomplutum
%dir %{_texdir}/texmf-dist/fonts/type1/public/gfsdidot
%dir %{_texdir}/texmf-dist/fonts/type1/public/gfsneohellenic
%dir %{_texdir}/texmf-dist/fonts/type1/public/gfsporson
%dir %{_texdir}/texmf-dist/fonts/type1/public/gfssolomos
%dir %{_texdir}/texmf-dist/fonts/type1/public/gothic
%dir %{_texdir}/texmf-dist/fonts/type1/public/grverb
%dir %{_texdir}/texmf-dist/fonts/type1/public/hfbright
%dir %{_texdir}/texmf-dist/fonts/type1/public/ibygrk
%dir %{_texdir}/texmf-dist/fonts/type1/public/inconsolata
%dir %{_texdir}/texmf-dist/fonts/type1/public/initials
%dir %{_texdir}/texmf-dist/fonts/type1/public/itrans
%dir %{_texdir}/texmf-dist/fonts/type1/public/iwona
%dir %{_texdir}/texmf-dist/fonts/type1/public/kerkis
%dir %{_texdir}/texmf-dist/fonts/type1/public/knitting
%dir %{_texdir}/texmf-dist/fonts/type1/public/kpfonts
%dir %{_texdir}/texmf-dist/fonts/type1/public/kurier
%dir %{_texdir}/texmf-dist/fonts/type1/public/libertine
%dir %{_texdir}/texmf-dist/fonts/type1/public/linearA
%dir %{_texdir}/texmf-dist/fonts/type1/public/lm
%dir %{_texdir}/texmf-dist/fonts/type1/public/lxfonts
%dir %{_texdir}/texmf-dist/fonts/type1/public/marvosym
%dir %{_texdir}/texmf-dist/fonts/type1/public/mathpazo
%dir %{_texdir}/texmf-dist/fonts/type1/public/mnsymbol
%dir %{_texdir}/texmf-dist/fonts/type1/public/montex
%dir %{_texdir}/texmf-dist/fonts/type1/public/musixtex
%dir %{_texdir}/texmf-dist/fonts/type1/public/ocherokee
%dir %{_texdir}/texmf-dist/fonts/type1/public/oinuit
%dir %{_texdir}/texmf-dist/fonts/type1/public/omega
%dir %{_texdir}/texmf-dist/fonts/type1/public/phaistos
%dir %{_texdir}/texmf-dist/fonts/type1/public/pigpen
%dir %{_texdir}/texmf-dist/fonts/type1/public/pl
%dir %{_texdir}/texmf-dist/fonts/type1/public/pxfonts
%dir %{_texdir}/texmf-dist/fonts/type1/public/recycle
%dir %{_texdir}/texmf-dist/fonts/type1/public/rsfs
%dir %{_texdir}/texmf-dist/fonts/type1/public/sanskrit
%dir %{_texdir}/texmf-dist/fonts/type1/public/semaphor
%dir %{_texdir}/texmf-dist/fonts/type1/public/skaknew
%dir %{_texdir}/texmf-dist/fonts/type1/public/staves
%dir %{_texdir}/texmf-dist/fonts/type1/public/tabvar
%dir %{_texdir}/texmf-dist/fonts/type1/public/tapir
%dir %{_texdir}/texmf-dist/fonts/type1/public/tex-gyre
%dir %{_texdir}/texmf-dist/fonts/type1/public/thailatex
%dir %{_texdir}/texmf-dist/fonts/type1/public/tipa
%dir %{_texdir}/texmf-dist/fonts/type1/public/trajan
%dir %{_texdir}/texmf-dist/fonts/type1/public/txfonts
%dir %{_texdir}/texmf-dist/fonts/type1/public/txfontsb
%dir %{_texdir}/texmf-dist/fonts/type1/public/velthuis
%dir %{_texdir}/texmf-dist/fonts/type1/public/wasy
%dir %{_texdir}/texmf-dist/fonts/type1/public/xypic
%dir %{_texdir}/texmf-dist/fonts/type1/public/yhmath
%dir %{_texdir}/texmf-dist/fonts/type1/uhc
%dir %{_texdir}/texmf-dist/fonts/type1/uhc/umj
%dir %{_texdir}/texmf-dist/fonts/type1/urw
%dir %{_texdir}/texmf-dist/fonts/type1/urw/antiqua
%dir %{_texdir}/texmf-dist/fonts/type1/urw/avantgar
%dir %{_texdir}/texmf-dist/fonts/type1/urw/bookman
%dir %{_texdir}/texmf-dist/fonts/type1/urw/courier
%dir %{_texdir}/texmf-dist/fonts/type1/urw/grotesq
%dir %{_texdir}/texmf-dist/fonts/type1/urw/helvetic
%dir %{_texdir}/texmf-dist/fonts/type1/urw/ncntrsbk
%dir %{_texdir}/texmf-dist/fonts/type1/urw/palatino
%dir %{_texdir}/texmf-dist/fonts/type1/urw/symbol
%dir %{_texdir}/texmf-dist/fonts/type1/urw/times
%dir %{_texdir}/texmf-dist/fonts/type1/urw/zapfchan
%dir %{_texdir}/texmf-dist/fonts/type1/urw/zapfding
%dir %{_texdir}/texmf-dist/fonts/type1/vntex
%dir %{_texdir}/texmf-dist/fonts/type1/vntex/arevvn
%dir %{_texdir}/texmf-dist/fonts/type1/vntex/chartervn
%dir %{_texdir}/texmf-dist/fonts/type1/vntex/cmbrightvn
%dir %{_texdir}/texmf-dist/fonts/type1/vntex/concretevn
%dir %{_texdir}/texmf-dist/fonts/type1/vntex/grotesqvn
%dir %{_texdir}/texmf-dist/fonts/type1/vntex/txttvn
%dir %{_texdir}/texmf-dist/fonts/type1/vntex/urwvn
%dir %{_texdir}/texmf-dist/fonts/type1/vntex/vnr
%dir %{_texdir}/texmf-dist/fonts/type1/vntex/vntopia
%dir %{_texdir}/texmf-dist/fonts/vf
%dir %{_texdir}/texmf-dist/fonts/vf/adobe
%dir %{_texdir}/texmf-dist/fonts/vf/adobe/avantgar
%dir %{_texdir}/texmf-dist/fonts/vf/adobe/bookman
%dir %{_texdir}/texmf-dist/fonts/vf/adobe/courier
%dir %{_texdir}/texmf-dist/fonts/vf/adobe/helvetic
%dir %{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk
%dir %{_texdir}/texmf-dist/fonts/vf/adobe/palatino
%dir %{_texdir}/texmf-dist/fonts/vf/adobe/times
%dir %{_texdir}/texmf-dist/fonts/vf/adobe/utopia
%dir %{_texdir}/texmf-dist/fonts/vf/adobe/zapfchan
%dir %{_texdir}/texmf-dist/fonts/vf/arkandis
%dir %{_texdir}/texmf-dist/fonts/vf/arkandis/baskervald
%dir %{_texdir}/texmf-dist/fonts/vf/arkandis/libris
%dir %{_texdir}/texmf-dist/fonts/vf/arkandis/romande
%dir %{_texdir}/texmf-dist/fonts/vf/arkandis/venturis
%dir %{_texdir}/texmf-dist/fonts/vf/arkandis/venturis2
%dir %{_texdir}/texmf-dist/fonts/vf/arkandis/venturisold
%dir %{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans
%dir %{_texdir}/texmf-dist/fonts/vf/arkandis/venturissans2
%dir %{_texdir}/texmf-dist/fonts/vf/arphic
%dir %{_texdir}/texmf-dist/fonts/vf/arphic/bkaimp
%dir %{_texdir}/texmf-dist/fonts/vf/arphic/bsmilp
%dir %{_texdir}/texmf-dist/fonts/vf/arphic/gbsnlp
%dir %{_texdir}/texmf-dist/fonts/vf/arphic/gkaimp
%dir %{_texdir}/texmf-dist/fonts/vf/bitstrea
%dir %{_texdir}/texmf-dist/fonts/vf/bitstrea/charter
%dir %{_texdir}/texmf-dist/fonts/vf/cg
%dir %{_texdir}/texmf-dist/fonts/vf/cg/courier
%dir %{_texdir}/texmf-dist/fonts/vf/cg/times
%dir %{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe
%dir %{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/avantgar
%dir %{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/bookman
%dir %{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/courier
%dir %{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/helvetic
%dir %{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/ncntrsbk
%dir %{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/palatino
%dir %{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/times
%dir %{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/zapfchan
%dir %{_texdir}/texmf-dist/fonts/vf/mathdesign
%dir %{_texdir}/texmf-dist/fonts/vf/mathdesign/mdbch
%dir %{_texdir}/texmf-dist/fonts/vf/mathdesign/mdput
%dir %{_texdir}/texmf-dist/fonts/vf/mathdesign/mdugm
%dir %{_texdir}/texmf-dist/fonts/vf/monotype
%dir %{_texdir}/texmf-dist/fonts/vf/monotype/helvetic
%dir %{_texdir}/texmf-dist/fonts/vf/ptex
%dir %{_texdir}/texmf-dist/fonts/vf/ptex/jis
%dir %{_texdir}/texmf-dist/fonts/vf/ptex/morisawa
%dir %{_texdir}/texmf-dist/fonts/vf/ptex/nmin-ngoth
%dir %{_texdir}/texmf-dist/fonts/vf/ptex/standard
%dir %{_texdir}/texmf-dist/fonts/vf/public
%dir %{_texdir}/texmf-dist/fonts/vf/public/ae
%dir %{_texdir}/texmf-dist/fonts/vf/public/arev
%dir %{_texdir}/texmf-dist/fonts/vf/public/augie
%dir %{_texdir}/texmf-dist/fonts/vf/public/bera
%dir %{_texdir}/texmf-dist/fonts/vf/public/bgreek
%dir %{_texdir}/texmf-dist/fonts/vf/public/blacklettert1
%dir %{_texdir}/texmf-dist/fonts/vf/public/brushscr
%dir %{_texdir}/texmf-dist/fonts/vf/public/cfr-lm
%dir %{_texdir}/texmf-dist/fonts/vf/public/cjhebrew
%dir %{_texdir}/texmf-dist/fonts/vf/public/cmcyr
%dir %{_texdir}/texmf-dist/fonts/vf/public/cm-lgc
%dir %{_texdir}/texmf-dist/fonts/vf/public/dozenal
%dir %{_texdir}/texmf-dist/fonts/vf/public/eco
%dir %{_texdir}/texmf-dist/fonts/vf/public/epigrafica
%dir %{_texdir}/texmf-dist/fonts/vf/public/eulervm
%dir %{_texdir}/texmf-dist/fonts/vf/public/fourier
%dir %{_texdir}/texmf-dist/fonts/vf/public/fouriernc
%dir %{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia
%dir %{_texdir}/texmf-dist/fonts/vf/public/gfsbaskerville
%dir %{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni
%dir %{_texdir}/texmf-dist/fonts/vf/public/gfscomplutum
%dir %{_texdir}/texmf-dist/fonts/vf/public/gfsdidot
%dir %{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic
%dir %{_texdir}/texmf-dist/fonts/vf/public/gfsporson
%dir %{_texdir}/texmf-dist/fonts/vf/public/gfssolomos
%dir %{_texdir}/texmf-dist/fonts/vf/public/gothic
%dir %{_texdir}/texmf-dist/fonts/vf/public/grverb
%dir %{_texdir}/texmf-dist/fonts/vf/public/hfoldsty
%dir %{_texdir}/texmf-dist/fonts/vf/public/kerkis
%dir %{_texdir}/texmf-dist/fonts/vf/public/kpfonts
%dir %{_texdir}/texmf-dist/fonts/vf/public/libertine
%dir %{_texdir}/texmf-dist/fonts/vf/public/mathpazo
%dir %{_texdir}/texmf-dist/fonts/vf/public/pslatex
%dir %{_texdir}/texmf-dist/fonts/vf/public/pxfonts
%dir %{_texdir}/texmf-dist/fonts/vf/public/qpxqtx
%dir %{_texdir}/texmf-dist/fonts/vf/public/tengwarscript
%dir %{_texdir}/texmf-dist/fonts/vf/public/txfonts
%dir %{_texdir}/texmf-dist/fonts/vf/public/txfontsb
%dir %{_texdir}/texmf-dist/fonts/vf/public/yhmath
%dir %{_texdir}/texmf-dist/fonts/vf/uhc
%dir %{_texdir}/texmf-dist/fonts/vf/uhc/uwmj
%dir %{_texdir}/texmf-dist/fonts/vf/uhc/wmj
%dir %{_texdir}/texmf-dist/fonts/vf/urw
%dir %{_texdir}/texmf-dist/fonts/vf/urw35vf
%dir %{_texdir}/texmf-dist/fonts/vf/urw35vf/avantgar
%dir %{_texdir}/texmf-dist/fonts/vf/urw35vf/bookman
%dir %{_texdir}/texmf-dist/fonts/vf/urw35vf/courier
%dir %{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic
%dir %{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk
%dir %{_texdir}/texmf-dist/fonts/vf/urw35vf/palatino
%dir %{_texdir}/texmf-dist/fonts/vf/urw35vf/times
%dir %{_texdir}/texmf-dist/fonts/vf/urw35vf/zapfchan
%dir %{_texdir}/texmf-dist/fonts/vf/urw/antiqua
%dir %{_texdir}/texmf-dist/fonts/vf/urw/grotesq
%dir %{_texdir}/texmf-dist/fonts/vf/vntex
%dir %{_texdir}/texmf-dist/fonts/vf/vntex/chartervn
%dir %{_texdir}/texmf-dist/fonts/vf/vntex/urwvn
%dir %{_texdir}/texmf-dist/fonts/vf/vntex/vntopia
%dir %{_texdir}/texmf-dist/makeindex
%dir %{_texdir}/texmf-dist/makeindex/arsclassica
%dir %{_texdir}/texmf-dist/makeindex/babel
%dir %{_texdir}/texmf-dist/makeindex/base
%dir %{_texdir}/texmf-dist/makeindex/bibarts
%dir %{_texdir}/texmf-dist/makeindex/confproc
%dir %{_texdir}/texmf-dist/makeindex/disser
%dir %{_texdir}/texmf-dist/makeindex/dtk
%dir %{_texdir}/texmf-dist/makeindex/expl3
%dir %{_texdir}/texmf-dist/makeindex/gatech-thesis
%dir %{_texdir}/texmf-dist/makeindex/gmdoc
%dir %{_texdir}/texmf-dist/makeindex/index
%dir %{_texdir}/texmf-dist/makeindex/iso
%dir %{_texdir}/texmf-dist/makeindex/juraabbrev
%dir %{_texdir}/texmf-dist/makeindex/latex
%dir %{_texdir}/texmf-dist/makeindex/memoir
%dir %{_texdir}/texmf-dist/makeindex/minitoc
%dir %{_texdir}/texmf-dist/makeindex/mkgrkindex
%dir %{_texdir}/texmf-dist/makeindex/multibib
%dir %{_texdir}/texmf-dist/makeindex/nomencl
%dir %{_texdir}/texmf-dist/makeindex/nomentbl
%dir %{_texdir}/texmf-dist/makeindex/nostarch
%dir %{_texdir}/texmf-dist/makeindex/plain
%dir %{_texdir}/texmf-dist/makeindex/repeatindex
%dir %{_texdir}/texmf-dist/makeindex/songbook
%dir %{_texdir}/texmf-dist/makeindex/startex
%dir %{_texdir}/texmf-dist/makeindex/xdoc
%dir %{_texdir}/texmf-dist/metafont
%dir %{_texdir}/texmf-dist/metafont/base
%dir %{_texdir}/texmf-dist/metafont/config
%dir %{_texdir}/texmf-dist/metafont/feynmf
%dir %{_texdir}/texmf-dist/metafont/mfpic
%dir %{_texdir}/texmf-dist/metafont/mftoeps
%dir %{_texdir}/texmf-dist/metafont/misc
%dir %{_texdir}/texmf-dist/metafont/roex
%dir %{_texdir}/texmf-dist/metapost
%dir %{_texdir}/texmf-dist/metapost/automata
%dir %{_texdir}/texmf-dist/metapost/base
%dir %{_texdir}/texmf-dist/metapost/bbcard
%dir %{_texdir}/texmf-dist/metapost/blockdraw_mp
%dir %{_texdir}/texmf-dist/metapost/bpolynomial
%dir %{_texdir}/texmf-dist/metapost/cmarrows
%dir %{_texdir}/texmf-dist/metapost/config
%dir %{_texdir}/texmf-dist/metapost/context
%dir %{_texdir}/texmf-dist/metapost/context/base
%dir %{_texdir}/texmf-dist/metapost/context/font
%dir %{_texdir}/texmf-dist/metapost/context/third
%dir %{_texdir}/texmf-dist/metapost/context/third/gnuplot
%dir %{_texdir}/texmf-dist/metapost/drv
%dir %{_texdir}/texmf-dist/metapost/dviincl
%dir %{_texdir}/texmf-dist/metapost/epsincl
%dir %{_texdir}/texmf-dist/metapost/expressg
%dir %{_texdir}/texmf-dist/metapost/exteps
%dir %{_texdir}/texmf-dist/metapost/featpost
%dir %{_texdir}/texmf-dist/metapost/feynmf
%dir %{_texdir}/texmf-dist/metapost/frcursive
%dir %{_texdir}/texmf-dist/metapost/garrigues
%dir %{_texdir}/texmf-dist/metapost/hatching
%dir %{_texdir}/texmf-dist/metapost/latexmp
%dir %{_texdir}/texmf-dist/metapost/makecirc
%dir %{_texdir}/texmf-dist/metapost/metago
%dir %{_texdir}/texmf-dist/metapost/metaobj
%dir %{_texdir}/texmf-dist/metapost/metaplot
%dir %{_texdir}/texmf-dist/metapost/metauml
%dir %{_texdir}/texmf-dist/metapost/mfpic
%dir %{_texdir}/texmf-dist/metapost/misc
%dir %{_texdir}/texmf-dist/metapost/mpattern
%dir %{_texdir}/texmf-dist/metapost/nkarta
%dir %{_texdir}/texmf-dist/metapost/piechartmp
%dir %{_texdir}/texmf-dist/metapost/slideshow
%dir %{_texdir}/texmf-dist/metapost/splines
%dir %{_texdir}/texmf-dist/metapost/suanpan
%dir %{_texdir}/texmf-dist/metapost/support
%dir %{_texdir}/texmf-dist/metapost/support/charlib
%dir %{_texdir}/texmf-dist/metapost/tabvar
%dir %{_texdir}/texmf-dist/metapost/textpath
%dir %{_texdir}/texmf-dist/metapost/venn
%dir %{_texdir}/texmf-dist/mft
%dir %{_texdir}/texmf-dist/mft/base
%dir %{_texdir}/texmf-dist/omega
%dir %{_texdir}/texmf-dist/omega/ocp
%dir %{_texdir}/texmf-dist/omega/ocp/antomega
%dir %{_texdir}/texmf-dist/omega/ocp/antomega/latin
%dir %{_texdir}/texmf-dist/omega/ocp/char2uni
%dir %{_texdir}/texmf-dist/omega/ocp/ethiop
%dir %{_texdir}/texmf-dist/omega/ocp/misc
%dir %{_texdir}/texmf-dist/omega/ocp/ocherokee
%dir %{_texdir}/texmf-dist/omega/ocp/oinuit
%dir %{_texdir}/texmf-dist/omega/ocp/omega
%dir %{_texdir}/texmf-dist/omega/ocp/otibet
%dir %{_texdir}/texmf-dist/omega/ocp/uni2char
%dir %{_texdir}/texmf-dist/omega/otp
%dir %{_texdir}/texmf-dist/omega/otp/antomega
%dir %{_texdir}/texmf-dist/omega/otp/antomega/latin
%dir %{_texdir}/texmf-dist/omega/otp/char2uni
%dir %{_texdir}/texmf-dist/omega/otp/ethiop
%dir %{_texdir}/texmf-dist/omega/otp/misc
%dir %{_texdir}/texmf-dist/omega/otp/ocherokee
%dir %{_texdir}/texmf-dist/omega/otp/omega
%dir %{_texdir}/texmf-dist/omega/otp/otibet
%dir %{_texdir}/texmf-dist/omega/otp/uni2char
%dir %{_texdir}/texmf-dist/pbibtex
%dir %{_texdir}/texmf-dist/pbibtex/bib
%dir %{_texdir}/texmf-dist/pbibtex/bst
%dir %{_texdir}/texmf-dist/scripts
%dir %{_texdir}/texmf-dist/scripts/accfonts
%dir %{_texdir}/texmf-dist/scripts/authorindex
%dir %{_texdir}/texmf-dist/scripts/bibexport
%dir %{_texdir}/texmf-dist/scripts/bundledoc
%dir %{_texdir}/texmf-dist/scripts/cachepic
%dir %{_texdir}/texmf-dist/scripts/context
%dir %{_texdir}/texmf-dist/scripts/context/lua
%dir %{_texdir}/texmf-dist/scripts/context/perl
%dir %{_texdir}/texmf-dist/scripts/context/ruby
%dir %{_texdir}/texmf-dist/scripts/context/ruby/base
%dir %{_texdir}/texmf-dist/scripts/context/ruby/base/kpse
%dir %{_texdir}/texmf-dist/scripts/context/ruby/graphics
%dir %{_texdir}/texmf-dist/scripts/context/stubs
%dir %{_texdir}/texmf-dist/scripts/context/stubs/mswin
%dir %{_texdir}/texmf-dist/scripts/context/stubs/source
%dir %{_texdir}/texmf-dist/scripts/context/stubs/unix
%dir %{_texdir}/texmf-dist/scripts/de-macro
%dir %{_texdir}/texmf-dist/scripts/dviasm
%dir %{_texdir}/texmf-dist/scripts/epspdf
%dir %{_texdir}/texmf-dist/scripts/epstopdf
%dir %{_texdir}/texmf-dist/scripts/fig4latex
%dir %{_texdir}/texmf-dist/scripts/findhyph
%dir %{_texdir}/texmf-dist/scripts/fontools
%dir %{_texdir}/texmf-dist/scripts/fragmaster
%dir %{_texdir}/texmf-dist/scripts/glossaries
%dir %{_texdir}/texmf-dist/scripts/jmlr
%dir %{_texdir}/texmf-dist/scripts/latex2man
%dir %{_texdir}/texmf-dist/scripts/latexdiff
%dir %{_texdir}/texmf-dist/scripts/latexmk
%dir %{_texdir}/texmf-dist/scripts/listings-ext
%dir %{_texdir}/texmf-dist/scripts/lua-alt-getopt
%dir %{_texdir}/texmf-dist/scripts/luaotfload
%dir %{_texdir}/texmf-dist/scripts/mathspic
%dir %{_texdir}/texmf-dist/scripts/mkgrkindex
%dir %{_texdir}/texmf-dist/scripts/oberdiek
%dir %{_texdir}/texmf-dist/scripts/pax
%dir %{_texdir}/texmf-dist/scripts/pdfcrop
%dir %{_texdir}/texmf-dist/scripts/pdfjam
%dir %{_texdir}/texmf-dist/scripts/perltex
%dir %{_texdir}/texmf-dist/scripts/pgfplots
%dir %{_texdir}/texmf-dist/scripts/pkfix
%dir %{_texdir}/texmf-dist/scripts/pkfix-helper
%dir %{_texdir}/texmf-dist/scripts/ppower4
%dir %{_texdir}/texmf-dist/scripts/pst2pdf
%dir %{_texdir}/texmf-dist/scripts/pst-pdf
%dir %{_texdir}/texmf-dist/scripts/purifyeps
%dir %{_texdir}/texmf-dist/scripts/shipunov
%dir %{_texdir}/texmf-dist/scripts/splitindex
%dir %{_texdir}/texmf-dist/scripts/splitindex/perl
%dir %{_texdir}/texmf-dist/scripts/svn-multi
%dir %{_texdir}/texmf-dist/scripts/tex4ht
%dir %{_texdir}/texmf-dist/scripts/texcount
%dir %{_texdir}/texmf-dist/scripts/texloganalyser
%dir %{_texdir}/texmf-dist/scripts/thumbpdf
%dir %{_texdir}/texmf-dist/scripts/ulqda
%dir %{_texdir}/texmf-dist/scripts/vpe
%dir %{_texdir}/texmf-dist/scripts/xetex
%dir %{_texdir}/texmf-dist/scripts/xetex/perl
%dir %{_texdir}/texmf-dist/scripts/xetex/perl/lib
%dir %{_texdir}/texmf-dist/scripts/xetex/perl/lib/PDF
%dir %{_texdir}/texmf-dist/scripts/xetex/perl/lib/PDF/Reuse
%dir %{_texdir}/texmf-dist/source
%dir %{_texdir}/texmf-dist/source/latex
%dir %{_texdir}/texmf-dist/source/latex/koma-script
%dir %{_texdir}/texmf-dist/source/latex/koma-script/doc
%dir %{_texdir}/texmf-dist/source/latex/koma-script/doc/bin
%dir %{_texdir}/texmf-dist/source/latex/koma-script/doc/english
%dir %{_texdir}/texmf-dist/source/latex/koma-script/doc/ngerman
%dir %{_texdir}/texmf-dist/tex
%dir %{_texdir}/texmf-dist/tex4ht
%dir %{_texdir}/texmf-dist/tex4ht/base
%dir %{_texdir}/texmf-dist/tex4ht/base/unix
%dir %{_texdir}/texmf-dist/tex4ht/bin
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/avantgar
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/bookman
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/courier
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/helvetic
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/mathppl
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/mathptmx
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/ncntrsbk
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/palatino
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/ppalatino
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/pslatex
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/symbol
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/times
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/utopia
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/zapfchan
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/adobe/zapfding
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/ae
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/ams
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/ams/euler
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/antt
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/arabi
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/arev
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/bitstrea
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/bitstrea/charter
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/cc-pl
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/chartervn
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/chess
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/cjk
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/cjk/b5ka
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/cm
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/cm/sauter
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/concrete
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/cs
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/currency
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/cyklop
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/cyrillic
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/cyrillic/cmcyr
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/aliase
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/ec
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/aliase/mathtime
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/eulervm
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/euro
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk/gbkcy
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk/gbkfs
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk/gbkhei
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk/gbkkai
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk/gbkli
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk/gbkshu
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk/gbksu
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk/gbkxh
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk/gbkxk
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk/gbkxw
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk/gbkyao
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/gbk/gbkyou
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/greek
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/greek/ibygrk
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/hebrew
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/iwona
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/iwona/cs-iwonacap
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/iwona/ec-iwonacap
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/iwona/qx
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/iwona/t5-iwonacap
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/iwona/texnansi
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/jknappen
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/jknappen/tc
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/cs-iwona
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/cs-iwonacap
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/ec
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/ex-iwona
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/exp-iwona
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/greek-iwona
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/mi-iwona
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/qx-iwona
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/qx-iwonacap
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/rm-iwona
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/sy-iwona
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/t2a-iwona
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/t2b-iwona
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/t2c-iwona
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/t5-iwona
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/t5-iwonacap
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/texnansi
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/kurier/wncy-iwona
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/latex
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lh
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lh/lh-t2a
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/libertine
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lm
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lm/lm-ec
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lm/lm-qx
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lm/lm-rep-cmin
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lm/lm-rep-cmrm
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lm/lm-rep-cmsc
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lm/lm-rep-csin
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lm/lm-rep-csrm
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lm/lm-rep-cstt
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lm/lm-rep-plrm
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lm/lm-rep-t5psn
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/lm/pre2005
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/marvosym
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/mathdesign
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/mathpple
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/mathtime
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/pazo
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/pl
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/pxfonts
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/qfonts
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/sw
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/times
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/tipa
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/txfonts
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex/arevvn
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex/chartervn
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex/classicovn
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex/cmbrightvn
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex/comicsansvn
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex/concretevn
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex/garamondvn
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex/grotesqvn
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex/mscorevn
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex/urwvn
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex/utopiavn
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/alias/vntex/vnr
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/ascii
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/ascii/manfnt
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/cp1256
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/cp1256/charset
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/css
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/css/emacspeak
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/css/emacspeak/cm
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/dbcs
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/dbcs/cjk
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/dbcs/cjk/b5ka
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/gb2312
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/gb2312/charset
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/gbk
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/gbk/charset
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/html-speech
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/html-speech/charset
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/charset
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/charset/uni
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/chess
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/cm
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/devanagari
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/euro
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/go
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/html
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/html/charset
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/ipa
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/mathtime
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/mongolian
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/ps2mf
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/sw
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/tibetan
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/1/xypic
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/2
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/2/charset
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/2/html
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/2/html/charset
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/5
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/5/charset
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/5/cm
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/5/cm/sauter
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/5/cyrillic
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/5/cyrillic/cmcyr
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/5/html
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/5/html/charset
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/5/lh
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/5/lh/lh-t2a
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/6
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/6/charset
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/6/html
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/6/html/charset
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/7
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/7/charset
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/8
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/iso8859/8/hebrew
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/jsml
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/jsml/charset
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/koi
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/koi/8r
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/koi/8r/charset
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/koi/8r/lh
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/koi/8r/lh/lh-t2a
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/mozilla
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/mozilla/charset
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/mozilla/charset/mnemonic
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/mozilla/charset/native
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/ooffice
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/ooffice/charset
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/share
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/share/adobe
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/share/adobe/helvetic
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/symbol
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/symbol/charset
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/symbol/cyrillic
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/symbol/hebrew
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/symbol/mathtime
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/adobe
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/adobe/courier
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/adobe/helvetic
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/adobe/mathptm
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/adobe/palatino
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/adobe/symbol
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/adobe/times
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/adobe/zapfding
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/ae
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/ams
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/ams/cyrillic
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/ams/euler
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/ams/symbols
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/antt
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/arabi
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/arev
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/bbold
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/bitstrea
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/bitstrea/charter
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/cbgreek
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/charset
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/chess
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/cjk
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/cjk/b5ka
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/cjk/gbksong
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/cjk/gbksong/long
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/cjk/utf8
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/cm
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/concrete
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/cs
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/currency
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/cyklop
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/cyrillic
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/cyrillic/cmcyr
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/dstroke
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/greek
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/greek/ibygrk
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/hebrew
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/html
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/html/charset
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/iwona
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/jknappen
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/jknappen/tc
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/latex
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/lh
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/lh/lh-t2a
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/libertine
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/lm
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/lm/pre2005
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/marvosym
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/math
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/mathdesign
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/mathtime
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/mflogo
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/misc
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/pl
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/public
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/pxfonts
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/stmaryrd
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/tibetan
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/tipa
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/unicode/txfonts
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/utf8
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/utf8/charset
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/viqr
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/viqr/charset
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/viscii
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/viscii/charset
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/win
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/win/1251
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/win/1251/charset
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/win/1251/cm
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/win/1251/cm/sauter
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/win/1251/cyrillic
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/win/1251/cyrillic/cmcyr
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/win/1251/lh
%dir %{_texdir}/texmf-dist/tex4ht/ht-fonts/win/1251/lh/lh-t2a
%dir %{_texdir}/texmf-dist/tex4ht/xtpipes
%dir %{_texdir}/texmf-dist/tex/alatex
%dir %{_texdir}/texmf-dist/tex/alatex/base
%dir %{_texdir}/texmf-dist/tex/amstex
%dir %{_texdir}/texmf-dist/tex/amstex/base
%dir %{_texdir}/texmf-dist/tex/amstex/config
%dir %{_texdir}/texmf-dist/tex/context
%dir %{_texdir}/texmf-dist/tex/context/base
%dir %{_texdir}/texmf-dist/tex/context/bib
%dir %{_texdir}/texmf-dist/tex/context/config
%dir %{_texdir}/texmf-dist/tex/context/extra
%dir %{_texdir}/texmf-dist/tex/context/fonts
%dir %{_texdir}/texmf-dist/tex/context/foxet
%dir %{_texdir}/texmf-dist/tex/context/interface
%dir %{_texdir}/texmf-dist/tex/context/interface/third
%dir %{_texdir}/texmf-dist/tex/context/patterns
%dir %{_texdir}/texmf-dist/tex/context/pgf
%dir %{_texdir}/texmf-dist/tex/context/pgf/basiclayer
%dir %{_texdir}/texmf-dist/tex/context/pgf/frontendlayer
%dir %{_texdir}/texmf-dist/tex/context/pgf/math
%dir %{_texdir}/texmf-dist/tex/context/pgf/systemlayer
%dir %{_texdir}/texmf-dist/tex/context/pgf/utilities
%dir %{_texdir}/texmf-dist/tex/context/sample
%dir %{_texdir}/texmf-dist/tex/context/test
%dir %{_texdir}/texmf-dist/tex/context/third
%dir %{_texdir}/texmf-dist/tex/context/third/account
%dir %{_texdir}/texmf-dist/tex/context/third/algorithmic
%dir %{_texdir}/texmf-dist/tex/context/third/bnf
%dir %{_texdir}/texmf-dist/tex/context/third/chromato
%dir %{_texdir}/texmf-dist/tex/context/third/construction-plan
%dir %{_texdir}/texmf-dist/tex/context/third/degrade
%dir %{_texdir}/texmf-dist/tex/context/third/fixme
%dir %{_texdir}/texmf-dist/tex/context/third/french
%dir %{_texdir}/texmf-dist/tex/context/third/fullpage
%dir %{_texdir}/texmf-dist/tex/context/third/games
%dir %{_texdir}/texmf-dist/tex/context/third/gentium
%dir %{_texdir}/texmf-dist/tex/context/third/gnuplot
%dir %{_texdir}/texmf-dist/tex/context/third/letter
%dir %{_texdir}/texmf-dist/tex/context/third/letter/base
%dir %{_texdir}/texmf-dist/tex/context/third/letter/extension
%dir %{_texdir}/texmf-dist/tex/context/third/letter/interface
%dir %{_texdir}/texmf-dist/tex/context/third/letter/style
%dir %{_texdir}/texmf-dist/tex/context/third/lettrine
%dir %{_texdir}/texmf-dist/tex/context/third/lilypond
%dir %{_texdir}/texmf-dist/tex/context/third/pgfplots
%dir %{_texdir}/texmf-dist/tex/context/third/ruby
%dir %{_texdir}/texmf-dist/tex/context/third/semaphor
%dir %{_texdir}/texmf-dist/tex/context/third/simplefonts
%dir %{_texdir}/texmf-dist/tex/context/third/simpleslides
%dir %{_texdir}/texmf-dist/tex/context/third/typearea
%dir %{_texdir}/texmf-dist/tex/context/third/typescripts
%dir %{_texdir}/texmf-dist/tex/context/third/vim
%dir %{_texdir}/texmf-dist/tex/context/user
%dir %{_texdir}/texmf-dist/tex/cslatex
%dir %{_texdir}/texmf-dist/tex/cslatex/base
%dir %{_texdir}/texmf-dist/tex/csplain
%dir %{_texdir}/texmf-dist/tex/csplain/base
%dir %{_texdir}/texmf-dist/tex/eplain
%dir %{_texdir}/texmf-dist/tex/fontinst
%dir %{_texdir}/texmf-dist/tex/fontinst/base
%dir %{_texdir}/texmf-dist/tex/fontinst/latinetx
%dir %{_texdir}/texmf-dist/tex/fontinst/latinmtx
%dir %{_texdir}/texmf-dist/tex/fontinst/mathetx
%dir %{_texdir}/texmf-dist/tex/fontinst/mathmtx
%dir %{_texdir}/texmf-dist/tex/fontinst/misc
%dir %{_texdir}/texmf-dist/tex/fontinst/smbletx
%dir %{_texdir}/texmf-dist/tex/fontinst/smblmtx
%dir %{_texdir}/texmf-dist/tex/generic
%dir %{_texdir}/texmf-dist/tex/generic/2up
%dir %{_texdir}/texmf-dist/tex/generic/abbr
%dir %{_texdir}/texmf-dist/tex/generic/abstyles
%dir %{_texdir}/texmf-dist/tex/generic/arrayjobx
%dir %{_texdir}/texmf-dist/tex/generic/babel
%dir %{_texdir}/texmf-dist/tex/generic/barr
%dir %{_texdir}/texmf-dist/tex/generic/colortab
%dir %{_texdir}/texmf-dist/tex/generic/context
%dir %{_texdir}/texmf-dist/tex/generic/c-pascal
%dir %{_texdir}/texmf-dist/tex/generic/dcpic
%dir %{_texdir}/texmf-dist/tex/generic/dehyph-exptl
%dir %{_texdir}/texmf-dist/tex/generic/dirtree
%dir %{_texdir}/texmf-dist/tex/generic/dratex
%dir %{_texdir}/texmf-dist/tex/generic/dvips
%dir %{_texdir}/texmf-dist/tex/generic/ean
%dir %{_texdir}/texmf-dist/tex/generic/edmac
%dir %{_texdir}/texmf-dist/tex/generic/eijkhout
%dir %{_texdir}/texmf-dist/tex/generic/encodings
%dir %{_texdir}/texmf-dist/tex/generic/enctex
%dir %{_texdir}/texmf-dist/tex/generic/epsf
%dir %{_texdir}/texmf-dist/tex/generic/fenixpar
%dir %{_texdir}/texmf-dist/tex/generic/fltpoint
%dir %{_texdir}/texmf-dist/tex/generic/frame
%dir %{_texdir}/texmf-dist/tex/generic/genmisc
%dir %{_texdir}/texmf-dist/tex/generic/german
%dir %{_texdir}/texmf-dist/tex/generic/hyphenex
%dir %{_texdir}/texmf-dist/tex/generic/hyph-utf8
%dir %{_texdir}/texmf-dist/tex/generic/hyph-utf8/conversions
%dir %{_texdir}/texmf-dist/tex/generic/hyph-utf8/loadhyph
%dir %{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns
%dir %{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex
%dir %{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/tex-special
%dir %{_texdir}/texmf-dist/tex/generic/hyph-utf8/patterns/txt
%dir %{_texdir}/texmf-dist/tex/generic/ibygrk
%dir %{_texdir}/texmf-dist/tex/generic/iftex
%dir %{_texdir}/texmf-dist/tex/generic/ifxetex
%dir %{_texdir}/texmf-dist/tex/generic/insbox
%dir %{_texdir}/texmf-dist/tex/generic/kastrup
%dir %{_texdir}/texmf-dist/tex/generic/librarian
%dir %{_texdir}/texmf-dist/tex/generic/mathabx
%dir %{_texdir}/texmf-dist/tex/generic/mathdots
%dir %{_texdir}/texmf-dist/tex/generic/metapost
%dir %{_texdir}/texmf-dist/tex/generic/mfpic
%dir %{_texdir}/texmf-dist/tex/generic/midnight
%dir %{_texdir}/texmf-dist/tex/generic/misc
%dir %{_texdir}/texmf-dist/tex/generic/multido
%dir %{_texdir}/texmf-dist/tex/generic/musixlyr
%dir %{_texdir}/texmf-dist/tex/generic/musixps
%dir %{_texdir}/texmf-dist/tex/generic/musixtex
%dir %{_texdir}/texmf-dist/tex/generic/oberdiek
%dir %{_texdir}/texmf-dist/tex/generic/ofs
%dir %{_texdir}/texmf-dist/tex/generic/omegahyph
%dir %{_texdir}/texmf-dist/tex/generic/pdf-trans
%dir %{_texdir}/texmf-dist/tex/generic/pgf
%dir %{_texdir}/texmf-dist/tex/generic/pgf/basiclayer
%dir %{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer
%dir %{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz
%dir %{_texdir}/texmf-dist/tex/generic/pgf/frontendlayer/tikz/libraries
%dir %{_texdir}/texmf-dist/tex/generic/pgf/libraries
%dir %{_texdir}/texmf-dist/tex/generic/pgf/math
%dir %{_texdir}/texmf-dist/tex/generic/pgf/modules
%dir %{_texdir}/texmf-dist/tex/generic/pgfplots
%dir %{_texdir}/texmf-dist/tex/generic/pgfplots/libs
%dir %{_texdir}/texmf-dist/tex/generic/pgfplots/liststructure
%dir %{_texdir}/texmf-dist/tex/generic/pgfplots/numtable
%dir %{_texdir}/texmf-dist/tex/generic/pgfplots/oldpgfcompatib
%dir %{_texdir}/texmf-dist/tex/generic/pgfplots/oldpgfplotscompatib
%dir %{_texdir}/texmf-dist/tex/generic/pgfplots/sys
%dir %{_texdir}/texmf-dist/tex/generic/pgfplots/util
%dir %{_texdir}/texmf-dist/tex/generic/pgf/systemlayer
%dir %{_texdir}/texmf-dist/tex/generic/pgf/utilities
%dir %{_texdir}/texmf-dist/tex/generic/poster-mac
%dir %{_texdir}/texmf-dist/tex/generic/pst-3d
%dir %{_texdir}/texmf-dist/tex/generic/pst-3dplot
%dir %{_texdir}/texmf-dist/tex/generic/pst-abspos
%dir %{_texdir}/texmf-dist/tex/generic/pst-asr
%dir %{_texdir}/texmf-dist/tex/generic/pst-bar
%dir %{_texdir}/texmf-dist/tex/generic/pst-barcode
%dir %{_texdir}/texmf-dist/tex/generic/pst-bezier
%dir %{_texdir}/texmf-dist/tex/generic/pst-blur
%dir %{_texdir}/texmf-dist/tex/generic/pst-bspline
%dir %{_texdir}/texmf-dist/tex/generic/pst-circ
%dir %{_texdir}/texmf-dist/tex/generic/pst-coil
%dir %{_texdir}/texmf-dist/tex/generic/pst-cox
%dir %{_texdir}/texmf-dist/tex/generic/pst-diffraction
%dir %{_texdir}/texmf-dist/tex/generic/pst-electricfield
%dir %{_texdir}/texmf-dist/tex/generic/pst-eps
%dir %{_texdir}/texmf-dist/tex/generic/pst-eucl
%dir %{_texdir}/texmf-dist/tex/generic/pst-fill
%dir %{_texdir}/texmf-dist/tex/generic/pst-fr3d
%dir %{_texdir}/texmf-dist/tex/generic/pst-fractal
%dir %{_texdir}/texmf-dist/tex/generic/pst-fun
%dir %{_texdir}/texmf-dist/tex/generic/pst-func
%dir %{_texdir}/texmf-dist/tex/generic/pst-gantt
%dir %{_texdir}/texmf-dist/tex/generic/pst-geo
%dir %{_texdir}/texmf-dist/tex/generic/pst-geo/data
%dir %{_texdir}/texmf-dist/tex/generic/pst-geo/dataII
%dir %{_texdir}/texmf-dist/tex/generic/pst-ghsb
%dir %{_texdir}/texmf-dist/tex/generic/pst-gr3d
%dir %{_texdir}/texmf-dist/tex/generic/pst-grad
%dir %{_texdir}/texmf-dist/tex/generic/pst-infixplot
%dir %{_texdir}/texmf-dist/tex/generic/pst-jtree
%dir %{_texdir}/texmf-dist/tex/generic/pst-knot
%dir %{_texdir}/texmf-dist/tex/generic/pst-labo
%dir %{_texdir}/texmf-dist/tex/generic/pst-lens
%dir %{_texdir}/texmf-dist/tex/generic/pst-light3d
%dir %{_texdir}/texmf-dist/tex/generic/pst-magneticfield
%dir %{_texdir}/texmf-dist/tex/generic/pst-math
%dir %{_texdir}/texmf-dist/tex/generic/pst-mirror
%dir %{_texdir}/texmf-dist/tex/generic/pst-node
%dir %{_texdir}/texmf-dist/tex/generic/pst-ob3d
%dir %{_texdir}/texmf-dist/tex/generic/pst-optexp
%dir %{_texdir}/texmf-dist/tex/generic/pst-optic
%dir %{_texdir}/texmf-dist/tex/generic/pst-osci
%dir %{_texdir}/texmf-dist/tex/generic/pst-pad
%dir %{_texdir}/texmf-dist/tex/generic/pst-pdgr
%dir %{_texdir}/texmf-dist/tex/generic/pst-plot
%dir %{_texdir}/texmf-dist/tex/generic/pst-poly
%dir %{_texdir}/texmf-dist/tex/generic/pst-qtree
%dir %{_texdir}/texmf-dist/tex/generic/pstricks
%dir %{_texdir}/texmf-dist/tex/generic/pstricks-add
%dir %{_texdir}/texmf-dist/tex/generic/pstricks/config
%dir %{_texdir}/texmf-dist/tex/generic/pst-sigsys
%dir %{_texdir}/texmf-dist/tex/generic/pst-slpe
%dir %{_texdir}/texmf-dist/tex/generic/pst-solides3d
%dir %{_texdir}/texmf-dist/tex/generic/pst-spectra
%dir %{_texdir}/texmf-dist/tex/generic/pst-stru
%dir %{_texdir}/texmf-dist/tex/generic/pst-text
%dir %{_texdir}/texmf-dist/tex/generic/pst-thick
%dir %{_texdir}/texmf-dist/tex/generic/pst-tree
%dir %{_texdir}/texmf-dist/tex/generic/pst-vue3d
%dir %{_texdir}/texmf-dist/tex/generic/qpxqtx
%dir %{_texdir}/texmf-dist/tex/generic/rlepsf
%dir %{_texdir}/texmf-dist/tex/generic/ruhyphen
%dir %{_texdir}/texmf-dist/tex/generic/shapepar
%dir %{_texdir}/texmf-dist/tex/generic/t2
%dir %{_texdir}/texmf-dist/tex/generic/t2/cyrfinst
%dir %{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/derivatives
%dir %{_texdir}/texmf-dist/tex/generic/t2/cyrfinst/etc
%dir %{_texdir}/texmf-dist/tex/generic/tabto-generic
%dir %{_texdir}/texmf-dist/tex/generic/tap
%dir %{_texdir}/texmf-dist/tex/generic/tex4ht
%dir %{_texdir}/texmf-dist/tex/generic/texapi
%dir %{_texdir}/texmf-dist/tex/generic/texdraw
%dir %{_texdir}/texmf-dist/tex/generic/tex-ewd
%dir %{_texdir}/texmf-dist/tex/generic/tex-ps
%dir %{_texdir}/texmf-dist/tex/generic/textmerg
%dir %{_texdir}/texmf-dist/tex/generic/thumbpdf
%dir %{_texdir}/texmf-dist/tex/generic/ukrhyph
%dir %{_texdir}/texmf-dist/tex/generic/ulem
%dir %{_texdir}/texmf-dist/tex/generic/variations
%dir %{_texdir}/texmf-dist/tex/generic/vaucanson-g
%dir %{_texdir}/texmf-dist/tex/generic/velthuis
%dir %{_texdir}/texmf-dist/tex/generic/xcomment
%dir %{_texdir}/texmf-dist/tex/generic/xecyr
%dir %{_texdir}/texmf-dist/tex/generic/xetexconfig
%dir %{_texdir}/texmf-dist/tex/generic/xkeyval
%dir %{_texdir}/texmf-dist/tex/generic/xlop
%dir %{_texdir}/texmf-dist/tex/generic/xstring
%dir %{_texdir}/texmf-dist/tex/generic/xypic
%dir %{_texdir}/texmf-dist/tex/generic/yax
%dir %{_texdir}/texmf-dist/tex/generic/zhmetrics
%dir %{_texdir}/texmf-dist/tex/jadetex
%dir %{_texdir}/texmf-dist/tex/jadetex/base
%dir %{_texdir}/texmf-dist/tex/lambda
%dir %{_texdir}/texmf-dist/tex/lambda/antomega
%dir %{_texdir}/texmf-dist/tex/lambda/base
%dir %{_texdir}/texmf-dist/tex/lambda/config
%dir %{_texdir}/texmf-dist/tex/lambda/oinuit
%dir %{_texdir}/texmf-dist/tex/latex
%dir %{_texdir}/texmf-dist/tex/latex/12many
%dir %{_texdir}/texmf-dist/tex/latex/a0poster
%dir %{_texdir}/texmf-dist/tex/latex/a5comb
%dir %{_texdir}/texmf-dist/tex/latex/aastex
%dir %{_texdir}/texmf-dist/tex/latex/abc
%dir %{_texdir}/texmf-dist/tex/latex/abstract
%dir %{_texdir}/texmf-dist/tex/latex/accfonts
%dir %{_texdir}/texmf-dist/tex/latex/achemso
%dir %{_texdir}/texmf-dist/tex/latex/achemso/config
%dir %{_texdir}/texmf-dist/tex/latex/acmconf
%dir %{_texdir}/texmf-dist/tex/latex/acromake
%dir %{_texdir}/texmf-dist/tex/latex/acronym
%dir %{_texdir}/texmf-dist/tex/latex/active-conf
%dir %{_texdir}/texmf-dist/tex/latex/addlines
%dir %{_texdir}/texmf-dist/tex/latex/adrconv
%dir %{_texdir}/texmf-dist/tex/latex/ae
%dir %{_texdir}/texmf-dist/tex/latex/aeguill
%dir %{_texdir}/texmf-dist/tex/latex/afthesis
%dir %{_texdir}/texmf-dist/tex/latex/aguplus
%dir %{_texdir}/texmf-dist/tex/latex/aiaa
%dir %{_texdir}/texmf-dist/tex/latex/AkkTeX
%dir %{_texdir}/texmf-dist/tex/latex/akletter
%dir %{_texdir}/texmf-dist/tex/latex/alg
%dir %{_texdir}/texmf-dist/tex/latex/algorithm2e
%dir %{_texdir}/texmf-dist/tex/latex/algorithmicx
%dir %{_texdir}/texmf-dist/tex/latex/algorithms
%dir %{_texdir}/texmf-dist/tex/latex/allrunes
%dir %{_texdir}/texmf-dist/tex/latex/alnumsec
%dir %{_texdir}/texmf-dist/tex/latex/alterqcm
%dir %{_texdir}/texmf-dist/tex/latex/altfont
%dir %{_texdir}/texmf-dist/tex/latex/ametsoc
%dir %{_texdir}/texmf-dist/tex/latex/amsaddr
%dir %{_texdir}/texmf-dist/tex/latex/amscls
%dir %{_texdir}/texmf-dist/tex/latex/amsfonts
%dir %{_texdir}/texmf-dist/tex/latex/amsmath
%dir %{_texdir}/texmf-dist/tex/latex/amsrefs
%dir %{_texdir}/texmf-dist/tex/latex/animate
%dir %{_texdir}/texmf-dist/tex/latex/anonchap
%dir %{_texdir}/texmf-dist/tex/latex/answers
%dir %{_texdir}/texmf-dist/tex/latex/antiqua
%dir %{_texdir}/texmf-dist/tex/latex/antp
%dir %{_texdir}/texmf-dist/tex/latex/antt
%dir %{_texdir}/texmf-dist/tex/latex/anyfontsize
%dir %{_texdir}/texmf-dist/tex/latex/anysize
%dir %{_texdir}/texmf-dist/tex/latex/apa
%dir %{_texdir}/texmf-dist/tex/latex/apacite
%dir %{_texdir}/texmf-dist/tex/latex/apalike
%dir %{_texdir}/texmf-dist/tex/latex/appendix
%dir %{_texdir}/texmf-dist/tex/latex/ar
%dir %{_texdir}/texmf-dist/tex/latex/arabi
%dir %{_texdir}/texmf-dist/tex/latex/arabtex
%dir %{_texdir}/texmf-dist/tex/latex/archaic
%dir %{_texdir}/texmf-dist/tex/latex/arcs
%dir %{_texdir}/texmf-dist/tex/latex/arev
%dir %{_texdir}/texmf-dist/tex/latex/armenian
%dir %{_texdir}/texmf-dist/tex/latex/arsclassica
%dir %{_texdir}/texmf-dist/tex/latex/arydshln
%dir %{_texdir}/texmf-dist/tex/latex/asaetr
%dir %{_texdir}/texmf-dist/tex/latex/ascelike
%dir %{_texdir}/texmf-dist/tex/latex/ascii
%dir %{_texdir}/texmf-dist/tex/latex/assignment
%dir %{_texdir}/texmf-dist/tex/latex/asyfig
%dir %{_texdir}/texmf-dist/tex/latex/attachfile
%dir %{_texdir}/texmf-dist/tex/latex/augie
%dir %{_texdir}/texmf-dist/tex/latex/auncial-new
%dir %{_texdir}/texmf-dist/tex/latex/aurical
%dir %{_texdir}/texmf-dist/tex/latex/authoraftertitle
%dir %{_texdir}/texmf-dist/tex/latex/authorindex
%dir %{_texdir}/texmf-dist/tex/latex/autoarea
%dir %{_texdir}/texmf-dist/tex/latex/auto-pst-pdf
%dir %{_texdir}/texmf-dist/tex/latex/avantgar
%dir %{_texdir}/texmf-dist/tex/latex/babelbib
%dir %{_texdir}/texmf-dist/tex/latex/background
%dir %{_texdir}/texmf-dist/tex/latex/bangtex
%dir %{_texdir}/texmf-dist/tex/latex/barcodes
%dir %{_texdir}/texmf-dist/tex/latex/bardiag
%dir %{_texdir}/texmf-dist/tex/latex/base
%dir %{_texdir}/texmf-dist/tex/latex/baskervald
%dir %{_texdir}/texmf-dist/tex/latex/bayer
%dir %{_texdir}/texmf-dist/tex/latex/bbding
%dir %{_texdir}/texmf-dist/tex/latex/bbm-macros
%dir %{_texdir}/texmf-dist/tex/latex/bbold
%dir %{_texdir}/texmf-dist/tex/latex/bclogo
%dir %{_texdir}/texmf-dist/tex/latex/beamer
%dir %{_texdir}/texmf-dist/tex/latex/beamer/art
%dir %{_texdir}/texmf-dist/tex/latex/beamer-contrib
%dir %{_texdir}/texmf-dist/tex/latex/beamer/emulation
%dir %{_texdir}/texmf-dist/tex/latex/beamer/emulation/examples
%dir %{_texdir}/texmf-dist/tex/latex/beamer-FUBerlin
%dir %{_texdir}/texmf-dist/tex/latex/beamer/multimedia
%dir %{_texdir}/texmf-dist/tex/latex/beamerposter
%dir %{_texdir}/texmf-dist/tex/latex/beamer/themes
%dir %{_texdir}/texmf-dist/tex/latex/beamer/themes/color
%dir %{_texdir}/texmf-dist/tex/latex/beamer/themes/font
%dir %{_texdir}/texmf-dist/tex/latex/beamer/themes/inner
%dir %{_texdir}/texmf-dist/tex/latex/beamer/themes/outer
%dir %{_texdir}/texmf-dist/tex/latex/beamer/themes/theme
%dir %{_texdir}/texmf-dist/tex/latex/beamer/themes/theme/compatibility
%dir %{_texdir}/texmf-dist/tex/latex/beamer/translator
%dir %{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts
%dir %{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-basic-dictionary
%dir %{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-bibliography-dictionary
%dir %{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-environment-dictionary
%dir %{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-months-dictionary
%dir %{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-numbers-dictionary
%dir %{_texdir}/texmf-dist/tex/latex/beamer/translator/dicts/translator-theorem-dictionary
%dir %{_texdir}/texmf-dist/tex/latex/begriff
%dir %{_texdir}/texmf-dist/tex/latex/bera
%dir %{_texdir}/texmf-dist/tex/latex/betababel
%dir %{_texdir}/texmf-dist/tex/latex/beton
%dir %{_texdir}/texmf-dist/tex/latex/bez123
%dir %{_texdir}/texmf-dist/tex/latex/bezos
%dir %{_texdir}/texmf-dist/tex/latex/bgreek
%dir %{_texdir}/texmf-dist/tex/latex/bibarts
%dir %{_texdir}/texmf-dist/tex/latex/biblatex
%dir %{_texdir}/texmf-dist/tex/latex/biblatex-apa
%dir %{_texdir}/texmf-dist/tex/latex/biblatex/bbx
%dir %{_texdir}/texmf-dist/tex/latex/biblatex/cbx
%dir %{_texdir}/texmf-dist/tex/latex/biblatex-chem
%dir %{_texdir}/texmf-dist/tex/latex/biblatex-chem/bbx
%dir %{_texdir}/texmf-dist/tex/latex/biblatex-chem/cbx
%dir %{_texdir}/texmf-dist/tex/latex/biblatex-chicago-notes-df
%dir %{_texdir}/texmf-dist/tex/latex/biblatex-dw
%dir %{_texdir}/texmf-dist/tex/latex/biblatex-dw/bbx
%dir %{_texdir}/texmf-dist/tex/latex/biblatex-dw/cbx
%dir %{_texdir}/texmf-dist/tex/latex/biblatex-dw/lbx
%dir %{_texdir}/texmf-dist/tex/latex/biblatex-historian
%dir %{_texdir}/texmf-dist/tex/latex/biblatex/lbx
%dir %{_texdir}/texmf-dist/tex/latex/biblatex-nature
%dir %{_texdir}/texmf-dist/tex/latex/biblatex-nature/bbx
%dir %{_texdir}/texmf-dist/tex/latex/biblatex-nature/cbx
%dir %{_texdir}/texmf-dist/tex/latex/biblatex-philosophy
%dir %{_texdir}/texmf-dist/tex/latex/biblatex-science
%dir %{_texdir}/texmf-dist/tex/latex/biblatex-science/bbx
%dir %{_texdir}/texmf-dist/tex/latex/biblatex-science/cbx
%dir %{_texdir}/texmf-dist/tex/latex/bibleref
%dir %{_texdir}/texmf-dist/tex/latex/biblist
%dir %{_texdir}/texmf-dist/tex/latex/bibtopic
%dir %{_texdir}/texmf-dist/tex/latex/bibtopicprefix
%dir %{_texdir}/texmf-dist/tex/latex/bibunits
%dir %{_texdir}/texmf-dist/tex/latex/bidi
%dir %{_texdir}/texmf-dist/tex/latex/bigfoot
%dir %{_texdir}/texmf-dist/tex/latex/bigints
%dir %{_texdir}/texmf-dist/tex/latex/binomexp
%dir %{_texdir}/texmf-dist/tex/latex/biocon
%dir %{_texdir}/texmf-dist/tex/latex/bizcard
%dir %{_texdir}/texmf-dist/tex/latex/blacklettert1
%dir %{_texdir}/texmf-dist/tex/latex/blindtext
%dir %{_texdir}/texmf-dist/tex/latex/blkarray
%dir %{_texdir}/texmf-dist/tex/latex/block
%dir %{_texdir}/texmf-dist/tex/latex/blowup
%dir %{_texdir}/texmf-dist/tex/latex/boisik
%dir %{_texdir}/texmf-dist/tex/latex/boites
%dir %{_texdir}/texmf-dist/tex/latex/bold-extra
%dir %{_texdir}/texmf-dist/tex/latex/boldtensors
%dir %{_texdir}/texmf-dist/tex/latex/bookest
%dir %{_texdir}/texmf-dist/tex/latex/bookhands
%dir %{_texdir}/texmf-dist/tex/latex/booklet
%dir %{_texdir}/texmf-dist/tex/latex/bookman
%dir %{_texdir}/texmf-dist/tex/latex/booktabs
%dir %{_texdir}/texmf-dist/tex/latex/boolexpr
%dir %{_texdir}/texmf-dist/tex/latex/bophook
%dir %{_texdir}/texmf-dist/tex/latex/bosisio
%dir %{_texdir}/texmf-dist/tex/latex/boxedminipage
%dir %{_texdir}/texmf-dist/tex/latex/boxhandler
%dir %{_texdir}/texmf-dist/tex/latex/bpchem
%dir %{_texdir}/texmf-dist/tex/latex/bracketkey
%dir %{_texdir}/texmf-dist/tex/latex/braille
%dir %{_texdir}/texmf-dist/tex/latex/braket
%dir %{_texdir}/texmf-dist/tex/latex/breakurl
%dir %{_texdir}/texmf-dist/tex/latex/brushscr
%dir %{_texdir}/texmf-dist/tex/latex/bullcntr
%dir %{_texdir}/texmf-dist/tex/latex/bundledoc
%dir %{_texdir}/texmf-dist/tex/latex/burmese
%dir %{_texdir}/texmf-dist/tex/latex/bussproofs
%dir %{_texdir}/texmf-dist/tex/latex/bytefield
%dir %{_texdir}/texmf-dist/tex/latex/cachepic
%dir %{_texdir}/texmf-dist/tex/latex/calctab
%dir %{_texdir}/texmf-dist/tex/latex/calrsfs
%dir %{_texdir}/texmf-dist/tex/latex/calxxxx
%dir %{_texdir}/texmf-dist/tex/latex/cancel
%dir %{_texdir}/texmf-dist/tex/latex/captcont
%dir %{_texdir}/texmf-dist/tex/latex/captdef
%dir %{_texdir}/texmf-dist/tex/latex/caption
%dir %{_texdir}/texmf-dist/tex/latex/capt-of
%dir %{_texdir}/texmf-dist/tex/latex/carlisle
%dir %{_texdir}/texmf-dist/tex/latex/cases
%dir %{_texdir}/texmf-dist/tex/latex/casyl
%dir %{_texdir}/texmf-dist/tex/latex/catechis
%dir %{_texdir}/texmf-dist/tex/latex/cbcoptic
%dir %{_texdir}/texmf-dist/tex/latex/ccaption
%dir %{_texdir}/texmf-dist/tex/latex/ccfonts
%dir %{_texdir}/texmf-dist/tex/latex/ccicons
%dir %{_texdir}/texmf-dist/tex/latex/cclicenses
%dir %{_texdir}/texmf-dist/tex/latex/cd
%dir %{_texdir}/texmf-dist/tex/latex/cd-cover
%dir %{_texdir}/texmf-dist/tex/latex/cdpbundl
%dir %{_texdir}/texmf-dist/tex/latex/cell
%dir %{_texdir}/texmf-dist/tex/latex/cellspace
%dir %{_texdir}/texmf-dist/tex/latex/cfr-lm
%dir %{_texdir}/texmf-dist/tex/latex/changebar
%dir %{_texdir}/texmf-dist/tex/latex/changelayout
%dir %{_texdir}/texmf-dist/tex/latex/changepage
%dir %{_texdir}/texmf-dist/tex/latex/changes
%dir %{_texdir}/texmf-dist/tex/latex/chappg
%dir %{_texdir}/texmf-dist/tex/latex/chapterfolder
%dir %{_texdir}/texmf-dist/tex/latex/chbibref
%dir %{_texdir}/texmf-dist/tex/latex/chemarrow
%dir %{_texdir}/texmf-dist/tex/latex/chemcompounds
%dir %{_texdir}/texmf-dist/tex/latex/chemcono
%dir %{_texdir}/texmf-dist/tex/latex/chemfig
%dir %{_texdir}/texmf-dist/tex/latex/chemstyle
%dir %{_texdir}/texmf-dist/tex/latex/chemstyle/config
%dir %{_texdir}/texmf-dist/tex/latex/chess
%dir %{_texdir}/texmf-dist/tex/latex/chessboard
%dir %{_texdir}/texmf-dist/tex/latex/chessfss
%dir %{_texdir}/texmf-dist/tex/latex/chess-problem-diagrams
%dir %{_texdir}/texmf-dist/tex/latex/chicago
%dir %{_texdir}/texmf-dist/tex/latex/chletter
%dir %{_texdir}/texmf-dist/tex/latex/chngcntr
%dir %{_texdir}/texmf-dist/tex/latex/chronology
%dir %{_texdir}/texmf-dist/tex/latex/circ
%dir %{_texdir}/texmf-dist/tex/latex/circuitikz
%dir %{_texdir}/texmf-dist/tex/latex/cite
%dir %{_texdir}/texmf-dist/tex/latex/cjhebrew
%dir %{_texdir}/texmf-dist/tex/latex/cjk
%dir %{_texdir}/texmf-dist/tex/latex/cjk/contrib
%dir %{_texdir}/texmf-dist/tex/latex/cjk/contrib/wadalab
%dir %{_texdir}/texmf-dist/tex/latex/cjkpunct
%dir %{_texdir}/texmf-dist/tex/latex/cjk/texinput
%dir %{_texdir}/texmf-dist/tex/latex/cjk/texinput/Bg5
%dir %{_texdir}/texmf-dist/tex/latex/cjk/texinput/CEF
%dir %{_texdir}/texmf-dist/tex/latex/cjk/texinput/CNS
%dir %{_texdir}/texmf-dist/tex/latex/cjk/texinput/GB
%dir %{_texdir}/texmf-dist/tex/latex/cjk/texinput/JIS
%dir %{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS
%dir %{_texdir}/texmf-dist/tex/latex/cjk/texinput/KS/HLaTeX
%dir %{_texdir}/texmf-dist/tex/latex/cjk/texinput/mule
%dir %{_texdir}/texmf-dist/tex/latex/cjk/texinput/SJIS
%dir %{_texdir}/texmf-dist/tex/latex/cjk/texinput/thai
%dir %{_texdir}/texmf-dist/tex/latex/cjk/texinput/UTF8
%dir %{_texdir}/texmf-dist/tex/latex/cjk/utils
%dir %{_texdir}/texmf-dist/tex/latex/cjk/utils/pyhyphen
%dir %{_texdir}/texmf-dist/tex/latex/classicthesis
%dir %{_texdir}/texmf-dist/tex/latex/clefval
%dir %{_texdir}/texmf-dist/tex/latex/cleveref
%dir %{_texdir}/texmf-dist/tex/latex/clock
%dir %{_texdir}/texmf-dist/tex/latex/clrscode
%dir %{_texdir}/texmf-dist/tex/latex/cmap
%dir %{_texdir}/texmf-dist/tex/latex/cmbright
%dir %{_texdir}/texmf-dist/tex/latex/cmdstring
%dir %{_texdir}/texmf-dist/tex/latex/cmdtrack
%dir %{_texdir}/texmf-dist/tex/latex/cm-lgc
%dir %{_texdir}/texmf-dist/tex/latex/cmll
%dir %{_texdir}/texmf-dist/tex/latex/cmsd
%dir %{_texdir}/texmf-dist/tex/latex/cm-super
%dir %{_texdir}/texmf-dist/tex/latex/codedoc
%dir %{_texdir}/texmf-dist/tex/latex/collref
%dir %{_texdir}/texmf-dist/tex/latex/colordoc
%dir %{_texdir}/texmf-dist/tex/latex/colorinfo
%dir %{_texdir}/texmf-dist/tex/latex/colortbl
%dir %{_texdir}/texmf-dist/tex/latex/colorwav
%dir %{_texdir}/texmf-dist/tex/latex/combelow
%dir %{_texdir}/texmf-dist/tex/latex/combine
%dir %{_texdir}/texmf-dist/tex/latex/combinedgraphics
%dir %{_texdir}/texmf-dist/tex/latex/comma
%dir %{_texdir}/texmf-dist/tex/latex/commath
%dir %{_texdir}/texmf-dist/tex/latex/comment
%dir %{_texdir}/texmf-dist/tex/latex/compactbib
%dir %{_texdir}/texmf-dist/tex/latex/complexity
%dir %{_texdir}/texmf-dist/tex/latex/computational-complexity
%dir %{_texdir}/texmf-dist/tex/latex/concmath
%dir %{_texdir}/texmf-dist/tex/latex/concprog
%dir %{_texdir}/texmf-dist/tex/latex/confproc
%dir %{_texdir}/texmf-dist/tex/latex/constants
%dir %{_texdir}/texmf-dist/tex/latex/context
%dir %{_texdir}/texmf-dist/tex/latex/contour
%dir %{_texdir}/texmf-dist/tex/latex/cooking
%dir %{_texdir}/texmf-dist/tex/latex/cookybooky
%dir %{_texdir}/texmf-dist/tex/latex/cool
%dir %{_texdir}/texmf-dist/tex/latex/coollist
%dir %{_texdir}/texmf-dist/tex/latex/coolstr
%dir %{_texdir}/texmf-dist/tex/latex/cooltooltips
%dir %{_texdir}/texmf-dist/tex/latex/coordsys
%dir %{_texdir}/texmf-dist/tex/latex/courier
%dir %{_texdir}/texmf-dist/tex/latex/courier-scaled
%dir %{_texdir}/texmf-dist/tex/latex/courseoutline
%dir %{_texdir}/texmf-dist/tex/latex/coursepaper
%dir %{_texdir}/texmf-dist/tex/latex/coverpage
%dir %{_texdir}/texmf-dist/tex/latex/covington
%dir %{_texdir}/texmf-dist/tex/latex/crop
%dir %{_texdir}/texmf-dist/tex/latex/crossreference
%dir %{_texdir}/texmf-dist/tex/latex/crossword
%dir %{_texdir}/texmf-dist/tex/latex/crosswrd
%dir %{_texdir}/texmf-dist/tex/latex/csbulletin
%dir %{_texdir}/texmf-dist/tex/latex/cslatex
%dir %{_texdir}/texmf-dist/tex/latex/csquotes
%dir %{_texdir}/texmf-dist/tex/latex/csvtools
%dir %{_texdir}/texmf-dist/tex/latex/ctable
%dir %{_texdir}/texmf-dist/tex/latex/ctex
%dir %{_texdir}/texmf-dist/tex/latex/ctex/back
%dir %{_texdir}/texmf-dist/tex/latex/ctex/cfg
%dir %{_texdir}/texmf-dist/tex/latex/ctex/def
%dir %{_texdir}/texmf-dist/tex/latex/ctex/engine
%dir %{_texdir}/texmf-dist/tex/latex/ctex/fd
%dir %{_texdir}/texmf-dist/tex/latex/ctex/fontset
%dir %{_texdir}/texmf-dist/tex/latex/ctex/opt
%dir %{_texdir}/texmf-dist/tex/latex/ctib
%dir %{_texdir}/texmf-dist/tex/latex/cuisine
%dir %{_texdir}/texmf-dist/tex/latex/currfile
%dir %{_texdir}/texmf-dist/tex/latex/currvita
%dir %{_texdir}/texmf-dist/tex/latex/curve
%dir %{_texdir}/texmf-dist/tex/latex/curve2e
%dir %{_texdir}/texmf-dist/tex/latex/curves
%dir %{_texdir}/texmf-dist/tex/latex/custom-bib
%dir %{_texdir}/texmf-dist/tex/latex/cv
%dir %{_texdir}/texmf-dist/tex/latex/cweb-latex
%dir %{_texdir}/texmf-dist/tex/latex/cyklop
%dir %{_texdir}/texmf-dist/tex/latex/cyrillic
%dir %{_texdir}/texmf-dist/tex/latex/dashbox
%dir %{_texdir}/texmf-dist/tex/latex/dashrule
%dir %{_texdir}/texmf-dist/tex/latex/dashundergaps
%dir %{_texdir}/texmf-dist/tex/latex/datatool
%dir %{_texdir}/texmf-dist/tex/latex/dateiliste
%dir %{_texdir}/texmf-dist/tex/latex/datenumber
%dir %{_texdir}/texmf-dist/tex/latex/datetime
%dir %{_texdir}/texmf-dist/tex/latex/dblfloatfix
%dir %{_texdir}/texmf-dist/tex/latex/decimal
%dir %{_texdir}/texmf-dist/tex/latex/delimtxt
%dir %{_texdir}/texmf-dist/tex/latex/diagmac2
%dir %{_texdir}/texmf-dist/tex/latex/diagnose
%dir %{_texdir}/texmf-dist/tex/latex/dichokey
%dir %{_texdir}/texmf-dist/tex/latex/dictsym
%dir %{_texdir}/texmf-dist/tex/latex/digiconfigs
%dir %{_texdir}/texmf-dist/tex/latex/dinbrief
%dir %{_texdir}/texmf-dist/tex/latex/dingbat
%dir %{_texdir}/texmf-dist/tex/latex/directory
%dir %{_texdir}/texmf-dist/tex/latex/disser
%dir %{_texdir}/texmf-dist/tex/latex/dk-bib
%dir %{_texdir}/texmf-dist/tex/latex/dlfltxb
%dir %{_texdir}/texmf-dist/tex/latex/dnaseq
%dir %{_texdir}/texmf-dist/tex/latex/docmfp
%dir %{_texdir}/texmf-dist/tex/latex/docmute
%dir %{_texdir}/texmf-dist/tex/latex/doi
%dir %{_texdir}/texmf-dist/tex/latex/doipubmed
%dir %{_texdir}/texmf-dist/tex/latex/dot2texi
%dir %{_texdir}/texmf-dist/tex/latex/dotarrow
%dir %{_texdir}/texmf-dist/tex/latex/dotseqn
%dir %{_texdir}/texmf-dist/tex/latex/dottex
%dir %{_texdir}/texmf-dist/tex/latex/doublestroke
%dir %{_texdir}/texmf-dist/tex/latex/dox
%dir %{_texdir}/texmf-dist/tex/latex/dozenal
%dir %{_texdir}/texmf-dist/tex/latex/dpfloat
%dir %{_texdir}/texmf-dist/tex/latex/dprogress
%dir %{_texdir}/texmf-dist/tex/latex/drac
%dir %{_texdir}/texmf-dist/tex/latex/draftcopy
%dir %{_texdir}/texmf-dist/tex/latex/draftwatermark
%dir %{_texdir}/texmf-dist/tex/latex/dramatist
%dir %{_texdir}/texmf-dist/tex/latex/drs
%dir %{_texdir}/texmf-dist/tex/latex/dtk
%dir %{_texdir}/texmf-dist/tex/latex/duerer-latex
%dir %{_texdir}/texmf-dist/tex/latex/duotenzor
%dir %{_texdir}/texmf-dist/tex/latex/dvdcoll
%dir %{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl
%dir %{_texdir}/texmf-dist/tex/latex/dvipdfmx-def
%dir %{_texdir}/texmf-dist/tex/latex/dyntree
%dir %{_texdir}/texmf-dist/tex/latex/ean13isbn
%dir %{_texdir}/texmf-dist/tex/latex/easy
%dir %{_texdir}/texmf-dist/tex/latex/easylist
%dir %{_texdir}/texmf-dist/tex/latex/ebezier
%dir %{_texdir}/texmf-dist/tex/latex/ebsthesis
%dir %{_texdir}/texmf-dist/tex/latex/ecclesiastic
%dir %{_texdir}/texmf-dist/tex/latex/ecltree
%dir %{_texdir}/texmf-dist/tex/latex/eco
%dir %{_texdir}/texmf-dist/tex/latex/economic
%dir %{_texdir}/texmf-dist/tex/latex/ecv
%dir %{_texdir}/texmf-dist/tex/latex/ed
%dir %{_texdir}/texmf-dist/tex/latex/edmargin
%dir %{_texdir}/texmf-dist/tex/latex/ednotes
%dir %{_texdir}/texmf-dist/tex/latex/eemeir
%dir %{_texdir}/texmf-dist/tex/latex/eepic
%dir %{_texdir}/texmf-dist/tex/latex/egameps
%dir %{_texdir}/texmf-dist/tex/latex/egplot
%dir %{_texdir}/texmf-dist/tex/latex/eiad-ltx
%dir %{_texdir}/texmf-dist/tex/latex/elbioimp
%dir %{_texdir}/texmf-dist/tex/latex/ellipsis
%dir %{_texdir}/texmf-dist/tex/latex/elmath
%dir %{_texdir}/texmf-dist/tex/latex/elpres
%dir %{_texdir}/texmf-dist/tex/latex/elsarticle
%dir %{_texdir}/texmf-dist/tex/latex/elsevier
%dir %{_texdir}/texmf-dist/tex/latex/eltex
%dir %{_texdir}/texmf-dist/tex/latex/em
%dir %{_texdir}/texmf-dist/tex/latex/emp
%dir %{_texdir}/texmf-dist/tex/latex/emptypage
%dir %{_texdir}/texmf-dist/tex/latex/emulateapj
%dir %{_texdir}/texmf-dist/tex/latex/encxvlna
%dir %{_texdir}/texmf-dist/tex/latex/endfloat
%dir %{_texdir}/texmf-dist/tex/latex/endheads
%dir %{_texdir}/texmf-dist/tex/latex/endnotes
%dir %{_texdir}/texmf-dist/tex/latex/engpron
%dir %{_texdir}/texmf-dist/tex/latex/engrec
%dir %{_texdir}/texmf-dist/tex/latex/engtlc
%dir %{_texdir}/texmf-dist/tex/latex/enumitem
%dir %{_texdir}/texmf-dist/tex/latex/envbig
%dir %{_texdir}/texmf-dist/tex/latex/environ
%dir %{_texdir}/texmf-dist/tex/latex/envlab
%dir %{_texdir}/texmf-dist/tex/latex/epigrafica
%dir %{_texdir}/texmf-dist/tex/latex/epigraph
%dir %{_texdir}/texmf-dist/tex/latex/epiolmec
%dir %{_texdir}/texmf-dist/tex/latex/epsdice
%dir %{_texdir}/texmf-dist/tex/latex/epspdfconversion
%dir %{_texdir}/texmf-dist/tex/latex/eqell
%dir %{_texdir}/texmf-dist/tex/latex/eqlist
%dir %{_texdir}/texmf-dist/tex/latex/eqparbox
%dir %{_texdir}/texmf-dist/tex/latex/erdc
%dir %{_texdir}/texmf-dist/tex/latex/errata
%dir %{_texdir}/texmf-dist/tex/latex/ESIEEcv
%dir %{_texdir}/texmf-dist/tex/latex/esint
%dir %{_texdir}/texmf-dist/tex/latex/esk
%dir %{_texdir}/texmf-dist/tex/latex/eskd
%dir %{_texdir}/texmf-dist/tex/latex/eskdx
%dir %{_texdir}/texmf-dist/tex/latex/eso-pic
%dir %{_texdir}/texmf-dist/tex/latex/estcpmm
%dir %{_texdir}/texmf-dist/tex/latex/esvect
%dir %{_texdir}/texmf-dist/tex/latex/etaremune
%dir %{_texdir}/texmf-dist/tex/latex/etex-pkg
%dir %{_texdir}/texmf-dist/tex/latex/etextools
%dir %{_texdir}/texmf-dist/tex/latex/ethiop
%dir %{_texdir}/texmf-dist/tex/latex/etoolbox
%dir %{_texdir}/texmf-dist/tex/latex/euenc
%dir %{_texdir}/texmf-dist/tex/latex/eukdate
%dir %{_texdir}/texmf-dist/tex/latex/euler
%dir %{_texdir}/texmf-dist/tex/latex/eulervm
%dir %{_texdir}/texmf-dist/tex/latex/euproposal
%dir %{_texdir}/texmf-dist/tex/latex/euro
%dir %{_texdir}/texmf-dist/tex/latex/eurofont
%dir %{_texdir}/texmf-dist/tex/latex/europecv
%dir %{_texdir}/texmf-dist/tex/latex/eurosans
%dir %{_texdir}/texmf-dist/tex/latex/eurosym
%dir %{_texdir}/texmf-dist/tex/latex/everypage
%dir %{_texdir}/texmf-dist/tex/latex/exam
%dir %{_texdir}/texmf-dist/tex/latex/examdesign
%dir %{_texdir}/texmf-dist/tex/latex/examplep
%dir %{_texdir}/texmf-dist/tex/latex/excludeonly
%dir %{_texdir}/texmf-dist/tex/latex/exercise
%dir %{_texdir}/texmf-dist/tex/latex/expdlist
%dir %{_texdir}/texmf-dist/tex/latex/expl3
%dir %{_texdir}/texmf-dist/tex/latex/export
%dir %{_texdir}/texmf-dist/tex/latex/exp-testopt
%dir %{_texdir}/texmf-dist/tex/latex/extarrows
%dir %{_texdir}/texmf-dist/tex/latex/extpfeil
%dir %{_texdir}/texmf-dist/tex/latex/extract
%dir %{_texdir}/texmf-dist/tex/latex/extsizes
%dir %{_texdir}/texmf-dist/tex/latex/facsimile
%dir %{_texdir}/texmf-dist/tex/latex/faktor
%dir %{_texdir}/texmf-dist/tex/latex/fancybox
%dir %{_texdir}/texmf-dist/tex/latex/fancyhdr
%dir %{_texdir}/texmf-dist/tex/latex/fancynum
%dir %{_texdir}/texmf-dist/tex/latex/fancypar
%dir %{_texdir}/texmf-dist/tex/latex/fancyref
%dir %{_texdir}/texmf-dist/tex/latex/fancytooltips
%dir %{_texdir}/texmf-dist/tex/latex/fancyvrb
%dir %{_texdir}/texmf-dist/tex/latex/fc
%dir %{_texdir}/texmf-dist/tex/latex/feyn
%dir %{_texdir}/texmf-dist/tex/latex/feynmf
%dir %{_texdir}/texmf-dist/tex/latex/fge
%dir %{_texdir}/texmf-dist/tex/latex/figbib
%dir %{_texdir}/texmf-dist/tex/latex/figsize
%dir %{_texdir}/texmf-dist/tex/latex/filecontents
%dir %{_texdir}/texmf-dist/tex/latex/filehook
%dir %{_texdir}/texmf-dist/tex/latex/fink
%dir %{_texdir}/texmf-dist/tex/latex/fix2col
%dir %{_texdir}/texmf-dist/tex/latex/fixfoot
%dir %{_texdir}/texmf-dist/tex/latex/fixme
%dir %{_texdir}/texmf-dist/tex/latex/fixme/layouts
%dir %{_texdir}/texmf-dist/tex/latex/fixme/layouts/env
%dir %{_texdir}/texmf-dist/tex/latex/fixme/layouts/target
%dir %{_texdir}/texmf-dist/tex/latex/fixme/themes
%dir %{_texdir}/texmf-dist/tex/latex/flabels
%dir %{_texdir}/texmf-dist/tex/latex/flacards
%dir %{_texdir}/texmf-dist/tex/latex/flagderiv
%dir %{_texdir}/texmf-dist/tex/latex/flashcards
%dir %{_texdir}/texmf-dist/tex/latex/flashmovie
%dir %{_texdir}/texmf-dist/tex/latex/flippdf
%dir %{_texdir}/texmf-dist/tex/latex/float
%dir %{_texdir}/texmf-dist/tex/latex/floatrow
%dir %{_texdir}/texmf-dist/tex/latex/flowfram
%dir %{_texdir}/texmf-dist/tex/latex/fltpage
%dir %{_texdir}/texmf-dist/tex/latex/fmp
%dir %{_texdir}/texmf-dist/tex/latex/fmtcount
%dir %{_texdir}/texmf-dist/tex/latex/fn2end
%dir %{_texdir}/texmf-dist/tex/latex/fnbreak
%dir %{_texdir}/texmf-dist/tex/latex/fncychap
%dir %{_texdir}/texmf-dist/tex/latex/fncylab
%dir %{_texdir}/texmf-dist/tex/latex/fnpara
%dir %{_texdir}/texmf-dist/tex/latex/foekfont
%dir %{_texdir}/texmf-dist/tex/latex/foilhtml
%dir %{_texdir}/texmf-dist/tex/latex/fonetika
%dir %{_texdir}/texmf-dist/tex/latex/fontinst
%dir %{_texdir}/texmf-dist/tex/latex/fontspec
%dir %{_texdir}/texmf-dist/tex/latex/fonttable
%dir %{_texdir}/texmf-dist/tex/latex/footbib
%dir %{_texdir}/texmf-dist/tex/latex/footmisc
%dir %{_texdir}/texmf-dist/tex/latex/footnpag
%dir %{_texdir}/texmf-dist/tex/latex/forarray
%dir %{_texdir}/texmf-dist/tex/latex/forloop
%dir %{_texdir}/texmf-dist/tex/latex/formular
%dir %{_texdir}/texmf-dist/tex/latex/fouridx
%dir %{_texdir}/texmf-dist/tex/latex/fourier
%dir %{_texdir}/texmf-dist/tex/latex/fouriernc
%dir %{_texdir}/texmf-dist/tex/latex/fp
%dir %{_texdir}/texmf-dist/tex/latex/fragments
%dir %{_texdir}/texmf-dist/tex/latex/framed
%dir %{_texdir}/texmf-dist/tex/latex/frankenstein
%dir %{_texdir}/texmf-dist/tex/latex/frcursive
%dir %{_texdir}/texmf-dist/tex/latex/frenchle
%dir %{_texdir}/texmf-dist/tex/latex/fribrief
%dir %{_texdir}/texmf-dist/tex/latex/frletter
%dir %{_texdir}/texmf-dist/tex/latex/frontespizio
%dir %{_texdir}/texmf-dist/tex/latex/ftcap
%dir %{_texdir}/texmf-dist/tex/latex/ftnxtra
%dir %{_texdir}/texmf-dist/tex/latex/functan
%dir %{_texdir}/texmf-dist/tex/latex/fundus
%dir %{_texdir}/texmf-dist/tex/latex/gaceta
%dir %{_texdir}/texmf-dist/tex/latex/galois
%dir %{_texdir}/texmf-dist/tex/latex/gastex
%dir %{_texdir}/texmf-dist/tex/latex/gatech-thesis
%dir %{_texdir}/texmf-dist/tex/latex/gauss
%dir %{_texdir}/texmf-dist/tex/latex/gb4e
%dir %{_texdir}/texmf-dist/tex/latex/g-brief
%dir %{_texdir}/texmf-dist/tex/latex/gcard
%dir %{_texdir}/texmf-dist/tex/latex/gchords
%dir %{_texdir}/texmf-dist/tex/latex/gcite
%dir %{_texdir}/texmf-dist/tex/latex/gene-logic
%dir %{_texdir}/texmf-dist/tex/latex/genmpage
%dir %{_texdir}/texmf-dist/tex/latex/geometry
%dir %{_texdir}/texmf-dist/tex/latex/germkorr
%dir %{_texdir}/texmf-dist/tex/latex/getfiledate
%dir %{_texdir}/texmf-dist/tex/latex/gfsartemisia
%dir %{_texdir}/texmf-dist/tex/latex/gfsbaskerville
%dir %{_texdir}/texmf-dist/tex/latex/gfsbodoni
%dir %{_texdir}/texmf-dist/tex/latex/gfscomplutum
%dir %{_texdir}/texmf-dist/tex/latex/gfsdidot
%dir %{_texdir}/texmf-dist/tex/latex/gfsneohellenic
%dir %{_texdir}/texmf-dist/tex/latex/gfsporson
%dir %{_texdir}/texmf-dist/tex/latex/gfssolomos
%dir %{_texdir}/texmf-dist/tex/latex/ginpenc
%dir %{_texdir}/texmf-dist/tex/latex/gloss
%dir %{_texdir}/texmf-dist/tex/latex/glossaries
%dir %{_texdir}/texmf-dist/tex/latex/glossaries/base
%dir %{_texdir}/texmf-dist/tex/latex/glossaries/dict
%dir %{_texdir}/texmf-dist/tex/latex/glossaries/expl
%dir %{_texdir}/texmf-dist/tex/latex/glossaries/styles
%dir %{_texdir}/texmf-dist/tex/latex/gmdoc
%dir %{_texdir}/texmf-dist/tex/latex/gmdoc-enhance
%dir %{_texdir}/texmf-dist/tex/latex/gmeometric
%dir %{_texdir}/texmf-dist/tex/latex/gmiflink
%dir %{_texdir}/texmf-dist/tex/latex/gmutils
%dir %{_texdir}/texmf-dist/tex/latex/gmverb
%dir %{_texdir}/texmf-dist/tex/latex/gmverse
%dir %{_texdir}/texmf-dist/tex/latex/gnuplottex
%dir %{_texdir}/texmf-dist/tex/latex/go
%dir %{_texdir}/texmf-dist/tex/latex/graphics
%dir %{_texdir}/texmf-dist/tex/latex/graphicx-psmin
%dir %{_texdir}/texmf-dist/tex/latex/greekdates
%dir %{_texdir}/texmf-dist/tex/latex/greek-inputenc
%dir %{_texdir}/texmf-dist/tex/latex/greektex
%dir %{_texdir}/texmf-dist/tex/latex/grfpaste
%dir %{_texdir}/texmf-dist/tex/latex/grid
%dir %{_texdir}/texmf-dist/tex/latex/gridset
%dir %{_texdir}/texmf-dist/tex/latex/grotesq
%dir %{_texdir}/texmf-dist/tex/latex/grverb
%dir %{_texdir}/texmf-dist/tex/latex/gu
%dir %{_texdir}/texmf-dist/tex/latex/guitar
%dir %{_texdir}/texmf-dist/tex/latex/guitlogo
%dir %{_texdir}/texmf-dist/tex/latex/hanging
%dir %{_texdir}/texmf-dist/tex/latex/HA-prosper
%dir %{_texdir}/texmf-dist/tex/latex/HA-prosper/Styles
%dir %{_texdir}/texmf-dist/tex/latex/HA-prosper/Styles/Aggie
%dir %{_texdir}/texmf-dist/tex/latex/HA-prosper/Styles/Capsules
%dir %{_texdir}/texmf-dist/tex/latex/HA-prosper/Styles/Ciment
%dir %{_texdir}/texmf-dist/tex/latex/HA-prosper/Styles/Fyma
%dir %{_texdir}/texmf-dist/tex/latex/HA-prosper/Styles/HA
%dir %{_texdir}/texmf-dist/tex/latex/HA-prosper/Styles/Lakar
%dir %{_texdir}/texmf-dist/tex/latex/HA-prosper/Styles/Simple
%dir %{_texdir}/texmf-dist/tex/latex/HA-prosper/Styles/TCS
%dir %{_texdir}/texmf-dist/tex/latex/HA-prosper/Styles/Tycja
%dir %{_texdir}/texmf-dist/tex/latex/har2nat
%dir %{_texdir}/texmf-dist/tex/latex/harmony
%dir %{_texdir}/texmf-dist/tex/latex/harpoon
%dir %{_texdir}/texmf-dist/tex/latex/harvard
%dir %{_texdir}/texmf-dist/tex/latex/hc
%dir %{_texdir}/texmf-dist/tex/latex/helvetic
%dir %{_texdir}/texmf-dist/tex/latex/hep
%dir %{_texdir}/texmf-dist/tex/latex/hepnames
%dir %{_texdir}/texmf-dist/tex/latex/hepparticles
%dir %{_texdir}/texmf-dist/tex/latex/hepthesis
%dir %{_texdir}/texmf-dist/tex/latex/hepunits
%dir %{_texdir}/texmf-dist/tex/latex/here
%dir %{_texdir}/texmf-dist/tex/latex/hexgame
%dir %{_texdir}/texmf-dist/tex/latex/hfoldsty
%dir %{_texdir}/texmf-dist/tex/latex/hhtensor
%dir %{_texdir}/texmf-dist/tex/latex/histogr
%dir %{_texdir}/texmf-dist/tex/latex/historische-zeitschrift
%dir %{_texdir}/texmf-dist/tex/latex/historische-zeitschrift/bbx
%dir %{_texdir}/texmf-dist/tex/latex/historische-zeitschrift/cbx
%dir %{_texdir}/texmf-dist/tex/latex/historische-zeitschrift/lbx
%dir %{_texdir}/texmf-dist/tex/latex/hitec
%dir %{_texdir}/texmf-dist/tex/latex/hpsdiss
%dir %{_texdir}/texmf-dist/tex/latex/hrlatex
%dir %{_texdir}/texmf-dist/tex/latex/hvfloat
%dir %{_texdir}/texmf-dist/tex/latex/hvindex
%dir %{_texdir}/texmf-dist/tex/latex/hypdvips
%dir %{_texdir}/texmf-dist/tex/latex/hyper
%dir %{_texdir}/texmf-dist/tex/latex/hypernat
%dir %{_texdir}/texmf-dist/tex/latex/hyperref
%dir %{_texdir}/texmf-dist/tex/latex/hyperxmp
%dir %{_texdir}/texmf-dist/tex/latex/hyphenat
%dir %{_texdir}/texmf-dist/tex/latex/ibycus-babel
%dir %{_texdir}/texmf-dist/tex/latex/icsv
%dir %{_texdir}/texmf-dist/tex/latex/idxlayout
%dir %{_texdir}/texmf-dist/tex/latex/IEEEconf
%dir %{_texdir}/texmf-dist/tex/latex/ieeepes
%dir %{_texdir}/texmf-dist/tex/latex/IEEEtran
%dir %{_texdir}/texmf-dist/tex/latex/ifmslide
%dir %{_texdir}/texmf-dist/tex/latex/ifmtarg
%dir %{_texdir}/texmf-dist/tex/latex/ifplatform
%dir %{_texdir}/texmf-dist/tex/latex/ifsym
%dir %{_texdir}/texmf-dist/tex/latex/ijmart
%dir %{_texdir}/texmf-dist/tex/latex/imac
%dir %{_texdir}/texmf-dist/tex/latex/image-gallery
%dir %{_texdir}/texmf-dist/tex/latex/imakeidx
%dir %{_texdir}/texmf-dist/tex/latex/import
%dir %{_texdir}/texmf-dist/tex/latex/imtekda
%dir %{_texdir}/texmf-dist/tex/latex/inconsolata
%dir %{_texdir}/texmf-dist/tex/latex/index
%dir %{_texdir}/texmf-dist/tex/latex/initials
%dir %{_texdir}/texmf-dist/tex/latex/inlinebib
%dir %{_texdir}/texmf-dist/tex/latex/inlinedef
%dir %{_texdir}/texmf-dist/tex/latex/interactiveworkbook
%dir %{_texdir}/texmf-dist/tex/latex/inversepath
%dir %{_texdir}/texmf-dist/tex/latex/ionumbers
%dir %{_texdir}/texmf-dist/tex/latex/iso
%dir %{_texdir}/texmf-dist/tex/latex/iso10303
%dir %{_texdir}/texmf-dist/tex/latex/isodate
%dir %{_texdir}/texmf-dist/tex/latex/isodoc
%dir %{_texdir}/texmf-dist/tex/latex/isomath
%dir %{_texdir}/texmf-dist/tex/latex/isonums
%dir %{_texdir}/texmf-dist/tex/latex/isorot
%dir %{_texdir}/texmf-dist/tex/latex/isotope
%dir %{_texdir}/texmf-dist/tex/latex/itnumpar
%dir %{_texdir}/texmf-dist/tex/latex/itrans
%dir %{_texdir}/texmf-dist/tex/latex/iwona
%dir %{_texdir}/texmf-dist/tex/latex/jeopardy
%dir %{_texdir}/texmf-dist/tex/latex/jknapltx
%dir %{_texdir}/texmf-dist/tex/latex/jmlr
%dir %{_texdir}/texmf-dist/tex/latex/jneurosci
%dir %{_texdir}/texmf-dist/tex/latex/jpsj
%dir %{_texdir}/texmf-dist/tex/latex/jura
%dir %{_texdir}/texmf-dist/tex/latex/juraabbrev
%dir %{_texdir}/texmf-dist/tex/latex/jurabib
%dir %{_texdir}/texmf-dist/tex/latex/juramisc
%dir %{_texdir}/texmf-dist/tex/latex/jurarsp
%dir %{_texdir}/texmf-dist/tex/latex/kalender
%dir %{_texdir}/texmf-dist/tex/latex/karnaugh
%dir %{_texdir}/texmf-dist/tex/latex/kerkis
%dir %{_texdir}/texmf-dist/tex/latex/kerntest
%dir %{_texdir}/texmf-dist/tex/latex/keycommand
%dir %{_texdir}/texmf-dist/tex/latex/keystroke
%dir %{_texdir}/texmf-dist/tex/latex/kluwer
%dir %{_texdir}/texmf-dist/tex/latex/knitting
%dir %{_texdir}/texmf-dist/tex/latex/knittingpattern
%dir %{_texdir}/texmf-dist/tex/latex/koma-script
%dir %{_texdir}/texmf-dist/tex/latex/kpfonts
%dir %{_texdir}/texmf-dist/tex/latex/kurier
%dir %{_texdir}/texmf-dist/tex/latex/labbook
%dir %{_texdir}/texmf-dist/tex/latex/labelcas
%dir %{_texdir}/texmf-dist/tex/latex/labels
%dir %{_texdir}/texmf-dist/tex/latex/lastpage
%dir %{_texdir}/texmf-dist/tex/latex/latex2man
%dir %{_texdir}/texmf-dist/tex/latex/latexconfig
%dir %{_texdir}/texmf-dist/tex/latex/layaureo
%dir %{_texdir}/texmf-dist/tex/latex/layouts
%dir %{_texdir}/texmf-dist/tex/latex/lazylist
%dir %{_texdir}/texmf-dist/tex/latex/lcd
%dir %{_texdir}/texmf-dist/tex/latex/lcg
%dir %{_texdir}/texmf-dist/tex/latex/lcyw
%dir %{_texdir}/texmf-dist/tex/latex/leading
%dir %{_texdir}/texmf-dist/tex/latex/leaflet
%dir %{_texdir}/texmf-dist/tex/latex/ledmac
%dir %{_texdir}/texmf-dist/tex/latex/leftidx
%dir %{_texdir}/texmf-dist/tex/latex/lettre
%dir %{_texdir}/texmf-dist/tex/latex/lettrine
%dir %{_texdir}/texmf-dist/tex/latex/lewis
%dir %{_texdir}/texmf-dist/tex/latex/lexikon
%dir %{_texdir}/texmf-dist/tex/latex/lh
%dir %{_texdir}/texmf-dist/tex/latex/lhcyr
%dir %{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyralt
%dir %{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrkoi
%dir %{_texdir}/texmf-dist/tex/latex/lhcyr/lhcyrwin
%dir %{_texdir}/texmf-dist/tex/latex/lhelp
%dir %{_texdir}/texmf-dist/tex/latex/libertine
%dir %{_texdir}/texmf-dist/tex/latex/libris
%dir %{_texdir}/texmf-dist/tex/latex/limap
%dir %{_texdir}/texmf-dist/tex/latex/linearA
%dir %{_texdir}/texmf-dist/tex/latex/linegoal
%dir %{_texdir}/texmf-dist/tex/latex/lineno
%dir %{_texdir}/texmf-dist/tex/latex/linguex
%dir %{_texdir}/texmf-dist/tex/latex/lipsum
%dir %{_texdir}/texmf-dist/tex/latex/listbib
%dir %{_texdir}/texmf-dist/tex/latex/listing
%dir %{_texdir}/texmf-dist/tex/latex/listings
%dir %{_texdir}/texmf-dist/tex/latex/listings-ext
%dir %{_texdir}/texmf-dist/tex/latex/listliketab
%dir %{_texdir}/texmf-dist/tex/latex/listofsymbols
%dir %{_texdir}/texmf-dist/tex/latex/lithuanian
%dir %{_texdir}/texmf-dist/tex/latex/liturg
%dir %{_texdir}/texmf-dist/tex/latex/lkproof
%dir %{_texdir}/texmf-dist/tex/latex/lm
%dir %{_texdir}/texmf-dist/tex/latex/locality
%dir %{_texdir}/texmf-dist/tex/latex/localloc
%dir %{_texdir}/texmf-dist/tex/latex/logical-markup-utils
%dir %{_texdir}/texmf-dist/tex/latex/logpap
%dir %{_texdir}/texmf-dist/tex/latex/lps
%dir %{_texdir}/texmf-dist/tex/latex/lsc
%dir %{_texdir}/texmf-dist/tex/latex/ltabptch
%dir %{_texdir}/texmf-dist/tex/latex/ltxdockit
%dir %{_texdir}/texmf-dist/tex/latex/ltxindex
%dir %{_texdir}/texmf-dist/tex/latex/ltxmisc
%dir %{_texdir}/texmf-dist/tex/latex/ltxnew
%dir %{_texdir}/texmf-dist/tex/latex/lxfonts
%dir %{_texdir}/texmf-dist/tex/latex/ly1
%dir %{_texdir}/texmf-dist/tex/latex/macqassign
%dir %{_texdir}/texmf-dist/tex/latex/mafr
%dir %{_texdir}/texmf-dist/tex/latex/magaz
%dir %{_texdir}/texmf-dist/tex/latex/mailing
%dir %{_texdir}/texmf-dist/tex/latex/mailmerge
%dir %{_texdir}/texmf-dist/tex/latex/makebarcode
%dir %{_texdir}/texmf-dist/tex/latex/makebox
%dir %{_texdir}/texmf-dist/tex/latex/makecell
%dir %{_texdir}/texmf-dist/tex/latex/makecmds
%dir %{_texdir}/texmf-dist/tex/latex/makedtx
%dir %{_texdir}/texmf-dist/tex/latex/makeglos
%dir %{_texdir}/texmf-dist/tex/latex/makeplot
%dir %{_texdir}/texmf-dist/tex/latex/manfnt
%dir %{_texdir}/texmf-dist/tex/latex/manuscript
%dir %{_texdir}/texmf-dist/tex/latex/mapcodes
%dir %{_texdir}/texmf-dist/tex/latex/margbib
%dir %{_texdir}/texmf-dist/tex/latex/marginnote
%dir %{_texdir}/texmf-dist/tex/latex/marvosym
%dir %{_texdir}/texmf-dist/tex/latex/mathcomp
%dir %{_texdir}/texmf-dist/tex/latex/mathdesign
%dir %{_texdir}/texmf-dist/tex/latex/mathdesign/mdbch
%dir %{_texdir}/texmf-dist/tex/latex/mathdesign/mdput
%dir %{_texdir}/texmf-dist/tex/latex/mathdesign/mdugm
%dir %{_texdir}/texmf-dist/tex/latex/mathexam
%dir %{_texdir}/texmf-dist/tex/latex/mathspic
%dir %{_texdir}/texmf-dist/tex/latex/mattens
%dir %{_texdir}/texmf-dist/tex/latex/maybemath
%dir %{_texdir}/texmf-dist/tex/latex/mcaption
%dir %{_texdir}/texmf-dist/tex/latex/mceinleger
%dir %{_texdir}/texmf-dist/tex/latex/mcite
%dir %{_texdir}/texmf-dist/tex/latex/mciteplus
%dir %{_texdir}/texmf-dist/tex/latex/mdframed
%dir %{_texdir}/texmf-dist/tex/latex/mdwtools
%dir %{_texdir}/texmf-dist/tex/latex/memexsupp
%dir %{_texdir}/texmf-dist/tex/latex/memoir
%dir %{_texdir}/texmf-dist/tex/latex/mentis
%dir %{_texdir}/texmf-dist/tex/latex/menu
%dir %{_texdir}/texmf-dist/tex/latex/metalogo
%dir %{_texdir}/texmf-dist/tex/latex/method
%dir %{_texdir}/texmf-dist/tex/latex/metre
%dir %{_texdir}/texmf-dist/tex/latex/mflogo
%dir %{_texdir}/texmf-dist/tex/latex/mfnfss
%dir %{_texdir}/texmf-dist/tex/latex/mfpic4ode
%dir %{_texdir}/texmf-dist/tex/latex/mftinc
%dir %{_texdir}/texmf-dist/tex/latex/mh
%dir %{_texdir}/texmf-dist/tex/latex/mhchem
%dir %{_texdir}/texmf-dist/tex/latex/mhequ
%dir %{_texdir}/texmf-dist/tex/latex/mhs
%dir %{_texdir}/texmf-dist/tex/latex/microtype
%dir %{_texdir}/texmf-dist/tex/latex/midpage
%dir %{_texdir}/texmf-dist/tex/latex/miller
%dir %{_texdir}/texmf-dist/tex/latex/minibox
%dir %{_texdir}/texmf-dist/tex/latex/minipage-marginpar
%dir %{_texdir}/texmf-dist/tex/latex/miniplot
%dir %{_texdir}/texmf-dist/tex/latex/minitoc
%dir %{_texdir}/texmf-dist/tex/latex/minted
%dir %{_texdir}/texmf-dist/tex/latex/minutes
%dir %{_texdir}/texmf-dist/tex/latex/misc209
%dir %{_texdir}/texmf-dist/tex/latex/mla-paper
%dir %{_texdir}/texmf-dist/tex/latex/mlist
%dir %{_texdir}/texmf-dist/tex/latex/mltex
%dir %{_texdir}/texmf-dist/tex/latex/mmap
%dir %{_texdir}/texmf-dist/tex/latex/mnsymbol
%dir %{_texdir}/texmf-dist/tex/latex/moderncv
%dir %{_texdir}/texmf-dist/tex/latex/modref
%dir %{_texdir}/texmf-dist/tex/latex/modroman
%dir %{_texdir}/texmf-dist/tex/latex/mongolian-babel
%dir %{_texdir}/texmf-dist/tex/latex/montex
%dir %{_texdir}/texmf-dist/tex/latex/morefloats
%dir %{_texdir}/texmf-dist/tex/latex/moresize
%dir %{_texdir}/texmf-dist/tex/latex/moreverb
%dir %{_texdir}/texmf-dist/tex/latex/movie15
%dir %{_texdir}/texmf-dist/tex/latex/mparhack
%dir %{_texdir}/texmf-dist/tex/latex/ms
%dir %{_texdir}/texmf-dist/tex/latex/msc
%dir %{_texdir}/texmf-dist/tex/latex/msg
%dir %{_texdir}/texmf-dist/tex/latex/mslapa
%dir %{_texdir}/texmf-dist/tex/latex/mtgreek
%dir %{_texdir}/texmf-dist/tex/latex/muench
%dir %{_texdir}/texmf-dist/tex/latex/muench/hrefhide
%dir %{_texdir}/texmf-dist/tex/latex/multibbl
%dir %{_texdir}/texmf-dist/tex/latex/multibib
%dir %{_texdir}/texmf-dist/tex/latex/multicap
%dir %{_texdir}/texmf-dist/tex/latex/multido
%dir %{_texdir}/texmf-dist/tex/latex/multiobjective
%dir %{_texdir}/texmf-dist/tex/latex/multirow
%dir %{_texdir}/texmf-dist/tex/latex/muthesis
%dir %{_texdir}/texmf-dist/tex/latex/mwcls
%dir %{_texdir}/texmf-dist/tex/latex/mylatexformat
%dir %{_texdir}/texmf-dist/tex/latex/nag
%dir %{_texdir}/texmf-dist/tex/latex/namespc
%dir %{_texdir}/texmf-dist/tex/latex/natbib
%dir %{_texdir}/texmf-dist/tex/latex/nath
%dir %{_texdir}/texmf-dist/tex/latex/ncclatex
%dir %{_texdir}/texmf-dist/tex/latex/ncctools
%dir %{_texdir}/texmf-dist/tex/latex/ncntrsbk
%dir %{_texdir}/texmf-dist/tex/latex/nddiss
%dir %{_texdir}/texmf-dist/tex/latex/needspace
%dir %{_texdir}/texmf-dist/tex/latex/newfile
%dir %{_texdir}/texmf-dist/tex/latex/newlfm
%dir %{_texdir}/texmf-dist/tex/latex/newspaper
%dir %{_texdir}/texmf-dist/tex/latex/newvbtm
%dir %{_texdir}/texmf-dist/tex/latex/newverbs
%dir %{_texdir}/texmf-dist/tex/latex/nextpage
%dir %{_texdir}/texmf-dist/tex/latex/nfssext-cfr
%dir %{_texdir}/texmf-dist/tex/latex/niceframe
%dir %{_texdir}/texmf-dist/tex/latex/nicetext
%dir %{_texdir}/texmf-dist/tex/latex/nih
%dir %{_texdir}/texmf-dist/tex/latex/nlctdoc
%dir %{_texdir}/texmf-dist/tex/latex/noitcrul
%dir %{_texdir}/texmf-dist/tex/latex/nolbreaks
%dir %{_texdir}/texmf-dist/tex/latex/nomencl
%dir %{_texdir}/texmf-dist/tex/latex/nomentbl
%dir %{_texdir}/texmf-dist/tex/latex/nonfloat
%dir %{_texdir}/texmf-dist/tex/latex/nopageno
%dir %{_texdir}/texmf-dist/tex/latex/nostarch
%dir %{_texdir}/texmf-dist/tex/latex/notes
%dir %{_texdir}/texmf-dist/tex/latex/notes2bib
%dir %{_texdir}/texmf-dist/tex/latex/notoccite
%dir %{_texdir}/texmf-dist/tex/latex/nrc
%dir %{_texdir}/texmf-dist/tex/latex/ntabbing
%dir %{_texdir}/texmf-dist/tex/latex/ntgclass
%dir %{_texdir}/texmf-dist/tex/latex/ntheorem
%dir %{_texdir}/texmf-dist/tex/latex/numname
%dir %{_texdir}/texmf-dist/tex/latex/numprint
%dir %{_texdir}/texmf-dist/tex/latex/oberdiek
%dir %{_texdir}/texmf-dist/tex/latex/objectz
%dir %{_texdir}/texmf-dist/tex/latex/ocgtools
%dir %{_texdir}/texmf-dist/tex/latex/ocr-latex
%dir %{_texdir}/texmf-dist/tex/latex/octavo
%dir %{_texdir}/texmf-dist/tex/latex/oldstyle
%dir %{_texdir}/texmf-dist/tex/latex/onlyamsmath
%dir %{_texdir}/texmf-dist/tex/latex/onrannual
%dir %{_texdir}/texmf-dist/tex/latex/opcit
%dir %{_texdir}/texmf-dist/tex/latex/optional
%dir %{_texdir}/texmf-dist/tex/latex/ordinalpt
%dir %{_texdir}/texmf-dist/tex/latex/othello
%dir %{_texdir}/texmf-dist/tex/latex/otibet
%dir %{_texdir}/texmf-dist/tex/latex/ot-tableau
%dir %{_texdir}/texmf-dist/tex/latex/outline
%dir %{_texdir}/texmf-dist/tex/latex/outliner
%dir %{_texdir}/texmf-dist/tex/latex/overpic
%dir %{_texdir}/texmf-dist/tex/latex/pacioli
%dir %{_texdir}/texmf-dist/tex/latex/pagecont
%dir %{_texdir}/texmf-dist/tex/latex/pagenote
%dir %{_texdir}/texmf-dist/tex/latex/pagerange
%dir %{_texdir}/texmf-dist/tex/latex/pageslts
%dir %{_texdir}/texmf-dist/tex/latex/palatino
%dir %{_texdir}/texmf-dist/tex/latex/paper
%dir %{_texdir}/texmf-dist/tex/latex/papercdcase
%dir %{_texdir}/texmf-dist/tex/latex/papermas
%dir %{_texdir}/texmf-dist/tex/latex/papertex
%dir %{_texdir}/texmf-dist/tex/latex/paralist
%dir %{_texdir}/texmf-dist/tex/latex/parallel
%dir %{_texdir}/texmf-dist/tex/latex/paresse
%dir %{_texdir}/texmf-dist/tex/latex/parrun
%dir %{_texdir}/texmf-dist/tex/latex/patchcmd
%dir %{_texdir}/texmf-dist/tex/latex/pauldoc
%dir %{_texdir}/texmf-dist/tex/latex/pawpict
%dir %{_texdir}/texmf-dist/tex/latex/pax
%dir %{_texdir}/texmf-dist/tex/latex/pb-diagram
%dir %{_texdir}/texmf-dist/tex/latex/pbox
%dir %{_texdir}/texmf-dist/tex/latex/pbsheet
%dir %{_texdir}/texmf-dist/tex/latex/pclnfss
%dir %{_texdir}/texmf-dist/tex/latex/pdf14
%dir %{_texdir}/texmf-dist/tex/latex/pdfcomment
%dir %{_texdir}/texmf-dist/tex/latex/pdfcprot
%dir %{_texdir}/texmf-dist/tex/latex/pdfmarginpar
%dir %{_texdir}/texmf-dist/tex/latex/pdfpages
%dir %{_texdir}/texmf-dist/tex/latex/pdfscreen
%dir %{_texdir}/texmf-dist/tex/latex/pdfslide
%dir %{_texdir}/texmf-dist/tex/latex/pdfsync
%dir %{_texdir}/texmf-dist/tex/latex/pdftex-def
%dir %{_texdir}/texmf-dist/tex/latex/pdftricks
%dir %{_texdir}/texmf-dist/tex/latex/pdfwin
%dir %{_texdir}/texmf-dist/tex/latex/pdfx
%dir %{_texdir}/texmf-dist/tex/latex/pecha
%dir %{_texdir}/texmf-dist/tex/latex/perltex
%dir %{_texdir}/texmf-dist/tex/latex/permute
%dir %{_texdir}/texmf-dist/tex/latex/petiteannonce
%dir %{_texdir}/texmf-dist/tex/latex/petri-nets
%dir %{_texdir}/texmf-dist/tex/latex/pgf
%dir %{_texdir}/texmf-dist/tex/latex/pgf/basiclayer
%dir %{_texdir}/texmf-dist/tex/latex/pgf/compatibility
%dir %{_texdir}/texmf-dist/tex/latex/pgf/frontendlayer
%dir %{_texdir}/texmf-dist/tex/latex/pgf/math
%dir %{_texdir}/texmf-dist/tex/latex/pgfopts
%dir %{_texdir}/texmf-dist/tex/latex/pgfplots
%dir %{_texdir}/texmf-dist/tex/latex/pgfplots/libs
%dir %{_texdir}/texmf-dist/tex/latex/pgf-soroban
%dir %{_texdir}/texmf-dist/tex/latex/pgf/systemlayer
%dir %{_texdir}/texmf-dist/tex/latex/pgf-umlsd
%dir %{_texdir}/texmf-dist/tex/latex/pgf/utilities
%dir %{_texdir}/texmf-dist/tex/latex/phaistos
%dir %{_texdir}/texmf-dist/tex/latex/philex
%dir %{_texdir}/texmf-dist/tex/latex/philosophersimprint
%dir %{_texdir}/texmf-dist/tex/latex/photo
%dir %{_texdir}/texmf-dist/tex/latex/picinpar
%dir %{_texdir}/texmf-dist/tex/latex/pict2e
%dir %{_texdir}/texmf-dist/tex/latex/pictex2
%dir %{_texdir}/texmf-dist/tex/latex/pigpen
%dir %{_texdir}/texmf-dist/tex/latex/pinlabel
%dir %{_texdir}/texmf-dist/tex/latex/pittetd
%dir %{_texdir}/texmf-dist/tex/latex/placeins
%dir %{_texdir}/texmf-dist/tex/latex/plantslabels
%dir %{_texdir}/texmf-dist/tex/latex/plari
%dir %{_texdir}/texmf-dist/tex/latex/plates
%dir %{_texdir}/texmf-dist/tex/latex/play
%dir %{_texdir}/texmf-dist/tex/latex/plweb
%dir %{_texdir}/texmf-dist/tex/latex/pmgraph
%dir %{_texdir}/texmf-dist/tex/latex/poemscol
%dir %{_texdir}/texmf-dist/tex/latex/polski
%dir %{_texdir}/texmf-dist/tex/latex/polyglot
%dir %{_texdir}/texmf-dist/tex/latex/polynom
%dir %{_texdir}/texmf-dist/tex/latex/polynomial
%dir %{_texdir}/texmf-dist/tex/latex/polytable
%dir %{_texdir}/texmf-dist/tex/latex/postcards
%dir %{_texdir}/texmf-dist/tex/latex/powerdot
%dir %{_texdir}/texmf-dist/tex/latex/powerdot-FUBerlin
%dir %{_texdir}/texmf-dist/tex/latex/ppower4
%dir %{_texdir}/texmf-dist/tex/latex/ppr-prv
%dir %{_texdir}/texmf-dist/tex/latex/pracjourn
%dir %{_texdir}/texmf-dist/tex/latex/preprint
%dir %{_texdir}/texmf-dist/tex/latex/prerex
%dir %{_texdir}/texmf-dist/tex/latex/prettyref
%dir %{_texdir}/texmf-dist/tex/latex/preview
%dir %{_texdir}/texmf-dist/tex/latex/printlen
%dir %{_texdir}/texmf-dist/tex/latex/proba
%dir %{_texdir}/texmf-dist/tex/latex/probsoln
%dir %{_texdir}/texmf-dist/tex/latex/procIAGssymp
%dir %{_texdir}/texmf-dist/tex/latex/program
%dir %{_texdir}/texmf-dist/tex/latex/progress
%dir %{_texdir}/texmf-dist/tex/latex/properties
%dir %{_texdir}/texmf-dist/tex/latex/prosper
%dir %{_texdir}/texmf-dist/tex/latex/protex
%dir %{_texdir}/texmf-dist/tex/latex/protocol
%dir %{_texdir}/texmf-dist/tex/latex/psbao
%dir %{_texdir}/texmf-dist/tex/latex/pseudocode
%dir %{_texdir}/texmf-dist/tex/latex/psfrag
%dir %{_texdir}/texmf-dist/tex/latex/psfragx
%dir %{_texdir}/texmf-dist/tex/latex/psgo
%dir %{_texdir}/texmf-dist/tex/latex/pslatex
%dir %{_texdir}/texmf-dist/tex/latex/psnfss
%dir %{_texdir}/texmf-dist/tex/latex/pspicture
%dir %{_texdir}/texmf-dist/tex/latex/pst-2dplot
%dir %{_texdir}/texmf-dist/tex/latex/pst-3d
%dir %{_texdir}/texmf-dist/tex/latex/pst-3dplot
%dir %{_texdir}/texmf-dist/tex/latex/pst-abspos
%dir %{_texdir}/texmf-dist/tex/latex/pst-am
%dir %{_texdir}/texmf-dist/tex/latex/pst-asr
%dir %{_texdir}/texmf-dist/tex/latex/pst-bar
%dir %{_texdir}/texmf-dist/tex/latex/pst-barcode
%dir %{_texdir}/texmf-dist/tex/latex/pst-bezier
%dir %{_texdir}/texmf-dist/tex/latex/pst-blur
%dir %{_texdir}/texmf-dist/tex/latex/pst-bspline
%dir %{_texdir}/texmf-dist/tex/latex/pst-calendar
%dir %{_texdir}/texmf-dist/tex/latex/pst-circ
%dir %{_texdir}/texmf-dist/tex/latex/pst-coil
%dir %{_texdir}/texmf-dist/tex/latex/pst-cox
%dir %{_texdir}/texmf-dist/tex/latex/pst-dbicons
%dir %{_texdir}/texmf-dist/tex/latex/pst-diffraction
%dir %{_texdir}/texmf-dist/tex/latex/pst-electricfield
%dir %{_texdir}/texmf-dist/tex/latex/pst-eps
%dir %{_texdir}/texmf-dist/tex/latex/pst-eucl
%dir %{_texdir}/texmf-dist/tex/latex/pst-exa
%dir %{_texdir}/texmf-dist/tex/latex/pst-fill
%dir %{_texdir}/texmf-dist/tex/latex/pst-fr3d
%dir %{_texdir}/texmf-dist/tex/latex/pst-fractal
%dir %{_texdir}/texmf-dist/tex/latex/pst-fun
%dir %{_texdir}/texmf-dist/tex/latex/pst-func
%dir %{_texdir}/texmf-dist/tex/latex/pst-gantt
%dir %{_texdir}/texmf-dist/tex/latex/pst-geo
%dir %{_texdir}/texmf-dist/tex/latex/pst-ghsb
%dir %{_texdir}/texmf-dist/tex/latex/pst-gr3d
%dir %{_texdir}/texmf-dist/tex/latex/pst-grad
%dir %{_texdir}/texmf-dist/tex/latex/pst-infixplot
%dir %{_texdir}/texmf-dist/tex/latex/pst-jtree
%dir %{_texdir}/texmf-dist/tex/latex/pst-knot
%dir %{_texdir}/texmf-dist/tex/latex/pst-labo
%dir %{_texdir}/texmf-dist/tex/latex/pst-lens
%dir %{_texdir}/texmf-dist/tex/latex/pst-light3d
%dir %{_texdir}/texmf-dist/tex/latex/pst-magneticfield
%dir %{_texdir}/texmf-dist/tex/latex/pst-math
%dir %{_texdir}/texmf-dist/tex/latex/pst-mirror
%dir %{_texdir}/texmf-dist/tex/latex/pst-node
%dir %{_texdir}/texmf-dist/tex/latex/pst-ob3d
%dir %{_texdir}/texmf-dist/tex/latex/pstool
%dir %{_texdir}/texmf-dist/tex/latex/pst-optexp
%dir %{_texdir}/texmf-dist/tex/latex/pst-optic
%dir %{_texdir}/texmf-dist/tex/latex/pst-osci
%dir %{_texdir}/texmf-dist/tex/latex/pst-pad
%dir %{_texdir}/texmf-dist/tex/latex/pst-pdf
%dir %{_texdir}/texmf-dist/tex/latex/pst-pdgr
%dir %{_texdir}/texmf-dist/tex/latex/pst-platon
%dir %{_texdir}/texmf-dist/tex/latex/pst-plot
%dir %{_texdir}/texmf-dist/tex/latex/pst-poly
%dir %{_texdir}/texmf-dist/tex/latex/pst-qtree
%dir %{_texdir}/texmf-dist/tex/latex/pstricks
%dir %{_texdir}/texmf-dist/tex/latex/pstricks-add
%dir %{_texdir}/texmf-dist/tex/latex/pst-sigsys
%dir %{_texdir}/texmf-dist/tex/latex/pst-slpe
%dir %{_texdir}/texmf-dist/tex/latex/pst-solides3d
%dir %{_texdir}/texmf-dist/tex/latex/pst-soroban
%dir %{_texdir}/texmf-dist/tex/latex/pst-spectra
%dir %{_texdir}/texmf-dist/tex/latex/pst-stru
%dir %{_texdir}/texmf-dist/tex/latex/pst-text
%dir %{_texdir}/texmf-dist/tex/latex/pst-thick
%dir %{_texdir}/texmf-dist/tex/latex/pst-tree
%dir %{_texdir}/texmf-dist/tex/latex/pst-uml
%dir %{_texdir}/texmf-dist/tex/latex/pst-vowel
%dir %{_texdir}/texmf-dist/tex/latex/pst-vue3d
%dir %{_texdir}/texmf-dist/tex/latex/psu-thesis
%dir %{_texdir}/texmf-dist/tex/latex/ptptex
%dir %{_texdir}/texmf-dist/tex/latex/pxfonts
%dir %{_texdir}/texmf-dist/tex/latex/qcm
%dir %{_texdir}/texmf-dist/tex/latex/qobitree
%dir %{_texdir}/texmf-dist/tex/latex/qstest
%dir %{_texdir}/texmf-dist/tex/latex/qsymbols
%dir %{_texdir}/texmf-dist/tex/latex/qtree
%dir %{_texdir}/texmf-dist/tex/latex/quotchap
%dir %{_texdir}/texmf-dist/tex/latex/quotmark
%dir %{_texdir}/texmf-dist/tex/latex/randbild
%dir %{_texdir}/texmf-dist/tex/latex/randtext
%dir %{_texdir}/texmf-dist/tex/latex/rccol
%dir %{_texdir}/texmf-dist/tex/latex/rcs
%dir %{_texdir}/texmf-dist/tex/latex/rcsinfo
%dir %{_texdir}/texmf-dist/tex/latex/rcs-multi
%dir %{_texdir}/texmf-dist/tex/latex/recipe
%dir %{_texdir}/texmf-dist/tex/latex/recipecard
%dir %{_texdir}/texmf-dist/tex/latex/rectopma
%dir %{_texdir}/texmf-dist/tex/latex/recycle
%dir %{_texdir}/texmf-dist/tex/latex/refcheck
%dir %{_texdir}/texmf-dist/tex/latex/refman
%dir %{_texdir}/texmf-dist/tex/latex/refstyle
%dir %{_texdir}/texmf-dist/tex/latex/regcount
%dir %{_texdir}/texmf-dist/tex/latex/register
%dir %{_texdir}/texmf-dist/tex/latex/relsize
%dir %{_texdir}/texmf-dist/tex/latex/repeatindex
%dir %{_texdir}/texmf-dist/tex/latex/revtex
%dir %{_texdir}/texmf-dist/tex/latex/revtex4
%dir %{_texdir}/texmf-dist/tex/latex/rjlparshap
%dir %{_texdir}/texmf-dist/tex/latex/rmpage
%dir %{_texdir}/texmf-dist/tex/latex/robustcommand
%dir %{_texdir}/texmf-dist/tex/latex/robustindex
%dir %{_texdir}/texmf-dist/tex/latex/romande
%dir %{_texdir}/texmf-dist/tex/latex/romannum
%dir %{_texdir}/texmf-dist/tex/latex/rotating
%dir %{_texdir}/texmf-dist/tex/latex/rotfloat
%dir %{_texdir}/texmf-dist/tex/latex/rotpages
%dir %{_texdir}/texmf-dist/tex/latex/roundbox
%dir %{_texdir}/texmf-dist/tex/latex/rsc
%dir %{_texdir}/texmf-dist/tex/latex/rst
%dir %{_texdir}/texmf-dist/tex/latex/rtkinenc
%dir %{_texdir}/texmf-dist/tex/latex/rtklage
%dir %{_texdir}/texmf-dist/tex/latex/r_und_s
%dir %{_texdir}/texmf-dist/tex/latex/ryethesis
%dir %{_texdir}/texmf-dist/tex/latex/sageep
%dir %{_texdir}/texmf-dist/tex/latex/sanskrit
%dir %{_texdir}/texmf-dist/tex/latex/sansmath
%dir %{_texdir}/texmf-dist/tex/latex/sauerj
%dir %{_texdir}/texmf-dist/tex/latex/sauterfonts
%dir %{_texdir}/texmf-dist/tex/latex/savefnmark
%dir %{_texdir}/texmf-dist/tex/latex/savesym
%dir %{_texdir}/texmf-dist/tex/latex/savetrees
%dir %{_texdir}/texmf-dist/tex/latex/scale
%dir %{_texdir}/texmf-dist/tex/latex/scalebar
%dir %{_texdir}/texmf-dist/tex/latex/schemabloc
%dir %{_texdir}/texmf-dist/tex/latex/scientificpaper
%dir %{_texdir}/texmf-dist/tex/latex/sciposter
%dir %{_texdir}/texmf-dist/tex/latex/sciwordconv
%dir %{_texdir}/texmf-dist/tex/latex/screenplay
%dir %{_texdir}/texmf-dist/tex/latex/sdrt
%dir %{_texdir}/texmf-dist/tex/latex/sectionbox
%dir %{_texdir}/texmf-dist/tex/latex/sectsty
%dir %{_texdir}/texmf-dist/tex/latex/selectp
%dir %{_texdir}/texmf-dist/tex/latex/semantic
%dir %{_texdir}/texmf-dist/tex/latex/semaphor
%dir %{_texdir}/texmf-dist/tex/latex/seminar
%dir %{_texdir}/texmf-dist/tex/latex/semioneside
%dir %{_texdir}/texmf-dist/tex/latex/seqsplit
%dir %{_texdir}/texmf-dist/tex/latex/setspace
%dir %{_texdir}/texmf-dist/tex/latex/seuthesis
%dir %{_texdir}/texmf-dist/tex/latex/sf298
%dir %{_texdir}/texmf-dist/tex/latex/sffms
%dir %{_texdir}/texmf-dist/tex/latex/sfg
%dir %{_texdir}/texmf-dist/tex/latex/sfmath
%dir %{_texdir}/texmf-dist/tex/latex/sgame
%dir %{_texdir}/texmf-dist/tex/latex/shadethm
%dir %{_texdir}/texmf-dist/tex/latex/shipunov
%dir %{_texdir}/texmf-dist/tex/latex/shorttoc
%dir %{_texdir}/texmf-dist/tex/latex/show2e
%dir %{_texdir}/texmf-dist/tex/latex/showexpl
%dir %{_texdir}/texmf-dist/tex/latex/showlabels
%dir %{_texdir}/texmf-dist/tex/latex/shuffle
%dir %{_texdir}/texmf-dist/tex/latex/sidecap
%dir %{_texdir}/texmf-dist/tex/latex/sides
%dir %{_texdir}/texmf-dist/tex/latex/siggraph
%dir %{_texdir}/texmf-dist/tex/latex/silence
%dir %{_texdir}/texmf-dist/tex/latex/simplecd
%dir %{_texdir}/texmf-dist/tex/latex/simplecv
%dir %{_texdir}/texmf-dist/tex/latex/simplewick
%dir %{_texdir}/texmf-dist/tex/latex/SIstyle
%dir %{_texdir}/texmf-dist/tex/latex/SIunits
%dir %{_texdir}/texmf-dist/tex/latex/siunitx
%dir %{_texdir}/texmf-dist/tex/latex/siunitx/config
%dir %{_texdir}/texmf-dist/tex/latex/skak
%dir %{_texdir}/texmf-dist/tex/latex/skeycommand
%dir %{_texdir}/texmf-dist/tex/latex/skeyval
%dir %{_texdir}/texmf-dist/tex/latex/skull
%dir %{_texdir}/texmf-dist/tex/latex/slantsc
%dir %{_texdir}/texmf-dist/tex/latex/smalltableof
%dir %{_texdir}/texmf-dist/tex/latex/smartref
%dir %{_texdir}/texmf-dist/tex/latex/snapshot
%dir %{_texdir}/texmf-dist/tex/latex/songbook
%dir %{_texdir}/texmf-dist/tex/latex/soton
%dir %{_texdir}/texmf-dist/tex/latex/soul
%dir %{_texdir}/texmf-dist/tex/latex/spanish-mx
%dir %{_texdir}/texmf-dist/tex/latex/sparklines
%dir %{_texdir}/texmf-dist/tex/latex/spie
%dir %{_texdir}/texmf-dist/tex/latex/splitbib
%dir %{_texdir}/texmf-dist/tex/latex/splitindex
%dir %{_texdir}/texmf-dist/tex/latex/spotcolor
%dir %{_texdir}/texmf-dist/tex/latex/spreadtab
%dir %{_texdir}/texmf-dist/tex/latex/spverbatim
%dir %{_texdir}/texmf-dist/tex/latex/srcltx
%dir %{_texdir}/texmf-dist/tex/latex/sseq
%dir %{_texdir}/texmf-dist/tex/latex/ssqquote
%dir %{_texdir}/texmf-dist/tex/latex/stack
%dir %{_texdir}/texmf-dist/tex/latex/stage
%dir %{_texdir}/texmf-dist/tex/latex/standalone
%dir %{_texdir}/texmf-dist/tex/latex/statex2
%dir %{_texdir}/texmf-dist/tex/latex/statistik
%dir %{_texdir}/texmf-dist/tex/latex/staves
%dir %{_texdir}/texmf-dist/tex/latex/stdclsdv
%dir %{_texdir}/texmf-dist/tex/latex/stdpage
%dir %{_texdir}/texmf-dist/tex/latex/steinmetz
%dir %{_texdir}/texmf-dist/tex/latex/stellenbosch
%dir %{_texdir}/texmf-dist/tex/latex/stellenbosch/logos
%dir %{_texdir}/texmf-dist/tex/latex/stex
%dir %{_texdir}/texmf-dist/tex/latex/stex/assignment
%dir %{_texdir}/texmf-dist/tex/latex/stex/cmathml
%dir %{_texdir}/texmf-dist/tex/latex/stex/cnx
%dir %{_texdir}/texmf-dist/tex/latex/stex/dcm
%dir %{_texdir}/texmf-dist/tex/latex/stex/mikoslides
%dir %{_texdir}/texmf-dist/tex/latex/stex/modules
%dir %{_texdir}/texmf-dist/tex/latex/stex/omd
%dir %{_texdir}/texmf-dist/tex/latex/stex/omdoc
%dir %{_texdir}/texmf-dist/tex/latex/stex/omtext
%dir %{_texdir}/texmf-dist/tex/latex/stex/presentation
%dir %{_texdir}/texmf-dist/tex/latex/stex/problem
%dir %{_texdir}/texmf-dist/tex/latex/stex/reqdoc
%dir %{_texdir}/texmf-dist/tex/latex/stex/sproof
%dir %{_texdir}/texmf-dist/tex/latex/stex/sref
%dir %{_texdir}/texmf-dist/tex/latex/stex/statements
%dir %{_texdir}/texmf-dist/tex/latex/stmaryrd
%dir %{_texdir}/texmf-dist/tex/latex/stringstrings
%dir %{_texdir}/texmf-dist/tex/latex/struktex
%dir %{_texdir}/texmf-dist/tex/latex/sttools
%dir %{_texdir}/texmf-dist/tex/latex/stubs
%dir %{_texdir}/texmf-dist/tex/latex/subdepth
%dir %{_texdir}/texmf-dist/tex/latex/subeqn
%dir %{_texdir}/texmf-dist/tex/latex/subeqnarray
%dir %{_texdir}/texmf-dist/tex/latex/subfig
%dir %{_texdir}/texmf-dist/tex/latex/subfigure
%dir %{_texdir}/texmf-dist/tex/latex/subfloat
%dir %{_texdir}/texmf-dist/tex/latex/substr
%dir %{_texdir}/texmf-dist/tex/latex/sudoku
%dir %{_texdir}/texmf-dist/tex/latex/sudokubundle
%dir %{_texdir}/texmf-dist/tex/latex/sugconf
%dir %{_texdir}/texmf-dist/tex/latex/supertabular
%dir %{_texdir}/texmf-dist/tex/latex/susy
%dir %{_texdir}/texmf-dist/tex/latex/svgcolor
%dir %{_texdir}/texmf-dist/tex/latex/svn
%dir %{_texdir}/texmf-dist/tex/latex/svninfo
%dir %{_texdir}/texmf-dist/tex/latex/svn-multi
%dir %{_texdir}/texmf-dist/tex/latex/svn-prov
%dir %{_texdir}/texmf-dist/tex/latex/syllogism
%dir %{_texdir}/texmf-dist/tex/latex/symbol
%dir %{_texdir}/texmf-dist/tex/latex/synproof
%dir %{_texdir}/texmf-dist/tex/latex/syntax
%dir %{_texdir}/texmf-dist/tex/latex/syntrace
%dir %{_texdir}/texmf-dist/tex/latex/synttree
%dir %{_texdir}/texmf-dist/tex/latex/t2
%dir %{_texdir}/texmf-dist/tex/latex/Tabbing
%dir %{_texdir}/texmf-dist/tex/latex/tableaux
%dir %{_texdir}/texmf-dist/tex/latex/tablenotes
%dir %{_texdir}/texmf-dist/tex/latex/tablists
%dir %{_texdir}/texmf-dist/tex/latex/tablor
%dir %{_texdir}/texmf-dist/tex/latex/tabls
%dir %{_texdir}/texmf-dist/tex/latex/tabto-ltx
%dir %{_texdir}/texmf-dist/tex/latex/tabularborder
%dir %{_texdir}/texmf-dist/tex/latex/tabularcalc
%dir %{_texdir}/texmf-dist/tex/latex/tabularew
%dir %{_texdir}/texmf-dist/tex/latex/tabulary
%dir %{_texdir}/texmf-dist/tex/latex/tabvar
%dir %{_texdir}/texmf-dist/tex/latex/talk
%dir %{_texdir}/texmf-dist/tex/latex/t-angles
%dir %{_texdir}/texmf-dist/tex/latex/taupin
%dir %{_texdir}/texmf-dist/tex/latex/tcldoc
%dir %{_texdir}/texmf-dist/tex/latex/tdclock
%dir %{_texdir}/texmf-dist/tex/latex/tdsfrmath
%dir %{_texdir}/texmf-dist/tex/latex/technics
%dir %{_texdir}/texmf-dist/tex/latex/ted
%dir %{_texdir}/texmf-dist/tex/latex/tengwarscript
%dir %{_texdir}/texmf-dist/tex/latex/tensor
%dir %{_texdir}/texmf-dist/tex/latex/termlist
%dir %{_texdir}/texmf-dist/tex/latex/teubner
%dir %{_texdir}/texmf-dist/tex/latex/tex-gyre
%dir %{_texdir}/texmf-dist/tex/latex/texilikechaps
%dir %{_texdir}/texmf-dist/tex/latex/texilikecover
%dir %{_texdir}/texmf-dist/tex/latex/tex-label
%dir %{_texdir}/texmf-dist/tex/latex/texlogos
%dir %{_texdir}/texmf-dist/tex/latex/texmate
%dir %{_texdir}/texmf-dist/tex/latex/texments
%dir %{_texdir}/texmf-dist/tex/latex/texpower
%dir %{_texdir}/texmf-dist/tex/latex/texshade
%dir %{_texdir}/texmf-dist/tex/latex/textcase
%dir %{_texdir}/texmf-dist/tex/latex/textfit
%dir %{_texdir}/texmf-dist/tex/latex/textopo
%dir %{_texdir}/texmf-dist/tex/latex/textpath
%dir %{_texdir}/texmf-dist/tex/latex/textpos
%dir %{_texdir}/texmf-dist/tex/latex/theoremref
%dir %{_texdir}/texmf-dist/tex/latex/thesis-titlepage-fhac
%dir %{_texdir}/texmf-dist/tex/latex/thinsp
%dir %{_texdir}/texmf-dist/tex/latex/thmbox
%dir %{_texdir}/texmf-dist/tex/latex/thmtools
%dir %{_texdir}/texmf-dist/tex/latex/threeparttable
%dir %{_texdir}/texmf-dist/tex/latex/threeparttablex
%dir %{_texdir}/texmf-dist/tex/latex/thumb
%dir %{_texdir}/texmf-dist/tex/latex/thumby
%dir %{_texdir}/texmf-dist/tex/latex/thuthesis
%dir %{_texdir}/texmf-dist/tex/latex/ticket
%dir %{_texdir}/texmf-dist/tex/latex/tikz-3dplot
%dir %{_texdir}/texmf-dist/tex/latex/tikz-inet
%dir %{_texdir}/texmf-dist/tex/latex/tikz-qtree
%dir %{_texdir}/texmf-dist/tex/latex/tikz-timing
%dir %{_texdir}/texmf-dist/tex/latex/times
%dir %{_texdir}/texmf-dist/tex/latex/timesht
%dir %{_texdir}/texmf-dist/tex/latex/tipa
%dir %{_texdir}/texmf-dist/tex/latex/titlefoot
%dir %{_texdir}/texmf-dist/tex/latex/titlepic
%dir %{_texdir}/texmf-dist/tex/latex/titleref
%dir %{_texdir}/texmf-dist/tex/latex/titlesec
%dir %{_texdir}/texmf-dist/tex/latex/titling
%dir %{_texdir}/texmf-dist/tex/latex/tkz-doc
%dir %{_texdir}/texmf-dist/tex/latex/tkz-linknodes
%dir %{_texdir}/texmf-dist/tex/latex/tkz-orm
%dir %{_texdir}/texmf-dist/tex/latex/tkz-tab
%dir %{_texdir}/texmf-dist/tex/latex/tocbibind
%dir %{_texdir}/texmf-dist/tex/latex/tocloft
%dir %{_texdir}/texmf-dist/tex/latex/tocvsec2
%dir %{_texdir}/texmf-dist/tex/latex/todo
%dir %{_texdir}/texmf-dist/tex/latex/todonotes
%dir %{_texdir}/texmf-dist/tex/latex/tokenizer
%dir %{_texdir}/texmf-dist/tex/latex/toolbox
%dir %{_texdir}/texmf-dist/tex/latex/tools
%dir %{_texdir}/texmf-dist/tex/latex/topfloat
%dir %{_texdir}/texmf-dist/tex/latex/toptesi
%dir %{_texdir}/texmf-dist/tex/latex/totcount
%dir %{_texdir}/texmf-dist/tex/latex/totpages
%dir %{_texdir}/texmf-dist/tex/latex/tpslifonts
%dir %{_texdir}/texmf-dist/tex/latex/trajan
%dir %{_texdir}/texmf-dist/tex/latex/trfsigns
%dir %{_texdir}/texmf-dist/tex/latex/trimspaces
%dir %{_texdir}/texmf-dist/tex/latex/trivfloat
%dir %{_texdir}/texmf-dist/tex/latex/trsym
%dir %{_texdir}/texmf-dist/tex/latex/truncate
%dir %{_texdir}/texmf-dist/tex/latex/tufte-latex
%dir %{_texdir}/texmf-dist/tex/latex/tugboat
%dir %{_texdir}/texmf-dist/tex/latex/turkmen
%dir %{_texdir}/texmf-dist/tex/latex/turnstile
%dir %{_texdir}/texmf-dist/tex/latex/twoinone
%dir %{_texdir}/texmf-dist/tex/latex/twoup
%dir %{_texdir}/texmf-dist/tex/latex/txfonts
%dir %{_texdir}/texmf-dist/tex/latex/txfontsb
%dir %{_texdir}/texmf-dist/tex/latex/type1cm
%dir %{_texdir}/texmf-dist/tex/latex/typedref
%dir %{_texdir}/texmf-dist/tex/latex/typehtml
%dir %{_texdir}/texmf-dist/tex/latex/typogrid
%dir %{_texdir}/texmf-dist/tex/latex/uaclasses
%dir %{_texdir}/texmf-dist/tex/latex/ucdavisthesis
%dir %{_texdir}/texmf-dist/tex/latex/ucs
%dir %{_texdir}/texmf-dist/tex/latex/ucs/data
%dir %{_texdir}/texmf-dist/tex/latex/ucthesis
%dir %{_texdir}/texmf-dist/tex/latex/uebungsblatt
%dir %{_texdir}/texmf-dist/tex/latex/uiucthesis
%dir %{_texdir}/texmf-dist/tex/latex/ulqda
%dir %{_texdir}/texmf-dist/tex/latex/umich-thesis
%dir %{_texdir}/texmf-dist/tex/latex/uml
%dir %{_texdir}/texmf-dist/tex/latex/umlaute
%dir %{_texdir}/texmf-dist/tex/latex/umoline
%dir %{_texdir}/texmf-dist/tex/latex/umthesis
%dir %{_texdir}/texmf-dist/tex/latex/underlin
%dir %{_texdir}/texmf-dist/tex/latex/underscore
%dir %{_texdir}/texmf-dist/tex/latex/undolabl
%dir %{_texdir}/texmf-dist/tex/latex/unicode-math
%dir %{_texdir}/texmf-dist/tex/latex/units
%dir %{_texdir}/texmf-dist/tex/latex/unitsdef
%dir %{_texdir}/texmf-dist/tex/latex/universa
%dir %{_texdir}/texmf-dist/tex/latex/upmethodology
%dir %{_texdir}/texmf-dist/tex/latex/upquote
%dir %{_texdir}/texmf-dist/tex/latex/url
%dir %{_texdir}/texmf-dist/tex/latex/ushort
%dir %{_texdir}/texmf-dist/tex/latex/ut-thesis
%dir %{_texdir}/texmf-dist/tex/latex/uwthesis
%dir %{_texdir}/texmf-dist/tex/latex/varindex
%dir %{_texdir}/texmf-dist/tex/latex/varsfromjobname
%dir %{_texdir}/texmf-dist/tex/latex/varwidth
%dir %{_texdir}/texmf-dist/tex/latex/velthuis
%dir %{_texdir}/texmf-dist/tex/latex/venturis
%dir %{_texdir}/texmf-dist/tex/latex/venturis2
%dir %{_texdir}/texmf-dist/tex/latex/venturisadf
%dir %{_texdir}/texmf-dist/tex/latex/venturisold
%dir %{_texdir}/texmf-dist/tex/latex/venturissans
%dir %{_texdir}/texmf-dist/tex/latex/venturissans2
%dir %{_texdir}/texmf-dist/tex/latex/verbatimbox
%dir %{_texdir}/texmf-dist/tex/latex/verbatimcopy
%dir %{_texdir}/texmf-dist/tex/latex/verbdef
%dir %{_texdir}/texmf-dist/tex/latex/verse
%dir %{_texdir}/texmf-dist/tex/latex/version
%dir %{_texdir}/texmf-dist/tex/latex/versions
%dir %{_texdir}/texmf-dist/tex/latex/vertbars
%dir %{_texdir}/texmf-dist/tex/latex/vhistory
%dir %{_texdir}/texmf-dist/tex/latex/vita
%dir %{_texdir}/texmf-dist/tex/latex/vmargin
%dir %{_texdir}/texmf-dist/tex/latex/vntex
%dir %{_texdir}/texmf-dist/tex/latex/volumes
%dir %{_texdir}/texmf-dist/tex/latex/vpe
%dir %{_texdir}/texmf-dist/tex/latex/vrsion
%dir %{_texdir}/texmf-dist/tex/latex/vwcol
%dir %{_texdir}/texmf-dist/tex/latex/vxu
%dir %{_texdir}/texmf-dist/tex/latex/wallpaper
%dir %{_texdir}/texmf-dist/tex/latex/warning
%dir %{_texdir}/texmf-dist/tex/latex/warpcol
%dir %{_texdir}/texmf-dist/tex/latex/was
%dir %{_texdir}/texmf-dist/tex/latex/wasysym
%dir %{_texdir}/texmf-dist/tex/latex/widetable
%dir %{_texdir}/texmf-dist/tex/latex/williams
%dir %{_texdir}/texmf-dist/tex/latex/wnri
%dir %{_texdir}/texmf-dist/tex/latex/wordlike
%dir %{_texdir}/texmf-dist/tex/latex/wrapfig
%dir %{_texdir}/texmf-dist/tex/latex/wsuipa
%dir %{_texdir}/texmf-dist/tex/latex/xargs
%dir %{_texdir}/texmf-dist/tex/latex/xcolor
%dir %{_texdir}/texmf-dist/tex/latex/xdoc
%dir %{_texdir}/texmf-dist/tex/latex/xfor
%dir %{_texdir}/texmf-dist/tex/latex/xifthen
%dir %{_texdir}/texmf-dist/tex/latex/xkeyval
%dir %{_texdir}/texmf-dist/tex/latex/xmpincl
%dir %{_texdir}/texmf-dist/tex/latex/xnewcommand
%dir %{_texdir}/texmf-dist/tex/latex/xoptarg
%dir %{_texdir}/texmf-dist/tex/latex/xpackages
%dir %{_texdir}/texmf-dist/tex/latex/xpackages/xbase
%dir %{_texdir}/texmf-dist/tex/latex/xpackages/xtras
%dir %{_texdir}/texmf-dist/tex/latex/xq
%dir %{_texdir}/texmf-dist/tex/latex/xskak
%dir %{_texdir}/texmf-dist/tex/latex/xtab
%dir %{_texdir}/texmf-dist/tex/latex/xwatermark
%dir %{_texdir}/texmf-dist/tex/latex/xyling
%dir %{_texdir}/texmf-dist/tex/latex/xypdf
%dir %{_texdir}/texmf-dist/tex/latex/xytree
%dir %{_texdir}/texmf-dist/tex/latex/yafoot
%dir %{_texdir}/texmf-dist/tex/latex/yagusylo
%dir %{_texdir}/texmf-dist/tex/latex/ydoc
%dir %{_texdir}/texmf-dist/tex/latex/yfonts
%dir %{_texdir}/texmf-dist/tex/latex/yhmath
%dir %{_texdir}/texmf-dist/tex/latex/york-thesis
%dir %{_texdir}/texmf-dist/tex/latex/youngtab
%dir %{_texdir}/texmf-dist/tex/latex/yplan
%dir %{_texdir}/texmf-dist/tex/latex/zapfchan
%dir %{_texdir}/texmf-dist/tex/latex/zapfding
%dir %{_texdir}/texmf-dist/tex/latex/zed-csp
%dir %{_texdir}/texmf-dist/tex/latex/zhmetrics
%dir %{_texdir}/texmf-dist/tex/latex/ziffer
%dir %{_texdir}/texmf-dist/tex/latex/zwgetfdate
%dir %{_texdir}/texmf-dist/tex/latex/zwpagelayout
%dir %{_texdir}/texmf-dist/tex/lualatex
%dir %{_texdir}/texmf-dist/tex/lualatex/luainputenc
%dir %{_texdir}/texmf-dist/tex/luatex
%dir %{_texdir}/texmf-dist/tex/luatex/hyph-utf8
%dir %{_texdir}/texmf-dist/tex/luatex/lualibs
%dir %{_texdir}/texmf-dist/tex/luatex/luamplib
%dir %{_texdir}/texmf-dist/tex/luatex/luaotfload
%dir %{_texdir}/texmf-dist/tex/luatex/luatexbase
%dir %{_texdir}/texmf-dist/tex/luatex/luatextra
%dir %{_texdir}/texmf-dist/tex/mex
%dir %{_texdir}/texmf-dist/tex/mex/base
%dir %{_texdir}/texmf-dist/tex/mex/config
%dir %{_texdir}/texmf-dist/tex/mex/utf8mex
%dir %{_texdir}/texmf-dist/tex/mltex
%dir %{_texdir}/texmf-dist/tex/mltex/config
%dir %{_texdir}/texmf-dist/tex/mptopdf
%dir %{_texdir}/texmf-dist/tex/mptopdf/config
%dir %{_texdir}/texmf-dist/tex/plain
%dir %{_texdir}/texmf-dist/tex/plain/amsfonts
%dir %{_texdir}/texmf-dist/tex/plain/antt
%dir %{_texdir}/texmf-dist/tex/plain/apalike
%dir %{_texdir}/texmf-dist/tex/plain/armenian
%dir %{_texdir}/texmf-dist/tex/plain/base
%dir %{_texdir}/texmf-dist/tex/plain/config
%dir %{_texdir}/texmf-dist/tex/plain/cweb
%dir %{_texdir}/texmf-dist/tex/plain/cyrplain
%dir %{_texdir}/texmf-dist/tex/plain/encxvlna
%dir %{_texdir}/texmf-dist/tex/plain/esint-type1
%dir %{_texdir}/texmf-dist/tex/plain/etex
%dir %{_texdir}/texmf-dist/tex/plain/fixpdfmag
%dir %{_texdir}/texmf-dist/tex/plain/fontch
%dir %{_texdir}/texmf-dist/tex/plain/font-change
%dir %{_texdir}/texmf-dist/tex/plain/fp
%dir %{_texdir}/texmf-dist/tex/plain/graphics-pln
%dir %{_texdir}/texmf-dist/tex/plain/gustlib
%dir %{_texdir}/texmf-dist/tex/plain/gustlib/biblotex
%dir %{_texdir}/texmf-dist/tex/plain/gustlib/licz
%dir %{_texdir}/texmf-dist/tex/plain/gustlib/map
%dir %{_texdir}/texmf-dist/tex/plain/gustlib/plbtx993
%dir %{_texdir}/texmf-dist/tex/plain/gustlib/plmac218
%dir %{_texdir}/texmf-dist/tex/plain/harvmac
%dir %{_texdir}/texmf-dist/tex/plain/hyplain
%dir %{_texdir}/texmf-dist/tex/plain/iwona
%dir %{_texdir}/texmf-dist/tex/plain/js-misc
%dir %{_texdir}/texmf-dist/tex/plain/kdgreek
%dir %{_texdir}/texmf-dist/tex/plain/knitting
%dir %{_texdir}/texmf-dist/tex/plain/kurier
%dir %{_texdir}/texmf-dist/tex/plain/lh
%dir %{_texdir}/texmf-dist/tex/plain/ly1
%dir %{_texdir}/texmf-dist/tex/plain/metatex
%dir %{_texdir}/texmf-dist/tex/plain/misc
%dir %{_texdir}/texmf-dist/tex/plain/mkpattern
%dir %{_texdir}/texmf-dist/tex/plain/newsletr
%dir %{_texdir}/texmf-dist/tex/plain/omega
%dir %{_texdir}/texmf-dist/tex/plain/pgf
%dir %{_texdir}/texmf-dist/tex/plain/pgf/basiclayer
%dir %{_texdir}/texmf-dist/tex/plain/pgf/frontendlayer
%dir %{_texdir}/texmf-dist/tex/plain/pgf/math
%dir %{_texdir}/texmf-dist/tex/plain/pgfplots
%dir %{_texdir}/texmf-dist/tex/plain/pgf/systemlayer
%dir %{_texdir}/texmf-dist/tex/plain/pgf/utilities
%dir %{_texdir}/texmf-dist/tex/plain/pitex
%dir %{_texdir}/texmf-dist/tex/plain/placeins-plain
%dir %{_texdir}/texmf-dist/tex/plain/plnfss
%dir %{_texdir}/texmf-dist/tex/plain/resumemac
%dir %{_texdir}/texmf-dist/tex/plain/rsfs
%dir %{_texdir}/texmf-dist/tex/plain/semaphor
%dir %{_texdir}/texmf-dist/tex/plain/timetable
%dir %{_texdir}/texmf-dist/tex/plain/treetex
%dir %{_texdir}/texmf-dist/tex/plain/tugboat-plain
%dir %{_texdir}/texmf-dist/tex/plain/varisize
%dir %{_texdir}/texmf-dist/tex/plain/velthuis
%dir %{_texdir}/texmf-dist/tex/plain/vntex
%dir %{_texdir}/texmf-dist/tex/plain/wasy
%dir %{_texdir}/texmf-dist/tex/platex
%dir %{_texdir}/texmf-dist/tex/platex/base
%dir %{_texdir}/texmf-dist/tex/platex/config
%dir %{_texdir}/texmf-dist/tex/platex/jsclasses
%dir %{_texdir}/texmf-dist/tex/psizzl
%dir %{_texdir}/texmf-dist/tex/psizzl/base
%dir %{_texdir}/texmf-dist/tex/psizzl/config
%dir %{_texdir}/texmf-dist/tex/ptex
%dir %{_texdir}/texmf-dist/tex/ptex/base
%dir %{_texdir}/texmf-dist/tex/ptex/config
%dir %{_texdir}/texmf-dist/tex/ptexgeneric
%dir %{_texdir}/texmf-dist/tex/ptexgeneric/config
%dir %{_texdir}/texmf-dist/tex/ptexgeneric/hyphen
%dir %{_texdir}/texmf-dist/tex/ptexgeneric/ruhyphen
%dir %{_texdir}/texmf-dist/tex/ptexgeneric/ukrhyph
%dir %{_texdir}/texmf-dist/tex/startex
%dir %{_texdir}/texmf-dist/tex/startex/base
%dir %{_texdir}/texmf-dist/tex/texinfo
%dir %{_texdir}/texmf-dist/tex/texsis
%dir %{_texdir}/texmf-dist/tex/texsis/base
%dir %{_texdir}/texmf-dist/tex/texsis/config
%dir %{_texdir}/texmf-dist/tex/xelatex
%dir %{_texdir}/texmf-dist/tex/xelatex/arabxetex
%dir %{_texdir}/texmf-dist/tex/xelatex/fontwrap
%dir %{_texdir}/texmf-dist/tex/xelatex/mathspec
%dir %{_texdir}/texmf-dist/tex/xelatex/philokalia
%dir %{_texdir}/texmf-dist/tex/xelatex/polyglossia
%dir %{_texdir}/texmf-dist/tex/xelatex/velthuis
%dir %{_texdir}/texmf-dist/tex/xelatex/xecjk
%dir %{_texdir}/texmf-dist/tex/xelatex/xecolour
%dir %{_texdir}/texmf-dist/tex/xelatex/xecyr
%dir %{_texdir}/texmf-dist/tex/xelatex/xeindex
%dir %{_texdir}/texmf-dist/tex/xelatex/xepersian
%dir %{_texdir}/texmf-dist/tex/xelatex/xetexconfig
%dir %{_texdir}/texmf-dist/tex/xelatex/xetex-def
%dir %{_texdir}/texmf-dist/tex/xelatex/xetex-pstricks
%dir %{_texdir}/texmf-dist/tex/xelatex/xgreek
%dir %{_texdir}/texmf-dist/tex/xelatex/xltxtra
%dir %{_texdir}/texmf-dist/tex/xelatex/xunicode
%dir %{_texdir}/texmf-dist/tex/xetex
%dir %{_texdir}/texmf-dist/tex/xetex/xesearch
%dir %{_texdir}/texmf-dist/tex/xetex/xetexfontinfo
%dir %{_texdir}/texmf-dist/tex/xetex/xetex-pstricks
%dir %{_texdir}/texmf-dist/tex/xetex/zhspacing
%dir %{_texdir}/texmf-dist/tex/xetex/zhspacing/context
%dir %{_texdir}/texmf-dist/tex/xetex/zhspacing/latex
%dir %{_texdir}/texmf-dist/tex/xetex/zhspacing/plain
%dir %{_texdir}/texmf-dist/tex/xmltex
%dir %{_texdir}/texmf-dist/tex/xmltex/base
%dir %{_texdir}/texmf-dist/tex/xmltex/config
%dir %{_texdir}/texmf-dist/tex/xmltex/passivetex
%dir %{_texdir}/texmf-dist/tex/xmltex/xmlplay
%dir %{_texdir}/texmf-dist/vtex
%dir %{_texdir}/texmf-dist/vtex/config
%dir %{_texdir}/texmf/doc
%dir %{_texdir}/texmf/doc/bg5conv
%dir %{_texdir}/texmf/doc/bibtex8
%dir %{_texdir}/texmf/doc/cef5conv
%dir %{_texdir}/texmf/doc/cefconv
%dir %{_texdir}/texmf/doc/cefsconv
%dir %{_texdir}/texmf/doc/chktex
%dir %{_texdir}/texmf/doc/dvipdfm
%dir %{_texdir}/texmf/doc/dvipng
%dir %{_texdir}/texmf/doc/dvips
%dir %{_texdir}/texmf/doc/extconv
%dir %{_texdir}/texmf/doc/generic
%dir %{_texdir}/texmf/doc/generic/elhyphen
%dir %{_texdir}/texmf/doc/generic/huhyphen
%dir %{_texdir}/texmf/doc/hbf2gf
%dir %{_texdir}/texmf/doc/info
%dir %{_texdir}/texmf/doc/kpathsea
%dir %{_texdir}/texmf/doc/man
%dir %{_texdir}/texmf/doc/man/man1
%dir %{_texdir}/texmf/doc/man/man5
%dir %{_texdir}/texmf/doc/sjisconv
%dir %{_texdir}/texmf/doc/tetex
%dir %{_texdir}/texmf/doc/texdoc
%dir %{_texdir}/texmf/doc/texlive
%dir %{_texdir}/texmf/doc/texlive/texlive-common
%dir %{_texdir}/texmf/doc/texlive/texlive-common/examples
%dir %{_texdir}/texmf/doc/texlive/texlive-cz
%dir %{_texdir}/texmf/doc/texlive/texlive-de
%dir %{_texdir}/texmf/doc/texlive/texlive-en
%dir %{_texdir}/texmf/doc/texlive/texlive-en/archive
%dir %{_texdir}/texmf/doc/texlive/texlive-fr
%dir %{_texdir}/texmf/doc/texlive/texlive-it
%dir %{_texdir}/texmf/doc/texlive/texlive-pl
%dir %{_texdir}/texmf/doc/texlive/texlive-ru
%dir %{_texdir}/texmf/doc/texlive/texlive-sr
%dir %{_texdir}/texmf/doc/texlive/texlive-sr/images
%dir %{_texdir}/texmf/doc/texlive/texlive-zh-cn
%dir %{_texdir}/texmf/doc/tpic2pdftex
%dir %{_texdir}/texmf/doc/ttf2pk
%dir %{_texdir}/texmf/doc/vlna
%dir %{_texdir}/texmf/doc/web2c
%dir %{_texdir}/texmf/dvipdfm
%dir %{_texdir}/texmf/dvipdfm/config
%dir %{_texdir}/texmf/dvipdfmx
%dir %{_texdir}/texmf/dvips
%dir %{_texdir}/texmf/dvips/base
%dir %{_texdir}/texmf/dvips/config
%dir %{_texdir}/texmf/dvips/gsftopk
%dir %{_texdir}/texmf/dvips/tetex
%dir %{_texdir}/texmf/fonts
%dir %{_texdir}/texmf/fonts/cmap
%dir %{_texdir}/texmf/fonts/cmap/dvipdfmx
%dir %{_texdir}/texmf/fonts/enc
%dir %{_texdir}/texmf/fonts/enc/dvips
%dir %{_texdir}/texmf/fonts/enc/dvips/afm2pl
%dir %{_texdir}/texmf/fonts/enc/dvips/tetex
%dir %{_texdir}/texmf/fonts/enc/ttf2pk
%dir %{_texdir}/texmf/fonts/enc/ttf2pk/base
%dir %{_texdir}/texmf/fonts/lig
%dir %{_texdir}/texmf/fonts/lig/afm2pl
%dir %{_texdir}/texmf/fonts/map
%dir %{_texdir}/texmf/fonts/map/dvipdfm
%dir %{_texdir}/texmf/fonts/map/dvipdfm/tetex
%dir %{_texdir}/texmf/fonts/map/dvipdfm/updmap
%dir %{_texdir}/texmf/fonts/map/dvipdfmx
%dir %{_texdir}/texmf/fonts/map/dvips
%dir %{_texdir}/texmf/fonts/map/dvips/tetex
%dir %{_texdir}/texmf/fonts/map/dvips/updmap
%dir %{_texdir}/texmf/fonts/map/pdftex
%dir %{_texdir}/texmf/fonts/map/pdftex/updmap
%dir %{_texdir}/texmf/fonts/map/ttf2pk
%dir %{_texdir}/texmf/fonts/map/ttf2pk/config
%dir %{_texdir}/texmf/hbf2gf
%dir %{_texdir}/texmf/scripts
%dir %{_texdir}/texmf/scripts/a2ping
%dir %{_texdir}/texmf/scripts/simpdftex
%dir %{_texdir}/texmf/scripts/tetex
%dir %{_texdir}/texmf/scripts/tex4ht
%dir %{_texdir}/texmf/scripts/texdoc
%dir %{_texdir}/texmf/scripts/texlive
%dir %{_texdir}/texmf/scripts/texlive/lua
%dir %{_texdir}/texmf/scripts/texlive/lua/texlive
%dir %{_texdir}/texmf/tex
%dir %{_texdir}/texmf/texconfig
%dir %{_texdir}/texmf/texconfig/g
%dir %{_texdir}/texmf/texconfig/v
%dir %{_texdir}/texmf/texconfig/x
%dir %{_texdir}/texmf/texdoc
%dir %{_texdir}/texmf/texdoctk
%dir %{_texdir}/texmf/tex/fontinst
%dir %{_texdir}/texmf/tex/fontinst/afm2pl
%dir %{_texdir}/texmf/tex/generic
%dir %{_texdir}/texmf/tex/generic/config
%dir %{_texdir}/texmf/tex/generic/hyphen
%dir %{_texdir}/texmf/tex/generic/pdftex
%dir %{_texdir}/texmf/tex/latex
%dir %{_texdir}/texmf/tex/latex/afm2pl
%dir %{_texdir}/texmf/tex/latex/dvipdfm
%dir %{_texdir}/texmf/ttf2pk
%dir %{_texdir}/texmf/web2c
%dir %{_texdir}/texmf/xdvi
%dir %{_texdir}/texmf/xdvi/pixmap
%dir %{_texdir}/tlpkg
%files scheme-basic
%defattr(-,root,root)

%files collection-basic
%defattr(-,root,root)

%files collection-documentation-base
%defattr(-,root,root)

%files kpathsea-bin
%defattr(-,root,root)
%doc lgpl.txt
%{_bindir}/kpseaccess
%{_bindir}/kpsepath
%{_bindir}/kpsereadlink
%{_bindir}/kpsestat
%{_bindir}/kpsetool
%{_bindir}/kpsewhich
%{_bindir}/kpsexpand
%{_bindir}/mkocp
%{_bindir}/mkofm
%{_bindir}/mktexfmt
%{_bindir}/mktexlsr
%{_bindir}/mktexmf
%{_bindir}/mktexpk
%{_bindir}/mktextfm
%{_bindir}/texhash

%files bibtex-bin
%defattr(-,root,root)
%doc other-free.txt
%{_bindir}/bibtex

%files dvipdfm-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/dvipdfm
%{_bindir}/dvipdft

%files dvipdfmx-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/dvipdfmx
%{_bindir}/ebb
%{_bindir}/extractbb

%files dvips-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/afm2tfm
%{_bindir}/dvips

%files gsftopk-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/gsftopk

%files luatex-bin
%defattr(-,root,root)
%doc gpl2.txt
%{_bindir}/dviluatex
%{_bindir}/luatex
%{_bindir}/texlua
%{_bindir}/texluac

%files makeindex-bin
%defattr(-,root,root)
%doc other-free.txt
%{_bindir}/makeindex
%{_bindir}/mkindex

%files metafont-bin
%defattr(-,root,root)
%doc knuth.txt
%{_bindir}/mf
%{_bindir}/mf-nowin

%files mfware-bin
%defattr(-,root,root)
%doc knuth.txt
%{_bindir}/gftodvi
%{_bindir}/gftopk
%{_bindir}/gftype
%{_bindir}/mft
%{_bindir}/pktogf
%{_bindir}/pktype

%files pdftex-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/etex
%{_bindir}/pdfetex
%{_bindir}/pdftex
%{_bindir}/simpdftex

%files tcdialog-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/tcdialog

%files tetex-bin
%defattr(-,root,root)
%doc other-free.txt
%{_bindir}/allcm
%{_bindir}/allec
%{_bindir}/allneeded
%{_bindir}/dvi2fax
%{_bindir}/dvired
%{_bindir}/fmtutil
%{_bindir}/fmtutil-sys
%{_bindir}/kpsewhere
%{_bindir}/texconfig-dialog
%{_bindir}/texconfig-sys
%{_bindir}/texlinks
%{_bindir}/updmap
%{_bindir}/updmap-sys

%files tex-bin
%defattr(-,root,root)
%doc knuth.txt
%{_bindir}/tex

%files texconfig-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/texconfig

%files texlive.infra-bin
%defattr(-,root,root)
%doc lppl.txt

%files texlive-scripts-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/rungs

%files xdvi-bin
%defattr(-,root,root)
%doc other-free.txt
%{_bindir}/xdvi
%{_bindir}/xdvi-xaw

%files collection-latex
%defattr(-,root,root)

%files latex-bin-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/dvilualatex
%{_bindir}/latex
%{_bindir}/lualatex
%{_bindir}/pdflatex

%files mptopdf-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/mptopdf

%files scheme-context
%defattr(-,root,root)

%files collection-context
%defattr(-,root,root)

%files metapost-bin
%defattr(-,root,root)
%doc lgpl.txt
%{_bindir}/dvitomp
%{_bindir}/mfplain
%{_bindir}/mpost

%files xetex-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/xdvipdfmx
%{_bindir}/xelatex
%{_bindir}/xetex

%files context-bin
%defattr(-,root,root)
%doc other-free.txt
%{_bindir}/context
%{_bindir}/ctxtools
%{_bindir}/luatools
%{_bindir}/metafun
%{_bindir}/mtxrun
%{_bindir}/pstopdf
%{_bindir}/rlxtools
%{_bindir}/texexec
%{_bindir}/texmfstart

%files collection-metapost
%defattr(-,root,root)

%files scheme-full
%defattr(-,root,root)

%files collection-bibtexextra
%defattr(-,root,root)

%files bibexport-bin
%defattr(-,root,root)
%doc lppl1.3.txt
%{_bindir}/bibexport

%files collection-binextra
%defattr(-,root,root)

%files a2ping-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/a2ping

%files bibtex8-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/bibtex8

%files bibtexu-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/bibtexu

%files bundledoc-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/arlatex
%{_bindir}/bundledoc

%files chktex-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/chktex
%{_bindir}/chkweb
%{_bindir}/deweb

%files ctie-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/ctie

%files cweb-bin
%defattr(-,root,root)
%doc knuth.txt
%{_bindir}/ctangle
%{_bindir}/cweave

%files de-macro-bin
%defattr(-,root,root)
%doc other-free.txt
%{_bindir}/de-macro

%files detex-bin
%defattr(-,root,root)
%doc other-free.txt
%{_bindir}/detex

%files dtl-bin
%defattr(-,root,root)
%doc pd.txt
%{_bindir}/dt2dv
%{_bindir}/dv2dt

%files dvi2tty-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/disdvi
%{_bindir}/dvi2tty

%files dviasm-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/dviasm

%files dvicopy-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/dvicopy

%files dviljk-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/dvihp
%{_bindir}/dvilj
%{_bindir}/dvilj2p
%{_bindir}/dvilj4
%{_bindir}/dvilj4l
%{_bindir}/dvilj6

%files dvipng-bin
%defattr(-,root,root)
%doc lgpl.txt
%{_bindir}/dvigif
%{_bindir}/dvipng

%files dvipos-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/dvipos

%files dvisvgm-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/dvisvgm

%files findhyph-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/findhyph

%files fragmaster-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/fragmaster

%files latex2man-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/latex2man

%files latexdiff-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/latexdiff
%{_bindir}/latexdiff-vc
%{_bindir}/latexrevise

%files latexmk-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/latexmk

%files listings-ext-bin
%defattr(-,root,root)
%doc lppl1.2.txt
%{_bindir}/listings-ext.sh

%files patgen-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/patgen

%files pdfcrop-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/pdfcrop
%{_bindir}/rpdfcrop

%files pdfjam-bin
%defattr(-,root,root)
%doc gpl2.txt
%{_bindir}/pdf180
%{_bindir}/pdf270
%{_bindir}/pdf90
%{_bindir}/pdfbook
%{_bindir}/pdfflip
%{_bindir}/pdfjam
%{_bindir}/pdfjam-pocketmod
%{_bindir}/pdfjam-slides3up
%{_bindir}/pdfjam-slides6up
%{_bindir}/pdfjoin
%{_bindir}/pdfnup
%{_bindir}/pdfpun

%files pdftools-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/e2pall
%{_bindir}/pdfatfi
%{_bindir}/pdfclose
%{_bindir}/pdfopen
%{_bindir}/pdftosrc
%{_bindir}/ps4pdf

%files pkfix-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/pkfix

%files pkfix-helper-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/pkfix-helper

%files purifyeps-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/purifyeps

%files seetexk-bin
%defattr(-,root,root)
%doc other-free.txt
%{_bindir}/dvibook
%{_bindir}/dviconcat
%{_bindir}/dviselect
%{_bindir}/dvitodvi

%files synctex-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/synctex

%files texcount-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/texcount

%files texdoc-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/texdoc
%{_bindir}/texdoctk

%files texloganalyser-bin
%defattr(-,root,root)
%doc other-free.txt
%{_bindir}/texloganalyser

%files texware-bin
%defattr(-,root,root)
%doc knuth.txt
%{_bindir}/dvitype
%{_bindir}/pooltype

%files tie-bin
%defattr(-,root,root)
%doc other-free.txt
%{_bindir}/tie

%files tpic2pdftex-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/tpic2pdftex

%files web-bin
%defattr(-,root,root)
%doc knuth.txt
%{_bindir}/tangle
%{_bindir}/weave

%files collection-documentation-arabic
%defattr(-,root,root)

%files collection-documentation-bulgarian
%defattr(-,root,root)

%files collection-documentation-chinese
%defattr(-,root,root)

%files collection-documentation-czechslovak
%defattr(-,root,root)

%files collection-documentation-dutch
%defattr(-,root,root)

%files collection-documentation-english
%defattr(-,root,root)

%files collection-documentation-finnish
%defattr(-,root,root)

%files collection-documentation-french
%defattr(-,root,root)

%files collection-documentation-german
%defattr(-,root,root)

%files collection-documentation-italian
%defattr(-,root,root)

%files collection-documentation-japanese
%defattr(-,root,root)

%files collection-documentation-korean
%defattr(-,root,root)

%files collection-documentation-mongolian
%defattr(-,root,root)

%files collection-documentation-polish
%defattr(-,root,root)

%files collection-documentation-portuguese
%defattr(-,root,root)

%files collection-documentation-russian
%defattr(-,root,root)

%files collection-documentation-serbian
%defattr(-,root,root)

%files collection-documentation-slovenian
%defattr(-,root,root)

%files collection-documentation-spanish
%defattr(-,root,root)

%files collection-documentation-thai
%defattr(-,root,root)

%files collection-documentation-turkish
%defattr(-,root,root)

%files collection-documentation-ukrainian
%defattr(-,root,root)

%files collection-documentation-vietnamese
%defattr(-,root,root)

%files collection-fontsextra
%defattr(-,root,root)

%files collection-fontsrecommended
%defattr(-,root,root)

%files collection-fontutils
%defattr(-,root,root)

%files accfonts-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/mkt1font
%{_bindir}/vpl2ovp
%{_bindir}/vpl2vpl

%files afm2pl-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/afm2pl

%files epstopdf-bin
%defattr(-,root,root)
%doc other-free.txt
%{_bindir}/epstopdf
%{_bindir}/repstopdf

%files fontware-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/pltotf
%{_bindir}/tftopl
%{_bindir}/vftovp
%{_bindir}/vptovf

%files lcdftypetools-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/cfftot1
%{_bindir}/mmafm
%{_bindir}/mmpfb
%{_bindir}/otfinfo
%{_bindir}/otftotfm
%{_bindir}/t1dotlessj
%{_bindir}/t1lint
%{_bindir}/t1rawafm
%{_bindir}/t1reencode
%{_bindir}/t1testpage
%{_bindir}/ttftotype42

%files pstools-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/bbox
%{_bindir}/ps2eps
%{_bindir}/ps2frag
%{_bindir}/pslatex

%files fontinst-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/fontinst

%files fontools-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/afm2afm
%{_bindir}/autoinst
%{_bindir}/cmap2enc
%{_bindir}/font2afm
%{_bindir}/ot2kpx
%{_bindir}/pfm2kpx
%{_bindir}/showglyphs

%files ttfutils-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/ttf2afm
%{_bindir}/ttf2pk
%{_bindir}/ttf2tfm
%{_bindir}/ttfdump

%files collection-formatsextra
%defattr(-,root,root)

%files eplain-bin
%defattr(-,root,root)
%doc gpl2.txt
%{_bindir}/eplain

%files mltex-bin
%defattr(-,root,root)
%doc knuth.txt
%{_bindir}/mllatex
%{_bindir}/mltex

%files texsis-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/texsis

%files collection-games
%defattr(-,root,root)

%files collection-genericextra
%defattr(-,root,root)

%files collection-genericrecommended
%defattr(-,root,root)

%files collection-htmlxml
%defattr(-,root,root)

%files jadetex-bin
%defattr(-,root,root)
%doc other-free.txt
%{_bindir}/jadetex
%{_bindir}/pdfjadetex

%files tex4ht-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/ht
%{_bindir}/htcontext
%{_bindir}/htlatex
%{_bindir}/htmex
%{_bindir}/httex
%{_bindir}/httexi
%{_bindir}/htxelatex
%{_bindir}/htxetex
%{_bindir}/mk4ht
%{_bindir}/t4ht
%{_bindir}/tex4ht

%files xmltex-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/pdfxmltex
%{_bindir}/xmltex

%files collection-humanities
%defattr(-,root,root)

%files collection-langafrican
%defattr(-,root,root)

%files collection-langarabic
%defattr(-,root,root)

%files collection-langarmenian
%defattr(-,root,root)

%files collection-langcjk
%defattr(-,root,root)

%files cjkutils-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/bg5+latex
%{_bindir}/bg5+pdflatex
%{_bindir}/bg5conv
%{_bindir}/bg5latex
%{_bindir}/bg5pdflatex
%{_bindir}/cef5conv
%{_bindir}/cef5latex
%{_bindir}/cef5pdflatex
%{_bindir}/cefconv
%{_bindir}/ceflatex
%{_bindir}/cefpdflatex
%{_bindir}/cefsconv
%{_bindir}/cefslatex
%{_bindir}/cefspdflatex
%{_bindir}/extconv
%{_bindir}/gbklatex
%{_bindir}/gbkpdflatex
%{_bindir}/hbf2gf
%{_bindir}/sjisconv
%{_bindir}/sjislatex
%{_bindir}/sjispdflatex

%files ptex-bin
%defattr(-,root,root)
%doc other-free.txt
%{_bindir}/makejvf
%{_bindir}/mendex
%{_bindir}/pbibtex
%{_bindir}/pdvitype
%{_bindir}/platex
%{_bindir}/ppltotf
%{_bindir}/ptex
%{_bindir}/ptftopl

%files collection-langcroatian
%defattr(-,root,root)

%files collection-langcyrillic
%defattr(-,root,root)

%files cyrillic-bin-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/rubibtex
%{_bindir}/rumakeindex

%files collection-langczechslovak
%defattr(-,root,root)

%files cslatex-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/cslatex
%{_bindir}/pdfcslatex

%files csplain-bin
%defattr(-,root,root)
%doc other-free.txt
%{_bindir}/csplain
%{_bindir}/pdfcsplain

%files vlna-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/vlna

%files collection-langdanish
%defattr(-,root,root)

%files collection-langdutch
%defattr(-,root,root)

%files collection-langfinnish
%defattr(-,root,root)

%files collection-langfrench
%defattr(-,root,root)

%files collection-langgerman
%defattr(-,root,root)

%files collection-langgreek
%defattr(-,root,root)

%files mkgrkindex-bin
%defattr(-,root,root)
%doc other-free.txt
%{_bindir}/mkgrkindex

%files collection-langhebrew
%defattr(-,root,root)

%files collection-langhungarian
%defattr(-,root,root)

%files collection-langindic
%defattr(-,root,root)

%files ebong-bin
%defattr(-,root,root)
%doc pd.txt
%{_bindir}/ebong

%files devnag-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/devnag

%files collection-langitalian
%defattr(-,root,root)

%files collection-langlatin
%defattr(-,root,root)

%files collection-langlatvian
%defattr(-,root,root)

%files collection-langlithuanian
%defattr(-,root,root)

%files collection-langmongolian
%defattr(-,root,root)

%files collection-langnorwegian
%defattr(-,root,root)

%files collection-langother
%defattr(-,root,root)

%files collection-langpolish
%defattr(-,root,root)

%files mex-bin
%defattr(-,root,root)
%doc pd.txt
%{_bindir}/mex
%{_bindir}/pdfmex
%{_bindir}/utf8mex

%files collection-langportuguese
%defattr(-,root,root)

%files collection-langspanish
%defattr(-,root,root)

%files collection-langswedish
%defattr(-,root,root)

%files collection-langtibetan
%defattr(-,root,root)

%files collection-langturkmen
%defattr(-,root,root)

%files collection-langenglish
%defattr(-,root,root)

%files collection-langvietnamese
%defattr(-,root,root)

%files collection-latex3
%defattr(-,root,root)

%files collection-latexextra
%defattr(-,root,root)

%files collection-pictures
%defattr(-,root,root)

%files cachepic-bin
%defattr(-,root,root)
%doc lppl1.3.txt
%{_bindir}/cachepic

%files epspdf-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/epspdf
%{_bindir}/epspdftk

%files fig4latex-bin
%defattr(-,root,root)
%doc gpl3.txt
%{_bindir}/fig4latex

%files mathspic-bin
%defattr(-,root,root)
%doc other-free.txt
%{_bindir}/mathspic

%files authorindex-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/authorindex

%files glossaries-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/makeglossaries

%files pax-bin
%defattr(-,root,root)
%doc other-free.txt
%{_bindir}/pdfannotextractor

%files perltex-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/perltex

%files ppower4-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/pdfthumb
%{_bindir}/ppower4

%files splitindex-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/splitindex

%files svn-multi-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/svn-multi

%files vpe-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/vpe

%files collection-latexrecommended
%defattr(-,root,root)

%files thumbpdf-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/thumbpdf

%files collection-luatex
%defattr(-,root,root)

%files luaotfload-bin
%defattr(-,root,root)
%doc gpl2.txt
%{_bindir}/mkluatexfontdb

%files collection-mathextra
%defattr(-,root,root)

%files amstex-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/amstex

%files collection-music
%defattr(-,root,root)

%files musixflx-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/musixflx

%files collection-omega
%defattr(-,root,root)

%files aleph-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/aleph
%{_bindir}/lamed

%files omegaware-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/odvicopy
%{_bindir}/odvitype
%{_bindir}/ofm2opl
%{_bindir}/omfonts
%{_bindir}/opl2ofm
%{_bindir}/otangle
%{_bindir}/otp2ocp
%{_bindir}/outocp
%{_bindir}/ovf2ovp
%{_bindir}/ovp2ovf

%files collection-plainextra
%defattr(-,root,root)

%files collection-pstricks
%defattr(-,root,root)

%files pst2pdf-bin
%defattr(-,root,root)
%doc gpl.txt
%{_bindir}/pst2pdf

%files collection-publishers
%defattr(-,root,root)

%files collection-science
%defattr(-,root,root)

%files ulqda-bin
%defattr(-,root,root)
%doc lppl.txt
%{_bindir}/ulqda

%files collection-texinfo
%defattr(-,root,root)

%files collection-xetex
%defattr(-,root,root)

%files scheme-gust
%defattr(-,root,root)

%files scheme-medium
%defattr(-,root,root)

%files scheme-minimal
%defattr(-,root,root)

%files scheme-tetex
%defattr(-,root,root)

%files scheme-xml
%defattr(-,root,root)


%files kpathsea-lib
%defattr(-,root,root)
%{_libdir}/*.so.*

%files kpathsea-lib-devel
%defattr(-,root,root)
%dir %{_includedir}/kpathsea
%{_includedir}/kpathsea/*
%{_libdir}/*.so

%changelog
* Mon Aug 23 2010 Jindrich Novy <jnovy@redhat.com> 2010-9.20100814
- fix file attributes and rpmlint warnings
- define libdir when calling configure
- rebuild against new poppler

* Thu Jul 15 2010 Jindrich Novy <jnovy@redhat.com> 2010-8.20100715
- move all the licenses and base directory hierarchy to texlive-base
noarch subpackage
- add automatic licensing code

* Fri Jun  4 2010 Jindrich Novy <jnovy@redhat.com> 2010-7.20100604
- sync with upstream (introducing mptopdf)
- compile C source with -fno-strict-aliasing

* Mon May 31 2010 Jindrich Novy <jnovy@redhat.com> 2010-7.20100531
- switch to "tlpretest" source tree
- add lua and ruby dependencies to packages requiring them
- generate global package database "texlive.tlpdb" directly from
tlpobj files shipped with each package

* Wed May 19 2010 Jindrich Novy <jnovy@redhat.com> 2010-6.20100521
- disable chktex so that build passes
- fix dist tags in releases in binary packages

* Fri Apr 30 2010 Jindrich Novy <jnovy@redhat.com> 2010-5.20100430
- add dependencies resolution among biblatex files
- another %%postun scriptlets fix

* Wed Apr 21 2010 Jindrich Novy <jnovy@redhat.com> 2010-4.20100421
- add Requires(posttrans) to the main package

* Mon Apr 19 2010 Jindrich Novy <jnovy@redhat.com> 2010-3.20100419
- bump version of binaries because of the kpathsea soname increase

* Fri Apr 16 2010 Jindrich Novy <jnovy@redhat.com> 2010-0.1.20100416
- sync with upstream, remove ptex stuff for now

* Fri Apr 09 2010 Jindrich Novy <jnovy@redhat.com> 2010-0.1.20100329
- use 2010 prefix
- do not ship/build asymptote (#548761)

* Fri Mar 26 2010 Jindrich Novy <jnovy@redhat.com> 2009-3.20100326
- declare fmutil.cnf, updmap.cfg, context.cnf and texmf.cnf as config files
so that they don't get overwritten with texlive-kpathsea update
- move man and info pages to the main packages, not -doc

* Fri Feb 19 2010 Jindrich Novy <jnovy@redhat.com> 2009-3.20100219
- blacklist a4wide.sty because of bad (noinfo) license

* Tue Nov 10 2009 Jindrich Novy <jnovy@redhat.com> 2009-2
- install man and info pages into proper locations visible
by man and info
- update scriptlets
- remove xindy bits

* Mon Nov 09 2009 Jindrich Novy <jnovy@redhat.com> 2009-1
- update to oficcially released TeX Live 2009
- enable large file support

* Sun Nov 01 2009 Jindrich Novy <jnovy@redhat.com> 2009-0.13
- remove postun scriptlet to avoid accidential removal of texmf bits
when not removing the package

* Fri Oct 23 2009 Jindrich Novy <jnovy@redhat.com> 2009-0.12
- tighten kpathsea devel dependency

* Tue Oct 20 2009 Jindrich Novy <jnovy@redhat.com> 2009-0.11
- fix generation of packages that ships only documentation
- fix versioning of packages without version but with revision
- fix heuristics for gathering .sty files dependencies
- include packages under GFSL license
- make files in old texmf tree from previous installs visible
- do not obsolete old kpathsea, try to coexist
- remove dvipdfm, dvipdfmx,depend of Fedora ones

* Sun Oct 18 2009 Jindrich Novy <jnovy@redhat.com> 2009-0.10
- TL2007 compatibility fixes:
- create /usr/share/texmf symlink
- clean all in post scriptlets

* Fri Oct 02 2009 Jindrich Novy <jnovy@redhat.com> 2009-0.9
- fix kpathsea Provides/Obsoletes

* Tue Sep 29 2009 Jindrich Novy <jnovy@redhat.com> 2009-0.8
- sync with latest upstream

* Sat Sep 12 2009 Jindrich Novy <jnovy@redhat.com> 2009-0.7
- make kpathsea independent on the main texlive package

* Thu Sep 10 2009 Jindrich Novy <jnovy@redhat.com> 2009-0.6
- remove packages under GFSL non-free license (tex-gyre)

* Thu Sep  3 2009 Jindrich Novy <jnovy@redhat.com> 2009-0.5
- fix dependencies to hyphenation packages
- fix provides/obsoletes

* Mon Aug 31 2009 Jindrich Novy <jnovy@redhat.com> 2009-0.4
- require recommended LaTeX bits, the installation of pure
scheme-basic is too minimalistic

* Tue Aug 25 2009 Jindrich Novy <jnovy@redhat.com> 2009-0.3
- require system psutils and t1utils and don't build the TL ones
- correctly obsolete old kpathsea
- binaries now have -bin postfix
- support for Fedora fonts

* Thu Aug 20 2009 Jindrich Novy <jnovy@redhat.com> 2009-0.2
- add tetex-* virtual provides
- fix unversioned requires
- filter out unwanted libs and utilities from source

* Wed Aug 12 2009 Jindrich Novy <jnovy@redhat.com> 2009-0.1
- update to TeX Live 2009 - pretest

* Mon Jun 29 2009 Jindrich Novy <jnovy@redhat.com> 2008-0.2
- update to today's svn sources of binaries from upstream
- fix directory -> symlink conversion
- add ly1 (#488651)

* Thu Aug 14 2008 Jindrich Novy <jnovy@redhat.com> 2008-0.1
- initial packaging for TeX Live 2008
- wrote tl2rpm.c to autogenerate packages and post scriptlets
from TeX Live metadata
- fix kpathsea default search path
