---
layout: default
title: GaussianImage++: Boosted Image Representation and Compression with 2D Gaussian Splatting
---

# GaussianImage++: Boosted Image Representation and Compression with 2D Gaussian Splatting
**arXiv**：[2512.19108v1](https://arxiv.org/abs/2512.19108) · [PDF](https://arxiv.org/pdf/2512.19108.pdf)  
**作者**：Tiantian Li, Xinjie Zhang, Xingtong Ge, Tongda Xu, Dailan He, Jun Zhang, Yan Wang  

**一句话要点**：提出GaussianImage++以利用有限高斯基元提升图像表示与压缩性能

**关键词**：图像表示, 图像压缩, 高斯泼溅, 失真驱动密集化, 量化感知训练

## 3 点简述
- 核心问题：现有2D高斯泼溅方法需过多基元维持高保真度，导致效率低下
- 方法要点：引入失真驱动密集化机制和上下文感知高斯滤波器优化基元分配
- 实验或效果：在表示与压缩上优于GaussianImage和INRs-based COIN，保持实时解码和低内存

## 摘要（原文）

> Implicit neural representations (INRs) have achieved remarkable success in image representation and compression, but they require substantial training time and memory. Meanwhile, recent 2D Gaussian Splatting (GS) methods (\textit{e.g.}, GaussianImage) offer promising alternatives through efficient primitive-based rendering. However, these methods require excessive Gaussian primitives to maintain high visual fidelity. To exploit the potential of GS-based approaches, we present GaussianImage++, which utilizes limited Gaussian primitives to achieve impressive representation and compression performance. Firstly, we introduce a distortion-driven densification mechanism. It progressively allocates Gaussian primitives according to signal intensity. Secondly, we employ context-aware Gaussian filters for each primitive, which assist in the densification to optimize Gaussian primitives based on varying image content. Thirdly, we integrate attribute-separated learnable scalar quantizers and quantization-aware training, enabling efficient compression of primitive attributes. Experimental results demonstrate the effectiveness of our method. In particular, GaussianImage++ outperforms GaussianImage and INRs-based COIN in representation and compression performance while maintaining real-time decoding and low memory usage.

