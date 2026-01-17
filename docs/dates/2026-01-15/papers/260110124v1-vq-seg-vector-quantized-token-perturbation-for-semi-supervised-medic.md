---
layout: default
title: VQ-Seg: Vector-Quantized Token Perturbation for Semi-Supervised Medical Image Segmentation
---

# VQ-Seg: Vector-Quantized Token Perturbation for Semi-Supervised Medical Image Segmentation
**arXiv**：[2601.10124v1](https://arxiv.org/abs/2601.10124) · [PDF](https://arxiv.org/pdf/2601.10124.pdf)  
**作者**：Sicheng Yang, Zhaohu Xing, Lei Zhu  

**一句话要点**：提出VQ-Seg，利用向量量化扰动解决半监督医学图像分割中dropout超参数敏感问题。

**关键词**：半监督医学图像分割, 向量量化, 特征扰动, 一致性学习, 肺癌分割, 量化扰动模块

## 3 点简述
- 核心问题：现有半监督医学图像分割方法依赖dropout进行特征扰动，其超参数敏感且难以优化，可能导致正则化效果不佳。
- 方法要点：设计量化扰动模块，通过向量量化离散化特征空间并扰动码书索引空间位置，实现可控正则化；采用双分支架构和特征适配器减少量化信息损失。
- 实验或效果：在自建肺癌数据集和公共基准上验证，性能优于现有方法，代码已开源。

## 摘要（原文）

> Consistency learning with feature perturbation is a widely used strategy in semi-supervised medical image segmentation. However, many existing perturbation methods rely on dropout, and thus require a careful manual tuning of the dropout rate, which is a sensitive hyperparameter and often difficult to optimize and may lead to suboptimal regularization. To overcome this limitation, we propose VQ-Seg, the first approach to employ vector quantization (VQ) to discretize the feature space and introduce a novel and controllable Quantized Perturbation Module (QPM) that replaces dropout. Our QPM perturbs discrete representations by shuffling the spatial locations of codebook indices, enabling effective and controllable regularization. To mitigate potential information loss caused by quantization, we design a dual-branch architecture where the post-quantization feature space is shared by both image reconstruction and segmentation tasks. Moreover, we introduce a Post-VQ Feature Adapter (PFA) to incorporate guidance from a foundation model (FM), supplementing the high-level semantic information lost during quantization. Furthermore, we collect a large-scale Lung Cancer (LC) dataset comprising 828 CT scans annotated for central-type lung carcinoma. Extensive experiments on the LC dataset and other public benchmarks demonstrate the effectiveness of our method, which outperforms state-of-the-art approaches. Code available at: https://github.com/script-Yang/VQ-Seg.

