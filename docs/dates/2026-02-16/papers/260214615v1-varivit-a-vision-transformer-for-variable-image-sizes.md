---
layout: default
title: VariViT: A Vision Transformer for Variable Image Sizes
---

# VariViT: A Vision Transformer for Variable Image Sizes
**arXiv**：[2602.14615v1](https://arxiv.org/abs/2602.14615) · [PDF](https://arxiv.org/pdf/2602.14615.pdf)  
**作者**：Aswathi Varma, Suprosanna Shit, Chinmay Prabhakar, Daniel Scholz, Hongwei Bran Li, Bjoern Menze, Daniel Rueckert, Benedikt Wiestler  

**一句话要点**：提出VariViT以解决Vision Transformer在医学影像中处理可变尺寸图像的问题。

**关键词**：Vision Transformer, 可变尺寸图像, 医学影像, 位置嵌入, 批处理策略, 脑肿瘤分类

## 3 点简述
- 核心问题：Vision Transformer需固定尺寸图像，医学影像中可变尺寸裁剪导致前景背景比变化和信息损失。
- 方法要点：引入位置嵌入调整方案和批处理策略，支持可变数量补丁，降低计算复杂度。
- 实验或效果：在脑MRI数据集上优于ViT和ResNet，F1分数达75.5%和76.3%，计算时间减少30%。

## 摘要（原文）

> Vision Transformers (ViTs) have emerged as the state-of-the-art architecture in representation learning, leveraging self-attention mechanisms to excel in various tasks. ViTs split images into fixed-size patches, constraining them to a predefined size and necessitating pre-processing steps like resizing, padding, or cropping. This poses challenges in medical imaging, particularly with irregularly shaped structures like tumors. A fixed bounding box crop size produces input images with highly variable foreground-to-background ratios. Resizing medical images can degrade information and introduce artefacts, impacting diagnosis. Hence, tailoring variable-sized crops to regions of interest can enhance feature representation capabilities. Moreover, large images are computationally expensive, and smaller sizes risk information loss, presenting a computation-accuracy tradeoff. We propose VariViT, an improved ViT model crafted to handle variable image sizes while maintaining a consistent patch size. VariViT employs a novel positional embedding resizing scheme for a variable number of patches. We also implement a new batching strategy within VariViT to reduce computational complexity, resulting in faster training and inference times. In our evaluations on two 3D brain MRI datasets, VariViT surpasses vanilla ViTs and ResNet in glioma genotype prediction and brain tumor classification. It achieves F1-scores of 75.5% and 76.3%, respectively, learning more discriminative features. Our proposed batching strategy reduces computation time by up to 30% compared to conventional architectures. These findings underscore the efficacy of VariViT in image representation learning. Our code can be found here: https://github.com/Aswathi-Varma/varivit

