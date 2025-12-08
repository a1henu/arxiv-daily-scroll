---
layout: default
title: SplatPainter: Interactive Authoring of 3D Gaussians from 2D Edits via Test-Time Training
---

# SplatPainter: Interactive Authoring of 3D Gaussians from 2D Edits via Test-Time Training
**arXiv**：[2512.05354v1](https://arxiv.org/abs/2512.05354) · [PDF](https://arxiv.org/pdf/2512.05354.pdf)  
**作者**：Yang Zheng, Hao Tan, Kai Zhang, Peng Wang, Leonidas Guibas, Gordon Wetzstein, Wang Yifan  

**一句话要点**：提出SplatPainter，通过测试时训练实现从2D编辑交互式创作3D高斯资产

**关键词**：3D高斯溅射, 交互式编辑, 测试时训练, 状态感知模型, 2D到3D转换

## 3 点简述
- 核心问题：现有方法在3D高斯资产交互式编辑中速度慢、破坏原始身份或缺乏精细控制
- 方法要点：使用状态感知前馈模型直接预测高斯属性更新，结合测试时训练实现迭代工作流
- 实验或效果：支持局部细节优化、局部涂绘和全局重新着色，在交互速度下保持高保真度

## 摘要（原文）

> The rise of 3D Gaussian Splatting has revolutionized photorealistic 3D asset creation, yet a critical gap remains for their interactive refinement and editing. Existing approaches based on diffusion or optimization are ill-suited for this task, as they are often prohibitively slow, destructive to the original asset's identity, or lack the precision for fine-grained control. To address this, we introduce \ourmethod, a state-aware feedforward model that enables continuous editing of 3D Gaussian assets from user-provided 2D view(s). Our method directly predicts updates to the attributes of a compact, feature-rich Gaussian representation and leverages Test-Time Training to create a state-aware, iterative workflow. The versatility of our approach allows a single architecture to perform diverse tasks, including high-fidelity local detail refinement, local paint-over, and consistent global recoloring, all at interactive speeds, paving the way for fluid and intuitive 3D content authoring.

