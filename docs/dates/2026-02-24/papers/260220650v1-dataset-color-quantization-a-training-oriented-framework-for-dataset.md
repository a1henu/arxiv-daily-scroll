---
layout: default
title: Dataset Color Quantization: A Training-Oriented Framework for Dataset-Level Compression
---

# Dataset Color Quantization: A Training-Oriented Framework for Dataset-Level Compression
**arXiv**：[2602.20650v1](https://arxiv.org/abs/2602.20650) · [PDF](https://arxiv.org/pdf/2602.20650.pdf)  
**作者**：Chenyue Yu, Lingao Xiao, Jinhong Deng, Ivor W. Tsang, Yang He  

**一句话要点**：提出数据集颜色量化框架，通过压缩颜色空间冗余以降低存储需求并保持训练性能。

**关键词**：数据集压缩, 颜色量化, 模型训练, 存储优化, 图像处理

## 3 点简述
- 核心问题：大规模图像数据集存储需求高，现有方法忽略颜色空间冗余。
- 方法要点：统一框架减少颜色冗余，保持语义重要颜色和结构细节。
- 实验或效果：在多个数据集上验证，显著提升压缩下的训练性能。

## 摘要（原文）

> Large-scale image datasets are fundamental to deep learning, but their high storage demands pose challenges for deployment in resource-constrained environments. While existing approaches reduce dataset size by discarding samples, they often ignore the significant redundancy within each image -- particularly in the color space. To address this, we propose Dataset Color Quantization (DCQ), a unified framework that compresses visual datasets by reducing color-space redundancy while preserving information crucial for model training. DCQ achieves this by enforcing consistent palette representations across similar images, selectively retaining semantically important colors guided by model perception, and maintaining structural details necessary for effective feature learning. Extensive experiments across CIFAR-10, CIFAR-100, Tiny-ImageNet, and ImageNet-1K show that DCQ significantly improves training performance under aggressive compression, offering a scalable and robust solution for dataset-level storage reduction. Code is available at \href{https://github.com/he-y/Dataset-Color-Quantization}{https://github.com/he-y/Dataset-Color-Quantization}.

