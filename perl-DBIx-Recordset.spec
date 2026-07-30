%define upstream_name	 DBIx-Recordset
%define upstream_version 0.26
Name:		perl-%{upstream_name}
Version:	0.26
Release:	3

Summary:	Perl extension for DBI recordsets
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/DBIx-Recordset
Source0:	https://cpan.metacpan.org/authors/id/G/GR/GRICHTER/DBIx-Recordset-0.26.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(DBI)
BuildRequires:  perl(DBD::Pg)
BuildArch:	noarch
Requires:	perl(DBI)

%description
DBIx::Recordset is a perl module for abstraction and simplification of database
access.

The goal is to make standard database access (select/insert/update/delete)
easier to handle and independend of the underlying DBMS. Special attention is
made on web applications to make it possible to handle the state-less access
and to process the posted data of formfields, but DBIx::Recordset is not
limited to web applications.

%prep
%setup -q -n DBIx-Recordset-0.26

%build
chmod 644 Changes Recordset.pm
perl -pi -e 's/\cM//' Changes
perl Makefile.PL INSTALLDIRS=vendor << EOF




EOF
make

%install
%makeinstall_std

%files
%doc Changes README TODO
%{_mandir}/*/*
%{perl_vendorlib}/DBIx


