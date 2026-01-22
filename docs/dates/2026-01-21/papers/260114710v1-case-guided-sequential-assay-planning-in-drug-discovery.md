---
layout: default
title: Case-Guided Sequential Assay Planning in Drug Discovery
---

# Case-Guided Sequential Assay Planning in Drug Discovery
**arXiv**：[2601.14710v1](https://arxiv.org/abs/2601.14710) · [PDF](https://arxiv.org/pdf/2601.14710.pdf)  
**作者**：Tianchi Chen, Jan Bima, Sean L. Wu, Otto Ritter, Bingjia Yang, Xiang Yu  

**一句话要点**：提出隐式贝叶斯马尔可夫决策过程，解决药物发现中无模拟器的序列实验规划问题

**关键词**：序列实验规划, 隐式贝叶斯马尔可夫决策过程, 药物发现, 蒙特卡洛树搜索, 非参数模型, 资源优化

## 3 点简述
- 核心问题：药物发现中序列实验规划面临严重不确定性和资源约束，且缺乏环境模拟器或转移数据
- 方法要点：构建基于历史案例的非参数信念分布，通过贝叶斯更新和集成蒙特卡洛树搜索实现稳定规划
- 实验或效果：在真实CNS药物发现任务中资源消耗减少达92%，在合成环境中决策质量显著优于确定性方法

## 摘要（原文）

> Optimally sequencing experimental assays in drug discovery is a high-stakes planning problem under severe uncertainty and resource constraints. A primary obstacle for standard reinforcement learning (RL) is the absence of an explicit environment simulator or transition data $(s, a, s')$; planning must rely solely on a static database of historical outcomes. We introduce the Implicit Bayesian Markov Decision Process (IBMDP), a model-based RL framework designed for such simulator-free settings. IBMDP constructs a case-guided implicit model of transition dynamics by forming a nonparametric belief distribution using similar historical outcomes. This mechanism enables Bayesian belief updating as evidence accumulates and employs ensemble MCTS planning to generate stable policies that balance information gain toward desired outcomes with resource efficiency. We validate IBMDP through comprehensive experiments. On a real-world central nervous system (CNS) drug discovery task, IBMDP reduced resource consumption by up to 92\% compared to established heuristics while maintaining decision confidence. To rigorously assess decision quality, we also benchmarked IBMDP in a synthetic environment with a computable optimal policy. Our framework achieves significantly higher alignment with this optimal policy than a deterministic value iteration alternative that uses the same similarity-based model, demonstrating the superiority of our ensemble planner. IBMDP offers a practical solution for sequential experimental design in data-rich but simulator-poor domains.

