---
layout: default
title: TRACER: Texture-Robust Affordance Chain-of-Thought for Deformable-Object Refinement
---

# TRACER: Texture-Robust Affordance Chain-of-Thought for Deformable-Object Refinement
**arXiv**：[2601.20208v1](https://arxiv.org/abs/2601.20208) · [PDF](https://arxiv.org/pdf/2601.20208.pdf)  
**作者**：Wanjun Jia, Kang Li, Fan Yang, Mengfei Duan, Wenrui Chen, Yiming Jiang, Hui Zhang, Kailun Yang, Zhiyong Li, Yaonan Wang  

**一句话要点**：提出TRACER框架，通过纹理鲁棒性推理链解决可变形物体操作中的语义-物理对齐问题。

**关键词**：可变形物体操作, 纹理鲁棒性, 推理链, 边界精炼, 功能区域预测, 机器人视觉

## 3 点简述
- 核心问题：可变形物体操作中，复杂外观和纹理变化导致语义指令与物理交互点难以对齐，现有方法易产生边界溢出和区域碎片化。
- 方法要点：引入树状推理链分解任务意图，结合空间约束边界精炼和交互收敛精炼流，提升功能区域的完整性和物理一致性。
- 实验或效果：在Fine-AGDDO15数据集和真实机器人平台上验证，显著提高不同纹理下的可操作性预测精度和长时任务成功率。

## 摘要（原文）

> The central challenge in robotic manipulation of deformable objects lies in aligning high-level semantic instructions with physical interaction points under complex appearance and texture variations. Due to near-infinite degrees of freedom, complex dynamics, and heterogeneous patterns, existing vision-based affordance prediction methods often suffer from boundary overflow and fragmented functional regions. To address these issues, we propose TRACER, a Texture-Robust Affordance Chain-of-thought with dEformable-object Refinement framework, which establishes a cross-hierarchical mapping from hierarchical semantic reasoning to appearance-robust and physically consistent functional region refinement. Specifically, a Tree-structured Affordance Chain-of-Thought (TA-CoT) is formulated to decompose high-level task intentions into hierarchical sub-task semantics, providing consistent guidance across various execution stages. To ensure spatial integrity, a Spatial-Constrained Boundary Refinement (SCBR) mechanism is introduced to suppress prediction spillover, guiding the perceptual response to converge toward authentic interaction manifolds. Furthermore, an Interactive Convergence Refinement Flow (ICRF) is developed to aggregate discrete pixels corrupted by appearance noise, significantly enhancing the spatial continuity and physical plausibility of the identified functional regions. Extensive experiments conducted on the Fine-AGDDO15 dataset and a real-world robotic platform demonstrate that TRACER significantly improves affordance grounding precision across diverse textures and patterns inherent to deformable objects. More importantly, it enhances the success rate of long-horizon tasks, effectively bridging the gap between high-level semantic reasoning and low-level physical execution. The source code and dataset will be made publicly available at https://github.com/Dikay1/TRACER.

