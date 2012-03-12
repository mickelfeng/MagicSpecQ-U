%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/interactiveworkbook.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/interactiveworkbook.doc.tar.xz

Name: texlive-interactiveworkbook
License: LPPL
Summary: latex-based interactive PDF on the web
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(interactiveworkbook-web.sty)
Provides: tex(interactiveworkbook.sty)
Requires: tex(epsfig.sty)
Requires: tex(color.sty)
Requires: tex(xspace.sty)
Requires: tex(ifthen.sty)

%description
The package interactiveworkbook gives the user the ability to
write LaTeX documents which, ultimately, create interactive
question-and-answer Portable Document Format (PDF) tutorials
meant to be used by Internet students and that, in particular,
freely use mathematical notation.

date: 2006-10-06 13:44:13 +0200

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
Summary: Documentation for interactiveworkbook
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for interactiveworkbook


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
%{_texdir}/texmf-dist/tex/latex/interactiveworkbook/interactiveworkbook-web.sty
%{_texdir}/texmf-dist/tex/latex/interactiveworkbook/interactiveworkbook.sty

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/documentation/interactiveworkbookmanual.pdf
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/documentation/interactiveworkbookmanual.tex
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/WS_FTP.LOG
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/buttonappearance.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/checkclear.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/checksubmit.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/exerques1.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/exerques10.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/exerques11.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/exerques12.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/exerques13.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/exerques14.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/exerques15.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/exerques16.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/exerques17.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/exerques18.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/exerques19.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/exerques2.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/exerques20.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/exerques3.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/exerques4.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/exerques5.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/exerques6.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/exerques7.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/exerques8.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/exerques9.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/fieldclear.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/fieldsubmit.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/ndex.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/next.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pageonecheckfive.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pageonecheckfour.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pageonecheckone.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pageonecheckthree.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pageonechecktwo.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pageonefieldfive.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pageonefieldfour.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pageonefieldone.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pageonefieldthree.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pageonefieldtwo.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pageonepopupfive.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pageonepopupfour.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pageonepopupone.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pageonepopupthree.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pageonepopuptwo.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pageoneradiofive.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pageoneradiofour.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pageoneradioone.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pageoneradiothree.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pageoneradiotwo.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagethreecheckfive.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagethreecheckfour.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagethreecheckone.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagethreecheckthree.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagethreechecktwo.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagethreefieldfive.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagethreefieldfour.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagethreefieldone.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagethreefieldthree.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagethreefieldtwo.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagethreepopupfive.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagethreepopupfour.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagethreepopupone.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagethreepopupthree.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagethreepopuptwo.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagethreeradiofive.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagethreeradiofour.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagethreeradioone.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagethreeradiothree.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagethreeradiotwo.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagetwocheckfive.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagetwocheckfour.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagetwocheckone.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagetwocheckthree.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagetwochecktwo.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagetwofieldfive.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagetwofieldfour.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagetwofieldone.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagetwofieldthree.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagetwofieldtwo.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagetwopopupfive.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagetwopopupfour.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagetwopopupone.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagetwopopupthree.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagetwopopuptwo.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagetworadiofive.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagetworadiofour.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagetworadioone.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagetworadiothree.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/pagetworadiotwo.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/popupclear.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/popupsubmit.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/prev.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/radioclear.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/radiosubmit.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/return.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/rightcheckcorrect.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/rightfieldcorrect.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/rightpopupcorrect.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/rightradiocorrect.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/wrongcheckcorrect.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/wrongfieldcorrect.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/wrongpopupcorrect.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/epsfiles/wrongradiocorrect.eps
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/samplefiles/check.pdf
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/samplefiles/check.tex
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/samplefiles/field.pdf
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/samplefiles/field.tex
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/samplefiles/ndex.pdf
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/samplefiles/ndex.tex
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/samplefiles/popup.pdf
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/samplefiles/popup.tex
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/samplefiles/radio.pdf
%{_texdir}/texmf-dist/doc/latex/interactiveworkbook/samplefiles/radio.tex


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
