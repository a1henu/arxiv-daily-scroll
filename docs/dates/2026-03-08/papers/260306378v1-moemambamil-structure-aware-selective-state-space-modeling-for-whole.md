---
layout: default
title: MoEMambaMIL: Structure-Aware Selective State Space Modeling for Whole-Slide Image Analysis
---

# MoEMambaMIL: Structure-Aware Selective State Space Modeling for Whole-Slide Image Analysis
**arXiv**：[2603.06378v1](https://arxiv.org/abs/2603.06378) · [PDF](https://arxiv.org/pdf/2603.06378.pdf)  
**作者**：Dongqing Xie, Yonghuang Wu  

**一句话要点**：提出MoEMambaMIL框架，通过结构感知状态空间建模解决全切片图像分析中的空间依赖捕获问题。

**关键词**：全切片图像分析, 状态空间模型, 混合专家, 多实例学习, 结构感知建模

## 3 点简述
- 核心问题：全切片图像分析中，现有方法将图像视为无序补丁集合，难以捕捉全局组织与局部模式的结构化依赖。
- 方法要点：结合区域嵌套选择性扫描与混合专家模型，组织多分辨率补丁序列，实现高效长序列建模和专家专业化。
- 实验或效果：在9个下游任务中取得最佳性能，验证了框架的有效性。

## 摘要（原文）

> Whole-slide image (WSI) analysis is challenging due to the gigapixel scale of slides and their inherent hierarchical multi-resolution structure. Existing multiple instance learning (MIL) approaches often model WSIs as unordered collections of patches, which limits their ability to capture structured dependencies between global tissue organization and local cellular patterns. Although recent State Space Models (SSMs) enable efficient modeling of long sequences, how to structure WSI tokens to fully exploit their spatial hierarchy remains an open problem.We propose MoEMambaMIL, a structure-aware SSM framework for WSI analysis that integrates region-nested selective scanning with mixture-of-experts (MoE) modeling. Leveraging multi-resolution preprocessing, MoEMambaMIL organizes patch tokens into region-aware sequences that preserve spatial containment across resolutions. On top of this structured sequence, we decouple resolution-aware encoding and region-adaptive contextual modeling via a combination of static, resolution-specific experts and dynamic sparse experts with learned routing. This design enables efficient long-sequence modeling while promoting expert specialization across heterogeneous diagnostic patterns. Experiments demonstrate that MoEMambaMIL achieves the best performance across 9 downstream tasks.

