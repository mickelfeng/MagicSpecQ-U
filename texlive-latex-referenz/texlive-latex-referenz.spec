%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/latex-referenz.doc.tar.xz

Name: texlive-latex-referenz-doc
License: LPPL
Summary: Documentation for latex-referenz
Version: %{tl_version}
Release: %{tl_noarch_release}.svn16980%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description
Documentation for latex-referenz


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
%{_texdir}/texmf-dist/doc/latex/latex-referenz/01-03-1.xltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/01-04-1.lux
%{_texdir}/texmf-dist/doc/latex/latex-referenz/01-04-2.lux
%{_texdir}/texmf-dist/doc/latex/latex-referenz/02-03-1.ltxps
%{_texdir}/texmf-dist/doc/latex/latex-referenz/02-03-2.ltx2crop
%{_texdir}/texmf-dist/doc/latex/latex-referenz/02-03-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/02-03-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/03-03-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/03-04-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/03-05-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/03-06-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/03-07-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/03-08-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/04-02-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/05-01-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/06-03-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/06-03-10.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/06-03-11.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/06-03-12.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/06-03-13.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/06-03-14.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/06-03-15.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/06-03-16.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/06-03-17.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/06-03-18.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/06-03-19.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/06-03-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/06-03-20.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/06-03-21.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/06-03-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/06-03-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/06-03-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/06-03-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/06-03-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/06-03-8.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/06-03-9.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-03-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-03-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-03-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-03-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-05-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-05-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-05-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-05-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-05-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-05-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-05-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-05-8.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-07-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-07-10.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-07-11.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-07-12.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-07-13.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-07-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-07-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-07-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-07-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-07-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-07-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-07-8.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-07-9.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-08-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-08-10.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-08-11.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-08-12.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-08-13.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-08-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-08-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-08-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-08-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-08-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-08-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-08-8.ltxps
%{_texdir}/texmf-dist/doc/latex/latex-referenz/08-08-9.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/09-02-1.ltx2crop
%{_texdir}/texmf-dist/doc/latex/latex-referenz/09-03-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/09-03-10.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/09-03-11.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/09-03-12.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/09-03-13.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/09-03-14.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/09-03-15.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/09-03-16.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-referenz/09-03-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/09-03-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/09-03-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/09-03-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/09-03-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/09-03-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/09-03-8.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/09-03-9.ltx
%{_texdir}/texmf-dist/doc/latex/latex-referenz/README


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
