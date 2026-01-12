---
layout: default
title: SceneFoundry: Generating Interactive Infinite 3D Worlds
---

# SceneFoundry: Generating Interactive Infinite 3D Worlds
**arXiv**：[2601.05810v1](https://arxiv.org/abs/2601.05810) · [PDF](https://arxiv.org/pdf/2601.05810.pdf)  
**作者**：ChunTeng Chen, YiChen Hsu, YiWen Liu, WeiFang Sun, TsaiChing Ni, ChunYi Lee, Min Sun, YuanFu Yang  

**一句话要点**：提出SceneFoundry语言引导扩散框架，生成交互式无限3D世界以支持机器人训练。

**关键词**：3D场景生成, 语言引导扩散, 铰接物体, 机器人训练, 物理可用性, 大规模环境生成

## 3 点简述
- 核心问题：现有方法难以生成功能复杂的真实室内环境，特别是包含可移动部件的铰接物体。
- 方法要点：结合LLM控制布局生成和扩散后验采样，从大规模3D库中填充铰接资产，并使用可微分指导确保物理可用性。
- 实验或效果：生成结构有效、语义连贯且功能交互的环境，适用于多样化场景类型和条件。

## 摘要（原文）

> The ability to automatically generate large-scale, interactive, and physically realistic 3D environments is crucial for advancing robotic learning and embodied intelligence. However, existing generative approaches often fail to capture the functional complexity of real-world interiors, particularly those containing articulated objects with movable parts essential for manipulation and navigation. This paper presents SceneFoundry, a language-guided diffusion framework that generates apartment-scale 3D worlds with functionally articulated furniture and semantically diverse layouts for robotic training. From natural language prompts, an LLM module controls floor layout generation, while diffusion-based posterior sampling efficiently populates the scene with articulated assets from large-scale 3D repositories. To ensure physical usability, SceneFoundry employs differentiable guidance functions to regulate object quantity, prevent articulation collisions, and maintain sufficient walkable space for robotic navigation. Extensive experiments demonstrate that our framework generates structurally valid, semantically coherent, and functionally interactive environments across diverse scene types and conditions, enabling scalable embodied AI research.

