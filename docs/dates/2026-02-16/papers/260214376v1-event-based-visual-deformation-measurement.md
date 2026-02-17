---
layout: default
title: Event-based Visual Deformation Measurement
---

# Event-based Visual Deformation Measurement
**arXiv**：[2602.14376v1](https://arxiv.org/abs/2602.14376) · [PDF](https://arxiv.org/pdf/2602.14376.pdf)  
**作者**：Yuliang Wu, Wei Zhai, Yuxin Cui, Tiesong Zhao, Yang Cao, Zheng-Jun Zha  

**一句话要点**：提出事件-帧融合框架以解决高动态场景下视觉变形测量的存储与计算限制

**关键词**：事件相机, 视觉变形测量, 事件-帧融合, 仿射不变单纯形, 密集跟踪, 基准数据集

## 3 点简述
- 传统图像方法依赖帧间小运动，限制高动态场景应用或需高速相机导致高开销
- 融合事件提供密集时间运动线索与帧提供空间精确估计，采用仿射不变单纯形框架分区线性化变形场
- 实验在超过120序列基准数据集上，生存率提升1.6%，存储与处理资源仅需高速视频方法的18.9%

## 摘要（原文）

> Visual Deformation Measurement (VDM) aims to recover dense deformation fields by tracking surface motion from camera observations. Traditional image-based methods rely on minimal inter-frame motion to constrain the correspondence search space, which limits their applicability to highly dynamic scenes or necessitates high-speed cameras at the cost of prohibitive storage and computational overhead. We propose an event-frame fusion framework that exploits events for temporally dense motion cues and frames for spatially dense precise estimation. Revisiting the solid elastic modeling prior, we propose an Affine Invariant Simplicial (AIS) framework. It partitions the deformation field into linearized sub-regions with low-parametric representation, effectively mitigating motion ambiguities arising from sparse and noisy events. To speed up parameter searching and reduce error accumulation, a neighborhood-greedy optimization strategy is introduced, enabling well-converged sub-regions to guide their poorly-converged neighbors, effectively suppress local error accumulation in long-term dense tracking. To evaluate the proposed method, a benchmark dataset with temporally aligned event streams and frames is established, encompassing over 120 sequences spanning diverse deformation scenarios. Experimental results show that our method outperforms the state-of-the-art baseline by 1.6% in survival rate. Remarkably, it achieves this using only 18.9% of the data storage and processing resources of high-speed video methods.

