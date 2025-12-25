---
layout: default
title: Multimodal Skeleton-Based Action Representation Learning via Decomposition and Composition
---

# Multimodal Skeleton-Based Action Representation Learning via Decomposition and Composition
**arXiv**：[2512.21064v1](https://arxiv.org/abs/2512.21064) · [PDF](https://arxiv.org/pdf/2512.21064.pdf)  
**作者**：Hongsong Wang, Heng Fei, Bingxuan Dai, Jie Gui  

**一句话要点**：提出Decomposition and Composition框架，通过自监督分解与组合多模态骨架特征，平衡动作理解效率与性能。

**关键词**：多模态动作理解, 骨架动作表示, 自监督学习, 特征分解, 特征组合, 计算效率

## 3 点简述
- 核心问题：多模态动作理解中，如何有效利用模态互补性同时保持模型效率，避免简单融合带来的计算开销或性能不足。
- 方法要点：采用自监督学习，先分解融合特征为单模态特征并与其真值对齐，再组合单模态特征作为指导增强多模态表示学习。
- 实验或效果：在NTU RGB+D 60、NTU RGB+D 120和PKU-MMD II数据集上验证，实现计算成本与模型性能的优异平衡。

## 摘要（原文）

> Multimodal human action understanding is a significant problem in computer vision, with the central challenge being the effective utilization of the complementarity among diverse modalities while maintaining model efficiency. However, most existing methods rely on simple late fusion to enhance performance, which results in substantial computational overhead. Although early fusion with a shared backbone for all modalities is efficient, it struggles to achieve excellent performance. To address the dilemma of balancing efficiency and effectiveness, we introduce a self-supervised multimodal skeleton-based action representation learning framework, named Decomposition and Composition. The Decomposition strategy meticulously decomposes the fused multimodal features into distinct unimodal features, subsequently aligning them with their respective ground truth unimodal counterparts. On the other hand, the Composition strategy integrates multiple unimodal features, leveraging them as self-supervised guidance to enhance the learning of multimodal representations. Extensive experiments on the NTU RGB+D 60, NTU RGB+D 120, and PKU-MMD II datasets demonstrate that the proposed method strikes an excellent balance between computational cost and model performance.

