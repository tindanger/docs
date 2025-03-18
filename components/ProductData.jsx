import { useEffect, useState } from 'react';

export function ProductData({ productCode, children }) {
  const [product, setProduct] = useState(null);

  useEffect(() => {
    fetch(`/api/products/${productCode}`)
      .then(res => res.json())
      .then(data => setProduct(data.data));
  }, [productCode]);

  if (!product) return null;
  
  return children(product);
}