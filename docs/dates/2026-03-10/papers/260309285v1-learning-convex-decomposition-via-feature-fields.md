---
layout: default
title: Learning Convex Decomposition via Feature Fields
---

# Learning Convex Decomposition via Feature Fields
**arXiv**：[2603.09285v1](https://arxiv.org/abs/2603.09285) · [PDF](https://arxiv.org/pdf/2603.09285.pdf)  
**作者**：Yuezhi Yang, Qixing Huang, Mikaela Angelina Uy, Nicholas Sharp  

**一句话要点**：提出基于特征场学习的凸分解方法，实现首个前馈模型用于开放世界凸分解。

**关键词**：凸分解, 特征场学习, 自监督学习, 3D形状分析, 物理模拟, 开放世界模型

## 3 点简述
- 核心问题：解决长期存在的凸分解问题，将3D形状分解为凸体以加速物理模拟中的碰撞检测。
- 方法要点：采用特征学习方法，学习连续特征场，通过自监督几何目标聚类获得高质量凸分解。
- 实验或效果：分解质量优于现有方法，泛化至开放世界对象及网格、CAD模型、高斯溅射等多种表示。

## 摘要（原文）

> This work proposes a new formulation to the long-standing problem of convex decomposition through learning feature fields, enabling the first feed-forward model for open-world convex decomposition. Our method produces high-quality decompositions of 3D shapes into a union of convex bodies, which are essential to accelerate collision detection in physical simulation, amongst many other applications. The key insight is to adopt a feature learning approach and learn a continuous feature field that can later be clustered to yield a good convex decomposition via our self-supervised, purely-geometric objective derived from the classical definition of convexity. Our formulation can be used for single shape optimization, but more importantly, feature prediction unlocks scalable, self-supervised learning on large datasets resulting in the first learned open-world model for convex decomposition. Experiments show that our decompositions are higher-quality than alternatives and generalize across open-world objects as well as across representations to meshes, CAD models, and even Gaussian splats. https://research.nvidia.com/labs/sil/projects/learning-convex-decomp/

