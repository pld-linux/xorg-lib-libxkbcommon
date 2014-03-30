Summary:	xkbcommon library - keymap compiler and support library
Summary(pl.UTF-8):	Biblioteka xkbcommon - kompilatora i obsługi map klawiszy
Name:		xorg-lib-libxkbcommon
Version:	0.4.1
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xkbcommon.org/download/libxkbcommon-%{version}.tar.xz
# Source0-md5:	b70f4ed97b6c9432dc956e4177f3336a
URL:		http://xkbcommon.org/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	doxygen
BuildRequires:	flex
BuildRequires:	libtool >= 2:2.0
BuildRequires:	libxcb-devel >= 1.10
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-proto-kbproto-devel >= 1.0.4
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.16
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libxkbcommon is a keymap compiler and support library which processes
a reduced subset of keymaps as defined by the XKB specification.

%description -l pl.UTF-8
libxkbcommon to biblioteka kompilatora i obsługi map klawiszy,
przetwarzająca ograniczony podzbiór map klawiszy zdefiniowanych w
specyfikacji XKB.

%package devel
Summary:	Header files for libxkbcommon library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libxkbcommon
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files needed to develop programs that
use libxkbcommon.

%description devel -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libxkbcommon.

%package static
Summary:	Static libxkbcommon library
Summary(pl.UTF-8):	Biblioteka statyczna libxkbcommon
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static libxkbcommon library.

%description static -l pl.UTF-8
Pakiet zawiera statyczną bibliotekę libxkbcommon.

%package x11
Summary:	X11 support for XKB library
Summary(pl.UTF-8):	Obsługa X11 dla biblioteki XKB
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxcb >= 1.10

%description x11
X11 support for XKB library.

%description x11 -l pl.UTF-8
Obsługa X11 dla biblioteki XKB.

%package x11-devel
Summary:	Header file for libxkbcommon-x11 library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki libxkbcommon-x11
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-x11 = %{version}-%{release}
Requires:	libxcb-devel >= 1.10

%description x11-devel
Header file for libxkbcommon-x11 library.

%description x11-devel -l pl.UTF-8
Plik nagłówkowy biblioteki libxkbcommon-x11.

%package x11-static
Summary:	Static libxkbcommon-x11 library
Summary(pl.UTF-8):	Statyczna biblioteka libxkbcommon-x11
Group:		X11/Development/Libraries
Requires:	%{name}-x11-devel = %{version}-%{release}

%description x11-static
Static libxkbcommon-x11 library.

%description x11-static -l pl.UTF-8
Statyczna biblioteka libxkbcommon-x11.

%package apidocs
Summary:	API documentation for libxkbcommon libraries
Summary(pl.UTF-8):	Dokumentacja API bibliotek libxkbcommon
Group:		Documentation

%description apidocs
API documentation for libxkbcommon libraries.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotek libxkbcommon.

%prep
%setup -q -n libxkbcommon-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libxkbcommon*.la
# packaged as %doc in -apidocs
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libxkbcommon

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	x11 -p /sbin/ldconfig
%postun x11 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README.md
%attr(755,root,root) %{_libdir}/libxkbcommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxkbcommon.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxkbcommon.so
%dir %{_includedir}/xkbcommon
%{_includedir}/xkbcommon/xkbcommon.h
%{_includedir}/xkbcommon/xkbcommon-compat.h
%{_includedir}/xkbcommon/xkbcommon-keysyms.h
%{_includedir}/xkbcommon/xkbcommon-names.h
%{_pkgconfigdir}/xkbcommon.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxkbcommon.a

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxkbcommon-x11.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxkbcommon-x11.so.0

%files x11-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxkbcommon-x11.so
%{_includedir}/xkbcommon/xkbcommon-x11.h
%{_pkgconfigdir}/xkbcommon-x11.pc

%files x11-static
%defattr(644,root,root,755)
%{_libdir}/libxkbcommon-x11.a

%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*
