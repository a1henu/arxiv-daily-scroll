---
layout: default
title: Coarse-to-Fine Monocular Re-Localization in OpenStreetMap via Semantic Alignment
---

# Coarse-to-Fine Monocular Re-Localization in OpenStreetMap via Semantic Alignment
**arXiv**：[2603.01613v1](https://arxiv.org/abs/2603.01613) · [PDF](https://arxiv.org/pdf/2603.01613.pdf)  
**作者**：Yuchen Zou, Xiao Hu, Dexing Zhong, Yuqing Tang  

**一句话要点**：提出基于语义对齐的从粗到细单目重定位框架，以解决OpenStreetMap中的跨模态差异与计算效率问题。

**关键词**：单目重定位, OpenStreetMap, 语义对齐, 从粗到细搜索, DINO-ViT, 跨模态定位

## 3 点简述
- 核心问题：传统方法依赖密集地图，存在可扩展性和隐私风险；OpenStreetMap提供轻量级语义几何信息，但面临跨模态差异和高计算成本挑战。
- 方法要点：利用DINO-ViT的语义感知能力建立图像与OSM的语义关系，设计从粗到细搜索范式替代全局密集匹配，实现高效渐进式精化。
- 实验或效果：实验表明方法显著提升定位精度和速度，在单数据集训练下，3°方向召回率优于现有方法的5°召回率。

## 摘要（原文）

> Monocular re-localization plays a crucial role in enabling intelligent agents to achieve human-like perception. However, traditional methods rely on dense maps, which face scalability limitations and privacy risks. OpenStreetMap (OSM), as a lightweight map that protects privacy, offers semantic and geometric information with global scalability. Nonetheless, there are still challenges in using OSM for localization: the inherent cross-modal discrepancies between natural images and OSM, as well as the high computational cost of global map-based localization. In this paper, we propose a hierarchical search framework with semantic alignment for localization in OSM. First, the semantic awareness capability of DINO-ViT is utilised to deconstruct visual elements to establish semantic relationships with OSM. Second, a coarse-to-fine search paradigm is designed to replace global dense matching, enabling efficient progressive refinement. Extensive experiments demonstrate that our method significantly improves both localization accuracy and speed. When trained on a single dataset, the 3° orientation recall of our method even outperforms the 5° recall of state-of-the-art methods.

