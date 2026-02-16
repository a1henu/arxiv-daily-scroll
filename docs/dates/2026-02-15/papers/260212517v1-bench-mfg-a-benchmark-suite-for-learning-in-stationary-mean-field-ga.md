---
layout: default
title: Bench-MFG: A Benchmark Suite for Learning in Stationary Mean Field Games
---

# Bench-MFG: A Benchmark Suite for Learning in Stationary Mean Field Games
**arXiv**：[2602.12517v1](https://arxiv.org/abs/2602.12517) · [PDF](https://arxiv.org/pdf/2602.12517.pdf)  
**作者**：Lorenzo Magnino, Jiacheng Shen, Matthieu Geist, Olivier Pietquin, Mathieu Laurière  

**一句话要点**：提出Bench-MFG基准套件以解决平均场博弈与强化学习领域缺乏标准化评估的问题

**关键词**：平均场博弈, 强化学习, 基准测试, 多智能体系统, 算法评估

## 3 点简述
- 核心问题：平均场博弈与强化学习领域缺乏统一评估协议，导致方法比较困难
- 方法要点：引入问题分类法和MF-Garnets方法，生成随机实例以支持统计测试
- 实验或效果：在多种环境中测试算法，提出标准化实验指南

## 摘要（原文）

> The intersection of Mean Field Games (MFGs) and Reinforcement Learning (RL) has fostered a growing family of algorithms designed to solve large-scale multi-agent systems. However, the field currently lacks a standardized evaluation protocol, forcing researchers to rely on bespoke, isolated, and often simplistic environments. This fragmentation makes it difficult to assess the robustness, generalization, and failure modes of emerging methods. To address this gap, we propose a comprehensive benchmark suite for MFGs (Bench-MFG), focusing on the discrete-time, discrete-space, stationary setting for the sake of clarity. We introduce a taxonomy of problem classes, ranging from no-interaction and monotone games to potential and dynamics-coupled games, and provide prototypical environments for each. Furthermore, we propose MF-Garnets, a method for generating random MFG instances to facilitate rigorous statistical testing. We benchmark a variety of learning algorithms across these environments, including a novel black-box approach (MF-PSO) for exploitability minimization. Based on our extensive empirical results, we propose guidelines to standardize future experimental comparisons. Code available at \href{https://github.com/lorenzomagnino/Bench-MFG}{https://github.com/lorenzomagnino/Bench-MFG}.

