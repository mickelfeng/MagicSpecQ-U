%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/oldlatin.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/oldlatin.doc.tar.xz

Name: texlive-oldlatin
License: LPPL
Summary: Compute Modern like font with long s
Version: %{tl_version}
Release: %{tl_noarch_release}.1.00.svn17932%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}

%description
Metafont sources modified from Computer Modern in order to
generate "long s" which was used in old text.

date: 2010-04-29 07:59:03 +0200

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
Summary: Documentation for oldlatin
Version: %{tl_version}
Release: %{tl_noarch_release}.1.00.svn17932%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for oldlatin


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
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olb10.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olbx10.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olbx12.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olbx5.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olbx6.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olbx7.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olbx8.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olbx9.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olbxsl10.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/oldunh10.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olff10.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olfib8.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olr10.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olr10s.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olr12.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olr17.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olr5.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olr6.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olr7.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olr8.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olr9.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olsl10.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olsl12.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olsl8.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olsl9.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olsltt10.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olss10.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olss12.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olss17.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olss8.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olss9.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olssbx10.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olssdc10.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olssi10.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olssi12.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olssi17.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olssi8.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olssi9.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olssq8.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olssqi8.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/oltt10.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/oltt12.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/oltt8.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/oltt9.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/olvtt10.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/oroman.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/oromanl.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/oromlig.mf
%{_texdir}/texmf-dist/fonts/source/public/oldlatin/oromligs.mf
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olbx12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olbx5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olbx6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olbx7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olbx8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olbx9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olbxsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/oldunh10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olff10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olfib8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olr12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olr17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olr5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olr6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olr7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olr8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olr9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olsl12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olsl8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olsl9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olsltt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olss10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olss12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olss17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olss8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olss9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olssbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olssdc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olssi10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olssi12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olssi17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olssi8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olssi9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olssq8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olssqi8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/oltt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/oltt12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/oltt8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/oltt9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/oldlatin/olvtt10.tfm

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/fonts/oldlatin/README
%{_texdir}/texmf-dist/doc/fonts/oldlatin/oldlatin.pdf
%{_texdir}/texmf-dist/doc/fonts/oldlatin/oldlatin.tex
%{_texdir}/texmf-dist/doc/fonts/oldlatin/test_alphabet.tex
%{_texdir}/texmf-dist/doc/fonts/oldlatin/test_ol_all.pdf
%{_texdir}/texmf-dist/doc/fonts/oldlatin/test_ol_all.tex
%{_texdir}/texmf-dist/doc/fonts/oldlatin/test_ol_bf.pdf
%{_texdir}/texmf-dist/doc/fonts/oldlatin/test_ol_bf.tex
%{_texdir}/texmf-dist/doc/fonts/oldlatin/test_ol_rm.pdf
%{_texdir}/texmf-dist/doc/fonts/oldlatin/test_ol_rm.tex
%{_texdir}/texmf-dist/doc/fonts/oldlatin/test_ol_sl.pdf
%{_texdir}/texmf-dist/doc/fonts/oldlatin/test_ol_sl.tex
%{_texdir}/texmf-dist/doc/fonts/oldlatin/test_ol_ss.pdf
%{_texdir}/texmf-dist/doc/fonts/oldlatin/test_ol_ss.tex
%{_texdir}/texmf-dist/doc/fonts/oldlatin/test_ol_tt.pdf
%{_texdir}/texmf-dist/doc/fonts/oldlatin/test_ol_tt.tex


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
