---
layout: default
title: Implicit Geometry Representations for Vision-and-Language Navigation from Web Videos
---

# Implicit Geometry Representations for Vision-and-Language Navigation from Web Videos
**arXiv**：[2603.09259v1](https://arxiv.org/abs/2603.09259) · [PDF](https://arxiv.org/pdf/2603.09259.pdf)  
**作者**：Mingfei Han, Haihong Hao, Liang Ma, Kamila Zhumakhanova, Ekaterina Radionova, Jingyi Zhang, Xiaojun Chang, Xiaodan Liang, Ivan Laptev  

**一句话要点**：提出基于网络视频的隐式几何表示框架，以解决视觉语言导航中数据多样性和可扩展性不足的问题。

**关键词**：视觉语言导航, 隐式几何表示, 网络视频数据, 大规模框架, 零样本导航, 室内导航

## 3 点简述
- 核心问题：视觉语言导航受限于模拟器数据集的有限多样性和可扩展性，难以捕捉真实世界环境的复杂性。
- 方法要点：从网络房间导览视频构建大规模视频-指令框架，集成描述丰富和动作丰富的轨迹，并引入隐式几何表示直接从RGB帧提取空间线索。
- 实验或效果：在多个VLN基准测试中实现新最优性能，并支持开发鲁棒的零样本导航代理，提升数据利用率和泛化能力。

## 摘要（原文）

> Vision-and-Language Navigation (VLN) has long been constrained by the limited diversity and scalability of simulator-curated datasets, which fail to capture the complexity of real-world environments. To overcome this limitation, we introduce a large-scale video-instruction framework derived from web-based room tour videos, enabling agents to learn from natural human walking demonstrations in diverse, realistic indoor settings. Unlike existing datasets, our framework integrates both open-ended description-enriched trajectories and action-enriched trajectories reconstructed in 3D, providing richer spatial and semantic supervision. A key extension in this work is the incorporation of implicit geometry representations, which extract spatial cues directly from RGB frames without requiring fragile 3D reconstruction. This approach substantially improves data utilization, alleviates reconstruction failures, and unlocks large portions of previously unusable video data. Comprehensive experiments across multiple VLN benchmarks (CVDN, SOON, R2R, and REVERIE) demonstrate that our method not only sets new state-of-the-art performance but also enables the development of robust zero-shot navigation agents. By bridging large-scale web videos with implicit spatial reasoning, this work advances embodied navigation towards more scalable, generalizable, and real-world applicable solutions.

