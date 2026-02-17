---
layout: default
title: Learning Proposes, Geometry Disposes: A Modular Framework for Efficient Spatial Reasoning
---

# Learning Proposes, Geometry Disposes: A Modular Framework for Efficient Spatial Reasoning
**arXiv**：[2602.14409v1](https://arxiv.org/abs/2602.14409) · [PDF](https://arxiv.org/pdf/2602.14409.pdf)  
**作者**：Haichao Zhu, Zhaorui Yang, Qian Zhang  

**一句话要点**：提出模块化框架，以学习提出几何假设、几何算法决策，用于RGB-D序列的相对相机姿态估计。

**关键词**：空间感知, 相对相机姿态估计, 模块化框架, RGB-D序列, 几何对齐, 学习与几何结合

## 3 点简述
- 核心问题：学习组件应直接替代几何估计还是作为中间模块，以提升空间感知的效率和鲁棒性。
- 方法要点：结合VGGT学习模型提出姿态和深度假设，后接点对平面RGB-D ICP几何后端进行验证和决策。
- 实验或效果：在TUM RGB-D基准上，几何对齐的学习深度结合几何处理阶段，在中等挑战刚性场景中带来一致改进。

## 摘要（原文）

> Spatial perception aims to estimate camera motion and scene structure from visual observations, a problem traditionally addressed through geometric modeling and physical consistency constraints. Recent learning-based methods have demonstrated strong representational capacity for geometric perception and are increasingly used to augment classical geometry-centric systems in practice. However, whether learning components should directly replace geometric estimation or instead serve as intermediate modules within such pipelines remains an open question.
>   In this work, we address this gap and investigate an end-to-end modular framework for effective spatial reasoning, where learning proposes geometric hypotheses, while geometric algorithms dispose estimation decisions. In particular, we study this principle in the context of relative camera pose estimation on RGB-D sequences. Using VGGT as a representative learning model, we evaluate learning-based pose and depth proposals under varying motion magnitudes and scene dynamics, followed by a classical point-to-plane RGB-D ICP as the geometric backend. Our experiments on the TUM RGB-D benchmark reveal three consistent findings: (1) learning-based pose proposals alone are unreliable; (2) learning-proposed geometry, when improperly aligned with camera intrinsics, can degrade performance; and (3) when learning-proposed depth is geometrically aligned and followed by a geometric disposal stage, consistent improvements emerge in moderately challenging rigid settings.
>   These results demonstrate that geometry is not merely a refinement component, but an essential arbiter that validates and absorbs learning-based geometric observations. Our study highlights the importance of modular, geometry-aware system design for robust spatial perception.

