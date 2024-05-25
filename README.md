# Bài tập lớn giữa kỳ chương trình VDT 2024 lĩnh vực Cloud

## Phát triển một 3-tier web application đơn giản 
[Source Code](https://github.com/realhugn/VDT_project)
### API
#### Enpoint
- `GET /users/` : Get All Users
- `GET /users/{id}`: Get An User
- `POST /users/` : Create User
- `PUT /users/{id}`: Update User
- `DELETE /users/{id}`: Delete User
</br>
![alt text](image/image.png)

#### Unit Test
![alt text](image/image3.png)

#### Pull Request
![alt text](image/image2.png)
### DB
- Postgres
### Web
- React
![alt text](image/image1.png)

## Triển khai web application sử dụng các DevOps tools & practices

1. <b>Containerization</b>
</br>
File Dockerfile cho từng dịch vụ:
- [web](web/Dockerfile)
- [db](db/Dockerfile)
- [api](api/fastapi_service/Dockerfile)

</br>
Output câu lệnh build và thông tin docker history của từng image
![alt text](image/image4.png)
<div align="center">
  <i>Pic. 1 - Postgres image docker history</i>
</div>

![alt text](image/image5.png)
<div align="center">
  <i>Pic. 2 - Web image docker history</i>
</div>

![alt text](image/image6.png)
<div align="center">
  <i>Pic. 3 - Api image docker history</i>
</div>

2. <b>Continuous Integration</b>
</br>

- [File setup công cụ CI ](.github/workflows)
- Output log của luồng CI

![alt text](image/image7.png)

- Các hình ảnh demo khác

![alt text](image/image8.png)

![alt text](image/image9.png)
