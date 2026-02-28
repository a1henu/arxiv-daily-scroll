---
layout: default
title: Unsupervised Continual Learning for Amortized Bayesian Inference
---

# Unsupervised Continual Learning for Amortized Bayesian Inference
**arXiv**：[2602.22884v1](https://arxiv.org/abs/2602.22884) · [PDF](https://arxiv.org/pdf/2602.22884.pdf)  
**作者**：Aayush Mishra, Šimon Kucharský, Paul-Christian Bürkner  

**一句话要点**：提出无监督持续学习框架以解决摊销贝叶斯推断在模型误设和序列数据下的性能退化问题。

**关键词**：摊销贝叶斯推断, 无监督持续学习, 自一致性训练, 灾难性遗忘, 模型误设, 序列数据

## 3 点简述
- 核心问题：摊销贝叶斯推断在模型误设和序列数据中易性能退化，现有方法局限于静态单任务。
- 方法要点：通过解耦模拟预训练与无监督序列自一致性微调，结合回放或弹性权重巩固缓解灾难性遗忘。
- 实验或效果：在三个案例中显著减轻遗忘，后验估计优于标准模拟训练，更接近MCMC参考。

## 摘要（原文）

> Amortized Bayesian Inference (ABI) enables efficient posterior estimation using generative neural networks trained on simulated data, but often suffers from performance degradation under model misspecification. While self-consistency (SC) training on unlabeled empirical data can enhance network robustness, current approaches are limited to static, single-task settings and fail to handle sequentially arriving data or distribution shifts. We propose a continual learning framework for ABI that decouples simulation-based pre-training from unsupervised sequential SC fine-tuning on real-world data. To address the challenge of catastrophic forgetting, we introduce two adaptation strategies: (1) SC with episodic replay, utilizing a memory buffer of past observations, and (2) SC with elastic weight consolidation, which regularizes updates to preserve task-critical parameters. Across three diverse case studies, our methods significantly mitigate forgetting and yield posterior estimates that outperform standard simulation-based training, achieving estimates closer to MCMC reference, providing a viable path for trustworthy ABI across a range of different tasks.

