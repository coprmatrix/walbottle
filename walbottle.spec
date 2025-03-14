Name:           walbottle
Version:        2.0
Release:        2%{?dist}
Summary:        Walbottle is a project for generating JSON unit test vectors from JSON Schemas.

License:        LGPL
URL:            https://github.com/pwithnall/walbottle/
Source:         %{name}-%{version}.tar.gz

%define soname walbottle-0

BuildRequires: 	meson
BuildRequires: 	gcc
BuildRequires: 	pkg-config
BuildRequires: 	cmake
BuildRequires: 	(ninja or ninja-build)

BuildRequires: 	pkgconfig(gobject-introspection-1.0)
BuildRequires: 	pkgconfig(gio-2.0)
BuildRequires: 	pkgconfig(glib-2.0)
BuildRequires: 	pkgconfig(gobject-2.0)
BuildRequires: 	pkgconfig(json-glib-1.0)
BuildRequires: 	gobject-introspection

Provides: 	/bin/json-schema-generate
Provides: 	/bin/json-schema-validate
Provides: 	/bin/json-validate
Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description
%{summary}.

%package -n lib%{name}
Summary:	Runtime library for %{name}

%description -n lib%{name}
%{summary}.

%package -n lib%{name}-devel
Summary:        Development libraries and header files for %{name}
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Provides:       pkgconfig(libwalbottle-0)

%description -n lib%{name}-devel
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

%files -n lib%{name}
%{_libdir}/lib*.so.*
%{_libdir}/girepository-1.0/*

%files
%{_bindir}/*

%files doc
%{_mandir}/*/*

%files -n lib%{name}-devel
%{_datadir}/gir-1.0/*
%{_libdir}/pkgconfig/*
%{_libdir}/lib*.so
%{_includedir}/%{soname}
%{_includedir}/lib%{soname}
