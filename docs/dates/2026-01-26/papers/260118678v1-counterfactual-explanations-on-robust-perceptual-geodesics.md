---
layout: default
title: Counterfactual Explanations on Robust Perceptual Geodesics
---

# Counterfactual Explanations on Robust Perceptual Geodesics
**arXiv**：[2601.18678v1](https://arxiv.org/abs/2601.18678) · [PDF](https://arxiv.org/pdf/2601.18678.pdf)  
**作者**：Eslam Zaher, Maciej Trzaskowski, Quan Nguyen, Fred Roosta  

**一句话要点**：提出感知反事实测地线方法，以解决反事实解释中距离度量选择导致的语义漂移问题

**关键词**：反事实解释, 感知度量, 测地线优化, 鲁棒特征, 视觉模型

## 3 点简述
- 核心问题：反事实解释方法因距离度量选择不当，易产生离流形伪影或对抗性崩溃
- 方法要点：基于鲁棒视觉特征诱导感知黎曼度量，沿测地线构建平滑、语义有效的反事实
- 实验或效果：在三个视觉数据集上优于基线，揭示标准度量下隐藏的失败模式

## 摘要（原文）

> Latent-space optimization methods for counterfactual explanations - framed as minimal semantic perturbations that change model predictions - inherit the ambiguity of Wachter et al.'s objective: the choice of distance metric dictates whether perturbations are meaningful or adversarial. Existing approaches adopt flat or misaligned geometries, leading to off-manifold artifacts, semantic drift, or adversarial collapse. We introduce Perceptual Counterfactual Geodesics (PCG), a method that constructs counterfactuals by tracing geodesics under a perceptually Riemannian metric induced from robust vision features. This geometry aligns with human perception and penalizes brittle directions, enabling smooth, on-manifold, semantically valid transitions. Experiments on three vision datasets show that PCG outperforms baselines and reveals failure modes hidden under standard metrics.

