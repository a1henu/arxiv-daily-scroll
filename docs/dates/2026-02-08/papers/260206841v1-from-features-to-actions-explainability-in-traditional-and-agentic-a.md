---
layout: default
title: From Features to Actions: Explainability in Traditional and Agentic AI Systems
---

# From Features to Actions: Explainability in Traditional and Agentic AI Systems
**arXiv**：[2602.06841v1](https://arxiv.org/abs/2602.06841) · [PDF](https://arxiv.org/pdf/2602.06841.pdf)  
**作者**：Sindhuja Chaduvula, Jessee Ho, Kina Kim, Aravind Narayanan, Mahshid Alinoori, Muskan Garg, Dhanesh Ramachandram, Shaina Raza  

**一句话要点**：比较静态与智能体AI系统的可解释性方法，强调轨迹级诊断的重要性

**关键词**：可解释AI, 智能体系统, 轨迹诊断, 归因方法, 状态跟踪, 基准测试

## 3 点简述
- 核心问题：传统可解释性方法在智能体AI系统中是否适用，如何解释多步决策行为
- 方法要点：对比基于归因的解释与基于轨迹的诊断，在静态分类和智能体基准测试中进行实证分析
- 实验或效果：归因方法在静态设置中稳定，但在智能体轨迹中不可靠；轨迹评估能定位行为故障，揭示状态跟踪不一致的影响

## 摘要（原文）

> Over the last decade, explainable AI has primarily focused on interpreting individual model predictions, producing post-hoc explanations that relate inputs to outputs under a fixed decision structure. Recent advances in large language models (LLMs) have enabled agentic AI systems whose behaviour unfolds over multi-step trajectories. In these settings, success and failure are determined by sequences of decisions rather than a single output. While useful, it remains unclear how explanation approaches designed for static predictions translate to agentic settings where behaviour emerges over time. In this work, we bridge the gap between static and agentic explainability by comparing attribution-based explanations with trace-based diagnostics across both settings. To make this distinction explicit, we empirically compare attribution-based explanations used in static classification tasks with trace-based diagnostics used in agentic benchmarks (TAU-bench Airline and AssistantBench). Our results show that while attribution methods achieve stable feature rankings in static settings (Spearman $ρ= 0.86$), they cannot be applied reliably to diagnose execution-level failures in agentic trajectories. In contrast, trace-grounded rubric evaluation for agentic settings consistently localizes behaviour breakdowns and reveals that state tracking inconsistency is 2.7$\times$ more prevalent in failed runs and reduces success probability by 49\%. These findings motivate a shift towards trajectory-level explainability for agentic systems when evaluating and diagnosing autonomous AI behaviour.
>   Resources:
>   https://github.com/VectorInstitute/unified-xai-evaluation-framework https://vectorinstitute.github.io/unified-xai-evaluation-framework

