---
layout: default
title: ASTRA-bench: Evaluating Tool-Use Agent Reasoning and Action Planning with Personal User Context
---

# ASTRA-bench: Evaluating Tool-Use Agent Reasoning and Action Planning with Personal User Context
**arXiv**：[2603.01357v1](https://arxiv.org/abs/2603.01357) · [PDF](https://arxiv.org/pdf/2603.01357.pdf)  
**作者**：Zidi Xiu, David Q. Sun, Kevin Cheng, Maitrik Patel, Josh Date, Yizhe Zhang, Jiarui Lu, Omar Attia, Raviteja Vemulapalli, Oncel Tuzel, Meng Cao, Samy Bengio  

**一句话要点**：提出ASTRA-bench基准，以评估工具使用代理在个人用户上下文中的推理与行动规划能力。

**关键词**：工具使用代理, 个人上下文推理, 行动规划基准, 事件驱动场景生成, 模型性能评估

## 3 点简述
- 核心问题：现有基准多为上下文无关和单轮交互，难以评估AI处理动态个人数据和复杂意图的能力。
- 方法要点：基于事件驱动管道生成2,413个场景，融合时间演化个人上下文、交互工具箱和复杂用户意图。
- 实验或效果：评估显示先进模型在高复杂度条件下性能显著下降，参数生成成为主要瓶颈。

## 摘要（原文）

> Next-generation AI must manage vast personal data, diverse tools, and multi-step reasoning, yet most benchmarks remain context-free and single-turn. We present ASTRA-bench (Assistant Skills in Tool-use, Reasoning \& Action-planning), a benchmark that uniquely unifies time-evolving personal context with an interactive toolbox and complex user intents. Our event-driven pipeline generates 2,413 scenarios across four protagonists, grounded in longitudinal life events and annotated by referential, functional, and informational complexity. Evaluation of state-of-the-art models (e.g., Claude-4.5-Opus, DeepSeek-V3.2) reveals significant performance degradation under high-complexity conditions, with argument generation emerging as the primary bottleneck. These findings expose critical limitations in current agents' ability to ground reasoning within messy personal context and orchestrate reliable multi-step plans. We release ASTRA-bench with a full execution environment and evaluation scripts to provide a diagnostic testbed for developing truly context-aware AI assistants.

