---
layout: default
title: Neural Collapse in Test-Time Adaptation
---

# Neural Collapse in Test-Time Adaptation
**arXiv**：[2512.10421v1](https://arxiv.org/abs/2512.10421) · [PDF](https://arxiv.org/pdf/2512.10421.pdf)  
**作者**：Xiao Chen, Zhongjing Du, Jiazhen Huang, Xu Jiang, Li Lu, Jingyan Jiang, Zhi Wang  

**一句话要点**：提出NCTTA方法以解决测试时适应中的样本对齐崩溃问题

**关键词**：测试时适应, 神经崩溃, 特征对齐, 域偏移, 伪标签可靠性

## 3 点简述
- 核心问题：测试时适应中性能下降源于样本特征与分类器权重对齐崩溃
- 方法要点：基于样本对齐崩溃现象，设计混合目标特征-分类器对齐方法
- 实验或效果：在ImageNet-C上比Tent提升14.52%，增强域偏移鲁棒性

## 摘要（原文）

> Test-Time Adaptation (TTA) enhances model robustness to out-of-distribution (OOD) data by updating the model online during inference, yet existing methods lack theoretical insights into the fundamental causes of performance degradation under domain shifts. Recently, Neural Collapse (NC) has been proposed as an emergent geometric property of deep neural networks (DNNs), providing valuable insights for TTA. In this work, we extend NC to the sample-wise level and discover a novel phenomenon termed Sample-wise Alignment Collapse (NC3+), demonstrating that a sample's feature embedding, obtained by a trained model, aligns closely with the corresponding classifier weight. Building on NC3+, we identify that the performance degradation stems from sample-wise misalignment in adaptation which exacerbates under larger distribution shifts. This indicates the necessity of realigning the feature embeddings with their corresponding classifier weights. However, the misalignment makes pseudo-labels unreliable under domain shifts. To address this challenge, we propose NCTTA, a novel feature-classifier alignment method with hybrid targets to mitigate the impact of unreliable pseudo-labels, which blends geometric proximity with predictive confidence. Extensive experiments demonstrate the effectiveness of NCTTA in enhancing robustness to domain shifts. For example, NCTTA outperforms Tent by 14.52% on ImageNet-C.

