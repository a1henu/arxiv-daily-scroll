---
layout: default
title: Optimal transport unlocks end-to-end learning for single-molecule localization
---

# Optimal transport unlocks end-to-end learning for single-molecule localization
**arXiv**：[2512.10683v1](https://arxiv.org/abs/2512.10683) · [PDF](https://arxiv.org/pdf/2512.10683.pdf)  
**作者**：Romain Seailles, Jean-Baptiste Masson, Jean Ponce, Julien Mairal  

**一句话要点**：提出基于最优传输的损失函数和迭代神经网络，以解决单分子定位显微镜中非最大抑制层不可微和真阳性丢失的问题。

**关键词**：单分子定位显微镜, 最优传输, 端到端学习, 集合匹配, 迭代神经网络, 超分辨率成像

## 3 点简述
- 核心问题：单分子定位显微镜在密集发射时依赖不可微的非最大抑制层，导致训练困难并可能丢弃真阳性。
- 方法要点：将训练目标重新表述为集合匹配问题，设计最优传输损失以消除推理时对非最大抑制的需求，并集成显微镜光学知识的迭代神经网络。
- 实验或效果：在合成基准和真实生物数据上，新方法在中等和高发射密度下超越现有技术，支持端到端训练。

## 摘要（原文）

> Single-molecule localization microscopy (SMLM) allows reconstructing biology-relevant structures beyond the diffraction limit by detecting and localizing individual fluorophores -- fluorescent molecules stained onto the observed specimen -- over time to reconstruct super-resolved images. Currently, efficient SMLM requires non-overlapping emitting fluorophores, leading to long acquisition times that hinders live-cell imaging. Recent deep-learning approaches can handle denser emissions, but they rely on variants of non-maximum suppression (NMS) layers, which are unfortunately non-differentiable and may discard true positives with their local fusion strategy. In this presentation, we reformulate the SMLM training objective as a set-matching problem, deriving an optimal-transport loss that eliminates the need for NMS during inference and enables end-to-end training. Additionally, we propose an iterative neural network that integrates knowledge of the microscope's optical system inside our model. Experiments on synthetic benchmarks and real biological data show that both our new loss function and architecture surpass the state of the art at moderate and high emitter densities. Code is available at https://github.com/RSLLES/SHOT.

