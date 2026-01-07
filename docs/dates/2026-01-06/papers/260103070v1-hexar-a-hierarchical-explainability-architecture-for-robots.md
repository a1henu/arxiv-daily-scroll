---
layout: default
title: HEXAR: a Hierarchical Explainability Architecture for Robots
---

# HEXAR: a Hierarchical Explainability Architecture for Robots
**arXiv**：[2601.03070v1](https://arxiv.org/abs/2601.03070) · [PDF](https://arxiv.org/pdf/2601.03070.pdf)  
**作者**：Tamlin Love, Ferran Gebellí, Pradip Pramanick, Antonio Andriella, Guillem Alenyà, Anais Garrell, Raquel Ros, Silvia Rossi  

**一句话要点**：提出HEXAR分层可解释性架构，以解决机器人复杂决策中模块化解释不足的问题。

**关键词**：机器人可解释性, 分层架构, 模块化解释, 因果模型, LLM推理, 辅助机器人

## 3 点简述
- 核心问题：现有机器人可解释性方法难以从高层行为角度查询或未充分利用模块化架构。
- 方法要点：HEXAR采用插件式分层框架，结合多种解释技术，通过选择器协调组件解释器。
- 实验或效果：在TIAGo机器人辅助任务中，HEXAR在根因识别、信息排除和运行时上显著优于基线方法。

## 摘要（原文）

> As robotic systems become increasingly complex, the need for explainable decision-making becomes critical. Existing explainability approaches in robotics typically either focus on individual modules, which can be difficult to query from the perspective of high-level behaviour, or employ monolithic approaches, which do not exploit the modularity of robotic architectures. We present HEXAR (Hierarchical EXplainability Architecture for Robots), a novel framework that provides a plug-in, hierarchical approach to generate explanations about robotic systems. HEXAR consists of specialised component explainers using diverse explanation techniques (e.g., LLM-based reasoning, causal models, feature importance, etc) tailored to specific robot modules, orchestrated by an explainer selector that chooses the most appropriate one for a given query. We implement and evaluate HEXAR on a TIAGo robot performing assistive tasks in a home environment, comparing it against end-to-end and aggregated baseline approaches across 180 scenario-query variations. We observe that HEXAR significantly outperforms baselines in root cause identification, incorrect information exclusion, and runtime, offering a promising direction for transparent autonomous systems.

