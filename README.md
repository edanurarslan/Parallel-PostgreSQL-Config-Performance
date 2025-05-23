## ENG - **PostgreSQL Configuration Performance Comparison**

###  Project Description

This project compares the performance of PostgreSQL under properly and improperly configured environments. Two identical Ubuntu virtual machines were set up with PostgreSQL. While Server A was tuned with optimal configuration parameters, Server B was intentionally misconfigured to simulate poor performance.

###  Tests Performed

* Execution time measurements of basic SQL queries
* Monitoring of system resource usage (`top`, `htop`)
* Sequential and parallel query tests using Python (`concurrent.futures`)

###  Technologies Used

* PostgreSQL 14
* Python 3 (`psycopg2`, `faker`)
* Ubuntu 22.04 LTS
* Oracle VirtualBox

###  Contents

* `create_data.py`: Loads 10 million rows of fake user data
* `sequential_test.py`: Sequential query performance test
* `parallel_test.py`: Parallel query performance test

---

## TR - **PostgreSQL Yapılandırma Performans Karşılaştırması**

###  Proje Açıklaması

Bu projede, PostgreSQL veritabanı yönetim sisteminin doğru ve yanlış yapılandırmalar altında gösterdiği performans karşılaştırmalı olarak analiz edilmiştir. Aynı donanım kaynaklarına sahip iki ayrı sanal Ubuntu sunucusunda PostgreSQL kurulmuş ve yapılandırılmıştır. Sunucu A, sistem kaynaklarına uygun şekilde optimize edilirken; Sunucu B kasıtlı olarak hatalı parametrelerle yapılandırılmıştır.

###  Yapılan Testler

* Temel SQL sorgularının süre ölçümleri
* Sistem kaynak kullanımı takibi (`top`, `htop`)
* Python ile sıralı ve paralel sorgu performans testi (`concurrent.futures`)

###  Kullanılan Teknolojiler

* PostgreSQL 14
* Python 3 (`psycopg2`, `faker`)
* Ubuntu 22.04 LTS
* Oracle VirtualBox

###  İçerik

* `create_data.py`: 10 milyon sahte veriyi PostgreSQL'e yükler
* `sequential_test.py`: Sıralı sorgu testi
* `parallel_test.py`: Paralel sorgu testi
