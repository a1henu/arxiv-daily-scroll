---
layout: default
title: PhysicsAgentABM: Physics-Guided Generative Agent-Based Modeling
---

# PhysicsAgentABM: Physics-Guided Generative Agent-Based Modeling
**arXiv**：[2602.06030v1](https://arxiv.org/abs/2602.06030) · [PDF](https://arxiv.org/pdf/2602.06030.pdf)  
**作者**：Kavana Venkatesh, Yinhan He, Jundong Li, Jiaming Cui  

**一句话要点**：提出PhysicsAgentABM，通过群体级推理和不确定性感知的神经符号融合，实现可扩展和校准的模拟。

**关键词**：智能体建模, 神经符号融合, 不确定性校准, 群体推理, LLM多智能体系统, 对比学习聚类

## 3 点简述
- 核心问题：基于LLM的多智能体系统扩展成本高且校准差，传统ABM难以整合个体信号和非平稳行为。
- 方法要点：使用行为聚类、神经符号融合和不确定性感知，解耦群体推理与个体变异性。
- 实验或效果：在公共卫生、金融和社会科学实验中，事件时间准确性和校准优于基线方法。

## 摘要（原文）

> Large language model (LLM)-based multi-agent systems enable expressive agent reasoning but are expensive to scale and poorly calibrated for timestep-aligned state-transition simulation, while classical agent-based models (ABMs) offer interpretability but struggle to integrate rich individual-level signals and non-stationary behaviors. We propose PhysicsAgentABM, which shifts inference to behaviorally coherent agent clusters: state-specialized symbolic agents encode mechanistic transition priors, a multimodal neural transition model captures temporal and interaction dynamics, and uncertainty-aware epistemic fusion yields calibrated cluster-level transition distributions. Individual agents then stochastically realize transitions under local constraints, decoupling population inference from entity-level variability. We further introduce ANCHOR, an LLM agent-driven clustering strategy based on cross-contextual behavioral responses and a novel contrastive loss, reducing LLM calls by up to 6-8 times. Experiments across public health, finance, and social sciences show consistent gains in event-time accuracy and calibration over mechanistic, neural, and LLM baselines. By re-architecting generative ABM around population-level inference with uncertainty-aware neuro-symbolic fusion, PhysicsAgentABM establishes a new paradigm for scalable and calibrated simulation with LLMs.

