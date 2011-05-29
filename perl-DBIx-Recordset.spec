%define upstream_name	 DBIx-Recordset
%define upstream_version 0.26

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Perl extension for DBI recordsets
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-DBI
BuildRequires:  perl-DBD-Pg
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%release}
Requires:	perl-DBI perl
Requires:	perl-base >= 2:5.8.7

%description
DBIx::Recordset is a perl module for abstraction and simplification of database
access.

The goal is to make standard database access (select/insert/update/delete)
easier to handle and independend of the underlying DBMS. Special attention is
made on web applications to make it possible to handle the state-less access
and to process the posted data of formfields, but DBIx::Recordset is not
limited to web applications.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
