---
layout: default
title: VesselFusion: Diffusion Models for Vessel Centerline Extraction from 3D CT Images
---

# VesselFusion: Diffusion Models for Vessel Centerline Extraction from 3D CT Images
**arXiv**：[2603.08135v1](https://arxiv.org/abs/2603.08135) · [PDF](https://arxiv.org/pdf/2603.08135.pdf)  
**作者**：Soichi Mita, Shumpei Takezaki, Ryoma Bise  

**一句话要点**：提出VesselFusion扩散模型以解决3D CT图像中血管中心线提取问题

**关键词**：血管中心线提取, 扩散模型, 3D CT图像, 粗到细表示, 投票聚合

## 3 点简述
- 核心问题：传统确定性模型难以捕捉复杂人体结构，导致血管中心线提取不自然。
- 方法要点：采用扩散模型，结合粗到细中心线表示和基于投票的聚合策略。
- 实验或效果：在公开CT数据集上评估，提取精度更高，结果更自然。

## 摘要（原文）

> Vessel centerline extraction from 3D CT images is an important task because it reduces annotation effort to build a model that estimates a vessel structure. It is challenging to estimate natural vessel structures since conventional approaches are deterministic models, which cannot capture a complex human structure. In this study, we propose VesselFusion, which is a diffusion model to extract the vessel centerline from 3D CT image. The proposed method uses a coarse-to-fine representation of the centerline and a voting-based aggregation for a natural and stable extraction. VesselFusion was evaluated on a publicly available CT image dataset and achieved higher extraction accuracy and a more natural result than conventional approaches.

