---
layout: default
title: A Masked Reverse Knowledge Distillation Method Incorporating Global and Local Information for Image Anomaly Detection
---

# A Masked Reverse Knowledge Distillation Method Incorporating Global and Local Information for Image Anomaly Detection
**arXiv**：[2512.15326v1](https://arxiv.org/abs/2512.15326) · [PDF](https://arxiv.org/pdf/2512.15326.pdf)  
**作者**：Yuxin Jiang, Yunkang Can, Weiming Shen  

**一句话要点**：提出掩码反向知识蒸馏方法，结合全局与局部信息以解决图像异常检测中的过泛化问题。

**关键词**：图像异常检测, 知识蒸馏, 掩码学习, 过泛化缓解, 全局局部信息融合

## 3 点简述
- 核心问题：知识蒸馏在图像异常检测中易过泛化，因输入与监督信号相似。
- 方法要点：通过图像级掩码和特征级掩码，将重建任务转为修复任务，增强上下文捕获能力。
- 实验或效果：在MVTec数据集上，图像级AU-ROC达98.9%，像素级AU-ROC达98.4%，AU-PRO为95.3%。

## 摘要（原文）

> Knowledge distillation is an effective image anomaly detection and localization scheme. However, a major drawback of this scheme is its tendency to overly generalize, primarily due to the similarities between input and supervisory signals. In order to address this issue, this paper introduces a novel technique called masked reverse knowledge distillation (MRKD). By employing image-level masking (ILM) and feature-level masking (FLM), MRKD transforms the task of image reconstruction into image restoration. Specifically, ILM helps to capture global information by differentiating input signals from supervisory signals. On the other hand, FLM incorporates synthetic feature-level anomalies to ensure that the learned representations contain sufficient local information. With these two strategies, MRKD is endowed with stronger image context capture capacity and is less likely to be overgeneralized. Experiments on the widely-used MVTec anomaly detection dataset demonstrate that MRKD achieves impressive performance: image-level 98.9% AU-ROC, pixel-level 98.4% AU-ROC, and 95.3% AU-PRO. In addition, extensive ablation experiments have validated the superiority of MRKD in mitigating the overgeneralization problem.

