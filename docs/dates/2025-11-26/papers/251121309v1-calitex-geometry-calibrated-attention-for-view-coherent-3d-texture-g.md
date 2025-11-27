---
layout: default
title: CaliTex: Geometry-Calibrated Attention for View-Coherent 3D Texture Generation
---

# CaliTex: Geometry-Calibrated Attention for View-Coherent 3D Texture Generation
**arXiv**：[2511.21309v1](https://arxiv.org/abs/2511.21309) · [PDF](https://arxiv.org/pdf/2511.21309.pdf)  
**作者**：Chenyu Liu, Hongze Chen, Jingzhi Bao, Lingting Zhu, Runze Zhang, Weikai Chen, Zeyu Hu, Yingda Yin, Keyang Luo, Xin Wang  

**一句话要点**：提出CaliTex框架以解决3D纹理生成中的跨视角不一致问题

**关键词**：3D纹理生成, 几何校准注意力, 扩散变换器, 跨视角一致性, 注意力机制

## 3 点简述
- 核心问题：现有3D纹理生成系统存在跨视角不一致，源于注意力模糊导致几何混淆
- 方法要点：引入几何校准注意力模块，包括部分对齐注意力和条件路由注意力
- 实验或效果：CaliTex在实验中优于开源和商业基线，生成无缝且视角一致的纹理

## 摘要（原文）

> Despite major advances brought by diffusion-based models, current 3D texture generation systems remain hindered by cross-view inconsistency -- textures that appear convincing from one viewpoint often fail to align across others. We find that this issue arises from attention ambiguity, where unstructured full attention is applied indiscriminately across tokens and modalities, causing geometric confusion and unstable appearance-structure coupling. To address this, we introduce CaliTex, a framework of geometry-calibrated attention that explicitly aligns attention with 3D structure. It introduces two modules: Part-Aligned Attention that enforces spatial alignment across semantically matched parts, and Condition-Routed Attention which routes appearance information through geometry-conditioned pathways to maintain spatial fidelity. Coupled with a two-stage diffusion transformer, CaliTex makes geometric coherence an inherent behavior of the network rather than a byproduct of optimization. Empirically, CaliTex produces seamless and view-consistent textures and outperforms both open-source and commercial baselines.

