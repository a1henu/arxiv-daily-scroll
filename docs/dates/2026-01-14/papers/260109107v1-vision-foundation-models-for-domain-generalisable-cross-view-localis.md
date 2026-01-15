---
layout: default
title: Vision Foundation Models for Domain Generalisable Cross-View Localisation in Planetary Ground-Aerial Robotic Teams
---

# Vision Foundation Models for Domain Generalisable Cross-View Localisation in Planetary Ground-Aerial Robotic Teams
**arXiv**：[2601.09107v1](https://arxiv.org/abs/2601.09107) · [PDF](https://arxiv.org/pdf/2601.09107.pdf)  
**作者**：Lachlan Holden, Feras Dayoub, Alberto Candela, David Harvey, Tat-Jun Chin  

**一句话要点**：提出基于视觉基础模型和合成数据的跨视图定位方法，用于行星地面-空中机器人团队定位。

**关键词**：跨视图定位, 视觉基础模型, 语义分割, 合成数据, 行星机器人, 粒子滤波

## 3 点简述
- 核心问题：行星机器人定位中真实数据稀缺，难以训练机器学习模型。
- 方法要点：利用视觉基础模型进行语义分割，结合大量合成数据弥合领域差距。
- 实验或效果：通过粒子滤波和跨视图网络，基于地面视图图像序列实现准确位置估计。

## 摘要（原文）

> Accurate localisation in planetary robotics enables the advanced autonomy required to support the increased scale and scope of future missions. The successes of the Ingenuity helicopter and multiple planetary orbiters lay the groundwork for future missions that use ground-aerial robotic teams. In this paper, we consider rovers using machine learning to localise themselves in a local aerial map using limited field-of-view monocular ground-view RGB images as input. A key consideration for machine learning methods is that real space data with ground-truth position labels suitable for training is scarce. In this work, we propose a novel method of localising rovers in an aerial map using cross-view-localising dual-encoder deep neural networks. We leverage semantic segmentation with vision foundation models and high volume synthetic data to bridge the domain gap to real images. We also contribute a new cross-view dataset of real-world rover trajectories with corresponding ground-truth localisation data captured in a planetary analogue facility, plus a high volume dataset of analogous synthetic image pairs. Using particle filters for state estimation with the cross-view networks allows accurate position estimation over simple and complex trajectories based on sequences of ground-view images.

