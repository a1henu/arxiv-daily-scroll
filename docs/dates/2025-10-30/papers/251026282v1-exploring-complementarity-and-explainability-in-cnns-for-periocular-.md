---
layout: default
title: Exploring Complementarity and Explainability in CNNs for Periocular Verification Across Acquisition Distances
---

# Exploring Complementarity and Explainability in CNNs for Periocular Verification Across Acquisition Distances
**arXiv**：[2510.26282v1](https://arxiv.org/abs/2510.26282) · [PDF](https://arxiv.org/pdf/2510.26282.pdf)  
**作者**：Fernando Alonso-Fernandez, Kevin Hernandez Diaz, Jose M. Buades, Kiran Raja, Josef Bigun  

**一句话要点**：探索CNN互补性与可解释性以提升不同距离下眼周验证性能

**关键词**：眼周验证, CNN互补性, 分数级融合, 注意力热图, UBIPr数据库, 可解释性分析

## 3 点简述
- 研究不同距离下眼周验证中CNN模型的互补性问题，使用UBIPr数据库
- 训练三种复杂度递增的CNN架构，分析性能并应用分数级融合与注意力模式比较
- 融合方法显著提升性能，热图显示网络关注不同区域，实现新SOTA结果

## 摘要（原文）

> We study the complementarity of different CNNs for periocular verification at
> different distances on the UBIPr database. We train three architectures of
> increasing complexity (SqueezeNet, MobileNetv2, and ResNet50) on a large set of
> eye crops from VGGFace2. We analyse performance with cosine and chi2 metrics,
> compare different network initialisations, and apply score-level fusion via
> logistic regression. In addition, we use LIME heatmaps and Jensen-Shannon
> divergence to compare attention patterns of the CNNs. While ResNet50
> consistently performs best individually, the fusion provides substantial gains,
> especially when combining all three networks. Heatmaps show that networks
> usually focus on distinct regions of a given image, which explains their
> complementarity. Our method significantly outperforms previous works on UBIPr,
> achieving a new state-of-the-art.

