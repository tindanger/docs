
module.exports = {
    encoding: "utf-8", // 强制所有输出文件使用 UTF-8
    markdown: {
      fileEncoding: "utf-8", // 单独指定 Markdown 编码
      chineseOptimization: true, // 启用中文字符特殊处理
      // 显式声明输入输出编码
      inputEncoding: 'UTF-8',
      outputEncoding: 'UTF-8//TRANSLIT', // 处理非常规字符
      // 禁用自动编码嗅探
      disableAutoDetect: true
    },
    // 兼容中文路径
    paths: {
      allowUnicode: true
    }
  }

