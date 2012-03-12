%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/lfb.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/lfb.doc.tar.xz

Name: texlive-lfb
License: LPPL
Summary: A Greek font with normal and bold variants
Version: %{tl_version}
Release: %{tl_noarch_release}.1.0.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}

%description
This is a Greek font written in MetaFont, with inspiration from
the Bodoni typefaces in old books. It is stylistically a little
more exotic than the standard textbook Greek fonts,
particularly in glyphs like the lowercase rho and kappa. It
aims for a rather calligraphic feel, but seems to blend well
with Computer Modern. There is a ligature scheme which
automatically inserts the breathings required for ancient
texts, making the input text more readable than in some
schemes.

date: 2006-10-18 08:58:01 +0200

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
Summary: Documentation for lfb
Version: %{tl_version}
Release: %{tl_noarch_release}.1.0.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for lfb


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
%{_texdir}/texmf-dist/fonts/source/public/lfb/accents.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/alpha.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/beta.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/capitals.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/charmap.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/delta.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/epsilon.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/eta.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/gamma.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/iota.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/kappa.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/khi.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/lambda.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/lfb.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/lfb10.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/lfb11.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/lfb12.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/lfb5.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/lfb6.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/lfb7.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/lfb8.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/lfb9.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/lfbb10.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/lfbb11.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/lfbb12.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/lfbb5.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/lfbb6.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/lfbb7.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/lfbb8.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/lfbb9.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/ligature.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/mu.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/nu.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/omega.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/omikron.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/others.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/phi.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/pi.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/psi.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/rho.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/serifs.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/sigma.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/sigmafin.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/tau.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/theta.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/upsilon.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/xi.mf
%{_texdir}/texmf-dist/fonts/source/public/lfb/zeta.mf
%{_texdir}/texmf-dist/fonts/tfm/public/lfb/lfb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lfb/lfb11.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lfb/lfb12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lfb/lfb5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lfb/lfb6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lfb/lfb7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lfb/lfb8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lfb/lfb9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lfb/lfbb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lfb/lfbb11.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lfb/lfbb12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lfb/lfbb5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lfb/lfbb6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lfb/lfbb7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lfb/lfbb8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/lfb/lfbb9.tfm

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/fonts/lfb/README
%{_texdir}/texmf-dist/doc/fonts/lfb/example.pdf
%{_texdir}/texmf-dist/doc/fonts/lfb/example.tex
%{_texdir}/texmf-dist/doc/fonts/lfb/lfb.make
%{_texdir}/texmf-dist/doc/fonts/lfb/lfbacc.tex


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
