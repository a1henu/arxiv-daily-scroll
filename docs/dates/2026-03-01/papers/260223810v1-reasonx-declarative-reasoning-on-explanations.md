---
layout: default
title: ReasonX: Declarative Reasoning on Explanations
---

# ReasonX: Declarative Reasoning on Explanations
**arXiv**：[2602.23810v1](https://arxiv.org/abs/2602.23810) · [PDF](https://arxiv.org/pdf/2602.23810.pdf)  
**作者**：Laura State, Salvatore Ruggieri, Franco Turini  

**一句话要点**：提出ReasonX工具，基于线性约束理论代数，为决策树提供声明式交互解释。

**关键词**：可解释人工智能, 声明式推理, 线性约束, 混合整数线性规划, 决策树解释

## 3 点简述
- 核心问题：当前XAI方法存在抽象不足、交互性有限和符号知识整合不充分等缺陷。
- 方法要点：利用混合整数线性规划在事实和对比实例特征上进行推理，支持用户以线性约束表达背景知识。
- 实验或效果：通过定性示例展示能力，并通过定量实验与其他XAI工具进行比较。

## 摘要（原文）

> Explaining opaque Machine Learning (ML) models has become an increasingly important challenge. However, current eXplanation in AI (XAI) methods suffer several shortcomings, including insufficient abstraction, limited user interactivity, and inadequate integration of symbolic knowledge. We propose ReasonX, an explanation tool based on expressions (or, queries) in a closed algebra of operators over theories of linear constraints. ReasonX provides declarative and interactive explanations for decision trees, which may represent the ML models under analysis or serve as global or local surrogate models for any black-box predictor. Users can express background or common sense knowledge as linear constraints. This allows for reasoning at multiple levels of abstraction, ranging from fully specified examples to under-specified or partially constrained ones. ReasonX leverages Mixed-Integer Linear Programming (MILP) to reason over the features of factual and contrastive instances. We present here the architecture of ReasonX, which consists of a Python layer, closer to the user, and a Constraint Logic Programming (CLP) layer, which implements a meta-interpreter of the query algebra. The capabilities of ReasonX are demonstrated through qualitative examples, and compared to other XAI tools through quantitative experiments.

