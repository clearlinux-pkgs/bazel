Name     : bazel
Version  : 0.29.0
Release  : 33
URL      : https://github.com/bazelbuild/bazel/archive/0.29.0.tar.gz
Source0  : https://github.com/bazelbuild/bazel/archive/0.29.0.tar.gz
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
Source13 : https://github.com/bazelbuild/skydoc/archive/41c28e43dffbae39c52dd4b91932d1209e5a8893.tar.gz
Source14 : https://mirror.bazel.build/github.com/bazelbuild/rules_sass/archive/8ccf4f1c351928b55d5dddf3672e3667f6978d60.tar.gz
Source15 : https://github.com/bazelbuild/rules_nodejs/archive/0.16.2.zip
Source16 : https://mirror.bazel.build/openjdk/azul-zulu11.29.3-ca-jdk11.0.2/zulu11.29.3-ca-jdk11.0.2-linux_x64-minimal-90755145cb6e6418584d8603cd5fa9afbb30aecc-1549209948.tar.gz
Source17 : https://mirror.bazel.build/openjdk/azul-zulu10.2+3-jdk10.0.1/zulu10.2+3-jdk10.0.1-linux_x64-allmodules.tar.gz
Source18 : https://mirror.bazel.build/openjdk/azul-zulu11.29.3-ca-jdk11.0.2/zulu11.29.3-ca-jdk11.0.2-linux_x64-minimal-7a3af9f6f98ce69c1ebd2931817c2664a18cf279-1552657479.tar.gz
Source19 : https://mirror.bazel.build/bazel_java_tools/java_tools_pkg-0.5.1.tar.gz
Source20 : https://mirror.bazel.build/openjdk/azul-zulu11.29.3-ca-jdk11.0.2/zulu11.29.3-ca-jdk11.0.2-linux_x64-minimal-524ae2ca2a782c9f15e00f08bd35b3f8ceacbd7f-1556011926.tar.gz
Source21 : https://mirror.bazel.build/openjdk/azul-zulu11.2.3-jdk11.0.1/zulu11.2.3-jdk11.0.1-linux_x64.tar.gz
Source22 : https://mirror.bazel.build/bazel_java_tools/releases/javac10/v3.1/java_tools_javac10_linux-v3.1.zip
Source23 : https://mirror.bazel.build/bazel_java_tools/releases/javac11/v2.0/java_tools_javac11_linux-v2.0.zip
Source24 : https://github.com/bazelbuild/platforms/archive/441afe1bfdadd6236988e9cac159df6b5a9f5a98.zip
Source25 : https://github.com/bazelbuild/bazel-toolchains/archive/0.27.1.tar.gz
Source26 : https://github.com/bazelbuild/rules_pkg/releases/download/0.2.0/rules_pkg-0.2.0.tar.gz
Source27 : https://github.com/bazelbuild/rules_cc/archive/0d5f3f2768c6ca2faca0079a997a97ce22997a0c.zip
Source28 : https://github.com/bazelbuild/rules_proto/archive/b0cc14be5da05168b01db282fe93bdf17aa2b9f4.tar.gz

# stripping ends up removing the java payload from the self extracting jar
%define __strip /bin/true
%define debug_package %{nil}

Patch1: 0001-build.patch
Patch2: rename-gettid-functions.patch

%description
This repository contains a python implementation of the Google commandline
flags module.

%prep
%setup -q -n bazel-0.29.0
#%patch1 -p1

# https://github.com/vbatts/copr-build-bazel/commit/75516ad2211feb6326ce330de0efcd4ee662aba4
pushd third_party/grpc/
%patch2 -p0
popd

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
InstallCache %{SOURCE17}
InstallCache %{SOURCE18}
InstallCache %{SOURCE19}
InstallCache %{SOURCE20}
InstallCache %{SOURCE21}
InstallCache %{SOURCE22}
InstallCache %{SOURCE23}
InstallCache %{SOURCE24}
InstallCache %{SOURCE25}
InstallCache %{SOURCE26}
InstallCache %{SOURCE27}
InstallCache %{SOURCE28}

#./compile.sh compile  /usr/bin/bazel
bazel --output_base=/tmp/bazel build --repository_cache=/tmp/cache   //src:bazel


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp bazel-bin/src/bazel %{buildroot}/usr/bin

%files
%defattr(-,root,root,-)
/usr/bin/bazel
