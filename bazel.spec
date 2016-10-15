Name     : bazel
Version  : 0.3.2
Release  : 9
URL      : https://github.com/bazelbuild/bazel/archive/0.3.2.tar.gz
Source0  : https://github.com/bazelbuild/bazel/archive/0.3.2.tar.gz
Summary  : A Python Mocking and Patching Library for Testing
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : openjdk-bin openjdk-dev
BuildRequires : zlib-dev zip

Requires : openjdk


%define __strip /bin/true
%define debug_package %{nil}

Patch1: 0001-build.patch

%description
This repository contains a python implementation of the Google commandline
flags module.

%prep
%setup -q -n bazel-0.3.2
%patch1 -p1

%build
./compile.sh

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp output/bazel %{buildroot}/usr/bin

%files
%defattr(-,root,root,-)
/usr/bin/bazel
