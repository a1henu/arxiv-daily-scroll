---
layout: default
title: Modeling Endogenous Logic: Causal Neuro-Symbolic Reasoning Model for Explainable Multi-Behavior Recommendation
---

# Modeling Endogenous Logic: Causal Neuro-Symbolic Reasoning Model for Explainable Multi-Behavior Recommendation
**arXiv**：[2601.21335v1](https://arxiv.org/abs/2601.21335) · [PDF](https://arxiv.org/pdf/2601.21335.pdf)  
**作者**：Yuzhe Chen, Jie Cao, Youquan Wang, Haicheng Tao, Darko B. Vukovic, Jia Wu  

**一句话要点**：提出因果神经符号推理模型CNRE，以解决多行为推荐中可解释性与性能的权衡问题。

**关键词**：多行为推荐, 神经符号推理, 因果推断, 可解释性, 内生逻辑, 偏好传播

## 3 点简述
- 核心问题：现有多行为推荐方法牺牲可解释性追求性能，且可解释方法依赖外部信息导致泛化性有限。
- 方法要点：结合因果推理与神经符号集成，通过层次偏好传播和自适应神经逻辑推理路径，模拟内生逻辑决策过程。
- 实验或效果：在三个大规模数据集上验证，CNRE显著优于基线，提供从模型设计到推荐结果的多层次可解释性。

## 摘要（原文）

> Existing multi-behavior recommendations tend to prioritize performance at the expense of explainability, while current explainable methods suffer from limited generalizability due to their reliance on external information. Neuro-Symbolic integration offers a promising avenue for explainability by combining neural networks with symbolic logic rule reasoning. Concurrently, we posit that user behavior chains inherently embody an endogenous logic suitable for explicit reasoning. However, these observational multiple behaviors are plagued by confounders, causing models to learn spurious correlations. By incorporating causal inference into this Neuro-Symbolic framework, we propose a novel Causal Neuro-Symbolic Reasoning model for Explainable Multi-Behavior Recommendation (CNRE). CNRE operationalizes the endogenous logic by simulating a human-like decision-making process. Specifically, CNRE first employs hierarchical preference propagation to capture heterogeneous cross-behavior dependencies. Subsequently, it models the endogenous logic rule implicit in the user's behavior chain based on preference strength, and adaptively dispatches to the corresponding neural-logic reasoning path (e.g., conjunction, disjunction). This process generates an explainable causal mediator that approximates an ideal state isolated from confounding effects. Extensive experiments on three large-scale datasets demonstrate CNRE's significant superiority over state-of-the-art baselines, offering multi-level explainability from model design and decision process to recommendation results.

