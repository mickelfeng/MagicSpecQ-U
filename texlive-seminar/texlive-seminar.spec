%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/seminar.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/seminar.doc.tar.xz

Name: texlive-seminar
License: LPPL
Summary: Make overhead slides
Version: %{tl_version}
Release: %{tl_noarch_release}.1.5.svn18322%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(npsfont.sty)
Provides: tex(sem-a4.sty)
Provides: tex(sem-page.sty)
Provides: tex(semcolor.sty)
Provides: tex(semhelv.sty)
Provides: tex(seminar.sty)
Provides: tex(semlayer.sty)
Provides: tex(semlcmss.sty)
Provides: tex(semrot.sty)
Provides: tex(slidesec.sty)
Requires: tex(pstricks.sty)

%description
A class that produces overhead slides (transparencies), with
many facilities. The class requires availability of the
fancybox package. Seminar is also the basis of other classes,
such as prosper. In fact, seminar is not nowadays reckoned a
good basis for a presentation -- users are advised to use more
recent classes such as powerdot or beamer, both of which are
tuned to 21st-century presentation styles. Note that the
seminar distribution relies on the xcomment package, which was
once part of the bundle, but now has a separate existence.

date: 2010-05-17 14:53:01 +0200

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
Summary: Documentation for seminar
Version: %{tl_version}
Release: %{tl_noarch_release}.1.5.svn18322%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for seminar


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/lppl1.2.txt lppl1.2.txt
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
%doc lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/seminar/npsfont.sty
%{_texdir}/texmf-dist/tex/latex/seminar/sem-a4.sty
%{_texdir}/texmf-dist/tex/latex/seminar/sem-page.sty
%{_texdir}/texmf-dist/tex/latex/seminar/semcolor.sty
%{_texdir}/texmf-dist/tex/latex/seminar/semhelv.sty
%{_texdir}/texmf-dist/tex/latex/seminar/seminar.bg2
%{_texdir}/texmf-dist/tex/latex/seminar/seminar.bug
%{_texdir}/texmf-dist/tex/latex/seminar/seminar.cls
%{_texdir}/texmf-dist/tex/latex/seminar/seminar.sty
%{_texdir}/texmf-dist/tex/latex/seminar/semlayer.sty
%{_texdir}/texmf-dist/tex/latex/seminar/semlcmss.sty
%{_texdir}/texmf-dist/tex/latex/seminar/semrot.sty
%{_texdir}/texmf-dist/tex/latex/seminar/slidesec.sty

%files doc
%defattr(-,root,root)
%doc lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/seminar/read-me.2e
%{_texdir}/texmf-dist/doc/latex/seminar/sem-read.me
%{_texdir}/texmf-dist/doc/latex/seminar/sem-user.pdf
%{_texdir}/texmf-dist/doc/latex/seminar/sem-user.tex
%{_texdir}/texmf-dist/doc/latex/seminar/semsamp1.tex
%{_texdir}/texmf-dist/doc/latex/seminar/semsamp2.tex
%{_texdir}/texmf-dist/doc/latex/seminar/tvz-code.sty
%{_texdir}/texmf-dist/doc/latex/seminar/tvz-hax.sty
%{_texdir}/texmf-dist/doc/latex/seminar/tvz-user.sty


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
