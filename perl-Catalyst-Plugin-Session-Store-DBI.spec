#
# Conditional build:
%bcond_with	tests		# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Plugin-Session-Store-DBI
Summary:	Catalyst::Plugin::Session::Store::DBI - Store your sessions in a database
Summary(pl.UTF-8):	Catalyst::Plugin::Session::Store::DBI - przechowywanie sesji w bazie danych
Name:		perl-Catalyst-Plugin-Session-Store-DBI
Version:	0.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fda0bc9f14049e375921dbf36e7fbb25
URL:		http://search.cpan.org/dist/Catalyst-Plugin-Session-Store-DBI/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst >= 5.49
BuildRequires:	perl-Catalyst-Plugin-Session >= 0.05
BuildRequires:	perl-DBI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This storage module will store session data in a database using DBI.

%description -l pl.UTF-8
Ten moduł przechowuje dane sesji w bazie danych przy użyciu DBI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -we 'WriteMakefile(NAME=>"Catalyst::Plugin::Session::Store::DBI")' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Catalyst/Plugin/Session/Store/*.pm
%{_mandir}/man3/*
