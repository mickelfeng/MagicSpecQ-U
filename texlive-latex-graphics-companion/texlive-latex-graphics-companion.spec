%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/latex-graphics-companion.doc.tar.xz

Name: texlive-latex-graphics-companion-doc
License: LPPL
Summary: Documentation for latex-graphics-companion
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description
Documentation for latex-graphics-companion


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
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/1-4-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/1-4-10.pic
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/1-4-11.pic
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/1-4-12.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/1-4-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/1-4-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/1-4-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/1-4-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/1-4-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/1-4-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/1-4-8.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/1-4-9.pic
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/10-1-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/10-1-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/10-1-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/10-1-4.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/10-1-5.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/10-5-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/11-3-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/11-6-1.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/12-0-1.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/12-0-10.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/12-0-11.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/12-0-12.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/12-0-2.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/12-0-3.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/12-0-4.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/12-0-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/12-0-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/12-0-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/12-0-8.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/12-0-9.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-2-1.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-2-10.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-2-11.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-2-12.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-2-13.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-2-14.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-2-15.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-2-16.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-2-17.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-2-18.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-2-19.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-2-2.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-2-20.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-2-3.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-2-4.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-2-5.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-2-6.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-2-7.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-2-8.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-2-9.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-3-1.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-3-10.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-3-11.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-3-12.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-3-13.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-3-14.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-3-15.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-3-16.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-3-17.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-3-2.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-3-3.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-3-4.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-3-5.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-3-6.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-3-7.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-3-8.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/2-3-9.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-1-1.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-1-2.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-1-3.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-1-4.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-1-5.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-1-6.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-1-7.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-1-8.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-1-9.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-2-1.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-2-2.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-2-3.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-3-1.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-3-10.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-3-11.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-3-12.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-3-13.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-3-14.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-3-15.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-3-16.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-3-17.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-3-18.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-3-19.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-3-2.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-3-3.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-3-4.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-3-5.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-3-6.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-3-7.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-3-8.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-3-9.mp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-4-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-4-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-4-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-4-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-4-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/3-4-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-10-1.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-10-10.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-10-11.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-10-2.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-10-3.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-10-4.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-10-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-10-6.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-10-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-10-8.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-10-9.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-2-1.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-2-2.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-2-3.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-2-4.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-2-5.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-3-1.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-3-2.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-4-1.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-4-10.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-4-11.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-4-12.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-4-2.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-4-3.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-4-4.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-4-5.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-4-6.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-4-7.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-4-8.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-4-9.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-5-1.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-5-10.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-5-11.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-5-12.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-5-13.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-5-14.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-5-15.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-5-16.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-5-2.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-5-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-5-4.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-5-5.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-5-6.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-5-7.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-5-8.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-5-9.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-1.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-10.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-11.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-12.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-13.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-14.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-15.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-16.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-17.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-18.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-19.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-2.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-20.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-21.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-22.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-23.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-24.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-25.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-26.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-27.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-28.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-29.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-3.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-30.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-31.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-32.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-33.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-34.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-35.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-36.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-37.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-38.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-39.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-4.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-40.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-41.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-42.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-43.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-44.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-45.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-46.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-5.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-6.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-7.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-8.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-6-9.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-7-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-7-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-7-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-7-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-8-1.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-8-2.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-8-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-8-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-8-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-9-1.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-9-10.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/4-9-2.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-2-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-3-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-3-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-3-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-3-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-3-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-3-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-3-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-3-8.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-3-9.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-4-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-4-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-4-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-4-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-10.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-11.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-12.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-13.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-14.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-15.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-16.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-17.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-18.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-19.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-20.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-21.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-22.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-23.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-24.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-25.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-26.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-27.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-28.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-29.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-30.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-31.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-32.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-33.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-34.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-35.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-8.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/5-5-9.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-2-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-2-10.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-2-11.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-2-12.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-2-13.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-2-14.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-2-15.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-2-16.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-2-17.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-2-18.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-2-19.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-2-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-2-20.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-2-21.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-2-22.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-2-23.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-2-24.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-2-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-2-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-2-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-2-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-2-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-2-8.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-2-9.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-3-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-3-10.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-3-11.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-3-12.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-3-13.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-3-14.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-3-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-3-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-3-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-3-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-3-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-3-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-3-8.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-3-9.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-4-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-4-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-4-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-5-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-6-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-6-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-6-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-6-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-6-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-6-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-6-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-7-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-7-1.m4
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-7-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-7-2.m4
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-7-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-7-3.m4
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-7-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/6-7-4.m4
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-2-1.mx1
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-2-1.mx2
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-2-1.ptx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-2-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-2-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-2-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-2-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-2-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-3-1.abc
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-3-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-3-3.abc
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-3-4.abc
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-3-5.abc
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-3-6.abc
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-3-7.abc
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-3-8.abc
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-3-9.abc
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-4-1.mpp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-4-10.mx1
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-4-10.mx2
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-4-10.ptx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-4-2.mpp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-4-3.mpp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-4-4.mpp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-4-5.mpp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-4-6.mpp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-4-7.mpp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-4-8.mpp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/7-4-9.mpp
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-1-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-1-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-1-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-1-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-2-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-2-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-2-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-3-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-3-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-3-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-4-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-4-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-5-1.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-6-1.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-6-2.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-6-3.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-6-4.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-6-5.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-6-6.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-6-7.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-6-8.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-7-1.acr
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-7-1.dwn
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-7-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-7-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-7-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/8-7-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-2-1.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-2-2.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-2-3.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-2-4.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-2-5.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-2-6.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-2-7.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-2-8.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-2-9.ltx
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-3-1.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-3-10.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-3-11.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-3-12.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-3-13.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-3-14.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-3-15.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-3-16.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-3-17.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-3-18.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-3-19.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-3-2.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-3-20.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-3-3.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-3-4.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-3-5.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-3-6.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-3-7.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-3-8.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/9-3-9.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/A-1-1.inl
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/Makefile
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/README
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/ages.dat
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/bar.ini
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/chap.dat
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/clef.ini
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/config.ps.gz
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/decade.dat
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/feature.ini
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/graves.dat
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/key.ini
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/langs.dat
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/langs2.dat
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/langs3.dat
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/macro.ini
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/mpp.tex
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/note.ini
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/notecc.ini
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/pot.dat
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/script.ini
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/scriptcc.ini
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/stones.dat
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/students.dat
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/veracx.mx1
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/veracx.tex
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/yearm.dat
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/years.dat
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/years.men
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/years.wom
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/yearw.dat
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/inputs/graphics.cfg
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/inputs/header.tex
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/inputs/mfpic.sty
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/inputs/ppex.cls


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
