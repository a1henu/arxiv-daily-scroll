---
layout: default
title: Online Algorithms with Unreliable Guidance
---

# Online Algorithms with Unreliable Guidance
**arXiv**：[2602.20706v1](https://arxiv.org/abs/2602.20706) · [PDF](https://arxiv.org/pdf/2602.20706.pdf)  
**作者**：Julien Dallot, Yuval Emek, Yuval Gil, Maciej Pacut, Stefan Schmid  

**一句话要点**：提出不可靠指导在线算法模型，分离预测与算法组件，提供统一分析框架。

**关键词**：在线算法, 机器学习增强, 不可靠指导, 一致性鲁棒性, DTB编译器, 请求-应答游戏

## 3 点简述
- 核心问题：在线决策中预测指导可能被对抗性破坏，需平衡一致性与鲁棒性。
- 方法要点：引入DTB编译器，将任何在线算法转换为学习增强算法，基于概率选择遵循或忽略指导。
- 实验或效果：在缓存、均匀度量任务系统和二分匹配问题中，DTB编译器生成算法达到最优或优于现有方法。

## 摘要（原文）

> This paper introduces a new model for ML-augmented online decision making, called online algorithms with unreliable guidance (OAG). This model completely separates between the predictive and algorithmic components, thus offering a single well-defined analysis framework that relies solely on the considered problem. Formulated through the lens of request-answer games, an OAG algorithm receives, with each incoming request, a piece of guidance which is taken from the problem's answer space; ideally, this guidance is the optimal answer for the current request, however with probability $β$, the guidance is adversarially corrupted. The goal is to develop OAG algorithms that admit good competitiveness when $β= 0$ (a.k.a. consistency) as well as when $β= 1$ (a.k.a. robustness); the appealing notion of smoothness, that in most prior work required a dedicated loss function, now arises naturally as $β$ shifts from $0$ to $1$.
>   We then describe a systematic method, called the drop or trust blindly (DTB) compiler, which transforms any online algorithm into a learning-augmented online algorithm in the OAG model. Given a prediction-oblivious online algorithm, its learning-augmented counterpart produced by applying the DTB compiler either follows the incoming guidance blindly or ignores it altogether and proceeds as the initial algorithm would have; the choice between these two alternatives is based on the outcome of a (biased) coin toss. As our main technical contribution, we prove (rigorously) that although remarkably simple, the class of algorithms produced via the DTB compiler includes algorithms with attractive consistency-robustness guarantees for three classic online problems: for caching and uniform metrical task systems our algorithms are optimal, whereas for bipartite matching (with adversarial arrival order), our algorithm outperforms the state-of-the-art.

