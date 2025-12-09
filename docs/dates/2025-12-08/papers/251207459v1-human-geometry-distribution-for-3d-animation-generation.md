---
layout: default
title: Human Geometry Distribution for 3D Animation Generation
---

# Human Geometry Distribution for 3D Animation Generation
**arXiv**：[2512.07459v1](https://arxiv.org/abs/2512.07459) · [PDF](https://arxiv.org/pdf/2512.07459.pdf)  
**作者**：Xiangjun Tang, Biao Zhang, Peter Wonka  

**一句话要点**：提出基于分布表示和生成动画模型的两阶段框架，以解决有限数据下人体几何动画生成中服装动态建模的挑战。

**关键词**：人体几何动画, 分布表示, 生成模型, 服装动态建模, 潜在空间学习, 身份条件生成

## 3 点简述
- 核心问题：在有限数据下生成具有自然服装动态和精细几何细节的人体几何动画。
- 方法要点：采用两阶段框架，第一阶段学习紧凑分布表示，第二阶段基于身份条件生成动画。
- 实验或效果：在潜在空间和动画模型上均取得最佳结果，如Chamfer距离降低90%，用户研究得分提高2.2倍。

## 摘要（原文）

> Generating realistic human geometry animations remains a challenging task, as it requires modeling natural clothing dynamics with fine-grained geometric details under limited data. To address these challenges, we propose two novel designs. First, we propose a compact distribution-based latent representation that enables efficient and high-quality geometry generation. We improve upon previous work by establishing a more uniform mapping between SMPL and avatar geometries. Second, we introduce a generative animation model that fully exploits the diversity of limited motion data. We focus on short-term transitions while maintaining long-term consistency through an identity-conditioned design. These two designs formulate our method as a two-stage framework: the first stage learns a latent space, while the second learns to generate animations within this latent space. We conducted experiments on both our latent space and animation model. We demonstrate that our latent space produces high-fidelity human geometry surpassing previous methods ($90\%$ lower Chamfer Dist.). The animation model synthesizes diverse animations with detailed and natural dynamics ($2.2 \times$ higher user study score), achieving the best results across all evaluation metrics.

