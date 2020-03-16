%global apiver %(v=2.1.0; echo ${v%.${v#[0-9].[0-9].}})

Name:           luajit
Version:        2.1.0
Release:        0.9beta3
Summary:        Just-In-Time Compiler for Lua
License:        MIT
URL:            http://luajit.org/
Source0:        http://luajit.org/download/LuaJIT-2.1.0-beta3.tar.gz

ExclusiveArch:  %{arm} %{ix86} x86_64 %{mips} aarch64

BuildRequires:  make

%description
LuaJIT is a Just-In-Time Compiler (JIT) for the Lua programming language. Lua is a powerful, dynamic and
light-weight programming language. It may be embedded or used as a general-purpose, stand-alone language.

%package        devel
Summary:        Development files for luajit
Requires:       luajit = 2.1.0-%{release}

%description    devel
This package contains development files for luajit.

%package        help
Summary: Documents for luajit

%description    help
Man pages and other related documents for luajit.

%prep
%autosetup -n LuaJIT-2.1.0-beta3 -p1

sed -i -e '/install -m/s/-m/-p -m/' Makefile

%build
%make_build amalg Q= E=@: PREFIX=%{_prefix} TARGET_STRIP=: \
           CFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}" \
           MULTILIB=%{_lib}

%install
%make_install PREFIX=%{_prefix} \
              MULTILIB=%{_lib}

rm -rf _tmp_html ; mkdir _tmp_html
cp -a doc _tmp_html/html
ln -s luajit-2.1.0-beta3 %{buildroot}%{_bindir}/luajit

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%doc README COPYRIGHT
%{_bindir}/%{name}
%{_bindir}/%{name}-2.1.0-beta3
%{_libdir}/lib%{name}-*.so.*
%{_datadir}/%{name}-2.1.0-beta3/

%files devel
%doc _tmp_html/html/
%{_includedir}/%{name}-%{apiver}/
%{_libdir}/lib%{name}-*.so
%{_libdir}/pkgconfig/%{name}.pc
%exclude %{_libdir}/*.a

%files help
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Mar 15 2020 zhangatao <zhangtao221@huawei.com> - 2.1.0-0.8beta3
- package init