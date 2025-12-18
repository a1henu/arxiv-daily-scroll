---
layout: default
title: MoonSeg3R: Monocular Online Zero-Shot Segment Anything in 3D with Reconstructive Foundation Priors
---

# MoonSeg3R: Monocular Online Zero-Shot Segment Anything in 3D with Reconstructive Foundation Priors
**arXiv**：[2512.15577v1](https://arxiv.org/abs/2512.15577) · [PDF](https://arxiv.org/pdf/2512.15577.pdf)  
**作者**：Zhipeng Du, Duolikun Danier, Jan Eric Lenssen, Hakan Bilen  

**一句话要点**：提出MoonSeg3R以实现在线零样本单目3D实例分割，利用重建基础模型提供几何先验。

**关键词**：单目3D分割, 零样本学习, 在线分割, 重建基础模型, 查询精炼, 时空一致性

## 3 点简述
- 核心问题：现有方法依赖RGB-D序列，无法实现在线零样本单目3D实例分割。
- 方法要点：引入查询精炼模块、3D查询索引记忆和状态分布令牌，从单目RGB流生成3D分割。
- 实验或效果：在ScanNet200和SceneNN上性能与基于RGB-D的先进系统竞争，首次实现在线单目3D分割。

## 摘要（原文）

> In this paper, we focus on online zero-shot monocular 3D instance segmentation, a novel practical setting where existing approaches fail to perform because they rely on posed RGB-D sequences. To overcome this limitation, we leverage CUT3R, a recent Reconstructive Foundation Model (RFM), to provide reliable geometric priors from a single RGB stream. We propose MoonSeg3R, which introduces three key components: (1) a self-supervised query refinement module with spatial-semantic distillation that transforms segmentation masks from 2D visual foundation models (VFMs) into discriminative 3D queries; (2) a 3D query index memory that provides temporal consistency by retrieving contextual queries; and (3) a state-distribution token from CUT3R that acts as a mask identity descriptor to strengthen cross-frame fusion. Experiments on ScanNet200 and SceneNN show that MoonSeg3R is the first method to enable online monocular 3D segmentation and achieves performance competitive with state-of-the-art RGB-D-based systems. Code and models will be released.

