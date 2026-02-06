---
layout: default
title: HyperPotter: Spell the Charm of High-Order Interactions in Audio Deepfake Detection
---

# HyperPotter: Spell the Charm of High-Order Interactions in Audio Deepfake Detection
**arXiv**：[2602.05670v1](https://arxiv.org/abs/2602.05670) · [PDF](https://arxiv.org/pdf/2602.05670.pdf)  
**作者**：Qing Wen, Haohao Li, Zhongjie Ba, Peng Cheng, Miao He, Li Lu, Kui Ren  

**一句话要点**：提出HyperPotter框架，通过超图建模高阶交互以提升音频深度伪造检测性能。

**关键词**：音频深度伪造检测, 高阶交互, 超图学习, 跨域泛化, AIGC安全

## 3 点简述
- 核心问题：现有音频深度伪造检测方法多依赖局部特征或成对关系，忽略高阶交互的判别模式。
- 方法要点：基于超图框架，通过聚类超边和类感知原型初始化显式建模高阶交互。
- 实验或效果：在11个数据集上平均相对增益22.15%，在4个跨域数据集上优于SOTA方法13.96%。

## 摘要（原文）

> Advances in AIGC technologies have enabled the synthesis of highly realistic audio deepfakes capable of deceiving human auditory perception. Although numerous audio deepfake detection (ADD) methods have been developed, most rely on local temporal/spectral features or pairwise relations, overlooking high-order interactions (HOIs). HOIs capture discriminative patterns that emerge from multiple feature components beyond their individual contributions. We propose HyperPotter, a hypergraph-based framework that explicitly models these synergistic HOIs through clustering-based hyperedges with class-aware prototype initialization. Extensive experiments demonstrate that HyperPotter surpasses its baseline by an average relative gain of 22.15% across 11 datasets and outperforms state-of-the-art methods by 13.96% on 4 challenging cross-domain datasets, demonstrating superior generalization to diverse attacks and speakers.

