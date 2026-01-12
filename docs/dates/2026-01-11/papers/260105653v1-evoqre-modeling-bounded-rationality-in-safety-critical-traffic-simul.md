---
layout: default
title: EvoQRE: Modeling Bounded Rationality in Safety-Critical Traffic Simulation via Evolutionary Quantal Response Equilibrium
---

# EvoQRE: Modeling Bounded Rationality in Safety-Critical Traffic Simulation via Evolutionary Quantal Response Equilibrium
**arXiv**：[2601.05653v1](https://arxiv.org/abs/2601.05653) · [PDF](https://arxiv.org/pdf/2601.05653.pdf)  
**作者**：Phu-Hoa Pham, Chi-Nguyen Tran, Duy-Minh Dao-Sy, Phu-Quy Nguyen-Lam, Trung-Kiet Huynh  

**一句话要点**：提出EvoQRE框架，通过进化量化响应均衡建模安全关键交通模拟中的有限理性行为

**关键词**：交通模拟, 有限理性建模, 量化响应均衡, 进化博弈动力学, 安全关键场景, 自动驾驶

## 3 点简述
- 现有交通模拟框架假设完全理性，但人类驾驶员存在有限理性问题
- EvoQRE结合量化响应均衡和进化博弈动力学，集成生成世界模型，捕捉随机行为
- 在Waymo和nuPlan数据集上验证，实现高真实度、安全性和可控场景生成

## 摘要（原文）

> Existing traffic simulation frameworks for autonomous vehicles typically rely on imitation learning or game-theoretic approaches that solve for Nash or coarse correlated equilibria, implicitly assuming perfectly rational agents. However, human drivers exhibit bounded rationality, making approximately optimal decisions under cognitive and perceptual constraints. We propose EvoQRE, a principled framework for modeling safety-critical traffic interactions as general-sum Markov games solved via Quantal Response Equilibrium (QRE) and evolutionary game dynamics. EvoQRE integrates a pre-trained generative world model with entropy-regularized replicator dynamics, capturing stochastic human behavior while maintaining equilibrium structure. We provide rigorous theoretical results, proving that the proposed dynamics converge to Logit-QRE under a two-timescale stochastic approximation with an explicit convergence rate of O(log k / k^{1/3}) under weak monotonicity assumptions. We further extend QRE to continuous action spaces using mixture-based and energy-based policy representations. Experiments on the Waymo Open Motion Dataset and nuPlan benchmark demonstrate that EvoQRE achieves state-of-the-art realism, improved safety metrics, and controllable generation of diverse safety-critical scenarios through interpretable rationality parameters.

