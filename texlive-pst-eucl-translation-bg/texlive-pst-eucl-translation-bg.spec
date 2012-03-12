%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/pst-eucl-translation-bg.doc.tar.xz

Name: texlive-pst-eucl-translation-bg-doc
License: GFDL
Summary: Documentation for pst-eucl-translation-bg
Version: %{tl_version}
Release: %{tl_noarch_release}.1.3.2.svn19296%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description
Documentation for pst-eucl-translation-bg


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/fdl.txt fdl.txt
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
%doc fdl.txt
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/abscur.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/abscur_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/angle.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/angle_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/arc.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/arc_in.log
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/arc_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/astro.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/astro_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/bissec.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/bissec_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/ccirc.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/ccirc_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/cercle.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/cercle_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/cinscex.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/cinscex_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/curvetype.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/curvetype_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/cyclo.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/cyclo_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/delto.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/droite.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/droite_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/envcardi.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/envcardi_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/envellipse.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/envellipse_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/euler.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/euler_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/fracthom.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/fracthom_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/gal_biss.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/gal_biss_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/gauss.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/gauss_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/gencur.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/gencur_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/geohyper.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/geohyper_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/geonode.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/geonode_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/german_ra.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/german_ra_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/grav.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/grav_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/homothetie.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/homothetie_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/hyperbole.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/hyperbole_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/hypocyclo.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/interCC.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/interCC_bis_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/interCC_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/interDC.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/interDC_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/interDD.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/interDD_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/interFC.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/interFC_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/interFF.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/interFF_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/interFL.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/interFL_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/mediator.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/mediator_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/milieu.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/milieu_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/oij.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/oij_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/orthocentre.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/orthocentre_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/orthoethyper.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/orthoethyper_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/parabole.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/parabole_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/projection.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/projection_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/ptfermat.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/ptfermat_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/remarq.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/remarq_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/rotation.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/rotation_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/segmentmark.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/segmentmark_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/symcentrale.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/symcentrale_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/symorthogonale.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/symorthogonale_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/tg1c.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/tg1c_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/tg2c.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/tg2c_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/translation.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/translation_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/triangle.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/Exemples/triangle_in.tex
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/README
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/README-bulgarian.txt
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/euclide_bg.sty
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/euclide_macros.ist
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/pst-eucl-docBG.cb
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/pst-eucl-docBG.pdf
%{_texdir}/texmf-dist/doc/latex/pst-eucl-translation-bg/pst-eucl-docBG.tex


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
