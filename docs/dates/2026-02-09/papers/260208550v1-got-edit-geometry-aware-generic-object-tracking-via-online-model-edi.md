---
layout: default
title: GOT-Edit: Geometry-Aware Generic Object Tracking via Online Model Editing
---

# GOT-Edit: Geometry-Aware Generic Object Tracking via Online Model Editing
**arXiv**：[2602.08550v1](https://arxiv.org/abs/2602.08550) · [PDF](https://arxiv.org/pdf/2602.08550.pdf)  
**作者**：Shih-Fang Chen, Jun-Cheng Chen, I-Hong Jhuo, Yen-Yu Lin  

**一句话要点**：提出GOT-Edit，通过在线模型编辑整合几何感知线索以提升通用目标跟踪在遮挡和杂乱场景下的性能。

**关键词**：通用目标跟踪, 几何感知, 在线模型编辑, 零空间约束, 视觉几何Transformer, 跨模态融合

## 3 点简述
- 核心问题：通用目标跟踪方法依赖2D特征，忽略3D几何线索，易受遮挡和干扰影响。
- 方法要点：利用预训练视觉几何Transformer提取几何线索，通过零空间约束在线编辑模型融合几何与语义信息。
- 实验或效果：在多个基准测试中表现优异，尤其在遮挡和杂乱环境下，实现更高鲁棒性和准确性。

## 摘要（原文）

> Human perception for effective object tracking in a 2D video stream arises from the implicit use of prior 3D knowledge combined with semantic reasoning. In contrast, most generic object tracking (GOT) methods primarily rely on 2D features of the target and its surroundings while neglecting 3D geometric cues, which makes them susceptible to partial occlusion, distractors, and variations in geometry and appearance. To address this limitation, we introduce GOT-Edit, an online cross-modality model editing approach that integrates geometry-aware cues into a generic object tracker from a 2D video stream. Our approach leverages features from a pre-trained Visual Geometry Grounded Transformer to enable geometric cue inference from only a few 2D images. To tackle the challenge of seamlessly combining geometry and semantics, GOT-Edit performs online model editing with null-space constrained updates that incorporate geometric information while preserving semantic discrimination, yielding consistently better performance across diverse scenarios. Extensive experiments on multiple GOT benchmarks demonstrate that GOT-Edit achieves superior robustness and accuracy, particularly under occlusion and clutter, establishing a new paradigm for combining 2D semantics with 3D geometric reasoning for generic object tracking.

