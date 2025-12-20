---
layout: default
title: AlignMerge - Alignment-Preserving Large Language Model Merging via Fisher-Guided Geometric Constraints
---

# AlignMerge - Alignment-Preserving Large Language Model Merging via Fisher-Guided Geometric Constraints
**arXiv**：[2512.16245v1](https://arxiv.org/abs/2512.16245) · [PDF](https://arxiv.org/pdf/2512.16245.pdf)  
**作者**：Aniruddha Roy, Jyoti Patel, Aman Chadha, Vinija Jain, Amitava Das  

**一句话要点**：提出AlignMerge框架，通过Fisher引导的几何约束实现对齐保持的大语言模型合并。

**关键词**：大语言模型合并, 对齐保持, Fisher几何, 几何约束优化, 安全模型融合

## 3 点简述
- 核心问题：标准模型合并方法可能破坏对齐性，导致安全风险。
- 方法要点：在Fisher几何中定义对齐子空间，优化几何、对齐和预算损失函数。
- 实验或效果：在多个模型家族中提升对齐指标，同时保持或超越专家模型性能。

## 摘要（原文）

> Merging large language models (LLMs) is a practical way to compose capabilities from multiple fine-tuned checkpoints without retraining. Yet standard schemes (linear weight soups, task vectors, and Fisher-weighted averaging) can preserve loss while quietly destroying alignment. We argue that merging is not a numerical trick but a geometry-constrained operation around an already-aligned anchor: fusion must be steered to respect safety geometry, not validated post hoc.
>   We introduce AlignMerge, a geometry-aware merging framework that makes alignment an explicit invariant. In a local Fisher chart around an instruction-tuned base, we estimate an alignment subspace with projector P_A and optimize:
>   L_AlignMerge = L_geo + lambda_align * L_align + lambda_bud * L_bud,
>   where L_geo keeps the merge close to its experts in Fisher-Rao geometry, L_align penalizes motion along alignment-sensitive directions, and L_bud enforces a soft alignment budget. As the alignment functional we use the decoding-invariant Alignment Quality Index (AQI), a latent-space criterion that captures how cleanly aligned and misaligned behaviors separate in representation space.
>   Across five model families (LLaMA-3 8B, Mistral 7B, Qwen 2, Phi-3.5, Gemma 2), merging safety anchors with task experts, AlignMerge improves alignment metrics (AQI, toxicity, LLM-judge alignment) while matching or exceeding the best expert on instruction-following, reasoning, and helpfulness. It also exhibits smaller alignment-subspace drift and fewer budget violations than Fisher soups, TIES, SafeMerge, and MergeAlign. These results make alignment-preserving merging a first-class design goal and suggest a path to geometry-aware composition of future foundation models.

