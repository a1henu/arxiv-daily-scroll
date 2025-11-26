---
layout: default
title: Improving Language Agents through BREW
---

# Improving Language Agents through BREW
**arXiv**：[2511.20297v1](https://arxiv.org/abs/2511.20297) · [PDF](https://arxiv.org/pdf/2511.20297.pdf)  
**作者**：Shashank Kirtania, Param Biyani, Priyanshu Gupta, Yasharth Bajpai, Roshni Iyer, Sumit Gulwani, Gustavo Soares  

**一句话要点**：提出BREW框架，通过构建和精炼知识库优化语言智能体性能。

**关键词**：语言智能体优化, 知识库构建, 结构化记忆, 任务评分, 行为准则, 计算效率

## 3 点简述
- 核心问题：现有智能体训练方法计算开销大且策略难以解释和适应。
- 方法要点：利用任务评分和行为准则构建结构化记忆，提升检索和精炼效率。
- 实验效果：在多个基准上任务精度提升10-20%，工具调用减少10-15%。

## 摘要（原文）

> Large Language Model (LLM)-based agents are increasingly applied to tasks requiring structured reasoning, tool use, and environmental adaptation, such as data manipulation, multistep planning, and computer-use automation. However, despite their versatility, current training paradigms for model weight optimization methods, like PPO and GRPO, remain relatively impractical with their high computational overhead for rollout convergence. In addition, the resulting agent policies are difficult to interpret, adapt, or incrementally improve. To address this, we investigate creating and refining structured memory of experiential learning of an agent from its environment as an alternative route to agent optimization. We introduce BREW (Bootstrapping expeRientially-learned Environmental knoWledge), a framework for agent optimization for downstream tasks via KB construction and refinement. In our formulation, we introduce an effective method for partitioning agent memory for more efficient retrieval and refinement. BREW uses task graders and behavior rubrics to learn insights while leveraging state-space search for ensuring robustness from the noise and non-specificity in natural language. Empirical results on real world, domain-grounded benchmarks -- OSWorld, $τ^2$Bench, and SpreadsheetBench -- show BREW achieves $10-20\%$ improvement in task precision, $10-15\%$ reduction in API/tool calls leading to faster execution time, all while maintaining computational efficiency on par with base models. Unlike prior work where memory is treated as static context, we establish the KB as a modular and controllable substrate for agent optimization -- an explicit lever for shaping behavior in a transparent, interpretable, and extensible manner.

