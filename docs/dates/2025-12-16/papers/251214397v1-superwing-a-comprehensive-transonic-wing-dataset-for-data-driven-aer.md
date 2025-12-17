---
layout: default
title: SuperWing: a comprehensive transonic wing dataset for data-driven aerodynamic design
---

# SuperWing: a comprehensive transonic wing dataset for data-driven aerodynamic design
**arXiv**：[2512.14397v1](https://arxiv.org/abs/2512.14397) · [PDF](https://arxiv.org/pdf/2512.14397.pdf)  
**作者**：Yunjia Yang, Weishao Tang, Mengxin Liu, Nils Thuerey, Yufei Zhang, Haixin Chen  

**一句话要点**：提出SuperWing数据集以解决三维机翼气动设计中数据稀缺和多样性不足的问题。

**关键词**：气动设计, 机器学习代理模型, 三维机翼数据集, 流场模拟, 零样本泛化

## 3 点简述
- 核心问题：现有数据集稀缺且多样性受限，阻碍了机器学习代理模型在三维机翼气动设计中的通用性发展。
- 方法要点：通过参数化几何生成4,239个机翼形状，模拟28,856个流场解，覆盖典型飞行包线，增强数据多样性。
- 实验或效果：基准测试显示Transformer模型准确预测表面流动，并在复杂基准机翼上表现出强零样本泛化能力。

## 摘要（原文）

> Machine-learning surrogate models have shown promise in accelerating aerodynamic design, yet progress toward generalizable predictors for three-dimensional wings has been limited by the scarcity and restricted diversity of existing datasets. Here, we present SuperWing, a comprehensive open dataset of transonic swept-wing aerodynamics comprising 4,239 parameterized wing geometries and 28,856 Reynolds-averaged Navier-Stokes flow field solutions. The wing shapes in the dataset are generated using a simplified yet expressive geometry parameterization that incorporates spanwise variations in airfoil shape, twist, and dihedral, allowing for an enhanced diversity without relying on perturbations of a baseline wing. All shapes are simulated under a broad range of Mach numbers and angles of attack covering the typical flight envelope. To demonstrate the dataset's utility, we benchmark two state-of-the-art Transformers that accurately predict surface flow and achieve a 2.5 drag-count error on held-out samples. Models pretrained on SuperWing further exhibit strong zero-shot generalization to complex benchmark wings such as DLR-F6 and NASA CRM, underscoring the dataset's diversity and potential for practical usage.

