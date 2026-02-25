---
layout: default
title: DA-Cal: Towards Cross-Domain Calibration in Semantic Segmentation
---

# DA-Cal: Towards Cross-Domain Calibration in Semantic Segmentation
**arXiv**：[2602.20860v1](https://arxiv.org/abs/2602.20860) · [PDF](https://arxiv.org/pdf/2602.20860.pdf)  
**作者**：Wangkai Li, Rui Sun, Zhaoyang Li, Yujia Chen, Tianzhu Zhang  

**一句话要点**：提出DA-Cal框架，通过软伪标签优化解决语义分割跨域校准问题。

**关键词**：语义分割, 无监督域适应, 跨域校准, 软伪标签优化, 元学习

## 3 点简述
- 核心问题：现有无监督域适应方法忽视校准质量，导致预测置信度与准确性不匹配。
- 方法要点：引入元温度网络生成像素级校准参数，采用双层优化关联软伪标签与域适应监督。
- 实验效果：在多个基准上无缝集成自训练框架，显著提升目标域校准和性能，无推理开销。

## 摘要（原文）

> While existing unsupervised domain adaptation (UDA) methods greatly enhance target domain performance in semantic segmentation, they often neglect network calibration quality, resulting in misalignment between prediction confidence and actual accuracy -- a significant risk in safety-critical applications. Our key insight emerges from observing that performance degrades substantially when soft pseudo-labels replace hard pseudo-labels in cross-domain scenarios due to poor calibration, despite the theoretical equivalence of perfectly calibrated soft pseudo-labels to hard pseudo-labels. Based on this finding, we propose DA-Cal, a dedicated cross-domain calibration framework that transforms target domain calibration into soft pseudo-label optimization. DA-Cal introduces a Meta Temperature Network to generate pixel-level calibration parameters and employs bi-level optimization to establish the relationship between soft pseudo-labels and UDA supervision, while utilizing complementary domain-mixing strategies to prevent overfitting and reduce domain discrepancies. Experiments demonstrate that DA-Cal seamlessly integrates with existing self-training frameworks across multiple UDA segmentation benchmarks, significantly improving target domain calibration while delivering performance gains without inference overhead. The code will be released.

