---
layout: default
title: Diffusion Model-Based Data Augmentation for Enhanced Neuron Segmentation
---

# Diffusion Model-Based Data Augmentation for Enhanced Neuron Segmentation
**arXiv**：[2601.15779v1](https://arxiv.org/abs/2601.15779) · [PDF](https://arxiv.org/pdf/2601.15779.pdf)  
**作者**：Liuyun Jiang, Yanchao Zhang, Jinyue Guo, Yizhuo Lu, Ruining Zhou, Hua Han  

**一句话要点**：提出基于扩散模型的数据增强框架，以提升低标注下神经元分割性能

**关键词**：扩散模型, 数据增强, 神经元分割, 电子显微镜, 低标注学习, 三维图像合成

## 3 点简述
- 问题：神经元分割依赖大规模标注数据，传统增强方法缺乏结构多样性。
- 方法：使用分辨率感知条件扩散模型，结合多尺度条件和生物学引导的掩模重塑。
- 效果：在AC3和AC4数据集上，ARAND指标分别提升32.1%和30.7%。

## 摘要（原文）

> Neuron segmentation in electron microscopy (EM) aims to reconstruct the complete neuronal connectome; however, current deep learning-based methods are limited by their reliance on large-scale training data and extensive, time-consuming manual annotations. Traditional methods augment the training set through geometric and photometric transformations; however, the generated samples remain highly correlated with the original images and lack structural diversity. To address this limitation, we propose a diffusion-based data augmentation framework capable of generating diverse and structurally plausible image-label pairs for neuron segmentation. Specifically, the framework employs a resolution-aware conditional diffusion model with multi-scale conditioning and EM resolution priors to enable voxel-level image synthesis from 3D masks. It further incorporates a biology-guided mask remodeling module that produces augmented masks with enhanced structural realism. Together, these components effectively enrich the training set and improve segmentation performance. On the AC3 and AC4 datasets under low-annotation regimes, our method improves the ARAND metric by 32.1% and 30.7%, respectively, when combined with two different post-processing methods. Our code is available at https://github.com/HeadLiuYun/NeuroDiff.

