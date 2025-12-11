---
layout: default
title: MODA: The First Challenging Benchmark for Multispectral Object Detection in Aerial Images
---

# MODA: The First Challenging Benchmark for Multispectral Object Detection in Aerial Images
**arXiv**：[2512.09489v1](https://arxiv.org/abs/2512.09489) · [PDF](https://arxiv.org/pdf/2512.09489.pdf)  
**作者**：Shuaihao Han, Tingfa Xu, Peifu Liu, Jianan Li  

**一句话要点**：提出MODA数据集和OSSDet框架以解决航空图像中多光谱目标检测的数据缺乏与性能挑战

**关键词**：多光谱目标检测, 航空图像, 数据集构建, 光谱-空间融合, 对象感知学习

## 3 点简述
- 核心问题：航空目标检测面临小目标和背景干扰，RGB图像信息不足，且缺乏多光谱训练数据。
- 方法要点：引入大规模MODA数据集，并提出OSSDet框架，通过光谱-空间调制、光谱相似性聚合和对象感知掩码优化检测。
- 实验或效果：OSSDet在参数和效率可比情况下优于现有方法，验证了多光谱数据的潜力。

## 摘要（原文）

> Aerial object detection faces significant challenges in real-world scenarios, such as small objects and extensive background interference, which limit the performance of RGB-based detectors with insufficient discriminative information. Multispectral images (MSIs) capture additional spectral cues across multiple bands, offering a promising alternative. However, the lack of training data has been the primary bottleneck to exploiting the potential of MSIs. To address this gap, we introduce the first large-scale dataset for Multispectral Object Detection in Aerial images (MODA), which comprises 14,041 MSIs and 330,191 annotations across diverse, challenging scenarios, providing a comprehensive data foundation for this field. Furthermore, to overcome challenges inherent to aerial object detection using MSIs, we propose OSSDet, a framework that integrates spectral and spatial information with object-aware cues. OSSDet employs a cascaded spectral-spatial modulation structure to optimize target perception, aggregates spectrally related features by exploiting spectral similarities to reinforce intra-object correlations, and suppresses irrelevant background via object-aware masking. Moreover, cross-spectral attention further refines object-related representations under explicit object-aware guidance. Extensive experiments demonstrate that OSSDet outperforms existing methods with comparable parameters and efficiency.

