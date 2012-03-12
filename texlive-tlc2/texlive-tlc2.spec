%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/tlc2.doc.tar.xz

Name: texlive-tlc2-doc
License: LPPL
Summary: Documentation for tlc2
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description
Documentation for tlc2


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/lppl.txt lppl.txt
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
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/tlc2/1-3-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/1-3-2.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/1-3-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/1-3-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/1-3-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-14.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-15.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-16.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-17.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-18.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-19.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-20.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-21.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-22.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-23.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-24.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-25.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-26.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-27.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-1-9.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/10-2-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-2-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-2-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-2-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-2-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-2-14.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-2-15.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-2-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-2-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-2-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-2-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-2-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-2-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-2-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-2-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-3-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-3-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-3-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-3-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-3-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-3-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-3-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-3-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-3-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-3-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-3-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-3-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-4-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-4-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-4-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/10-4-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-1-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-1-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-1-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-2-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-2-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-2-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-2-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-2-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-2-14.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-2-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-2-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-2-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-2-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-2-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-2-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-2-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-2-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-14.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-15.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-16.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-17.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-18.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-19.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-20.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-21.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-22.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-23.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-24.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-25.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-26.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-27.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-3-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-4-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-4-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-4-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-4-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-4-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-4-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-4-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-4-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-14.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-15.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-16.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-17.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-18.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-19.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-20.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-21.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-22.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-23.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-24.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-25.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-26.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-27.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-28.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-29.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-30.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-31.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-32.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-33.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-34.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-35.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-36.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-37.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-38.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-39.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-40.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-41.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-42.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-43.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-44.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-45.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-46.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-47.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-48.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-49.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-5-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-6-1.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/12-6-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-6-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-6-3.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/12-6-4.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/12-6-5.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/12-6-6.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/12-6-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-6-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/12-6-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/13-4-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/13-4-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/13-5-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/13-5-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/13-5-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/13-5-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/13-5-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/13-5-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/13-5-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/14-4-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/14-4-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-1-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-2-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-2-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-2-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-2-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-2-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-2-14.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-2-15.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-2-16.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-2-17.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-2-18.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-2-19.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-2-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-2-20.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-2-21.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/2-2-22.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-2-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-2-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-2-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-2-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-2-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-2-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-2-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-3-1.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/2-3-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-3-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-3-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-3-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-3-14.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-3-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-3-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-3-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-3-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-3-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-3-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-3-8.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/2-3-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-4-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-4-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-4-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-4-4.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/2-4-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-4-6.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/2-4-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-4-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/2-4-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-14.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-15.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-16.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-17.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-18.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-19.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-20.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-21.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-22.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-23.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-24.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-25.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-26.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-27.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-28.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-29.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-30.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-31.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-32.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-33.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-34.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-35.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-36.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-37.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-38.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-39.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-40.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-41.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-42.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-43.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-44.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-45.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-46.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-47.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-48.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-49.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-50.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-51.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-52.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-53.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-1-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-14.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-15.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-16.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-17.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-18.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-19.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-20.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-21.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-22.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-23.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-24.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-25.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-26.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-27.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-28.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-7.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-2-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-14.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-15.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-16.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-17.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-18.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-19.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-20.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-21.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-22.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-23.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-24.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-25.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-26.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-27.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-28.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-29.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-30.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-3-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-14.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-15.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-16.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-17.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-18.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-19.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-20.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-21.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-22.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-23.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-24.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-25.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-26.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-27.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-28.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-29.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-30.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-31.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-32.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-33.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-34.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-35.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-36.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-37.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-38.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-39.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-40.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-41.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-42.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-4-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-5-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-5-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-5-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-5-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-5-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-5-14.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-5-15.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-5-16.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-5-17.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-5-18.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-5-19.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-5-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-5-20.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-5-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-5-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-5-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-5-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-5-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-5-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/3-5-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/4-1-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/4-2-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/4-2-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/4-2-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/4-2-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/4-2-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/4-2-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/4-2-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/4-2-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/4-2-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/4-2-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/4-2-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/4-2-8.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/4-2-9.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/4-3-1.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/4-3-2.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/4-3-3.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/4-4-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/4-4-10.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/4-4-11.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/4-4-12.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/4-4-13.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/4-4-14.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/4-4-15.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/4-4-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/4-4-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/4-4-4.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/4-4-5.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/4-4-6.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/4-4-7.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/4-4-8.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/4-4-9.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/4-5-1.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/4-5-2.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/5-1-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-1-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-1-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-1-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-2-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-2-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-2-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-2-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-2-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-2-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-2-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-2-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-2-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-2-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-2-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-2-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-2-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-3-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-3-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-3-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-3-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-3-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-3-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-4-1.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/5-4-2.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/5-4-3.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/5-4-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-4-5.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/5-4-6.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/5-5-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-5-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-6-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-6-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-6-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-6-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-6-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-6-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-6-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-6-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-7-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-7-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-7-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-7-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-7-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-7-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-7-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-7-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-8-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-8-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-9-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-9-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-9-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-9-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-9-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/5-9-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-3-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-3-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-3-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-3-4.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/6-3-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-3-6.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/6-3-7.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/6-4-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-4-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-4-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-4-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-4-5.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/6-4-6.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/6-4-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-4-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-5-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-5-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-5-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-5-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-5-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-5-14.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/6-5-15.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-5-16.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-5-17.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-5-18.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/6-5-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-5-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-5-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-5-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-5-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-5-7.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/6-5-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/6-5-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-10-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-12-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-3-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-3-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-3-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-3-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-3-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-3-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-3-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-3-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-4-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-4-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-4-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-4-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-4-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-5-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-5-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-5-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-5-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-5-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-5-14.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-5-15.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-5-16.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-5-17.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-5-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-5-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-5-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-5-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-5-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-5-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-5-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-5-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-6-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-6-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-6-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-6-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-6-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-6-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-6-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-6-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-6-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-6-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-6-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-6-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-14.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-15.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-16.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-17.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-18.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-19.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-20.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-21.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-22.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-23.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-24.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-25.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-26.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-27.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-28.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-29.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-7-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-8-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-8-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-8-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-8-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-8-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-8-14.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-8-15.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-8-16.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-8-17.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-8-18.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-8-19.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-8-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-8-20.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-8-21.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-8-22.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-8-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-8-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-8-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-8-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-8-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-8-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-8-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-9-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/7-9-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-14.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-15.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-16.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-17.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-18.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-19.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-20.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-21.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-22.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-23.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-24.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-25.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-26.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-27.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-28.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-29.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-2-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-14.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-15.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-16.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-17.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-18.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-19.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-20.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-21.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-22.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-23.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-24.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-25.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-26.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-27.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-28.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-29.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-30.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-31.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-32.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-33.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-34.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-35.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-36.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-37.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-38.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-39.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-3-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-4-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-4-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-4-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-4-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-4-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-4-14.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-4-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-4-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-4-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-4-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-4-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-4-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-4-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-4-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-5-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-5-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-5-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-5-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-6-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-6-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-6-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-6-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-7-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-7-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-7-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-7-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-7-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-7-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-7-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-14.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-15.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-16.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-17.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-18.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-19.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-20.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-21.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-22.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-23.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-24.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-25.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-8-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-9-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-9-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-9-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-9-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-9-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-9-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-9-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/8-9-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-2-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-2-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-2-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-2-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-2-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-2-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-2-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-2-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-14.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-15.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-16.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-17.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-18.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-19.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-20.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-21.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-22.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-23.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-24.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-25.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-26.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-27.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-28.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-29.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-30.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-31.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-32.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-33.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-34.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-35.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-36.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-37.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-38.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-39.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-3-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-4-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-4-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-4-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-4-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-4-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/9-5-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-1-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-1-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-1-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-1-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-1-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-1-14.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-1-15.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-1-16.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-1-17.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-1-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-1-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-1-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-1-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-1-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-1-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-1-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-1-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-2-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-2-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-2-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-2-12.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-2-13.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-2-14.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-2-15.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-2-16.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-2-17.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-2-18.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-2-19.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-2-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-2-20.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-2-21.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-2-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-2-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-2-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-2-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-2-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-2-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-2-9.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-3-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-3-10.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-3-11.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-3-2.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-3-3.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-3-4.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-3-5.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-3-6.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-3-7.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-3-8.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/A-3-9.ltx2
%{_texdir}/texmf-dist/doc/latex/tlc2/B-3-1.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/Escher.ps
%{_texdir}/texmf-dist/doc/latex/tlc2/cat.ps
%{_texdir}/texmf-dist/doc/latex/tlc2/companion.ctan
%{_texdir}/texmf-dist/doc/latex/tlc2/elephant.ps
%{_texdir}/texmf-dist/doc/latex/tlc2/indexexa.ltx
%{_texdir}/texmf-dist/doc/latex/tlc2/jura.bib
%{_texdir}/texmf-dist/doc/latex/tlc2/partial.toc
%{_texdir}/texmf-dist/doc/latex/tlc2/rosette.ps
%{_texdir}/texmf-dist/doc/latex/tlc2/tex.bib
%{_texdir}/texmf-dist/doc/latex/tlc2/ttctexa.cls
%{_texdir}/texmf-dist/doc/latex/tlc2/ttctexamargin.cls
%{_texdir}/texmf-dist/doc/latex/tlc2/ttctexareport.cls
%{_texdir}/texmf-dist/doc/latex/tlc2/w.eps
%{_texdir}/texmf-dist/doc/latex/tlc2/w.ps


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
