---
layout: default
title: Detecting radar targets swarms in range profiles with a partially complex-valued neural network
---

# Detecting radar targets swarms in range profiles with a partially complex-valued neural network
**arXiv**：[2602.09597v1](https://arxiv.org/abs/2602.09597) · [PDF](https://arxiv.org/pdf/2602.09597.pdf)  
**作者**：Martin Bauw  

**一句话要点**：提出部分复值神经网络以解决雷达距离剖面中多目标检测问题

**关键词**：雷达目标检测, 部分复值神经网络, 距离剖面处理, 多目标检测, 自适应阈值

## 3 点简述
- 核心问题：雷达目标检测受杂波、波形失真及目标邻近影响，导致检测困难。
- 方法要点：采用部分复值神经网络作为自适应距离剖面处理，一次性处理整个接收信号生成检测剖面。
- 实验或效果：通过模拟数据集比较脉冲压缩与神经网络方法，后者在生成完整检测剖面方面表现未知。

## 摘要（原文）

> Correctly detecting radar targets is usually challenged by clutter and waveform distortion. An additional difficulty stems from the relative proximity of several targets, the latter being perceived as a single target in the worst case, or influencing each other's detection thresholds. The negative impact of targets proximity notably depends on the range resolution defined by the radar parameters and the adaptive threshold adopted. This paper addresses the matter of targets detection in radar range profiles containing multiple targets with varying proximity and distorted echoes. Inspired by recent contributions in the radar and signal processing literature, this work proposes partially complex-valued neural networks as an adaptive range profile processing. Simulated datasets are generated and experiments are conducted to compare a common pulse compression approach with a simple neural network partially defined by complex-valued parameters. Whereas the pulse compression processes one pulse length at a time, the neural network put forward is a generative architecture going through the entire received signal in one go to generate a complete detection profile.

