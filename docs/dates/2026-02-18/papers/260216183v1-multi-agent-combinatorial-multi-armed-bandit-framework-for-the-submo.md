---
layout: default
title: Multi-Agent Combinatorial-Multi-Armed-Bandit framework for the Submodular Welfare Problem under Bandit Feedback
---

# Multi-Agent Combinatorial-Multi-Armed-Bandit framework for the Submodular Welfare Problem under Bandit Feedback
**arXiv**：[2602.16183v1](https://arxiv.org/abs/2602.16183) · [PDF](https://arxiv.org/pdf/2602.16183.pdf)  
**作者**：Subham Pokhriyal, Shweta Jain, Vaneet Aggarwal  

**一句话要点**：提出多智能体组合多臂老虎机框架，解决带老虎机反馈的子模福利问题

**关键词**：子模福利问题, 多智能体组合老虎机, 老虎机反馈, 探索-提交策略, 遗憾分析, 随机分配

## 3 点简述
- 研究子模福利问题，在老虎机反馈下最大化总福利，扩展至多智能体组合老虎机框架
- 提出探索-提交策略，通过随机分配实现与(1-1/e)基准的亚线性遗憾保证
- 首次为基于划分的子模福利问题提供老虎机反馈下的遗憾保证，适用于非通信智能体

## 摘要（原文）

> We study the \emph{Submodular Welfare Problem} (SWP), where items are partitioned among agents with monotone submodular utilities to maximize the total welfare under \emph{bandit feedback}. Classical SWP assumes full value-oracle access, achieving $(1-1/e)$ approximations via continuous-greedy algorithms. We extend this to a \emph{multi-agent combinatorial bandit} framework (\textsc{MA-CMAB}), where actions are partitions under full-bandit feedback with non-communicating agents. Unlike prior single-agent or separable multi-agent CMAB models, our setting couples agents through shared allocation constraints. We propose an explore-then-commit strategy with randomized assignments, achieving $\tilde{\mathcal{O}}(T^{2/3})$ regret against a $(1-1/e)$ benchmark, the first such guarantee for partition-based submodular welfare problem under bandit feedback.

