---
layout: default
title: Generalized Information Gathering Under Dynamics Uncertainty
---

# Generalized Information Gathering Under Dynamics Uncertainty
**arXiv**：[2601.21988v1](https://arxiv.org/abs/2601.21988) · [PDF](https://arxiv.org/pdf/2601.21988.pdf)  
**作者**：Fernando Palafox, Jingqi Li, Jesse Milzman, David Fridovich-Keil  

**一句话要点**：提出基于有向信息的统一框架，以解决未知动态系统中主动信息收集的通用成本设计问题。

**关键词**：主动信息收集, 动态系统学习, 有向信息, 贝叶斯估计, 多智能体系统

## 3 点简述
- 核心问题：现有主动信息收集方法依赖特定建模选择，缺乏通用成本设计框架。
- 方法要点：通过暴露参数、信念和控制间的因果依赖，推导基于Massey有向信息的通用信息收集成本。
- 实验或效果：在线性、非线性和多智能体系统中验证框架的实用性和理论连接。

## 摘要（原文）

> An agent operating in an unknown dynamical system must learn its dynamics from observations. Active information gathering accelerates this learning, but existing methods derive bespoke costs for specific modeling choices: dynamics models, belief update procedures, observation models, and planners. We present a unifying framework that decouples these choices from the information-gathering cost by explicitly exposing the causal dependencies between parameters, beliefs, and controls. Using this framework, we derive a general information-gathering cost based on Massey's directed information that assumes only Markov dynamics with additive noise and is otherwise agnostic to modeling choices. We prove that the mutual information cost used in existing literature is a special case of our cost. Then, we leverage our framework to establish an explicit connection between the mutual information cost and information gain in linearized Bayesian estimation, thereby providing theoretical justification for mutual information-based active learning approaches. Finally, we illustrate the practical utility of our framework through experiments spanning linear, nonlinear, and multi-agent systems.

