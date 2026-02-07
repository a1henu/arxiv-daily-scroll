---
layout: default
title: FlashBlock: Attention Caching for Efficient Long-Context Block Diffusion
---

# FlashBlock: Attention Caching for Efficient Long-Context Block Diffusion
**arXiv**：[2602.05305v1](https://arxiv.org/abs/2602.05305) · [PDF](https://arxiv.org/pdf/2602.05305.pdf)  
**作者**：Zhuokun Chen, Jianfei Cai, Bohan Zhuang  

**一句话要点**：提出FlashBlock注意力缓存机制，以高效处理长上下文块扩散中的计算冗余问题。

**关键词**：注意力缓存, 块扩散, 长上下文生成, KV缓存优化, 视频生成, 扩散语言模型

## 3 点简述
- 核心问题：块扩散在长上下文设置中，因重复计算注意力于增长的KV缓存而产生显著开销。
- 方法要点：基于块内注意力变化大、块外注意力稳定的观察，设计缓存块外注意力输出以重用。
- 实验或效果：在扩散语言模型和视频生成中，提升吞吐量达1.44倍，减少注意力时间达1.6倍，质量影响可忽略。

## 摘要（原文）

> Generating long-form content, such as minute-long videos and extended texts, is increasingly important for modern generative models. Block diffusion improves inference efficiency via KV caching and block-wise causal inference and has been widely adopted in diffusion language models and video generation. However, in long-context settings, block diffusion still incurs substantial overhead from repeatedly computing attention over a growing KV cache. We identify an underexplored property of block diffusion: cross-step redundancy of attention within a block. Our analysis shows that attention outputs from tokens outside the current block remain largely stable across diffusion steps, while block-internal attention varies significantly. Based on this observation, we propose FlashBlock, a cached block-external attention mechanism that reuses stable attention output, reducing attention computation and KV cache access without modifying the diffusion process. Moreover, FlashBlock is orthogonal to sparse attention and can be combined as a complementary residual reuse strategy, substantially improving model accuracy under aggressive sparsification. Experiments on diffusion language models and video generation demonstrate up to 1.44$\times$ higher token throughput and up to 1.6$\times$ reduction in attention time, with negligible impact on generation quality. Project page: https://caesarhhh.github.io/FlashBlock/.

