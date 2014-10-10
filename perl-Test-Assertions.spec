%define upstream_name    Test-Assertions
%define upstream_version 1.054

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Base for test scripts
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(Log::Trace)
BuildArch:	noarch

%description
Test::Assertions provides a convenient set of tools for constructing tests,
such as unit tests or run-time assertion checks (like C's ASSERT macro).
Unlike some of the Test:: modules available on CPAN, Test::Assertions is
not limited to unit test scripts; for example it can be used to check
output is as expected within a benchmarking script. When it is used for
unit tests, it generates output in the standard form for CPAN unit testing
(under Test::Harness).

The package's import method is used to control the behaviour of ASSERT:
whether it dies, warns, prints 'ok'/'not ok', or does nothing.

In 'test' mode the script also exports plan(), only() and ignore()
functions. In 'test/ok' mode an ok() function is also exported for
compatibility with Test/Test::Harness. The plan function attempts to count
the number of tests if it isn't told a number (this works fine in simple
test scripts but not in loops/subroutines). In either mode, a warning will
be emitted if the planned number of tests is not the same as the number of
tests actually run, e.g.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.54.0-3mdv2011.0
+ Revision: 658885
- rebuild for updated spec-helper

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.54.0-2mdv2011.0
+ Revision: 552179
- rebuild

* Fri Jul 10 2009 Jérôme Quelin <jquelin@mandriva.org> 1.54.0-1mdv2010.0
+ Revision: 394298
- import perl-Test-Assertions


* Fri Jul 10 2009 cpan2dist 1.054-1mdv
- initial mdv release, generated with cpan2dist
