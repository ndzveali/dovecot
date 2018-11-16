#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x18A348AEED409DA1 (dovecot-ce@dovecot.org)
#
Name     : dovecot
Version  : 2.3.3
Release  : 6
URL      : https://dovecot.org/releases/2.3/dovecot-2.3.3.tar.gz
Source0  : https://dovecot.org/releases/2.3/dovecot-2.3.3.tar.gz
Source1  : dovecot.service
Source2  : dovecot.tmpfiles
Source99 : https://dovecot.org/releases/2.3/dovecot-2.3.3.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1 MIT
Requires: dovecot-bin = %{version}-%{release}
Requires: dovecot-config = %{version}-%{release}
Requires: dovecot-data = %{version}-%{release}
Requires: dovecot-lib = %{version}-%{release}
Requires: dovecot-libexec = %{version}-%{release}
Requires: dovecot-license = %{version}-%{release}
Requires: dovecot-man = %{version}-%{release}
Requires: dovecot-services = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : bzip2-dev
BuildRequires : libcap-dev
BuildRequires : lz4-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : xz-dev
Patch1: include-crypt-h.patch

%description
INSTALLATION
See INSTALL.md file.
CONFIGURATION
See doc/documentation.txt or http://wiki2.dovecot.org/

%package bin
Summary: bin components for the dovecot package.
Group: Binaries
Requires: dovecot-data = %{version}-%{release}
Requires: dovecot-libexec = %{version}-%{release}
Requires: dovecot-config = %{version}-%{release}
Requires: dovecot-license = %{version}-%{release}
Requires: dovecot-man = %{version}-%{release}
Requires: dovecot-services = %{version}-%{release}

%description bin
bin components for the dovecot package.


%package config
Summary: config components for the dovecot package.
Group: Default

%description config
config components for the dovecot package.


%package data
Summary: data components for the dovecot package.
Group: Data

%description data
data components for the dovecot package.


%package dev
Summary: dev components for the dovecot package.
Group: Development
Requires: dovecot-lib = %{version}-%{release}
Requires: dovecot-bin = %{version}-%{release}
Requires: dovecot-data = %{version}-%{release}
Provides: dovecot-devel = %{version}-%{release}

%description dev
dev components for the dovecot package.


%package doc
Summary: doc components for the dovecot package.
Group: Documentation
Requires: dovecot-man = %{version}-%{release}

%description doc
doc components for the dovecot package.


%package lib
Summary: lib components for the dovecot package.
Group: Libraries
Requires: dovecot-data = %{version}-%{release}
Requires: dovecot-libexec = %{version}-%{release}
Requires: dovecot-license = %{version}-%{release}

%description lib
lib components for the dovecot package.


%package libexec
Summary: libexec components for the dovecot package.
Group: Default
Requires: dovecot-config = %{version}-%{release}
Requires: dovecot-license = %{version}-%{release}

%description libexec
libexec components for the dovecot package.


%package license
Summary: license components for the dovecot package.
Group: Default

%description license
license components for the dovecot package.


%package man
Summary: man components for the dovecot package.
Group: Default

%description man
man components for the dovecot package.


%package services
Summary: services components for the dovecot package.
Group: Systemd services

%description services
services components for the dovecot package.


%prep
%setup -q -n dovecot-2.3.3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542395091
export CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error   -Wl,-z,max-page-size=0x1000 -m64 -march=westmere -mtune=haswell"
export CXXFLAGS=$CFLAGS
unset LDFLAGS
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1542395091
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dovecot
cp COPYING %{buildroot}/usr/share/package-licenses/dovecot/COPYING
cp COPYING.LGPL %{buildroot}/usr/share/package-licenses/dovecot/COPYING.LGPL
cp COPYING.MIT %{buildroot}/usr/share/package-licenses/dovecot/COPYING.MIT
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/dovecot.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/tmpfiles.d/dovecot.conf

%files
%defattr(-,root,root,-)
/usr/lib64/dovecot/dovecot-config

%files bin
%defattr(-,root,root,-)
/usr/bin/doveadm
/usr/bin/doveconf
/usr/bin/dovecot
/usr/bin/dsync

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/dovecot.conf

%files data
%defattr(-,root,root,-)
/usr/share/dovecot/stopwords/stopwords_da.txt
/usr/share/dovecot/stopwords/stopwords_de.txt
/usr/share/dovecot/stopwords/stopwords_en.txt
/usr/share/dovecot/stopwords/stopwords_es.txt
/usr/share/dovecot/stopwords/stopwords_fi.txt
/usr/share/dovecot/stopwords/stopwords_fr.txt
/usr/share/dovecot/stopwords/stopwords_it.txt
/usr/share/dovecot/stopwords/stopwords_nl.txt
/usr/share/dovecot/stopwords/stopwords_no.txt
/usr/share/dovecot/stopwords/stopwords_pt.txt
/usr/share/dovecot/stopwords/stopwords_ro.txt
/usr/share/dovecot/stopwords/stopwords_ru.txt
/usr/share/dovecot/stopwords/stopwords_sv.txt

