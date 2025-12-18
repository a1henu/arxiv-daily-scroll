---
layout: default
title: VLA-AN: An Efficient and Onboard Vision-Language-Action Framework for Aerial Navigation in Complex Environments
---

# VLA-AN: An Efficient and Onboard Vision-Language-Action Framework for Aerial Navigation in Complex Environments
**arXiv**：[2512.15258v1](https://arxiv.org/abs/2512.15258) · [PDF](https://arxiv.org/pdf/2512.15258.pdf)  
**作者**：Yuze Wu, Mo Zhu, Xingxing Li, Yuheng Du, Yuxin Fan, Wenjun Li, Xin Zhou, Fei Gao  

**一句话要点**：提出VLA-AN框架，以解决复杂环境中无人机自主导航的四大限制问题。

**关键词**：视觉-语言-动作框架, 无人机导航, 3D高斯溅射, 渐进训练, 机载部署优化, 安全校正

## 3 点简述
- 核心问题：现有大型空中导航模型存在数据域差距、时序推理不足、生成动作策略的安全风险及机载部署限制。
- 方法要点：构建3D高斯溅射数据集，采用三阶段渐进训练，设计轻量实时动作模块与几何安全校正。
- 实验或效果：在资源受限无人机上实现推理吞吐量8.3倍提升，单任务成功率最高达98.1%。

## 摘要（原文）

> This paper proposes VLA-AN, an efficient and onboard Vision-Language-Action (VLA) framework dedicated to autonomous drone navigation in complex environments. VLA-AN addresses four major limitations of existing large aerial navigation models: the data domain gap, insufficient temporal navigation with reasoning, safety issues with generative action policies, and onboard deployment constraints. First, we construct a high-fidelity dataset utilizing 3D Gaussian Splatting (3D-GS) to effectively bridge the domain gap. Second, we introduce a progressive three-stage training framework that sequentially reinforces scene comprehension, core flight skills, and complex navigation capabilities. Third, we design a lightweight, real-time action module coupled with geometric safety correction. This module ensures fast, collision-free, and stable command generation, mitigating the safety risks inherent in stochastic generative policies. Finally, through deep optimization of the onboard deployment pipeline, VLA-AN achieves a robust real-time 8.3x improvement in inference throughput on resource-constrained UAVs. Extensive experiments demonstrate that VLA-AN significantly improves spatial grounding, scene reasoning, and long-horizon navigation, achieving a maximum single-task success rate of 98.1%, and providing an efficient, practical solution for realizing full-chain closed-loop autonomy in lightweight aerial robots.

