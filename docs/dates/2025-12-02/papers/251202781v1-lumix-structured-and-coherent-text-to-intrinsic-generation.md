---
layout: default
title: LumiX: Structured and Coherent Text-to-Intrinsic Generation
---

# LumiX: Structured and Coherent Text-to-Intrinsic Generation
**arXiv**：[2512.02781v1](https://arxiv.org/abs/2512.02781) · [PDF](https://arxiv.org/pdf/2512.02781.pdf)  
**作者**：Xu Han, Biao Zhang, Xiangjun Tang, Xianzhi Li, Peter Wonka  

**一句话要点**：提出LumiX结构化扩散框架，用于文本到内在属性的连贯生成，确保物理一致性。

**关键词**：文本到内在属性生成, 结构化扩散框架, 查询广播注意力, 张量LoRA, 物理一致性, 联合训练

## 3 点简述
- 核心问题：文本到内在属性生成中缺乏结构一致性和物理合理性。
- 方法要点：采用查询广播注意力和张量LoRA，实现跨地图关系建模和稳定联合训练。
- 实验或效果：在内在属性生成上，比现有方法对齐度提高23%，偏好得分更优，并支持图像条件分解。

## 摘要（原文）

> We present LumiX, a structured diffusion framework for coherent text-to-intrinsic generation. Conditioned on text prompts, LumiX jointly generates a comprehensive set of intrinsic maps (e.g., albedo, irradiance, normal, depth, and final color), providing a structured and physically consistent description of an underlying scene. This is enabled by two key contributions: 1) Query-Broadcast Attention, a mechanism that ensures structural consistency by sharing queries across all maps in each self-attention block. 2) Tensor LoRA, a tensor-based adaptation that parameter-efficiently models cross-map relations for efficient joint training. Together, these designs enable stable joint diffusion training and unified generation of multiple intrinsic properties. Experiments show that LumiX produces coherent and physically meaningful results, achieving 23% higher alignment and a better preference score (0.19 vs. -0.41) compared to the state of the art, and it can also perform image-conditioned intrinsic decomposition within the same framework.

