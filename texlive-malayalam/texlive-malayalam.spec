%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/malayalam.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/malayalam.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/malayalam.source.tar.xz

Name: texlive-malayalam
License: LPPL
Summary: LaTeX for Malayalam
Version: %{tl_version}
Release: %{tl_noarch_release}.0.9.6.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}

%description
Fonts (in Adobe Type 1 format), metrics and macros for
typesetting Malayalam with LaTeX.

date: 2007-11-17 22:03:55 +0100

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
Summary: Documentation for malayalam
Version: %{tl_version}
Release: %{tl_noarch_release}.0.9.6.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for malayalam


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
%{_texdir}/texmf-dist/fonts/source/public/malayalam/effects/effect.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/effects/esoteric.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/effects/hstripes.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/effects/malayalam-reverse.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/effects/outline.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/effects/shadow.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/fnt_code.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/mm.bat
%{_texdir}/texmf-dist/fonts/source/public/malayalam/mm.fts
%{_texdir}/texmf-dist/fonts/source/public/malayalam/mm.job
%{_texdir}/texmf-dist/fonts/source/public/malayalam/mmcillu.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/mmcoding.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/mmconj.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/mmcons.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/mmcvconj.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/mmdefs.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/mmfnt.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/mmfont.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/mmlnums.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/mmnums.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/mmpunct.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/mmrconj.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/mmscons.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/mmsec.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/mmstyles.txt
%{_texdir}/texmf-dist/fonts/source/public/malayalam/mmtest.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/mmvowels.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/orn10.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/rejected.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/var_ja.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mm10.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mm10s.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mm12.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mm12s.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mm17.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mm17s.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mm6.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mm6s.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mm8.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mm8s.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmb10.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmb10s.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmb12.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmb12s.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmb17.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmb17s.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmbig.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmbigo.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmc10.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmc10s.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmc12.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmc12s.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmc17.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmc17s.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmcb10.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmcb10s.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmcb12.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmcb12s.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmcb17.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmcb17s.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmcsl10.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmcsl10s.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmcsl12.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmcsl12s.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmexpa12.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmexpb12.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmexpc12.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmsl10.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmsl10s.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmsl12.mf
%{_texdir}/texmf-dist/fonts/source/public/malayalam/styles/mmsl12s.mf
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mm10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mm10s.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mm12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mm12s.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mm17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mm17s.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mm6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mm6s.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mm8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mm8s.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmb10s.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmb12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmb12s.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmb17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmb17s.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmbig.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmbigo.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmc10s.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmc12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmc12s.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmc17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmc17s.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmcb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmcb10s.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmcb12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmcb12s.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmcb17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmcb17s.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmcsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmcsl10s.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmcsl12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmcsl12s.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmexpa12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmexpb12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmexpc12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmsl10s.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmsl12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/mmsl12s.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/malayalam/orn10.tfm

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/fonts/malayalam/FILES
%{_texdir}/texmf-dist/doc/fonts/malayalam/INSTALL
%{_texdir}/texmf-dist/doc/fonts/malayalam/README
%{_texdir}/texmf-dist/doc/fonts/malayalam/charity
%{_texdir}/texmf-dist/doc/fonts/malayalam/todo
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/elephant.mm
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/elephant.tex
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/lion.mm
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/lion.tex
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmarticl.mm
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmarticl.tex
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmchart.tex
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmconj.mm
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmconj.tex
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmexp.mm
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmexp.tex
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmfont.tex
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmfuture.tex
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmguide.dvi
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmguide.mm
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmguide.tex
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmmacs.tex
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmphmacs.tex
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmqfont.tex
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmqmacs.tex
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmsample.mm
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmsample.tex
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmscript.mm
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmtable.mm
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmtable.tex
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmtrans.mm
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmtrans.tex
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmtrmacs.tex
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/mmxfont.tex
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/ornament.tex
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/prodigal.mm
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/prodigal.tex
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/test.mm
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/test.tex
%{_texdir}/texmf-dist/doc/fonts/malayalam/article/twolines.tex


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
