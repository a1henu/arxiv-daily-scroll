---
layout: default
title: 3D Foundation Model-Based Loop Closing for Decentralized Collaborative SLAM
---

# 3D Foundation Model-Based Loop Closing for Decentralized Collaborative SLAM
**arXiv**：[2602.02430v1](https://arxiv.org/abs/2602.02430) · [PDF](https://arxiv.org/pdf/2602.02430.pdf)  
**作者**：Pierre-Yves Lajoie, Benjamin Ramtoula, Daniele De Martini, Giovanni Beltrame  

**一句话要点**：提出基于3D基础模型的闭环检测方法，以解决去中心化协同SLAM中视角差异导致的图重叠识别难题。

**关键词**：协同SLAM, 3D基础模型, 闭环检测, 去中心化系统, 位姿图优化

## 3 点简述
- 核心问题：去中心化协同SLAM中，机器人间视角差异大，难以识别地图重叠。
- 方法要点：利用3D基础模型从单目图像对估计相对位姿，集成到现有SLAM流程中。
- 实验或效果：相比现有方法，提升了定位与建图精度，并显著提高计算与内存效率。

## 摘要（原文）

> Decentralized Collaborative Simultaneous Localization And Mapping (C-SLAM) techniques often struggle to identify map overlaps due to significant viewpoint variations among robots. Motivated by recent advancements in 3D foundation models, which can register images despite large viewpoint differences, we propose a robust loop closing approach that leverages these models to establish inter-robot measurements. In contrast to resource-intensive methods requiring full 3D reconstruction within a centralized map, our approach integrates foundation models into existing SLAM pipelines, yielding scalable and robust multi-robot mapping. Our contributions include: (1) integrating 3D foundation models to reliably estimate relative poses from monocular image pairs within decentralized C-SLAM; (2) introducing robust outlier mitigation techniques critical to the use of these relative poses; and (3) developing specialized pose graph optimization formulations that efficiently resolve scale ambiguities. We evaluate our method against state-of-the-art approaches, demonstrating improvements in localization and mapping accuracy, alongside significant gains in computational and memory efficiency. These results highlight the potential of our approach for deployment in large-scale multi-robot scenarios.

