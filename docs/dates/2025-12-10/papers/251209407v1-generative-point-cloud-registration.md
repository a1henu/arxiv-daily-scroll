---
layout: default
title: Generative Point Cloud Registration
---

# Generative Point Cloud Registration
**arXiv**：[2512.09407v1](https://arxiv.org/abs/2512.09407) · [PDF](https://arxiv.org/pdf/2512.09407.pdf)  
**作者**：Haobo Jiang, Jin Xie, Jian Yang, Liang Yu, Jianmin Zheng  

**一句话要点**：提出生成式点云配准范式，通过生成跨视图一致图像对增强3D配准性能。

**关键词**：点云配准, 生成模型, 几何一致性, 纹理一致性, ControlNet, 3D匹配

## 3 点简述
- 核心问题：传统3D配准方法可能受限于几何特征，缺乏纹理信息融合。
- 方法要点：引入Match-ControlNet，利用ControlNet生成几何对齐图像，并通过耦合条件去噪和提示引导确保纹理一致性。
- 实验或效果：在3DMatch和ScanNet数据集上验证有效性，可集成到多种配准方法提升性能。

## 摘要（原文）

> In this paper, we propose a novel 3D registration paradigm, Generative Point Cloud Registration, which bridges advanced 2D generative models with 3D matching tasks to enhance registration performance. Our key idea is to generate cross-view consistent image pairs that are well-aligned with the source and target point clouds, enabling geometry-color feature fusion to facilitate robust matching. To ensure high-quality matching, the generated image pair should feature both 2D-3D geometric consistency and cross-view texture consistency. To achieve this, we introduce Match-ControlNet, a matching-specific, controllable 2D generative model. Specifically, it leverages the depth-conditioned generation capability of ControlNet to produce images that are geometrically aligned with depth maps derived from point clouds, ensuring 2D-3D geometric consistency. Additionally, by incorporating a coupled conditional denoising scheme and coupled prompt guidance, Match-ControlNet further promotes cross-view feature interaction, guiding texture consistency generation. Our generative 3D registration paradigm is general and could be seamlessly integrated into various registration methods to enhance their performance. Extensive experiments on 3DMatch and ScanNet datasets verify the effectiveness of our approach.

