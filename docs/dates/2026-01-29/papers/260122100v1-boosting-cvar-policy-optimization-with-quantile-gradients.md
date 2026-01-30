---
layout: default
title: Boosting CVaR Policy Optimization with Quantile Gradients
---

# Boosting CVaR Policy Optimization with Quantile Gradients
**arXiv**：[2601.22100v1](https://arxiv.org/abs/2601.22100) · [PDF](https://arxiv.org/pdf/2601.22100.pdf)  
**作者**：Yudong Luo, Erick Delage  

**一句话要点**：提出基于分位数梯度的CVaR策略优化方法以提升样本效率

**关键词**：条件风险价值, 策略优化, 样本效率, 分位数梯度, 风险规避

## 3 点简述
- CVaR策略梯度方法因聚焦尾部性能而样本效率低下
- 通过引入期望分位数项，利用动态规划利用所有采样数据
- 实验显示在可验证风险规避场景中优于现有方法

## 摘要（原文）

> Optimizing Conditional Value-at-risk (CVaR) using policy gradient (a.k.a CVaR-PG) faces significant challenges of sample inefficiency. This inefficiency stems from the fact that it focuses on tail-end performance and overlooks many sampled trajectories. We address this problem by augmenting CVaR with an expected quantile term. Quantile optimization admits a dynamic programming formulation that leverages all sampled data, thus improves sample efficiency. This does not alter the CVaR objective since CVaR corresponds to the expectation of quantile over the tail. Empirical results in domains with verifiable risk-averse behavior show that our algorithm within the Markovian policy class substantially improves upon CVaR-PG and consistently outperforms other existing methods.

