---
layout: default
title: ACS-SegNet: An Attention-Based CNN-SegFormer Segmentation Network for Tissue Segmentation in Histopathology
---

# ACS-SegNet: An Attention-Based CNN-SegFormer Segmentation Network for Tissue Segmentation in Histopathology
**arXiv**：[2510.20754v1](https://arxiv.org/abs/2510.20754) · [PDF](https://arxiv.org/pdf/2510.20754.pdf)  
**作者**：Nima Torbati, Anastasia Meshcheryakova, Ramona Woitek, Diana Mechtcheriakova, Amirreza Mahbod  

**一句话要点**：提出基于注意力的CNN与ViT融合网络，用于组织病理学图像分割

**关键词**：组织病理学图像分割, 注意力机制, CNN-ViT融合, 语义分割, 双编码器模型

## 3 点简述
- 核心问题：自动化组织病理学图像分割，以辅助疾病诊断。
- 方法要点：采用注意力机制融合CNN和ViT特征，构建双编码器模型。
- 实验或效果：在GCPS和PUMA数据集上，μIoU/μDice得分优于现有方法。

## 摘要（原文）

> Automated histopathological image analysis plays a vital role in
> computer-aided diagnosis of various diseases. Among developed algorithms, deep
> learning-based approaches have demonstrated excellent performance in multiple
> tasks, including semantic tissue segmentation in histological images. In this
> study, we propose a novel approach based on attention-driven feature fusion of
> convolutional neural networks (CNNs) and vision transformers (ViTs) within a
> unified dual-encoder model to improve semantic segmentation performance.
> Evaluation on two publicly available datasets showed that our model achieved
> {\mu}IoU/{\mu}Dice scores of 76.79%/86.87% on the GCPS dataset and
> 64.93%/76.60% on the PUMA dataset, outperforming state-of-the-art and baseline
> benchmarks. The implementation of our method is publicly available in a GitHub
> repository: https://github.com/NimaTorbati/ACS-SegNet

