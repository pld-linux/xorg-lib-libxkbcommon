#
# Conditional build:
%bcond_without	tests	# check target
#
Summary:	xkbcommon library - keymap compiler and support library
Summary(pl.UTF-8):	Biblioteka xkbcommon - kompilatora i obsługi map klawiszy
Name:		xorg-lib-libxkbcommon
Version:	1.0.3
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xkbcommon.org/download/libxkbcommon-%{version}.tar.xz
# Source0-md5:	bd0ff892fe937e39ec3bb4daeb348f76
URL:		https://xkbcommon.org/
BuildRequires:	bison
BuildRequires:	doxygen
BuildRequires:	flex
BuildRequires:	libxcb-devel >= 1.10
BuildRequires:	libxml2-devel
BuildRequires:	meson >= 0.49.0
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-proto-kbproto-devel >= 1.0.4
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.16
BuildRequires:	xz
%if %{with tests}
# wayland-client, wayland-scanner
BuildRequires:	wayland-devel >= 1.2
BuildRequires:	wayland-protocols >= 1.7
BuildRequires:	xorg-app-xkbcomp
BuildRequires:	xorg-xserver-Xvfb
%endif
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

%package tools
Summary:	Tools to interact with XKB keymaps
Summary(pl.UTF-8):	Narzędzia do współpracy z mapowaniami klawiszy XKB
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-x11 = %{version}-%{release}
Requires:	libxkbregistry = %{version}-%{release}

%description tools
Tools to interact with XKB keymaps.

%description tools -l pl.UTF-8
Narzędzia do współpracy z mapowaniami klawiszy XKB.

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
%{?noarchpackage}

%description apidocs
API documentation for libxkbcommon libraries.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotek libxkbcommon.

%package -n libxkbregistry
Summary:	Library to query available RMLVO
Summary(pl.UTF-8):	Biblioteka do odpytywania dostępnych RMLVO
Group:		Development/Libraries

%description -n libxkbregistry
Library to query available RMLVO.

%description -n libxkbregistry -l pl.UTF-8
Biblioteka do odpytywania dostępnych RMLVO.

%package -n libxkbregistry-devel
Summary:	Header files for libxkbregistry library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libxkbregistry
Group:		Development/Libraries
Requires:	libxkbregistry = %{version}-%{release}

%description -n libxkbregistry-devel
This package contains the header files needed to develop programs that
use libxkbregistry.

%description -n libxkbregistry-devel -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libxkbregistry.

%package -n libxkbregistry-static
Summary:	Static libxkbregistry library
Summary(pl.UTF-8):	Biblioteka statyczna libxkbregistry
Group:		Development/Libraries
Requires:	libxkbregistry-devel = %{version}-%{release}

%description -n libxkbregistry-static
This package contains the static libxkbregistry library.

%description -n libxkbregistry-static -l pl.UTF-8
Pakiet zawiera statyczną bibliotekę libxkbregistry.

%prep
%setup -q -n libxkbcommon-%{version}

%build
%meson build

%ninja_build -C build

%if %{with tests}
%ninja_test -C build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# packaged as %doc in -apidocs
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libxkbcommon

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	x11 -p /sbin/ldconfig
%postun x11 -p /sbin/ldconfig

%post	-n libxkbregistry -p /sbin/ldconfig
%postun	-n libxkbregistry -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README.md
%attr(755,root,root) %{_libdir}/libxkbcommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxkbcommon.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxkbcommon.so
%dir %{_includedir}/xkbcommon
%{_includedir}/xkbcommon/xkbcommon.h
%{_includedir}/xkbcommon/xkbcommon-compat.h
%{_includedir}/xkbcommon/xkbcommon-compose.h
%{_includedir}/xkbcommon/xkbcommon-keysyms.h
%{_includedir}/xkbcommon/xkbcommon-names.h
%{_pkgconfigdir}/xkbcommon.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxkbcommon.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xkbcli
%dir %{_libexecdir}/xkbcommon
%attr(755,root,root) %{_libexecdir}/xkbcommon/xkbcli-compile-keymap
%attr(755,root,root) %{_libexecdir}/xkbcommon/xkbcli-how-to-type
%attr(755,root,root) %{_libexecdir}/xkbcommon/xkbcli-interactive-evdev
%attr(755,root,root) %{_libexecdir}/xkbcommon/xkbcli-interactive-wayland
%attr(755,root,root) %{_libexecdir}/xkbcommon/xkbcli-interactive-x11
%attr(755,root,root) %{_libexecdir}/xkbcommon/xkbcli-list
%{_mandir}/man1/xkbcli.1*
%{_mandir}/man1/xkbcli-compile-keymap.1*
%{_mandir}/man1/xkbcli-how-to-type.1*
%{_mandir}/man1/xkbcli-interactive-evdev.1*
%{_mandir}/man1/xkbcli-interactive-wayland.1*
%{_mandir}/man1/xkbcli-interactive-x11.1*
%{_mandir}/man1/xkbcli-list.1*

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
%doc build/html/*

%files -n libxkbregistry
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxkbregistry.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxkbregistry.so.0

%files -n libxkbregistry-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxkbregistry.so
%{_includedir}/xkbcommon/xkbregistry.h
%{_pkgconfigdir}/xkbregistry.pc

%files -n libxkbregistry-static
%defattr(644,root,root,755)
%{_libdir}/libxkbregistry.a
