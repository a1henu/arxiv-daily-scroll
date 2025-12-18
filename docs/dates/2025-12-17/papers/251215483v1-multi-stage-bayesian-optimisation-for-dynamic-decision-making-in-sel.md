---
layout: default
title: Multi-stage Bayesian optimisation for dynamic decision-making in self-driving labs
---

# Multi-stage Bayesian optimisation for dynamic decision-making in self-driving labs
**arXiv**：[2512.15483v1](https://arxiv.org/abs/2512.15483) · [PDF](https://arxiv.org/pdf/2512.15483.pdf)  
**作者**：Luca Torresi, Pascal Friederich  

**一句话要点**：提出多阶段贝叶斯优化以支持自驱动实验室中的动态决策

**关键词**：自驱动实验室, 贝叶斯优化, 动态决策, 多阶段工作流, 代理测量

## 3 点简述
- 核心问题：标准贝叶斯优化无法处理多阶段实验流程和中间测量决策
- 方法要点：扩展贝叶斯优化，引入代理测量以优化多阶段工作流
- 实验或效果：代理测量在广泛场景中显著提升解决方案的发现速度和最优性

## 摘要（原文）

> Self-driving laboratories (SDLs) are combining recent technological advances in robotics, automation, and machine learning based data analysis and decision-making to perform autonomous experimentation toward human-directed goals without requiring any direct human intervention. SDLs are successfully used in materials science, chemistry, and beyond, to optimise processes, materials, and devices in a systematic and data-efficient way. At present, the most widely used algorithm to identify the most informative next experiment is Bayesian optimisation. While relatively simple to apply to a wide range of optimisation problems, standard Bayesian optimisation relies on a fixed experimental workflow with a clear set of optimisation parameters and one or more measurable objective functions. This excludes the possibility of making on-the-fly decisions about changes in the planned sequence of operations and including intermediate measurements in the decision-making process. Therefore, many real-world experiments need to be adapted and simplified to be converted to the common setting in self-driving labs. In this paper, we introduce an extension to Bayesian optimisation that allows flexible sampling of multi-stage workflows and makes optimal decisions based on intermediate observables, which we call proxy measurements. We systematically compare the advantage of taking into account proxy measurements over conventional Bayesian optimisation, in which only the final measurement is observed. We find that over a wide range of scenarios, proxy measurements yield a substantial improvement, both in the time to find good solutions and in the overall optimality of found solutions. This not only paves the way to use more complex and thus more realistic experimental workflows in autonomous labs but also to smoothly combine simulations and experiments in the next generation of SDLs.

