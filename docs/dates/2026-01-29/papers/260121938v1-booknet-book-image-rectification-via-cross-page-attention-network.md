---
layout: default
title: BookNet: Book Image Rectification via Cross-Page Attention Network
---

# BookNet: Book Image Rectification via Cross-Page Attention Network
**arXiv**：[2601.21938v1](https://arxiv.org/abs/2601.21938) · [PDF](https://arxiv.org/pdf/2601.21938.pdf)  
**作者**：Shaokai Liu, Hao Feng, Bozhi Luan, Min Hou, Jiajun Deng, Wengang Zhou  

**一句话要点**：提出BookNet以解决书籍图像因装订导致的左右页不对称扭曲问题

**关键词**：书籍图像矫正, 跨页注意力网络, 双分支架构, 合成数据集, 几何扭曲建模

## 3 点简述
- 核心问题：书籍图像因装订约束产生复杂几何扭曲，左右页呈现不对称曲率模式，现有单页方法无法捕捉相邻页的耦合关系。
- 方法要点：采用双分支架构与跨页注意力机制，端到端估计单页和整页扭曲流，显式建模左右页相互影响。
- 实验或效果：构建Book3D合成数据集和Book100真实基准，实验显示BookNet优于现有方法。

## 摘要（原文）

> Book image rectification presents unique challenges in document image processing due to complex geometric distortions from binding constraints, where left and right pages exhibit distinctly asymmetric curvature patterns. However, existing single-page document image rectification methods fail to capture the coupled geometric relationships between adjacent pages in books. In this work, we introduce BookNet, the first end-to-end deep learning framework specifically designed for dual-page book image rectification. BookNet adopts a dual-branch architecture with cross-page attention mechanisms, enabling it to estimate warping flows for both individual pages and the complete book spread, explicitly modeling how left and right pages influence each other. Moreover, to address the absence of specialized datasets, we present Book3D, a large-scale synthetic dataset for training, and Book100, a comprehensive real-world benchmark for evaluation. Extensive experiments demonstrate that BookNet outperforms existing state-of-the-art methods on book image rectification. Code and dataset will be made publicly available.

