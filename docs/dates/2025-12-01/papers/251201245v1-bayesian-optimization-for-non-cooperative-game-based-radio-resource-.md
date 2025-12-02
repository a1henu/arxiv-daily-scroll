---
layout: default
title: Bayesian Optimization for Non-Cooperative Game-Based Radio Resource Management
---

# Bayesian Optimization for Non-Cooperative Game-Based Radio Resource Management
**arXiv**：[2512.01245v1](https://arxiv.org/abs/2512.01245) · [PDF](https://arxiv.org/pdf/2512.01245.pdf)  
**作者**：Yunchuan Zhang, Jiechen Chen, Junshuo Liu, Robert C. Qiu  

**一句话要点**：提出PPR-UCB贝叶斯优化策略以解决非合作博弈中基站资源分配的均衡求解问题

**关键词**：贝叶斯优化, 非合作博弈, 资源分配, 高斯过程, 纳什均衡, 无线网络

## 3 点简述
- 核心问题：蜂窝网络中基站资源分配存在冲突，需在仅能通过昂贵黑盒评估下协调策略以实现稳定均衡
- 方法要点：基于高斯过程代理和鞅技术，构建高概率置信界以量化不确定性，学习序列决策-评估对近似纯纳什均衡
- 实验或效果：在多小区多天线系统下行传输功率分配实验中，PPR-UCB能在少量数据样本内有效识别均衡解

## 摘要（原文）

> Radio resource management in modern cellular networks often calls for the optimization of complex utility functions that are potentially conflicting between different base stations (BSs). Coordinating the resource allocation strategies efficiently across BSs to ensure stable network service poses significant challenges, especially when each utility is accessible only via costly, black-box evaluations. This paper considers formulating the resource allocation among spectrum sharing BSs as a non-cooperative game, with the goal of aligning their allocation incentives toward a stable outcome. To address this challenge, we propose PPR-UCB, a novel Bayesian optimization (BO) strategy that learns from sequential decision-evaluation pairs to approximate pure Nash equilibrium (PNE) solutions. PPR-UCB applies martingale techniques to Gaussian process (GP) surrogates and constructs high probability confidence bounds for utilities uncertainty quantification. Experiments on downlink transmission power allocation in a multi-cell multi-antenna system demonstrate the efficiency of PPR-UCB in identifying effective equilibrium solutions within a few data samples.

