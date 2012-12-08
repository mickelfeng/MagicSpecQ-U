# Generated from ZenTest-4.1.4.gem by gem2rpm -*- rpm-spec -*-
%global gemdir %{gem_dir}
%global gemname ZenTest
%global	gem_name %{gemname}
%global geminstdir %{gem_instdir}

%global rubyabi 1.9.1

Summary: Automated test scaffolding for Ruby
Name: rubygem-%{gemname}
Version: 4.6.2
Release: 4%{?dist}
Group: Development/Languages
License: MIT
URL: http://www.zenspider.com/ZSS/Products/ZenTest/
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
#Patch0:  zentest-remove-broken-test.patch

Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems)
BuildRequires: rubygems-devel
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygem(minitest)
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
ZenTest is an automated test scaffolding for Ruby that provides 4 different
tools: zentest, unit_diff, autotest and multiruby. These tools can be used for
test conformance auditing and rapid XP.

%package doc
Summary: Documentation for %{name}
Group: Documentation

Requires: %{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%prep
%setup -q -c -T

mkdir -p .%{gemdir}
gem install --local --install-dir .%{gemdir} \
            --force -V --rdoc %{SOURCE0}

pushd .%{geminstdir}
#%%patch0 -p0

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* %{buildroot}%{gemdir}/

mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod 0755

# Various files marked executable that shouldn't be, and remove needless
# shebangs
find %{buildroot}%{geminstdir}/bin -type f | \
  xargs -n 1 sed -i -e 's"^#!/usr/bin/env ruby"#!/usr/bin/ruby"'
find %{buildroot}%{geminstdir}/bin -type f | \
  xargs -n 1 sed -i -e 's"^#!/usr/local/bin/ruby"#!/usr/bin/ruby"'
find %{buildroot}%{geminstdir}/test -type f | \
  xargs -n 1 sed -i  -e '/^#!\/usr\/.*\/ruby.*/d'
# Ships with extremely tight permissions, bring them inline with other gems
find %{buildroot}%{geminstdir} -type f | \
  xargs chmod 0644
find %{buildroot}%{geminstdir}/bin -type f | \
  xargs chmod 0755

%check
pushd .%{geminstdir}
testrb -Ilib test/test_*.rb
popd

%files
%{_bindir}/autotest
%{_bindir}/multigem
%{_bindir}/multiruby
%{_bindir}/multiruby_setup
%{_bindir}/unit_diff
%{_bindir}/zentest
%doc %{geminstdir}/History.txt
%doc %{geminstdir}/Manifest.txt
%doc %{geminstdir}/README.txt
%dir %{geminstdir}
%{geminstdir}/bin
%{geminstdir}/lib
%{geminstdir}/.gemtest
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%{geminstdir}/Rakefile
%{geminstdir}/test
%{geminstdir}/.autotest
%{geminstdir}/articles
%{geminstdir}/example*.rb
%{geminstdir}/example.txt
%{gemdir}/doc/%{gemname}-%{version}

%changelog
* Sat Dec 08 2012 Liu Di <liudidi@gmail.com> - 4.6.2-4
- 为 Magic 3.0 重建

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 07 2012 Vít Ondruch <vondruch@redhat.com> - 4.6.2-2
- Remove Rake dependency.

* Sun Jan 21 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.6.2-1
- 4.6.2

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 09 2011 Mo Morsi - 4.6.0-1
- New upstream version. Minor fixes and enhancements.

* Mon Aug 08 2011 Mo Morsi <mmorsi@redhat.com> - 4.3.3-3
- Replace BR(check) with BR

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 26 2010 Matthew Kent <mkent@magoazul.com> - 4.3.3-1
- New upstream version. Minor fixes and enhancements.

* Tue May 4 2010 Matthew Kent <mkent@magoazul.com> - 4.3.1-1
- New upstream version. Minor bugfixes - 1.9 compatibility.

* Sun Jan 24 2010 Matthew Kent <mkent@magoazul.com> - 4.2.1-1
- New upstream version.
- Don't reorganize files, leave as upstream intended.

* Sat Nov 21 2009 Matthew Kent <mkent@magoazul.com> - 4.1.4-3
- Drop Requires on hoe, only used by Rakefile (#539442).
- Move Rakefile to -doc (#539442).

* Sat Nov 21 2009 Matthew Kent <mkent@magoazul.com> - 4.1.4-2
- Better Source (#539442).
- More standard permissions on files.

* Mon Nov 16 2009 Matthew Kent <mkent@magoazul.com> - 4.1.4-1
- Initial package
