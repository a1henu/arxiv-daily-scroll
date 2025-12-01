---
layout: default
title: MIMM-X: Disentangling Spurious Correlations for Medical Image Analysis
---

# MIMM-X: Disentangling Spurious Correlations for Medical Image Analysis
**arXiv**：[2511.22990v1](https://arxiv.org/abs/2511.22990) · [PDF](https://arxiv.org/pdf/2511.22990.pdf)  
**作者**：Louisa Fay, Hajer Reguigui, Bin Yang, Sergios Gatidis, Thomas Küstner  

**一句话要点**：提出MIMM-X框架，通过最小化互信息来解耦医学图像中的因果特征与多重伪相关，以缓解捷径学习问题。

**关键词**：医学图像分析, 捷径学习, 特征解耦, 伪相关缓解, 互信息最小化, 泛化能力

## 3 点简述
- 核心问题：深度学习模型在医学图像分析中易受多重伪相关影响，导致泛化能力差和误分类风险。
- 方法要点：MIMM-X通过最小化因果特征与多重伪相关之间的互信息，实现特征解耦，使预测基于真实因果关系。
- 实验或效果：在UK Biobank、NAKO和CheXpert数据集上评估，涵盖MRI和X-ray模态，结果显示能有效缓解多重伪相关的捷径学习。

## 摘要（原文）

> Deep learning models can excel on medical tasks, yet often experience spurious correlations, known as shortcut learning, leading to poor generalization in new environments. Particularly in medical imaging, where multiple spurious correlations can coexist, misclassifications can have severe consequences. We propose MIMM-X, a framework that disentangles causal features from multiple spurious correlations by minimizing their mutual information. It enables predictions based on true underlying causal relationships rather than dataset-specific shortcuts. We evaluate MIMM-X on three datasets (UK Biobank, NAKO, CheXpert) across two imaging modalities (MRI and X-ray). Results demonstrate that MIMM-X effectively mitigates shortcut learning of multiple spurious correlations.

