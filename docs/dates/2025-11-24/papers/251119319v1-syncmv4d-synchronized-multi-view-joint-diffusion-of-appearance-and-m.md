---
layout: default
title: SyncMV4D: Synchronized Multi-view Joint Diffusion of Appearance and Motion for Hand-Object Interaction Synthesis
---

# SyncMV4D: Synchronized Multi-view Joint Diffusion of Appearance and Motion for Hand-Object Interaction Synthesis
**arXiv**：[2511.19319v1](https://arxiv.org/abs/2511.19319) · [PDF](https://arxiv.org/pdf/2511.19319.pdf)  
**作者**：Lingwei Dang, Zonghan Li, Juntong Li, Hongwen Zhang, Liang An, Yebin Liu, Qingyao Wu  

**一句话要点**：提出SyncMV4D模型，联合生成同步多视角手物交互视频与4D运动，以解决单视角几何失真和3D方法泛化差问题。

**关键词**：手物交互合成, 多视角视频生成, 4D运动生成, 联合扩散模型, 点云对齐

## 3 点简述
- 核心问题：单视角HOI生成易导致几何失真，3D方法依赖实验室数据，泛化能力差。
- 方法要点：采用多视角联合扩散模型和扩散点对齐器，耦合2D外观与4D动态。
- 实验效果：在视觉真实感、运动合理性和多视角一致性上优于现有方法。

## 摘要（原文）

> Hand-Object Interaction (HOI) generation plays a critical role in advancing applications across animation and robotics. Current video-based methods are predominantly single-view, which impedes comprehensive 3D geometry perception and often results in geometric distortions or unrealistic motion patterns. While 3D HOI approaches can generate dynamically plausible motions, their dependence on high-quality 3D data captured in controlled laboratory settings severely limits their generalization to real-world scenarios. To overcome these limitations, we introduce SyncMV4D, the first model that jointly generates synchronized multi-view HOI videos and 4D motions by unifying visual prior, motion dynamics, and multi-view geometry. Our framework features two core innovations: (1) a Multi-view Joint Diffusion (MJD) model that co-generates HOI videos and intermediate motions, and (2) a Diffusion Points Aligner (DPA) that refines the coarse intermediate motion into globally aligned 4D metric point tracks. To tightly couple 2D appearance with 4D dynamics, we establish a closed-loop, mutually enhancing cycle. During the diffusion denoising process, the generated video conditions the refinement of the 4D motion, while the aligned 4D point tracks are reprojected to guide next-step joint generation. Experimentally, our method demonstrates superior performance to state-of-the-art alternatives in visual realism, motion plausibility, and multi-view consistency.

