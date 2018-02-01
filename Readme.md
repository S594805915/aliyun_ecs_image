# 自动生成阿里云ECS基础镜像
使用packer基于阿里云ECS基础镜像烧制适合自己的基础镜像， 方便新建ECS instance

## 用法
1. 首先安装packer [https://www.packer.io/]
1. 在阿里云控制台生成securityID和securityKEY
2. 配置到环境变量, packer会从环境里读取ID+KEY,用于创建必要的资源
    ```
    export ALICLOUD_ACCESS_KEY=ALICLOUD_ACCESS_KEY
    export ALICLOUD_SECRET_KEY=ALICLOUD_SECRET_KEY
    export ALICLOUD_REGION=cn-shenzhen
    ```
3. 执行./build.sh，生成的image名格式[ubuntu16_04_YYYYmdHHMMSS]
4. 在阿里云控制台或者其他平台创建ECS，就可以使用这个image了


## 注意事项
1. file目录下的文件只是个例子，需要根据自己需求修改