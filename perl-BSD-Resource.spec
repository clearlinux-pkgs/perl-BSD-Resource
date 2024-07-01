#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-BSD-Resource
Version  : 1.2911
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/J/JH/JHI/BSD-Resource-1.2911.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JH/JHI/BSD-Resource-1.2911.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libb/libbsd-resource-perl/libbsd-resource-perl_1.2911-1.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-2.0 GPL-2.0 MIT
Requires: perl-BSD-Resource-license = %{version}-%{release}
Requires: perl-BSD-Resource-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This Perl extension implements the BSD process resource limit functions
getrusage()	getrlimit()	setrlimit()

%package dev
Summary: dev components for the perl-BSD-Resource package.
Group: Development
Provides: perl-BSD-Resource-devel = %{version}-%{release}
Requires: perl-BSD-Resource = %{version}-%{release}

%description dev
dev components for the perl-BSD-Resource package.


%package license
Summary: license components for the perl-BSD-Resource package.
Group: Default

%description license
license components for the perl-BSD-Resource package.


%package perl
Summary: perl components for the perl-BSD-Resource package.
Group: Default
Requires: perl-BSD-Resource = %{version}-%{release}

%description perl
perl components for the perl-BSD-Resource package.


%prep
%setup -q -n BSD-Resource-1.2911
cd %{_builddir}
tar xf %{_sourcedir}/libbsd-resource-perl_1.2911-1.debian.tar.xz
cd %{_builddir}/BSD-Resource-1.2911
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/BSD-Resource-1.2911/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-BSD-Resource
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-BSD-Resource/e480be47ede00434fc8827bbce2d3d8688646967
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/BSD::Resource.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-BSD-Resource/e480be47ede00434fc8827bbce2d3d8688646967

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
