---
layout: default
title: Make-It-Poseable: Feed-forward Latent Posing Model for 3D Humanoid Character Animation
---

# Make-It-Poseable: Feed-forward Latent Posing Model for 3D Humanoid Character Animation
**arXiv**：[2512.16767v1](https://arxiv.org/abs/2512.16767) · [PDF](https://arxiv.org/pdf/2512.16767.pdf)  
**作者**：Zhiyang Guo, Ori Zhang, Jax Xiang, Alan Zhao, Wengang Zhou, Houqiang Li  

**一句话要点**：提出Make-It-Poseable，一种前馈潜在空间变换框架，用于3D人形角色动画的精准摆姿。

**关键词**：3D角色摆姿, 潜在空间变换, 前馈框架, 骨骼运动控制, 几何保真, 拓扑适应

## 3 点简述
- 核心问题：现有方法在蒙皮权重预测、拓扑缺陷和姿态一致性方面存在挑战，影响鲁棒性和泛化性。
- 方法要点：通过潜在空间变换，使用潜在摆姿变换器基于骨骼运动操作形状令牌，结合密集姿态表示和自适应补全模块。
- 实验或效果：在摆姿质量上表现优越，并自然扩展到部件替换和细化等3D编辑应用。

## 摘要（原文）

> Posing 3D characters is a fundamental task in computer graphics and vision. However, existing methods like auto-rigging and pose-conditioned generation often struggle with challenges such as inaccurate skinning weight prediction, topological imperfections, and poor pose conformance, limiting their robustness and generalizability. To overcome these limitations, we introduce Make-It-Poseable, a novel feed-forward framework that reformulates character posing as a latent-space transformation problem. Instead of deforming mesh vertices as in traditional pipelines, our method reconstructs the character in new poses by directly manipulating its latent representation. At the core of our method is a latent posing transformer that manipulates shape tokens based on skeletal motion. This process is facilitated by a dense pose representation for precise control. To ensure high-fidelity geometry and accommodate topological changes, we also introduce a latent-space supervision strategy and an adaptive completion module. Our method demonstrates superior performance in posing quality. It also naturally extends to 3D editing applications like part replacement and refinement.

