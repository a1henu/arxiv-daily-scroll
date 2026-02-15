---
layout: default
title: Any House Any Task: Scalable Long-Horizon Planning for Abstract Human Tasks
---

# Any House Any Task: Scalable Long-Horizon Planning for Abstract Human Tasks
**arXiv**：[2602.12244v1](https://arxiv.org/abs/2602.12244) · [PDF](https://arxiv.org/pdf/2602.12244.pdf)  
**作者**：Zhihong Liu, Yang Li, Rengming Huang, Cewu Lu, Panpan Cai  

**一句话要点**：提出AHAT以解决大规模家庭环境中基于模糊指令的长时程任务规划问题

**关键词**：长时程规划, 家庭任务规划, 语言条件规划, 符号推理, 强化学习, 场景图

## 3 点简述
- 核心问题：开放世界语言条件任务规划在环境规模、计划长度、指令模糊性和约束复杂性增加时性能下降
- 方法要点：利用LLM将任务指令和文本场景图映射为PDDL子目标，通过符号推理生成最优长时程计划
- 实验或效果：在人类风格家庭任务中，AHAT显著优于现有提示、规划和学习方法

## 摘要（原文）

> Open world language conditioned task planning is crucial for robots operating in large-scale household environments. While many recent works attempt to address this problem using Large Language Models (LLMs) via prompting or training, a key challenge remains scalability. Performance often degrades rapidly with increasing environment size, plan length, instruction ambiguity, and constraint complexity. In this work, we propose Any House Any Task (AHAT), a household task planner optimized for long-horizon planning in large environments given ambiguous human instructions. At its core, AHAT utilizes an LLM trained to map task instructions and textual scene graphs into grounded subgoals defined in the Planning Domain Definition Language (PDDL). These subgoals are subsequently solved to generate feasible and optimal long-horizon plans through explicit symbolic reasoning. To enhance the model's ability to decompose complex and ambiguous intentions, we introduce TGPO, a novel reinforcement learning algorithm that integrates external correction of intermediate reasoning traces into Group Relative Policy Optimization (GRPO). Experiments demonstrate that AHAT achieves significant performance gains over state-of-the-art prompting, planning, and learning methods, particularly in human-style household tasks characterized by brief instructions but requiring complex execution plans.

