---
layout: default
title: FedGRPO: Privately Optimizing Foundation Models with Group-Relative Rewards from Domain Client
---

# FedGRPO: Privately Optimizing Foundation Models with Group-Relative Rewards from Domain Client
**arXiv**：[2602.12014v1](https://arxiv.org/abs/2602.12014) · [PDF](https://arxiv.org/pdf/2602.12014.pdf)  
**作者**：Gongxi Zhu, Hanlin Gu, Lixin Fan, Qiang Yang, Yuxing Han  

**一句话要点**：提出FedGRPO框架，通过基于组相对奖励的强化学习评估，在保护隐私下优化联邦基础模型。

**关键词**：联邦学习, 基础模型优化, 隐私保护, 强化学习, 组相对策略优化, 通信效率

## 3 点简述
- 核心问题：现有联邦基础模型方法存在高本地训练成本、通信开销和隐私风险。
- 方法要点：基于置信图进行专家选择，并利用组相对奖励聚合策略，仅交换标量奖励信号。
- 实验或效果：在多样领域任务中，FedGRPO在准确性和通信效率上优于传统基线。

## 摘要（原文）

> One important direction of Federated Foundation Models (FedFMs) is leveraging data from small client models to enhance the performance of a large server-side foundation model. Existing methods based on model level or representation level knowledge transfer either require expensive local training or incur high communication costs and introduce unavoidable privacy risks. We reformulate this problem as a reinforcement learning style evaluation process and propose FedGRPO, a privacy preserving framework comprising two modules. The first module performs competence-based expert selection by building a lightweight confidence graph from auxiliary data to identify the most suitable clients for each question. The second module leverages the "Group Relative" concept from the Group Relative Policy Optimization (GRPO) framework by packaging each question together with its solution rationale into candidate policies, dispatching these policies to a selected subset of expert clients, and aggregating solely the resulting scalar reward signals via a federated group-relative loss function. By exchanging reward values instead of data or model updates, FedGRPO reduces privacy risk and communication overhead while enabling parallel evaluation across heterogeneous devices. Empirical results on diverse domain tasks demonstrate that FedGRPO achieves superior downstream accuracy and communication efficiency compared to conventional FedFMs baselines.

