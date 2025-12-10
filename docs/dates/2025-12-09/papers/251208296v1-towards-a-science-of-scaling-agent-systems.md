---
layout: default
title: Towards a Science of Scaling Agent Systems
---

# Towards a Science of Scaling Agent Systems
**arXiv**：[2512.08296v1](https://arxiv.org/abs/2512.08296) · [PDF](https://arxiv.org/pdf/2512.08296.pdf)  
**作者**：Yubin Kim, Ken Gu, Chanwoo Park, Chunjong Park, Samuel Schmidgall, A. Ali Heydari, Yao Yan, Zhihan Zhang, Yuchen Zhuang, Mark Malhotra, Paul Pu Liang, Hae Won Park, Yuzhe Yang, Xuhai Xu, Yilun Du, Shwetak Patel, Tim Althoff, Daniel McDuff, Xin Liu  

**一句话要点**：提出基于经验协调度量的定量缩放原则，以预测多智能体系统性能

**关键词**：智能体缩放, 协调度量, 多智能体架构, 性能预测, 语言模型系统

## 3 点简述
- 核心问题：智能体系统性能缺乏量化原则，依赖启发式设计
- 方法要点：通过五种架构在四个基准上评估180种配置，使用效率、开销等度量建模
- 实验或效果：模型交叉验证R^2=0.513，识别工具协调权衡等效应，预测87%配置最优策略

## 摘要（原文）

> Agents, language model (LM)-based systems that are capable of reasoning, planning, and acting are becoming the dominant paradigm for real-world AI applications. Despite this widespread adoption, the principles that determine their performance remain underexplored, leaving practitioners to rely on heuristics rather than principled design choices. We address this gap by deriving quantitative scaling principles for agent systems. We evaluate this across four diverse benchmarks: Finance-Agent, BrowseComp-Plus, PlanCraft, and Workbench. Using five canonical architectures (Single, Independent, Centralized, Decentralized, Hybrid) instantiated across three LLM families, we perform a controlled evaluation spanning 180 configurations with standardized tools and token budgets. We derive a predictive model using empirical coordination metrics, including efficiency, overhead, error amplification, and redundancy, that achieves cross-validated R^2=0.513. We identify three dominant effects: (1) a tool-coordination trade-off: under fixed computational budgets, tool-heavy tasks suffer disproportionately from multi-agent overhead. (2) a capability saturation: coordination yields diminishing or negative returns (beta=-0.408, p<0.001) once single-agent baselines exceed ~45%. (3) topology-dependent error amplification: independent agents amplify errors 17.2x through unchecked propagation, while centralized coordination contains this to 4.4x. Centralized coordination improves performance by 80.9% on parallelizable tasks like financial reasoning, while decentralized coordination excels on dynamic web navigation (+9.2% vs. +0.2%). Yet for sequential reasoning tasks, all multi-agent variants degraded performance by 39-70%. The framework predicts the optimal coordination strategy for 87% of held-out configurations, providing a predictive principle of agentic scaling based on measurable task properties.

