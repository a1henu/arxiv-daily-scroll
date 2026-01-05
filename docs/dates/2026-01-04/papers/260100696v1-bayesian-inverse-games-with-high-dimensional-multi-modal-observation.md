---
layout: default
title: Bayesian Inverse Games with High-Dimensional Multi-Modal Observations
---

# Bayesian Inverse Games with High-Dimensional Multi-Modal Observations
**arXiv**：[2601.00696v1](https://arxiv.org/abs/2601.00696) · [PDF](https://arxiv.org/pdf/2601.00696.pdf)  
**作者**：Yash Jain, Xinjie Liu, Lasse Peters, David Fridovich-Keil, Ufuk Topcu  

**一句话要点**：提出贝叶斯逆博弈框架，利用多模态观测实时推断多智能体目标分布以提升下游决策安全性。

**关键词**：逆博弈, 贝叶斯推断, 多智能体交互, 变分自编码器, 多模态观测, 不确定性量化

## 3 点简述
- 核心问题：现有逆博弈方法仅提供点估计，无法量化不确定性，导致下游规划可能过度自信地采取不安全行动。
- 方法要点：基于结构化变分自编码器和可微分纳什博弈求解器，无需真实目标标签，从交互数据中学习先验和后验分布。
- 实验或效果：在实验中成功学习分布，相比最大似然估计方法提升推断质量，并实现更安全的下游决策而不牺牲效率。

## 摘要（原文）

> Many multi-agent interaction scenarios can be naturally modeled as noncooperative games, where each agent's decisions depend on others' future actions. However, deploying game-theoretic planners for autonomous decision-making requires a specification of all agents' objectives. To circumvent this practical difficulty, recent work develops maximum likelihood techniques for solving inverse games that can identify unknown agent objectives from interaction data. Unfortunately, these methods only infer point estimates and do not quantify estimator uncertainty; correspondingly, downstream planning decisions can overconfidently commit to unsafe actions. We present an approximate Bayesian inference approach for solving the inverse game problem, which can incorporate observation data from multiple modalities and be used to generate samples from the Bayesian posterior over the hidden agent objectives given limited sensor observations in real time. Concretely, the proposed Bayesian inverse game framework trains a structured variational autoencoder with an embedded differentiable Nash game solver on interaction datasets and does not require labels of agents' true objectives. Extensive experiments show that our framework successfully learns prior and posterior distributions, improves inference quality over maximum likelihood estimation-based inverse game approaches, and enables safer downstream decision-making without sacrificing efficiency. When trajectory information is uninformative or unavailable, multimodal inference further reduces uncertainty by exploiting additional observation modalities.

