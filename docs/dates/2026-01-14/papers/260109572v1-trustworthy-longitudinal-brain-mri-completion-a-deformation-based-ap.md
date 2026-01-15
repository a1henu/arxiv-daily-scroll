---
layout: default
title: Trustworthy Longitudinal Brain MRI Completion: A Deformation-Based Approach with KAN-Enhanced Diffusion Model
---

# Trustworthy Longitudinal Brain MRI Completion: A Deformation-Based Approach with KAN-Enhanced Diffusion Model
**arXiv**：[2601.09572v1](https://arxiv.org/abs/2601.09572) · [PDF](https://arxiv.org/pdf/2601.09572.pdf)  
**作者**：Tianli Tao, Ziyang Wang, Delong Yang, Han Zhang, Le Zhang  

**一句话要点**：提出DF-DiffCom，基于变形场与KAN增强扩散模型，解决纵向脑MRI缺失数据的可信完成问题。

**关键词**：纵向脑MRI, 图像补全, 扩散模型, 变形场, KAN增强, 模态无关

## 3 点简述
- 核心问题：纵向脑MRI数据缺失率高，现有生成模型依赖图像强度，可信度与灵活性受限。
- 方法要点：利用变形场结合KAN增强扩散模型，提升生成图像的可信度与模态无关性。
- 实验或效果：在OASIS-3数据集上优于现有方法，PSNR提升5.6%，SSIM提升0.12。

## 摘要（原文）

> Longitudinal brain MRI is essential for lifespan study, yet high attrition rates often lead to missing data, complicating analysis. Deep generative models have been explored, but most rely solely on image intensity, leading to two key limitations: 1) the fidelity or trustworthiness of the generated brain images are limited, making downstream studies questionable; 2) the usage flexibility is restricted due to fixed guidance rooted in the model structure, restricting full ability to versatile application scenarios. To address these challenges, we introduce DF-DiffCom, a Kolmogorov-Arnold Networks (KAN)-enhanced diffusion model that smartly leverages deformation fields for trustworthy longitudinal brain image completion. Trained on OASIS-3, DF-DiffCom outperforms state-of-the-art methods, improving PSNR by 5.6% and SSIM by 0.12. More importantly, its modality-agnostic nature allows smooth extension to varied MRI modalities, even to attribute maps such as brain tissue segmentation results.

