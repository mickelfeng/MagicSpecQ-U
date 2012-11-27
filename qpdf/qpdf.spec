Summary: Command-line tools and library for transforming PDF files
Name:    qpdf
Version: 3.0.2
Release: 1%{?dist}
License: Artistic 2.0
Group:   System Environment/Base
URL:     http://qpdf.sourceforge.net/
Source0: http://downloads.sourceforge.net/sourceforge/qpdf/qpdf-%{version}.tar.gz

BuildRequires: zlib-devel
BuildRequires: pcre-devel

# for fix-qdf and test suite
BuildRequires: perl
BuildRequires: perl(Digest::MD5)

# for autoreconf
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

Requires: qpdf-libs%{?_isa} = %{version}-%{release}

%package libs
Summary: QPDF library for transforming PDF files
Group:   System Environment/Libraries

%package devel
Summary: Development files for QPDF library
Group:   Development/Libraries
Requires: qpdf-libs%{?_isa} = %{version}-%{release}

%package doc
Summary: QPDF Manual
Group:   Documentation
BuildArch: noarch
Requires: qpdf-libs = %{version}-%{release}

%description
QPDF is a command-line program that does structural, content-preserving
transformations on PDF files. It could have been called something
like pdf-to-pdf. It includes support for merging and splitting PDFs
and to manipulate the list of pages in a PDF file. It is not a PDF viewer
or a program capable of converting PDF into other formats.

%description libs
QPDF is a C++ library that inspect and manipulate the structure of PDF files.
It can encrypt and linearize files, expose the internals of a PDF file,
and do many other operations useful to PDF developers.

%description devel
Header files and libraries necessary
for developing programs using the QPDF library.

%description doc
QPDF Manual

%prep
%setup -q

%build
# work-around check-rpaths errors
autoreconf --verbose --force --install

%configure --disable-static \
           --enable-show-failed-test-output

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# https://fedoraproject.org/wiki/Packaging_tricks#With_.25doc
mkdir __doc
mv  %{buildroot}%{_datadir}/doc/qpdf/* __doc
rm -rf %{buildroot}%{_datadir}/doc/qpdf

%check
make check

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%{_bindir}/fix-qdf
%{_bindir}/qpdf
%{_bindir}/zlib-flate
%{_mandir}/man1/*

%files libs
%doc README TODO ChangeLog Artistic-2.0
%{_libdir}/libqpdf*.so.*

%files devel
%doc examples/*.cc examples/*.c
%{_includedir}/*
%{_libdir}/libqpdf*.so
%{_libdir}/pkgconfig/libqpdf.pc

%files doc
%doc __doc/*

%changelog
* Fri Sep 07 2012 Jiri Popelka <jpopelka@redhat.com> 3.0.2-1
- 3.0.2

* Thu Aug 16 2012 Jiri Popelka <jpopelka@redhat.com> 3.0.1-3
- the previously added requirement doesn't need to be arch-specific

* Thu Aug 16 2012 Jiri Popelka <jpopelka@redhat.com> 3.0.1-2
- doc subpackage requires libs subpackage due to license file (#848466)

* Wed Aug 15 2012 Jiri Popelka <jpopelka@redhat.com> 3.0.1-1
- initial spec file
