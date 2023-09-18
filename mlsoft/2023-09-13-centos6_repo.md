
# 32Bit

```
yum clean all
touch /var/cache/yum/i386/6/base/mirrorlist.txt
echo "https://vault.centos.org/6.10/os/i386/" > /var/cache/yum/i386/6/base/mirrorlist.txt
echo "http://vault.centos.org/6.10/extras/i386/" > /var/cache/yum/i386/6/extras/mirrorlist.txt
echo "http://vault.centos.org/6.10/updates/i386/" > /var/cache/yum/i386/6/updates/mirrorlist.txt
```


---

# 64Bit

```
yum clean all
echo "https://vault.centos.org/6.10/os/x86_64/" > /var/cache/yum/x86_64/6/base/mirrorlist.txt
echo "http://vault.centos.org/6.10/extras/x86_64/" > /var/cache/yum/x86_64/6/extras/mirrorlist.txt
echo "http://vault.centos.org/6.10/updates/x86_64/" > /var/cache/yum/x86_64/6/updates/mirrorlist.txt
```
