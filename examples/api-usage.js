// 获取产品信息
async function getProductInfo(productCode) {
  try {
    const response = await fetch(`/api/products/${productCode}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    });
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('获取产品信息失败:', error);
  }
}

// 更新产品信息
async function updateProduct(productData) {
  try {
    const response = await fetch('/api/products', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(productData)
    });
    const result = await response.json();
    return result;
  } catch (error) {
    console.error('更新产品信息失败:', error);
  }
}

// 使用示例
const displayProduct = async () => {
  const product = await getProductInfo('LB-GZ-BJ-2024');
  if (product) {
    // 渲染产品基本信息
    document.getElementById('productName').textContent = product.basicInfo.productName;
    document.getElementById('productDesc').textContent = product.basicInfo.description;
    
    // 渲染保障责任
    const coverageList = product.coverage.mainCoverage.map(item => `
      <li>
        <h3>${item.name}</h3>
        <p>保额：${item.amount}</p>
        <p>说明：${item.description}</p>
      </li>
    `).join('');
    document.getElementById('coverageList').innerHTML = coverageList;
  }
};