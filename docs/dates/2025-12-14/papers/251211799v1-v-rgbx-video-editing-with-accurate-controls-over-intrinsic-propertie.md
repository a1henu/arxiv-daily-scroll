---
layout: default
title: V-RGBX: Video Editing with Accurate Controls over Intrinsic Properties
---

# V-RGBX: Video Editing with Accurate Controls over Intrinsic Properties
**arXiv**：[2512.11799v1](https://arxiv.org/abs/2512.11799) · [PDF](https://arxiv.org/pdf/2512.11799.pdf)  
**作者**：Ye Fang, Tong Wu, Valentin Deschaintre, Duygu Ceylan, Iliyan Georgiev, Chun-Hao Paul Huang, Yiwei Hu, Xuelin Chen, Tuanfeng Yang Wang  

**一句话要点**：提出V-RGBX框架，实现基于内在属性的视频编辑，支持关键帧编辑与物理一致性传播。

**关键词**：视频编辑, 内在属性感知, 逆渲染, 关键帧编辑, 物理一致性, 场景重照明

## 3 点简述
- 核心问题：现有视频生成模型缺乏联合理解与编辑内在场景属性的闭环框架。
- 方法要点：通过视频逆渲染、合成与关键帧条件编辑，统一内在属性感知的视频编辑能力。
- 实验或效果：在物体外观编辑和场景重照明等应用中，生成时间一致、逼真的视频，超越先前方法。

## 摘要（原文）

> Large-scale video generation models have shown remarkable potential in modeling photorealistic appearance and lighting interactions in real-world scenes. However, a closed-loop framework that jointly understands intrinsic scene properties (e.g., albedo, normal, material, and irradiance), leverages them for video synthesis, and supports editable intrinsic representations remains unexplored. We present V-RGBX, the first end-to-end framework for intrinsic-aware video editing. V-RGBX unifies three key capabilities: (1) video inverse rendering into intrinsic channels, (2) photorealistic video synthesis from these intrinsic representations, and (3) keyframe-based video editing conditioned on intrinsic channels. At the core of V-RGBX is an interleaved conditioning mechanism that enables intuitive, physically grounded video editing through user-selected keyframes, supporting flexible manipulation of any intrinsic modality. Extensive qualitative and quantitative results show that V-RGBX produces temporally consistent, photorealistic videos while propagating keyframe edits across sequences in a physically plausible manner. We demonstrate its effectiveness in diverse applications, including object appearance editing and scene-level relighting, surpassing the performance of prior methods.

