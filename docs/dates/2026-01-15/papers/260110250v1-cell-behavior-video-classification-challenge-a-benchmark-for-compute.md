---
layout: default
title: Cell Behavior Video Classification Challenge, a benchmark for computer vision methods in time-lapse microscopy
---

# Cell Behavior Video Classification Challenge, a benchmark for computer vision methods in time-lapse microscopy
**arXiv**：[2601.10250v1](https://arxiv.org/abs/2601.10250) · [PDF](https://arxiv.org/pdf/2601.10250.pdf)  
**作者**：Raffaella Fiamma Cabini, Deborah Barkauskas, Guangyu Chen, Zhi-Qi Cheng, David E Cicchetti, Judith Drazba, Rodrigo Fernandez-Gonzalez, Raymond Hawkins, Yujia Hu, Jyoti Kini, Charles LeWarne, Xufeng Lin, Sai Preethi Nakkina, John W Peterson, Koert Schreurs, Ayushi Singh, Kumaran Bala Kandan Viswanathan, Inge MN Wortel, Sanjian Zhang, Rolf Krause, Santiago Fernandez Gonzalez, Diego Ulisse Pizzagalli  

**一句话要点**：组织细胞行为视频分类挑战赛，基准测试三种计算机视觉方法以解决显微镜视频中复杂细胞行为的分类问题。

**关键词**：细胞行为视频分类, 显微镜视频分析, 时空特征提取, 端到端深度学习, 跟踪衍生特征, 计算机视觉基准测试

## 3 点简述
- 核心问题：显微镜视频中复杂细胞行为的分类是计算机视觉前沿，需建模无刚性边界物体的形状与运动、提取序列的层次时空特征、处理多对象。
- 方法要点：基准测试35种方法，基于跟踪衍生特征分类、端到端深度学习架构直接学习视频序列特征、或集成跟踪与图像特征。
- 实验或效果：讨论参与者结果，比较各方法的潜力与局限性，为细胞动力学研究提供方法开发基础。

## 摘要（原文）

> The classification of microscopy videos capturing complex cellular behaviors is crucial for understanding and quantifying the dynamics of biological processes over time. However, it remains a frontier in computer vision, requiring approaches that effectively model the shape and motion of objects without rigid boundaries, extract hierarchical spatiotemporal features from entire image sequences rather than static frames, and account for multiple objects within the field of view.
>   To this end, we organized the Cell Behavior Video Classification Challenge (CBVCC), benchmarking 35 methods based on three approaches: classification of tracking-derived features, end-to-end deep learning architectures to directly learn spatiotemporal features from the entire video sequence without explicit cell tracking, or ensembling tracking-derived with image-derived features.
>   We discuss the results achieved by the participants and compare the potential and limitations of each approach, serving as a basis to foster the development of computer vision methods for studying cellular dynamics.

