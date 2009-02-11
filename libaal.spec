%define version 1.0.5
%define release %mkrel 1

%define major	5
%define api	1.0
%define libname %mklibname aal- %{api} %{major}
%define libname_basic %mklibname aal-%{api}
%define minimal_libname	%mklibname aal-minimal 0

Summary:	Library for Reiser4 filesystem
Name:		libaal
Version:	%{version}
Release:	%{release}
License:	GPLv2
Group:		System/Libraries
Source0:	http://www.kernel.org/pub/linux/utils/fs/reiser4/libaal/%{name}-%{version}.tar.bz2
Patch0:		libaal-1.0.5-rpmoptflags.patch
Patch1:		libaal.castint.patch
URL:		http://www.kernel.org/pub/linux/utils/fs/reiser4/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
libaal library - needed for Reiser4 filesystem utilities.

%package -n	%{libname}
Summary:	Library for Reiser4 filesystem
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Provides:	%{_lib}aal-%{api} = %{version}-%{release}

%description -n	%{libname}
libaal library - needed for Reiser4 filesystem utilities.

%package	devel
Summary:	Development related files for libaal library
Group:		Development/C
Requires: 	%{libname} = %{version}
Requires: 	%{minimal_libname} = %{version}
# Don't provide! This is just temporary
Obsoletes:	libaal3-devel libaal2-devel

%description	devel
Development related files for libaal library.

%package	static-devel
Summary:	Static libaal library
Group:		Development/C
Requires: 	%{name}-devel = %{version}
# Don't provide! This is just temporary
Obsoletes:	libaal3-static-devel libaal2-static-devel

%description	static-devel
The static libaal library.

%package -n	%{minimal_libname}
Summary:	%{name} library with miminal footprint
Group:		System/Libraries

%description -n %{minimal_libname}
%{name} library with miminal memory foorprint. This is
useful when you need to build grub with Reiser4 support.

%prep
%setup -q
%patch0 -p1 -b .cflags
%patch1 -p1 -b .castint

%build
# be very pedantic
# needed for patch0
autoreconf -f
libtoolize
%configure2_5x \
	--enable-Werror \
	%{?debug:--enable-debug}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post   -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%post   -n %{minimal_libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{minimal_libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root,-)
# COPYING contains information other than GPL text
%doc AUTHORS BUGS COPYING CREDITS ChangeLog README THANKS TODO
%{_libdir}/libaal-%{api}.so.%{major}*

%files -n %{minimal_libname}
%defattr(-,root,root,-)
%{_libdir}/libaal-minimal.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_datadir}/aclocal/*.m4

%files static-devel
%defattr(-,root,root,-)
%{_libdir}/lib*.a
