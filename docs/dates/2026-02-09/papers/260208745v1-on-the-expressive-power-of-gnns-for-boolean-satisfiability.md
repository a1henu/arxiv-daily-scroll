---
layout: default
title: On the Expressive Power of GNNs for Boolean Satisfiability
---

# On the Expressive Power of GNNs for Boolean Satisfiability
**arXiv**：[2602.08745v1](https://arxiv.org/abs/2602.08745) · [PDF](https://arxiv.org/pdf/2602.08745.pdf)  
**作者**：Saku Peltonen, Roger Wattenhofer  

**一句话要点**：分析GNN在布尔可满足性问题中的表达能力，证明WL层次无法区分可满足与不可满足实例。

**关键词**：图神经网络, 布尔可满足性, Weisfeiler-Leman测试, 表达能力分析, SAT求解, 工业实例

## 3 点简述
- 核心问题：评估GNN在SAT求解中的表达能力，基于Weisfeiler-Leman测试。
- 方法要点：证明高阶WL无法区分可满足与不可满足实例，并分析WL有界求解器的实际限制。
- 实验或效果：在G4SAT基准和SAT竞赛实例上实验，显示工业实例需要更高表达能力。

## 摘要（原文）

> Machine learning approaches to solving Boolean Satisfiability (SAT) aim to replace handcrafted heuristics with learning-based models. Graph Neural Networks have emerged as the main architecture for SAT solving, due to the natural graph representation of Boolean formulas. We analyze the expressive power of GNNs for SAT solving through the lens of the Weisfeiler-Leman (WL) test. As our main result, we prove that the full WL hierarchy cannot, in general, distinguish between satisfiable and unsatisfiable instances. We show that indistinguishability under higher-order WL carries over to practical limitations for WL-bounded solvers that set variables sequentially. We further study the expressivity required for several important families of SAT instances, including regular, random and planar instances. To quantify expressivity needs in practice, we conduct experiments on random instances from the G4SAT benchmark and industrial instances from the International SAT Competition. Our results suggest that while random instances are largely distinguishable, industrial instances often require more expressivity to predict a satisfying assignment.

