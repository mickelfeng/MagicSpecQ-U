Name:		twolame
Version:	0.3.13
Release:	3%{?dist}
Summary:	TwoLAME is an optimised MPEG Audio Layer 2 encoding library based on tooLAME
Group:		Applications/Multimedia
License:	LGPLv2+
URL:		http://www.twolame.org/
Source:		http://downloads.sourceforge.net/twolame/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	libsndfile-devel
#BuildRequires:	libtool

%description
TwoLAME is an optimised MPEG Audio Layer 2 encoding library based on tooLAME,
which in turn is based heavily on
- the ISO dist10 code
- improvement to algorithms as part of the LAME project (www.sulaco.org/mp3)

This package contains the command line frontend.
                                                                                
%package libs
Summary:	TwoLAME is an optimised MPEG Audio Layer 2 encoding library based on tooLAME
Group:		System Environment/Libraries
Obsoletes:	%{name} < 0.3.12-1

%description libs
TwoLAME is an optimised MPEG Audio Layer 2 encoding library based on tooLAME,
which in turn is based heavily on
- the ISO dist10 code
- improvement to algorithms as part of the LAME project (www.sulaco.org/mp3)

This package contains the shared library.

%package devel
Summary:	Development tools for TwoLAME applications
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	pkgconfig

%description devel
This package contains the header files and documentation
needed to develop applications with TwoLAME.

%prep
%setup -q
# convert manpage to UTF8
pushd doc
iconv -f iso8859-1 -t utf8 %{name}.1 > %{name}.1.utf && mv %{name}.1.utf %{name}.1
# fix HTML docs line endings
for file in html/*.html ; do
	tr -d '\r' <$file >$file.unix && mv $file.unix $file
done
popd

%build
#autoreconf -f -i
%configure --disable-static

# remove rpath from libtool
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%{__make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_docdir}

%clean 
rm -rf $RPM_BUILD_ROOT

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files libs
%defattr(-,root,root,-)
%attr(755,root,root) %{_libdir}/lib%{name}.so.*

%files devel
%defattr(644,root,root,755)
%doc doc/api.txt doc/html doc/psycho.txt doc/vbr.txt
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.h

%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 0.3.13-3
- 为 Magic 3.0 重建

* Fri Feb 17 2012 Liu Di <liudidi@gmail.com> - 0.3.13-2
- 为 Magic 3.0 重建


