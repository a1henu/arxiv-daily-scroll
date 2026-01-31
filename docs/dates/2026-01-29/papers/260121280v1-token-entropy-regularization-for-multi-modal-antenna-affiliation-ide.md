---
layout: default
title: Token Entropy Regularization for Multi-modal Antenna Affiliation Identification
---

# Token Entropy Regularization for Multi-modal Antenna Affiliation Identification
**arXiv**：[2601.21280v1](https://arxiv.org/abs/2601.21280) · [PDF](https://arxiv.org/pdf/2601.21280.pdf)  
**作者**：Dong Chen, Ruoyu Li, Xinyan Zhang, Jialei Xu, Ruoseng Zhao, Zhikang Zhang, Lingyun Li, Zizhuang Wei  

**一句话要点**：提出Token Entropy Regularization模块，通过多模态对齐解决天线归属识别问题。

**关键词**：多模态对齐, 天线归属识别, Token Entropy Regularization, 通信网络优化, 预训练框架

## 3 点简述
- 核心问题：天线归属识别依赖人工巡检，现有预训练模型因通信领域数据缺乏而跨模态对齐困难。
- 方法要点：融合视频、几何特征和PCI信号，引入Token Entropy Regularization模块在预训练阶段对齐图像与信号表示。
- 实验或效果：TER加速收敛并提升性能，分析显示首令牌熵与模态相关，代码将公开。

## 摘要（原文）

> Accurate antenna affiliation identification is crucial for optimizing and maintaining communication networks. Current practice, however, relies on the cumbersome and error-prone process of manual tower inspections. We propose a novel paradigm shift that fuses video footage of base stations, antenna geometric features, and Physical Cell Identity (PCI) signals, transforming antenna affiliation identification into multi-modal classification and matching tasks. Publicly available pretrained transformers struggle with this unique task due to a lack of analogous data in the communications domain, which hampers cross-modal alignment. To address this, we introduce a dedicated training framework that aligns antenna images with corresponding PCI signals. To tackle the representation alignment challenge, we propose a novel Token Entropy Regularization module in the pretraining stage. Our experiments demonstrate that TER accelerates convergence and yields significant performance gains. Further analysis reveals that the entropy of the first token is modality-dependent. Code will be made available upon publication.

