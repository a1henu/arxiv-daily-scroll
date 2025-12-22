---
layout: default
title: Dialectics for Artificial Intelligence
---

# Dialectics for Artificial Intelligence
**arXiv**：[2512.17373v1](https://arxiv.org/abs/2512.17373) · [PDF](https://arxiv.org/pdf/2512.17373.pdf)  
**作者**：Zhengmian Hu  

**一句话要点**：提出基于算法信息论的AI概念发现框架，以解决无监督概念学习与对齐问题。

**关键词**：概念发现, 算法信息论, 无监督学习, 多智能体对齐, 信息冗余

## 3 点简述
- 核心问题：AI能否从原始经验中无监督地发现人类概念，并处理概念的动态变化。
- 方法要点：将概念定义为信息对象，基于可逆一致性关系和冗余信息度量，驱动概念优化。
- 实验或效果：未知，但理论框架支持概念传输和多智能体对齐的通信效率分析。

## 摘要（原文）

> Can artificial intelligence discover, from raw experience and without human supervision, concepts that humans have discovered? One challenge is that human concepts themselves are fluid: conceptual boundaries can shift, split, and merge as inquiry progresses (e.g., Pluto is no longer considered a planet). To make progress, we need a definition of "concept" that is not merely a dictionary label, but a structure that can be revised, compared, and aligned across agents. We propose an algorithmic-information viewpoint that treats a concept as an information object defined only through its structural relation to an agent's total experience. The core constraint is determination: a set of parts forms a reversible consistency relation if any missing part is recoverable from the others (up to the standard logarithmic slack in Kolmogorov-style identities). This reversibility prevents "concepts" from floating free of experience and turns concept existence into a checkable structural claim. To judge whether a decomposition is natural, we define excess information, measuring the redundancy overhead introduced by splitting experience into multiple separately described parts. On top of these definitions, we formulate dialectics as an optimization dynamics: as new patches of information appear (or become contested), competing concepts bid to explain them via shorter conditional descriptions, driving systematic expansion, contraction, splitting, and merging. Finally, we formalize low-cost concept transmission and multi-agent alignment using small grounds/seeds that allow another agent to reconstruct the same concept under a shared protocol, making communication a concrete compute-bits trade-off.

