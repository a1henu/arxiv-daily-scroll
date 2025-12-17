---
layout: default
title: ART: Articulated Reconstruction Transformer
---

# ART: Articulated Reconstruction Transformer
**arXiv**：[2512.14671v1](https://arxiv.org/abs/2512.14671) · [PDF](https://arxiv.org/pdf/2512.14671.pdf)  
**作者**：Zizhang Li, Cheng Zhang, Zhengqin Li, Henry Howard-Jenkins, Zhaoyang Lv, Chen Geng, Jiajun Wu, Richard Newcombe, Jakob Engel, Zhao Dong  

**一句话要点**：提出ART以从稀疏多状态RGB图像重建完整3D关节物体

**关键词**：关节物体重建, Transformer架构, 部件预测, 3D重建, 稀疏图像输入

## 3 点简述
- 核心问题：现有方法依赖缓慢优化或局限于特定类别，难以高效通用重建关节物体
- 方法要点：将关节物体视为刚性部件组装，通过Transformer预测部件几何、纹理和关节参数
- 实验或效果：在大规模数据集上训练，评估显示优于基线，建立新SOTA

## 摘要（原文）

> We introduce ART, Articulated Reconstruction Transformer -- a category-agnostic, feed-forward model that reconstructs complete 3D articulated objects from only sparse, multi-state RGB images. Previous methods for articulated object reconstruction either rely on slow optimization with fragile cross-state correspondences or use feed-forward models limited to specific object categories. In contrast, ART treats articulated objects as assemblies of rigid parts, formulating reconstruction as part-based prediction. Our newly designed transformer architecture maps sparse image inputs to a set of learnable part slots, from which ART jointly decodes unified representations for individual parts, including their 3D geometry, texture, and explicit articulation parameters. The resulting reconstructions are physically interpretable and readily exportable for simulation. Trained on a large-scale, diverse dataset with per-part supervision, and evaluated across diverse benchmarks, ART achieves significant improvements over existing baselines and establishes a new state of the art for articulated object reconstruction from image inputs.

