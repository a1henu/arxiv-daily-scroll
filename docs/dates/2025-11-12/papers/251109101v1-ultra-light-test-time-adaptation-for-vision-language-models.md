---
layout: default
title: Ultra-Light Test-Time Adaptation for Vision--Language Models
---

# Ultra-Light Test-Time Adaptation for Vision--Language Models
**arXiv**：[2511.09101v1](https://arxiv.org/abs/2511.09101) · [PDF](https://arxiv.org/pdf/2511.09101.pdf)  
**作者**：Byunghyun Kim  

**一句话要点**：提出超轻测试时适应方法，解决视觉语言模型在域偏移下的性能下降问题

**关键词**：测试时适应, 视觉语言模型, 域偏移, 贝叶斯更新, 无训练优化, 在线学习

## 3 点简述
- 视觉语言模型在域偏移时面临特征漂移、类先验不匹配和校准错误问题
- 采用无训练、无反向传播的在线EM风格方法，仅调整logit级参数
- 在多个基准测试中提升准确率并降低校准误差，延迟开销低于8%

## 摘要（原文）

> Vision-Language Models (VLMs) such as CLIP achieve strong zero-shot recognition by comparing image embeddings to text-derived class prototypes. However, under domain shift, they suffer from feature drift, class-prior mismatch, and severe miscalibration. Existing test-time adaptation (TTA) methods often require backpropagation through large backbones, covariance estimation, or heavy memory/state, which is problematic for streaming and edge scenarios. We propose Ultra-Light Test-Time Adaptation (UL-TTA), a fully training-free and backprop-free framework that freezes the backbone and adapts only logit-level parameters: class prototypes, class priors, and temperature. UL-TTA performs an online EM-style procedure with (i) selective sample filtering to use only confident predictions, (ii) closed-form Bayesian updates for prototypes and priors anchored by text and Dirichlet priors, (iii) decoupled temperatures for prediction vs. calibration, and (iv) lightweight guards (norm clipping, prior KL constraints, smoothed temperature) to prevent drift in long streams. Across large-scale cross-domain and OOD benchmarks (PACS, Office-Home, DomainNet, Terra Incognita, ImageNet-R/A/V2/Sketch; ~726K test samples) and strong TTA baselines including Tent, T3A, CoTTA, SAR, Tip-Adapter, and FreeTTA, UL-TTA consistently improves top-1 accuracy (e.g., +4.7 points over zero-shot CLIP on average) while reducing ECE by 20-30%, with less than 8% latency overhead. Long-stream experiments up to 200K samples show no collapse. Our results demonstrate that logit-level Bayesian adaptation is sufficient to obtain state-of-the-art accuracy-calibration trade-offs for VLMs under domain shift, without updating any backbone parameters.

