---
layout: default
title: GimmBO: Interactive Generative Image Model Merging via Bayesian Optimization
---

# GimmBO: Interactive Generative Image Model Merging via Bayesian Optimization
**arXiv**：[2601.18585v1](https://arxiv.org/abs/2601.18585) · [PDF](https://arxiv.org/pdf/2601.18585.pdf)  
**作者**：Chenxi Liu, Selena Ling, Alec Jacobson  

**一句话要点**：提出GimmBO以通过贝叶斯优化交互式探索扩散模型适配器合并

**关键词**：扩散模型, 适配器合并, 贝叶斯优化, 交互式探索, 图像生成

## 3 点简述
- 问题：手动调整适配器权重效率低，难以探索高维设计空间。
- 方法：采用两阶段贝叶斯优化后端，提升采样效率和收敛性。
- 效果：在模拟和用户研究中显示收敛改进、高成功率，优于基线。

## 摘要（原文）

> Fine-tuning-based adaptation is widely used to customize diffusion-based image generation, leading to large collections of community-created adapters that capture diverse subjects and styles. Adapters derived from the same base model can be merged with weights, enabling the synthesis of new visual results within a vast and continuous design space. To explore this space, current workflows rely on manual slider-based tuning, an approach that scales poorly and makes weight selection difficult, even when the candidate set is limited to 20-30 adapters. We propose GimmBO to support interactive exploration of adapter merging for image generation through Preferential Bayesian Optimization (PBO). Motivated by observations from real-world usage, including sparsity and constrained weight ranges, we introduce a two-stage BO backend that improves sampling efficiency and convergence in high-dimensional spaces. We evaluate our approach with simulated users and a user study, demonstrating improved convergence, high success rates, and consistent gains over BO and line-search baselines, and further show the flexibility of the framework through several extensions.

