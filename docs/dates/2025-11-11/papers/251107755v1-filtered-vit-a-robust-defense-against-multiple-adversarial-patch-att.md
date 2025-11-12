---
layout: default
title: Filtered-ViT: A Robust Defense Against Multiple Adversarial Patch Attacks
---

# Filtered-ViT: A Robust Defense Against Multiple Adversarial Patch Attacks
**arXiv**：[2511.07755v1](https://arxiv.org/abs/2511.07755) · [PDF](https://arxiv.org/pdf/2511.07755.pdf)  
**作者**：Aja Khanal, Ahmed Faid, Apurva Narayan  

**一句话要点**：提出Filtered-ViT以防御多对抗补丁攻击，提升安全关键领域视觉系统鲁棒性

**关键词**：对抗补丁防御, 视觉Transformer, 多尺度过滤, 鲁棒性增强, 医疗影像分析

## 3 点简述
- 深度学习视觉系统易受多对抗补丁攻击，现有防御方法在多重局部干扰下失效
- 集成SMART-VMF机制，实现空间自适应多尺度过滤，选择性抑制损坏区域并保留语义细节
- 在ImageNet多补丁攻击下，鲁棒准确率达46.3%，并在医疗影像中有效缓解自然伪影

## 摘要（原文）

> Deep learning vision systems are increasingly deployed in safety-critical domains such as healthcare, yet they remain vulnerable to small adversarial patches that can trigger misclassifications. Most existing defenses assume a single patch and fail when multiple localized disruptions occur, the type of scenario adversaries and real-world artifacts often exploit. We propose Filtered-ViT, a new vision transformer architecture that integrates SMART Vector Median Filtering (SMART-VMF), a spatially adaptive, multi-scale, robustness-aware mechanism that enables selective suppression of corrupted regions while preserving semantic detail. On ImageNet with LaVAN multi-patch attacks, Filtered-ViT achieves 79.8% clean accuracy and 46.3% robust accuracy under four simultaneous 1\% patches, outperforming existing defenses. Beyond synthetic benchmarks, a real-world case study on radiographic medical imagery shows that Filtered-ViT mitigates natural artifacts such as occlusions and scanner noise without degrading diagnostic content. This establishes Filtered-ViT as the first transformer to demonstrate unified robustness against both adversarial and naturally occurring patch-like disruptions, charting a path toward reliable vision systems in truly high-stakes environments.

