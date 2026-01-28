---
layout: default
title: Localized Latent Editing for Dose-Response Modeling in Botulinum Toxin Injection Planning
---

# Localized Latent Editing for Dose-Response Modeling in Botulinum Toxin Injection Planning
**arXiv**：[2601.19593v1](https://arxiv.org/abs/2601.19593) · [PDF](https://arxiv.org/pdf/2601.19593.pdf)  
**作者**：Estèphe Arnaud, Mohamed Daoudi, Pierre Guerreschi  

**一句话要点**：提出局部潜在编辑框架，通过剂量-响应建模模拟肉毒毒素注射效果以优化注射规划

**关键词**：肉毒毒素注射规划, 剂量-响应建模, 局部潜在编辑, StyleGAN2, 区域特定潜在轴发现, 人机协同工作流

## 3 点简述
- 核心问题：肉毒毒素注射剂量确定依赖直觉，常导致次优结果，需更精确的剂量-响应建模。
- 方法要点：开发区域特定潜在轴发现方法，在StyleGAN2潜在空间中学习局部肌肉松弛轨迹，实现精准面部区域控制。
- 实验或效果：在临床数据集上比较直接度量回归与基于图像的生成模拟，生成模型在几何不对称度量上显示中到强结构相关性。

## 摘要（原文）

> Botulinum toxin (Botox) injections are the gold standard for managing facial asymmetry and aesthetic rejuvenation, yet determining the optimal dosage remains largely intuitive, often leading to suboptimal outcomes. We propose a localized latent editing framework that simulates Botulinum Toxin injection effects for injection planning through dose-response modeling. Our key contribution is a Region-Specific Latent Axis Discovery method that learns localized muscle relaxation trajectories in StyleGAN2's latent space, enabling precise control over specific facial regions without global side effects. By correlating these localized latent trajectories with injected toxin units, we learn a predictive dose-response model. We rigorously compare two approaches: direct metric regression versus image-based generative simulation on a clinical dataset of N=360 images from 46 patients. On a hold-out test set, our framework demonstrates moderate-to-strong structural correlations for geometric asymmetry metrics, confirming that the generative model correctly captures the direction of morphological changes. While biological variability limits absolute precision, we introduce a hybrid "Human-in-the-Loop" workflow where clinicians interactively refine simulations, bridging the gap between pathological reconstruction and cosmetic planning.

