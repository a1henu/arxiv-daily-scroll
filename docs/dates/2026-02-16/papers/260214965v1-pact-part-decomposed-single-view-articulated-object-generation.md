---
layout: default
title: PAct: Part-Decomposed Single-View Articulated Object Generation
---

# PAct: Part-Decomposed Single-View Articulated Object Generation
**arXiv**：[2602.14965v1](https://arxiv.org/abs/2602.14965) · [PDF](https://arxiv.org/pdf/2602.14965.pdf)  
**作者**：Qingming Liu, Xinyue Yao, Shuyuan Zhang, Yueci Deng, Guiliang Liu, Zhen Liu, Kui Jia  

**一句话要点**：提出PAct：基于部件分解的单视图铰接物体生成框架，以快速合成高保真铰接资产。

**关键词**：铰接物体生成, 部件分解, 单视图重建, 快速推理, 运动学建模

## 3 点简述
- 核心问题：铰接物体生成需可靠部件分解与运动学装配，现有方法效率低或准确性不足。
- 方法要点：采用部件中心生成框架，通过部件感知条件合成几何、组合与运动，避免逐实例优化。
- 实验或效果：在常见类别上优于优化与检索基线，提升输入一致性、部件准确性与运动合理性，大幅减少推理时间。

## 摘要（原文）

> Articulated objects are central to interactive 3D applications, including embodied AI, robotics, and VR/AR, where functional part decomposition and kinematic motion are essential. Yet producing high-fidelity articulated assets remains difficult to scale because it requires reliable part decomposition and kinematic rigging. Existing approaches largely fall into two paradigms: optimization-based reconstruction or distillation, which can be accurate but often takes tens of minutes to hours per instance, and inference-time methods that rely on template or part retrieval, producing plausible results that may not match the specific structure and appearance in the input observation. We introduce a part-centric generative framework for articulated object creation that synthesizes part geometry, composition, and articulation under explicit part-aware conditioning. Our representation models an object as a set of movable parts, each encoded by latent tokens augmented with part identity and articulation cues. Conditioned on a single image, the model generates articulated 3D assets that preserve instance-level correspondence while maintaining valid part structure and motion. The resulting approach avoids per-instance optimization, enables fast feed-forward inference, and supports controllable assembly and articulation, which are important for embodied interaction. Experiments on common articulated categories (e.g., drawers and doors) show improved input consistency, part accuracy, and articulation plausibility over optimization-based and retrieval-driven baselines, while substantially reducing inference time.

