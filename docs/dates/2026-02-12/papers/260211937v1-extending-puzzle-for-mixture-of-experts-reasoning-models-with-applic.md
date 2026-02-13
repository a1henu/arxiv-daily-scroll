---
layout: default
title: Extending Puzzle for Mixture-of-Experts Reasoning Models with Application to GPT-OSS Acceleration
---

# Extending Puzzle for Mixture-of-Experts Reasoning Models with Application to GPT-OSS Acceleration
**arXiv**：[2602.11937v1](https://arxiv.org/abs/2602.11937) · [PDF](https://arxiv.org/pdf/2602.11937.pdf)  
**作者**：Akhiad Bercovich, Nir Ailon, Vladimir Anisimov, Tomer Asida, Nave Assaf, Mohammad Dabbah, Ido Galil, Amnon Geifman, Yonatan Geifman, Izhak Golan, Roi Koren, Itay Levy, Zach Moshe, Pavlo Molchanov, Najeeb Nabwani, Mostofa Patwari, Omri Puny, Tomer Ronen, Itamar Schen, Elad Segal, Ido Shahaf, Oren Tropp, Ran Zilberstein, Ran El-Yaniv  

**一句话要点**：扩展Puzzle框架优化GPT-OSS推理，通过混合专家剪枝与量化提升效率

**关键词**：推理优化, 混合专家模型, 后训练架构搜索, 量化加速, 窗口注意力, 请求级效率

## 3 点简述
- 推理型LLMs生成长推理轨迹增加服务成本，需优化推理效率。
- 应用Puzzle框架进行后训练架构搜索，结合MoE剪枝、窗口注意力替换和FP8量化。
- 在保持准确性的同时，实现吞吐量提升和请求级效率改进，模型性能匹配或略超原版。

## 摘要（原文）

> Reasoning-focused LLMs improve answer quality by generating longer reasoning traces, but the additional tokens dramatically increase serving cost, motivating inference optimization. We extend and apply Puzzle, a post-training neural architecture search (NAS) framework, to gpt-oss-120B to produce gpt-oss-puzzle-88B, a deployment-optimized derivative. Our approach combines heterogeneous MoE expert pruning, selective replacement of full-context attention with window attention, FP8 KV-cache quantization with calibrated scales, and post-training reinforcement learning to recover accuracy, while maintaining low generation length. In terms of per-token speeds, on an 8XH100 node we achieve 1.63X and 1.22X throughput speedups in long-context and short-context settings, respectively. gpt-oss-puzzle-88B also delivers throughput speedups of 2.82X on a single NVIDIA H100 GPU. However, because token counts can change with reasoning effort and model variants, per-token throughput (tok/s) and latency (ms/token) do not necessarily lead to end-to-end speedups: a 2X throughput gain is erased if traces grow 2X. Conversely, throughput gains can be spent on more reasoning tokens to improve accuracy; we therefore advocate request-level efficiency metrics that normalize throughput by tokens generated and trace an accuracy--speed frontier across reasoning efforts. We show that gpt-oss-puzzle-88B improves over gpt-oss-120B along the entire frontier, delivering up to 1.29X higher request-level efficiency. Across various benchmarks, gpt-oss-puzzle-88B matches or slightly exceeds the parent on suite-average accuracy across reasoning efforts, with retention ranging from 100.8% (high) to 108.2% (low), showing that post-training architecture search can substantially reduce inference costs without sacrificing quality.

