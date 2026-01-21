---
layout: default
title: Breaking the Data Barrier in Learning Symbolic Computation: A Case Study on Variable Ordering Suggestion for Cylindrical Algebraic Decomposition
---

# Breaking the Data Barrier in Learning Symbolic Computation: A Case Study on Variable Ordering Suggestion for Cylindrical Algebraic Decomposition
**arXiv**：[2601.13731v1](https://arxiv.org/abs/2601.13731) · [PDF](https://arxiv.org/pdf/2601.13731.pdf)  
**作者**：Rui-Juan Jing, Yuegang Zhao, Changbo Chen  

**一句话要点**：提出基于Transformer的预训练-微调方法，以解决圆柱代数分解中变量排序的数据获取难题。

**关键词**：符号计算, 圆柱代数分解, 变量排序, Transformer模型, 预训练微调, 数据增强

## 3 点简述
- 核心问题：符号计算中圆柱代数分解的变量排序效率受限于标注数据稀缺，阻碍学习加速。
- 方法要点：设计关联任务生成大量标注数据，预训练Transformer模型后微调于排序任务。
- 实验或效果：在公开数据集上，新模型预测的排序平均显著优于最佳启发式方法。

## 摘要（原文）

> Symbolic computation, powered by modern computer algebra systems, has important applications in mathematical reasoning through exact deep computations. The efficiency of symbolic computation is largely constrained by such deep computations in high dimension. This creates a fundamental barrier on labelled data acquisition if leveraging supervised deep learning to accelerate symbolic computation. Cylindrical algebraic decomposition (CAD) is a pillar symbolic computation method for reasoning with first-order logic formulas over reals with many applications in formal verification and automatic theorem proving. Variable orderings have a huge impact on its efficiency. Impeded by the difficulty to acquire abundant labelled data, existing learning-based approaches are only competitive with the best expert-based heuristics. In this work, we address this problem by designing a series of intimately connected tasks for which a large amount of annotated data can be easily obtained. We pre-train a Transformer model with these data and then fine-tune it on the datasets for CAD ordering. Experiments on publicly available CAD ordering datasets show that on average the orderings predicted by the new model are significantly better than those suggested by the best heuristic methods.

