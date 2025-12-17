---
layout: default
title: Adaptable Segmentation Pipeline for Diverse Brain Tumors with Radiomic-guided Subtyping and Lesion-Wise Model Ensemble
---

# Adaptable Segmentation Pipeline for Diverse Brain Tumors with Radiomic-guided Subtyping and Lesion-Wise Model Ensemble
**arXiv**：[2512.14648v1](https://arxiv.org/abs/2512.14648) · [PDF](https://arxiv.org/pdf/2512.14648.pdf)  
**作者**：Daniel Capellán-Martín, Abhijeet Parida, Zhifan Jiang, Nishad Kulkarni, Krithika Iyer, Austin Tapp, Syed Muhammad Anwar, María J. Ledesma-Carbayo, Marius George Linguraru  

**一句话要点**：提出可适应分割流程，结合影像组学引导亚型分类与病灶级模型集成，以提升脑肿瘤分割的鲁棒性。

**关键词**：脑肿瘤分割, 影像组学, 模型集成, 病灶级处理, 多参数MRI, 模块化流程

## 3 点简述
- 核心问题：脑肿瘤类型多样，在MRI上实现鲁棒且泛化的分割具有挑战性。
- 方法要点：采用模块化流程，通过影像组学特征检测亚型以平衡训练，并基于病灶级指标进行模型集成与后处理优化。
- 实验或效果：在BraTS 2025测试集上，性能与顶级算法相当，验证了方法的有效性。

## 摘要（原文）

> Robust and generalizable segmentation of brain tumors on multi-parametric magnetic resonance imaging (MRI) remains difficult because tumor types differ widely. The BraTS 2025 Lighthouse Challenge benchmarks segmentation methods on diverse high-quality datasets of adult and pediatric tumors: multi-consortium international pediatric brain tumor segmentation (PED), preoperative meningioma tumor segmentation (MEN), meningioma radiotherapy segmentation (MEN-RT), and segmentation of pre- and post-treatment brain metastases (MET). We present a flexible, modular, and adaptable pipeline that improves segmentation performance by selecting and combining state-of-the-art models and applying tumor- and lesion-specific processing before and after training. Radiomic features extracted from MRI help detect tumor subtype, ensuring a more balanced training. Custom lesion-level performance metrics determine the influence of each model in the ensemble and optimize post-processing that further refines the predictions, enabling the workflow to tailor every step to each case. On the BraTS testing sets, our pipeline achieved performance comparable to top-ranked algorithms across multiple challenges. These findings confirm that custom lesion-aware processing and model selection yield robust segmentations yet without locking the method to a specific network architecture. Our method has the potential for quantitative tumor measurement in clinical practice, supporting diagnosis and prognosis.

