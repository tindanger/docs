# 聚千保平台文档中心

本仓库包含聚千保平台的所有文档，包括：

* 用户指南
* 产品文档
* API 文档
* 系统功能说明
* 条款与协议

### 本地开发

1. 安装 Mintlify CLI：

```bash
npm i -g mintlify
```

2. 在文档根目录（docs.json 所在目录）运行：

```bash
mintlify dev
```

3. 在浏览器打开 http://localhost:3000 预览文档

### 文档结构

```
docs/
├── UserGuide/          # 用户指南
├── ProductDocumentation/   # 产品文档
├── SystemFeatures/     # 系统功能
├── api/               # API文档
├── Terms/             # 条款协议
└── FAQ/               # 常见问题
```

### 注意事项

1. 所有文档必须使用 UTF-8 编码
2. 图片请放在 public/images 目录下
3. API 示例代码请放在 api/examples 目录下
4. 产品数据模型请放在 api/schemas 目录下


需要我进一步调整吗？