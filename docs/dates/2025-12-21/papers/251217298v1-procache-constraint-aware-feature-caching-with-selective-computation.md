---
layout: default
title: ProCache: Constraint-Aware Feature Caching with Selective Computation for Diffusion Transformer Acceleration
---

# ProCache: Constraint-Aware Feature Caching with Selective Computation for Diffusion Transformer Acceleration
**arXiv**：[2512.17298v1](https://arxiv.org/abs/2512.17298) · [PDF](https://arxiv.org/pdf/2512.17298.pdf)  
**作者**：Fanpu Cao, Yaofo Chen, Zeng You, Wei Luo, Cen Chen  

**一句话要点**：提出ProCache框架，通过约束感知缓存和选择性计算加速扩散Transformer推理

**关键词**：扩散Transformer, 特征缓存, 推理加速, 选择性计算, 约束优化, 生成模型

## 3 点简述
- 核心问题：扩散Transformer计算成本高，现有特征缓存方法因均匀间隔和误差累积导致性能下降
- 方法要点：基于离线约束采样生成非均匀缓存模式，并在缓存段内对深层块和高重要性令牌进行选择性计算
- 实验或效果：在PixArt-alpha和DiT上实现最高2.90倍加速，质量损失可忽略，优于先前缓存方法

## 摘要（原文）

> Diffusion Transformers (DiTs) have achieved state-of-the-art performance in generative modeling, yet their high computational cost hinders real-time deployment. While feature caching offers a promising training-free acceleration solution by exploiting temporal redundancy, existing methods suffer from two key limitations: (1) uniform caching intervals fail to align with the non-uniform temporal dynamics of DiT, and (2) naive feature reuse with excessively large caching intervals can lead to severe error accumulation. In this work, we analyze the evolution of DiT features during denoising and reveal that both feature changes and error propagation are highly time- and depth-varying. Motivated by this, we propose ProCache, a training-free dynamic feature caching framework that addresses these issues via two core components: (i) a constraint-aware caching pattern search module that generates non-uniform activation schedules through offline constrained sampling, tailored to the model's temporal characteristics; and (ii) a selective computation module that selectively computes within deep blocks and high-importance tokens for cached segments to mitigate error accumulation with minimal overhead. Extensive experiments on PixArt-alpha and DiT demonstrate that ProCache achieves up to 1.96x and 2.90x acceleration with negligible quality degradation, significantly outperforming prior caching-based methods.

