---
layout: default
title: Active Asymmetric Multi-Agent Multimodal Learning under Uncertainty
---

# Active Asymmetric Multi-Agent Multimodal Learning under Uncertainty
**arXiv**：[2602.04763v1](https://arxiv.org/abs/2602.04763) · [PDF](https://arxiv.org/pdf/2602.04763.pdf)  
**作者**：Rui Liu, Pratap Tokekar, Ming Lin  

**一句话要点**：提出A2MAML方法，通过模态级协作解决多智能体系统中异构传感器不确定性下的协同感知问题。

**关键词**：多智能体系统, 多模态学习, 不确定性建模, 贝叶斯融合, 协同感知, 自动驾驶

## 3 点简述
- 核心问题：多智能体系统异构传感器引入模态和智能体依赖的不确定性，现有方法在传感器损坏时鲁棒性受限。
- 方法要点：建模模态特征为带不确定性的随机估计，主动选择可靠智能体-模态对，基于贝叶斯逆方差加权聚合信息。
- 实验或效果：在协同自动驾驶事故检测场景中，A2MAML优于单智能体和协同基线，检测率提升最高达18.7%。

## 摘要（原文）

> Multi-agent systems are increasingly equipped with heterogeneous multimodal sensors, enabling richer perception but introducing modality-specific and agent-dependent uncertainty. Existing multi-agent collaboration frameworks typically reason at the agent level, assume homogeneous sensing, and handle uncertainty implicitly, limiting robustness under sensor corruption. We propose Active Asymmetric Multi-Agent Multimodal Learning under Uncertainty (A2MAML), a principled approach for uncertainty-aware, modality-level collaboration. A2MAML models each modality-specific feature as a stochastic estimate with uncertainty prediction, actively selects reliable agent-modality pairs, and aggregates information via Bayesian inverse-variance weighting. This formulation enables fine-grained, modality-level fusion, supports asymmetric modality availability, and provides a principled mechanism to suppress corrupted or noisy modalities. Extensive experiments on connected autonomous driving scenarios for collaborative accident detection demonstrate that A2MAML consistently outperforms both single-agent and collaborative baselines, achieving up to 18.7% higher accident detection rate.

