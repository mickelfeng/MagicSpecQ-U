%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/beebe.tar.xz

Name: texlive-beebe
License: LPPL
Summary: beebe package
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18307%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}

%description
beebe package

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
%{_texdir}/texmf-dist/bibtex/bib/beebe/gut.bib
%{_texdir}/texmf-dist/bibtex/bib/beebe/komoedie.bib
%{_texdir}/texmf-dist/bibtex/bib/beebe/texbook1.bib
%{_texdir}/texmf-dist/bibtex/bib/beebe/texbook2.bib
%{_texdir}/texmf-dist/bibtex/bib/beebe/texbook3.bib
%{_texdir}/texmf-dist/bibtex/bib/beebe/texgraph.bib
%{_texdir}/texmf-dist/bibtex/bib/beebe/texjourn.bib
%{_texdir}/texmf-dist/bibtex/bib/beebe/texnique.bib
%{_texdir}/texmf-dist/bibtex/bib/beebe/tugboat.bib
%{_texdir}/texmf-dist/bibtex/bst/beebe/aaai-named.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/abstract.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/annotate.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/annotation.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/apa.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/apalike2.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/astron.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/authordate1.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/authordate2.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/authordate3.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/authordate4.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/bbs.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/bibtoref.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/cbe.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/chicagoa.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/econometrica.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/humanbio.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/humannat.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/is-abbrv.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/is-alpha.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/is-plain.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/is-unsrt.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/jas99.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/jbact.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/jmb.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/jtb.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/jthcarsu.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/named.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/namunsrt.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/nar.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/newapa.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/phaip.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/phapalik.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/phcpc.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/phiaea.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/phjcp.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/phnf.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/phnflet.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/phpf.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/phppcf.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/phreport.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/phrmp.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/plainyr.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/refer.bst
%{_texdir}/texmf-dist/bibtex/bst/beebe/xbtxbst.doc


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
