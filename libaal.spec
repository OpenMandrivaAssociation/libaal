%define major 5
%define api 1.0
%define libname %mklibname aal- %{api} %{major}
%define libname_basic %mklibname aal-%{api}
%define minimal_libname	%mklibname aal-minimal 0

Summary:	Library for Reiser4 filesystem
Name:		libaal
Version:	1.0.6
Release:	1
License:	GPLv2
Group:		System/Libraries
Source0:	http://www.kernel.org/pub/linux/utils/fs/reiser4/libaal/%{name}-%{version}.tar.gz
Patch0:		libaal-1.0.5-rpmoptflags.patch
Patch1:		libaal.castint.patch
URL:		http://www.kernel.org/pub/linux/utils/fs/reiser4/

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
%global optflags %{optflags} -Qunused-arguments

# be very pedantic
# needed for patch0
autoreconf -f
libtoolize
%configure \
	--libdir=/%{_lib}\
	--libexecdir=/%{_lib}\
	--enable-Werror \
	%{?debug:--enable-debug}

%make

%install
%makeinstall_std

%files -n %{libname}
# COPYING contains information other than GPL text
%doc AUTHORS BUGS COPYING CREDITS ChangeLog README THANKS TODO
/%{_lib}/libaal-%{api}.so.%{major}*

%files -n %{minimal_libname}
/%{_lib}/libaal-minimal.so.*

%files devel
/%{_lib}/lib*.so
%{_includedir}/*
%{_datadir}/aclocal/*.m4

%files static-devel
/%{_lib}/lib*.a
