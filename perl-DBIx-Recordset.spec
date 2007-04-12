%define module	DBIx-Recordset
%define	name	perl-%{module}
%define version 0.26
%define release %mkrel 3

Summary:	Perl extension for DBI recordsets
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%release}-buildroot/
BuildRequires:	perl-DBI
BuildRequires:	perl-devel
BuildRequires:  perl-DBD-Pg
Requires:	perl-DBI perl
Requires:	perl-base >= 2:5.8.7
BuildArch:	noarch

%description
DBIx::Recordset is a perl module for abstraction and simplification of database
access.

The goal is to make standard database access (select/insert/update/delete)
easier to handle and independend of the underlying DBMS. Special attention is
made on web applications to make it possible to handle the state-less access
and to process the posted data of formfields, but DBIx::Recordset is not
limited to web applications.

%prep
%setup -q -n %{module}-%{version}

%build
chmod 644 Changes Recordset.pm
perl -pi -e 's/\cM//' Changes
perl Makefile.PL INSTALLDIRS=vendor << EOF




EOF
make

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README TODO
%{_mandir}/*/*
%{perl_vendorlib}/DBIx


