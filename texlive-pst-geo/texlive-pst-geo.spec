%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/pst-geo.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/pst-geo.doc.tar.xz

Name: texlive-pst-geo
License: LPPL
Summary: Geographical Projections
Version: %{tl_version}
Release: %{tl_noarch_release}.2.03.svn17751%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(pst-map2d.sty)
Provides: tex(pst-map2dII.sty)
Provides: tex(pst-map3d.sty)
Provides: tex(pst-map3dII.sty)
Requires: tex(pstricks.sty)

%description
pst-geo is a set of PSTricks related packages for various
cartographic projections of the terrestrial sphere. The package
pst-map2d provides conventional projections such as Mercator,
Lambert, cylindrical, etc. The package pst-map3d treats
representation in three dimensions of the terrestrial sphere.
Packages pst-map2dII and pst-map3dII allow use of the CIA World
DataBank II. Various parameters of the packages allow for
choice of the level of the detail and the layouts possible
(cities, borders, rivers etc). Substantial data files are
provided, in an (internally) compressed format. Decompression
happens on-the-fly as a document using the data is displayed,
printed or converted to PDF format. A Perl script is provided
for the user to do the decompression, if the need should arise.

date: 2009-08-31 11:47:07 +0200

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
Summary: Documentation for pst-geo
Version: %{tl_version}
Release: %{tl_noarch_release}.2.03.svn17751%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for pst-geo


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
%{_texdir}/texmf-dist/dvips/pst-geo/pst-map3d.pro
%{_texdir}/texmf-dist/dvips/pst-geo/pst-map3dII.pro
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/README
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/aus.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/c-cap.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/c-sub.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/canada.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/capitales.tex
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/capitales3d.tex
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/capitals.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/cities.data
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/cities.tex
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/citycapitals.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/citysub.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/convert.py
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/corse.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/france.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/mex.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/pborder.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/pcoast.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/pisland.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/plake.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/rhone.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/ridge.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/river.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/seine.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/transfrm.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/trench.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/usa.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/villesFrance.tex
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/villesFrance3d.tex
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/villesItalia.tex
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/villesItalia3d.tex
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/wfraczon.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/data/wmaglin.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/dataII/README
%{_texdir}/texmf-dist/tex/generic/pst-geo/dataII/africa-bdy.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/dataII/africa-cil.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/dataII/africa-riv.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/dataII/asia-bdy.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/dataII/asia-cil.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/dataII/asia-isl.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/dataII/asia-riv.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/dataII/c-cap.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/dataII/c-sub.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/dataII/citycapitals.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/dataII/citysub.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/dataII/europe-bdy.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/dataII/europe-cil.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/dataII/europe-riv.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/dataII/namer-bdy.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/dataII/namer-cil.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/dataII/namer-pby.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/dataII/namer-riv.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/dataII/samer-arc.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/dataII/samer-bdy.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/dataII/samer-cil.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/dataII/samer-riv.dat
%{_texdir}/texmf-dist/tex/generic/pst-geo/pst-map2d.tex
%{_texdir}/texmf-dist/tex/generic/pst-geo/pst-map2dII.tex
%{_texdir}/texmf-dist/tex/generic/pst-geo/pst-map3d.tex
%{_texdir}/texmf-dist/tex/generic/pst-geo/pst-map3dII.tex
%{_texdir}/texmf-dist/tex/latex/pst-geo/pst-map2d.sty
%{_texdir}/texmf-dist/tex/latex/pst-geo/pst-map2dII.sty
%{_texdir}/texmf-dist/tex/latex/pst-geo/pst-map3d.sty
%{_texdir}/texmf-dist/tex/latex/pst-geo/pst-map3dII.sty

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/generic/pst-geo/Changes
%{_texdir}/texmf-dist/doc/generic/pst-geo/PSTricks.bib
%{_texdir}/texmf-dist/doc/generic/pst-geo/README
%{_texdir}/texmf-dist/doc/generic/pst-geo/pst-geo-compress.pl
%{_texdir}/texmf-dist/doc/generic/pst-geo/pst-geo-decompress.pl
%{_texdir}/texmf-dist/doc/generic/pst-geo/pst-map2d-doc.pdf
%{_texdir}/texmf-dist/doc/generic/pst-geo/pst-map2d-doc.tex
%{_texdir}/texmf-dist/doc/generic/pst-geo/pst-map2dII-doc.pdf
%{_texdir}/texmf-dist/doc/generic/pst-geo/pst-map2dII-doc.tex
%{_texdir}/texmf-dist/doc/generic/pst-geo/pst-map3d-doc-pdf.pdf
%{_texdir}/texmf-dist/doc/generic/pst-geo/pst-map3d-doc-pdf.tex
%{_texdir}/texmf-dist/doc/generic/pst-geo/pst-map3d-doc.pdf
%{_texdir}/texmf-dist/doc/generic/pst-geo/pst-map3d-doc.tex
%{_texdir}/texmf-dist/doc/generic/pst-geo/pst-map3dII-doc.pdf
%{_texdir}/texmf-dist/doc/generic/pst-geo/pst-map3dII-doc.tex


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
