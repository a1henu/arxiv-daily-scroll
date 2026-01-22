---
layout: default
title: FeedbackSTS-Det: Sparse Frames-Based Spatio-Temporal Semantic Feedback Network for Infrared Small Target Detection
---

# FeedbackSTS-Det: Sparse Frames-Based Spatio-Temporal Semantic Feedback Network for Infrared Small Target Detection
**arXiv**：[2601.14690v1](https://arxiv.org/abs/2601.14690) · [PDF](https://arxiv.org/pdf/2601.14690.pdf)  
**作者**：Yian Huang, Qing Qin, Aji Mao, Xiangyu Qiu, Liang Xu, Xian Zhang, Zhenming Peng  

**一句话要点**：提出基于稀疏帧的时空语义反馈网络以解决复杂背景下红外小目标检测问题

**关键词**：红外小目标检测, 时空语义反馈, 稀疏帧建模, 长程依赖, 隐式帧间配准, 语义细化

## 3 点简述
- 核心问题：红外小目标检测面临信噪比极低、动态干扰和特征不明显等挑战，现有方法长程依赖建模效率低且鲁棒性不足。
- 方法要点：设计时空语义反馈策略，包含前向和后向细化模块，嵌入稀疏语义模块以低成本捕获长程依赖，实现隐式帧间配准和语义细化。
- 实验或效果：在多个基准数据集上验证有效性，代码和模型已开源，未知具体性能指标。

## 摘要（原文）

> Infrared small target detection (ISTD) under complex backgrounds remains a critical yet challenging task, primarily due to the extremely low signal-to-clutter ratio, persistent dynamic interference, and the lack of distinct target features. While multi-frame detection methods leverages temporal cues to improve upon single-frame approaches, existing methods still struggle with inefficient long-range dependency modeling and insufficient robustness. To overcome these issues, we propose a novel scheme for ISTD, realized through a sparse frames-based spatio-temporal semantic feedback network named FeedbackSTS-Det. The core of our approach is a novel spatio-temporal semantic feedback strategy with a closed-loop semantic association mechanism, which consists of paired forward and backward refinement modules that work cooperatively across the encoder and decoder. Moreover, both modules incorporate an embedded sparse semantic module (SSM), which performs structured sparse temporal modeling to capture long-range dependencies with low computational cost. This integrated design facilitates robust implicit inter-frame registration and continuous semantic refinement, effectively suppressing false alarms. Furthermore, our overall procedure maintains a consistent training-inference pipeline, which ensures reliable performance transfer and increases model robustness. Extensive experiments on multiple benchmark datasets confirm the effectiveness of FeedbackSTS-Det. Code and models are available at: https://github.com/IDIP-Lab/FeedbackSTS-Det.

