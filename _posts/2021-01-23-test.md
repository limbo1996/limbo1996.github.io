 ---
 layout: post
 title: Gsutil下载Google Cloud data
 ---

## Gsutil安装

[文档](https://cloud.google.com/storage/docs/gsutil_install)



需要Python3(3.5-3.8)或者Python2（2.7.9以上）



```shell
wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-320.0.0-linux-x86_64.tar.gz
```

下载后解压

之后运行脚本

```shell
./google-cloud-sdk/install.sh
```

然后初始化

```shell
./google-cloud-sdk/bin/gcloud init
```

重启shell即完成安装

## 数据下载

主要命令是`gsutil cp`



以人类参考基因组数据等为例

文件在(https://console.cloud.google.com/storage/browser/genomics-public-data/resources/broad/hg38/v0)



### 下载命令

```
gsutil cp gs://BUCKET_NAME/OBJECT_NAME SAVE_TO_LOCATION
```

其中：

- `BUCKET_NAME` 是包含要下载的对象的存储分区名称，例如 `my-bucket`。
- `OBJECT_NAME` 是要下载的对象的名称，例如 `pets/dog.png`。
- `SAVE_TO_LOCATION` 是保存对象的本地路径，例如 `Desktop/Images`。



例如

```shell
gsutil cp gs://genomics-publicdata/resources/broad/hg38/v0/Homo_sapiens_assembly38.fasta .
```

下载整个目录加上参数`-r`.