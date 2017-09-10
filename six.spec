#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : six
Version  : 1.10.0
Release  : 28
URL      : http://pypi.debian.net/six/six-1.10.0.tar.gz
Source0  : http://pypi.debian.net/six/six-1.10.0.tar.gz
Summary  : Python 2 and 3 compatibility utilities
Group    : Development/Tools
License  : MIT
Requires: six-legacypython
Requires: six-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
for smoothing over the differences between the Python versions with the goal of
        writing Python code that is compatible on both Python versions.  See the
        documentation for more information on what is provided.
        
        Six supports every Python version since 2.6.  It is contained in only one Python
        file, so it can be easily copied into your project. (The copyright and license
        notice must be retained.)

%package legacypython
Summary: legacypython components for the six package.
Group: Default

%description legacypython
legacypython components for the six package.


%package python
Summary: python components for the six package.
Group: Default
Requires: six-legacypython

%description python
python components for the six package.


%prep
%setup -q -n six-1.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505071526
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test -v
%install
export SOURCE_DATE_EPOCH=1505071526
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
/usr/lib/python3*/*
