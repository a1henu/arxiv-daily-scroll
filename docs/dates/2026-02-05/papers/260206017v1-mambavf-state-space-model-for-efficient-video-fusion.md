---
layout: default
title: MambaVF: State Space Model for Efficient Video Fusion
---

# MambaVF: State Space Model for Efficient Video Fusion
**arXiv**：[2602.06017v1](https://arxiv.org/abs/2602.06017) · [PDF](https://arxiv.org/pdf/2602.06017.pdf)  
**作者**：Zixiang Zhao, Yukun Cui, Lilun Deng, Haowen Bai, Haotong Qin, Tao Feng, Konrad Schindler  

**一句话要点**：提出MambaVF状态空间模型以高效解决视频融合任务，避免显式运动估计。

**关键词**：视频融合, 状态空间模型, 时序建模, 高效计算, 多任务基准

## 3 点简述
- 现有视频融合方法依赖光流估计和特征变形，导致计算开销大且可扩展性有限。
- MambaVF基于状态空间模型，通过序列状态更新和时空双向扫描机制实现线性复杂度的长程时序建模。
- 实验表明，MambaVF在多种视频融合任务中达到先进性能，显著降低参数和计算成本，提升速度。

## 摘要（原文）

> Video fusion is a fundamental technique in various video processing tasks. However, existing video fusion methods heavily rely on optical flow estimation and feature warping, resulting in severe computational overhead and limited scalability. This paper presents MambaVF, an efficient video fusion framework based on state space models (SSMs) that performs temporal modeling without explicit motion estimation. First, by reformulating video fusion as a sequential state update process, MambaVF captures long-range temporal dependencies with linear complexity while significantly reducing computation and memory costs. Second, MambaVF proposes a lightweight SSM-based fusion module that replaces conventional flow-guided alignment via a spatio-temporal bidirectional scanning mechanism. This module enables efficient information aggregation across frames. Extensive experiments across multiple benchmarks demonstrate that our MambaVF achieves state-of-the-art performance in multi-exposure, multi-focus, infrared-visible, and medical video fusion tasks. We highlight that MambaVF enjoys high efficiency, reducing up to 92.25% of parameters and 88.79% of computational FLOPs and a 2.1x speedup compared to existing methods. Project page: https://mambavf.github.io

