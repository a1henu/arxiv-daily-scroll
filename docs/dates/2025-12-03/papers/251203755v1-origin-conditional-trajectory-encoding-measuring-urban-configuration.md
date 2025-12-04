---
layout: default
title: Origin-Conditional Trajectory Encoding: Measuring Urban Configurational Asymmetries through Neural Decomposition
---

# Origin-Conditional Trajectory Encoding: Measuring Urban Configurational Asymmetries through Neural Decomposition
**arXiv**：[2512.03755v1](https://arxiv.org/abs/2512.03755) · [PDF](https://arxiv.org/pdf/2512.03755.pdf)  
**作者**：Stephen Law, Tao Yang, Nanjiang Chen, Xuhui Lin  

**一句话要点**：提出条件轨迹编码器以解决城市轨迹分析中时空表示分离和方向不对称性问题

**关键词**：轨迹分析, 城市形态学, 条件编码, 认知不对称, 几何特征, 对比学习

## 3 点简述
- 核心问题：现有方法分离时空表示，忽略导航方向不对称性，依赖辅助数据而非几何特征
- 方法要点：使用双向LSTM处理几何特征，通过对比学习分解为共享模式和起点特定签名
- 实验或效果：在合成和真实城市验证，量化认知不对称性，为规划提供工具

## 摘要（原文）

> Urban analytics increasingly relies on AI-driven trajectory analysis, yet current approaches suffer from methodological fragmentation: trajectory learning captures movement patterns but ignores spatial context, while spatial embedding methods encode street networks but miss temporal dynamics. Three gaps persist: (1) lack of joint training that integrates spatial and temporal representations, (2) origin-agnostic treatment that ignores directional asymmetries in navigation ($A \to B \ne B \to A$), and (3) over-reliance on auxiliary data (POIs, imagery) rather than fundamental geometric properties of urban space. We introduce a conditional trajectory encoder that jointly learns spatial and movement representations while preserving origin-dependent asymmetries using geometric features. This framework decomposes urban navigation into shared cognitive patterns and origin-specific spatial narratives, enabling quantitative measurement of cognitive asymmetries across starting locations. Our bidirectional LSTM processes visibility ratio and curvature features conditioned on learnable origin embeddings, decomposing representations into shared urban patterns and origin-specific signatures through contrastive learning. Results from six synthetic cities and real-world validation on Beijing's Xicheng District demonstrate that urban morphology creates systematic cognitive inequalities. This provides urban planners quantitative tools for assessing experiential equity, offers architects insights into layout decisions' cognitive impacts, and enables origin-aware analytics for navigation systems.

