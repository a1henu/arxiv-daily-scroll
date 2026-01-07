---
layout: default
title: ToxiGAN: Toxic Data Augmentation via LLM-Guided Directional Adversarial Generation
---

# ToxiGAN: Toxic Data Augmentation via LLM-Guided Directional Adversarial Generation
**arXiv**：[2601.03121v1](https://arxiv.org/abs/2601.03121) · [PDF](https://arxiv.org/pdf/2601.03121.pdf)  
**作者**：Peiran Li, Jan Fillies, Adrian Paschke  

**一句话要点**：提出ToxiGAN框架，通过LLM引导的定向对抗生成增强毒性数据，以提升毒性分类的鲁棒性。

**关键词**：毒性数据增强, 对抗生成, LLM引导, 语义压舱石, 定向训练, 仇恨言论分类

## 3 点简述
- 核心问题：毒性数据增强面临监督有限和分布偏斜的挑战，传统方法易导致模式崩溃和语义漂移。
- 方法要点：结合对抗生成与LLM语义引导，采用两步定向训练策略，利用LLM生成的中性文本作为语义压舱石。
- 实验或效果：在四个仇恨言论基准测试中，ToxiGAN在宏F1和仇恨F1上平均表现最强，优于传统和基于LLM的增强方法。

## 摘要（原文）

> Augmenting toxic language data in a controllable and class-specific manner is crucial for improving robustness in toxicity classification, yet remains challenging due to limited supervision and distributional skew. We propose ToxiGAN, a class-aware text augmentation framework that combines adversarial generation with semantic guidance from large language models (LLMs). To address common issues in GAN-based augmentation such as mode collapse and semantic drift, ToxiGAN introduces a two-step directional training strategy and leverages LLM-generated neutral texts as semantic ballast. Unlike prior work that treats LLMs as static generators, our approach dynamically selects neutral exemplars to provide balanced guidance. Toxic samples are explicitly optimized to diverge from these exemplars, reinforcing class-specific contrastive signals. Experiments on four hate speech benchmarks show that ToxiGAN achieves the strongest average performance in both macro-F1 and hate-F1, consistently outperforming traditional and LLM-based augmentation methods. Ablation and sensitivity analyses further confirm the benefits of semantic ballast and directional training in enhancing classifier robustness.

