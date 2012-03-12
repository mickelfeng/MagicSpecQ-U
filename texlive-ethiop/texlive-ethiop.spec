%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/ethiop.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/ethiop.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/ethiop.source.tar.xz

Name: texlive-ethiop
License: GPL+
Summary: LaTeX macros and fonts for typesetting Amharic
Version: %{tl_version}
Release: %{tl_noarch_release}.0.7.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(etharab.sty)
Provides: tex(ethiop.sty)

%description
Ethiopian language support for the babel package, including a
collection of fonts and TeX macros for typesetting the
characters of the languages of Ethiopia, with MetaFont fonts
based on EthTeX's.

date: 2007-02-14 08:57:40 +0100

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
Summary: Documentation for ethiop
Version: %{tl_version}
Release: %{tl_noarch_release}.0.7.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for ethiop


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/gpl.txt gpl.txt
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
%doc gpl.txt
%{_texdir}/texmf-dist/fonts/ofm/public/ethiop/etho10.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/ethiop/ethob10.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/ethiop/ethos10.ofm
%{_texdir}/texmf-dist/fonts/ofm/public/ethiop/ethosb10.ofm
%{_texdir}/texmf-dist/fonts/ovf/public/ethiop/etho10.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/ethiop/ethob10.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/ethiop/ethos10.ovf
%{_texdir}/texmf-dist/fonts/ovf/public/ethiop/ethosb10.ovf
%{_texdir}/texmf-dist/fonts/ovp/public/ethiop/etho10.ovp
%{_texdir}/texmf-dist/fonts/ovp/public/ethiop/ethob10.ovp
%{_texdir}/texmf-dist/fonts/ovp/public/ethiop/ethos10.ovp
%{_texdir}/texmf-dist/fonts/ovp/public/ethiop/ethosb10.ovp
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth__a.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth__g.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_acce.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_b.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_c_c.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_cc.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_cc_c.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_ccc2.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_d.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_dd.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_f.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_fu.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_g.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_g_a.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_gg.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_ggu.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_gu.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_h.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_h_a.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_h_c.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_hh.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_hu_c.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_j.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_k.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_k_a.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_kk.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_kku.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_ku.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_l.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_m.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_mrf.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_mu.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_n.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_nn.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_num.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_p.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_pp.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_pu.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_punc.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_q.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_q_a.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_qq.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_qqu.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_qu.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_r.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_s.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_s_a.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_s_c.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_ss.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_t.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_tt.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_v.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_w.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_wu.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_y.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_z.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/eth_z_c.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/etha10.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/etha6.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/etha7.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/etha8.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/etha_cod.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/etha_drv.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/etha_lig.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethab10.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethab11.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethab12.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethab14.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethab18.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethab24.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethab36.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethab9.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethas10.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethasb10.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethasb11.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethasb12.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethasb14.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethasb18.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethasb24.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethasb36.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethasb9.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethatt10.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethb10.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethb6.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethb7.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethb8.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethb_cod.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethb_drv.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethb_lig.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethbb10.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethbb11.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethbb12.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethbb14.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethbb18.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethbb24.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethbb36.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethbb9.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethbs10.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethbsb10.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethbsb11.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethbsb12.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethbsb14.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethbsb18.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethbsb24.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethbsb36.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethbsb9.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethbtt10.mf
%{_texdir}/texmf-dist/fonts/source/public/ethiop/ethiomac.mf
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/etha10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/etha6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/etha7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/etha8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethab10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethab11.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethab12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethab14.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethab18.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethab24.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethab36.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethab9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethas10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethasb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethasb11.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethasb12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethasb14.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethasb18.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethasb24.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethasb36.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethasb9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethatt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethb6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethb7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethb8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethbb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethbb11.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethbb12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethbb14.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethbb18.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethbb24.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethbb36.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethbb9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethbs10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethbsb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethbsb11.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethbsb12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethbsb14.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethbsb18.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethbsb24.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethbsb36.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethbsb9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/ethbtt10.tfm
%{_texdir}/texmf-dist/omega/ocp/ethiop/ethospc.ocp
%{_texdir}/texmf-dist/omega/otp/ethiop/ethospc.otp
%{_texdir}/texmf-dist/tex/latex/ethiop/etharab.sty
%{_texdir}/texmf-dist/tex/latex/ethiop/ethiop.ldf
%{_texdir}/texmf-dist/tex/latex/ethiop/ethiop.sty
%{_texdir}/texmf-dist/tex/latex/ethiop/uetha.fd
%{_texdir}/texmf-dist/tex/latex/ethiop/uethb.fd
%{_texdir}/texmf-dist/tex/latex/ethiop/uetho.fd

%files doc
%defattr(-,root,root)
%doc gpl.txt
%{_texdir}/texmf-dist/doc/latex/ethiop/MANIFEST
%{_texdir}/texmf-dist/doc/latex/ethiop/README
%{_texdir}/texmf-dist/doc/latex/ethiop/codeetha.tex
%{_texdir}/texmf-dist/doc/latex/ethiop/codeethb.tex
%{_texdir}/texmf-dist/doc/latex/ethiop/ethiodoc.pdf
%{_texdir}/texmf-dist/doc/latex/ethiop/ethiodoc.tex


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
