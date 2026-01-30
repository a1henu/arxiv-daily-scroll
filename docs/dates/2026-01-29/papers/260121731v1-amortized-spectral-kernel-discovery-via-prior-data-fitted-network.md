---
layout: default
title: Amortized Spectral Kernel Discovery via Prior-Data Fitted Network
---

# Amortized Spectral Kernel Discovery via Prior-Data Fitted Network
**arXiv**：[2601.21731v1](https://arxiv.org/abs/2601.21731) · [PDF](https://arxiv.org/pdf/2601.21731.pdf)  
**作者**：Kaustubh Sharma, Srijan Tiwari, Ojasva Nema, Parikshit Pareek  

**一句话要点**：提出基于先验数据拟合网络的摊销谱核发现框架，以解决下游任务中核函数不透明问题。

**关键词**：先验数据拟合网络, 谱核发现, 摊销推理, 注意力机制, 高斯过程回归, 核函数估计

## 3 点简述
- 先验数据拟合网络（PFNs）在摊销推理中高效，但缺乏对学习先验和核函数的透明访问，阻碍了需要显式协方差模型的下游应用。
- 通过机制分析识别注意力潜在输出为关键中介，提出解码器架构将PFN潜在映射到显式谱密度估计和静止核函数。
- 在单实现和多实现场景中验证，解码器能恢复复杂多峰谱混合，支持高斯过程回归，推理时间比优化基线大幅减少。

## 摘要（原文）

> Prior-Data Fitted Networks (PFNs) enable efficient amortized inference but lack transparent access to their learned priors and kernels. This opacity hinders their use in downstream tasks, such as surrogate-based optimization, that require explicit covariance models. We introduce an interpretability-driven framework for amortized spectral discovery from pre-trained PFNs with decoupled attention. We perform a mechanistic analysis on a trained PFN that identifies attention latent output as the key intermediary, linking observed function data to spectral structure. Building on this insight, we propose decoder architectures that map PFN latents to explicit spectral density estimates and corresponding stationary kernels via Bochner's theorem. We study this pipeline in both single-realization and multi-realization regimes, contextualizing theoretical limits on spectral identifiability and proving consistency when multiple function samples are available. Empirically, the proposed decoders recover complex multi-peak spectral mixtures and produce explicit kernels that support Gaussian process regression with accuracy comparable to PFNs and optimization-based baselines, while requiring only a single forward pass. This yields orders-of-magnitude reductions in inference time compared to optimization-based baselines.

