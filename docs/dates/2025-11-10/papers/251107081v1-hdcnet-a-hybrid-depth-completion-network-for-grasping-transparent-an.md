---
layout: default
title: HDCNet: A Hybrid Depth Completion Network for Grasping Transparent and Reflective Objects
---

# HDCNet: A Hybrid Depth Completion Network for Grasping Transparent and Reflective Objects
**arXiv**：[2511.07081v1](https://arxiv.org/abs/2511.07081) · [PDF](https://arxiv.org/pdf/2511.07081.pdf)  
**作者**：Guanghu Xie, Mingxu Li, Songwei Wu, Yang Liu, Zongwu Xie, Baoshi Cao, Hong Liu  

**一句话要点**：提出HDCNet混合深度补全网络，以解决机器人抓取透明和反射物体的深度感知问题。

**关键词**：深度补全, 机器人抓取, 透明物体感知, 混合神经网络, 多模态融合

## 3 点简述
- 核心问题：传统深度传感器在透明和反射表面测量不可靠，限制机器人抓取性能。
- 方法要点：集成Transformer、CNN和Mamba架构，设计双分支编码器和混合融合模块。
- 实验或效果：在多个数据集上实现SOTA性能，抓取成功率提升高达60%。

## 摘要（原文）

> Depth perception of transparent and reflective objects has long been a
> critical challenge in robotic manipulation.Conventional depth sensors often
> fail to provide reliable measurements on such surfaces, limiting the
> performance of robots in perception and grasping tasks. To address this issue,
> we propose a novel depth completion network,HDCNet,which integrates the
> complementary strengths of Transformer,CNN and Mamba
> architectures.Specifically,the encoder is designed as a dual-branch
> Transformer-CNN framework to extract modality-specific features. At the shallow
> layers of the encoder, we introduce a lightweight multimodal fusion module to
> effectively integrate low-level features. At the network bottleneck,a
> Transformer-Mamba hybrid fusion module is developed to achieve deep integration
> of high-level semantic and global contextual information, significantly
> enhancing depth completion accuracy and robustness. Extensive evaluations on
> multiple public datasets demonstrate that HDCNet achieves
> state-of-the-art(SOTA) performance in depth completion
> tasks.Furthermore,robotic grasping experiments show that HDCNet substantially
> improves grasp success rates for transparent and reflective objects,achieving
> up to a 60% increase.

