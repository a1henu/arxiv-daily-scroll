---
layout: default
title: CharDiff: A Diffusion Model with Character-Level Guidance for License Plate Image Restoration
---

# CharDiff: A Diffusion Model with Character-Level Guidance for License Plate Image Restoration
**arXiv**：[2510.17330v1](https://arxiv.org/abs/2510.17330) · [PDF](https://arxiv.org/pdf/2510.17330.pdf)  
**作者**：Gyuhwan Park, Kihyun Na, Injung Kim  

**一句话要点**：提出CharDiff扩散模型，通过字符级指导解决真实场景下车牌图像恢复问题。

**关键词**：车牌图像恢复, 扩散模型, 字符级指导, 光学字符识别, 注意力机制, 图像增强

## 3 点简述
- 核心问题：真实场景下车牌图像严重退化，影响识别和证据价值。
- 方法要点：结合字符分割和OCR提取先验，使用CHARM模块实现区域掩码注意力指导。
- 实验或效果：在Roboflow-LP数据集上，CER相对降低28%，恢复质量和识别精度显著提升。

## 摘要（原文）

> The significance of license plate image restoration goes beyond the
> preprocessing stage of License Plate Recognition (LPR) systems, as it also
> serves various purposes, including increasing evidential value, enhancing the
> clarity of visual interface, and facilitating further utilization of license
> plate images. We propose a novel diffusion-based framework with character-level
> guidance, CharDiff, which effectively restores and recognizes severely degraded
> license plate images captured under realistic conditions. CharDiff leverages
> fine-grained character-level priors extracted through external segmentation and
> Optical Character Recognition (OCR) modules tailored for low-quality license
> plate images. For precise and focused guidance, CharDiff incorporates a novel
> Character-guided Attention through Region-wise Masking (CHARM) module, which
> ensures that each character's guidance is restricted to its own region, thereby
> avoiding interference with other regions. In experiments, CharDiff
> significantly outperformed the baseline restoration models in both restoration
> quality and recognition accuracy, achieving a 28% relative reduction in CER on
> the Roboflow-LP dataset, compared to the best-performing baseline model. These
> results indicate that the structured character-guided conditioning effectively
> enhances the robustness of diffusion-based license plate restoration and
> recognition in practical deployment scenarios.

