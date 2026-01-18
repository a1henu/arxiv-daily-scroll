---
layout: default
title: Distributed Perceptron under Bounded Staleness, Partial Participation, and Noisy Communication
---

# Distributed Perceptron under Bounded Staleness, Partial Participation, and Noisy Communication
**arXiv**：[2601.10705v1](https://arxiv.org/abs/2601.10705) · [PDF](https://arxiv.org/pdf/2601.10705.pdf)  
**作者**：Keval Jain, Anant Raj, Saurav Prakash, Girish Varma  

**一句话要点**：提出基于陈旧性桶聚合的分布式感知机，在延迟、部分参与和噪声通信下保证有限错误界。

**关键词**：分布式感知机, 陈旧性聚合, 部分参与, 通信噪声, 迭代参数混合, 联邦学习

## 3 点简述
- 研究分布式感知机训练，处理双向版本延迟、部分客户端参与和通信噪声的系统效应。
- 引入服务器端陈旧性桶聚合规则，确定性控制更新陈旧性，无需假设延迟或参与的随机模型。
- 在可分性和数据半径有界下，证明有限轮次内累积感知机错误的期望界，噪声影响以平方根增长。

## 摘要（原文）

> We study a semi-asynchronous client-server perceptron trained via iterative parameter mixing (IPM-style averaging): clients run local perceptron updates and a server forms a global model by aggregating the updates that arrive in each communication round. The setting captures three system effects in federated and distributed deployments: (i) stale updates due to delayed model delivery and delayed application of client computations (two-sided version lag), (ii) partial participation (intermittent client availability), and (iii) imperfect communication on both downlink and uplink, modeled as effective zero-mean additive noise with bounded second moment. We introduce a server-side aggregation rule called staleness-bucket aggregation with padding that deterministically enforces a prescribed staleness profile over update ages without assuming any stochastic model for delays or participation. Under margin separability and bounded data radius, we prove a finite-horizon expected bound on the cumulative weighted number of perceptron mistakes over a given number of server rounds: the impact of delay appears only through the mean enforced staleness, whereas communication noise contributes an additional term that grows on the order of the square root of the horizon with the total noise energy. In the noiseless case, we show how a finite expected mistake budget yields an explicit finite-round stabilization bound under a mild fresh-participation condition.

