---
layout: default
title: Stopping Computation for Converged Tokens in Masked Diffusion-LM Decoding
---

# Stopping Computation for Converged Tokens in Masked Diffusion-LM Decoding
**arXiv**：[2602.06412v1](https://arxiv.org/abs/2602.06412) · [PDF](https://arxiv.org/pdf/2602.06412.pdf)  
**作者**：Daisuke Oba, Danushka Bollegala, Masahiro Kaneko, Naoaki Okazaki  

**一句话要点**：提出SureLock方法以减少掩码扩散语言模型解码中的计算浪费

**关键词**：掩码扩散语言模型, 计算优化, 解码加速, 注意力机制, 生成质量保持

## 3 点简述
- 掩码扩散语言模型在解码时对所有位置重复计算，即使未掩码令牌已稳定，导致计算浪费。
- SureLock在未掩码位置后验稳定时锁定该位置，跳过其查询投影和前馈子层，缓存注意力键值供其他位置使用。
- 在LLaDA-8B上，SureLock减少算法FLOPs 30-50%，保持生成质量，并提供理论分析确保概率偏差有界。

## 摘要（原文）

> Masked Diffusion Language Models generate sequences via iterative sampling that progressively unmasks tokens. However, they still recompute the attention and feed-forward blocks for every token position at every step -- even when many unmasked tokens are essentially fixed, resulting in substantial waste in compute. We propose SureLock: when the posterior at an unmasked position has stabilized across steps (our sure condition), we lock that position -- thereafter skipping its query projection and feed-forward sublayers -- while caching its attention keys and values so other positions can continue to attend to it. This reduces the dominant per-iteration computational cost from $O(N^2d)$ to $O(MNd)$ where $N$ is the sequence length, $M$ is the number of unlocked token positions, and $d$ is the model dimension. In practice, $M$ decreases as the iteration progresses, yielding substantial savings. On LLaDA-8B, SureLock reduces algorithmic FLOPs by 30--50% relative to the same sampler without locking, while maintaining comparable generation quality. We also provide a theoretical analysis to justify the design rationale of SureLock: monitoring only the local KL at the lock step suffices to bound the deviation in final token probabilities. Our code will be available at https://daioba.github.io/surelock .

