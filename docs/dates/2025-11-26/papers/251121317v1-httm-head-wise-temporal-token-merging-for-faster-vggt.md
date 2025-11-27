---
layout: default
title: HTTM: Head-wise Temporal Token Merging for Faster VGGT
---

# HTTM: Head-wise Temporal Token Merging for Faster VGGT
**arXiv**：[2511.21317v1](https://arxiv.org/abs/2511.21317) · [PDF](https://arxiv.org/pdf/2511.21317.pdf)  
**作者**：Weitian Wang, Lukas Meiner, Rai Shubham, Cecilia De La Parra, Akash Kumar  

**一句话要点**：提出头级时序令牌合并以加速视觉几何基础Transformer

**关键词**：3D场景重建, 令牌合并, 多头注意力, 推理加速, 视觉Transformer

## 3 点简述
- VGGT在长序列输入时全局注意力计算导致高延迟
- HTTM在多头粒度合并令牌，保持特征独特性并利用时空局部性
- 实验显示HTTM实现7倍加速且性能下降可忽略

## 摘要（原文）

> The Visual Geometry Grounded Transformer (VGGT) marks a significant leap forward in 3D scene reconstruction, as it is the first model that directly infers all key 3D attributes (camera poses, depths, and dense geometry) jointly in one pass. However, this joint inference mechanism requires global attention layers that perform all-to-all attention computation on tokens from all views. For reconstruction of large scenes with long-sequence inputs, this causes a significant latency bottleneck. In this paper, we propose head-wise temporal merging (HTTM), a training-free 3D token merging method for accelerating VGGT. Existing merging techniques merge tokens uniformly across different attention heads, resulting in identical tokens in the layers' output, which hinders the model's representational ability. HTTM tackles this problem by merging tokens in multi-head granularity, which preserves the uniqueness of feature tokens after head concatenation. Additionally, this enables HTTM to leverage the spatial locality and temporal correspondence observed at the head level to achieve higher merging ratios with lower merging costs compared to existing methods. Thus, HTTM achieves up to 7x acceleration with negligible performance drops in a GPU-based inference.

