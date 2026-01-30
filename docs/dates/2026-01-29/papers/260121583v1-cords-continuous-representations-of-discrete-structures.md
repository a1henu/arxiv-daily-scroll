---
layout: default
title: CORDS: Continuous Representations of Discrete Structures
---

# CORDS: Continuous Representations of Discrete Structures
**arXiv**：[2601.21583v1](https://arxiv.org/abs/2601.21583) · [PDF](https://arxiv.org/pdf/2601.21583.pdf)  
**作者**：Tin Hadži Veljković, Erik Bekkers, Michael Tiemann, Jan-Willem van de Meent  

**一句话要点**：提出CORDS方法，通过连续场表示可变大小集合以解决未知对象数量的预测问题。

**关键词**：连续表示, 可变大小集合, 可逆映射, 密度场, 特征场, 未知对象数量预测

## 3 点简述
- 核心问题：预测可变大小集合时，现有方法依赖填充或显式推断集合大小，面临挑战。
- 方法要点：提供可逆映射，将空间对象集合转换为连续密度场和特征场，模型在连续空间操作。
- 实验或效果：在分子生成、物体检测等任务中评估，展示对未知集合大小的鲁棒处理与竞争性准确性。

## 摘要（原文）

> Many learning problems require predicting sets of objects when the number of objects is not known beforehand. Examples include object detection, molecular modeling, and scientific inference tasks such as astrophysical source detection. Existing methods often rely on padded representations or must explicitly infer the set size, which often poses challenges. We present a novel strategy for addressing this challenge by casting prediction of variable-sized sets as a continuous inference problem. Our approach, CORDS (Continuous Representations of Discrete Structures), provides an invertible mapping that transforms a set of spatial objects into continuous fields: a density field that encodes object locations and count, and a feature field that carries their attributes over the same support. Because the mapping is invertible, models operate entirely in field space while remaining exactly decodable to discrete sets. We evaluate CORDS across molecular generation and regression, object detection, simulation-based inference, and a mathematical task involving recovery of local maxima, demonstrating robust handling of unknown set sizes with competitive accuracy.

