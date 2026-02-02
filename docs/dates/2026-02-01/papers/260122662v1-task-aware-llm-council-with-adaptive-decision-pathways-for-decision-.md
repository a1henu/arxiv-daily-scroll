---
layout: default
title: Task-Aware LLM Council with Adaptive Decision Pathways for Decision Support
---

# Task-Aware LLM Council with Adaptive Decision Pathways for Decision Support
**arXiv**：[2601.22662v1](https://arxiv.org/abs/2601.22662) · [PDF](https://arxiv.org/pdf/2601.22662.pdf)  
**作者**：Wei Zhu, Lixing Yu, Hao-Ren Yao, Zhiwen Tang, Kun Yue  

**一句话要点**：提出任务感知LLM委员会框架，通过自适应决策路径提升决策支持能力

**关键词**：任务感知路由, 蒙特卡洛树搜索, LLM委员会, 决策支持, 自适应规划

## 3 点简述
- 核心问题：现有方法忽视LLM的专业化差异，难以适应不同任务需求
- 方法要点：结合LLM委员会与蒙特卡洛树搜索，实现动态专家选择和语义匹配路由
- 实验或效果：在WebShop等任务上验证了更高的任务成功率和搜索效率

## 摘要（原文）

> Large language models (LLMs) have shown strong capabilities across diverse decision-making tasks. However, existing approaches often overlook the specialization differences among available models, treating all LLMs as uniformly applicable regardless of task characteristics. This limits their ability to adapt to varying reasoning demands and task complexities. In this work, we propose Task-Aware LLM Council (TALC), a task-adaptive decision framework that integrates a council of LLMs with Monte Carlo Tree Search (MCTS) to enable dynamic expert selection and efficient multi-step planning. Each LLM is equipped with a structured success memory profile derived from prior task trajectories, enabling semantic matching between current reasoning context and past successes. At each decision point, TALC routes control to the most contextually appropriate model and estimates node value using a dual-signal mechanism that fuses model-based evaluations with historical utility scores. These signals are adaptively weighted based on intra-node variance and used to guide MCTS selection, allowing the system to balance exploration depth with planning confidence. Experiments on WebShop, HumanEval, and the Game of 24 demonstrate that TALC achieves superior task success rates and improved search efficiency compared to strong baselines, validating the benefits of specialization-aware routing and adaptive planning.

