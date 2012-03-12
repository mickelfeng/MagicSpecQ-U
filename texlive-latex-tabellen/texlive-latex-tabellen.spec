%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/latex-tabellen.doc.tar.xz

Name: texlive-latex-tabellen-doc
License: LPPL
Summary: Documentation for latex-tabellen
Version: %{tl_version}
Release: %{tl_noarch_release}.svn16979%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description
Documentation for latex-tabellen


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
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-01-1.ltxps
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-01-10.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-01-11.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-01-12.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-01-13.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-01-14.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-01-15.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-01-16.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-01-17.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-01-18.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-01-19.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-01-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-01-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-01-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-01-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-01-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-01-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-01-8.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-01-9.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-02-1.ltxps
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-02-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-02-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-02-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-02-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-02-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-02-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-02-8.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/01-02-9.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-01-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-01-10.ltxps
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-01-11.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-01-12.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-01-13.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-01-14.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-01-15.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-01-16.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-01-17.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-01-18.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-01-19.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-01-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-01-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-01-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-01-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-01-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-01-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-01-8.ltxps
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-01-9.ltxps
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-02-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-02-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-02-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-02-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-02-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-02-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-03-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-03-10.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-03-11.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-03-12.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-03-13.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-03-14.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-03-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-03-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-03-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-03-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-03-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-03-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-03-8.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-03-9.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-04-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-04-10.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-04-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-04-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-04-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-04-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-04-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-04-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-04-8.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-04-9.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-05-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-05-10.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-05-11.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-05-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-05-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-05-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-05-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-05-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-05-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-05-8.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-05-9.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-06-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-06-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-06-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-06-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-06-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-07-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-07-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-07-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-07-4.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-07-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-08-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-08-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-08-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-08-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-08-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-08-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-08-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-08-8.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-09-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-09-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-09-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-10-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-11-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-11-10.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-11-11.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-11-12.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-11-13.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-11-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-11-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-11-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-11-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-11-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-11-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-11-8.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-11-9.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-12-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-12-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-13-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-13-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-13-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-13-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-14-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-14-10.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-14-11.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-14-12.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-14-13.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-14-14.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-14-15.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-14-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-14-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-14-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-14-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-14-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-14-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-14-8.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-14-9.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-15-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-15-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-15-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-16-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-16-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-16-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-17-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-18-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-18-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-18-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-18-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-18-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-19-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-19-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-20-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-20-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-21-1.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-21-2.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-22-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-22-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-22-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-22-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-23-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-24-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-24-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-24-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-24-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-25-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-25-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-26-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-26-10.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-26-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-26-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-26-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-26-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-26-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-26-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-26-8.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-26-9.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-27-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-28-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-28-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-28-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-28-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-29-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/02-29-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-01-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-01-10.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-01-11.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-01-12.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-01-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-01-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-01-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-01-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-01-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-01-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-01-8.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-01-9.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-02-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-02-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-02-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-02-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-02-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-02-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-02-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-03-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-03-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-03-3.ltxb
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-03-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-03-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/03-03-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-01-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-01-10.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-01-11.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-01-12.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-01-13.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-01-14.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-01-15.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-01-2.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-01-3.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-01-4.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-01-5.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-01-6.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-01-7.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-01-8.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-01-9.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-02-1.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-02-2.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-03-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-03-2.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-03-3.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-04-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-04-2.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-04-3.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-04-4.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-04-5.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-05-1.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-05-2.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-05-3.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-05-4.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-05-5.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-05-6.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-05-7.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-05-8.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-06-1.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-06-2.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-06-3.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-06-4.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-06-5.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-06-6.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-06-7.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-06-8.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/04-06-9.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/05-01-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/05-01-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/05-01-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/05-01-4.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/05-01-5.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/05-02-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/05-03-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/05-03-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/05-03-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/05-04-1.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/05-04-2.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/05-05-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/05-05-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/05-06-1.ltxE
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/05-06-2.ltxE
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/05-06-3.ltxE
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-1.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-10.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-11.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-12.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-13.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-14.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-15.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-16.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-17.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-18.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-19.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-2.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-20.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-21.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-22.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-23.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-24.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-25.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-26.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-27.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-28.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-29.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-3.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-30.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-31.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-32.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-33.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-34.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-35.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-36.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-37.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-38.ltxps
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-39.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-4.ltxps
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-40.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-41.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-42.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-43.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-44.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-45.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-46.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-5.ltxps
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-6.ltxps
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-7.ltxps
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-8.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/06-00-9.ltx
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/07-03-1.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/07-03-2.ltx2
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/README


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
