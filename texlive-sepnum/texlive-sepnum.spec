# revision 20186
# category Package
# catalog-ctan /macros/latex/contrib/sepnum
# catalog-date 2010-10-24 14:34:20 +0200
# catalog-license lppl
# catalog-version 2.0

%{!?_texdir: %global _texdir %{_datadir}/texlive}
%define _texmfdistdir %{_texdir}/texmf-dist

Name:		texlive-sepnum
Version:	2011
Release:	2%{?dist}
Summary:	Print numbers in a "friendly" format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sepnum
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sepnum.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sepnum.doc.tar.xz
BuildArch:	noarch

%description
Provides a command to print a number with (potentially
different) separators every three digits in the parts either
side of the decimal point (the point itself is also
configurable). The macro is fully expandable and not fragile
(unless one of the separators is). There is also a command
\sepnumform, that may be used when defining \the<counter>
macros.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sepnum/sepnum.sty
%doc %{_texmfdistdir}/doc/latex/sepnum/sepnum-doc.pdf
%doc %{_texmfdistdir}/doc/latex/sepnum/sepnum-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.0-2
+ Revision: 755908
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.0-1
+ Revision: 719506
- texlive-sepnum
- texlive-sepnum
- texlive-sepnum
- texlive-sepnum

