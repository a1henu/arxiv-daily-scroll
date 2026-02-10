---
layout: default
title: Trajectory Stitching for Solving Inverse Problems with Flow-Based Models
---

# Trajectory Stitching for Solving Inverse Problems with Flow-Based Models
**arXiv**：[2602.08538v1](https://arxiv.org/abs/2602.08538) · [PDF](https://arxiv.org/pdf/2602.08538.pdf)  
**作者**：Alexander Denker, Moshe Eliasof, Zeljko Kereta, Carola-Bibiane Schönlieb  

**一句话要点**：提出MS-Flow以解决基于流的生成模型在逆问题中的内存和稳定性问题

**关键词**：流基生成模型, 逆问题求解, 轨迹拼接, 内存优化, 图像重建, 计算机断层扫描

## 3 点简述
- 基于流的生成模型作为先验解决逆问题时，直接优化初始潜在码导致高内存消耗和数值不稳定
- MS-Flow将轨迹表示为中间潜在状态序列，通过局部流动力学和轨迹匹配惩罚耦合段，交替更新状态并强制与观测数据一致
- 在图像恢复和逆问题（如修复、超分辨率和计算机断层扫描）上，MS-Flow相比现有方法减少了内存消耗并提高了重建质量

## 摘要（原文）

> Flow-based generative models have emerged as powerful priors for solving inverse problems. One option is to directly optimize the initial latent code (noise), such that the flow output solves the inverse problem. However, this requires backpropagating through the entire generative trajectory, incurring high memory costs and numerical instability. We propose MS-Flow, which represents the trajectory as a sequence of intermediate latent states rather than a single initial code. By enforcing the flow dynamics locally and coupling segments through trajectory-matching penalties, MS-Flow alternates between updating intermediate latent states and enforcing consistency with observed data. This reduces memory consumption while improving reconstruction quality. We demonstrate the effectiveness of MS-Flow over existing methods on image recovery and inverse problems, including inpainting, super-resolution, and computed tomography.

