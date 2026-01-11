---
layout: default
title: Distributed Online Convex Optimization with Efficient Communication: Improved Algorithm and Lower bounds
---

# Distributed Online Convex Optimization with Efficient Communication: Improved Algorithm and Lower bounds
**arXiv**：[2601.04907v1](https://arxiv.org/abs/2601.04907) · [PDF](https://arxiv.org/pdf/2601.04907.pdf)  
**作者**：Sifan Yang, Wenhao Yang, Wei Jiang, Lijun Zhang  

**一句话要点**：提出两层级块更新框架以改进分布式在线凸优化的通信效率与后悔界

**关键词**：分布式在线优化, 压缩通信, 后悔界分析, 共识算法, 下界证明, 带反馈优化

## 3 点简述
- 研究分布式在线凸优化中的压缩通信问题，旨在降低对压缩质量因子和节点数的依赖
- 设计两层级块更新框架，结合在线八卦策略和误差补偿方案，提升学习者间共识
- 建立首个下界证明结果最优性，并扩展至带反馈场景以增强现有后悔界

## 摘要（原文）

> We investigate distributed online convex optimization with compressed communication, where $n$ learners connected by a network collaboratively minimize a sequence of global loss functions using only local information and compressed data from neighbors. Prior work has established regret bounds of $O(\max\{ω^{-2}ρ^{-4}n^{1/2},ω^{-4}ρ^{-8}\}n\sqrt{T})$ and $O(\max\{ω^{-2}ρ^{-4}n^{1/2},ω^{-4}ρ^{-8}\}n\ln{T})$ for convex and strongly convex functions, respectively, where $ω\in(0,1]$ is the compression quality factor ($ω=1$ means no compression) and $ρ<1$ is the spectral gap of the communication matrix. However, these regret bounds suffer from a \emph{quadratic} or even \emph{quartic} dependence on $ω^{-1}$. Moreover, the \emph{super-linear} dependence on $n$ is also undesirable. To overcome these limitations, we propose a novel algorithm that achieves improved regret bounds of $\tilde{O}(ω^{-1/2}ρ^{-1}n\sqrt{T})$ and $\tilde{O}(ω^{-1}ρ^{-2}n\ln{T})$ for convex and strongly convex functions, respectively. The primary idea is to design a \emph{two-level blocking update framework} incorporating two novel ingredients: an online gossip strategy and an error compensation scheme, which collaborate to \emph{achieve a better consensus} among learners. Furthermore, we establish the first lower bounds for this problem, justifying the optimality of our results with respect to both $ω$ and $T$. Additionally, we consider the bandit feedback scenario, and extend our method with the classic gradient estimators to enhance existing regret bounds.

