Name     : bazel
Version  : 3.6.0
Release  : 35
URL      : https://github.com/bazelbuild/bazel/releases/download/3.6.0/bazel-3.6.0-dist.zip
Source0  : https://github.com/bazelbuild/bazel/releases/download/3.6.0/bazel-3.6.0-dist.zip
Summary  : Open-source build and test tool
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : openjdk
BuildRequires : openjdk-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : protobuf-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : usrbinjava
BuildRequires : which
BuildRequires : zip
BuildRequires : zlib-dev
Requires : openjdk
Requires : usrbinjava

# stripping ends up removing the java payload from the self extracting jar
%define __strip /bin/true
%define debug_package %{nil}

%description
Bazel is an open-source build and test tool similar to Make, Maven, and Gradle.
It uses a human-readable, high-level build language. Bazel supports projects in
multiple languages and builds outputs for multiple platforms. Bazel supports
large codebases across multiple repositories, and large numbers of users.

%prep
%setup -q -c -n bazel-%{version}

%build
export SOURCE_DATE_EPOCH=1602285960
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk/
export EXTRA_BAZEL_ARGS="--host_javabase=@local_jdk//:jdk"
./compile.sh

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp -a output/bazel %{buildroot}/usr/bin

%files
%defattr(-,root,root,-)
/usr/bin/bazel
