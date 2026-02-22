---
layout: default
title: AutoNumerics: An Autonomous, PDE-Agnostic Multi-Agent Pipeline for Scientific Computing
---

# AutoNumerics: An Autonomous, PDE-Agnostic Multi-Agent Pipeline for Scientific Computing
**arXiv**：[2602.17607v1](https://arxiv.org/abs/2602.17607) · [PDF](https://arxiv.org/pdf/2602.17607.pdf)  
**作者**：Jianda Du, Youran Sun, Haizhao Yang  

**一句话要点**：提出AutoNumerics多智能体框架，以自动设计PDE数值求解器，解决传统方法依赖专家知识的问题。

**关键词**：偏微分方程求解, 多智能体系统, 数值分析, 自动求解器设计, 科学计算自动化

## 3 点简述
- 核心问题：PDE数值求解器设计需大量数学专家知识和手动调参，现有神经网络方法成本高且可解释性差。
- 方法要点：基于多智能体框架，从自然语言描述自主生成基于经典数值分析的透明求解器，采用粗到细执行策略和残差自验证机制。
- 实验效果：在24个PDE问题上，相比现有神经和LLM基线，达到竞争性或更优精度，并能根据PDE结构正确选择数值方案。

## 摘要（原文）

> PDEs are central to scientific and engineering modeling, yet designing accurate numerical solvers typically requires substantial mathematical expertise and manual tuning. Recent neural network-based approaches improve flexibility but often demand high computational cost and suffer from limited interpretability. We introduce \texttt{AutoNumerics}, a multi-agent framework that autonomously designs, implements, debugs, and verifies numerical solvers for general PDEs directly from natural language descriptions. Unlike black-box neural solvers, our framework generates transparent solvers grounded in classical numerical analysis. We introduce a coarse-to-fine execution strategy and a residual-based self-verification mechanism. Experiments on 24 canonical and real-world PDE problems demonstrate that \texttt{AutoNumerics} achieves competitive or superior accuracy compared to existing neural and LLM-based baselines, and correctly selects numerical schemes based on PDE structural properties, suggesting its viability as an accessible paradigm for automated PDE solving.

