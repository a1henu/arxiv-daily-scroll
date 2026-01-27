---
layout: default
title: HalluGuard: Demystifying Data-Driven and Reasoning-Driven Hallucinations in LLMs
---

# HalluGuard: Demystifying Data-Driven and Reasoning-Driven Hallucinations in LLMs
**arXiv**：[2601.18753v1](https://arxiv.org/abs/2601.18753) · [PDF](https://arxiv.org/pdf/2601.18753.pdf)  
**作者**：Xinyue Zeng, Junhong Lin, Yujun Yan, Feng Guo, Liang Shi, Jun Wu, Dawei Zhou  

**一句话要点**：提出HalluGuard框架，基于NTK联合检测LLM的数据驱动和推理驱动幻觉。

**关键词**：大语言模型幻觉, 数据驱动幻觉, 推理驱动幻觉, NTK检测, 幻觉风险界, 多基准评估

## 3 点简述
- 核心问题：LLM幻觉源于数据驱动和推理驱动，现有方法泛化性不足。
- 方法要点：引入幻觉风险界理论框架，并基于NTK几何和表示设计检测分数。
- 实验或效果：在10个基准、11个基线、9个LLM上实现SOTA性能。

## 摘要（原文）

> The reliability of Large Language Models (LLMs) in high-stakes domains such as healthcare, law, and scientific discovery is often compromised by hallucinations. These failures typically stem from two sources: data-driven hallucinations and reasoning-driven hallucinations. However, existing detection methods usually address only one source and rely on task-specific heuristics, limiting their generalization to complex scenarios. To overcome these limitations, we introduce the Hallucination Risk Bound, a unified theoretical framework that formally decomposes hallucination risk into data-driven and reasoning-driven components, linked respectively to training-time mismatches and inference-time instabilities. This provides a principled foundation for analyzing how hallucinations emerge and evolve. Building on this foundation, we introduce HalluGuard, an NTK-based score that leverages the induced geometry and captured representations of the NTK to jointly identify data-driven and reasoning-driven hallucinations. We evaluate HalluGuard on 10 diverse benchmarks, 11 competitive baselines, and 9 popular LLM backbones, consistently achieving state-of-the-art performance in detecting diverse forms of LLM hallucinations.

