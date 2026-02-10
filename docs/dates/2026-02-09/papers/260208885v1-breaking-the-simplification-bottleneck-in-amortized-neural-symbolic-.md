---
layout: default
title: Breaking the Simplification Bottleneck in Amortized Neural Symbolic Regression
---

# Breaking the Simplification Bottleneck in Amortized Neural Symbolic Regression
**arXiv**：[2602.08885v1](https://arxiv.org/abs/2602.08885) · [PDF](https://arxiv.org/pdf/2602.08885.pdf)  
**作者**：Paul Saegert, Ullrich Köthe  

**一句话要点**：提出SimpliPy简化引擎以解决摊销神经符号回归中的计算瓶颈

**关键词**：符号回归, 摊销学习, 表达式简化, 计算机代数系统, 神经符号方法

## 3 点简述
- 核心问题：摊销符号回归因缺乏快速表达式简化而难以扩展至实际科学复杂度
- 方法要点：开发基于规则的SimpliPy简化引擎，相比SymPy实现百倍加速
- 实验或效果：在Flash-ANSR框架中提升准确率，与PySR性能相当但表达式更简洁

## 摘要（原文）

> Symbolic regression (SR) aims to discover interpretable analytical expressions that accurately describe observed data. Amortized SR promises to be much more efficient than the predominant genetic programming SR methods, but currently struggles to scale to realistic scientific complexity. We find that a key obstacle is the lack of a fast reduction of equivalent expressions to a concise normalized form. Amortized SR has addressed this by general-purpose Computer Algebra Systems (CAS) like SymPy, but the high computational cost severely limits training and inference speed. We propose SimpliPy, a rule-based simplification engine achieving a 100-fold speed-up over SymPy at comparable quality. This enables substantial improvements in amortized SR, including scalability to much larger training sets, more efficient use of the per-expression token budget, and systematic training set decontamination with respect to equivalent test expressions. We demonstrate these advantages in our Flash-ANSR framework, which achieves much better accuracy than amortized baselines (NeSymReS, E2E) on the FastSRB benchmark. Moreover, it performs on par with state-of-the-art direct optimization (PySR) while recovering more concise instead of more complex expressions with increasing inference budget.

