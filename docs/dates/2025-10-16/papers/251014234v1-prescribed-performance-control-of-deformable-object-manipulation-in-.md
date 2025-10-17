---
layout: default
title: Prescribed Performance Control of Deformable Object Manipulation in Spatial Latent Space
---

# Prescribed Performance Control of Deformable Object Manipulation in Spatial Latent Space
**arXiv**：[2510.14234v1](https://arxiv.org/abs/2510.14234) · [PDF](https://arxiv.org/pdf/2510.14234.pdf)  
**作者**：Ning Han, Gu Gong, Bin Zhang, Yuexuan Xu, Bohan Yang, Yunhui Liu, David Navarro-Alarcon  

**一句话要点**：提出基于关键点与规定性能控制的模型无关方法，用于三维可变形物体形状控制。

**关键词**：可变形物体操纵, 规定性能控制, 关键点提取, 视觉伺服, 障碍李雅普诺夫函数, 变形雅可比矩阵

## 3 点简述
- 核心问题：三维可变形物体操纵因无限维状态空间和复杂变形动力学而具挑战性。
- 方法要点：使用关键点坐标作为特征向量，结合变形雅可比矩阵和障碍李雅普诺夫函数进行控制。
- 实验或效果：实验验证了方法的有效性和鲁棒性，闭环系统稳定性通过李雅普诺夫方法分析。

## 摘要（原文）

> Manipulating three-dimensional (3D) deformable objects presents significant
> challenges for robotic systems due to their infinite-dimensional state space
> and complex deformable dynamics. This paper proposes a novel model-free
> approach for shape control with constraints imposed on key points. Unlike
> existing methods that rely on feature dimensionality reduction, the proposed
> controller leverages the coordinates of key points as the feature vector, which
> are extracted from the deformable object's point cloud using deep learning
> methods. This approach not only reduces the dimensionality of the feature space
> but also retains the spatial information of the object. By extracting key
> points, the manipulation of deformable objects is simplified into a visual
> servoing problem, where the shape dynamics are described using a deformation
> Jacobian matrix. To enhance control accuracy, a prescribed performance control
> method is developed by integrating barrier Lyapunov functions (BLF) to enforce
> constraints on the key points. The stability of the closed-loop system is
> rigorously analyzed and verified using the Lyapunov method. Experimental
> results further demonstrate the effectiveness and robustness of the proposed
> method.

