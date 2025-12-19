---
layout: default
title: Make-It-Poseable: Feed-forward Latent Posing Model for 3D Humanoid Character Animation
---

# Make-It-Poseable: Feed-forward Latent Posing Model for 3D Humanoid Character Animation
**arXiv**：[2512.16767v1](https://arxiv.org/abs/2512.16767) · [PDF](https://arxiv.org/pdf/2512.16767.pdf)  
**作者**：Zhiyang Guo, Ori Zhang, Jax Xiang, Alan Zhao, Wengang Zhou, Houqiang Li  

**一句话要点**：提出Make-It-Poseable，通过潜在空间变换解决3D人形角色动画中的姿态生成问题。

**关键词**：3D角色动画, 潜在空间变换, 姿态生成, 前馈模型, 几何重建, 拓扑适应

## 3 点简述
- 核心问题：现有方法在蒙皮权重预测、拓扑缺陷和姿态一致性方面存在局限，影响鲁棒性和泛化性。
- 方法要点：采用前馈框架，通过潜在姿态变换器基于骨骼运动操作形状令牌，实现直接潜在空间操控。
- 实验或效果：引入潜在空间监督和自适应补全模块，提升几何保真度，支持拓扑变化，并在姿态质量和3D编辑中表现优异。

## 摘要（原文）

> Posing 3D characters is a fundamental task in computer graphics and vision. However, existing methods like auto-rigging and pose-conditioned generation often struggle with challenges such as inaccurate skinning weight prediction, topological imperfections, and poor pose conformance, limiting their robustness and generalizability. To overcome these limitations, we introduce Make-It-Poseable, a novel feed-forward framework that reformulates character posing as a latent-space transformation problem. Instead of deforming mesh vertices as in traditional pipelines, our method reconstructs the character in new poses by directly manipulating its latent representation. At the core of our method is a latent posing transformer that manipulates shape tokens based on skeletal motion. This process is facilitated by a dense pose representation for precise control. To ensure high-fidelity geometry and accommodate topological changes, we also introduce a latent-space supervision strategy and an adaptive completion module. Our method demonstrates superior performance in posing quality. It also naturally extends to 3D editing applications like part replacement and refinement.

