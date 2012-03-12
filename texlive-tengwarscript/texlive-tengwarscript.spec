%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/tengwarscript.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/tengwarscript.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/tengwarscript.source.tar.xz

Name: texlive-tengwarscript
License: LPPL
Summary: LaTeX support for using Tengwar fonts
Version: %{tl_version}
Release: %{tl_noarch_release}.1.3.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(tengwarscript.sty)
Requires: tex(fp-basic.sty)
Requires: tex(fp-snap.sty)

%description
The package provides "mid-level" access to tengwar fonts,
providing good quality output. Each tengwar sign is represented
by a command, which will place the sign nicely in relation to
previous signs. A transcription package is available from the
package's home page: writing all those tengwar commands would
quickly become untenable. The package supports the use of a
wide variety of tengwar fonts that are available from the net;
metric and map files are provided for all the supported fonts.

date: 2007-05-24 10:43:22 +0200

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
Summary: Documentation for tengwarscript
Version: %{tl_version}
Release: %{tl_noarch_release}.1.3.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for tengwarscript


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
%{_texdir}/texmf-dist/fonts/enc/dvips/tengwarscript/tengwaralt.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tengwarscript/tengwarcap.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tengwarscript/tengwarscript.enc
%{_texdir}/texmf-dist/fonts/map/dvips/tengwarscript/tengwarscript.map
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/Elfica32.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/Parmaite.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/Parmaite_alt.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/Parmaite_full.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/TengwarFormal12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/TengwarFormalA12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/TengwarFormal_full.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/TengwarGothika050.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/TengwarNoldor.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/TengwarNoldorAlt.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/TengwarNoldorCapitals1.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/TengwarNoldorCapitals2.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/TengwarNoldor_full.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/TengwarQuenya.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/TengwarQuenyaAlt.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/TengwarQuenyaCapitals1.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/TengwarQuenyaCapitals2.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/TengwarQuenya_full.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/TengwarSindarin.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/TengwarSindarinAlt.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/TengwarSindarinCapitals1.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/TengwarSindarinCapitals2.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/TengwarSindarin_full.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/TengwarTelerin.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/UnicodeParmaite.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/tngan.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/tngan_full.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/tngana.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/tnganab.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/tnganabi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/tnganai.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/tnganb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/tnganb_full.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/tnganbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/tnganbi_full.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/tngani.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tengwarscript/tngani_full.tfm
%{_texdir}/texmf-dist/fonts/vf/public/tengwarscript/Parmaite_full.vf
%{_texdir}/texmf-dist/fonts/vf/public/tengwarscript/TengwarFormal_full.vf
%{_texdir}/texmf-dist/fonts/vf/public/tengwarscript/TengwarNoldor_full.vf
%{_texdir}/texmf-dist/fonts/vf/public/tengwarscript/TengwarQuenya_full.vf
%{_texdir}/texmf-dist/fonts/vf/public/tengwarscript/TengwarSindarin_full.vf
%{_texdir}/texmf-dist/fonts/vf/public/tengwarscript/tngan_full.vf
%{_texdir}/texmf-dist/fonts/vf/public/tengwarscript/tnganb_full.vf
%{_texdir}/texmf-dist/fonts/vf/public/tengwarscript/tnganbi_full.vf
%{_texdir}/texmf-dist/fonts/vf/public/tengwarscript/tngani_full.vf
%{_texdir}/texmf-dist/tex/latex/tengwarscript/annatar.cfg
%{_texdir}/texmf-dist/tex/latex/tengwarscript/annatarbold.cfg
%{_texdir}/texmf-dist/tex/latex/tengwarscript/annatarbolditalic.cfg
%{_texdir}/texmf-dist/tex/latex/tengwarscript/annataritalic.cfg
%{_texdir}/texmf-dist/tex/latex/tengwarscript/elfica.cfg
%{_texdir}/texmf-dist/tex/latex/tengwarscript/formal.cfg
%{_texdir}/texmf-dist/tex/latex/tengwarscript/gothika.cfg
%{_texdir}/texmf-dist/tex/latex/tengwarscript/noldor.cfg
%{_texdir}/texmf-dist/tex/latex/tengwarscript/noldorcapI.cfg
%{_texdir}/texmf-dist/tex/latex/tengwarscript/noldorcapII.cfg
%{_texdir}/texmf-dist/tex/latex/tengwarscript/parmaite.cfg
%{_texdir}/texmf-dist/tex/latex/tengwarscript/quenya.cfg
%{_texdir}/texmf-dist/tex/latex/tengwarscript/quenyacapI.cfg
%{_texdir}/texmf-dist/tex/latex/tengwarscript/quenyacapII.cfg
%{_texdir}/texmf-dist/tex/latex/tengwarscript/sindarin.cfg
%{_texdir}/texmf-dist/tex/latex/tengwarscript/sindarincapI.cfg
%{_texdir}/texmf-dist/tex/latex/tengwarscript/sindarincapII.cfg
%{_texdir}/texmf-dist/tex/latex/tengwarscript/teleri.cfg
%{_texdir}/texmf-dist/tex/latex/tengwarscript/tengwarscript.sty
%{_texdir}/texmf-dist/tex/latex/tengwarscript/unicodeparmaite.cfg

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/tengwarscript/COPYING
%{_texdir}/texmf-dist/doc/latex/tengwarscript/README
%{_texdir}/texmf-dist/doc/latex/tengwarscript/quetta.eps
%{_texdir}/texmf-dist/doc/latex/tengwarscript/quetta.pdf
%{_texdir}/texmf-dist/doc/latex/tengwarscript/tengfonts.pdf
%{_texdir}/texmf-dist/doc/latex/tengwarscript/tengfonts.tex
%{_texdir}/texmf-dist/doc/latex/tengwarscript/tengtest.pdf
%{_texdir}/texmf-dist/doc/latex/tengwarscript/tengtest.tex
%{_texdir}/texmf-dist/doc/latex/tengwarscript/tengwarscript.pdf


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
