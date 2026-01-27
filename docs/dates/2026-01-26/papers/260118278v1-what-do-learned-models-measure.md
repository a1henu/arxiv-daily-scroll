---
layout: default
title: What Do Learned Models Measure?
---

# What Do Learned Models Measure?
**arXiv**：[2601.18278v1](https://arxiv.org/abs/2601.18278) · [PDF](https://arxiv.org/pdf/2601.18278.pdf)  
**作者**：Indrė Žliobaitė  

**一句话要点**：提出测量稳定性以评估机器学习模型作为测量工具时的可靠性

**关键词**：测量稳定性, 学习测量函数, 模型评估, 分布偏移, 机器学习应用

## 3 点简述
- 核心问题：机器学习模型用作测量工具时，标准评估标准无法保证测量映射的稳定性
- 方法要点：形式化学习测量函数，引入测量稳定性作为评估维度，强调跨学习过程和上下文的恒定性
- 实验或效果：通过真实案例研究，展示预测性能相当的模型可实现系统不等价的测量函数，分布偏移凸显此问题

## 摘要（原文）

> In many scientific and data-driven applications, machine learning models are increasingly used as measurement instruments, rather than merely as predictors of predefined labels. When the measurement function is learned from data, the mapping from observations to quantities is determined implicitly by the training distribution and inductive biases, allowing multiple inequivalent mappings to satisfy standard predictive evaluation criteria. We formalize learned measurement functions as a distinct focus of evaluation and introduce measurement stability, a property capturing invariance of the measured quantity across admissible realizations of the learning process and across contexts. We show that standard evaluation criteria in machine learning, including generalization error, calibration, and robustness, do not guarantee measurement stability. Through a real-world case study, we show that models with comparable predictive performance can implement systematically inequivalent measurement functions, with distribution shift providing a concrete illustration of this failure. Taken together, our results highlight a limitation of existing evaluation frameworks in settings where learned model outputs are identified as measurements, motivating the need for an additional evaluative dimension.

