---
layout: default
title: ViSA-Enhanced Aerial VLN: A Visual-Spatial Reasoning Enhanced Framework for Aerial Vision-Language Navigation
---

# ViSA-Enhanced Aerial VLN: A Visual-Spatial Reasoning Enhanced Framework for Aerial Vision-Language Navigation
**arXiv**：[2603.08007v1](https://arxiv.org/abs/2603.08007) · [PDF](https://arxiv.org/pdf/2603.08007.pdf)  
**作者**：Haoyu Tong, Xiangyu Dong, Xiaoguang Ma, Haoran Zhao, Yaoming Zhou, Chenghao Lin  

**一句话要点**：提出视觉-空间推理增强框架以解决空中视觉语言导航中的空间推理不足和语言歧义问题

**关键词**：空中视觉语言导航, 视觉-空间推理, 视觉语言模型, 结构化视觉提示, 三重协作架构, CityNav基准

## 3 点简述
- 现有方法依赖检测-规划流程，导致空间推理能力不足和语言歧义
- 设计三重协作架构，利用结构化视觉提示，使视觉语言模型直接在图像平面上推理
- 在CityNav基准上评估，成功率比全训练SOTA方法提升70.3%

## 摘要（原文）

> Existing aerial Vision-Language Navigation (VLN) methods predominantly adopt a detection-and-planning pipeline, which converts open-vocabulary detections into discrete textual scene graphs. These approaches are plagued by inadequate spatial reasoning capabilities and inherent linguistic ambiguities. To address these bottlenecks, we propose a Visual-Spatial Reasoning (ViSA) enhanced framework for aerial VLN. Specifically, a triple-phase collaborative architecture is designed to leverage structured visual prompting, enabling Vision-Language Models (VLMs) to perform direct reasoning on image planes without the need for additional training or complex intermediate representations. Comprehensive evaluations on the CityNav benchmark demonstrate that the ViSA-enhanced VLN achieves a 70.3\% improvement in success rate compared to the fully trained state-of-the-art (SOTA) method, elucidating its great potential as a backbone for aerial VLN systems.

