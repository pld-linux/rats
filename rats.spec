Summary:	Rough Auditing Tool for Security
Summary(pl):	Narz�dzie do pobie�nych audyt�w bezpiecze�stwa
Name:		rats
Version:	0.9
Release:	2
License:	GPL v2
Vendor:		Secure Software Solutions
Group:		Development/Tools
Source0:	http://www.securesw.com/rats/%{name}-%{version}.tar.gz
URL:		http://www.securesw.com/rats/
BuildRequires:	autoconf
BuildRequires:	automake
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

%description -l pl
RATS skanuje kod, znajduj�c wywo�ania potencjalnie niebezpiecznych
funkcji. Celem tego narz�dzia nie jest (jeszcze) definitywne
znajdowanie b��d�w. Aktualnym celem jest dostarczenie sensownego
punktu startowego do przeprowadzania r�cznych audyt�w bezpiecze�stwa.

Pocz�tkowa baza dziur jest brana bezpo�rednio z rzeczy, kt�re mog� by�
�atwo znalezione przy lekturze nadchodz�cej ksi��ki "Building Secure
Software" napisanaj przez Vieg� i McGrawa.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}}

install rats $RPM_BUILD_ROOT%{_bindir}
install rats.xml $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/rats
%{_libdir}/rats.xml
