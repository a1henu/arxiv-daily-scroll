---
layout: default
title: FineTec: Fine-Grained Action Recognition Under Temporal Corruption via Skeleton Decomposition and Sequence Completion
---

# FineTec: Fine-Grained Action Recognition Under Temporal Corruption via Skeleton Decomposition and Sequence Completion
**arXiv**：[2512.25067v1](https://arxiv.org/abs/2512.25067) · [PDF](https://arxiv.org/pdf/2512.25067.pdf)  
**作者**：Dian Shao, Mingfei Shi, Like Liu  

**一句话要点**：提出FineTec框架，通过骨架分解与序列补全解决时间损坏下的细粒度动作识别问题。

**关键词**：细粒度动作识别, 时间损坏, 骨架序列补全, 空间分解, 物理驱动估计, 图卷积网络

## 3 点简述
- 核心问题：时间损坏骨架序列中恢复细粒度动作的挑战，现有方法易丢失细微运动线索。
- 方法要点：结合上下文感知补全、骨架空间分解和物理驱动加速度估计，增强时空表示。
- 实验或效果：在粗粒度和细粒度基准上显著优于先前方法，尤其在Gym99和Gym288严重损坏设置中表现突出。

## 摘要（原文）

> Recognizing fine-grained actions from temporally corrupted skeleton sequences remains a significant challenge, particularly in real-world scenarios where online pose estimation often yields substantial missing data. Existing methods often struggle to accurately recover temporal dynamics and fine-grained spatial structures, resulting in the loss of subtle motion cues crucial for distinguishing similar actions. To address this, we propose FineTec, a unified framework for Fine-grained action recognition under Temporal Corruption. FineTec first restores a base skeleton sequence from corrupted input using context-aware completion with diverse temporal masking. Next, a skeleton-based spatial decomposition module partitions the skeleton into five semantic regions, further divides them into dynamic and static subgroups based on motion variance, and generates two augmented skeleton sequences via targeted perturbation. These, along with the base sequence, are then processed by a physics-driven estimation module, which utilizes Lagrangian dynamics to estimate joint accelerations. Finally, both the fused skeleton position sequence and the fused acceleration sequence are jointly fed into a GCN-based action recognition head. Extensive experiments on both coarse-grained (NTU-60, NTU-120) and fine-grained (Gym99, Gym288) benchmarks show that FineTec significantly outperforms previous methods under various levels of temporal corruption. Specifically, FineTec achieves top-1 accuracies of 89.1% and 78.1% on the challenging Gym99-severe and Gym288-severe settings, respectively, demonstrating its robustness and generalizability. Code and datasets could be found at https://smartdianlab.github.io/projects-FineTec/.

