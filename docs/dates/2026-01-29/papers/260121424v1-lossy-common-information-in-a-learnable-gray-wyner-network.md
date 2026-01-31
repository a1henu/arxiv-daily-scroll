---
layout: default
title: Lossy Common Information in a Learnable Gray-Wyner Network
---

# Lossy Common Information in a Learnable Gray-Wyner Network
**arXiv**：[2601.21424v1](https://arxiv.org/abs/2601.21424) · [PDF](https://arxiv.org/pdf/2601.21424.pdf)  
**作者**：Anderson de Andrade, Alon Harell, Ivan V. Bajić  

**一句话要点**：提出可学习的Gray-Wyner网络以分离计算机视觉任务中的共享与特定信息，减少冗余表示。

**关键词**：Gray-Wyner网络, 损失性公共信息, 多任务表示学习, 计算机视觉编解码, 信息理论应用, 冗余减少

## 3 点简述
- 核心问题：计算机视觉任务间存在大量重叠信息，传统编解码器忽略此点导致表示冗余低效。
- 方法要点：基于Gray-Wyner理论，开发三通道可学习编解码器，分离共享信息和任务特定细节。
- 实验或效果：在六个视觉基准的双任务场景中，该方法显著减少冗余，持续优于独立编码。

## 摘要（原文）

> Many computer vision tasks share substantial overlapping information, yet conventional codecs tend to ignore this, leading to redundant and inefficient representations. The Gray-Wyner network, a classical concept from information theory, offers a principled framework for separating common and task-specific information. Inspired by this idea, we develop a learnable three-channel codec that disentangles shared information from task-specific details across multiple vision tasks. We characterize the limits of this approach through the notion of lossy common information, and propose an optimization objective that balances inherent tradeoffs in learning such representations. Through comparisons of three codec architectures on two-task scenarios spanning six vision benchmarks, we demonstrate that our approach substantially reduces redundancy and consistently outperforms independent coding. These results highlight the practical value of revisiting Gray-Wyner theory in modern machine learning contexts, bridging classic information theory with task-driven representation learning.

