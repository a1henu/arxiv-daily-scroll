---
layout: default
title: Explanation Beyond Intuition: A Testable Criterion for Inherent Explainability
---

# Explanation Beyond Intuition: A Testable Criterion for Inherent Explainability
**arXiv**：[2512.17316v1](https://arxiv.org/abs/2512.17316) · [PDF](https://arxiv.org/pdf/2512.17316.pdf)  
**作者**：Michael Merry, Pat Riddle, Jim Warren  

**一句话要点**：提出基于图论的可解释性准则，以结构-局部解释和全局重组解决XAI中固有可解释性定义与测试缺失问题。

**关键词**：固有可解释性, 图论模型分解, 假设-证据结构, 可解释人工智能, 临床风险模型, 监管合规测试

## 3 点简述
- 核心问题：固有可解释性缺乏一致定义和可测试标准，现有方法依赖直觉或度量。
- 方法要点：使用图论表示和分解模型，形成可验证的假设-证据结构作为结构-局部解释。
- 实验或效果：应用准则于临床心血管风险模型PREDICT，证明其固有可解释性，为监管提供灵活测试框架。

## 摘要（原文）

> Inherent explainability is the gold standard in Explainable Artificial Intelligence (XAI). However, there is not a consistent definition or test to demonstrate inherent explainability. Work to date either characterises explainability through metrics, or appeals to intuition - "we know it when we see it". We propose a globally applicable criterion for inherent explainability. The criterion uses graph theory for representing and decomposing models for structure-local explanation, and recomposing them into global explanations. We form the structure-local explanations as annotations, a verifiable hypothesis-evidence structure that allows for a range of explanatory methods to be used. This criterion matches existing intuitions on inherent explainability, and provides justifications why a large regression model may not be explainable but a sparse neural network could be. We differentiate explainable -- a model that allows for explanation -- and \textit{explained} -- one that has a verified explanation. Finally, we provide a full explanation of PREDICT -- a Cox proportional hazards model of cardiovascular disease risk, which is in active clinical use in New Zealand. It follows that PREDICT is inherently explainable. This work provides structure to formalise other work on explainability, and allows regulators a flexible but rigorous test that can be used in compliance frameworks.

