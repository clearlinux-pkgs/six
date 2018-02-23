#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : six
Version  : 1.11.0
Release  : 37
URL      : http://pypi.debian.net/six/six-1.11.0.tar.gz
Source0  : http://pypi.debian.net/six/six-1.11.0.tar.gz
Summary  : Python 2 and 3 compatibility utilities
Group    : Development/Tools
License  : MIT
Requires: six-python3
Requires: six-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
.. image:: http://img.shields.io/pypi/v/six.svg
:target: https://pypi.python.org/pypi/six

%package legacypython
Summary: legacypython components for the six package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the six package.


%package python
Summary: python components for the six package.
Group: Default
Requires: six-python3

%description python
python components for the six package.


%package python3
Summary: python3 components for the six package.
Group: Default
Requires: python3-core

%description python3
python3 components for the six package.


%prep
%setup -q -n six-1.11.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519407217
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test -v
%install
export SOURCE_DATE_EPOCH=1519407217
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
