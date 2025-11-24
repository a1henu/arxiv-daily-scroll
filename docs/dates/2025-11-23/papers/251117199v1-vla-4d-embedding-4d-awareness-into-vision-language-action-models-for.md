---
layout: default
title: VLA-4D: Embedding 4D Awareness into Vision-Language-Action Models for SpatioTemporally Coherent Robotic Manipulation
---

# VLA-4D: Embedding 4D Awareness into Vision-Language-Action Models for SpatioTemporally Coherent Robotic Manipulation
**arXiv**：[2511.17199v1](https://arxiv.org/abs/2511.17199) · [PDF](https://arxiv.org/pdf/2511.17199.pdf)  
**作者**：Hanyu Zhou, Chuanhao Ma, Gim Hee Lee  

**一句话要点**：提出VLA-4D模型，通过4D感知实现机器人操作的时空一致性

**关键词**：视觉-语言-动作模型, 4D感知, 时空一致性, 机器人操作, 多模态融合

## 3 点简述
- 现有VLA模型在时空一致性操作中表现不佳，难以实现时间连贯控制
- 方法包括4D感知视觉表示和时空动作表示，融合时间与空间信息
- 实验验证模型在多种机器人操作任务中优于现有方法

## 摘要（原文）

> Vision-language-action (VLA) models show potential for general robotic tasks, but remain challenging in spatiotemporally coherent manipulation, which requires fine-grained representations. Typically, existing methods embed 3D positions into visual representations to enhance the spatial precision of actions. However, these methods struggle to achieve temporally coherent control over action execution. In this work, we propose VLA-4D, a general VLA model with 4D awareness for spatiotemporally coherent robotic manipulation. Our model is guided by two key designs: 1) 4D-aware visual representation. We extract visual features, embed 1D time into 3D positions for 4D embeddings, and fuse them into a unified visual representation via a cross-attention mechanism. 2) Spatiotemporal action representation. We extend conventional spatial action representations with temporal information to enable the spatiotemporal planning, and align the multimodal representations into the LLM for spatiotemporal action prediction. Within this unified framework, the designed visual and action representations jointly make robotic manipulation spatially-smooth and temporally-coherent. In addition, we extend the VLA dataset with temporal action annotations for fine-tuning our model. Extensive experiments have been conducted to verify the superiority of our method across different tasks of robotic manipulation.

