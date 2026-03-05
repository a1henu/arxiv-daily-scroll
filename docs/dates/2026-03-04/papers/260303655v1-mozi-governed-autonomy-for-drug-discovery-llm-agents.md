---
layout: default
title: Mozi: Governed Autonomy for Drug Discovery LLM Agents
---

# Mozi: Governed Autonomy for Drug Discovery LLM Agents
**arXiv**：[2603.03655v1](https://arxiv.org/abs/2603.03655) · [PDF](https://arxiv.org/pdf/2603.03655.pdf)  
**作者**：He Cao, Siyu Liu, Fan Zhang, Zijing Liu, Hao Li, Bin Feng, Shengyuan Bai, Leqing Chen, Kai Xie, Yu Li  

**一句话要点**：提出Mozi架构以解决药物发现中LLM代理的治理与可靠性问题

**关键词**：药物发现, LLM代理, 治理架构, 技能图, 长程可靠性, 工具使用

## 3 点简述
- 核心问题：药物发现中LLM代理存在工具使用无约束和长程可靠性差，导致错误累积。
- 方法要点：采用双层架构，控制层实施治理与反思重规划，工作流层将药物发现阶段建模为技能图。
- 实验或效果：在PharmaBench基准上表现优于基线，并通过案例研究展示候选药物生成能力。

## 摘要（原文）

> Tool-augmented large language model (LLM) agents promise to unify scientific reasoning with computation, yet their deployment in high-stakes domains like drug discovery is bottlenecked by two critical barriers: unconstrained tool-use governance and poor long-horizon reliability. In dependency-heavy pharmaceutical pipelines, autonomous agents often drift into irreproducible trajectories, where early-stage hallucinations multiplicatively compound into downstream failures. To overcome this, we present Mozi, a dual-layer architecture that bridges the flexibility of generative AI with the deterministic rigor of computational biology. Layer A (Control Plane) establishes a governed supervisor--worker hierarchy that enforces role-based tool isolation, limits execution to constrained action spaces, and drives reflection-based replanning. Layer B (Workflow Plane) operationalizes canonical drug discovery stages -- from Target Identification to Lead Optimization -- as stateful, composable skill graphs. This layer integrates strict data contracts and strategic human-in-the-loop (HITL) checkpoints to safeguard scientific validity at high-uncertainty decision boundaries.
>   Operating on the design principle of ``free-form reasoning for safe tasks, structured execution for long-horizon pipelines,'' Mozi provides built-in robustness mechanisms and trace-level audibility to completely mitigate error accumulation. We evaluate Mozi on PharmaBench, a curated benchmark for biomedical agents, demonstrating superior orchestration accuracy over existing baselines. Furthermore, through end-to-end therapeutic case studies, we demonstrate Mozi's ability to navigate massive chemical spaces, enforce stringent toxicity filters, and generate highly competitive in silico candidates, effectively transforming the LLM from a fragile conversationalist into a reliable, governed co-scientist.

