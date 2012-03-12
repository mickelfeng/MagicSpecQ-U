%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/bgreek.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/bgreek.doc.tar.xz

Name: texlive-bgreek
License: LPPL
Summary: Using Beccari's fonts in betacode for classical Greek
Version: %{tl_version}
Release: %{tl_noarch_release}.0.3.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(bgreek.sty)
Provides: tex(ibygreek.sty)

%description
This package implements a dialect of the Beta Code encoding
(TLG and Perseus Projects) for typesetting classical Greek
using Claudio Beccari's Greek Fonts. The package provides
virtual fonts, to reference Beccari's fonts in bgreek mode, and
support macros for use with LaTeX.

date: 2009-02-21 22:05:10 +0100

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
Summary: Documentation for bgreek
Version: %{tl_version}
Release: %{tl_noarch_release}.0.3.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for bgreek


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
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmc0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmc0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmc0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmc0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmc0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmc1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmc1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmc1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmc1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmc1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmc2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmc2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmn0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmn0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmn0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmn0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmn0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmn1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmn1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmn1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmn1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmn1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmn2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmn2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmo0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmo0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmo0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmo0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmo0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmo1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmo1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmo1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmo1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmo1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmo2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgmo2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxc0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxc0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxc0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxc0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxc0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxc1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxc1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxc1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxc1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxc1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxc2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxc2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxn0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxn0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxn0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxn0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxn0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxn1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxn1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxn1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxn1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxn1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxn2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxn2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxo0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxo0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxo0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxo0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxo0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxo1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxo1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxo1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxo1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxo1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxo2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bgxo2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmc0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmc0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmc0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmc0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmc0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmc1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmc1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmc1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmc1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmc1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmc2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmc2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmn0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmn0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmn0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmn0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmn0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmn1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmn1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmn1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmn1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmn1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmn2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmn2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmo0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmo0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmo0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmo0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmo0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmo1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmo1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmo1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmo1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmo1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmo2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqmo2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxc0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxc0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxc0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxc0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxc0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxc1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxc1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxc1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxc1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxc1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxc2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxc2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxn0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxn0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxn0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxn0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxn0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxn1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxn1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxn1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxn1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxn1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxn2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxn2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxo0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxo0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxo0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxo0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxo0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxo1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxo1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxo1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxo1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxo1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxo2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/bqxo2488.tfm
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmc0500.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmc0600.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmc0700.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmc0800.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmc0900.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmc1000.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmc1095.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmc1200.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmc1440.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmc1728.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmc2074.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmc2488.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmn0500.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmn0600.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmn0700.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmn0800.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmn0900.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmn1000.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmn1095.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmn1200.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmn1440.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmn1728.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmn2074.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmn2488.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmo0500.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmo0600.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmo0700.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmo0800.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmo0900.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmo1000.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmo1095.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmo1200.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmo1440.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmo1728.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmo2074.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgmo2488.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxc0500.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxc0600.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxc0700.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxc0800.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxc0900.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxc1000.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxc1095.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxc1200.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxc1440.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxc1728.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxc2074.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxc2488.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxn0500.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxn0600.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxn0700.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxn0800.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxn0900.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxn1000.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxn1095.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxn1200.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxn1440.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxn1728.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxn2074.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxn2488.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxo0500.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxo0600.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxo0700.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxo0800.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxo0900.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxo1000.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxo1095.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxo1200.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxo1440.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxo1728.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxo2074.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bgxo2488.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmc0500.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmc0600.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmc0700.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmc0800.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmc0900.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmc1000.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmc1095.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmc1200.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmc1440.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmc1728.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmc2074.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmc2488.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmn0500.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmn0600.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmn0700.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmn0800.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmn0900.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmn1000.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmn1095.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmn1200.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmn1440.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmn1728.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmn2074.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmn2488.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmo0500.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmo0600.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmo0700.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmo0800.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmo0900.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmo1000.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmo1095.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmo1200.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmo1440.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmo1728.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmo2074.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqmo2488.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxc0500.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxc0600.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxc0700.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxc0800.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxc0900.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxc1000.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxc1095.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxc1200.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxc1440.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxc1728.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxc2074.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxc2488.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxn0500.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxn0600.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxn0700.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxn0800.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxn0900.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxn1000.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxn1095.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxn1200.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxn1440.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxn1728.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxn2074.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxn2488.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxo0500.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxo0600.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxo0700.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxo0800.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxo0900.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxo1000.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxo1095.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxo1200.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxo1440.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxo1728.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxo2074.vf
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/bqxo2488.vf
%{_texdir}/texmf-dist/tex/latex/bgreek/bcgcmr.fd
%{_texdir}/texmf-dist/tex/latex/bgreek/bcgenc.def
%{_texdir}/texmf-dist/tex/latex/bgreek/bcglmr.fd
%{_texdir}/texmf-dist/tex/latex/bgreek/bcqcmr.fd
%{_texdir}/texmf-dist/tex/latex/bgreek/bcqenc.def
%{_texdir}/texmf-dist/tex/latex/bgreek/bcqlmr.fd
%{_texdir}/texmf-dist/tex/latex/bgreek/bgfonts.tex
%{_texdir}/texmf-dist/tex/latex/bgreek/bgreek.ldf
%{_texdir}/texmf-dist/tex/latex/bgreek/bgreek.sty
%{_texdir}/texmf-dist/tex/latex/bgreek/ibygreek.ldf

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/bgreek/MANIFEST.TXT
%{_texdir}/texmf-dist/doc/latex/bgreek/README
%{_texdir}/texmf-dist/doc/latex/bgreek/bgman.pdf
%{_texdir}/texmf-dist/doc/latex/bgreek/bgman.tex
%{_texdir}/texmf-dist/doc/latex/bgreek/bgreek.etx
%{_texdir}/texmf-dist/doc/latex/bgreek/cbgreek.etx
%{_texdir}/texmf-dist/doc/latex/bgreek/qbgreek.etx


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
