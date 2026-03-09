---
layout: default
title: Towards High-resolution and Disentangled Reference-based Sketch Colorization
---

# Towards High-resolution and Disentangled Reference-based Sketch Colorization
**arXiv**：[2603.05971v1](https://arxiv.org/abs/2603.05971) · [PDF](https://arxiv.org/pdf/2603.05971.pdf)  
**作者**：Dingkun Yan, Xinrui Wang, Ru Wang, Zhuoru Li, Jinze Yu, Yusuke Iwasawa, Yutaka Matsuo, Jiaxian Guo  

**一句话要点**：提出双分支框架以解决草图着色中的分布偏移问题，实现高分辨率与可控着色。

**关键词**：草图着色, 分布偏移, 双分支框架, Gram正则化, 可控着色, 高分辨率

## 3 点简述
- 核心问题：草图着色中训练与测试数据分布偏移导致质量下降。
- 方法要点：采用语义对齐与不对齐双分支建模，结合Gram正则化损失增强分布一致性。
- 实验或效果：通过定量、定性比较和用户研究，在质量和可控性上达到先进水平。

## 摘要（原文）

> Sketch colorization is a critical task for automating and assisting in the creation of animations and digital illustrations. Previous research identified the primary difficulty as the distribution shift between semantically aligned training data and highly diverse test data, and focused on mitigating the artifacts caused by the distribution shift instead of fundamentally resolving the problem. In this paper, we present a framework that directly minimizes the distribution shift, thereby achieving superior quality, resolution, and controllability of colorization. We propose a dual-branch framework to explicitly model the data distributions of the training process and inference process with a semantic-aligned branch and a semantic-misaligned branch, respectively. A Gram Regularization Loss is applied across the feature maps of both branches, effectively enforcing cross-domain distribution coherence and stability. Furthermore, we adopt an anime-specific Tagger Network to extract fine-grained attributions from reference images and modulate SDXL's conditional encoders to ensure precise control, and a plugin module to enhance texture transfer. Quantitative and qualitative comparisons, alongside user studies, confirm that our method effectively overcomes the distribution shift challenge, establishing State-of-the-Art performance across both quality and controllability metrics. Ablation study reveals the influence of each component.

