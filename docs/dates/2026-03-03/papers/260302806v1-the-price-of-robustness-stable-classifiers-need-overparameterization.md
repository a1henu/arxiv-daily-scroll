---
layout: default
title: The Price of Robustness: Stable Classifiers Need Overparameterization
---

# The Price of Robustness: Stable Classifiers Need Overparameterization
**arXiv**：[2603.02806v1](https://arxiv.org/abs/2603.02806) · [PDF](https://arxiv.org/pdf/2603.02806.pdf)  
**作者**：Jonas von Berg, Adalbert Fono, Massimiliano Datres, Sohir Maskey, Gitta Kutyniok  

**一句话要点**：提出基于类稳定性的泛化界，揭示不连续分类器中过参数化对鲁棒性的必要性。

**关键词**：鲁棒性理论, 过参数化, 泛化界, 类稳定性, 不连续分类器, 决策边界

## 3 点简述
- 研究不连续分类器中过参数化、稳定性和泛化的关系，定义类稳定性为输入域决策边界的期望距离。
- 建立有限函数类的泛化界，其改进与类稳定性成反比，并推导出鲁棒性定律，扩展至不连续函数。
- 实验表明稳定性随模型规模增加，与测试性能相关，而传统范数度量则信息有限。

## 摘要（原文）

> The relationship between overparameterization, stability, and generalization remains incompletely understood in the setting of discontinuous classifiers. We address this gap by establishing a generalization bound for finite function classes that improves inversely with class stability, defined as the expected distance to the decision boundary in the input domain (margin). Interpreting class stability as a quantifiable notion of robustness, we derive as a corollary a law of robustness for classification that extends the results of Bubeck and Sellke beyond smoothness assumptions to discontinuous functions. In particular, any interpolating model with $p \approx n$ parameters on $n$ data points must be unstable, implying that substantial overparameterization is necessary to achieve high stability. We obtain analogous results for parameterized infinite function classes by analyzing a stronger robustness measure derived from the margin in the codomain, which we refer to as the normalized co-stability. Experiments support our theory: stability increases with model size and correlates with test performance, while traditional norm-based measures remain largely uninformative.

