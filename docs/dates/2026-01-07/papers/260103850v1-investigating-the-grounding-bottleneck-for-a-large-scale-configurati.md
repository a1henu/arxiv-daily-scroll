---
layout: default
title: Investigating the Grounding Bottleneck for a Large-Scale Configuration Problem: Existing Tools and Constraint-Aware Guessing
---

# Investigating the Grounding Bottleneck for a Large-Scale Configuration Problem: Existing Tools and Constraint-Aware Guessing
**arXiv**：[2601.03850v1](https://arxiv.org/abs/2601.03850) · [PDF](https://arxiv.org/pdf/2601.03850.pdf)  
**作者**：Veronika Semmelrock, Gerhard Friedrich  

**一句话要点**：提出约束感知猜测方法以解决大规模配置问题中的接地瓶颈

**关键词**：答案集编程, 接地瓶颈, 大规模配置, 约束感知猜测, 电子系统配置

## 3 点简述
- 核心问题：大规模电子系统配置中，接地瓶颈导致内存需求急剧增加，限制ASP技术可扩展性。
- 方法要点：分析接地过程，开发约束感知猜测方法，显著降低内存需求。
- 实验或效果：该方法有效减少内存使用，提升大规模配置问题的处理能力。

## 摘要（原文）

> Answer set programming (ASP) aims to realize the AI vision: The user specifies the problem, and the computer solves it. Indeed, ASP has made this vision true in many application domains. However, will current ASP solving techniques scale up for large configuration problems? As a benchmark for such problems, we investigated the configuration of electronic systems, which may comprise more than 30,000 components. We show the potential and limits of current ASP technology, focusing on methods that address the so-called grounding bottleneck, i.e., the sharp increase of memory demands in the size of the problem instances. To push the limits, we investigated the incremental solving approach, which proved effective in practice. However, even in the incremental approach, memory demands impose significant limits. Based on an analysis of grounding, we developed the method constraint-aware guessing, which significantly reduced the memory need.

