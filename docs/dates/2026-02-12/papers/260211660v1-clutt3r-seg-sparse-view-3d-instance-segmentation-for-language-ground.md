---
layout: default
title: Clutt3R-Seg: Sparse-view 3D Instance Segmentation for Language-grounded Grasping in Cluttered Scenes
---

# Clutt3R-Seg: Sparse-view 3D Instance Segmentation for Language-grounded Grasping in Cluttered Scenes
**arXiv**：[2602.11660v1](https://arxiv.org/abs/2602.11660) · [PDF](https://arxiv.org/pdf/2602.11660.pdf)  
**作者**：Jeongho Noh, Tai Hyoung Rhee, Eunho Lee, Jeongyun Kim, Sunwoo Lee, Ayoung Kim  

**一句话要点**：提出Clutt3R-Seg，通过层次实例树实现稀疏视图下的鲁棒3D实例分割，用于杂乱场景中的语言引导抓取。

**关键词**：3D实例分割, 稀疏视图, 语言引导抓取, 杂乱场景, 零样本学习, 机器人操作

## 3 点简述
- 核心问题：杂乱环境中遮挡、有限视角和噪声掩码导致3D实例分割不可靠，影响语言引导的机器人操作。
- 方法要点：利用噪声掩码作为信息线索，通过跨视图分组和条件替换构建层次实例树，抑制过分割和欠分割，生成视图一致的掩码和鲁棒3D实例。
- 实验或效果：在合成和真实数据集上评估，优于现有基线，在重杂乱序列中AP@25达61.66，仅用四个输入视图性能超过八视图基线两倍以上。

## 摘要（原文）

> Reliable 3D instance segmentation is fundamental to language-grounded robotic manipulation. Its critical application lies in cluttered environments, where occlusions, limited viewpoints, and noisy masks degrade perception. To address these challenges, we present Clutt3R-Seg, a zero-shot pipeline for robust 3D instance segmentation for language-grounded grasping in cluttered scenes. Our key idea is to introduce a hierarchical instance tree of semantic cues. Unlike prior approaches that attempt to refine noisy masks, our method leverages them as informative cues: through cross-view grouping and conditional substitution, the tree suppresses over- and under-segmentation, yielding view-consistent masks and robust 3D instances. Each instance is enriched with open-vocabulary semantic embeddings, enabling accurate target selection from natural language instructions. To handle scene changes during multi-stage tasks, we further introduce a consistency-aware update that preserves instance correspondences from only a single post-interaction image, allowing efficient adaptation without rescanning. Clutt3R-Seg is evaluated on both synthetic and real-world datasets, and validated on a real robot. Across all settings, it consistently outperforms state-of-the-art baselines in cluttered and sparse-view scenarios. Even on the most challenging heavy-clutter sequences, Clutt3R-Seg achieves an AP@25 of 61.66, over 2.2x higher than baselines, and with only four input views it surpasses MaskClustering with eight views by more than 2x. The code is available at: https://github.com/jeonghonoh/clutt3r-seg.

