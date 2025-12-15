---
layout: default
title: SATMapTR: Satellite Image Enhanced Online HD Map Construction
---

# SATMapTR: Satellite Image Enhanced Online HD Map Construction
**arXiv**：[2512.11319v1](https://arxiv.org/abs/2512.11319) · [PDF](https://arxiv.org/pdf/2512.11319.pdf)  
**作者**：Bingyuan Huang, Guanyi Zhao, Qian Xu, Yang Lou, Yung-Hui Li, Jianping Wang  

**一句话要点**：提出SATMapTR模型，通过融合卫星图像增强在线高精地图构建，以解决车载传感器数据质量低的问题。

**关键词**：高精地图构建, 卫星图像融合, 在线地图生成, 自动驾驶感知, 特征融合, BEV视角

## 3 点简述
- 核心问题：车载传感器数据因遮挡和能力限制导致高精地图构建不完整、噪声大，影响自动驾驶。
- 方法要点：引入门控特征细化模块和几何感知融合模块，自适应过滤卫星图像特征并高效融合BEV特征。
- 实验或效果：在nuScenes数据集上达到73.8 mAP，优于现有卫星增强模型，并在恶劣条件下表现更稳健。

## 摘要（原文）

> High-definition (HD) maps are evolving from pre-annotated to real-time construction to better support autonomous driving in diverse scenarios. However, this process is hindered by low-quality input data caused by onboard sensors limited capability and frequent occlusions, leading to incomplete, noisy, or missing data, and thus reduced mapping accuracy and robustness. Recent efforts have introduced satellite images as auxiliary input, offering a stable, wide-area view to complement the limited ego perspective. However, satellite images in Bird's Eye View are often degraded by shadows and occlusions from vegetation and buildings. Prior methods using basic feature extraction and fusion remain ineffective. To address these challenges, we propose SATMapTR, a novel online map construction model that effectively fuses satellite image through two key components: (1) a gated feature refinement module that adaptively filters satellite image features by integrating high-level semantics with low-level structural cues to extract high signal-to-noise ratio map-relevant representations; and (2) a geometry-aware fusion module that consistently fuse satellite and BEV features at a grid-to-grid level, minimizing interference from irrelevant regions and low-quality inputs. Experimental results on the nuScenes dataset show that SATMapTR achieves the highest mean average precision (mAP) of 73.8, outperforming state-of-the-art satellite-enhanced models by up to 14.2 mAP. It also shows lower mAP degradation under adverse weather and sensor failures, and achieves nearly 3 times higher mAP at extended perception ranges.

