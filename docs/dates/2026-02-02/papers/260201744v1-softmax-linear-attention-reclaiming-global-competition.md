---
layout: default
title: Softmax Linear Attention: Reclaiming Global Competition
---

# Softmax Linear Attention: Reclaiming Global Competition
**arXiv**：[2602.01744v1](https://arxiv.org/abs/2602.01744) · [PDF](https://arxiv.org/pdf/2602.01744.pdf)  
**作者**：Mingwei Xu, Xuan Lin, Xinnan Guo, Wanqing Xu, Wanyun Cui  

**一句话要点**：提出Softmax Linear Attention以在线性复杂度下恢复全局竞争机制，提升长上下文理解与检索鲁棒性。

**关键词**：线性注意力, 全局竞争机制, 多头注意力, 长上下文理解, 检索鲁棒性, 语言建模

## 3 点简述
- 线性注意力因移除softmax而缺乏全局竞争，导致表达力不足和长上下文噪声处理困难。
- SLA将softmax提升到头级别，利用多头作为语义槽，通过竞争门控动态选择相关子空间。
- 实验表明SLA增强RetNet等基线模型，在语言建模和长上下文基准中，尤其在噪声检索场景提升鲁棒性。

## 摘要（原文）

> While linear attention reduces the quadratic complexity of standard Transformers to linear time, it often lags behind in expressivity due to the removal of softmax normalization. This omission eliminates \emph{global competition}, a critical mechanism that enables models to sharply focus on relevant information amidst long-context noise. In this work, we propose \textbf{Softmax Linear Attention (SLA)}, a framework designed to restore this competitive selection without sacrificing efficiency. By lifting the softmax operation from the token level to the head level, SLA leverages attention heads as coarse semantic slots, applying a competitive gating mechanism to dynamically select the most relevant subspaces. This reintroduces the ``winner-take-all'' dynamics essential for precise retrieval and robust long-context understanding. Distinct from prior methods that focus on refining local kernel functions, SLA adopts a broader perspective by exploiting the higher-level multi-head aggregation structure. Extensive experiments demonstrate that SLA consistently enhances state-of-the-art linear baselines (RetNet, GLA, GDN) across language modeling and long-context benchmarks, particularly in challenging retrieval scenarios where it significantly boosts robustness against noise, validating its capability to restore precise focus while maintaining linear complexity.

