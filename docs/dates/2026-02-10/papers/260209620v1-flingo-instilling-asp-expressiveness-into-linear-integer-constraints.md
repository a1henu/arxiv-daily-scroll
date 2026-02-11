---
layout: default
title: FLINGO -- Instilling ASP Expressiveness into Linear Integer Constraints
---

# FLINGO -- Instilling ASP Expressiveness into Linear Integer Constraints
**arXiv**：[2602.09620v1](https://arxiv.org/abs/2602.09620) · [PDF](https://arxiv.org/pdf/2602.09620.pdf)  
**作者**：Jorge Fandinno, Pedro Cabalar, Philipp Wanko, Torsten Schaub  

**一句话要点**：提出FLINGO语言以在约束答案集编程中融入ASP表达性

**关键词**：约束答案集编程, 答案集编程, 数值约束, 语言设计, 语义翻译

## 3 点简述
- 核心问题：CASP中数值约束表达性不足，丢失ASP的默认值、未定义属性等特性
- 方法要点：设计FLINGO语言，将ASP表达性嵌入数值约束，并翻译为标准CASP格式
- 实验或效果：通过示例展示FLINGO应用，基于先前语义基础实现语法翻译

## 摘要（原文）

> Constraint Answer Set Programming (CASP) is a hybrid paradigm that enriches Answer Set Programming (ASP) with numerical constraint processing, something required in many real-world applications. The usual specification of constraints in most CASP solvers is closer to the numerical back-end expressiveness and semantics, rather than to standard specification in ASP. In the latter, numerical attributes are represented with predicates and this allows declaring default values, leaving the attribute undefined, making non-deterministic assignments with choice rules or using aggregated values. In CASP, most (if not all) of these features are lost once we switch to a constraint-based representation of those same attributes. In this paper, we present the FLINGO language (and tool) that incorporates the aforementioned expressiveness inside the numerical constraints and we illustrate its use with several examples. Based on previous work that established its semantic foundations, we also present a translation from the newly introduced FLINGO syntax to regular CASP programs following the CLINGCON input format.

