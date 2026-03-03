---
layout: default
title: Towards Principled Dataset Distillation: A Spectral Distribution Perspective
---

# Towards Principled Dataset Distillation: A Spectral Distribution Perspective
**arXiv**：[2603.01698v1](https://arxiv.org/abs/2603.01698) · [PDF](https://arxiv.org/pdf/2603.01698.pdf)  
**作者**：Ruixi Wu, Shaobo Wang, Jiahuan Chen, Zhiyuan Liu, Yicun Yang, Zhaorun Chen, Zekai Li, Kaixin Li, Xinming Wang, Hongzhu Yi, Kai Wang, Linfeng Zhang  

**一句话要点**：提出类感知谱分布匹配以解决长尾数据集蒸馏中的分布对齐和类别不平衡问题。

**关键词**：数据集蒸馏, 长尾分布, 谱分布匹配, 类别不平衡, 核函数, 合成数据集

## 3 点简述
- 核心问题：现有数据集蒸馏方法在长尾数据集上性能显著下降，源于启发式分布差异度量和类别处理不均。
- 方法要点：通过核函数谱重新定义分布对齐，引入谱分布距离，并基于振幅-相位分解自适应优化尾部类别的真实性。
- 实验或效果：在CIFAR-10-LT上，每类10张图像，CSDM比最先进方法提升14.0%，尾部类别图像数从500降至25时性能仅下降5.7%。

## 摘要（原文）

> Dataset distillation (DD) aims to compress large-scale datasets into compact synthetic counterparts for efficient model training. However, existing DD methods exhibit substantial performance degradation on long-tailed datasets. We identify two fundamental challenges: heuristic design choices for distribution discrepancy measure and uniform treatment of imbalanced classes. To address these limitations, we propose Class-Aware Spectral Distribution Matching (CSDM), which reformulates distribution alignment via the spectrum of a well-behaved kernel function. This technique maps the original samples into frequency space, resulting in the Spectral Distribution Distance (SDD). To mitigate class imbalance, we exploit the unified form of SDD to perform amplitude-phase decomposition, which adaptively prioritizes the realism in tail classes. On CIFAR-10-LT, with 10 images per class, CSDM achieves a 14.0% improvement over state-of-the-art DD methods, with only a 5.7% performance drop when the number of images in tail classes decreases from 500 to 25, demonstrating strong stability on long-tailed data.

