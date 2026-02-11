---
layout: default
title: WildCat: Near-Linear Attention in Theory and Practice
---

# WildCat: Near-Linear Attention in Theory and Practice
**arXiv**：[2602.10056v1](https://arxiv.org/abs/2602.10056) · [PDF](https://arxiv.org/pdf/2602.10056.pdf)  
**作者**：Tobias Schröder, Lester Mackey  

**一句话要点**：提出WildCat方法，通过加权核心集实现近线性注意力，解决注意力机制二次方计算成本问题。

**关键词**：注意力机制压缩, 近线性计算, 核心集选择, 随机枢轴Cholesky, 图像生成, KV缓存压缩

## 3 点简述
- 注意力机制因输入序列长度二次方计算成本而部署昂贵，是核心问题。
- WildCat使用随机枢轴Cholesky算法选择核心集并优化权重，以最小化重构误差。
- 实验在图像生成、分类和语言模型KV缓存压缩中验证了WildCat的高精度和低开销。

## 摘要（原文）

> We introduce WildCat, a high-accuracy, low-cost approach to compressing the attention mechanism in neural networks. While attention is a staple of modern network architectures, it is also notoriously expensive to deploy due to resource requirements that scale quadratically with the input sequence length $n$. WildCat avoids these quadratic costs by only attending over a small weighted coreset. Crucially, we select the coreset using a fast but spectrally-accurate subsampling algorithm -- randomly pivoted Cholesky -- and weight the elements optimally to minimise reconstruction error. Remarkably, given bounded inputs, WildCat approximates exact attention with super-polynomial $O(n^{-\sqrt{\log(\log(n))}})$ error decay while running in near-linear $O(n^{1+o(1)})$ time. In contrast, prior practical approximations either lack error guarantees or require quadratic runtime to guarantee such high fidelity. We couple this advance with a GPU-optimized PyTorch implementation and a suite of benchmark experiments demonstrating the benefits of WildCat for image generation, image classification, and language model KV cache compression.

