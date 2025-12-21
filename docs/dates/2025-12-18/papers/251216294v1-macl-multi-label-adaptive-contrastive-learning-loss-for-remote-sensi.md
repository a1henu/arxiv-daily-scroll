---
layout: default
title: MACL: Multi-Label Adaptive Contrastive Learning Loss for Remote Sensing Image Retrieval
---

# MACL: Multi-Label Adaptive Contrastive Learning Loss for Remote Sensing Image Retrieval
**arXiv**：[2512.16294v1](https://arxiv.org/abs/2512.16294) · [PDF](https://arxiv.org/pdf/2512.16294.pdf)  
**作者**：Amna Amir, Erchan Aptoula  

**一句话要点**：提出多标签自适应对比学习损失以解决遥感图像检索中的语义重叠与不平衡问题。

**关键词**：遥感图像检索, 多标签学习, 对比学习, 自适应损失, 语义不平衡, 表示学习

## 3 点简述
- 核心问题：遥感图像中土地覆盖类别语义重叠、标签分布高度不平衡及复杂类间共现模式。
- 方法要点：集成标签感知采样、频率敏感加权和动态温度缩放，实现平衡表示学习。
- 实验或效果：在三个基准数据集上优于对比损失基线，缓解语义不平衡，提升检索可靠性。

## 摘要（原文）

> Semantic overlap among land-cover categories, highly imbalanced label distributions, and complex inter-class co-occurrence patterns constitute significant challenges for multi-label remote-sensing image retrieval. In this article, Multi-Label Adaptive Contrastive Learning (MACL) is introduced as an extension of contrastive learning to address them. It integrates label-aware sampling, frequency-sensitive weighting, and dynamic-temperature scaling to achieve balanced representation learning across both common and rare categories. Extensive experiments on three benchmark datasets (DLRSD, ML-AID, and WHDLD), show that MACL consistently outperforms contrastive-loss based baselines, effectively mitigating semantic imbalance and delivering more reliable retrieval performance in large-scale remote-sensing archives. Code, pretrained models, and evaluation scripts will be released at https://github.com/amna/MACL upon acceptance.