%files dev
%defattr(-,root,root,-)
/usr/include/dovecot/access-lookup.h
/usr/include/dovecot/acl-api-private.h
/usr/include/dovecot/acl-api.h
/usr/include/dovecot/acl-cache.h
/usr/include/dovecot/acl-global-file.h
/usr/include/dovecot/acl-lookup-dict.h
/usr/include/dovecot/acl-plugin.h
/usr/include/dovecot/acl-storage.h
/usr/include/dovecot/anvil-client.h
/usr/include/dovecot/aqueue.h
/usr/include/dovecot/array-decl.h
/usr/include/dovecot/array.h
/usr/include/dovecot/askpass.h
/usr/include/dovecot/auth-cache.h
/usr/include/dovecot/auth-client-connection.h
/usr/include/dovecot/auth-client-interface.h
/usr/include/dovecot/auth-client-private.h
/usr/include/dovecot/auth-client-request.h
/usr/include/dovecot/auth-client.h
/usr/include/dovecot/auth-common.h
/usr/include/dovecot/auth-fields.h
/usr/include/dovecot/auth-master-connection.h
/usr/include/dovecot/auth-master.h
/usr/include/dovecot/auth-penalty.h
/usr/include/dovecot/auth-policy.h
/usr/include/dovecot/auth-postfix-connection.h
/usr/include/dovecot/auth-request-handler.h
/usr/include/dovecot/auth-request-stats.h
/usr/include/dovecot/auth-request-var-expand.h
/usr/include/dovecot/auth-request.h
/usr/include/dovecot/auth-server-connection.h
/usr/include/dovecot/auth-settings.h
/usr/include/dovecot/auth-stats.h
/usr/include/dovecot/auth-token.h
/usr/include/dovecot/auth-worker-client.h
/usr/include/dovecot/auth-worker-server.h
/usr/include/dovecot/auth.h
/usr/include/dovecot/backtrace-string.h
/usr/include/dovecot/base32.h
/usr/include/dovecot/base64.h
/usr/include/dovecot/bits.h
/usr/include/dovecot/bloomfilter.h
/usr/include/dovecot/bsearch-insert-pos.h
/usr/include/dovecot/buffer.h
/usr/include/dovecot/byteorder.h
/usr/include/dovecot/charset-utf8-private.h
/usr/include/dovecot/charset-utf8.h
/usr/include/dovecot/child-wait.h
/usr/include/dovecot/client-common.h
/usr/include/dovecot/compat.h
/usr/include/dovecot/compression.h
/usr/include/dovecot/config-filter.h
/usr/include/dovecot/config-parser-private.h
/usr/include/dovecot/config-parser.h
/usr/include/dovecot/config-request.h
/usr/include/dovecot/config.h
/usr/include/dovecot/connection.h
/usr/include/dovecot/crc32.h
/usr/include/dovecot/cydir-storage.h
/usr/include/dovecot/cydir-sync.h
/usr/include/dovecot/data-stack.h
/usr/include/dovecot/db-checkpassword.h
/usr/include/dovecot/db-dict.h
/usr/include/dovecot/db-ldap.h
/usr/include/dovecot/db-oauth2.h
/usr/include/dovecot/db-passwd-file.h
/usr/include/dovecot/db-sql.h
/usr/include/dovecot/dbox-attachment.h
/usr/include/dovecot/dbox-file.h
/usr/include/dovecot/dbox-mail.h
/usr/include/dovecot/dbox-save.h
/usr/include/dovecot/dbox-storage.h
/usr/include/dovecot/dcrypt-iostream.h
/usr/include/dovecot/dcrypt-private.h
/usr/include/dovecot/dcrypt.h
/usr/include/dovecot/dict-client.h
/usr/include/dovecot/dict-private.h
/usr/include/dovecot/dict-transaction-memory.h
/usr/include/dovecot/dict.h
/usr/include/dovecot/dns-lookup.h
/usr/include/dovecot/dns-util.h
/usr/include/dovecot/doveadm-cmd.h
/usr/include/dovecot/doveadm-dsync.h
/usr/include/dovecot/doveadm-dump.h
/usr/include/dovecot/doveadm-mail-iter.h
/usr/include/dovecot/doveadm-mail.h
/usr/include/dovecot/doveadm-mailbox-list-iter.h
/usr/include/dovecot/doveadm-print-private.h
/usr/include/dovecot/doveadm-print.h
/usr/include/dovecot/doveadm-settings.h
/usr/include/dovecot/doveadm-util.h
/usr/include/dovecot/doveadm.h
/usr/include/dovecot/dovecot-version.h
/usr/include/dovecot/dsasl-client-private.h
/usr/include/dovecot/dsasl-client.h
/usr/include/dovecot/dsync-brain.h
/usr/include/dovecot/dsync-ibc.h
/usr/include/dovecot/eacces-error.h
/usr/include/dovecot/env-util.h
/usr/include/dovecot/event-filter.h
/usr/include/dovecot/event-log.h
/usr/include/dovecot/execv-const.h
/usr/include/dovecot/fail-mail-storage.h
/usr/include/dovecot/failures-private.h
/usr/include/dovecot/failures.h
/usr/include/dovecot/fd-util.h
/usr/include/dovecot/fdatasync-path.h
/usr/include/dovecot/fdpass.h
/usr/include/dovecot/file-cache.h
/usr/include/dovecot/file-copy.h
/usr/include/dovecot/file-create-locked.h
/usr/include/dovecot/file-dotlock.h
/usr/include/dovecot/file-lock.h
/usr/include/dovecot/file-set-size.h
/usr/include/dovecot/fs-api-private.h
/usr/include/dovecot/fs-api.h
/usr/include/dovecot/fs-sis-common.h
/usr/include/dovecot/fs-test.h
/usr/include/dovecot/fs-wrapper.h
/usr/include/dovecot/fsync-mode.h
/usr/include/dovecot/fts-api-private.h
/usr/include/dovecot/fts-api.h
/usr/include/dovecot/fts-common.h
/usr/include/dovecot/fts-expunge-log.h
/usr/include/dovecot/fts-filter-common.h
/usr/include/dovecot/fts-filter-private.h
/usr/include/dovecot/fts-filter.h
/usr/include/dovecot/fts-icu.h
/usr/include/dovecot/fts-indexer.h
/usr/include/dovecot/fts-language.h
/usr/include/dovecot/fts-library.h
/usr/include/dovecot/fts-parser.h
/usr/include/dovecot/fts-storage.h
/usr/include/dovecot/fts-tokenizer-common.h
/usr/include/dovecot/fts-tokenizer-generic-private.h
/usr/include/dovecot/fts-tokenizer-private.h
/usr/include/dovecot/fts-tokenizer.h
/usr/include/dovecot/fts-user.h
/usr/include/dovecot/guid.h
/usr/include/dovecot/hash-decl.h
/usr/include/dovecot/hash-format.h
/usr/include/dovecot/hash-method.h
/usr/include/dovecot/hash.h
/usr/include/dovecot/hash2.h
/usr/include/dovecot/hex-binary.h
/usr/include/dovecot/hex-dec.h
/usr/include/dovecot/hmac-cram-md5.h
/usr/include/dovecot/hmac.h
/usr/include/dovecot/home-expand.h
/usr/include/dovecot/hook-build.h
/usr/include/dovecot/hostpid.h
/usr/include/dovecot/http-auth.h
/usr/include/dovecot/http-client-private.h
/usr/include/dovecot/http-client.h
/usr/include/dovecot/http-common.h
/usr/include/dovecot/http-date.h
/usr/include/dovecot/http-header-parser.h
/usr/include/dovecot/http-header.h
/usr/include/dovecot/http-message-parser.h
/usr/include/dovecot/http-parser.h
/usr/include/dovecot/http-request-parser.h
/usr/include/dovecot/http-request.h
/usr/include/dovecot/http-response-parser.h
/usr/include/dovecot/http-response.h
/usr/include/dovecot/http-server-private.h
/usr/include/dovecot/http-server.h
/usr/include/dovecot/http-transfer.h
/usr/include/dovecot/http-url.h
/usr/include/dovecot/imap-arg.h
/usr/include/dovecot/imap-base-subject.h
/usr/include/dovecot/imap-bodystructure.h
/usr/include/dovecot/imap-client.h
/usr/include/dovecot/imap-commands-util.h
/usr/include/dovecot/imap-commands.h
/usr/include/dovecot/imap-common.h
/usr/include/dovecot/imap-date.h
/usr/include/dovecot/imap-envelope.h
/usr/include/dovecot/imap-expunge.h
/usr/include/dovecot/imap-fetch.h
/usr/include/dovecot/imap-id.h
/usr/include/dovecot/imap-keepalive.h
/usr/include/dovecot/imap-list.h
/usr/include/dovecot/imap-login-client.h
/usr/include/dovecot/imap-login-commands.h
/usr/include/dovecot/imap-login-settings.h
/usr/include/dovecot/imap-master-client.h
/usr/include/dovecot/imap-match.h
/usr/include/dovecot/imap-metadata.h
/usr/include/dovecot/imap-msgpart-url.h
/usr/include/dovecot/imap-msgpart.h
/usr/include/dovecot/imap-notify.h
/usr/include/dovecot/imap-parser.h
/usr/include/dovecot/imap-quote.h
/usr/include/dovecot/imap-resp-code.h
/usr/include/dovecot/imap-search-args.h
/usr/include/dovecot/imap-search.h
/usr/include/dovecot/imap-seqset.h
/usr/include/dovecot/imap-settings.h
/usr/include/dovecot/imap-state.h
/usr/include/dovecot/imap-status.h
/usr/include/dovecot/imap-sync-private.h
/usr/include/dovecot/imap-sync.h
/usr/include/dovecot/imap-url.h
/usr/include/dovecot/imap-urlauth-backend.h
/usr/include/dovecot/imap-urlauth-connection.h
/usr/include/dovecot/imap-urlauth-fetch.h
/usr/include/dovecot/imap-urlauth-private.h
/usr/include/dovecot/imap-urlauth.h
/usr/include/dovecot/imap-utf7.h
/usr/include/dovecot/imap-util.h
/usr/include/dovecot/imapc-client-private.h
/usr/include/dovecot/imapc-client.h
/usr/include/dovecot/imapc-connection.h
/usr/include/dovecot/imapc-list.h
/usr/include/dovecot/imapc-mail.h
/usr/include/dovecot/imapc-msgmap.h
/usr/include/dovecot/imapc-search.h
/usr/include/dovecot/imapc-settings.h
/usr/include/dovecot/imapc-storage.h
/usr/include/dovecot/imapc-sync.h
/usr/include/dovecot/imem.h
/usr/include/dovecot/index-attachment.h
/usr/include/dovecot/index-mail.h
/usr/include/dovecot/index-mailbox-size.h
/usr/include/dovecot/index-pop3-uidl.h
/usr/include/dovecot/index-rebuild.h
/usr/include/dovecot/index-search-private.h
/usr/include/dovecot/index-search-result.h
/usr/include/dovecot/index-sort-private.h
/usr/include/dovecot/index-sort.h
/usr/include/dovecot/index-storage.h
/usr/include/dovecot/index-sync-changes.h
/usr/include/dovecot/index-sync-private.h
/usr/include/dovecot/index-thread-private.h
/usr/include/dovecot/ioloop-iolist.h
/usr/include/dovecot/ioloop-notify-fd.h
/usr/include/dovecot/ioloop-private.h
/usr/include/dovecot/ioloop.h
/usr/include/dovecot/iostream-lz4.h
/usr/include/dovecot/iostream-openssl.h
/usr/include/dovecot/iostream-private.h
/usr/include/dovecot/iostream-proxy.h
/usr/include/dovecot/iostream-pump.h
/usr/include/dovecot/iostream-rawlog-private.h
/usr/include/dovecot/iostream-rawlog.h
/usr/include/dovecot/iostream-ssl-private.h
/usr/include/dovecot/iostream-ssl.h
/usr/include/dovecot/iostream-temp.h
/usr/include/dovecot/iostream.h
/usr/include/dovecot/ipc-client.h
/usr/include/dovecot/ipc-server.h
/usr/include/dovecot/ipwd.h
/usr/include/dovecot/iso8601-date.h
/usr/include/dovecot/istream-attachment-connector.h
/usr/include/dovecot/istream-attachment-extractor.h
/usr/include/dovecot/istream-base64.h
/usr/include/dovecot/istream-binary-converter.h
/usr/include/dovecot/istream-callback.h
/usr/include/dovecot/istream-chain.h
/usr/include/dovecot/istream-concat.h
/usr/include/dovecot/istream-crlf.h
/usr/include/dovecot/istream-decrypt.h
/usr/include/dovecot/istream-dot.h
/usr/include/dovecot/istream-failure-at.h
/usr/include/dovecot/istream-file-private.h
/usr/include/dovecot/istream-fs-file.h
/usr/include/dovecot/istream-fs-stats.h
/usr/include/dovecot/istream-hash.h
/usr/include/dovecot/istream-header-filter.h
/usr/include/dovecot/istream-jsonstr.h
/usr/include/dovecot/istream-mail.h
/usr/include/dovecot/istream-metawrap.h
/usr/include/dovecot/istream-multiplex.h
/usr/include/dovecot/istream-nonuls.h
/usr/include/dovecot/istream-private.h
/usr/include/dovecot/istream-qp.h
/usr/include/dovecot/istream-raw-mbox.h
/usr/include/dovecot/istream-rawlog.h
/usr/include/dovecot/istream-seekable.h
/usr/include/dovecot/istream-sized.h
/usr/include/dovecot/istream-tee.h
/usr/include/dovecot/istream-timeout.h
/usr/include/dovecot/istream-try.h
/usr/include/dovecot/istream-unix.h
/usr/include/dovecot/istream-zlib.h
/usr/include/dovecot/istream.h
/usr/include/dovecot/json-parser.h
/usr/include/dovecot/json-tree.h
/usr/include/dovecot/lda-settings.h
/usr/include/dovecot/lib-event-private.h
/usr/include/dovecot/lib-event.h
/usr/include/dovecot/lib-signals.h
/usr/include/dovecot/lib.h
/usr/include/dovecot/llist.h
/usr/include/dovecot/log-throttle.h
/usr/include/dovecot/login-common.h
/usr/include/dovecot/login-proxy-state.h
/usr/include/dovecot/login-proxy.h
/usr/include/dovecot/login-settings.h
/usr/include/dovecot/macros.h
/usr/include/dovecot/mail-autoexpunge.h
/usr/include/dovecot/mail-cache-private.h
/usr/include/dovecot/mail-cache.h
/usr/include/dovecot/mail-copy.h
/usr/include/dovecot/mail-deliver.h
/usr/include/dovecot/mail-duplicate.h
/usr/include/dovecot/mail-error.h
/usr/include/dovecot/mail-html2text.h
/usr/include/dovecot/mail-index-alloc-cache.h
/usr/include/dovecot/mail-index-modseq.h
/usr/include/dovecot/mail-index-private.h
/usr/include/dovecot/mail-index-strmap.h
/usr/include/dovecot/mail-index-sync-private.h
/usr/include/dovecot/mail-index-transaction-private.h
/usr/include/dovecot/mail-index-util.h
/usr/include/dovecot/mail-index-view-private.h
/usr/include/dovecot/mail-index.h
/usr/include/dovecot/mail-namespace.h
/usr/include/dovecot/mail-search-build.h
/usr/include/dovecot/mail-search-mime-build.h
/usr/include/dovecot/mail-search-mime-register.h
/usr/include/dovecot/mail-search-mime.h
/usr/include/dovecot/mail-search-parser-private.h
/usr/include/dovecot/mail-search-parser.h
/usr/include/dovecot/mail-search-register.h
/usr/include/dovecot/mail-search.h
/usr/include/dovecot/mail-send.h
/usr/include/dovecot/mail-storage-hooks.h
/usr/include/dovecot/mail-storage-private.h
/usr/include/dovecot/mail-storage-service.h
/usr/include/dovecot/mail-storage-settings.h
/usr/include/dovecot/mail-storage.h
/usr/include/dovecot/mail-thread.h
/usr/include/dovecot/mail-transaction-log-private.h
/usr/include/dovecot/mail-transaction-log-view-private.h
/usr/include/dovecot/mail-transaction-log.h
/usr/include/dovecot/mail-types.h
/usr/include/dovecot/mail-user-hash.h
/usr/include/dovecot/mail-user.h
/usr/include/dovecot/mailbox-attribute-internal.h
/usr/include/dovecot/mailbox-attribute-private.h
/usr/include/dovecot/mailbox-attribute.h
/usr/include/dovecot/mailbox-guid-cache.h
/usr/include/dovecot/mailbox-list-delete.h
/usr/include/dovecot/mailbox-list-fs.h
/usr/include/dovecot/mailbox-list-index-storage.h
/usr/include/dovecot/mailbox-list-index-sync.h
/usr/include/dovecot/mailbox-list-index.h
/usr/include/dovecot/mailbox-list-iter-private.h
/usr/include/dovecot/mailbox-list-iter.h
/usr/include/dovecot/mailbox-list-maildir.h
/usr/include/dovecot/mailbox-list-notify-tree.h
/usr/include/dovecot/mailbox-list-notify.h
/usr/include/dovecot/mailbox-list-private.h
/usr/include/dovecot/mailbox-list-subscriptions.h
/usr/include/dovecot/mailbox-list.h
/usr/include/dovecot/mailbox-log.h
/usr/include/dovecot/mailbox-recent-flags.h
/usr/include/dovecot/mailbox-search-result-private.h
/usr/include/dovecot/mailbox-tree.h
/usr/include/dovecot/mailbox-uidvalidity.h
/usr/include/dovecot/mailbox-watch.h
/usr/include/dovecot/maildir-filename-flags.h
/usr/include/dovecot/maildir-filename.h
/usr/include/dovecot/maildir-keywords.h
/usr/include/dovecot/maildir-settings.h
/usr/include/dovecot/maildir-storage.h
/usr/include/dovecot/maildir-sync.h
/usr/include/dovecot/maildir-uidlist.h
/usr/include/dovecot/malloc-overflow.h
/usr/include/dovecot/master-auth.h
/usr/include/dovecot/master-instance.h
/usr/include/dovecot/master-interface.h
/usr/include/dovecot/master-login-auth.h
/usr/include/dovecot/master-login.h
/usr/include/dovecot/master-service-private.h
/usr/include/dovecot/master-service-settings-cache.h
/usr/include/dovecot/master-service-settings.h
/usr/include/dovecot/master-service-ssl-settings.h
/usr/include/dovecot/master-service-ssl.h
/usr/include/dovecot/master-service.h
/usr/include/dovecot/mbox-file.h
/usr/include/dovecot/mbox-from.h
/usr/include/dovecot/mbox-lock.h
/usr/include/dovecot/mbox-md5.h
/usr/include/dovecot/mbox-settings.h
/usr/include/dovecot/mbox-storage.h
/usr/include/dovecot/mbox-sync-private.h
/usr/include/dovecot/md4.h
/usr/include/dovecot/md5.h
/usr/include/dovecot/mdbox-file.h
/usr/include/dovecot/mdbox-map-private.h
/usr/include/dovecot/mdbox-map.h
/usr/include/dovecot/mdbox-settings.h
/usr/include/dovecot/mdbox-storage-rebuild.h
/usr/include/dovecot/mdbox-storage.h
/usr/include/dovecot/mdbox-sync.h
/usr/include/dovecot/mech-otp-skey-common.h
/usr/include/dovecot/mech-plain-common.h
/usr/include/dovecot/mech.h
/usr/include/dovecot/memarea.h
/usr/include/dovecot/mempool.h
/usr/include/dovecot/message-address.h
/usr/include/dovecot/message-binary-part.h
/usr/include/dovecot/message-date.h
/usr/include/dovecot/message-decoder.h
/usr/include/dovecot/message-header-decode.h
/usr/include/dovecot/message-header-encode.h
/usr/include/dovecot/message-header-hash.h
/usr/include/dovecot/message-header-parser.h
/usr/include/dovecot/message-id.h
/usr/include/dovecot/message-parser.h
/usr/include/dovecot/message-part-data.h
/usr/include/dovecot/message-part-serialize.h
/usr/include/dovecot/message-part.h
/usr/include/dovecot/message-search.h
/usr/include/dovecot/message-size.h
/usr/include/dovecot/message-snippet.h
/usr/include/dovecot/mkdir-parents.h
/usr/include/dovecot/mmap-util.h
/usr/include/dovecot/module-context.h
/usr/include/dovecot/module-dir.h
/usr/include/dovecot/mountpoint.h
/usr/include/dovecot/murmurhash3.h
/usr/include/dovecot/mycrypt.h
/usr/include/dovecot/net.h
/usr/include/dovecot/nfs-workarounds.h
/usr/include/dovecot/notify-plugin-private.h
/usr/include/dovecot/notify-plugin.h
/usr/include/dovecot/numpack.h
/usr/include/dovecot/oauth2.h
/usr/include/dovecot/ostream-cmp.h
/usr/include/dovecot/ostream-dot.h
/usr/include/dovecot/ostream-encrypt.h
/usr/include/dovecot/ostream-failure-at.h
/usr/include/dovecot/ostream-file-private.h
/usr/include/dovecot/ostream-hash.h
/usr/include/dovecot/ostream-metawrap.h
/usr/include/dovecot/ostream-multiplex.h
/usr/include/dovecot/ostream-null.h
/usr/include/dovecot/ostream-private.h
/usr/include/dovecot/ostream-rawlog.h
/usr/include/dovecot/ostream-unix.h
/usr/include/dovecot/ostream-zlib.h
/usr/include/dovecot/ostream.h
/usr/include/dovecot/passdb-blocking.h
/usr/include/dovecot/passdb-cache.h
/usr/include/dovecot/passdb-template.h
/usr/include/dovecot/passdb.h
/usr/include/dovecot/password-scheme.h
/usr/include/dovecot/path-util.h
/usr/include/dovecot/pkcs5.h
/usr/include/dovecot/pop3-capability.h
/usr/include/dovecot/pop3-client.h
/usr/include/dovecot/pop3-commands.h
/usr/include/dovecot/pop3-common.h
/usr/include/dovecot/pop3-settings.h
/usr/include/dovecot/pop3c-client.h
/usr/include/dovecot/pop3c-settings.h
/usr/include/dovecot/pop3c-storage.h
/usr/include/dovecot/pop3c-sync.h
/usr/include/dovecot/primes.h
/usr/include/dovecot/printf-format-fix.h
/usr/include/dovecot/priorityq.h
/usr/include/dovecot/process-title.h
/usr/include/dovecot/program-client.h
/usr/include/dovecot/push-notification-drivers.h
/usr/include/dovecot/push-notification-event-flagsclear.h
/usr/include/dovecot/push-notification-event-flagsset.h
/usr/include/dovecot/push-notification-event-mailboxcreate.h
/usr/include/dovecot/push-notification-event-mailboxdelete.h
/usr/include/dovecot/push-notification-event-mailboxrename.h
/usr/include/dovecot/push-notification-event-mailboxsubscribe.h
/usr/include/dovecot/push-notification-event-mailboxunsubscribe.h
/usr/include/dovecot/push-notification-event-message-common.h
/usr/include/dovecot/push-notification-event-messageappend.h
/usr/include/dovecot/push-notification-event-messageexpunge.h
/usr/include/dovecot/push-notification-event-messagenew.h
/usr/include/dovecot/push-notification-event-messageread.h
/usr/include/dovecot/push-notification-event-messagetrash.h
/usr/include/dovecot/push-notification-events-rfc5423.h
/usr/include/dovecot/push-notification-events.h
/usr/include/dovecot/push-notification-plugin.h
/usr/include/dovecot/push-notification-triggers.h
/usr/include/dovecot/push-notification-txn-mbox.h
/usr/include/dovecot/push-notification-txn-msg.h
/usr/include/dovecot/qp-decoder.h
/usr/include/dovecot/qp-encoder.h
/usr/include/dovecot/quota-fs.h
/usr/include/dovecot/quota-plugin.h
/usr/include/dovecot/quota-private.h
/usr/include/dovecot/quota.h
/usr/include/dovecot/quoted-printable.h
/usr/include/dovecot/randgen.h
/usr/include/dovecot/raw-storage.h
/usr/include/dovecot/raw-sync.h
/usr/include/dovecot/read-full.h
/usr/include/dovecot/restrict-access.h
/usr/include/dovecot/restrict-process-size.h
/usr/include/dovecot/rfc2231-parser.h
/usr/include/dovecot/rfc822-parser.h
/usr/include/dovecot/safe-memset.h
/usr/include/dovecot/safe-mkdir.h
/usr/include/dovecot/safe-mkstemp.h
/usr/include/dovecot/sasl-server.h
/usr/include/dovecot/sdbox-file.h
/usr/include/dovecot/sdbox-storage.h
/usr/include/dovecot/sdbox-sync.h
/usr/include/dovecot/sendfile-util.h
/usr/include/dovecot/seq-range-array.h
/usr/include/dovecot/service-settings.h
/usr/include/dovecot/settings-parser.h
/usr/include/dovecot/settings.h
/usr/include/dovecot/sha-common.h
/usr/include/dovecot/sha1.h
/usr/include/dovecot/sha2.h
/usr/include/dovecot/sha3.h
/usr/include/dovecot/shared-storage.h
/usr/include/dovecot/smtp-address.h
/usr/include/dovecot/smtp-client-command.h
/usr/include/dovecot/smtp-client-connection.h
/usr/include/dovecot/smtp-client-private.h
/usr/include/dovecot/smtp-client-transaction.h
/usr/include/dovecot/smtp-client.h
/usr/include/dovecot/smtp-command-parser.h
/usr/include/dovecot/smtp-command.h
/usr/include/dovecot/smtp-common.h
/usr/include/dovecot/smtp-params.h
/usr/include/dovecot/smtp-parser.h
/usr/include/dovecot/smtp-reply-parser.h
/usr/include/dovecot/smtp-reply.h
/usr/include/dovecot/smtp-server-private.h
/usr/include/dovecot/smtp-server.h
/usr/include/dovecot/smtp-submit-settings.h
/usr/include/dovecot/smtp-submit.h
/usr/include/dovecot/smtp-syntax.h
/usr/include/dovecot/sort.h
/usr/include/dovecot/sql-api-private.h
/usr/include/dovecot/sql-api.h
/usr/include/dovecot/sql-db-cache.h
/usr/include/dovecot/stats-client.h
/usr/include/dovecot/stats-connection.h
/usr/include/dovecot/stats-dist.h
/usr/include/dovecot/stats-parser.h
/usr/include/dovecot/stats.h
/usr/include/dovecot/str-find.h
/usr/include/dovecot/str-sanitize.h
/usr/include/dovecot/str-table.h
/usr/include/dovecot/str.h
/usr/include/dovecot/strescape.h
/usr/include/dovecot/strfuncs.h
/usr/include/dovecot/strnum.h
/usr/include/dovecot/subscription-file.h
/usr/include/dovecot/syslog-util.h
/usr/include/dovecot/test-common.h
/usr/include/dovecot/time-util.h
/usr/include/dovecot/unichar.h
/usr/include/dovecot/unix-socket-create.h
/usr/include/dovecot/unlink-directory.h
/usr/include/dovecot/unlink-old-files.h
/usr/include/dovecot/uri-util.h
/usr/include/dovecot/userdb-blocking.h
/usr/include/dovecot/userdb-template.h
/usr/include/dovecot/userdb-vpopmail.h
/usr/include/dovecot/userdb.h
/usr/include/dovecot/utc-mktime.h
/usr/include/dovecot/utc-offset.h
/usr/include/dovecot/var-expand-private.h
/usr/include/dovecot/var-expand.h
/usr/include/dovecot/wildcard-match.h
/usr/include/dovecot/write-full.h
/usr/share/aclocal/*.m4

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/dovecot/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/dovecot/auth/lib20_auth_var_expand_crypt.so
/usr/lib64/dovecot/auth/libauthdb_imap.so
/usr/lib64/dovecot/doveadm/lib10_doveadm_acl_plugin.so
/usr/lib64/dovecot/doveadm/lib10_doveadm_expire_plugin.so
/usr/lib64/dovecot/doveadm/lib10_doveadm_quota_plugin.so
/usr/lib64/dovecot/doveadm/lib20_doveadm_fts_plugin.so
/usr/lib64/dovecot/doveadm/libdoveadm_mail_crypt_plugin.so
/usr/lib64/dovecot/lib01_acl_plugin.so
/usr/lib64/dovecot/lib02_imap_acl_plugin.so
/usr/lib64/dovecot/lib02_lazy_expunge_plugin.so
/usr/lib64/dovecot/lib05_mail_crypt_acl_plugin.so
/usr/lib64/dovecot/lib05_pop3_migration_plugin.so
/usr/lib64/dovecot/lib05_snarf_plugin.so
/usr/lib64/dovecot/lib10_last_login_plugin.so
/usr/lib64/dovecot/lib10_mail_crypt_plugin.so
/usr/lib64/dovecot/lib10_mail_filter_plugin.so
/usr/lib64/dovecot/lib10_quota_plugin.so
/usr/lib64/dovecot/lib11_imap_quota_plugin.so
/usr/lib64/dovecot/lib11_trash_plugin.so
/usr/lib64/dovecot/lib15_notify_plugin.so
/usr/lib64/dovecot/lib20_autocreate_plugin.so
/usr/lib64/dovecot/lib20_charset_alias_plugin.so
/usr/lib64/dovecot/lib20_expire_plugin.so
/usr/lib64/dovecot/lib20_fts_plugin.so
/usr/lib64/dovecot/lib20_listescape_plugin.so
/usr/lib64/dovecot/lib20_mail_log_plugin.so
/usr/lib64/dovecot/lib20_mailbox_alias_plugin.so
/usr/lib64/dovecot/lib20_notify_status_plugin.so
/usr/lib64/dovecot/lib20_push_notification_plugin.so
/usr/lib64/dovecot/lib20_quota_clone_plugin.so
/usr/lib64/dovecot/lib20_replication_plugin.so
/usr/lib64/dovecot/lib20_var_expand_crypt.so
/usr/lib64/dovecot/lib20_virtual_plugin.so
/usr/lib64/dovecot/lib20_zlib_plugin.so
/usr/lib64/dovecot/lib21_fts_squat_plugin.so
/usr/lib64/dovecot/lib30_imap_zlib_plugin.so
/usr/lib64/dovecot/lib90_old_stats_plugin.so
/usr/lib64/dovecot/lib95_imap_old_stats_plugin.so
/usr/lib64/dovecot/lib99_welcome_plugin.so
/usr/lib64/dovecot/libdcrypt_openssl.so
/usr/lib64/dovecot/libdovecot-compression.so
/usr/lib64/dovecot/libdovecot-compression.so.0
/usr/lib64/dovecot/libdovecot-compression.so.0.0.0
/usr/lib64/dovecot/libdovecot-dsync.so
/usr/lib64/dovecot/libdovecot-dsync.so.0
/usr/lib64/dovecot/libdovecot-dsync.so.0.0.0
/usr/lib64/dovecot/libdovecot-fts.so
/usr/lib64/dovecot/libdovecot-fts.so.0
/usr/lib64/dovecot/libdovecot-fts.so.0.0.0
/usr/lib64/dovecot/libdovecot-lda.so
/usr/lib64/dovecot/libdovecot-lda.so.0
/usr/lib64/dovecot/libdovecot-lda.so.0.0.0
/usr/lib64/dovecot/libdovecot-login.so
/usr/lib64/dovecot/libdovecot-login.so.0
/usr/lib64/dovecot/libdovecot-login.so.0.0.0
/usr/lib64/dovecot/libdovecot-sql.so
/usr/lib64/dovecot/libdovecot-sql.so.0
/usr/lib64/dovecot/libdovecot-sql.so.0.0.0
/usr/lib64/dovecot/libdovecot-storage.so
/usr/lib64/dovecot/libdovecot-storage.so.0
/usr/lib64/dovecot/libdovecot-storage.so.0.0.0
/usr/lib64/dovecot/libdovecot.so
/usr/lib64/dovecot/libdovecot.so.0
/usr/lib64/dovecot/libdovecot.so.0.0.0
/usr/lib64/dovecot/libfs_compress.so
/usr/lib64/dovecot/libfs_crypt.so
/usr/lib64/dovecot/libfs_mail_crypt.so
/usr/lib64/dovecot/libssl_iostream_openssl.so
/usr/lib64/dovecot/old-stats/libold_stats_mail.so
/usr/lib64/dovecot/old-stats/libstats_auth.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/dovecot/aggregator
/usr/libexec/dovecot/anvil
/usr/libexec/dovecot/auth
/usr/libexec/dovecot/checkpassword-reply
/usr/libexec/dovecot/config
/usr/libexec/dovecot/decode2text.sh
/usr/libexec/dovecot/deliver
/usr/libexec/dovecot/dict
/usr/libexec/dovecot/director
/usr/libexec/dovecot/dns-client
/usr/libexec/dovecot/doveadm-server
/usr/libexec/dovecot/dovecot-lda
/usr/libexec/dovecot/gdbhelper
/usr/libexec/dovecot/imap
/usr/libexec/dovecot/imap-hibernate
/usr/libexec/dovecot/imap-login
/usr/libexec/dovecot/imap-urlauth
/usr/libexec/dovecot/imap-urlauth-login
/usr/libexec/dovecot/imap-urlauth-worker
/usr/libexec/dovecot/indexer
/usr/libexec/dovecot/indexer-worker
/usr/libexec/dovecot/ipc
/usr/libexec/dovecot/lmtp
/usr/libexec/dovecot/log
/usr/libexec/dovecot/maildirlock
/usr/libexec/dovecot/old-stats
/usr/libexec/dovecot/pop3
/usr/libexec/dovecot/pop3-login
/usr/libexec/dovecot/quota-status
/usr/libexec/dovecot/rawlog
/usr/libexec/dovecot/replicator
/usr/libexec/dovecot/script
/usr/libexec/dovecot/script-login
/usr/libexec/dovecot/stats
/usr/libexec/dovecot/submission
/usr/libexec/dovecot/submission-login
/usr/libexec/dovecot/xml2text

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dovecot/COPYING
/usr/share/package-licenses/dovecot/COPYING.LGPL
/usr/share/package-licenses/dovecot/COPYING.MIT

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/deliver.1
/usr/share/man/man1/doveadm-acl.1
/usr/share/man/man1/doveadm-altmove.1
/usr/share/man/man1/doveadm-auth.1
/usr/share/man/man1/doveadm-backup.1
/usr/share/man/man1/doveadm-batch.1
/usr/share/man/man1/doveadm-config.1
/usr/share/man/man1/doveadm-copy.1
/usr/share/man/man1/doveadm-deduplicate.1
/usr/share/man/man1/doveadm-director.1
/usr/share/man/man1/doveadm-dump.1
/usr/share/man/man1/doveadm-exec.1
/usr/share/man/man1/doveadm-expunge.1
/usr/share/man/man1/doveadm-fetch.1
/usr/share/man/man1/doveadm-flags.1
/usr/share/man/man1/doveadm-force-resync.1
/usr/share/man/man1/doveadm-fs.1
/usr/share/man/man1/doveadm-fts.1
/usr/share/man/man1/doveadm-help.1
/usr/share/man/man1/doveadm-import.1
/usr/share/man/man1/doveadm-index.1
/usr/share/man/man1/doveadm-instance.1
/usr/share/man/man1/doveadm-kick.1
/usr/share/man/man1/doveadm-log.1
/usr/share/man/man1/doveadm-mailbox-cryptokey.1
/usr/share/man/man1/doveadm-mailbox.1
/usr/share/man/man1/doveadm-move.1
/usr/share/man/man1/doveadm-penalty.1
/usr/share/man/man1/doveadm-proxy.1
/usr/share/man/man1/doveadm-purge.1
/usr/share/man/man1/doveadm-pw.1
/usr/share/man/man1/doveadm-quota.1
/usr/share/man/man1/doveadm-rebuild.1
/usr/share/man/man1/doveadm-reload.1
/usr/share/man/man1/doveadm-replicator.1
/usr/share/man/man1/doveadm-save.1
/usr/share/man/man1/doveadm-search.1
/usr/share/man/man1/doveadm-stats.1
/usr/share/man/man1/doveadm-stop.1
/usr/share/man/man1/doveadm-sync.1
/usr/share/man/man1/doveadm-user.1
/usr/share/man/man1/doveadm-who.1
/usr/share/man/man1/doveadm.1
/usr/share/man/man1/doveconf.1
/usr/share/man/man1/dovecot-lda.1
/usr/share/man/man1/dovecot.1
/usr/share/man/man1/dsync.1
/usr/share/man/man7/doveadm-search-query.7

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/dovecot.service
