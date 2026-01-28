---
layout: default
title: Robustness of Constraint Automata for Description Logics with Concrete Domains
---

# Robustness of Constraint Automata for Description Logics with Concrete Domains
**arXiv**：[2601.19644v1](https://arxiv.org/abs/2601.19644) · [PDF](https://arxiv.org/pdf/2601.19644.pdf)  
**作者**：Stéphane Demri, Tianwen Gu  

**一句话要点**：提出基于约束自动机的方法，为带具体域的描述逻辑提供EXPTIME最优上界

**关键词**：描述逻辑, 具体域, 约束自动机, EXPTIME复杂度, 本体一致性, 符号约束

## 3 点简述
- 研究带具体域的描述逻辑一致性问题的可判定性与复杂度，传统方法基于表或类型消除
- 引入约束自动机，通过符号约束丰富转移，证明非空问题在EXPTIME内
- 将结果扩展至逆角色、功能角色名和约束断言，保持EXPTIME成员资格，展示方法鲁棒性

## 摘要（原文）

> Decidability or complexity issues about the consistency problem for description logics with concrete domains have already been analysed with tableaux-based or type elimination methods. Concrete domains in ontologies are essential to consider concrete objects and predefined relations. In this work, we expose an automata-based approach leading to the optimal upper bound EXPTIME, that is designed by enriching the transitions with symbolic constraints. We show that the nonemptiness problem for such automata belongs to EXPTIME if the concrete domains satisfy a few simple properties. Then, we provide a reduction from the consistency problem for ontologies, yielding EXPTIME-membership.Thanks to the expressivity of constraint automata, the results are extended to additional ingredients such as inverse roles, functional role names and constraint assertions, while maintaining EXPTIME-membership, which illustrates the robustness of the approach

