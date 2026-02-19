---
layout: default
title: Causal and Compositional Abstraction
---

# Causal and Compositional Abstraction
**arXiv**：[2602.16612v1](https://arxiv.org/abs/2602.16612) · [PDF](https://arxiv.org/pdf/2602.16612.pdf)  
**作者**：Robin Lorenz, Sean Tull  

**一句话要点**：提出基于范畴论的因果抽象统一框架，以自然变换形式化高低层模型间的抽象关系。

**关键词**：因果抽象, 范畴论, 自然变换, 组合模型, 量子电路, 可解释AI

## 3 点简述
- 核心问题：如何形式化因果模型间的抽象，以统一文献中的多种概念，如构造性因果抽象和Q-τ一致性。
- 方法要点：使用范畴论，定义向下和向上抽象，并引入组件级抽象以强化机制层面的构造性因果抽象。
- 实验或效果：证明组件级抽象的表征结果，并推广到量子组合电路模型，探索可解释量子AI的初步步骤。

## 摘要（原文）

> Abstracting from a low level to a more explanatory high level of description, and ideally while preserving causal structure, is fundamental to scientific practice, to causal inference problems, and to robust, efficient and interpretable AI. We present a general account of abstractions between low and high level models as natural transformations, focusing on the case of causal models. This provides a new formalisation of causal abstraction, unifying several notions in the literature, including constructive causal abstraction, Q-$τ$ consistency, abstractions based on interchange interventions, and `distributed' causal abstractions. Our approach is formalised in terms of category theory, and uses the general notion of a compositional model with a given set of queries and semantics in a monoidal, cd- or Markov category; causal models and their queries such as interventions being special cases. We identify two basic notions of abstraction: downward abstractions mapping queries from high to low level; and upward abstractions, mapping concrete queries such as Do-interventions from low to high. Although usually presented as the latter, we show how common causal abstractions may, more fundamentally, be understood in terms of the former. Our approach also leads us to consider a new stronger notion of `component-level' abstraction, applying to the individual components of a model. In particular, this yields a novel, strengthened form of constructive causal abstraction at the mechanism-level, for which we prove characterisation results. Finally, we show that abstraction can be generalised to further compositional models, including those with a quantum semantics implemented by quantum circuits, and we take first steps in exploring abstractions between quantum compositional circuit models and high-level classical causal models as a means to explainable quantum AI.

