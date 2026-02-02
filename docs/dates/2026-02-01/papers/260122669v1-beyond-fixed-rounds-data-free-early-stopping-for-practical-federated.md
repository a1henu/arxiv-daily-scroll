---
layout: default
title: Beyond Fixed Rounds: Data-Free Early Stopping for Practical Federated Learning
---

# Beyond Fixed Rounds: Data-Free Early Stopping for Practical Federated Learning
**arXiv**：[2601.22669v1](https://arxiv.org/abs/2601.22669) · [PDF](https://arxiv.org/pdf/2601.22669.pdf)  
**作者**：Youngjoon Lee, Hyukjoon Lee, Seungrok Jung, Andy Luo, Jinu Gong, Yang Cao, Joonhyuk Kang  

**一句话要点**：提出无数据早期停止框架以解决联邦学习中固定轮次或验证数据依赖问题

**关键词**：联邦学习, 早期停止, 无数据学习, 任务向量, 隐私保护, 计算效率

## 3 点简述
- 核心问题：联邦学习依赖固定全局轮次或验证数据进行超参数调优，导致高计算成本和隐私风险。
- 方法要点：通过仅监控服务器端参数的任务向量增长率，确定最优停止点，无需任何验证数据。
- 实验或效果：在皮肤病变和血细胞分类任务中，性能优于基于验证数据的早期停止，平均轮次更少。

## 摘要（原文）

> Federated Learning (FL) facilitates decentralized collaborative learning without transmitting raw data. However, reliance on fixed global rounds or validation data for hyperparameter tuning hinders practical deployment by incurring high computational costs and privacy risks. To address this, we propose a data-free early stopping framework that determines the optimal stopping point by monitoring the task vector's growth rate using solely server-side parameters. The numerical results on skin lesion/blood cell classification demonstrate that our approach is comparable to validation-based early stopping across various state-of-the-art FL methods. In particular, the proposed framework spends an average of 47/20 (skin lesion/blood cell) rounds to achieve over 12.5%/10.3% higher performance than early stopping based on validation data. To the best of our knowledge, this is the first work to propose an early stopping framework for FL methods without using any validation data.

