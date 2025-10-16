---
layout: default
title: Real-Time Crowd Counting for Embedded Systems with Lightweight Architecture
---

# Real-Time Crowd Counting for Embedded Systems with Lightweight Architecture
**arXiv**：[2510.13250v1](https://arxiv.org/abs/2510.13250) · [PDF](https://arxiv.org/pdf/2510.13250.pdf)  
**作者**：Zhiyuan Zhao, Yubin Wen, Siyu Yang, Lichen Ning, Yuandong Liu, Junyu Gao  

**一句话要点**：提出轻量级架构实现嵌入式系统上的超实时人群计数，兼顾速度与精度

**关键词**：人群计数, 轻量级架构, 嵌入式系统, 实时推理, 多尺度特征融合

## 3 点简述
- 核心问题：现有方法在嵌入式系统上参数多、计算复杂，难以满足实时需求
- 方法要点：采用stem-encoder-decoder结构，结合大卷积核、条件通道加权和多分支融合
- 实验效果：在多个基准测试中推理速度最快，GTX 1080Ti达381.7 FPS，Jetson TX1达71.9 FPS

## 摘要（原文）

> Crowd counting is a task of estimating the number of the crowd through
> images, which is extremely valuable in the fields of intelligent security,
> urban planning, public safety management, and so on. However, the existing
> counting methods have some problems in practical application on embedded
> systems for these fields, such as excessive model parameters, abundant complex
> calculations, etc. The practical application of embedded systems requires the
> model to be real-time, which means that the model is fast enough. Considering
> the aforementioned problems, we design a super real-time model with a
> stem-encoder-decoder structure for crowd counting tasks, which achieves the
> fastest inference compared with state-of-the-arts. Firstly, large convolution
> kernels in the stem network are used to enlarge the receptive field, which
> effectively extracts detailed head information. Then, in the encoder part, we
> use conditional channel weighting and multi-branch local fusion block to merge
> multi-scale features with low computational consumption. This part is crucial
> to the super real-time performance of the model. Finally, the feature pyramid
> networks are added to the top of the encoder to alleviate its incomplete fusion
> problems. Experiments on three benchmarks show that our network is suitable for
> super real-time crowd counting on embedded systems, ensuring competitive
> accuracy. At the same time, the proposed network reasoning speed is the
> fastest. Specifically, the proposed network achieves 381.7 FPS on NVIDIA GTX
> 1080Ti and 71.9 FPS on NVIDIA Jetson TX1.

