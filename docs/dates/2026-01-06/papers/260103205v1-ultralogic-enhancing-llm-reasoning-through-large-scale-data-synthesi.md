---
layout: default
title: UltraLogic: Enhancing LLM Reasoning through Large-Scale Data Synthesis and Bipolar Float Reward
---

# UltraLogic: Enhancing LLM Reasoning through Large-Scale Data Synthesis and Bipolar Float Reward
**arXiv**：[2601.03205v1](https://arxiv.org/abs/2601.03205) · [PDF](https://arxiv.org/pdf/2601.03205.pdf)  
**作者**：Yile Liu, Yixian Liu, Zongwei Li, Yufei Huang, Xinhua Feng, Zhichao Hu, Jinglu Hu, Jianfeng Yan, Fengzong Lian, Yuhong Liu  

**一句话要点**：提出UltraLogic框架，通过大规模数据合成和双极浮动奖励增强LLM的通用推理能力。

**关键词**：大语言模型推理, 数据合成, 强化学习奖励, 逻辑验证, 难度校准

## 3 点简述
- 核心问题：LLM在复杂通用推理中面临数据稀缺和奖励稀疏的瓶颈。
- 方法要点：采用基于代码的求解方法自动化生成高质量数据，并引入双极浮动奖励机制。
- 实验或效果：任务多样性是推理提升的关键，结合难度匹配策略显著提高训练效率。

## 摘要（原文）

> While Large Language Models (LLMs) have demonstrated significant potential in natural language processing , complex general-purpose reasoning requiring multi-step logic, planning, and verification remains a critical bottleneck. Although Reinforcement Learning with Verifiable Rewards (RLVR) has succeeded in specific domains , the field lacks large-scale, high-quality, and difficulty-calibrated data for general reasoning. To address this, we propose UltraLogic, a framework that decouples the logical core of a problem from its natural language expression through a Code-based Solving methodology to automate high-quality data production. The framework comprises hundreds of unique task types and an automated calibration pipeline across ten difficulty levels. Furthermore, to mitigate binary reward sparsity and the Non-negative Reward Trap, we introduce the Bipolar Float Reward (BFR) mechanism, utilizing graded penalties to effectively distinguish perfect responses from those with logical flaws. Our experiments demonstrate that task diversity is the primary driver for reasoning enhancement , and that BFR, combined with a difficulty matching strategy, significantly improves training efficiency, guiding models toward global logical optima.

