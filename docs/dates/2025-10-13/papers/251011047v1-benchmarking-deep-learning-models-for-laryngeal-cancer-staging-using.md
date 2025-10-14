---
layout: default
title: Benchmarking Deep Learning Models for Laryngeal Cancer Staging Using the LaryngealCT Dataset
---

# Benchmarking Deep Learning Models for Laryngeal Cancer Staging Using the LaryngealCT Dataset
**arXiv**：[2510.11047v1](https://arxiv.org/abs/2510.11047) · [PDF](https://arxiv.org/pdf/2510.11047.pdf)  
**作者**：Nivea Roy, Son Tran, Atul Sajjanhar, K. Devaraja, Prakashini Koteshwara, Yong Xiang, Divya Rao  

**一句话要点**：提出LaryngealCT数据集和基准测试，以解决喉癌分期缺乏标准化数据的问题。

**关键词**：喉癌分期, 深度学习基准测试, 3D医学影像, 模型可解释性, CT扫描数据集

## 3 点简述
- 核心问题：喉癌影像研究缺乏标准化数据集，影响深度学习模型的可复现性。
- 方法要点：构建包含1029个CT扫描的LaryngealCT数据集，使用弱监督参数搜索提取感兴趣区域。
- 实验或效果：在早期vs晚期和T4vs非T4分类任务中，3D CNN和ResNet18模型表现最佳。

## 摘要（原文）

> Laryngeal cancer imaging research lacks standardised datasets to enable
> reproducible deep learning (DL) model development. We present LaryngealCT, a
> curated benchmark of 1,029 computed tomography (CT) scans aggregated from six
> collections from The Cancer Imaging Archive (TCIA). Uniform 1 mm isotropic
> volumes of interest encompassing the larynx were extracted using a weakly
> supervised parameter search framework validated by clinical experts. 3D DL
> architectures (3D CNN, ResNet18,50,101, DenseNet121) were benchmarked on (i)
> early (Tis,T1,T2) vs. advanced (T3,T4) and (ii) T4 vs. non-T4 classification
> tasks. 3D CNN (AUC-0.881, F1-macro-0.821) and ResNet18 (AUC-0.892,
> F1-macro-0.646) respectively outperformed the other models in the two tasks.
> Model explainability assessed using 3D GradCAMs with thyroid cartilage overlays
> revealed greater peri-cartilage attention in non-T4 cases and focal activations
> in T4 predictions. Through open-source data, pretrained models, and integrated
> explainability tools, LaryngealCT offers a reproducible foundation for
> AI-driven research to support clinical decisions in laryngeal oncology.

