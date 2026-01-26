---
layout: default
title: FedSGM: A Unified Framework for Constraint Aware, Bidirectionally Compressed, Multi-Step Federated Optimization
---

# FedSGM: A Unified Framework for Constraint Aware, Bidirectionally Compressed, Multi-Step Federated Optimization
**arXiv**：[2601.16897v1](https://arxiv.org/abs/2601.16897) · [PDF](https://arxiv.org/pdf/2601.16897.pdf)  
**作者**：Antesh Upadhyay, Sang Bin Moon, Abolfazl Hashemi  

**一句话要点**：提出FedSGM统一框架以解决联邦学习中约束、压缩、本地更新和部分参与四大挑战

**关键词**：联邦学习, 约束优化, 梯度压缩, 本地更新, 部分参与, 切换梯度法

## 3 点简述
- 核心问题：联邦学习面临功能约束、通信瓶颈、本地更新和部分客户端参与的综合挑战
- 方法要点：基于切换梯度法，提供无投影、仅原变量的更新，结合双向误差反馈处理压缩偏差
- 实验或效果：在Neyman-Pearson分类和约束马尔可夫决策过程任务中验证理论保证

## 摘要（原文）

> We introduce FedSGM, a unified framework for federated constrained optimization that addresses four major challenges in federated learning (FL): functional constraints, communication bottlenecks, local updates, and partial client participation. Building on the switching gradient method, FedSGM provides projection-free, primal-only updates, avoiding expensive dual-variable tuning or inner solvers. To handle communication limits, FedSGM incorporates bi-directional error feedback, correcting the bias introduced by compression while explicitly understanding the interaction between compression noise and multi-step local updates. We derive convergence guarantees showing that the averaged iterate achieves the canonical $\boldsymbol{\mathcal{O}}(1/\sqrt{T})$ rate, with additional high-probability bounds that decouple optimization progress from sampling noise due to partial participation. Additionally, we introduce a soft switching version of FedSGM to stabilize updates near the feasibility boundary. To our knowledge, FedSGM is the first framework to unify functional constraints, compression, multiple local updates, and partial client participation, establishing a theoretically grounded foundation for constrained federated learning. Finally, we validate the theoretical guarantees of FedSGM via experimentation on Neyman-Pearson classification and constrained Markov decision process (CMDP) tasks.

