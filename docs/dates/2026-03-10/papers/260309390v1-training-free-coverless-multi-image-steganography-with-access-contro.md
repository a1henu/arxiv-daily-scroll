---
layout: default
title: Training-Free Coverless Multi-Image Steganography with Access Control
---

# Training-Free Coverless Multi-Image Steganography with Access Control
**arXiv**：[2603.09390v1](https://arxiv.org/abs/2603.09390) · [PDF](https://arxiv.org/pdf/2603.09390.pdf)  
**作者**：Minyeol Bae, Si-Hyeon Lee  

**一句话要点**：提出MIDAS框架以解决无载体隐写中多图像隐藏与用户访问控制问题

**关键词**：无载体隐写, 访问控制, 扩散模型, 多图像隐藏, 训练免费

## 3 点简述
- 核心问题：现有无载体隐写方法缺乏稳健访问控制，难以在多用户场景下选择性揭示隐藏内容
- 方法要点：基于扩散模型，通过随机基机制和潜在向量融合实现训练免费的多图像隐藏与用户特定访问控制
- 实验或效果：在访问控制功能、隐写图像质量、抗噪声和抗隐写分析方面优于现有训练免费基线

## 摘要（原文）

> Coverless Image Steganography (CIS) hides information without explicitly modifying a cover image, providing strong imperceptibility and inherent robustness to steganalysis. However, existing CIS methods largely lack robust access control, making it difficult to selectively reveal different hidden contents to different authorized users. Such access control is critical for scalable and privacy-sensitive information hiding in multi-user settings. We propose MIDAS, a training-free diffusion-based CIS framework that enables multi-image hiding with user-specific access control via latent-level fusion. MIDAS introduces a Random Basis mechanism to suppress residual structural information and a Latent Vector Fusion module that reshapes aggregated latents to align with the diffusion process. Experimental results demonstrate that MIDAS consistently outperforms existing training-free CIS baselines in access control functionality, stego image quality and diversity, robustness to noise, and resistance to steganalysis, establishing a practical and scalable approach to access-controlled coverless steganography.

