---
layout: default
title: Understanding or Memorizing? A Case Study of German Definite Articles in Language Models
---

# Understanding or Memorizing? A Case Study of German Definite Articles in Language Models
**arXiv**：[2601.09313v1](https://arxiv.org/abs/2601.09313) · [PDF](https://arxiv.org/pdf/2601.09313.pdf)  
**作者**：Jonathan Drechsel, Erisa Bytyqi, Steffen Herbold  

**一句话要点**：提出GRADIEND方法以分析语言模型对德语定冠词的处理机制，揭示其依赖记忆而非严格规则。

**关键词**：语言模型解释性, 梯度分析, 语法泛化, 记忆机制, 德语定冠词

## 3 点简述
- 核心问题：语言模型在德语定冠词语法一致上的表现是基于规则泛化还是记忆关联。
- 方法要点：使用GRADIEND梯度解释方法学习性别-格特定冠词转换的参数更新方向。
- 实验或效果：发现针对特定转换的更新常影响无关设置，神经元重叠显著，支持记忆主导。

## 摘要（原文）

> Language models perform well on grammatical agreement, but it is unclear whether this reflects rule-based generalization or memorization. We study this question for German definite singular articles, whose forms depend on gender and case. Using GRADIEND, a gradient-based interpretability method, we learn parameter update directions for gender-case specific article transitions. We find that updates learned for a specific gender-case article transition frequently affect unrelated gender-case settings, with substantial overlap among the most affected neurons across settings. These results argue against a strictly rule-based encoding of German definite articles, indicating that models at least partly rely on memorized associations rather than abstract grammatical rules.

