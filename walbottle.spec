Name:           walbottle
Version:        2.0
%define soname  walbottle-0
Release:        1%{?dist}
Summary:        Walbottle is a project for generating JSON unit test vectors from JSON Schemas.

License:        LGPL
URL:            https://github.com/pwithnall/walbottle/
Source:         %{name}-%{version}.tar.gz

BuildRequires: meson
BuildRequires: gcc
BuildRequires: pkg-config
BuildRequires: cmake
BuildRequires: (ninja or ninja-build)

BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: gobject-introspection

Provides: /bin/json-schema-generate
Provides: /bin/json-schema-validate
Provides: /bin/json-validate


%description
%{summary}.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       pkgconfig(libwalbottle-0)

%description devel
%{summary}.

%package doc
Summary:        Documentations for %{name}

%description doc
%{summary}.

%prep
%setup -q


%build
%meson
%meson_build

%install
%meson_install
ln -sTf 'lib%{soname}' '%{buildroot}%{_includedir}/%{soname}'

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/lib*.so.*
%{_bindir}/*

%files doc
%{_mandir}/*/*

%files devel
%{_datadir}/gir-1.0/*
%{_libdir}/girepository-1.0/*
%{_libdir}/pkgconfig/*
%{_libdir}/lib*.so
%{_includedir}/%{soname}
%{_includedir}/lib%{soname}
