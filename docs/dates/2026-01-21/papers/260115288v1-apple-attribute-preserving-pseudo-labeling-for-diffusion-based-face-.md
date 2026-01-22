---
layout: default
title: APPLE: Attribute-Preserving Pseudo-Labeling for Diffusion-Based Face Swapping
---

# APPLE: Attribute-Preserving Pseudo-Labeling for Diffusion-Based Face Swapping
**arXiv**：[2601.15288v1](https://arxiv.org/abs/2601.15288) · [PDF](https://arxiv.org/pdf/2601.15288.pdf)  
**作者**：Jiwon Kang, Yeji Choi, JoungBin Lee, Wooseok Jang, Jinhyeok Choi, Taekeun Kang, Yongjae Park, Myungin Kim, Seungryong Kim  

**一句话要点**：提出APPLE框架，通过属性感知伪标签监督解决扩散换脸中的属性保留问题

**关键词**：人脸交换, 扩散模型, 属性保留, 伪标签监督, 师生框架, 条件去模糊

## 3 点简述
- 核心问题：真实换脸数据缺失，现有扩散方法因掩码条件导致属性错位，难以同时实现身份转移和属性保留
- 方法要点：采用师生框架，将换脸重构为条件去模糊任务，并引入属性感知反演方案以提升细节属性保留
- 实验或效果：在属性保留和身份转移方面达到先进水平，生成更逼真且忠实于目标的结果

## 摘要（原文）

> Face swapping aims to transfer the identity of a source face onto a target face while preserving target-specific attributes such as pose, expression, lighting, skin tone, and makeup. However, since real ground truth for face swapping is unavailable, achieving both accurate identity transfer and high-quality attribute preservation remains challenging. In addition, recent diffusion-based approaches attempt to improve visual fidelity through conditional inpainting on masked target images, but the masked condition removes crucial appearance cues of target, resulting in plausible yet misaligned attributes. To address these limitations, we propose APPLE (Attribute-Preserving Pseudo-Labeling), a diffusion-based teacher-student framework that enhances attribute fidelity through attribute-aware pseudo-label supervision. We reformulate face swapping as a conditional deblurring task to more faithfully preserve target-specific attributes such as lighting, skin tone, and makeup. In addition, we introduce an attribute-aware inversion scheme to further improve detailed attribute preservation. Through an elaborate attribute-preserving design for teacher learning, APPLE produces high-quality pseudo triplets that explicitly provide the student with direct face-swapping supervision. Overall, APPLE achieves state-of-the-art performance in terms of attribute preservation and identity transfer, producing more photorealistic and target-faithful results.

