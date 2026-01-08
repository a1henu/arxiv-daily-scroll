---
layout: default
title: ADEPT: Adaptive Dynamic Early-Exit Process for Transformers
---

# ADEPT: Adaptive Dynamic Early-Exit Process for Transformers
**arXiv**：[2601.03700v1](https://arxiv.org/abs/2601.03700) · [PDF](https://arxiv.org/pdf/2601.03700.pdf)  
**作者**：Sangmin Yoo, Srikanth Malla, Chiho Choi, Wei D. Lu, Joon Hee Choi  

**一句话要点**：提出ADEPT以解决Transformer推理中KV缓存瓶颈，实现动态早退

**关键词**：Transformer推理优化, 动态早退策略, KV缓存管理, 自适应计算, 语言模型效率, 令牌级早退

## 3 点简述
- 核心问题：早退策略在生成阶段仅适用于首个令牌或预填充阶段，KV缓存成为后续令牌生成瓶颈。
- 方法要点：引入自适应令牌级早退机制，基于令牌复杂度动态调整计算，并解耦跳过层的序列依赖。
- 实验或效果：在语言生成任务中效率提升达25%，下游分类任务速度提升4倍，性能改善达45%。

## 摘要（原文）

> The inference of large language models imposes significant computational workloads, often requiring the processing of billions of parameters. Although early-exit strategies have proven effective in reducing computational demands by halting inference earlier, they apply either to only the first token in the generation phase or at the prompt level in the prefill phase. Thus, the Key-Value (KV) cache for skipped layers remains a bottleneck for subsequent token generation, limiting the benefits of early exit. We introduce ADEPT (Adaptive Dynamic Early-exit Process for Transformers), a novel approach designed to overcome this issue and enable dynamic early exit in both the prefill and generation phases. The proposed adaptive token-level early-exit mechanism adjusts computation dynamically based on token complexity, optimizing efficiency without compromising performance. ADEPT further enhances KV generation procedure by decoupling sequential dependencies in skipped layers, making token-level early exit more practical. Experimental results demonstrate that ADEPT improves efficiency by up to 25% in language generation tasks and achieves a 4x speed-up in downstream classification tasks, with up to a 45% improvement in performance.

