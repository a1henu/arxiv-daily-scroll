---
layout: default
title: ZSPAPrune: Zero-Shot Prompt-Aware Token Pruning for Vision-Language Models
---

# ZSPAPrune: Zero-Shot Prompt-Aware Token Pruning for Vision-Language Models
**arXiv**：[2510.17197v1](https://arxiv.org/abs/2510.17197) · [PDF](https://arxiv.org/pdf/2510.17197.pdf)  
**作者**：Pu Zhang, Yuwei Li, Xingyuan Xian, Guoming Tang  

**一句话要点**：提出零样本提示感知令牌剪枝方法以降低视觉语言模型推理成本

**关键词**：视觉语言模型, 令牌剪枝, 零样本学习, 推理优化, 提示感知

## 3 点简述
- 视觉语言模型输入大导致视觉令牌冗余，增加推理开销
- 基于提示感知建模剪枝，平衡任务相关性与信息多样性
- 实验显示剪枝90%令牌时性能接近最优，显著减少内存和延迟

## 摘要（原文）

> As the capabilities of Vision-Language Models (VLMs) advance, they can
> process increasingly large inputs, which, unlike in LLMs, generates significant
> visual token redundancy and leads to prohibitive inference costs. While many
> methods aim to reduce these costs by pruning visual tokens, existing
> approaches, whether based on attention or diversity, typically neglect the
> guidance of the text prompt and thus fail to prioritize task relevance. In this
> work, we propose a novel, zero-shot method that reframes the problem by
> introducing a prompt-aware perspective, explicitly modeling visual token
> pruning as a balance between task relevance and information diversity. Our
> hierarchical approach first selects a core set of task-relevant visual tokens
> and then supplements them with diversity tokens to preserve broader context.
> Experiments across multiple models and benchmarks show that our method achieves
> performance that matches or surpasses the state-of-the-art with only minimal
> accuracy loss, even when pruning up to 90\% of the tokens. Furthermore, these
> gains are accompanied by significant reductions in GPU memory footprint and
> inference latency.

