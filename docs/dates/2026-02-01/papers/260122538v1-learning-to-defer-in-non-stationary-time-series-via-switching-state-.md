---
layout: default
title: Learning to Defer in Non-Stationary Time Series via Switching State-Space Models
---

# Learning to Defer in Non-Stationary Time Series via Switching State-Space Models
**arXiv**：[2601.22538v1](https://arxiv.org/abs/2601.22538) · [PDF](https://arxiv.org/pdf/2601.22538.pdf)  
**作者**：Yannis Montreuil, Letian Yu, Axel Carlier, Lai Xing Ng, Wei Tsang Ooi  

**一句话要点**：提出L2D-SLDS模型与IDS路由规则，以解决非平稳时间序列中专家选择与信息传递问题。

**关键词**：学习延迟, 非平稳时间序列, 状态空间模型, 专家系统, 信息论决策采样, 部分反馈

## 3 点简述
- 研究非平稳时间序列中的学习延迟问题，涉及部分反馈和时变专家可用性。
- 使用因子化切换线性高斯状态空间模型建模专家残差，支持专家动态注册和跨专家信息共享。
- 基于一步预测信念设计路由规则，实验显示优于上下文多臂老虎机基准和无共享因子消融。

## 摘要（原文）

> We study Learning to Defer for non-stationary time series with partial feedback and time-varying expert availability. At each time step, the router selects an available expert, observes the target, and sees only the queried expert's prediction. We model signed expert residuals using L2D-SLDS, a factorized switching linear-Gaussian state-space model with context-dependent regime transitions, a shared global factor enabling cross-expert information transfer, and per-expert idiosyncratic states. The model supports expert entry and pruning via a dynamic registry. Using one-step-ahead predictive beliefs, we propose an IDS-inspired routing rule that trades off predicted cost against information gained about the latent regime and shared factor. Experiments show improvements over contextual-bandit baselines and a no-shared-factor ablation.

