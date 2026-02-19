---
layout: default
title: Temporal Panel Selection in Ongoing Citizens' Assemblies
---

# Temporal Panel Selection in Ongoing Citizens' Assemblies
**arXiv**：[2602.16194v1](https://arxiv.org/abs/2602.16194) · [PDF](https://arxiv.org/pdf/2602.16194.pdf)  
**作者**：Yusuf Hakan Kalayci, Evi Micha  

**一句话要点**：提出持续公民大会中的时间面板选择算法，以在度量空间中实现比例代表性和个体公平性。

**关键词**：公民大会, 时间排序, 比例代表性, 个体公平性, 度量空间, 算法设计

## 3 点简述
- 核心问题：如何在持续公民大会中，通过旋转面板实现跨时间序列的比例代表性和个体公平性。
- 方法要点：扩展比例代表性到时间设置，要求面板序列的每个初始段累积反映人口结构。
- 实验或效果：未知，但算法提供不同保证，在个体面板内和跨面板序列中维持代表性。

## 摘要（原文）

> Permanent citizens' assemblies are ongoing deliberative bodies composed of randomly selected citizens, organized into panels that rotate over time. Unlike one-off panels, which represent the population in a single snapshot, permanent assemblies enable shifting participation across multiple rounds. This structure offers a powerful framework for ensuring that different groups of individuals are represented over time across successive panels. In particular, it allows smaller groups of individuals that may not warrant representation in every individual panel to be represented across a sequence of them. We formalize this temporal sortition framework by requiring proportional representation both within each individual panel and across the sequence of panels.
>   Building on the work of Ebadian and Micha (2025), we consider a setting in which the population lies in a metric space, and the goal is to achieve both proportional representation, ensuring that every group of citizens receives adequate representation, and individual fairness, ensuring that each individual has an equal probability of being selected. We extend the notion of representation to a temporal setting by requiring that every initial segment of the panel sequence, viewed as a cumulative whole, proportionally reflects the structure of the population. We present algorithms that provide varying guarantees of proportional representation, both within individual panels and across any sequence of panels, while also maintaining individual fairness over time.

