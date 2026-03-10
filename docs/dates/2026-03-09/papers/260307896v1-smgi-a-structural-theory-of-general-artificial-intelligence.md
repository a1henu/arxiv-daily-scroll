---
layout: default
title: SMGI: A Structural Theory of General Artificial Intelligence
---

# SMGI: A Structural Theory of General Artificial Intelligence
**arXiv**：[2603.07896v1](https://arxiv.org/abs/2603.07896) · [PDF](https://arxiv.org/pdf/2603.07896.pdf)  
**作者**：Aomar Osmani  

**一句话要点**：提出SMGI结构理论，将通用人工智能定义为可容许耦合动态系统。

**关键词**：通用人工智能理论, 结构模型, 类型化元模型, 泛化界, 动态系统, 学习接口演化

## 3 点简述
- 核心问题：从固定环境中的假设优化转向学习接口的受控演化。
- 方法要点：通过类型化元模型定义结构本体与行为语义的严格分离。
- 实验或效果：证明结构泛化界，并展示经典学习模型为SMGI的结构受限实例。

## 摘要（原文）

> We introduce SMGI, a structural theory of general artificial intelligence, and recast the foundational problem of learning from the optimization of hypotheses within fixed environments to the controlled evolution of the learning interface itself. We formalize the Structural Model of General Intelligence (SMGI) via a typed meta-model $θ= (r,\mathcal H,Π,\mathcal L,\mathcal E,\mathcal M)$ that treats representational maps, hypothesis spaces, structural priors, multi-regime evaluators, and memory operators as explicitly typed, dynamic components. By enforcing a strict mathematical separation between this structural ontology ($θ$) and its induced behavioral semantics ($T_θ$), we define general artificial intelligence as a class of admissible coupled dynamics $(θ, T_θ)$ satisfying four obligations: structural closure under typed transformations, dynamical stability under certified evolution, bounded statistical capacity, and evaluative invariance across regime shifts. We prove a structural generalization bound that links sequential PAC-Bayes analysis and Lyapunov stability, providing sufficient conditions for capacity control and bounded drift under admissible task transformations. Furthermore, we establish a strict structural inclusion theorem demonstrating that classical empirical risk minimization, reinforcement learning, program-prior models (Solomonoff-style), and modern frontier agentic pipelines operate as structurally restricted instances of SMGI.

