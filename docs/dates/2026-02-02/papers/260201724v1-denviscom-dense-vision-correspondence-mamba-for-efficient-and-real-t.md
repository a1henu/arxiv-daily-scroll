---
layout: default
title: DenVisCoM: Dense Vision Correspondence Mamba for Efficient and Real-time Optical Flow and Stereo Estimation
---

# DenVisCoM: Dense Vision Correspondence Mamba for Efficient and Real-time Optical Flow and Stereo Estimation
**arXiv**：[2602.01724v1](https://arxiv.org/abs/2602.01724) · [PDF](https://arxiv.org/pdf/2602.01724.pdf)  
**作者**：Tushar Anand, Maheswar Bora, Antitza Dantcheva, Abhijit Das  

**一句话要点**：提出DenVisCoM混合架构，以高效实时联合估计光流与视差

**关键词**：光流估计, 视差估计, Mamba架构, Transformer注意力, 实时处理, 多视图几何

## 3 点简述
- 核心问题：光流与视差估计需兼顾实时性与准确性，传统方法难以平衡。
- 方法要点：结合Mamba块与Transformer注意力块，设计统一架构处理多视图几何与运动任务。
- 实验或效果：在多个数据集上验证，模型能实时准确估计光流与视差，代码已开源。

## 摘要（原文）

> In this work, we propose a novel Mamba block DenVisCoM, as well as a novel hybrid architecture specifically tailored for accurate and real-time estimation of optical flow and disparity estimation. Given that such multi-view geometry and motion tasks are fundamentally related, we propose a unified architecture to tackle them jointly. Specifically, the proposed hybrid architecture is based on DenVisCoM and a Transformer-based attention block that efficiently addresses real-time inference, memory footprint, and accuracy at the same time for joint estimation of motion and 3D dense perception tasks. We extensively analyze the benchmark trade-off of accuracy and real-time processing on a large number of datasets. Our experimental results and related analysis suggest that our proposed model can accurately estimate optical flow and disparity estimation in real time. All models and associated code are available at https://github.com/vimstereo/DenVisCoM.

