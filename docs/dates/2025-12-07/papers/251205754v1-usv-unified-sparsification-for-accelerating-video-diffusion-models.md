---
layout: default
title: USV: Unified Sparsification for Accelerating Video Diffusion Models
---

# USV: Unified Sparsification for Accelerating Video Diffusion Models
**arXiv**：[2512.05754v1](https://arxiv.org/abs/2512.05754) · [PDF](https://arxiv.org/pdf/2512.05754.pdf)  
**作者**：Xinjian Wu, Hongmei Wang, Yuan Zhou, Qinglin Lu  

**一句话要点**：提出USV框架，通过统一稀疏化加速视频扩散模型，解决冗余计算瓶颈问题。

**关键词**：视频扩散模型, 稀疏化加速, 动态策略, 联合优化, 计算冗余, 去噪加速

## 3 点简述
- 视频扩散模型面临全局时空注意力二次复杂度和长迭代去噪轨迹的计算冗余。
- USV联合优化模型内部计算和采样过程，学习动态稀疏化策略，包括剪枝注意力连接、合并相似令牌和减少去噪步数。
- 实验显示USV在去噪过程加速达83.3%，端到端加速22.7%，同时保持高视觉保真度。

## 摘要（原文）

> The scalability of high-fidelity video diffusion models (VDMs) is constrained by two key sources of redundancy: the quadratic complexity of global spatio-temporal attention and the computational overhead of long iterative denoising trajectories. Existing accelerators -- such as sparse attention and step-distilled samplers -- typically target a single dimension in isolation and quickly encounter diminishing returns, as the remaining bottlenecks become dominant. In this work, we introduce USV (Unified Sparsification for Video diffusion models), an end-to-end trainable framework that overcomes this limitation by jointly orchestrating sparsification across both the model's internal computation and its sampling process. USV learns a dynamic, data- and timestep-dependent sparsification policy that prunes redundant attention connections, adaptively merges semantically similar tokens, and reduces denoising steps, treating them not as independent tricks but as coordinated actions within a single optimization objective. This multi-dimensional co-design enables strong mutual reinforcement among previously disjoint acceleration strategies. Extensive experiments on large-scale video generation benchmarks demonstrate that USV achieves up to 83.3% speedup in the denoising process and 22.7% end-to-end acceleration, while maintaining high visual fidelity. Our results highlight unified, dynamic sparsification as a practical path toward efficient, high-quality video generation.

