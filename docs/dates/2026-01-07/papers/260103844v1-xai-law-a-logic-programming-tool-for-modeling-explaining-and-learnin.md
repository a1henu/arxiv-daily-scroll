---
layout: default
title: XAI-LAW: A Logic Programming Tool for Modeling, Explaining, and Learning Legal Decisions
---

# XAI-LAW: A Logic Programming Tool for Modeling, Explaining, and Learning Legal Decisions
**arXiv**：[2601.03844v1](https://arxiv.org/abs/2601.03844) · [PDF](https://arxiv.org/pdf/2601.03844.pdf)  
**作者**：Agostino Dovier, Talissa Dreossi, Andrea Formisano, Benedetta Strizzolo  

**一句话要点**：提出基于答案集编程的意大利刑法建模与半自动规则学习工具，支持法律决策推理与解释。

**关键词**：答案集编程, 法律决策建模, 规则学习, 可解释人工智能, 刑法分析, 归纳逻辑编程

## 3 点简述
- 核心问题：如何建模意大利刑法条款并基于司法案例半自动学习法律规则，以支持刑事审判推理。
- 方法要点：使用答案集编程编码刑法条款，处理矛盾，通过稳定模型支持性提供解释，并集成归纳逻辑编程系统。
- 实验或效果：在先前判决集上验证模型，生成新案例决策，增强决策过程可解释性。

## 摘要（原文）

> We propose an approach to model articles of the Italian Criminal Code (ICC), using Answer Set Programming (ASP), and to semi-automatically learn legal rules from examples based on prior judicial decisions. The developed tool is intended to support legal experts during the criminal trial phase by providing reasoning and possible legal outcomes. The methodology involves analyzing and encoding articles of the ICC in ASP, including "crimes against the person" and property offenses. The resulting model is validated on a set of previous verdicts and refined as necessary. During the encoding process, contradictions may arise; these are properly handled by the system, which also generates possible decisions for new cases and provides explanations through a tool that leverages the "supportedness" of stable models. The automatic explainability offered by the tool can also be used to clarify the logic behind judicial decisions, making the decision-making process more interpretable. Furthermore, the tool integrates an inductive logic programming system for ASP, which is employed to generalize legal rules from case examples.

