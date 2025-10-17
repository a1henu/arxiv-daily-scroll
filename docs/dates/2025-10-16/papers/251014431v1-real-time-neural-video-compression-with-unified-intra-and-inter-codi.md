---
layout: default
title: Real-Time Neural Video Compression with Unified Intra and Inter Coding
---

# Real-Time Neural Video Compression with Unified Intra and Inter Coding
**arXiv**：[2510.14431v1](https://arxiv.org/abs/2510.14431) · [PDF](https://arxiv.org/pdf/2510.14431.pdf)  
**作者**：Hui Xiang, Yifan Bian, Li Li, Jingran Wu, Xianguo Zhang, Dong Liu  

**一句话要点**：提出统一帧内帧间编码的神经视频压缩框架，以解决遮挡和误差传播问题。

**关键词**：神经视频压缩, 帧内帧间编码, 实时编码, 误差传播抑制, 双向帧压缩

## 3 点简述
- 核心问题：现有神经视频压缩在处理遮挡、新内容和帧间误差传播时效率低下。
- 方法要点：引入帧内编码工具，单模型自适应处理帧内和帧间编码，支持双向帧压缩。
- 实验或效果：相比DCVC-RT平均BD-rate降低10.7%，帧比特率和质量更稳定，保持实时性能。

## 摘要（原文）

> Neural video compression (NVC) technologies have advanced rapidly in recent
> years, yielding state-of-the-art schemes such as DCVC-RT that offer superior
> compression efficiency to H.266/VVC and real-time encoding/decoding
> capabilities. Nonetheless, existing NVC schemes have several limitations,
> including inefficiency in dealing with disocclusion and new content, interframe
> error propagation and accumulation, among others. To eliminate these
> limitations, we borrow the idea from classic video coding schemes, which allow
> intra coding within inter-coded frames. With the intra coding tool enabled,
> disocclusion and new content are properly handled, and interframe error
> propagation is naturally intercepted without the need for manual refresh
> mechanisms. We present an NVC framework with unified intra and inter coding,
> where every frame is processed by a single model that is trained to perform
> intra/inter coding adaptively. Moreover, we propose a simultaneous two-frame
> compression design to exploit interframe redundancy not only forwardly but also
> backwardly. Experimental results show that our scheme outperforms DCVC-RT by an
> average of 10.7\% BD-rate reduction, delivers more stable bitrate and quality
> per frame, and retains real-time encoding/decoding performances. Code and
> models will be released.

