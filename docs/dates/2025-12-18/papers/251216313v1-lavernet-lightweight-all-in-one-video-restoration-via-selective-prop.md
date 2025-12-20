---
layout: default
title: LaverNet: Lightweight All-in-one Video Restoration via Selective Propagation
---

# LaverNet: Lightweight All-in-one Video Restoration via Selective Propagation
**arXiv**：[2512.16313v1](https://arxiv.org/abs/2512.16313) · [PDF](https://arxiv.org/pdf/2512.16313.pdf)  
**作者**：Haiyu Zhao, Yiwen Shan, Yuanbiao Gou, Xi Peng  

**一句话要点**：提出LaverNet轻量级一体化视频修复网络，通过选择性传播解决时变退化干扰问题。

**关键词**：视频修复, 轻量级网络, 选择性传播, 一体化模型, 时变退化

## 3 点简述
- 核心问题：时变退化主导时间建模，混淆模型关注伪影而非视频内容。
- 方法要点：引入选择性传播机制，仅传输退化无关特征，减少退化影响。
- 实验或效果：仅362K参数，性能可比或优于现有大模型，参数少于1%。

## 摘要（原文）

> Recent studies have explored all-in-one video restoration, which handles multiple degradations with a unified model. However, these approaches still face two challenges when dealing with time-varying degradations. First, the degradation can dominate temporal modeling, confusing the model to focus on artifacts rather than the video content. Second, current methods typically rely on large models to handle all-in-one restoration, concealing those underlying difficulties. To address these challenges, we propose a lightweight all-in-one video restoration network, LaverNet, with only 362K parameters. To mitigate the impact of degradations on temporal modeling, we introduce a novel propagation mechanism that selectively transmits only degradation-agnostic features across frames. Through LaverNet, we demonstrate that strong all-in-one restoration can be achieved with a compact network. Despite its small size, less than 1\% of the parameters of existing models, LaverNet achieves comparable, even superior performance across benchmarks.

