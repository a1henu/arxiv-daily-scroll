---
layout: default
title: LASER: Layer-wise Scale Alignment for Training-Free Streaming 4D Reconstruction
---

# LASER: Layer-wise Scale Alignment for Training-Free Streaming 4D Reconstruction
**arXiv**：[2512.13680v1](https://arxiv.org/abs/2512.13680) · [PDF](https://arxiv.org/pdf/2512.13680.pdf)  
**作者**：Tianye Ding, Yiming Xie, Yiqing Liang, Moitreya Chatterjee, Pedro Miraldo, Huaizu Jiang  

**一句话要点**：提出LASER训练免费框架，通过层尺度对齐实现离线模型到流式4D重建的转换

**关键词**：流式4D重建, 训练免费框架, 层尺度对齐, 深度预测, 相机姿态估计, 点云重建

## 3 点简述
- 核心问题：现有前馈重建模型因二次内存复杂度无法处理流式视频，而流式方法需重训练且未充分利用离线模型几何先验。
- 方法要点：引入层尺度对齐，将深度预测分段为离散层，计算每层尺度因子并在相邻窗口和时间戳间传播，解决简单相似变换对齐的层深度错位问题。
- 实验或效果：在相机姿态估计和点云重建上达到先进性能，在RTX A6000 GPU上以14 FPS和6 GB峰值内存运行，支持千米级流式视频部署。

## 摘要（原文）

> Recent feed-forward reconstruction models like VGGT and $π^3$ achieve impressive reconstruction quality but cannot process streaming videos due to quadratic memory complexity, limiting their practical deployment. While existing streaming methods address this through learned memory mechanisms or causal attention, they require extensive retraining and may not fully leverage the strong geometric priors of state-of-the-art offline models. We propose LASER, a training-free framework that converts an offline reconstruction model into a streaming system by aligning predictions across consecutive temporal windows. We observe that simple similarity transformation ($\mathrm{Sim}(3)$) alignment fails due to layer depth misalignment: monocular scale ambiguity causes relative depth scales of different scene layers to vary inconsistently between windows. To address this, we introduce layer-wise scale alignment, which segments depth predictions into discrete layers, computes per-layer scale factors, and propagates them across both adjacent windows and timestamps. Extensive experiments show that LASER achieves state-of-the-art performance on camera pose estimation and point map reconstruction %quality with offline models while operating at 14 FPS with 6 GB peak memory on a RTX A6000 GPU, enabling practical deployment for kilometer-scale streaming videos. Project website: $\href{https://neu-vi.github.io/LASER/}{\texttt{https://neu-vi.github.io/LASER/}}$

