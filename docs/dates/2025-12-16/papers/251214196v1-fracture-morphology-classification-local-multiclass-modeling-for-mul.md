---
layout: default
title: Fracture Morphology Classification: Local Multiclass Modeling for Multilabel Complexity
---

# Fracture Morphology Classification: Local Multiclass Modeling for Multilabel Complexity
**arXiv**：[2512.14196v1](https://arxiv.org/abs/2512.14196) · [PDF](https://arxiv.org/pdf/2512.14196.pdf)  
**作者**：Cassandra Krause, Mattias P. Heinrich, Ron Keuth  

**一句话要点**：提出局部多类建模方法以解决骨折形态分类中的多标签复杂性，提升诊断准确性。

**关键词**：骨折形态分类, 多标签任务, 局部多类建模, AO代码, 医学图像分析, F1分数提升

## 3 点简述
- 核心问题：儿童骨折诊断需准确分类骨折形态，但现有方法面临多标签任务复杂性挑战。
- 方法要点：通过自动分配全局AO代码到骨折边界框，将全局多标签任务转化为局部多类任务。
- 实验或效果：在公共数据集上平均F1分数提升7.89%，但使用不完美检测器时性能下降。

## 摘要（原文）

> Between $15\,\%$ and $45\,\%$ of children experience a fracture during their growth years, making accurate diagnosis essential. Fracture morphology, alongside location and fragment angle, is a key diagnostic feature. In this work, we propose a method to extract fracture morphology by assigning automatically global AO codes to corresponding fracture bounding boxes. This approach enables the use of public datasets and reformulates the global multilabel task into a local multiclass one, improving the average F1 score by $7.89\,\%$. However, performance declines when using imperfect fracture detectors, highlighting challenges for real-world deployment. Our code is available on GitHub.

