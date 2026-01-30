---
layout: default
title: Towards Geometry-Aware and Motion-Guided Video Human Mesh Recovery
---

# Towards Geometry-Aware and Motion-Guided Video Human Mesh Recovery
**arXiv**：[2601.21376v1](https://arxiv.org/abs/2601.21376) · [PDF](https://arxiv.org/pdf/2601.21376.pdf)  
**作者**：Hongjun Chen, Huan Zheng, Wencheng Han, Jianbing Shen  

**一句话要点**：提出HMRMamba框架，通过几何感知提升与运动引导重建解决视频人体网格恢复的物理不合理问题。

**关键词**：视频人体网格恢复, 结构化状态空间模型, 几何感知提升, 运动引导重建, 时空一致性, 计算效率

## 3 点简述
- 现有方法依赖有缺陷的3D姿态锚点，难以建模复杂时空动态，导致结果物理不合理。
- 引入结构化状态空间模型，设计几何感知提升模块和运动引导重建网络，增强重建的准确性和时间一致性。
- 在3DPW等基准测试中达到新最优性能，提升重建精度和时间一致性，同时计算效率高。

## 摘要（原文）

> Existing video-based 3D Human Mesh Recovery (HMR) methods often produce physically implausible results, stemming from their reliance on flawed intermediate 3D pose anchors and their inability to effectively model complex spatiotemporal dynamics. To overcome these deep-rooted architectural problems, we introduce HMRMamba, a new paradigm for HMR that pioneers the use of Structured State Space Models (SSMs) for their efficiency and long-range modeling prowess. Our framework is distinguished by two core contributions. First, the Geometry-Aware Lifting Module, featuring a novel dual-scan Mamba architecture, creates a robust foundation for reconstruction. It directly grounds the 2D-to-3D pose lifting process with geometric cues from image features, producing a highly reliable 3D pose sequence that serves as a stable anchor. Second, the Motion-guided Reconstruction Network leverages this anchor to explicitly process kinematic patterns over time. By injecting this crucial temporal awareness, it significantly enhances the final mesh's coherence and robustness, particularly under occlusion and motion blur. Comprehensive evaluations on 3DPW, MPI-INF-3DHP, and Human3.6M benchmarks confirm that HMRMamba sets a new state-of-the-art, outperforming existing methods in both reconstruction accuracy and temporal consistency while offering superior computational efficiency.

