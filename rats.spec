Name: rats
Summary: Rough Auditing Tool for Security
Version: 0.9
Release: 1
Copyright: GPL
Group: Development
Source0: http://www.securesw.com/rats/rats-%{version}.tar.gz
Packager: Scott Shinn <scott@securesw.com>
Vendor: Secure Software Solutions
Buildroot: /var/tmp/%{name}-root
BuildPrereq: expat-devel
Requires: expat


%description
RATS scans through code,
finding potentially dangerous function calls.  The goal of this tool
is not to definitively find bugs (yet).  The current goal is to provide a reasonable starting point for performing manual security audits.

The initial vulnerability database is taken directly from things that
could be easily found when starting with the forthcoming book, 
"Building Secure Software" by Viega and McGraw.  

RATS is released under version 2 of the GNU Public License (GPL).


%prep
%setup 

%build
CFLAGS="$RPM_OPT_FLAGS"; export CFLAGS
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{usr/lib/,/usr/bin}
install -c rats $RPM_BUILD_ROOT/usr/bin/
install -c -m644 rats.xml $RPM_BUILD_ROOT/usr/lib/

%post

%preun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/lib/rats.xml
/usr/bin/rats

%changelog
* Mon May 21 2001 Scott Shinn <scott@securesw.com>
- initial release
