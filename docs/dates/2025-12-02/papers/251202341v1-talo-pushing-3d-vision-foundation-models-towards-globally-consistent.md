---
layout: default
title: TALO: Pushing 3D Vision Foundation Models Towards Globally Consistent Online Reconstruction
---

# TALO: Pushing 3D Vision Foundation Models Towards Globally Consistent Online Reconstruction
**arXiv**：[2512.02341v1](https://arxiv.org/abs/2512.02341) · [PDF](https://arxiv.org/pdf/2512.02341.pdf)  
**作者**：Fengyi Zhang, Tianjun Zhang, Kasra Khosoussi, Zheng Zhang, Zi Huang, Yadan Luo  

**一句话要点**：提出TALO框架，基于薄板样条实现高自由度长期对齐，以解决在线3D重建中的时空不一致问题。

**关键词**：在线3D重建, 时空一致性, 薄板样条对齐, 点无关配准, 多相机兼容, 鲁棒几何预测

## 3 点简述
- 核心问题：在线场景下，3D视觉基础模型预测存在时空不一致性，现有方法在假设有效性、局部对齐范围和噪声鲁棒性方面受限。
- 方法要点：采用薄板样条进行高自由度长期对齐，通过全局传播控制点校正空间变化不一致，并设计点无关子图配准以增强噪声鲁棒性。
- 实验或效果：在多个数据集、骨干模型和相机设置下，TALO一致产生更连贯的几何和更低的轨迹误差，验证了其鲁棒性和通用性。

## 摘要（原文）

> 3D vision foundation models have shown strong generalization in reconstructing key 3D attributes from uncalibrated images through a single feed-forward pass. However, when deployed in online settings such as driving scenarios, predictions are made over temporal windows, making it non-trivial to maintain consistency across time. Recent strategies align consecutive predictions by solving global transformation, yet our analysis reveals their fundamental limitations in assumption validity, local alignment scope, and robustness under noisy geometry. In this work, we propose a higher-DOF and long-term alignment framework based on Thin Plate Spline, leveraging globally propagated control points to correct spatially varying inconsistencies. In addition, we adopt a point-agnostic submap registration design that is inherently robust to noisy geometry predictions. The proposed framework is fully plug-and-play, compatible with diverse 3D foundation models and camera configurations (e.g., monocular or surround-view). Extensive experiments demonstrate that our method consistently yields more coherent geometry and lower trajectory errors across multiple datasets, backbone models, and camera setups, highlighting its robustness and generality. Codes are publicly available at \href{https://github.com/Xian-Bei/TALO}{https://github.com/Xian-Bei/TALO}.

