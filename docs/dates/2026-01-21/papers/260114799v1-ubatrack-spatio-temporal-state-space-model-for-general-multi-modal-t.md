---
layout: default
title: UBATrack: Spatio-Temporal State Space Model for General Multi-Modal Tracking
---

# UBATrack: Spatio-Temporal State Space Model for General Multi-Modal Tracking
**arXiv**：[2601.14799v1](https://arxiv.org/abs/2601.14799) · [PDF](https://arxiv.org/pdf/2601.14799.pdf)  
**作者**：Qihua Liang, Liang Chen, Yaozong Zheng, Jian Nong, Zhiyi Mo, Bineng Zhong  

**一句话要点**：提出基于状态空间模型的多模态跟踪框架UBATrack，以提升时空线索建模效率与性能

**关键词**：多模态目标跟踪, 状态空间模型, 时空建模, 适配器调优, 特征融合, 长序列建模

## 3 点简述
- 当前多模态跟踪器忽视时空线索的有效捕获，影响性能
- UBATrack引入时空Mamba适配器和动态多模态特征混合器，通过适配器调优联合建模跨模态依赖与时空视觉线索
- 实验在RGB-T、RGB-D和RGB-E基准上超越现有方法，训练效率高

## 摘要（原文）

> Multi-modal object tracking has attracted considerable attention by integrating multiple complementary inputs (e.g., thermal, depth, and event data) to achieve outstanding performance. Although current general-purpose multi-modal trackers primarily unify various modal tracking tasks (i.e., RGB-Thermal infrared, RGB-Depth or RGB-Event tracking) through prompt learning, they still overlook the effective capture of spatio-temporal cues. In this work, we introduce a novel multi-modal tracking framework based on a mamba-style state space model, termed UBATrack. Our UBATrack comprises two simple yet effective modules: a Spatio-temporal Mamba Adapter (STMA) and a Dynamic Multi-modal Feature Mixer. The former leverages Mamba's long-sequence modeling capability to jointly model cross-modal dependencies and spatio-temporal visual cues in an adapter-tuning manner. The latter further enhances multi-modal representation capacity across multiple feature dimensions to improve tracking robustness. In this way, UBATrack eliminates the need for costly full-parameter fine-tuning, thereby improving the training efficiency of multi-modal tracking algorithms. Experiments show that UBATrack outperforms state-of-the-art methods on RGB-T, RGB-D, and RGB-E tracking benchmarks, achieving outstanding results on the LasHeR, RGBT234, RGBT210, DepthTrack, VOT-RGBD22, and VisEvent datasets.

