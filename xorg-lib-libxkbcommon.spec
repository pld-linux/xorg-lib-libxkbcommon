Summary:	xkbcommon library - keymap compiler and support library
Summary(pl.UTF-8):	Biblioteka xkbcommon - kompilatora i obsługi map klawiszy
Name:		xorg-lib-libxkbcommon
Version:	0.2.0
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xkbcommon.org/download/libxkbcommon-%{version}.tar.bz2
# Source0-md5:	2be3d4a255d02c7d46fc6a9486f21f6a
URL:		http://xkbcommon.org/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	doxygen
BuildRequires:	flex
BuildRequires:	libtool >= 2:2.0
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-kbproto-devel >= 1.0.4
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
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
xkbcommon library.

This package contains the header files needed to develop programs that
use libxkbcommon.

%description devel -l pl.UTF-8
Biblioteka xkbcommon.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libxkbcommon.

%package static
Summary:	Static libxkbcommon library
Summary(pl.UTF-8):	Biblioteka statyczna libxkbcommon
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
xkbcommon library.

This package contains the static libxkbcommon library.

%description static -l pl.UTF-8
Biblioteka xkbcommon.

Pakiet zawiera statyczną bibliotekę libxkbcommon.

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
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libxkbcommon.la
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libxkbcommon

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libxkbcommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxkbcommon.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/html/*
%attr(755,root,root) %{_libdir}/libxkbcommon.so
%{_includedir}/xkbcommon
%{_pkgconfigdir}/xkbcommon.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxkbcommon.a
