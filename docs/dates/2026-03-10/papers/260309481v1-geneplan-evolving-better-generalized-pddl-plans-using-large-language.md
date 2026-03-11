---
layout: default
title: GenePlan: Evolving Better Generalized PDDL Plans using Large Language Models
---

# GenePlan: Evolving Better Generalized PDDL Plans using Large Language Models
**arXiv**：[2603.09481v1](https://arxiv.org/abs/2603.09481) · [PDF](https://arxiv.org/pdf/2603.09481.pdf)  
**作者**：Andrew Murray, Danial Dervovic, Alberto Pozanco, Michael Cashmore  

**一句话要点**：提出GenePlan框架，利用LLM辅助进化算法生成PDDL领域依赖的广义规划器。

**关键词**：广义规划, 进化算法, 大型语言模型, PDDL规划, 优化问题, 可解释规划器

## 3 点简述
- 核心问题：为PDDL描述的经典规划任务生成领域依赖的广义规划器，以最小化计划长度。
- 方法要点：结合大型语言模型和进化算法，迭代演化可解释的Python规划器。
- 实验或效果：在多个基准域中平均SAT得分0.91，接近最优规划器，且求解速度快、成本低。

## 摘要（原文）

> We present GenePlan (GENeralized Evolutionary Planner), a novel framework that leverages large language model (LLM) assisted evolutionary algorithms to generate domain-dependent generalized planners for classical planning tasks described in PDDL. By casting generalized planning as an optimization problem, GenePlan iteratively evolves interpretable Python planners that minimize plan length across diverse problem instances. In empirical evaluation across six existing benchmark domains and two new domains, GenePlan achieved an average SAT score of 0.91, closely matching the performance of the state-of-the-art planners (SAT score 0.93), and significantly outperforming other LLM-based baselines such as chain-of-thought (CoT) prompting (average SAT score 0.64). The generated planners solve new instances rapidly (average 0.49 seconds per task) and at low cost (average $1.82 per domain using GPT-4o).

