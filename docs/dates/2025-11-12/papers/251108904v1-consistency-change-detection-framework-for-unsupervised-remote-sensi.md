---
layout: default
title: Consistency Change Detection Framework for Unsupervised Remote Sensing Change Detection
---

# Consistency Change Detection Framework for Unsupervised Remote Sensing Change Detection
**arXiv**：[2511.08904v1](https://arxiv.org/abs/2511.08904) · [PDF](https://arxiv.org/pdf/2511.08904.pdf)  
**作者**：Yating Liu, Yan Lu  

**一句话要点**：提出一致性变化检测框架以解决无监督遥感变化检测中生成器过拟合问题

**关键词**：无监督变化检测, 遥感图像, 生成器网络, 循环一致性, 语义一致性, 变化检测框架

## 3 点简述
- 核心问题：无监督遥感变化检测中生成器过拟合导致性能不佳
- 方法要点：引入循环一致性模块和语义一致性模块减少过拟合并实现细节重建
- 实验或效果：广泛实验表明方法优于其他先进方法

## 摘要（原文）

> Unsupervised remote sensing change detection aims to monitor and analyze changes from multi-temporal remote sensing images in the same geometric region at different times, without the need for labeled training data. Previous unsupervised methods attempt to achieve style transfer across multi-temporal remote sensing images through reconstruction by a generator network, and then capture the unreconstructable areas as the changed regions. However, it often leads to poor performance due to generator overfitting. In this paper, we propose a novel Consistency Change Detection Framework (CCDF) to address this challenge. Specifically, we introduce a Cycle Consistency (CC) module to reduce the overfitting issues in the generator-based reconstruction. Additionally, we propose a Semantic Consistency (SC) module to enable detail reconstruction. Extensive experiments demonstrate that our method outperforms other state-of-the-art approaches.

