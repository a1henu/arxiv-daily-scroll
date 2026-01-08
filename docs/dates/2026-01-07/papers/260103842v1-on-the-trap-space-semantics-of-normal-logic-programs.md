---
layout: default
title: On the Trap Space Semantics of Normal Logic Programs
---

# On the Trap Space Semantics of Normal Logic Programs
**arXiv**：[2601.03842v1](https://arxiv.org/abs/2601.03842) · [PDF](https://arxiv.org/pdf/2601.03842.pdf)  
**作者**：Van-Giang Trinh, Sylvain Soliman, François Fages, Belaid Benhamou  

**一句话要点**：提出陷阱空间语义以统一解释普通逻辑程序的模型论与动态行为。

**关键词**：逻辑程序语义, 陷阱空间, 模型论, 动态语义, 布尔网络, 统一框架

## 3 点简述
- 核心问题：传统语义如稳定模型和正则模型缺乏统一框架，难以全面捕捉程序行为。
- 方法要点：将布尔网络的陷阱空间概念推广至普通逻辑程序，建立模型论与动态表征。
- 实验或效果：证明陷阱空间语义能统一证明支持类、严格稳定类和正则模型的存在性。

## 摘要（原文）

> The logical semantics of normal logic programs has traditionally been based on the notions of Clark's completion and two-valued or three-valued canonical models, including supported, stable, regular, and well-founded models. Two-valued interpretations can also be seen as states evolving under a program's update operator, producing a transition graph whose fixed points and cycles capture stable and oscillatory behaviors, respectively. We refer to this view as dynamical semantics since it characterizes the program's meaning in terms of state-space trajectories, as first introduced in the stable (supported) class semantics. Recently, we have established a formal connection between Datalog^\neg programs (i.e., normal logic programs without function symbols) and Boolean networks, leading to the introduction of the trap space concept for Datalog^\neg programs. In this paper, we generalize the trap space concept to arbitrary normal logic programs, introducing trap space semantics as a new approach to their interpretation. This new semantics admits both model-theoretic and dynamical characterizations, providing a comprehensive approach to understanding program behavior. We establish the foundational properties of the trap space semantics and systematically relate it to the established model-theoretic semantics, including the stable (supported), stable (supported) partial, regular, and L-stable model semantics, as well as to the dynamical stable (supported) class semantics. Our results demonstrate that the trap space semantics offers a unified and precise framework for proving the existence of supported classes, strict stable (supported) classes, and regular models, in addition to uncovering and formalizing deeper relationships among the existing semantics of normal logic programs.

