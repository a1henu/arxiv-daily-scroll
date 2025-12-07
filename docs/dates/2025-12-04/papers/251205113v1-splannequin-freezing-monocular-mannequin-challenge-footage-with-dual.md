---
layout: default
title: Splannequin: Freezing Monocular Mannequin-Challenge Footage with Dual-Detection Splatting
---

# Splannequin: Freezing Monocular Mannequin-Challenge Footage with Dual-Detection Splatting
**arXiv**：[2512.05113v1](https://arxiv.org/abs/2512.05113) · [PDF](https://arxiv.org/pdf/2512.05113.pdf)  
**作者**：Hao-Jen Chien, Yi-Chuan Huang, Chung-Ho Wu, Wei-Lun Chao, Yu-Lun Liu  

**一句话要点**：提出Splannequin正则化方法，通过双重检测与时间锚定提升单目Mannequin-Challenge视频的冻结场景重建质量

**关键词**：动态高斯泼溅, 单目视频重建, 时间锚定, 正则化方法, 冻结场景合成

## 3 点简述
- 核心问题：单目Mannequin-Challenge视频重建冻结场景时，稀疏时间监督导致高斯原语出现鬼影和模糊等伪影
- 方法要点：检测高斯原语的隐藏和缺陷状态，并应用时间锚定，无需修改架构或增加推理开销
- 实验或效果：显著改善视觉质量，实现高保真用户可选冻结时间渲染，获得96%用户偏好

## 摘要（原文）

> Synthesizing high-fidelity frozen 3D scenes from monocular Mannequin-Challenge (MC) videos is a unique problem distinct from standard dynamic scene reconstruction. Instead of focusing on modeling motion, our goal is to create a frozen scene while strategically preserving subtle dynamics to enable user-controlled instant selection. To achieve this, we introduce a novel application of dynamic Gaussian splatting: the scene is modeled dynamically, which retains nearby temporal variation, and a static scene is rendered by fixing the model's time parameter. However, under this usage, monocular capture with sparse temporal supervision introduces artifacts like ghosting and blur for Gaussians that become unobserved or occluded at weakly supervised timestamps. We propose Splannequin, an architecture-agnostic regularization that detects two states of Gaussian primitives, hidden and defective, and applies temporal anchoring. Under predominantly forward camera motion, hidden states are anchored to their recent well-observed past states, while defective states are anchored to future states with stronger supervision. Our method integrates into existing dynamic Gaussian pipelines via simple loss terms, requires no architectural changes, and adds zero inference overhead. This results in markedly improved visual quality, enabling high-fidelity, user-selectable frozen-time renderings, validated by a 96% user preference. Project page: https://chien90190.github.io/splannequin/

