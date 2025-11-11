---
layout: default
title: Otter: Mitigating Background Distractions of Wide-Angle Few-Shot Action Recognition with Enhanced RWKV
---

# Otter: Mitigating Background Distractions of Wide-Angle Few-Shot Action Recognition with Enhanced RWKV
**arXiv**：[2511.06741v1](https://arxiv.org/abs/2511.06741) · [PDF](https://arxiv.org/pdf/2511.06741.pdf)  
**作者**：Wenbo Huang, Jinghui Zhang, Zhenghao Chen, Guang Li, Lei Zhang, Yang Cao, Fang Dong, Takahiro Ogawa, Miki Haseyama  

**一句话要点**：提出Otter方法以解决宽视角少样本动作识别中的背景干扰问题

**关键词**：少样本动作识别, 宽视角视频, 背景干扰缓解, 时间关系重建, RWKV增强

## 3 点简述
- 核心问题：宽视角视频中背景干扰和相似背景帧导致的时间关系退化影响动作识别。
- 方法要点：设计CSM模块分割关键补丁突出主体，TRM模块双向扫描重建时间关系。
- 实验或效果：在多个基准数据集上实现SOTA性能，并在VideoBadminton上验证优越性。

## 摘要（原文）

> Wide-angle videos in few-shot action recognition (FSAR) effectively express
> actions within specific scenarios. However, without a global understanding of
> both subjects and background, recognizing actions in such samples remains
> challenging because of the background distractions. Receptance Weighted Key
> Value (RWKV), which learns interaction between various dimensions, shows
> promise for global modeling. While directly applying RWKV to wide-angle FSAR
> may fail to highlight subjects due to excessive background information.
> Additionally, temporal relation degraded by frames with similar backgrounds is
> difficult to reconstruct, further impacting performance. Therefore, we design
> the CompOund SegmenTation and Temporal REconstructing RWKV (Otter).
> Specifically, the Compound Segmentation Module~(CSM) is devised to segment and
> emphasize key patches in each frame, effectively highlighting subjects against
> background information. The Temporal Reconstruction Module (TRM) is
> incorporated into the temporal-enhanced prototype construction to enable
> bidirectional scanning, allowing better reconstruct temporal relation.
> Furthermore, a regular prototype is combined with the temporal-enhanced
> prototype to simultaneously enhance subject emphasis and temporal modeling,
> improving wide-angle FSAR performance. Extensive experiments on benchmarks such
> as SSv2, Kinetics, UCF101, and HMDB51 demonstrate that Otter achieves
> state-of-the-art performance. Extra evaluation on the VideoBadminton dataset
> further validates the superiority of Otter in wide-angle FSAR.

