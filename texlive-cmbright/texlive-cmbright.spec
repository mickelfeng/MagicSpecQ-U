%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cmbright.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cmbright.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cmbright.source.tar.xz

Name: texlive-cmbright
License: LPPL
Summary: Computer Modern Bright fonts
Version: %{tl_version}
Release: %{tl_noarch_release}.8.1.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(cmbright.sty)

%description
A family of sans serif fonts for TeX and LaTeX, based on Donald
Knuth's CM fonts. It comprises OT1, T1 and TS1 encoded text
fonts of various shapes as well as all the fonts necessary for
mathematical typesetting, including AMS symbols. This
collection provides all the necessary files for using the fonts
with LaTeX. A commercial-quality Adobe Type 1 version of these
fonts is available from Micropress. Free versions are
available, in the cm-super font bundle (the T1 and TS1 encoded
part of the set), and in the hfbright (the OT1 encoded part,
and the maths fonts).

date: 2007-01-01 00:37:00 +0100

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
Summary: Documentation for cmbright
Version: %{tl_version}
Release: %{tl_noarch_release}.8.1.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for cmbright


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
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ams10pt.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ams8pt.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ams9pt.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/baccent.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/bgreeku.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/bitalms.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/bpunct.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/br10pt.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/br17pt.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/br8pt.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/br9pt.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/brmsa.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/brmsb.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/broman.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/bromanl.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/bromlig.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/bromms.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/brs10pt.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/brs17pt.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/brs8pt.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/brs9pt.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/cmbr10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/cmbr17.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/cmbr8.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/cmbr9.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/cmbras10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/cmbras8.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/cmbras9.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/cmbrbs10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/cmbrbs8.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/cmbrbs9.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/cmbrbx10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/cmbrmb10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/cmbrmi10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/cmbrmi8.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/cmbrmi9.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/cmbrsl10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/cmbrsl17.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/cmbrsl8.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/cmbrsl9.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/cmbrsy10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/cmbrsy8.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/cmbrsy9.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/cmsltl10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/cmtl10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebaccess.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebbase.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebbraces.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebbx10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebmo10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebmo17.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebmo8.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebmo9.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebmr10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebmr17.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebmr8.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebmr9.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebpseudo.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebpunct.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebrleast.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebrlig.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebrligtb.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebrllett.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebrlwest.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebroman.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebso10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebso17.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebso8.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebso9.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebsr10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebsr17.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebsr8.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebsr9.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebtl10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ebto10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/mathsl.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/msa.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/msb.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/tbbx10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/tbmo10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/tbmo17.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/tbmo8.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/tbmo9.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/tbmr10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/tbmr17.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/tbmr8.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/tbmr9.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/tbpseudo.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/tbso10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/tbso17.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/tbso8.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/tbso9.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/tbsr10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/tbsr17.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/tbsr8.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/tbsr9.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/tbsymb.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/tbsymbol.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/tbtl10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/tbto10.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ttsymb.mf
%{_texdir}/texmf-dist/fonts/source/public/cmbright/ttsymbol.mf
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/cmbr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/cmbr17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/cmbr8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/cmbr9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/cmbras10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/cmbras8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/cmbras9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/cmbrbs10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/cmbrbs8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/cmbrbs9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/cmbrbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/cmbrmb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/cmbrmi10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/cmbrmi8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/cmbrmi9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/cmbrsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/cmbrsl17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/cmbrsl8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/cmbrsl9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/cmbrsy10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/cmbrsy8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/cmbrsy9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/cmsltl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/cmtl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/ebbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/ebmo10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/ebmo17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/ebmo8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/ebmo9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/ebmr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/ebmr17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/ebmr8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/ebmr9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/ebso10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/ebso17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/ebso8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/ebso9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/ebsr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/ebsr17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/ebsr8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/ebsr9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/ebtl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/ebto10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/tbbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/tbmo10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/tbmo17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/tbmo8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/tbmo9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/tbmr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/tbmr17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/tbmr8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/tbmr9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/tbso10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/tbso17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/tbso8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/tbso9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/tbsr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/tbsr17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/tbsr8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/tbsr9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/tbtl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/tbto10.tfm
%{_texdir}/texmf-dist/tex/latex/cmbright/cmbright.sty
%{_texdir}/texmf-dist/tex/latex/cmbright/omlcmbr.fd
%{_texdir}/texmf-dist/tex/latex/cmbright/omlcmbrm.fd
%{_texdir}/texmf-dist/tex/latex/cmbright/omscmbr.fd
%{_texdir}/texmf-dist/tex/latex/cmbright/omscmbrs.fd
%{_texdir}/texmf-dist/tex/latex/cmbright/ot1cmbr.fd
%{_texdir}/texmf-dist/tex/latex/cmbright/ot1cmtl.fd
%{_texdir}/texmf-dist/tex/latex/cmbright/t1cmbr.fd
%{_texdir}/texmf-dist/tex/latex/cmbright/t1cmtl.fd
%{_texdir}/texmf-dist/tex/latex/cmbright/ts1cmbr.fd
%{_texdir}/texmf-dist/tex/latex/cmbright/ts1cmtl.fd

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/fonts/cmbright/LICENSE
%{_texdir}/texmf-dist/doc/fonts/cmbright/README
%{_texdir}/texmf-dist/doc/fonts/cmbright/cmbright.txt
%{_texdir}/texmf-dist/doc/fonts/cmbright/manifest.txt
%{_texdir}/texmf-dist/doc/latex/cmbright/cmbright.pdf

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
