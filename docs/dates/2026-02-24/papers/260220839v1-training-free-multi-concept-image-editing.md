---
layout: default
title: Training-Free Multi-Concept Image Editing
---

# Training-Free Multi-Concept Image Editing
**arXiv**：[2602.20839v1](https://arxiv.org/abs/2602.20839) · [PDF](https://arxiv.org/pdf/2602.20839.pdf)  
**作者**：Niki Foteinopoulou, Ignas Budvytis, Stephan Liwicki  

**一句话要点**：提出无需训练的多概念图像编辑框架，结合优化DDS与LoRA概念组合以解决文本表达不足问题。

**关键词**：无需训练图像编辑, 多概念控制, 扩散模型优化, LoRA概念组合, 文本与视觉融合

## 3 点简述
- 核心问题：扩散模型无需训练编辑图像时，文本提示难以表达视觉概念如面部结构或材质纹理。
- 方法要点：统一优化DDS与LoRA驱动概念组合，通过有序时间步、正则化和负提示提升稳定性和可控性。
- 实验或效果：在InstructPix2Pix和ComposLoRA基准上，定量和定性结果优于现有无需训练扩散编辑方法。

## 摘要（原文）

> Editing images with diffusion models without training remains challenging. While recent optimisation-based methods achieve strong zero-shot edits from text, they struggle to preserve identity or capture details that language alone cannot express. Many visual concepts such as facial structure, material texture, or object geometry are impossible to express purely through text prompts alone. To address this gap, we introduce a training-free framework for concept-based image editing, which unifies Optimised DDS with LoRA-driven concept composition, where the training data of the LoRA represent the concept. Our approach enables combining and controlling multiple visual concepts directly within the diffusion process, integrating semantic guidance from text with low-level cues from pretrained concept adapters. We further refine DDS for stability and controllability through ordered timesteps, regularisation, and negative-prompt guidance. Quantitative and qualitative results demonstrate consistent improvements over existing training-free diffusion editing methods on InstructPix2Pix and ComposLoRA benchmarks. Code will be made publicly available.

