---
layout: default
title: MPF-Net: Exposing High-Fidelity AI-Generated Video Forgeries via Hierarchical Manifold Deviation and Micro-Temporal Fluctuations
---

# MPF-Net: Exposing High-Fidelity AI-Generated Video Forgeries via Hierarchical Manifold Deviation and Micro-Temporal Fluctuations
**arXiv**：[2601.21408v1](https://arxiv.org/abs/2601.21408) · [PDF](https://arxiv.org/pdf/2601.21408.pdf)  
**作者**：Xinan He, Kaiqing Lin, Yue Zhou, Jiaming Zhong, Wei Ye, Wenhui Yi, Bing Fan, Feng Ding, Haodong Li, Bo Cao, Bin Li  

**一句话要点**：提出MPF-Net框架，通过分层流形偏差和微时序波动检测高保真AI生成视频伪造

**关键词**：视频伪造检测, 流形偏差, 微时序波动, 双路径框架, AI生成视频

## 3 点简述
- 核心问题：AI生成视频在宏观语义和时序一致性上难以区分，但像素组合逻辑存在结构化同质特征
- 方法要点：采用静态流形偏差分支和微时序波动分支的双路径框架，顺序过滤空间异常和计算指纹
- 实验或效果：未知，但框架旨在暴露伪造，无论表现为全局流形偏差还是细微计算痕迹

## 摘要（原文）

> With the rapid advancement of video generation models such as Veo and Wan, the visual quality of synthetic content has reached a level where macro-level semantic errors and temporal inconsistencies are no longer prominent. However, this does not imply that the distinction between real and cutting-edge high-fidelity fake is untraceable. We argue that AI-generated videos are essentially products of a manifold-fitting process rather than a physical recording. Consequently, the pixel composition logic of consecutive adjacent frames residual in AI videos exhibits a structured and homogenous characteristic. We term this phenomenon `Manifold Projection Fluctuations' (MPF). Driven by this insight, we propose a hierarchical dual-path framework that operates as a sequential filtering process. The first, the Static Manifold Deviation Branch, leverages the refined perceptual boundaries of Large-Scale Vision Foundation Models (VFMs) to capture residual spatial anomalies or physical violations that deviate from the natural real-world manifold (off-manifold). For the remaining high-fidelity videos that successfully reside on-manifold and evade spatial detection, we introduce the Micro-Temporal Fluctuation Branch as a secondary, fine-grained filter. By analyzing the structured MPF that persists even in visually perfect sequences, our framework ensures that forgeries are exposed regardless of whether they manifest as global real-world manifold deviations or subtle computational fingerprints.

