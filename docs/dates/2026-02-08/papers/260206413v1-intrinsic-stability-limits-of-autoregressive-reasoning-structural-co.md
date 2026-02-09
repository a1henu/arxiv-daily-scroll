---
layout: default
title: Intrinsic Stability Limits of Autoregressive Reasoning: Structural Consequences for Long-Horizon Execution
---

# Intrinsic Stability Limits of Autoregressive Reasoning: Structural Consequences for Long-Horizon Execution
**arXiv**：[2602.06413v1](https://arxiv.org/abs/2602.06413) · [PDF](https://arxiv.org/pdf/2602.06413.pdf)  
**作者**：Hsien-Jyh Liao  

**一句话要点**：提出自回归推理存在内在稳定性极限，解释长视野任务性能下降的结构性原因。

**关键词**：自回归推理, 长视野任务, 稳定性极限, 结构化治理, 推理性能下降

## 3 点简述
- 核心问题：自回归推理在长视野任务中性能急剧下降，传统解释如任务复杂性不完整。
- 方法要点：理论证明单路径自回归决策优势随执行长度指数衰减，导致推理链稳定性极限。
- 实验或效果：合成环境和真实任务实验显示性能断崖，与理论预测一致，支持结构化治理需求。

## 摘要（原文）

> Large language models (LLMs) demonstrate remarkable reasoning capabilities, yet their performance often deteriorates sharply in long-horizon tasks, exhibiting systematic breakdown beyond certain scales. Conventional explanations primarily attribute this phenomenon to task complexity, such as combinatorial search explosion or long-term credit assignment challenges. In this work, we argue that these explanations are incomplete: even in linear, unbranched tasks without semantic ambiguity, autoregressive execution is subject to an intrinsic stability limit.
>   We propose that the fundamental constraint on long-horizon reasoning arises from process-level instability in autoregressive generation rather than solely from search or task complexity, reframing long-horizon reasoning as a problem of structural governance. We derive Theorem~A, showing that decision advantage in single-path autoregressive reasoning decays exponentially with execution length, imposing a fundamental bound on maintainable reasoning chains. This result implies a structural consequence: stable long-horizon reasoning requires discrete segmentation, naturally inducing graph-like execution structures such as directed acyclic graphs (DAGs).
>   Empirical studies in both synthetic environments and real TextWorld tasks reveal observable performance cliffs consistent with theoretical predictions. Our findings provide a dynamical perspective on long-horizon reasoning failure and suggest new limitations on maintaining long-term coherence under purely autoregressive architectures. Furthermore, we highlight that short-horizon evaluation protocols may obscure structural instability, indicating a potential shift from scaling toward structured governance in future reasoning systems.

