---
layout: default
title: Scientific Theory of a Black-Box: A Life Cycle-Scale XAI Framework Based on Constructive Empiricism
---

# Scientific Theory of a Black-Box: A Life Cycle-Scale XAI Framework Based on Constructive Empiricism
**arXiv**：[2602.02215v1](https://arxiv.org/abs/2602.02215) · [PDF](https://arxiv.org/pdf/2602.02215.pdf)  
**作者**：Sebastian Müller, Vanessa Toborek, Eike Stadtländer, Tamás Horváth, Brendan Balcerak Jackson, Christian Bauckhage  

**一句话要点**：提出基于建构经验主义的黑盒科学理论框架，以支持生命周期可审计的解释性AI

**关键词**：可解释人工智能, 黑盒模型, 建构经验主义, 生命周期管理, 规则代理, 可审计性

## 3 点简述
- 核心问题：缺乏将黑盒模型解释信息整合为持久可审计制品的原则性方法
- 方法要点：基于建构经验主义，定义黑盒科学理论，强调经验充分性、可适应性和可审计性
- 实验或效果：实例化框架于神经网络分类器，开发CoBoT算法在线构建规则代理

## 摘要（原文）

> Explainable AI (XAI) offers a growing number of algorithms that aim to answer specific questions about black-box models. What is missing is a principled way to consolidate explanatory information about a fixed black-box model into a persistent, auditable artefact, that accompanies the black-box throughout its life cycle. We address this gap by introducing the notion of a scientific theory of a black (SToBB). Grounded in Constructive Empiricism, a SToBB fulfils three obligations: (i) empirical adequacy with respect to all available observations of black-box behaviour, (ii) adaptability via explicit update commitments that restore adequacy when new observations arrive, and (iii) auditability through transparent documentation of assumptions, construction choices, and update behaviour. We operationalise these obligations as a general framework that specifies an extensible observation base, a traceable hypothesis class, algorithmic components for construction and revision, and documentation sufficient for third-party assessment. Explanations for concrete stakeholder needs are then obtained by querying the maintained record through interfaces, rather than by producing isolated method outputs. As a proof of concept, we instantiate a complete SToBB for a neural-network classifier on a tabular task and introduce the Constructive Box Theoriser (CoBoT) algorithm, an online procedure that constructs and maintains an empirically adequate rule-based surrogate as observations accumulate. Together, these contributions position SToBBs as a life cycle-scale, inspectable point of reference that supports consistent, reusable analyses and systematic external scrutiny.

