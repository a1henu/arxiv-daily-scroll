---
layout: default
title: Enhancing Indoor Occupancy Prediction via Sparse Query-Based Multi-Level Consistent Knowledge Distillation
---

# Enhancing Indoor Occupancy Prediction via Sparse Query-Based Multi-Level Consistent Knowledge Distillation
**arXiv**：[2602.02318v1](https://arxiv.org/abs/2602.02318) · [PDF](https://arxiv.org/pdf/2602.02318.pdf)  
**作者**：Xiang Li, Yupeng Zheng, Pengfei Li, Yilun Chen, Ya-Qin Zhang, Wenchao Ding  

**一句话要点**：提出DiScene框架，通过多级一致知识蒸馏增强稀疏查询的室内占用预测效率与鲁棒性

**关键词**：室内占用预测, 稀疏查询, 知识蒸馏, 多级对齐, 效率优化, 鲁棒性增强

## 3 点简述
- 核心问题：室内占用预测面临效率-精度权衡，稀疏方法在复杂场景中鲁棒性不足
- 方法要点：采用多级一致知识蒸馏，包括编码器、查询、先验和锚点四级对齐，以及教师引导初始化
- 实验或效果：在Occ-Scannet基准上，DiScene超越基线方法OPUS 36.1%，集成深度后达到新SOTA，推理速度提升1.62倍

## 摘要（原文）

> Occupancy prediction provides critical geometric and semantic understanding for robotics but faces efficiency-accuracy trade-offs. Current dense methods suffer computational waste on empty voxels, while sparse query-based approaches lack robustness in diverse and complex indoor scenes. In this paper, we propose DiScene, a novel sparse query-based framework that leverages multi-level distillation to achieve efficient and robust occupancy prediction. In particular, our method incorporates two key innovations: (1) a Multi-level Consistent Knowledge Distillation strategy, which transfers hierarchical representations from large teacher models to lightweight students through coordinated alignment across four levels, including encoder-level feature alignment, query-level feature matching, prior-level spatial guidance, and anchor-level high-confidence knowledge transfer and (2) a Teacher-Guided Initialization policy, employing optimized parameter warm-up to accelerate model convergence. Validated on the Occ-Scannet benchmark, DiScene achieves 23.2 FPS without depth priors while outperforming our baseline method, OPUS, by 36.1% and even better than the depth-enhanced version, OPUS†. With depth integration, DiScene† attains new SOTA performance, surpassing EmbodiedOcc by 3.7% with 1.62$\times$ faster inference speed. Furthermore, experiments on the Occ3D-nuScenes benchmark and in-the-wild scenarios demonstrate the versatility of our approach in various environments. Code and models can be accessed at https://github.com/getterupper/DiScene.

