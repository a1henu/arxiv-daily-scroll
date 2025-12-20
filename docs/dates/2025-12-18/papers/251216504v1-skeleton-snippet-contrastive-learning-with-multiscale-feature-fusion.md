---
layout: default
title: Skeleton-Snippet Contrastive Learning with Multiscale Feature Fusion for Action Localization
---

# Skeleton-Snippet Contrastive Learning with Multiscale Feature Fusion for Action Localization
**arXiv**：[2512.16504v1](https://arxiv.org/abs/2512.16504) · [PDF](https://arxiv.org/pdf/2512.16504.pdf)  
**作者**：Qiushuo Cheng, Jingjing Liu, Catherine Morgan, Alan Whone, Majid Mirmehdi  

**一句话要点**：提出基于骨架片段的对比学习与多尺度特征融合方法，以提升骨架时序动作定位性能。

**关键词**：骨架动作定位, 对比学习, 自监督预训练, 多尺度特征融合, 时序动作检测

## 3 点简述
- 核心问题：骨架时序动作定位中，现有自监督预训练方法缺乏对时间敏感特征的学习，难以捕捉动作边界处的细微差异。
- 方法要点：设计片段判别前置任务，通过对比学习区分非重叠骨架片段；融合中间特征，使用U形模块增强特征分辨率以支持帧级定位。
- 实验或效果：在BABEL数据集上改进现有对比学习方法，在PKUMMD上实现迁移学习的最新性能。

## 摘要（原文）

> The self-supervised pretraining paradigm has achieved great success in learning 3D action representations for skeleton-based action recognition using contrastive learning. However, learning effective representations for skeleton-based temporal action localization remains challenging and underexplored. Unlike video-level {action} recognition, detecting action boundaries requires temporally sensitive features that capture subtle differences between adjacent frames where labels change. To this end, we formulate a snippet discrimination pretext task for self-supervised pretraining, which densely projects skeleton sequences into non-overlapping segments and promotes features that distinguish them across videos via contrastive learning. Additionally, we build on strong backbones of skeleton-based action recognition models by fusing intermediate features with a U-shaped module to enhance feature resolution for frame-level localization. Our approach consistently improves existing skeleton-based contrastive learning methods for action localization on BABEL across diverse subsets and evaluation protocols. We also achieve state-of-the-art transfer learning performance on PKUMMD with pretraining on NTU RGB+D and BABEL.

