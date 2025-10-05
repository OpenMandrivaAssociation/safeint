# Mixing gcc and clang during testing (and since no binary
# is being generated, performance gain from LTO doesn't exist
# anyway)
%global _disable_lto 1

Name:           safeint
Version:        3.0.28a
Release:        2
Summary:        Class library for C++ that manages integer overflows
License:        MIT
URL:            https://github.com/dcleblanc/SafeInt
Source0:        https://github.com/dcleblanc/SafeInt/archive/%{version}/SafeInt-%{version}.tar.gz

BuildArch:	noarch

BuildSystem:	cmake
BuildOption:	-DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}/SafeInt

%patchlist
https://data.gpo.zugaina.org/guru/dev-cpp/safeint/files/safeint-3.0.28a-install-the-library.patch
https://data.gpo.zugaina.org/guru/dev-cpp/safeint/files/safeint-3.0.28a-make-tests-optional.patch
https://data.gpo.zugaina.org/guru/dev-cpp/safeint/files/safeint-3.0.28a-remove-broken-tests.patch
safeint-3.0.28a-fix-tests.patch

%description
Class library for C++ that manages integer overflows

%package devel
Summary: %{summary}

%description devel
Class library for C++ that manages integer overflows

%files devel
%license %{_docdir}/SafeInt/LICENSE
%doc README.md
%dir %{_includedir}/SafeInt
%{_includedir}/SafeInt/SafeInt.hpp
%{_includedir}/SafeInt/safe_math.h
%{_includedir}/SafeInt/safe_math_impl.h
