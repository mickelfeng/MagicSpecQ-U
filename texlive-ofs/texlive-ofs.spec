%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/ofs.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/ofs.doc.tar.xz

Name: texlive-ofs
License: Knuth
Summary: Macros for managing large font collections
Version: %{tl_version}
Release: %{tl_noarch_release}.svn16991%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(a35.sty)
Provides: tex(allfonts.sty)
Provides: tex(ofs.sty)

%description
OFS (Olsak's Font System) is a set of Plain TeX and LaTeX
macros for managing large font collections; it has been used by
Czech/Slovak users for many years. Main features include: -
Mapping from long names of fonts to the metric file name. The
user can specify only exact long names in documents. - Support
for many font encodings. - Printing of catalogues of fonts and
test samples of font families; the interactive macro \showfonts
shows all font families you have installed via OFS. - The user
interface is the same for Plain TeX and for LaTeX, but the
implementation differs: the LaTeX variant of OFS uses NFSS, but
the Plain variant implements its own font management (which may
even be better than NFSS) - Support for math fonts including TX
fonts.

date: 2010-02-12 21:26:56 +0100

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
Summary: Documentation for ofs
Version: %{tl_version}
Release: %{tl_noarch_release}.svn16991%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for ofs


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/knuth.txt knuth.txt
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
%doc knuth.txt
%{_texdir}/texmf-dist/tex/generic/ofs/a117.tex
%{_texdir}/texmf-dist/tex/generic/ofs/a35.sty
%{_texdir}/texmf-dist/tex/generic/ofs/a35.tex
%{_texdir}/texmf-dist/tex/generic/ofs/allfonts.sty
%{_texdir}/texmf-dist/tex/generic/ofs/allfonts.tex
%{_texdir}/texmf-dist/tex/generic/ofs/amsfn.tex
%{_texdir}/texmf-dist/tex/generic/ofs/mtfn.tex
%{_texdir}/texmf-dist/tex/generic/ofs/ofs-6a.tex
%{_texdir}/texmf-dist/tex/generic/ofs/ofs-6c.tex
%{_texdir}/texmf-dist/tex/generic/ofs/ofs-6k.tex
%{_texdir}/texmf-dist/tex/generic/ofs/ofs-6s.tex
%{_texdir}/texmf-dist/tex/generic/ofs/ofs-6t.tex
%{_texdir}/texmf-dist/tex/generic/ofs/ofs-6x.tex
%{_texdir}/texmf-dist/tex/generic/ofs/ofs-6y.tex
%{_texdir}/texmf-dist/tex/generic/ofs/ofs-8c.tex
%{_texdir}/texmf-dist/tex/generic/ofs/ofs-8t.tex
%{_texdir}/texmf-dist/tex/generic/ofs/ofs-8x.tex
%{_texdir}/texmf-dist/tex/generic/ofs/ofs-8z.tex
%{_texdir}/texmf-dist/tex/generic/ofs/ofs-ams.tex
%{_texdir}/texmf-dist/tex/generic/ofs/ofs-cm.tex
%{_texdir}/texmf-dist/tex/generic/ofs/ofs-mt.tex
%{_texdir}/texmf-dist/tex/generic/ofs/ofs-ps.tex
%{_texdir}/texmf-dist/tex/generic/ofs/ofs-px.tex
%{_texdir}/texmf-dist/tex/generic/ofs/ofs-slt.tex
%{_texdir}/texmf-dist/tex/generic/ofs/ofs-tx.tex
%{_texdir}/texmf-dist/tex/generic/ofs/ofs.sty
%{_texdir}/texmf-dist/tex/generic/ofs/ofs.tex
%{_texdir}/texmf-dist/tex/generic/ofs/ofsdef.tex
%{_texdir}/texmf-dist/tex/generic/ofs/pantyk.tex
%{_texdir}/texmf-dist/tex/generic/ofs/txfn.tex

%files doc
%defattr(-,root,root)
%doc knuth.txt
%{_texdir}/texmf-dist/doc/generic/ofs/changes.txt
%{_texdir}/texmf-dist/doc/generic/ofs/eurotex2003-ofs.pdf
%{_texdir}/texmf-dist/doc/generic/ofs/eurotex2003-ofs.tex
%{_texdir}/texmf-dist/doc/generic/ofs/ofs-slt.pdf
%{_texdir}/texmf-dist/doc/generic/ofs/ofsdoc-e.pdf
%{_texdir}/texmf-dist/doc/generic/ofs/ofsdoc-e.tex
%{_texdir}/texmf-dist/doc/generic/ofs/ofsdoc.pdf
%{_texdir}/texmf-dist/doc/generic/ofs/ofsdoc.tex
%{_texdir}/texmf-dist/doc/generic/ofs/ofsmtdef.tex
%{_texdir}/texmf-dist/doc/generic/ofs/ofstest.tex
%{_texdir}/texmf-dist/doc/generic/ofs/readme.ofs


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
