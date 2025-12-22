---
layout: default
title: SkinGenBench: Generative Model and Preprocessing Effects for Synthetic Dermoscopic Augmentation in Melanoma Diagnosis
---

# SkinGenBench: Generative Model and Preprocessing Effects for Synthetic Dermoscopic Augmentation in Melanoma Diagnosis
**arXiv**：[2512.17585v1](https://arxiv.org/abs/2512.17585) · [PDF](https://arxiv.org/pdf/2512.17585.pdf)  
**作者**：N. A. Adarsh Pritam, Jeba Shiney O, Sanyam Jain  

**一句话要点**：提出SkinGenBench基准，评估生成模型与预处理对皮肤镜图像合成及黑色素瘤诊断的影响。

**关键词**：皮肤镜图像合成, 生成模型评估, 黑色素瘤诊断, 数据增强, 图像预处理, 医学影像基准

## 3 点简述
- 核心问题：生成模型选择和预处理复杂度如何影响合成皮肤镜图像的质量和下游诊断性能。
- 方法要点：使用StyleGAN2-ADA和DDPMs，结合几何增强与伪影去除，评估图像保真度和分布对齐。
- 实验或效果：StyleGAN2-ADA在图像保真度上更优，合成数据增强显著提升黑色素瘤检测性能，预处理改进有限。

## 摘要（原文）

> This work introduces SkinGenBench, a systematic biomedical imaging benchmark that investigates how preprocessing complexity interacts with generative model choice for synthetic dermoscopic image augmentation and downstream melanoma diagnosis. Using a curated dataset of 14,116 dermoscopic images from HAM10000 and MILK10K across five lesion classes, we evaluate the two representative generative paradigms: StyleGAN2-ADA and Denoising Diffusion Probabilistic Models (DDPMs) under basic geometric augmentation and advanced artifact removal pipelines. Synthetic melanoma images are assessed using established perceptual and distributional metrics (FID, KID, IS), feature space analysis, and their impact on diagnostic performance across five downstream classifiers. Experimental results demonstrate that generative architecture choice has a stronger influence on both image fidelity and diagnostic utility than preprocessing complexity. StyleGAN2-ADA consistently produced synthetic images more closely aligned with real data distributions, achieving the lowest FID (~65.5) and KID (~0.05), while diffusion models generated higher variance samples at the cost of reduces perceptual fidelity and class anchoring. Advanced artifact removal yielded only marginal improvements in generative metrics and provided limited downstream diagnostic gains, suggesting possible suppression of clinically relevant texture cues. In contrast, synthetic data augmentation substantially improved melanoma detection with 8-15% absolute gains in melanoma F1-score, and ViT-B/16 achieving F1~0.88 and ROC-AUC~0.98, representing an improvement of approximately 14% over non-augmented baselines. Our code can be found at https://github.com/adarsh-crafts/SkinGenBench

