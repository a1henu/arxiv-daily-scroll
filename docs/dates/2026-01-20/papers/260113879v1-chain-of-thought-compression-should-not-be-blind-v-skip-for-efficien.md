---
layout: default
title: Chain-of-Thought Compression Should Not Be Blind: V-Skip for Efficient Multimodal Reasoning via Dual-Path Anchoring
---

# Chain-of-Thought Compression Should Not Be Blind: V-Skip for Efficient Multimodal Reasoning via Dual-Path Anchoring
**arXiv**：[2601.13879v1](https://arxiv.org/abs/2601.13879) · [PDF](https://arxiv.org/pdf/2601.13879.pdf)  
**作者**：Dongxu Zhang, Yiding Sun, Cheng Tan, Wenbiao Yan, Ning Yang, Jihua Zhu, Hiajun Zhang  

**一句话要点**：提出V-Skip方法，通过双路径锚定解决多模态推理中链式思维压缩的视觉遗忘问题，实现高效推理。

**关键词**：多模态推理, 链式思维压缩, 视觉锚定, 令牌剪枝, 信息瓶颈优化, 双路径门控

## 3 点简述
- 核心问题：链式思维推理在多模态大语言模型中导致高延迟，且现有压缩方法因盲目应用文本指标引发视觉遗忘幻觉。
- 方法要点：V-Skip将令牌剪枝重构为视觉锚定信息瓶颈优化，利用双路径门控机制结合语言惊奇度和跨模态注意力流评估重要性。
- 实验或效果：在Qwen2-VL和Llama-3.2模型上实现2.9倍加速，精度损失可忽略，在DocVQA上超越基线30%以上。

## 摘要（原文）

> While Chain-of-Thought (CoT) reasoning significantly enhances the performance of Multimodal Large Language Models (MLLMs), its autoregressive nature incurs prohibitive latency constraints. Current efforts to mitigate this via token compression often fail by blindly applying text-centric metrics to multimodal contexts. We identify a critical failure mode termed Visual Amnesia, where linguistically redundant tokens are erroneously pruned, leading to hallucinations. To address this, we introduce V-Skip that reformulates token pruning as a Visual-Anchored Information Bottleneck (VA-IB) optimization problem. V-Skip employs a dual-path gating mechanism that weighs token importance through both linguistic surprisal and cross-modal attention flow, effectively rescuing visually salient anchors. Extensive experiments on Qwen2-VL and Llama-3.2 families demonstrate that V-Skip achieves a $2.9\times$ speedup with negligible accuracy loss. Specifically, it preserves fine-grained visual details, outperforming other baselines over 30\% on the DocVQA.

