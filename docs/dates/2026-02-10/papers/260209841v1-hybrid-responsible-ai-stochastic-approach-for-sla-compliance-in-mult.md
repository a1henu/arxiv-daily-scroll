---
layout: default
title: Hybrid Responsible AI-Stochastic Approach for SLA Compliance in Multivendor 6G Networks
---

# Hybrid Responsible AI-Stochastic Approach for SLA Compliance in Multivendor 6G Networks
**arXiv**：[2602.09841v1](https://arxiv.org/abs/2602.09841) · [PDF](https://arxiv.org/pdf/2602.09841.pdf)  
**作者**：Emanuel Figetakis, Ahmed Refaey Hussein  

**一句话要点**：提出混合负责任AI-随机学习框架以解决多供应商6G网络中SLA合规的责任归属问题

**关键词**：负责任AI, 6G网络自动化, SLA合规, 多供应商管理, 随机优化, 可审计性

## 3 点简述
- 核心问题：AI与6G网络自动化融合导致多供应商管理系统中SLA违规的责任归属不明确
- 方法要点：集成RAI博弈与随机优化，嵌入公平性、鲁棒性和可审计性到网络控制循环
- 实验或效果：在合成数据集上，最差组准确率提升达10.5%，审计机制成功追踪99%模拟SLA违规

## 摘要（原文）

> The convergence of AI and 6G network automation introduces new challenges in maintaining transparency, fairness, and accountability across multivendor management systems. Although closed-loop AI orchestration improves adaptability and self-optimization, it also creates a responsibility gap, where violations of SLAs cannot be causally attributed to specific agents or vendors. This paper presents a hybrid responsible AI-stochastic learning framework that embeds fairness, robustness, and auditability directly into the network control loop. The framework integrates RAI games with stochastic optimization, enabling dynamic adversarial reweighting and probabilistic exploration across heterogeneous vendor domains. An RAAP continuously records AI-driven decision trajectories and produces dual accountability reports: user-level SLA summaries and operator-level responsibility analytics. Experimental evaluations on synthetic two-class multigroup datasets demonstrate that the proposed hybrid model improves the accuracy of the worst group by up to 10.5\%. Specifically, hybrid RAI achieved a WGAcc of 60.5\% and an AvgAcc of 72.7\%, outperforming traditional RAI-GA (50.0\%) and ERM (21.5\%). The audit mechanism successfully traced 99\% simulated SLA violations to the AI entities responsible, producing both vendor and agent-level accountability indices. These results confirm that the proposed hybrid approach enhances fairness and robustness as well as establishes a concrete accountability framework for autonomous SLA assurance in multivendor 6G networks.

