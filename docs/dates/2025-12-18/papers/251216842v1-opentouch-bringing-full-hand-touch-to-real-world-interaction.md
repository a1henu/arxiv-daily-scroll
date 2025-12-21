---
layout: default
title: OPENTOUCH: Bringing Full-Hand Touch to Real-World Interaction
---

# OPENTOUCH: Bringing Full-Hand Touch to Real-World Interaction
**arXiv**：[2512.16842v1](https://arxiv.org/abs/2512.16842) · [PDF](https://arxiv.org/pdf/2512.16842.pdf)  
**作者**：Yuxin Ray Song, Jinzhou Li, Rao Fu, Devin Murphy, Kaichen Zhou, Rishi Shiv, Yaqi Li, Haoyu Xiong, Crystal Elaine Owens, Yilun Du, Yiyue Luo, Xianyi Cheng, Antonio Torralba, Wojciech Matusik, Paul Pu Liang  

**一句话要点**：提出OpenTouch数据集以解决野外第一人称全手触觉感知缺失问题

**关键词**：第一人称视觉, 触觉感知, 多模态数据集, 野外交互, 抓握理解, 跨模态对齐

## 3 点简述
- 核心问题：缺乏野外环境下同步视频与全手触觉数据，限制视觉感知与物理交互的融合。
- 方法要点：构建首个野外第一人称全手触觉数据集，包含同步视频-触觉-姿态数据和详细文本标注。
- 实验或效果：通过检索和分类基准验证触觉信号对抓握理解、跨模态对齐的有效性，并展示从视频查询中可靠检索触觉。

## 摘要（原文）

> The human hand is our primary interface to the physical world, yet egocentric perception rarely knows when, where, or how forcefully it makes contact. Robust wearable tactile sensors are scarce, and no existing in-the-wild datasets align first-person video with full-hand touch. To bridge the gap between visual perception and physical interaction, we present OpenTouch, the first in-the-wild egocentric full-hand tactile dataset, containing 5.1 hours of synchronized video-touch-pose data and 2,900 curated clips with detailed text annotations. Using OpenTouch, we introduce retrieval and classification benchmarks that probe how touch grounds perception and action. We show that tactile signals provide a compact yet powerful cue for grasp understanding, strengthen cross-modal alignment, and can be reliably retrieved from in-the-wild video queries. By releasing this annotated vision-touch-pose dataset and benchmark, we aim to advance multimodal egocentric perception, embodied learning, and contact-rich robotic manipulation.

