---
layout: default
title: Beyond Scaling: Assessing Strategic Reasoning and Rapid Decision-Making Capability of LLMs in Zero-sum Environments
---

# Beyond Scaling: Assessing Strategic Reasoning and Rapid Decision-Making Capability of LLMs in Zero-sum Environments
**arXiv**：[2603.09337v1](https://arxiv.org/abs/2603.09337) · [PDF](https://arxiv.org/pdf/2603.09337.pdf)  
**作者**：Yang Li, Xing Chen, Yutao Liu, Gege Qi, Yanxian BI, Zizhe Wang, Yunjian Zhang, Yao Zhu  

**一句话要点**：提出STAR基准以评估大语言模型在零和对抗环境中的战略推理与快速决策能力

**关键词**：战略推理评估, 零和对抗环境, 多智能体基准, 实时决策, 策略-执行差距

## 3 点简述
- 核心问题：现有评估忽视大语言模型在对抗性、时间敏感环境中的交互式决策能力
- 方法要点：引入STAR基准，支持回合制和实时设置，评估战略规划和战术执行
- 实验或效果：评估揭示策略-执行差距，推理密集型模型在实时场景中因延迟表现不佳

## 摘要（原文）

> Large Language Models (LLMs) have achieved strong performance on static reasoning benchmarks, yet their effectiveness as interactive agents operating in adversarial, time-sensitive environments remains poorly understood. Existing evaluations largely treat reasoning as a single-shot capability, overlooking the challenges of opponent-aware decision-making, temporal constraints, and execution under pressure. This paper introduces Strategic Tactical Agent Reasoning (STAR) Benchmark, a multi-agent evaluation framework that assesses LLMs through 1v1 zero-sum competitive interactions, framing reasoning as an iterative, adaptive decision-making process. STAR supports both turn-based and real-time settings, enabling controlled analysis of long-horizon strategic planning and fast-paced tactical execution within a unified environment. Built on a modular architecture with a standardized API and fully implemented execution engine, STAR facilitates reproducible evaluation and flexible task customization. To move beyond binary win-loss outcomes, we introduce a Strategic Evaluation Suite that assesses not only competitive success but also the quality of strategic behavior, such as execution efficiency and outcome stability. Extensive pairwise evaluations reveal a pronounced strategy-execution gap: while reasoning-intensive models dominate turn-based settings, their inference latency often leads to inferior performance in real-time scenarios, where faster instruction-tuned models prevail. These results show that strategic intelligence in interactive environments depends not only on reasoning depth, but also on the ability to translate plans into timely actions, positioning STAR as a principled benchmark for studying this trade-off in competitive, dynamic settings.

