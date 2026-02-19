---
layout: default
title: Causally-Guided Automated Feature Engineering with Multi-Agent Reinforcement Learning
---

# Causally-Guided Automated Feature Engineering with Multi-Agent Reinforcement Learning
**arXiv**：[2602.16435v1](https://arxiv.org/abs/2602.16435) · [PDF](https://arxiv.org/pdf/2602.16435.pdf)  
**作者**：Arun Vignesh Malarkkan, Wangyang Ying, Yanjie Fu  

**一句话要点**：提出CAFE框架，通过因果引导的多智能体强化学习解决自动化特征工程在分布偏移下的脆弱性问题

**关键词**：自动化特征工程, 因果引导学习, 多智能体强化学习, 分布偏移鲁棒性, 特征构造优化

## 3 点简述
- 现有自动化特征工程方法依赖统计启发式，在分布偏移时产生脆弱特征
- CAFE将特征工程重构为因果引导的序列决策过程，结合因果发现与强化学习
- 在15个基准测试中提升性能达7%，分布偏移下性能下降减少约4倍

## 摘要（原文）

> Automated feature engineering (AFE) enables AI systems to autonomously construct high-utility representations from raw tabular data. However, existing AFE methods rely on statistical heuristics, yielding brittle features that fail under distribution shift. We introduce CAFE, a framework that reformulates AFE as a causally-guided sequential decision process, bridging causal discovery with reinforcement learning-driven feature construction. Phase I learns a sparse directed acyclic graph over features and the target to obtain soft causal priors, grouping features as direct, indirect, or other based on their causal influence with respect to the target. Phase II uses a cascading multi-agent deep Q-learning architecture to select causal groups and transformation operators, with hierarchical reward shaping and causal group-level exploration strategies that favor causally plausible transformations while controlling feature complexity. Across 15 public benchmarks (classification with macro-F1; regression with inverse relative absolute error), CAFE achieves up to 7% improvement over strong AFE baselines, reduces episodes-to-convergence, and delivers competitive time-to-target. Under controlled covariate shifts, CAFE reduces performance drop by ~4x relative to a non-causal multi-agent baseline, and produces more compact feature sets with more stable post-hoc attributions. These findings underscore that causal structure, used as a soft inductive prior rather than a rigid constraint, can substantially improve the robustness and efficiency of automated feature engineering.

