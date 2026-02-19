---
layout: default
title: Local adapt-then-combine algorithms for distributed nonsmooth optimization: Achieving provable communication acceleration
---

# Local adapt-then-combine algorithms for distributed nonsmooth optimization: Achieving provable communication acceleration
**arXiv**：[2602.16148v1](https://arxiv.org/abs/2602.16148) · [PDF](https://arxiv.org/pdf/2602.16148.pdf)  
**作者**：Luyao Guo, Xinli Shi, Wenying Xu, Jinde Cao  

**一句话要点**：提出FlexATC框架以解决分布式非光滑优化中的通信效率问题

**关键词**：分布式优化, 非光滑优化, 通信效率, 局部更新, 收敛分析, ATC框架

## 3 点简述
- 研究分布式复合优化问题，涉及局部光滑项和公共非光滑项
- 基于概率局部更新机制，提出统一ATC框架FlexATC，实现通信加速
- 理论证明在强凸设置下线性收敛率与函数和网络拓扑解耦，实验验证有效性

## 摘要（原文）

> This paper is concerned with the distributed composite optimization problem over networks, where agents aim to minimize a sum of local smooth components and a common nonsmooth term. Leveraging the probabilistic local updates mechanism, we propose a communication-efficient Adapt-Then-Combine (ATC) framework, FlexATC, unifying numerous ATC-based distributed algorithms. Under stepsizes independent of the network topology and the number of local updates, we establish sublinear and linear convergence rates for FlexATC in convex and strongly convex settings, respectively. Remarkably, in the strong convex setting, the linear rate is decoupled from the objective functions and network topology, and FlexATC permits communication to be skipped in most iterations without any deterioration of the linear rate. In addition, the proposed unified theory demonstrates for the first time that local updates provably lead to communication acceleration for ATC-based distributed algorithms. Numerical experiments further validate the efficacy of the proposed framework and corroborate the theoretical results.

