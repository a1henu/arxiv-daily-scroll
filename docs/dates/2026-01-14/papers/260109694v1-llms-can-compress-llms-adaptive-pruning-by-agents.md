---
layout: default
title: LLMs can Compress LLMs: Adaptive Pruning by Agents
---

# LLMs can Compress LLMs: Adaptive Pruning by Agents
**arXiv**：[2601.09694v1](https://arxiv.org/abs/2601.09694) · [PDF](https://arxiv.org/pdf/2601.09694.pdf)  
**作者**：Sai Varun Kodathala, Rakesh Vunnam  

**一句话要点**：提出基于智能代理的自适应剪枝方法，以解决大语言模型剪枝中的知识退化问题。

**关键词**：大语言模型剪枝, 自适应剪枝, 知识保留, 代理引导压缩, 无重训练剪枝

## 3 点简述
- 现有剪枝方法依赖均匀或启发式层稀疏度，导致事实知识严重退化。
- 引入基础模型作为代理，结合权重-激活指标和梯度重要性，迭代优化剪枝策略。
- 在45%稀疏度下，相比基线在MMLU准确率提升56%，事实知识保留改善19倍。

## 摘要（原文）

> As Large Language Models (LLMs) continue to scale, post-training pruning has emerged as a promising approach to reduce computational costs while preserving performance. Existing methods such as SparseGPT and Wanda achieve high sparsity through layer-wise weight reconstruction or activation-aware magnitude pruning, but rely on uniform or hand-crafted heuristics to determine per-layer sparsity ratios. Moreover, recent work has shown that pruned LLMs suffer from severe factual knowledge degradation, with structured pruning methods experiencing near-total collapse in factual question-answering capabilities. We introduce agent-guided pruning, where a foundation model acts as an adaptive pruning agent to intelligently select which layers to prune at each iteration while preserving critical knowledge pathways. Our method constructs layer-wise sensitivity profiles by combining Wanda-inspired weight-activation metrics with gradient importance scores, normalized as z-scores for model-agnostic comparison. These statistics are processed by an LLM agent equipped with self-reflection capabilities, enabling it to learn from previous pruning outcomes and iteratively refine its strategy. A checkpoint rollback mechanism maintains model quality by reverting when perplexity degradation exceeds a threshold. We evaluate our approach on Qwen3 models (4B and 8B parameters) at approximately 45% sparsity, demonstrating substantial improvements over structured pruning baselines: 56% relative improvement in MMLU accuracy, 19x better factual knowledge retention on FreebaseQA, and 69% lower perplexity degradation. Notably, our framework requires no retraining, operates in a model-agnostic manner, and exhibits effective self-correction with only 2-4 rollbacks across 21-40 iterations, demonstrating that foundation models can effectively guide the compression of other foundation models.

