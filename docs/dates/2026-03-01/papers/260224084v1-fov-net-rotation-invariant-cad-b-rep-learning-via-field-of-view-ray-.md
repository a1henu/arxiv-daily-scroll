---
layout: default
title: FoV-Net: Rotation-Invariant CAD B-rep Learning via Field-of-View Ray Casting
---

# FoV-Net: Rotation-Invariant CAD B-rep Learning via Field-of-View Ray Casting
**arXiv**：[2602.24084v1](https://arxiv.org/abs/2602.24084) · [PDF](https://arxiv.org/pdf/2602.24084.pdf)  
**作者**：Matteo Ballegeer, Dries F. Benoit  

**一句话要点**：提出FoV-Net以解决B-rep学习中的旋转敏感性问题

**关键词**：B-rep学习, 旋转不变性, 视场射线投射, 图注意力网络, CAD分析, 3D形状表示

## 3 点简述
- 现有B-rep学习方法依赖绝对坐标，对旋转高度敏感，准确率可能从95%降至10%
- FoV-Net通过局部参考帧UV网格和视场射线投射网格，以旋转不变方式编码局部几何和全局上下文
- 在B-rep分类和分割基准上实现最先进性能，对任意旋转鲁棒且训练数据需求更少

## 摘要（原文）

> Learning directly from boundary representations (B-reps) has significantly advanced 3D CAD analysis. However, state-of-the-art B-rep learning methods rely on absolute coordinates and normals to encode global context, making them highly sensitive to rotations. Our experiments reveal that models achieving over 95% accuracy on aligned benchmarks can collapse to as low as 10% under arbitrary $\mathbf{SO}(3)$ rotations. To address this, we introduce FoV-Net, the first B-rep learning framework that captures both local surface geometry and global structural context in a rotation-invariant manner. Each face is represented by a Local Reference Frame (LRF) UV-grid that encodes its local surface geometry, and by Field-of-View (FoV) grids that capture the surrounding 3D context by casting rays and recording intersections with neighboring faces. Lightweight CNNs extract per-face features, which are propagated over the B-rep graph using a graph attention network. FoV-Net achieves state-of-the-art performance on B-rep classification and segmentation benchmarks, demonstrating robustness to arbitrary rotations while also requiring less training data to achieve strong results.

