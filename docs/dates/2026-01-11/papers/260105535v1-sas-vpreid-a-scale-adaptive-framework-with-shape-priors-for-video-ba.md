---
layout: default
title: SAS-VPReID: A Scale-Adaptive Framework with Shape Priors for Video-based Person Re-Identification at Extreme Far Distances
---

# SAS-VPReID: A Scale-Adaptive Framework with Shape Priors for Video-based Person Re-Identification at Extreme Far Distances
**arXiv**：[2601.05535v1](https://arxiv.org/abs/2601.05535) · [PDF](https://arxiv.org/pdf/2601.05535.pdf)  
**作者**：Qiwei Yang, Pingping Zhang, Yuhao Wang, Zijing Gong  

**一句话要点**：提出SAS-VPReID框架，通过尺度自适应与形状先验解决极端远距离视频行人重识别问题。

**关键词**：视频行人重识别, 尺度自适应, 形状先验, 时序建模, 记忆增强, 极端远距离

## 3 点简述
- 核心问题：极端远距离下视频行人重识别面临分辨率退化、视角变化和外观噪声挑战。
- 方法要点：结合记忆增强视觉骨干、多粒度时序建模和先验正则化形状动态模块提取判别性特征。
- 实验或效果：在VReID-XFD基准测试中验证模块有效性，并在挑战排行榜上排名第一。

## 摘要（原文）

> Video-based Person Re-IDentification (VPReID) aims to retrieve the same person from videos captured by non-overlapping cameras. At extreme far distances, VPReID is highly challenging due to severe resolution degradation, drastic viewpoint variation and inevitable appearance noise. To address these issues, we propose a Scale-Adaptive framework with Shape Priors for VPReID, named SAS-VPReID. The framework is built upon three complementary modules. First, we deploy a Memory-Enhanced Visual Backbone (MEVB) to extract discriminative feature representations, which leverages the CLIP vision encoder and multi-proxy memory. Second, we propose a Multi-Granularity Temporal Modeling (MGTM) to construct sequences at multiple temporal granularities and adaptively emphasize motion cues across scales. Third, we incorporate Prior-Regularized Shape Dynamics (PRSD) to capture body structure dynamics. With these modules, our framework can obtain more discriminative feature representations. Experiments on the VReID-XFD benchmark demonstrate the effectiveness of each module and our final framework ranks the first on the VReID-XFD challenge leaderboard. The source code is available at https://github.com/YangQiWei3/SAS-VPReID.

