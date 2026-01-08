---
layout: default
title: MGPC: Multimodal Network for Generalizable Point Cloud Completion With Modality Dropout and Progressive Decoding
---

# MGPC: Multimodal Network for Generalizable Point Cloud Completion With Modality Dropout and Progressive Decoding
**arXiv**：[2601.03660v1](https://arxiv.org/abs/2601.03660) · [PDF](https://arxiv.org/pdf/2601.03660.pdf)  
**作者**：Jiangyuan Liu, Hongxuan Ma, Yuhao Zhao, Zhe Liu, Jian Wang, Wei Zou  

**一句话要点**：提出MGPC多模态网络，通过模态丢弃和渐进解码实现可泛化的点云补全

**关键词**：点云补全, 多模态学习, 模态丢弃, 渐进解码, Transformer融合, 大规模基准

## 3 点简述
- 点云补全在真实场景泛化困难，现有方法受限于模态、可扩展性和生成能力
- MGPC整合点云、RGB图像和文本，采用模态丢弃策略、Transformer融合模块和渐进生成器
- 构建MGPC-1M大规模基准，实验显示在真实世界数据上优于基线并具强泛化性

## 摘要（原文）

> Point cloud completion aims to recover complete 3D geometry from partial observations caused by limited viewpoints and occlusions. Existing learning-based works, including 3D Convolutional Neural Network (CNN)-based, point-based, and Transformer-based methods, have achieved strong performance on synthetic benchmarks. However, due to the limitations of modality, scalability, and generative capacity, their generalization to novel objects and real-world scenarios remains challenging. In this paper, we propose MGPC, a generalizable multimodal point cloud completion framework that integrates point clouds, RGB images, and text within a unified architecture. MGPC introduces an innovative modality dropout strategy, a Transformer-based fusion module, and a novel progressive generator to improve robustness, scalability, and geometric modeling capability. We further develop an automatic data generation pipeline and construct MGPC-1M, a large-scale benchmark with over 1,000 categories and one million training pairs. Extensive experiments on MGPC-1M and in-the-wild data demonstrate that the proposed method consistently outperforms prior baselines and exhibits strong generalization under real-world conditions.

