---
layout: default
title: VHOI: Controllable Video Generation of Human-Object Interactions from Sparse Trajectories via Motion Densification
---

# VHOI: Controllable Video Generation of Human-Object Interactions from Sparse Trajectories via Motion Densification
**arXiv**：[2512.09646v1](https://arxiv.org/abs/2512.09646) · [PDF](https://arxiv.org/pdf/2512.09646.pdf)  
**作者**：Wanyue Zhang, Lin Geng Foo, Thabo Beeler, Rishabh Dabral, Christian Theobalt  

**一句话要点**：提出VHOI框架，通过运动稠密化从稀疏轨迹生成可控的人-物交互视频

**关键词**：可控视频生成, 人-物交互, 运动稠密化, 视频扩散模型, 稀疏轨迹

## 3 点简述
- 核心问题：现有可控视频生成方法在稀疏控制（易指定但缺乏实例感知）与稠密信号（信息丰富但获取成本高）间存在权衡。
- 方法要点：采用两阶段框架，先稠密化稀疏轨迹为人-物交互掩码序列，再基于掩码微调视频扩散模型，引入人-物交互感知运动表示。
- 实验或效果：在可控人-物交互视频生成中实现先进结果，并能端到端生成包含导航的完整交互场景。

## 摘要（原文）

> Synthesizing realistic human-object interactions (HOI) in video is challenging due to the complex, instance-specific interaction dynamics of both humans and objects. Incorporating controllability in video generation further adds to the complexity. Existing controllable video generation approaches face a trade-off: sparse controls like keypoint trajectories are easy to specify but lack instance-awareness, while dense signals such as optical flow, depths or 3D meshes are informative but costly to obtain. We propose VHOI, a two-stage framework that first densifies sparse trajectories into HOI mask sequences, and then fine-tunes a video diffusion model conditioned on these dense masks. We introduce a novel HOI-aware motion representation that uses color encodings to distinguish not only human and object motion, but also body-part-specific dynamics. This design incorporates a human prior into the conditioning signal and strengthens the model's ability to understand and generate realistic HOI dynamics. Experiments demonstrate state-of-the-art results in controllable HOI video generation. VHOI is not limited to interaction-only scenarios and can also generate full human navigation leading up to object interactions in an end-to-end manner. Project page: https://vcai.mpi-inf.mpg.de/projects/vhoi/.

