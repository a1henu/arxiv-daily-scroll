---
layout: default
title: Accelerating Single-Pass SGD for Generalized Linear Prediction
---

# Accelerating Single-Pass SGD for Generalized Linear Prediction
**arXiv**：[2603.01951v1](https://arxiv.org/abs/2603.01951) · [PDF](https://arxiv.org/pdf/2603.01951.pdf)  
**作者**：Qian Chen, Shihong Ding, Cong Fang  

**一句话要点**：提出数据依赖近端方法以在流式设置中加速广义线性预测的单通随机梯度下降

**关键词**：广义线性预测, 单通随机梯度下降, 动量加速, 流式学习, 超额风险分析, 数据依赖优化

## 3 点简述
- 研究流式设置下单通非二次随机优化的动量加速问题，解决Jain等人提出的开放问题
- 提出首个通过数据依赖近端方法实现双动量加速的算法，改进优化误差
- 理论分析分解超额风险为优化、统计和模型误设误差，证明动量比方差缩减更有效

## 摘要（原文）

> We study generalized linear prediction under a streaming setting, where each iteration uses only one fresh data point for a gradient-level update. While momentum is well-established in deterministic optimization, a fundamental open question is whether it can accelerate such single-pass non-quadratic stochastic optimization. We propose the first algorithm that successfully incorporates momentum via a novel data-dependent proximal method, achieving dual-momentum acceleration. Our derived excess risk bound decomposes into three components: an improved optimization error, a minimax optimal statistical error, and a higher-order model-misspecification error. The proof handles mis-specification via a fine-grained stationary analysis of inner updates, while localizing statistical error through a two-phase outer-loop analysis. As a result, we resolve the open problem posed by Jain et al. [2018a] and demonstrate that momentum acceleration is more effective than variance reduction for generalized linear prediction in the streaming setting.

