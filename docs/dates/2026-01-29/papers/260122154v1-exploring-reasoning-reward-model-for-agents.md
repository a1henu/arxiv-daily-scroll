---
layout: default
title: Exploring Reasoning Reward Model for Agents
---

# Exploring Reasoning Reward Model for Agents
**arXiv**：[2601.22154v1](https://arxiv.org/abs/2601.22154) · [PDF](https://arxiv.org/pdf/2601.22154.pdf)  
**作者**：Kaixuan Fan, Kaituo Feng, Manyuan Zhang, Tianshuo Peng, Zhixun Li, Yilei Jiang, Shuang Chen, Peng Pei, Xunliang Cai, Xiangyu Yue  

**一句话要点**：提出Agent Reasoning Reward Model以解决智能体强化学习中稀疏奖励导致的推理质量评估不足问题

**关键词**：智能体强化学习, 推理奖励模型, 结构化反馈, 训练策略, 基准评估, 代码开源

## 3 点简述
- 核心问题：现有智能体强化学习依赖稀疏结果奖励，无法区分中间推理质量，导致训练效果不佳
- 方法要点：引入多面奖励模型，提供结构化反馈，包括显式推理轨迹、聚焦批判和整体评分
- 实验或效果：在12个基准测试中验证，Reagent-U策略在GAIA和WebWalkerQA上分别达到43.7%和46.2%的性能提升

## 摘要（原文）

> Agentic Reinforcement Learning (Agentic RL) has achieved notable success in enabling agents to perform complex reasoning and tool use. However, most methods still relies on sparse outcome-based reward for training. Such feedback fails to differentiate intermediate reasoning quality, leading to suboptimal training results. In this paper, we introduce Agent Reasoning Reward Model (Agent-RRM), a multi-faceted reward model that produces structured feedback for agentic trajectories, including (1) an explicit reasoning trace , (2) a focused critique that provides refinement guidance by highlighting reasoning flaws, and (3) an overall score that evaluates process performance. Leveraging these signals, we systematically investigate three integration strategies: Reagent-C (text-augmented refinement), Reagent-R (reward-augmented guidance), and Reagent-U (unified feedback integration). Extensive evaluations across 12 diverse benchmarks demonstrate that Reagent-U yields substantial performance leaps, achieving 43.7% on GAIA and 46.2% on WebWalkerQA, validating the effectiveness of our reasoning reward model and training schemes. Code, models, and datasets are all released to facilitate future research.

