---
layout: default
title: Implementing Metric Temporal Answer Set Programming
---

# Implementing Metric Temporal Answer Set Programming
**arXiv**：[2601.20735v1](https://arxiv.org/abs/2601.20735) · [PDF](https://arxiv.org/pdf/2601.20735.pdf)  
**作者**：Arvid Becker, Pedro Cabalar, Martin Diéguez, Susana Hahn, Javier Romero, Torsten Schaub  

**一句话要点**：提出基于差异约束的度量时序ASP方法，以解决细粒度时间约束下的可扩展性问题。

**关键词**：度量时序ASP, 差异约束, 可扩展性优化, 时间约束处理, 基础化瓶颈

## 3 点简述
- 核心问题：度量ASP在处理细粒度时间约束时面临可扩展性瓶颈，导致基础化过程复杂化。
- 方法要点：利用ASP扩展的差异约束外部处理时间相关方面，解耦时间粒度与度量ASP。
- 实验或效果：该方法有效提升可扩展性，不受时间精度影响，保持解决方案的稳定性。

## 摘要（原文）

> We develop a computational approach to Metric Answer Set Programming (ASP) to allow for expressing quantitative temporal constraints, like durations and deadlines. A central challenge is to maintain scalability when dealing with fine-grained timing constraints, which can significantly exacerbate ASP's grounding bottleneck. To address this issue, we leverage extensions of ASP with difference constraints, a simplified form of linear constraints, to handle time-related aspects externally. Our approach effectively decouples metric ASP from the granularity of time, resulting in a solution that is unaffected by time precision.

