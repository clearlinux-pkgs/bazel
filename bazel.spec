Name     : bazel
Version  : 0.17.2
Release  : 28
URL      : https://github.com/bazelbuild/bazel/archive/0.17.2.tar.gz
Source0  : https://github.com/bazelbuild/bazel/archive/0.17.2.tar.gz
Summary  : A Python Mocking and Patching Library for Testing
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : openjdk-bin openjdk-dev
BuildRequires : zlib-dev zip
BuildRequires : bazel
BuildRequires : protobuf-dev

Requires : openjdk

Source10: https://github.com/google/desugar_jdk_libs/archive/fd937f4180c1b557805219af4482f1a27eb0ff2b.zip
Source11: https://mirror.bazel.build/openjdk/azul-zulu-9.0.7.1-jdk9.0.7/zulu9.0.7.1-jdk9.0.7-linux_x64-allmodules.tar.gz
Source12: https://github.com/bazelbuild/bazel-skylib/archive/7490380c6bbf9a5a060df78dc2222e7de6ffae5c.tar.gz

%define __strip /bin/true
%define debug_package %{nil}

Patch1: 0001-build.patch

%description
This repository contains a python implementation of the Google commandline
flags module.

%prep
%setup -q -n bazel-0.17.2
%patch1 -p1

%build

InstallCache() {
	sha256=`sha256sum $1 | cut -f1 -d" "`
	mkdir -p /tmp/cache/content_addressable/sha256/$sha256/
	cp $1 /tmp/cache/content_addressable/sha256/$sha256/file
}

InstallCache %{SOURCE10}
InstallCache %{SOURCE11}
InstallCache %{SOURCE12}

#./compile.sh compile  /usr/bin/bazel
bazel --output_base=/tmp/bazel build --repository_cache=/tmp/cache   //src:bazel


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp bazel-bin/src/bazel %{buildroot}/usr/bin

%files
%defattr(-,root,root,-)
/usr/bin/bazel
