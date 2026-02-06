---
layout: default
title: MambaVF: State Space Model for Efficient Video Fusion
---

# MambaVF: State Space Model for Efficient Video Fusion
**arXiv**：[2602.06017v1](https://arxiv.org/abs/2602.06017) · [PDF](https://arxiv.org/pdf/2602.06017.pdf)  
**作者**：Zixiang Zhao, Yukun Cui, Lilun Deng, Haowen Bai, Haotong Qin, Tao Feng, Konrad Schindler  

**一句话要点**：提出MambaVF状态空间模型，以高效视频融合解决传统方法依赖光流导致的计算开销问题。

**关键词**：视频融合, 状态空间模型, 时序建模, 高效计算, 多任务基准

## 3 点简述
- 核心问题：现有视频融合方法依赖光流估计和特征扭曲，计算开销大且可扩展性有限。
- 方法要点：基于状态空间模型，通过序列状态更新和时空双向扫描机制，无需显式运动估计实现高效时序建模。
- 实验或效果：在多个基准测试中实现SOTA性能，参数减少92.25%，计算FLOPs降低88.79%，速度提升2.1倍。

## 摘要（原文）

> Video fusion is a fundamental technique in various video processing tasks. However, existing video fusion methods heavily rely on optical flow estimation and feature warping, resulting in severe computational overhead and limited scalability. This paper presents MambaVF, an efficient video fusion framework based on state space models (SSMs) that performs temporal modeling without explicit motion estimation. First, by reformulating video fusion as a sequential state update process, MambaVF captures long-range temporal dependencies with linear complexity while significantly reducing computation and memory costs. Second, MambaVF proposes a lightweight SSM-based fusion module that replaces conventional flow-guided alignment via a spatio-temporal bidirectional scanning mechanism. This module enables efficient information aggregation across frames. Extensive experiments across multiple benchmarks demonstrate that our MambaVF achieves state-of-the-art performance in multi-exposure, multi-focus, infrared-visible, and medical video fusion tasks. We highlight that MambaVF enjoys high efficiency, reducing up to 92.25% of parameters and 88.79% of computational FLOPs and a 2.1x speedup compared to existing methods. Project page: https://mambavf.github.io

