---
layout: default
title: Defense against Unauthorized Distillation in Image Restoration via Feature Space Perturbation
---

# Defense against Unauthorized Distillation in Image Restoration via Feature Space Perturbation
**arXiv**：[2510.08925v1](https://arxiv.org/abs/2510.08925) · [PDF](https://arxiv.org/pdf/2510.08925.pdf)  
**作者**：Han Hu, Zhuoran Zheng, Chen Lyu  
**一句话要点**：提出自适应奇异值扰动以防御图像恢复模型的知识蒸馏攻击

**关键词**：图像恢复, 知识蒸馏防御, 奇异值分解, 特征扰动, 模型保护

## 3 点简述
- 知识蒸馏攻击威胁模型知识产权，图像恢复因连续高维输出难以防御
- ASVP在运行时扰动教师模型特征图，放大奇异值注入高频扰动
- 实验显示ASVP显著降低学生性能，对教师影响可忽略，覆盖多种任务

## 摘要（原文）

> Knowledge distillation (KD) attacks pose a significant threat to deep model
> intellectual property by enabling adversaries to train student networks using a
> teacher model's outputs. While recent defenses in image classification have
> successfully disrupted KD by perturbing output probabilities, extending these
> methods to image restoration is difficult. Unlike classification, restoration
> is a generative task with continuous, high-dimensional outputs that depend on
> spatial coherence and fine details. Minor perturbations are often insufficient,
> as students can still learn the underlying mapping.To address this, we propose
> Adaptive Singular Value Perturbation (ASVP), a runtime defense tailored for
> image restoration models. ASVP operates on internal feature maps of the teacher
> using singular value decomposition (SVD). It amplifies the topk singular values
> to inject structured, high-frequency perturbations, disrupting the alignment
> needed for distillation. This hinders student learning while preserving the
> teacher's output quality.We evaluate ASVP across five image restoration tasks:
> super-resolution, low-light enhancement, underwater enhancement, dehazing, and
> deraining. Experiments show ASVP reduces student PSNR by up to 4 dB and SSIM by
> 60-75%, with negligible impact on the teacher's performance. Compared to prior
> methods, ASVP offers a stronger and more consistent defense.Our approach
> provides a practical solution to protect open-source restoration models from
> unauthorized knowledge distillation.

