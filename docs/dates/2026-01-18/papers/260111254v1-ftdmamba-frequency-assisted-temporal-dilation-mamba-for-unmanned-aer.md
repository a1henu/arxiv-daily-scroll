---
layout: default
title: FTDMamba: Frequency-Assisted Temporal Dilation Mamba for Unmanned Aerial Vehicle Video Anomaly Detection
---

# FTDMamba: Frequency-Assisted Temporal Dilation Mamba for Unmanned Aerial Vehicle Video Anomaly Detection
**arXiv**：[2601.11254v1](https://arxiv.org/abs/2601.11254) · [PDF](https://arxiv.org/pdf/2601.11254.pdf)  
**作者**：Cheng-Zhuang Liu, Si-Bao Chen, Qing-Ling Shu, Chris Ding, Jin Tang, Bin Luo  

**一句话要点**：提出FTDMamba网络，通过频率解耦与时序扩张Mamba解决无人机视频动态背景下的异常检测问题。

**关键词**：无人机视频异常检测, 动态背景处理, 频率分析, 时序建模, Mamba网络, 数据集构建

## 3 点简述
- 核心问题：无人机视频动态背景导致多源运动耦合，现有方法易误判或漏检异常。
- 方法要点：结合频率分析解耦运动模式，利用Mamba建模多时间尺度的时空依赖。
- 实验或效果：在静态基准和新构建的动态数据集MUVAD上实现SOTA性能，代码与数据集开源。

## 摘要（原文）

> Recent advances in video anomaly detection (VAD) mainly focus on ground-based surveillance or unmanned aerial vehicle (UAV) videos with static backgrounds, whereas research on UAV videos with dynamic backgrounds remains limited. Unlike static scenarios, dynamically captured UAV videos exhibit multi-source motion coupling, where the motion of objects and UAV-induced global motion are intricately intertwined. Consequently, existing methods may misclassify normal UAV movements as anomalies or fail to capture true anomalies concealed within dynamic backgrounds. Moreover, many approaches do not adequately address the joint modeling of inter-frame continuity and local spatial correlations across diverse temporal scales. To overcome these limitations, we propose the Frequency-Assisted Temporal Dilation Mamba (FTDMamba) network for UAV VAD, including two core components: (1) a Frequency Decoupled Spatiotemporal Correlation Module, which disentangles coupled motion patterns and models global spatiotemporal dependencies through frequency analysis; and (2) a Temporal Dilation Mamba Module, which leverages Mamba's sequence modeling capability to jointly learn fine-grained temporal dynamics and local spatial structures across multiple temporal receptive fields. Additionally, unlike existing UAV VAD datasets which focus on static backgrounds, we construct a large-scale Moving UAV VAD dataset (MUVAD), comprising 222,736 frames with 240 anomaly events across 12 anomaly types. Extensive experiments demonstrate that FTDMamba achieves state-of-the-art (SOTA) performance on two public static benchmarks and the new MUVAD dataset. The code and MUVAD dataset will be available at: https://github.com/uavano/FTDMamba.

