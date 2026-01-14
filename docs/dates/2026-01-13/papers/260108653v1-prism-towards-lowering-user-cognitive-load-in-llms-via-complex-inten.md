---
layout: default
title: Prism: Towards Lowering User Cognitive Load in LLMs via Complex Intent Understanding
---

# Prism: Towards Lowering User Cognitive Load in LLMs via Complex Intent Understanding
**arXiv**：[2601.08653v1](https://arxiv.org/abs/2601.08653) · [PDF](https://arxiv.org/pdf/2601.08653.pdf)  
**作者**：Zenghua Liao, Jinzhi Liao, Xiang Zhao  

**一句话要点**：提出Prism框架以降低LLMs中用户认知负荷，通过复杂意图理解实现逻辑一致的澄清交互。

**关键词**：复杂意图理解, 认知负荷理论, 逻辑澄清生成, 意图感知奖励, 自进化调优, 用户-LLM交互

## 3 点简述
- 核心问题：现有方法未能建模澄清问题间的逻辑依赖，导致用户意图理解效率低。
- 方法要点：Prism包含意图分解、逻辑澄清生成、意图感知奖励和自进化调优四个模块。
- 实验或效果：在逻辑一致性、用户满意度和任务完成时间上显著优于基线，减少逻辑冲突至11.5%。

## 摘要（原文）

> Large Language Models are rapidly emerging as web-native interfaces to social platforms. On the social web, users frequently have ambiguous and dynamic goals, making complex intent understanding-rather than single-turn execution-the cornerstone of effective human-LLM collaboration. Existing approaches attempt to clarify user intents through sequential or parallel questioning, yet they fall short of addressing the core challenge: modeling the logical dependencies among clarification questions. Inspired by the Cognitive Load Theory, we propose Prism, a novel framework for complex intent understanding that enables logically coherent and efficient intent clarification. Prism comprises four tailored modules: a complex intent decomposition module, which decomposes user intents into smaller, well-structured elements and identifies logical dependencies among them; a logical clarification generation module, which organizes clarification questions based on these dependencies to ensure coherent, low-friction interactions; an intent-aware reward module, which evaluates the quality of clarification trajectories via an intent-aware reward function and leverages Monte Carlo Sample to simulate user-LLM interactions for large-scale,high-quality training data generation; and a self-evolved intent tuning module, which iteratively refines the LLM's logical clarification capability through data-driven feedback and optimization. Prism consistently outperforms existing approaches across clarification interactions, intent execution, and cognitive load benchmarks. It achieves stateof-the-art logical consistency, reduces logical conflicts to 11.5%, increases user satisfaction by 14.4%, and decreases task completion time by 34.8%. All data and code are released.

