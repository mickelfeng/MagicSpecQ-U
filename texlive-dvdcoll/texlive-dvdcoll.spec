%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/dvdcoll.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/dvdcoll.doc.tar.xz

Name: texlive-dvdcoll
License: LPPL
Summary: A class for typesetting DVD archives
Version: %{tl_version}
Release: %{tl_noarch_release}.v1.1a.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(dcwrtbib.sty)
Provides: tex(dvdcoll.sty)
Provides: tex(pdfnotiz.sty)
Requires: tex(afterpage.sty)
Requires: tex(xkeyval.sty)
Requires: tex(ifthen.sty)
Requires: tex(tabularx.sty)
Requires: tex(booktabs.sty)
Requires: tex(array.sty)
Requires: tex(multicol.sty)
Requires: tex(ragged2e.sty)
Requires: tex(hyperref.sty)
Requires: tex(ifpdf.sty)
Requires: tex(marginnote.sty)

%description
Having lost the overview of my DVD archives, I simply could not
remember if I already recorded the documentary running on TV
that day. I chose to recreate the index using LaTeX: the design
aim was a hyperlinked and fully searchable PDF-document,
listing my DVDs with all titles, lengths and so on. Further
requirements were support for seasons of tv series and a list
with all faulty or missing programs for rerecording. The
dvdcoll class supports all these requirements. dvdcoll.cls
follows the structure <number><title><length>. As a result, the
class is not limited to DVDs--you can of course typeset
archives of CD-ROMs, Audio-CDs and so on. Supported languages
at the moment: English, French, German, Italian, Polish,
Portuguese, Spanish. Some help is needed for other languages!

date: 2008-04-30 11:48:45 +0200

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
Summary: Documentation for dvdcoll
Version: %{tl_version}
Release: %{tl_noarch_release}.v1.1a.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for dvdcoll


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
%{_texdir}/texmf-dist/bibtex/bst/dvdcoll/dcbib.bst
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/UKenglish.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/USenglish.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/acadian.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/american.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/australian.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/austrian.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/brazil.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/brazilian.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/british.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/canadian.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/canadien.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/english.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/francais.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/french.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/frenchb.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/german.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/germanb.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/italian.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/naustrian.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/newzealand.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/ngerman.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/polish.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/portuges.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/portuguese.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcl/spanish.dcl
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dcwrtbib.sty
%{_texdir}/texmf-dist/tex/latex/dvdcoll/dvdcoll.cls
%{_texdir}/texmf-dist/tex/latex/dvdcoll/pdfnotiz.sty

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/dvdcoll/CHANGES
%{_texdir}/texmf-dist/doc/latex/dvdcoll/INSTALL
%{_texdir}/texmf-dist/doc/latex/dvdcoll/README
%{_texdir}/texmf-dist/doc/latex/dvdcoll/dcexample.pdf
%{_texdir}/texmf-dist/doc/latex/dvdcoll/dcexample.tex
%{_texdir}/texmf-dist/doc/latex/dvdcoll/dvdcoll.pdf
%{_texdir}/texmf-dist/doc/latex/dvdcoll/dvdcoll_de.pdf
%{_texdir}/texmf-dist/doc/latex/dvdcoll/manifest.txt


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
