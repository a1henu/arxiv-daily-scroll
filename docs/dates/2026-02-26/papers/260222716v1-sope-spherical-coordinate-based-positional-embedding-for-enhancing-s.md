---
layout: default
title: SoPE: Spherical Coordinate-Based Positional Embedding for Enhancing Spatial Perception of 3D LVLMs
---

# SoPE: Spherical Coordinate-Based Positional Embedding for Enhancing Spatial Perception of 3D LVLMs
**arXiv**：[2602.22716v1](https://arxiv.org/abs/2602.22716) · [PDF](https://arxiv.org/pdf/2602.22716.pdf)  
**作者**：Guanting Ye, Qiyan Zhao, Wenhao Yu, Liangyu Yuan, Mingkai Li, Xiaofeng Zhang, Jianmin Ji, Yanyong Zhang, Qing Jiang, Ka-Veng Yuen  

**一句话要点**：提出SoPE位置嵌入以增强3D大视觉语言模型的空间感知能力

**关键词**：3D大视觉语言模型, 位置嵌入, 球坐标系, 多模态学习, 点云处理

## 3 点简述
- 核心问题：RoPE位置嵌入在3D多模态理解中无法保持空间结构和方向依赖
- 方法要点：将点云令牌映射到球坐标系，统一建模位置和角度，并融合多尺度频率
- 实验或效果：在多个3D场景基准上验证有效性，实际部署展示强泛化能力

## 摘要（原文）

> 3D Large Vision-Language Models (3D LVLMs) built upon Large Language Models (LLMs) have achieved remarkable progress across various multimodal tasks. However, their inherited position-dependent modeling mechanism, Rotary Position Embedding (RoPE), remains suboptimal for 3D multimodal understanding. The vanilla RoPE formulation fails to preserve essential three-dimensional spatial structures when encoding 3D tokens, and its relative distance computation overlooks angular dependencies, hindering the model's ability to capture directional variations in visual representations. To overcome these limitations, we introduce Spherical Coordinate-based Positional Embedding (SoPE). Our method maps point-cloud token indices into a 3D spherical coordinate space, enabling unified modeling of spatial locations and directional angles. This formulation preserves the inherent geometric structure of point-cloud data, enhances spatial awareness, and yields more consistent and expressive geometric representations for multimodal learning. In addition, we introduce a multi-scale frequency mixing strategy to fuse feature information across different frequency domains. Experimental results on multiple 3D scene benchmarks validate the effectiveness of our approach, while real-world deployment experiments further demonstrate its strong generalization capability.

