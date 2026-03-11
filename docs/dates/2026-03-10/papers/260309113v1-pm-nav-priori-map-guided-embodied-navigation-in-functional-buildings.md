---
layout: default
title: PM-Nav: Priori-Map Guided Embodied Navigation in Functional Buildings
---

# PM-Nav: Priori-Map Guided Embodied Navigation in Functional Buildings
**arXiv**：[2603.09113v1](https://arxiv.org/abs/2603.09113) · [PDF](https://arxiv.org/pdf/2603.09113.pdf)  
**作者**：Jiang Gao, Xiangyu Dong, Haozhou Li, Haoran Zhao, Yaoming Zhou, Xiaoguang Ma  

**一句话要点**：提出PM-Nav，利用先验地图解决功能建筑中语言驱动导航的相似特征挑战。

**关键词**：具身导航, 先验地图, 功能建筑, 语义地图, 路径规划, 多模型协作

## 3 点简述
- 核心问题：功能建筑特征高度相似，现有语言驱动导航缺乏有效利用先验空间知识的能力。
- 方法要点：将环境地图转换为语义先验地图，设计分层思维链提示模板，构建多模型协作动作输出机制。
- 实验或效果：在自制数据集上，仿真和真实世界性能显著超越SG-Nav和InstructNav，提升幅度达数百百分比。

## 摘要（原文）

> Existing language-driven embodied navigation paradigms face challenges in functional buildings (FBs) with highly similar features, as they lack the ability to effectively utilize priori spatial knowledge. To tackle this issue, we propose a Priori-Map Guided Embodied Navigation (PM-Nav), wherein environmental maps are transformed into navigation-friendly semantic priori-maps, a hierarchical chain-of-thought prompt template with an annotation priori-map is designed to enable precise path planning, and a multi-model collaborative action output mechanism is built to accomplish positioning decisions and execution control for navigation planning. Comprehensive tests using a home-made FB dataset show that the PM-Nav obtains average improvements of 511\% and 1175\%, and 650\% and 400\% over the SG-Nav and the InstructNav in simulation and real-world, respectively. These tremendous boosts elucidate the great potential of using the PM-Nav as a backbone navigation framework for FBs.

