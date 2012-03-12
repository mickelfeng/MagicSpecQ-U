%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/hyphen-indic.tar.xz

Name: texlive-hyphen-indic
License: LPPL
Summary: hyphen-indic package
Version: %{tl_version}
Release: %{tl_noarch_release}.svn18673%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires: texlive-hyphen-base = %{tl_version}
Requires: texlive-hyph-utf8 = %{tl_version}

%description
hyphen-indic package

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "assamese loadhyph-as.tex" >> %{_texdir}/texmf/tex/generic/config/language.dat
echo "\addlanguage{assamese}{loadhyph-as.tex}{}{1}{1}" >> %{_texdir}/texmf/tex/generic/config/language.def
echo "bengali loadhyph-bn.tex" >> %{_texdir}/texmf/tex/generic/config/language.dat
echo "\addlanguage{bengali}{loadhyph-bn.tex}{}{1}{1}" >> %{_texdir}/texmf/tex/generic/config/language.def
echo "gujarati loadhyph-gu.tex" >> %{_texdir}/texmf/tex/generic/config/language.dat
echo "\addlanguage{gujarati}{loadhyph-gu.tex}{}{1}{1}" >> %{_texdir}/texmf/tex/generic/config/language.def
echo "hindi loadhyph-hi.tex" >> %{_texdir}/texmf/tex/generic/config/language.dat
echo "\addlanguage{hindi}{loadhyph-hi.tex}{}{1}{1}" >> %{_texdir}/texmf/tex/generic/config/language.def
echo "kannada loadhyph-kn.tex" >> %{_texdir}/texmf/tex/generic/config/language.dat
echo "\addlanguage{kannada}{loadhyph-kn.tex}{}{1}{1}" >> %{_texdir}/texmf/tex/generic/config/language.def
echo "malayalam loadhyph-ml.tex" >> %{_texdir}/texmf/tex/generic/config/language.dat
echo "\addlanguage{malayalam}{loadhyph-ml.tex}{}{1}{1}" >> %{_texdir}/texmf/tex/generic/config/language.def
echo "marathi loadhyph-mr.tex" >> %{_texdir}/texmf/tex/generic/config/language.dat
echo "\addlanguage{marathi}{loadhyph-mr.tex}{}{1}{1}" >> %{_texdir}/texmf/tex/generic/config/language.def
echo "oriya loadhyph-or.tex" >> %{_texdir}/texmf/tex/generic/config/language.dat
echo "\addlanguage{oriya}{loadhyph-or.tex}{}{1}{1}" >> %{_texdir}/texmf/tex/generic/config/language.def
echo "panjabi loadhyph-pa.tex" >> %{_texdir}/texmf/tex/generic/config/language.dat
echo "\addlanguage{panjabi}{loadhyph-pa.tex}{}{1}{1}" >> %{_texdir}/texmf/tex/generic/config/language.def
echo "tamil loadhyph-ta.tex" >> %{_texdir}/texmf/tex/generic/config/language.dat
echo "\addlanguage{tamil}{loadhyph-ta.tex}{}{1}{1}" >> %{_texdir}/texmf/tex/generic/config/language.def
echo "telugu loadhyph-te.tex" >> %{_texdir}/texmf/tex/generic/config/language.dat
echo "\addlanguage{telugu}{loadhyph-te.tex}{}{1}{1}" >> %{_texdir}/texmf/tex/generic/config/language.def
touch /var/run/texlive/run-fmtutil
:

%postun
if [ $1 == 0 ]; then
  sed -i '/assamese loadhyph-as.tex/d' %{_texdir}/texmf/tex/generic/config/language.dat
  sed -i '/\\addlanguage{assamese}{loadhyph-as.tex}{}{1}{1}/d' %{_texdir}/texmf/tex/generic/config/language.def
  sed -i '/bengali loadhyph-bn.tex/d' %{_texdir}/texmf/tex/generic/config/language.dat
  sed -i '/\\addlanguage{bengali}{loadhyph-bn.tex}{}{1}{1}/d' %{_texdir}/texmf/tex/generic/config/language.def
  sed -i '/gujarati loadhyph-gu.tex/d' %{_texdir}/texmf/tex/generic/config/language.dat
  sed -i '/\\addlanguage{gujarati}{loadhyph-gu.tex}{}{1}{1}/d' %{_texdir}/texmf/tex/generic/config/language.def
  sed -i '/hindi loadhyph-hi.tex/d' %{_texdir}/texmf/tex/generic/config/language.dat
  sed -i '/\\addlanguage{hindi}{loadhyph-hi.tex}{}{1}{1}/d' %{_texdir}/texmf/tex/generic/config/language.def
  sed -i '/kannada loadhyph-kn.tex/d' %{_texdir}/texmf/tex/generic/config/language.dat
  sed -i '/\\addlanguage{kannada}{loadhyph-kn.tex}{}{1}{1}/d' %{_texdir}/texmf/tex/generic/config/language.def
  sed -i '/malayalam loadhyph-ml.tex/d' %{_texdir}/texmf/tex/generic/config/language.dat
  sed -i '/\\addlanguage{malayalam}{loadhyph-ml.tex}{}{1}{1}/d' %{_texdir}/texmf/tex/generic/config/language.def
  sed -i '/marathi loadhyph-mr.tex/d' %{_texdir}/texmf/tex/generic/config/language.dat
  sed -i '/\\addlanguage{marathi}{loadhyph-mr.tex}{}{1}{1}/d' %{_texdir}/texmf/tex/generic/config/language.def
  sed -i '/oriya loadhyph-or.tex/d' %{_texdir}/texmf/tex/generic/config/language.dat
  sed -i '/\\addlanguage{oriya}{loadhyph-or.tex}{}{1}{1}/d' %{_texdir}/texmf/tex/generic/config/language.def
  sed -i '/panjabi loadhyph-pa.tex/d' %{_texdir}/texmf/tex/generic/config/language.dat
  sed -i '/\\addlanguage{panjabi}{loadhyph-pa.tex}{}{1}{1}/d' %{_texdir}/texmf/tex/generic/config/language.def
  sed -i '/tamil loadhyph-ta.tex/d' %{_texdir}/texmf/tex/generic/config/language.dat
  sed -i '/\\addlanguage{tamil}{loadhyph-ta.tex}{}{1}{1}/d' %{_texdir}/texmf/tex/generic/config/language.def
  sed -i '/telugu loadhyph-te.tex/d' %{_texdir}/texmf/tex/generic/config/language.dat
  sed -i '/\\addlanguage{telugu}{loadhyph-te.tex}{}{1}{1}/d' %{_texdir}/texmf/tex/generic/config/language.def
  %{_bindir}/texhash 2> /dev/null
  %{_bindir}/fmtutil-sys --missing &> /dev/null
else
  mkdir -p /var/run/texlive
  touch /var/run/texlive/run-texhash
  touch /var/run/texlive/run-fmtutil
fi
:

%posttrans
[ -e /var/run/texlive/run-texhash ] && %{_bindir}/texhash 2> /dev/null && rm -f /var/run/texlive/run-texhash
[ -e /var/run/texlive/run-fmtutil ] && %{_bindir}/fmtutil-sys --missing &> /dev/null && rm -f /var/run/texlive/run-fmtutil
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
