#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-latest
Version  : 0.03
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/A/AN/ANDYA/latest-0.03.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AN/ANDYA/latest-0.03.tar.gz
Summary  : Use the latest Perl features
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-latest-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
latest version 0.03
INSTALLATION
To install this module, run the following commands:

%package dev
Summary: dev components for the perl-latest package.
Group: Development
Provides: perl-latest-devel = %{version}-%{release}
Requires: perl-latest = %{version}-%{release}

%description dev
dev components for the perl-latest package.


%package perl
Summary: perl components for the perl-latest package.
Group: Default
Requires: perl-latest = %{version}-%{release}

%description perl
perl components for the perl-latest package.


%prep
%setup -q -n latest-0.03
cd %{_builddir}/latest-0.03

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

%install
rm -rf %{buildroot}
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
/usr/share/man/man3/latest.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/latest.pm
