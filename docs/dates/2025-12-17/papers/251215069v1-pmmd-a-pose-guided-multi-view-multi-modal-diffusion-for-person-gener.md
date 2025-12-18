---
layout: default
title: PMMD: A pose-guided multi-view multi-modal diffusion for person generation
---

# PMMD: A pose-guided multi-view multi-modal diffusion for person generation
**arXiv**：[2512.15069v1](https://arxiv.org/abs/2512.15069) · [PDF](https://arxiv.org/pdf/2512.15069.pdf)  
**作者**：Ziyu Shang, Haoran Liu, Rongchao Zhang, Zhiqian Wei, Tongtong Feng  

**一句话要点**：提出PMMD扩散框架，通过多模态融合生成姿态可控、外观一致的人物图像

**关键词**：人物图像生成, 扩散模型, 多模态融合, 姿态引导, 细节增强

## 3 点简述
- 核心问题：现有方法在人物图像生成中常出现遮挡、服装风格漂移和姿态错位问题
- 方法要点：设计多模态编码器联合建模视觉、姿态和文本，并引入ResCVA模块增强细节
- 实验或效果：在DeepFashion MultiModal数据集上，PMMD在一致性、细节保持和可控性方面优于基线

## 摘要（原文）

> Generating consistent human images with controllable pose and appearance is essential for applications in virtual try on, image editing, and digital human creation. Current methods often suffer from occlusions, garment style drift, and pose misalignment. We propose Pose-guided Multi-view Multimodal Diffusion (PMMD), a diffusion framework that synthesizes photorealistic person images conditioned on multi-view references, pose maps, and text prompts. A multimodal encoder jointly models visual views, pose features, and semantic descriptions, which reduces cross modal discrepancy and improves identity fidelity. We further design a ResCVA module to enhance local detail while preserving global structure, and a cross modal fusion module that integrates image semantics with text throughout the denoising pipeline. Experiments on the DeepFashion MultiModal dataset show that PMMD outperforms representative baselines in consistency, detail preservation, and controllability. Project page and code are available at https://github.com/ZANMANGLOOPYE/PMMD.

