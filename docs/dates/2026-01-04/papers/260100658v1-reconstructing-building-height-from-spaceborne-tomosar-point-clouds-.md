---
layout: default
title: Reconstructing Building Height from Spaceborne TomoSAR Point Clouds Using a Dual-Topology Network
---

# Reconstructing Building Height from Spaceborne TomoSAR Point Clouds Using a Dual-Topology Network
**arXiv**：[2601.00658v1](https://arxiv.org/abs/2601.00658) · [PDF](https://arxiv.org/pdf/2601.00658.pdf)  
**作者**：Zhaiyu Chen, Yuanyuan Wang, Yilei Shi, Xiao Xiang Zhu  

**一句话要点**：提出双拓扑网络从星载TomoSAR点云重建建筑高度，解决噪声和缺失问题。

**关键词**：星载SAR层析成像, 建筑高度重建, 双拓扑网络, 点云处理, 深度学习框架, 城市遥感

## 3 点简述
- 核心问题：星载TomoSAR点云存在噪声、各向异性分布和表面不连贯导致的数据空洞，阻碍准确高度重建。
- 方法要点：设计双拓扑网络，交替处理点分支和网格分支，联合建模不规则散射特征并增强空间一致性，实现去噪和补全。
- 实验或效果：在慕尼黑和柏林数据上验证有效性，可扩展结合光学卫星影像提升重建质量，首次实现大规模城市高度映射概念验证。

## 摘要（原文）

> Reliable building height estimation is essential for various urban applications. Spaceborne SAR tomography (TomoSAR) provides weather-independent, side-looking observations that capture facade-level structure, offering a promising alternative to conventional optical methods. However, TomoSAR point clouds often suffer from noise, anisotropic point distributions, and data voids on incoherent surfaces, all of which hinder accurate height reconstruction. To address these challenges, we introduce a learning-based framework for converting raw TomoSAR points into high-resolution building height maps. Our dual-topology network alternates between a point branch that models irregular scatterer features and a grid branch that enforces spatial consistency. By jointly processing these representations, the network denoises the input points and inpaints missing regions to produce continuous height estimates. To our knowledge, this is the first proof of concept for large-scale urban height mapping directly from TomoSAR point clouds. Extensive experiments on data from Munich and Berlin validate the effectiveness of our approach. Moreover, we demonstrate that our framework can be extended to incorporate optical satellite imagery, further enhancing reconstruction quality. The source code is available at https://github.com/zhu-xlab/tomosar2height.

