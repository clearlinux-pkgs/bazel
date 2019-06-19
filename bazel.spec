Name     : bazel
Version  : 0.23.0
Release  : 31
URL      : https://github.com/bazelbuild/bazel/archive/0.23.0.tar.gz
Source0  : https://github.com/bazelbuild/bazel/archive/0.23.0.tar.gz
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

Source10 : https://github.com/google/desugar_jdk_libs/archive/e0b0291b2c51fbe5a7cfa14473a1ae850f94f021.zip
Source11 : https://mirror.bazel.build/openjdk/azul-zulu-9.0.7.1-jdk9.0.7/zulu9.0.7.1-jdk9.0.7-linux_x64-allmodules.tar.gz
Source12 : https://github.com/bazelbuild/bazel-skylib/archive/f83cb8dd6f5658bc574ccd873e25197055265d1c.tar.gz
Source13 : https://github.com/bazelbuild/skydoc/archive/2d9566b21fbe405acf5f7bf77eda30df72a4744c.tar.gz
Source14 : https://mirror.bazel.build/github.com/bazelbuild/rules_sass/archive/8ccf4f1c351928b55d5dddf3672e3667f6978d60.tar.gz
Source15 : https://github.com/bazelbuild/rules_nodejs/archive/0.16.2.zip
Source16 : https://mirror.bazel.build/openjdk/azul-zulu11.29.3-ca-jdk11.0.2/zulu11.29.3-ca-jdk11.0.2-linux_x64-minimal-90755145cb6e6418584d8603cd5fa9afbb30aecc-1549209948.tar.gz

%define __strip /bin/true
%define debug_package %{nil}

Patch1: 0001-build.patch

%description
This repository contains a python implementation of the Google commandline
flags module.

%prep
%setup -q -n bazel-0.23.0
#%patch1 -p1

%build

InstallCache() {
	sha256=`sha256sum $1 | cut -f1 -d" "`
	mkdir -p /tmp/cache/content_addressable/sha256/$sha256/
	cp $1 /tmp/cache/content_addressable/sha256/$sha256/file
}

InstallCache %{SOURCE10}
InstallCache %{SOURCE11}
InstallCache %{SOURCE12}
InstallCache %{SOURCE13}
InstallCache %{SOURCE14}
InstallCache %{SOURCE15}
InstallCache %{SOURCE16}

#./compile.sh compile  /usr/bin/bazel
bazel --output_base=/tmp/bazel build --repository_cache=/tmp/cache   //src:bazel


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp bazel-bin/src/bazel %{buildroot}/usr/bin

%files
%defattr(-,root,root,-)
/usr/bin/bazel
