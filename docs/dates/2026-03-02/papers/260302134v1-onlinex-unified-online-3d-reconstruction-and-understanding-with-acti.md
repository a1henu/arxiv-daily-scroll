---
layout: default
title: OnlineX: Unified Online 3D Reconstruction and Understanding with Active-to-Stable State Evolution
---

# OnlineX: Unified Online 3D Reconstruction and Understanding with Active-to-Stable State Evolution
**arXiv**：[2603.02134v1](https://arxiv.org/abs/2603.02134) · [PDF](https://arxiv.org/pdf/2603.02134.pdf)  
**作者**：Chong Xia, Fangfu Liu, Yule Wang, Yize Pang, Yueqi Duan  

**一句话要点**：提出OnlineX框架，通过解耦主动-稳定状态演化实现在线3D重建与理解

**关键词**：在线3D重建, 高斯泼溅, 状态演化, 语义理解, 实时推理, 累积漂移

## 3 点简述
- 核心问题：现有3D高斯泼溅方法为离线重建，无法处理在线场景中的累积漂移问题
- 方法要点：将记忆状态解耦为主动状态和稳定状态，并融合视觉外观与语言场进行联合建模
- 实验或效果：在主流数据集上优于先前工作，支持实时推理，适应不同长度输入序列

## 摘要（原文）

> Recent advances in generalizable 3D Gaussian Splatting (3DGS) have enabled rapid 3D scene reconstruction within seconds, eliminating the need for per-scene optimization. However, existing methods primarily follow an offline reconstruction paradigm, lacking the capacity for continuous reconstruction, which limits their applicability to online scenarios such as robotics and VR/AR. In this paper, we introduce OnlineX, a feed-forward framework that reconstructs both 3D visual appearance and language fields in an online manner using only streaming images. A key challenge in online formulation is the cumulative drift issue, which is rooted in the fundamental conflict between two opposing roles of the memory state: an active role that constantly refreshes to capture high-frequency local geometry, and a stable role that conservatively accumulates and preserves the long-term global structure. To address this, we introduce a decoupled active-to-stable state evolution paradigm. Our framework decouples the memory state into a dedicated active state and a persistent stable state, and then cohesively fuses the information from the former into the latter to achieve both fidelity and stability. Moreover, we jointly model visual appearance and language fields and incorporate an implicit Gaussian fusion module to enhance reconstruction quality. Experiments on mainstream datasets demonstrate that our method consistently outperforms prior work in novel view synthesis and semantic understanding, showcasing robust performance across input sequences of varying lengths with real-time inference speed.

