---
layout: default
title: Augment to Augment: Diverse Augmentations Enable Competitive Ultra-Low-Field MRI Enhancement
---

# Augment to Augment: Diverse Augmentations Enable Competitive Ultra-Low-Field MRI Enhancement
**arXiv**：[2511.09366v1](https://arxiv.org/abs/2511.09366) · [PDF](https://arxiv.org/pdf/2511.09366.pdf)  
**作者**：Felix F Zimmermann  

**一句话要点**：提出多样化数据增强方法以提升超低场MRI图像增强性能

**关键词**：超低场MRI, 图像增强, 数据增强, 深度学习, 图像到图像翻译

## 3 点简述
- 超低场MRI图像存在信噪比低、分辨率差和对比度偏差问题
- 采用任务适应数据增强，包括在高场数据上执行辅助任务
- 在ULF-EnC挑战中验证，显著改善图像保真度，排名靠前

## 摘要（原文）

> Ultra-low-field (ULF) MRI promises broader accessibility but suffers from low signal-to-noise ratio (SNR), reduced spatial resolution, and contrasts that deviate from high-field standards. Imageto- image translation can map ULF images to a high-field appearance, yet efficacy is limited by scarce paired training data. Working within the ULF-EnC challenge constraints (50 paired 3D volumes; no external data), we study how task-adapted data augmentations impact a standard deep model for ULF image enhancement. We show that strong, diverse augmentations, including auxiliary tasks on high-field data, substantially improve fidelity. Our submission ranked third by brain-masked SSIM on the public validation leaderboard and fourth by the official score on the final test leaderboard. Code is available at https://github.com/fzimmermann89/low-field-enhancement.

