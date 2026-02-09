---
layout: default
title: Evolutionary Generation of Multi-Agent Systems
---

# Evolutionary Generation of Multi-Agent Systems
**arXiv**：[2602.06511v1](https://arxiv.org/abs/2602.06511) · [PDF](https://arxiv.org/pdf/2602.06511.pdf)  
**作者**：Yuntong Hu, Matthew Trager, Yuting Zhang, Yi Zhang, Shuo Yang, Wei Xia, Stefano Soatto  

**一句话要点**：提出EvoMAS以进化生成多智能体系统配置，提升任务性能与鲁棒性。

**关键词**：多智能体系统, 进化算法, 配置生成, 大语言模型, 任务性能

## 3 点简述
- 问题：基于LLM的多智能体系统设计依赖人工或模板，易导致可执行性差与泛化困难。
- 方法：将MAS生成视为配置生成，通过进化算法在配置空间中进行反馈引导的突变与交叉。
- 效果：在BBEH、SWE-Bench等基准上超越人工设计与现有方法，提高可执行性与鲁棒性。

## 摘要（原文）

> Large language model (LLM)-based multi-agent systems (MAS) show strong promise for complex reasoning, planning, and tool-augmented tasks, but designing effective MAS architectures remains labor-intensive, brittle, and hard to generalize. Existing automatic MAS generation methods either rely on code generation, which often leads to executability and robustness failures, or impose rigid architectural templates that limit expressiveness and adaptability. We propose Evolutionary Generation of Multi-Agent Systems (EvoMAS), which formulates MAS generation as structured configuration generation. EvoMAS performs evolutionary generation in configuration space. Specifically, EvoMAS selects initial configurations from a pool, applies feedback-conditioned mutation and crossover guided by execution traces, and iteratively refines both the candidate pool and an experience memory. We evaluate EvoMAS on diverse benchmarks, including BBEH, SWE-Bench, and WorkBench, covering reasoning, software engineering, and tool-use tasks. EvoMAS consistently improves task performance over both human-designed MAS and prior automatic MAS generation methods, while producing generated systems with higher executability and runtime robustness. EvoMAS outperforms the agent evolution method EvoAgent by +10.5 points on BBEH reasoning and +7.1 points on WorkBench. With Claude-4.5-Sonnet, EvoMAS also reaches 79.1% on SWE-Bench-Verified, matching the top of the leaderboard.

