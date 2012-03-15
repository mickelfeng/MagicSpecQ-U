# revision 19963
# category Package
# catalog-ctan /macros/latex/contrib/parskip
# catalog-date 2010-09-30 14:11:14 +0200
# catalog-license lppl
# catalog-version 2.0

%{!?_texdir: %global _texdir %{_datadir}/texlive}
%define _texmfdistdir %{_texdir}/texmf-dist

Name:		texlive-parskip
Version:	2011
Release:	2%{?dist}
Summary:	Layout with zero \parindent, non-zero \parskip
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/parskip
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parskip.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parskip.doc.tar.xz
BuildArch:	noarch

%description
Simply changing \parskip and \parindent leaves a layout that is
untidy; this package (though it is no substitute for a
properly-designed class) helps alleviate this untidiness.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/parskip/parskip.sty
%doc %{_texmfdistdir}/doc/latex/parskip/parskip-doc.pdf
%doc %{_texmfdistdir}/doc/latex/parskip/parskip-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.0-2
+ Revision: 754649
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.0-1
+ Revision: 719200
- texlive-parskip
- texlive-parskip
- texlive-parskip
- texlive-parskip

