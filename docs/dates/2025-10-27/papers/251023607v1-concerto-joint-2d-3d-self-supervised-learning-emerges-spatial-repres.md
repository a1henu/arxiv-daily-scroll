---
layout: default
title: Concerto: Joint 2D-3D Self-Supervised Learning Emerges Spatial Representations
---

# Concerto: Joint 2D-3D Self-Supervised Learning Emerges Spatial Representations
**arXiv**：[2510.23607v1](https://arxiv.org/abs/2510.23607) · [PDF](https://arxiv.org/pdf/2510.23607.pdf)  
**作者**：Yujia Zhang, Xiaoyang Wu, Yixing Lao, Chengyao Wang, Zhuotao Tian, Naiyan Wang, Hengshuang Zhao  

**一句话要点**：提出Concerto联合2D-3D自监督学习，以增强空间认知表示

**关键词**：自监督学习, 2D-3D联合嵌入, 空间表示学习, 多模态学习, 场景理解

## 3 点简述
- 核心问题：如何通过多模态学习模拟人类空间概念形成，提升单模态表示能力
- 方法要点：结合3D模态内自蒸馏与2D-3D跨模态联合嵌入，实现简单高效训练
- 实验或效果：在3D场景感知线性探测中超越SOTA模型，并在多个基准上创下新记录

## 摘要（原文）

> Humans learn abstract concepts through multisensory synergy, and once formed,
> such representations can often be recalled from a single modality. Inspired by
> this principle, we introduce Concerto, a minimalist simulation of human concept
> learning for spatial cognition, combining 3D intra-modal self-distillation with
> 2D-3D cross-modal joint embedding. Despite its simplicity, Concerto learns more
> coherent and informative spatial features, as demonstrated by zero-shot
> visualizations. It outperforms both standalone SOTA 2D and 3D self-supervised
> models by 14.2% and 4.8%, respectively, as well as their feature concatenation,
> in linear probing for 3D scene perception. With full fine-tuning, Concerto sets
> new SOTA results across multiple scene understanding benchmarks (e.g., 80.7%
> mIoU on ScanNet). We further present a variant of Concerto tailored for
> video-lifted point cloud spatial understanding, and a translator that linearly
> projects Concerto representations into CLIP's language space, enabling
> open-world perception. These results highlight that Concerto emerges spatial
> representations with superior fine-grained geometric and semantic consistency.

