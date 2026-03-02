---
layout: default
title: BiM-GeoAttn-Net: Linear-Time Depth Modeling with Geometry-Aware Attention for 3D Aortic Dissection CTA Segmentation
---

# BiM-GeoAttn-Net: Linear-Time Depth Modeling with Geometry-Aware Attention for 3D Aortic Dissection CTA Segmentation
**arXiv**：[2602.23803v1](https://arxiv.org/abs/2602.23803) · [PDF](https://arxiv.org/pdf/2602.23803.pdf)  
**作者**：Yuan Zhang, Lei Liu, Jialin Zhang, Ya-Nan Zhang, Ling Wang, Nan Mu  

**一句话要点**：提出BiM-GeoAttn-Net，结合线性时间深度建模与几何感知注意力，用于3D主动脉夹层CTA分割。

**关键词**：3D医学图像分割, 主动脉夹层, 状态空间模型, 几何感知注意力, CT血管造影

## 3 点简述
- 核心问题：主动脉夹层CTA分割中，长程上下文建模不足和低对比度下结构区分困难。
- 方法要点：使用双向深度Mamba捕获跨切片依赖，几何感知血管注意力模块优化管状结构。
- 实验或效果：在多源数据集上，Dice分数达93.35%，HD95为12.36毫米，优于基线方法。

## 摘要（原文）

> Accurate segmentation of aortic dissection (AD) lumens in CT angiography (CTA) is essential for quantitative morphological assessment and clinical decision-making. However, reliable 3D delineation remains challenging due to limited long-range context modeling, which compromises inter-slice coherence, and insufficient structural discrimination under low-contrast conditions. To address these limitations, we propose BiM-GeoAttn-Net, a lightweight framework that integrates linear-time depth-wise state-space modeling with geometry-aware vessel refinement. Our approach is featured by Bidirectional Depth Mamba (BiM) to efficiently capture cross-slice dependencies and Geometry-Aware Vessel Attention (GeoAttn) module that employs orientation-sensitive anisotropic filtering to refine tubular structures and sharpen ambiguous boundaries. Extensive experiments on a multi-source AD CTA dataset demonstrate that BiM-GeoAttn-Net achieves a Dice score of 93.35% and an HD95 of 12.36 mm, outperforming representative CNN-, Transformer-, and SSM-based baselines in overlap metrics while maintaining competitive boundary accuracy. These results suggest that coupling linear-time depth modeling with geometry-aware refinement provides an effective, computationally efficient solution for robust 3D AD segmentation.

