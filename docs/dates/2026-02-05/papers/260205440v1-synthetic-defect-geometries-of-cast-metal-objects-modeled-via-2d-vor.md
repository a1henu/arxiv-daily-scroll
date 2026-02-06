---
layout: default
title: Synthetic Defect Geometries of Cast Metal Objects Modeled via 2d Voronoi Tessellations
---

# Synthetic Defect Geometries of Cast Metal Objects Modeled via 2d Voronoi Tessellations
**arXiv**：[2602.05440v1](https://arxiv.org/abs/2602.05440) · [PDF](https://arxiv.org/pdf/2602.05440.pdf)  
**作者**：Natascha Jeziorski, Petra Gospodnetić, Claudia Redenbach  

**一句话要点**：提出基于2D Voronoi剖分的参数化缺陷建模方法，用于生成铸造金属对象的合成缺陷数据以支持无损检测训练。

**关键词**：合成缺陷建模, Voronoi剖分, 无损检测, 参数化几何, 机器学习训练数据, 铸造缺陷

## 3 点简述
- 核心问题：工业无损检测中，自动化缺陷检测需要大量高质量训练数据，但真实数据获取困难且罕见缺陷样本不足。
- 方法要点：采用参数化方法，基于2D Voronoi剖分建模3D网格缺陷几何，可生成可控的合成缺陷对象，适用于多种缺陷类型。
- 实验或效果：通过物理模拟生成合成数据，支持像素级标注，能生成大规模可变数据集，包括罕见缺陷，提升机器学习模型训练效果。

## 摘要（原文）

> In industry, defect detection is crucial for quality control. Non-destructive testing (NDT) methods are preferred as they do not influence the functionality of the object while inspecting. Automated data evaluation for automated defect detection is a growing field of research. In particular, machine learning approaches show promising results. To provide training data in sufficient amount and quality, synthetic data can be used. Rule-based approaches enable synthetic data generation in a controllable environment. Therefore, a digital twin of the inspected object including synthetic defects is needed. We present parametric methods to model 3d mesh objects of various defect types that can then be added to the object geometry to obtain synthetic defective objects. The models are motivated by common defects in metal casting but can be transferred to other machining procedures that produce similar defect shapes. Synthetic data resembling the real inspection data can then be created by using a physically based Monte Carlo simulation of the respective testing method. Using our defect models, a variable and arbitrarily large synthetic data set can be generated with the possibility to include rarely occurring defects in sufficient quantity. Pixel-perfect annotation can be created in parallel. As an example, we will use visual surface inspection, but the procedure can be applied in combination with simulations for any other NDT method.

