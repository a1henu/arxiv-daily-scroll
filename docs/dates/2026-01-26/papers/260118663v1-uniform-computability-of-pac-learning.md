---
layout: default
title: Uniform Computability of PAC Learning
---

# Uniform Computability of PAC Learning
**arXiv**：[2601.18663v1](https://arxiv.org/abs/2601.18663) · [PDF](https://arxiv.org/pdf/2601.18663.pdf)  
**作者**：Vasco Brattka, Guillaume Chirache  

**一句话要点**：使用Weihrauch复杂度分析PAC学习的均匀可计算性，分类不同信息表示下的计算复杂度

**关键词**：PAC学习, Weihrauch复杂度, 均匀可计算性, VC维度, 闭概念类, 计算复杂度分类

## 3 点简述
- 研究PAC学习的均匀可计算性，基于Weihrauch复杂度理论
- 分析闭概念类在不同信息表示下的计算等价关系，如正信息与Baire空间极限操作
- 分类VC维度操作的计算复杂度，并探讨其对PAC学习可构造性的影响

## 摘要（原文）

> We study uniform computability properties of PAC learning using Weihrauch complexity. We focus on closed concept classes, which are either represented by positive, by negative or by full information. Among other results, we prove that proper PAC learning from positive information is equivalent to the limit operation on Baire space, whereas improper PAC learning from positive information is closely related to Weak Kőnig's Lemma and even equivalent to it, when we have some negative information about the admissible hypotheses. If arbitrary hypotheses are allowed, then improper PAC learning from positive information is still in a finitary DNC range, which implies that it is non-deterministically computable, but does not allow for probabilistic algorithms. These results can also be seen as a classification of the degree of constructivity of the Fundamental Theorem of Statistical Learning. All the aforementioned results hold if an upper bound of the VC dimension is provided as an additional input information. We also study the question of how these results are affected if the VC dimension is not given, but only promised to be finite or if concept classes are represented by negative or full information. Finally, we also classify the complexity of the VC dimension operation itself, which is a problem that is of independent interest. For positive or full information it turns out to be equivalent to the binary sorting problem, for negative information it is equivalent to the jump of sorting. This classification allows also conclusions regarding the Borel complexity of PAC learnability.

