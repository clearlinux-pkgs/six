#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : six
Version  : 1.12.0
Release  : 57
URL      : https://files.pythonhosted.org/packages/dd/bf/4138e7bfb757de47d1f4b6994648ec67a51efe58fa907c1e11e350cddfca/six-1.12.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/dd/bf/4138e7bfb757de47d1f4b6994648ec67a51efe58fa907c1e11e350cddfca/six-1.12.0.tar.gz
Summary  : Python 2 and 3 compatibility utilities
Group    : Development/Tools
License  : MIT
Requires: six-license = %{version}-%{release}
Requires: six-python = %{version}-%{release}
Requires: six-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : py
BuildRequires : pytest

%description
.. image:: https://img.shields.io/pypi/v/six.svg
:target: https://pypi.org/project/six/
:alt: six on PyPI

%package license
Summary: license components for the six package.
Group: Default

%description license
license components for the six package.


%package python
Summary: python components for the six package.
Group: Default
Requires: six-python3 = %{version}-%{release}

%description python
python components for the six package.


%package python3
Summary: python3 components for the six package.
Group: Default
Requires: python3-core

%description python3
python3 components for the six package.


%prep
%setup -q -n six-1.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570824833
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test -v || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/six
cp %{_builddir}/six-1.12.0/LICENSE %{buildroot}/usr/share/package-licenses/six/7dd6a5376d6f9dfa45a7499823adcece772b3f01
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/six/7dd6a5376d6f9dfa45a7499823adcece772b3f01

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
