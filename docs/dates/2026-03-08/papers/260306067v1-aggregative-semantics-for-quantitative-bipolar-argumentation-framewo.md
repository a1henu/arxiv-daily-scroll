---
layout: default
title: Aggregative Semantics for Quantitative Bipolar Argumentation Frameworks
---

# Aggregative Semantics for Quantitative Bipolar Argumentation Frameworks
**arXiv**：[2603.06067v1](https://arxiv.org/abs/2603.06067) · [PDF](https://arxiv.org/pdf/2603.06067.pdf)  
**作者**：Yann Munro, Isabelle Bloch, Marie-Jeanne Lesot  

**一句话要点**：提出聚合语义以增强定量双极论证框架的可解释性和参数化能力

**关键词**：定量双极论证框架, 聚合语义, 渐进语义, 论证权重, 可解释性, 参数化计算

## 3 点简述
- 针对定量双极论证框架中攻击者和支持者非对称角色问题，引入聚合语义家族
- 通过三阶段计算分别聚合攻击者和支持者权重，再与论证内在权重结合
- 讨论聚合函数性质，并通过示例和测试展示语义的多样性和可理解性

## 摘要（原文）

> Formal argumentation is being used increasingly in artificial intelligence as an effective and understandable way to model potentially conflicting pieces of information, called arguments, and identify so-called acceptable arguments depending on a chosen semantics. This paper deals with the specific context of Quantitative Bipolar Argumentation Frameworks (QBAF), where arguments have intrinsic weights and can attack or support each other. In this context, we introduce a novel family of gradual semantics, called aggregative semantics. In order to deal with situations in which attackers and supporters do not play a symmetric role, and in contrast to modular semantics, we propose to aggregate attackers and supporters separately. This leads to a three-stage computation, which consists in computing a global weight for attackers and another for supporters, before aggregating these two values with the intrinsic weight of the argument. We discuss the properties that the three aggregation functions should satisfy depending on the context, as well as their relationships with the classical principles for gradual semantics. This discussion is supported by various simple examples, as well as a final example on which five hundred aggregative semantics are tested and compared, illustrating the range of possible behaviours with aggregative semantics. Decomposing the computation into three distinct and interpretable steps leads to a more parametrisable computation: it keeps the bipolarity one step further than what is done in the literature, and it leads to more understandable gradual semantics.

