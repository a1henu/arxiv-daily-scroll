---
layout: default
title: Hypernetworks That Evolve Themselves
---

# Hypernetworks That Evolve Themselves
**arXiv**：[2512.16406v1](https://arxiv.org/abs/2512.16406) · [PDF](https://arxiv.org/pdf/2512.16406.pdf)  
**作者**：Joachim Winther Pedersen, Erwan Plantec, Eleni Nisioti, Marcello Barylli, Milton Montero, Kathrin Korte, Sebastian Risi  

**一句话要点**：提出自指图超网络，通过内嵌变异和继承机制实现神经网络自主进化。

**关键词**：自指超网络, 自主进化, 图神经网络, 强化学习, 变异率自适应, 种群动态

## 3 点简述
- 核心问题：神经网络如何不依赖外部优化器实现自主进化。
- 方法要点：结合超网络、随机参数生成和图表示，使网络自变异、自评估并自适应变异率。
- 实验或效果：在强化学习基准中展示快速适应、涌现种群动态和自主微调能力。

## 摘要（原文）

> How can neural networks evolve themselves without relying on external optimizers? We propose Self-Referential Graph HyperNetworks, systems where the very machinery of variation and inheritance is embedded within the network. By uniting hypernetworks, stochastic parameter generation, and graph-based representations, Self-Referential GHNs mutate and evaluate themselves while adapting mutation rates as selectable traits. Through new reinforcement learning benchmarks with environmental shifts (CartPoleSwitch, LunarLander-Switch), Self-Referential GHNs show swift, reliable adaptation and emergent population dynamics. In the locomotion benchmark Ant-v5, they evolve coherent gaits, showing promising fine-tuning capabilities by autonomously decreasing variation in the population to concentrate around promising solutions. Our findings support the idea that evolvability itself can emerge from neural self-reference. Self-Referential GHNs reflect a step toward synthetic systems that more closely mirror biological evolution, offering tools for autonomous, open-ended learning agents.

