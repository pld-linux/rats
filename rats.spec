Summary:	Rough Auditing Tool for Security
Name:		rats
Version:	0.9
Release:	1
License:	GPL v2
Vendor:		Secure Software Solutions
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	http://www.securesw.com/rats/%{name}-%{version}.tar.gz
URL:		http://www.securesw.com/rats/
BuildRequires:	expat-devel
BuildRequires:	flex
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		%{_datadir}/misc

%description
RATS scans through code, finding potentially dangerous function calls.
The goal of this tool is not to definitively find bugs (yet). The
current goal is to provide a reasonable starting point for performing
manual security audits.

The initial vulnerability database is taken directly from things that
could be easily found when starting with the forthcoming book,
"Building Secure Software" by Viega and McGraw.

%prep
%setup -q 

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}}

install rats $RPM_BUILD_ROOT%{_bindir}
install rats.xml $RPM_BUILD_ROOT%{_libdir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/rats
%{_libdir}/rats.xml
