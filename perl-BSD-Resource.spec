#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-BSD-Resource
Version  : 1.2911
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/J/JH/JHI/BSD-Resource-1.2911.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JH/JHI/BSD-Resource-1.2911.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libb/libbsd-resource-perl/libbsd-resource-perl_1.2911-1.debian.tar.xz
Summary  : getrusage(), s/getrlimit(), s/getpriority()
Group    : Development/Tools
License  : Artistic-2.0 GPL-2.0 MIT
Requires: perl-BSD-Resource-lib = %{version}-%{release}
Requires: perl-BSD-Resource-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This Perl extension implements the BSD process resource limit functions
getrusage()	getrlimit()	setrlimit()

%package dev
Summary: dev components for the perl-BSD-Resource package.
Group: Development
Requires: perl-BSD-Resource-lib = %{version}-%{release}
Provides: perl-BSD-Resource-devel = %{version}-%{release}
Requires: perl-BSD-Resource = %{version}-%{release}

%description dev
dev components for the perl-BSD-Resource package.


%package lib
Summary: lib components for the perl-BSD-Resource package.
Group: Libraries
Requires: perl-BSD-Resource-license = %{version}-%{release}

%description lib
lib components for the perl-BSD-Resource package.


%package license
Summary: license components for the perl-BSD-Resource package.
Group: Default

%description license
license components for the perl-BSD-Resource package.


%prep
%setup -q -n BSD-Resource-1.2911
cd ..
%setup -q -T -D -n BSD-Resource-1.2911 -b 1
mkdir -p deblicense/
cp -r %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/BSD-Resource-1.2911/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-BSD-Resource
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-BSD-Resource/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/BSD/Resource.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/_find_prio.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/_find_rlimit.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/_g.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/autosplit.ix
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/get_prios.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/get_rlimits.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/getpriority.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/getrlimit.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/getrusage.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/hard.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/idrss.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/inblock.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/isrss.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/ixrss.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/majflt.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/maxrss.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/minflt.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/msgrcv.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/msgsnd.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/nivcsw.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/nsignals.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/nswap.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/nvcsw.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/oublock.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/setpriority.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/setrlimit.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/soft.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/stime.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/times.al
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/utime.al

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/BSD::Resource.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/BSD/Resource/Resource.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-BSD-Resource/deblicense_copyright
