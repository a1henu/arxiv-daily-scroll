---
layout: default
title: Towards Label-Free Brain Tumor Segmentation: Unsupervised Learning with Multimodal MRI
---

# Towards Label-Free Brain Tumor Segmentation: Unsupervised Learning with Multimodal MRI
**arXiv**：[2510.15684v1](https://arxiv.org/abs/2510.15684) · [PDF](https://arxiv.org/pdf/2510.15684.pdf)  
**作者**：Gerard Comas-Quiles, Carles Garcia-Cabrera, Julia Dietlmeier, Noel E. O'Connor, Ferran Marques  

**一句话要点**：提出多模态视觉变换器自编码器，用于无监督脑肿瘤分割以解决标注数据稀缺问题。

**关键词**：无监督异常检测, 脑肿瘤分割, 多模态MRI, 视觉变换器, 重建误差图, 标签高效工具

## 3 点简述
- 核心问题：脑肿瘤分割中标注数据有限、昂贵或不一致，限制监督学习可扩展性。
- 方法要点：使用健康脑MRI训练自编码器，通过重建误差图检测肿瘤，并融合多模态MRI序列。
- 实验或效果：在BraTS-GoAT数据集上，Dice系数达0.437（全肿瘤），检测率89.4%。

## 摘要（原文）

> Unsupervised anomaly detection (UAD) presents a complementary alternative to
> supervised learning for brain tumor segmentation in magnetic resonance imaging
> (MRI), particularly when annotated datasets are limited, costly, or
> inconsistent. In this work, we propose a novel Multimodal Vision Transformer
> Autoencoder (MViT-AE) trained exclusively on healthy brain MRIs to detect and
> localize tumors via reconstruction-based error maps. This unsupervised paradigm
> enables segmentation without reliance on manual labels, addressing a key
> scalability bottleneck in neuroimaging workflows. Our method is evaluated in
> the BraTS-GoAT 2025 Lighthouse dataset, which includes various types of tumors
> such as gliomas, meningiomas, and pediatric brain tumors. To enhance
> performance, we introduce a multimodal early-late fusion strategy that
> leverages complementary information across multiple MRI sequences, and a
> post-processing pipeline that integrates the Segment Anything Model (SAM) to
> refine predicted tumor contours. Despite the known challenges of UAD,
> particularly in detecting small or non-enhancing lesions, our method achieves
> clinically meaningful tumor localization, with lesion-wise Dice Similarity
> Coefficient of 0.437 (Whole Tumor), 0.316 (Tumor Core), and 0.350 (Enhancing
> Tumor) on the test set, and an anomaly Detection Rate of 89.4% on the
> validation set. These findings highlight the potential of transformer-based
> unsupervised models to serve as scalable, label-efficient tools for
> neuro-oncological imaging.

