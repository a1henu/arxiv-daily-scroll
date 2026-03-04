---
layout: default
title: Channel-Adaptive Edge AI: Maximizing Inference Throughput by Adapting Computational Complexity to Channel States
---

# Channel-Adaptive Edge AI: Maximizing Inference Throughput by Adapting Computational Complexity to Channel States
**arXiv**：[2603.03146v1](https://arxiv.org/abs/2603.03146) · [PDF](https://arxiv.org/pdf/2603.03146.pdf)  
**作者**：Jierui Zhang, Jianhao Huang, Kaibin Huang  

**一句话要点**：提出信道自适应边缘AI算法，通过调整计算复杂度最大化信道状态下的推理吞吐量

**关键词**：边缘推理, 信道自适应, 端到端性能建模, 混合冯·米塞斯分布, 推理吞吐量最大化, 通信计算集成

## 3 点简述
- 核心问题：缺乏端到端推理性能的理论框架，需同时考虑信道失真和AI模型复杂度
- 方法要点：使用混合冯·米塞斯分布建模特征分布，推导推理精度闭式表达式，并联合优化特征压缩和模型复杂度
- 实验或效果：算法在延迟和精度约束下优于固定复杂度方法，实现通信与计算全集成

## 摘要（原文）

> \emph{Integrated communication and computation} (IC$^2$) has emerged as a new paradigm for enabling efficient edge inference in sixth-generation (6G) networks. However, the design of IC$^2$ technologies is hindered by the lack of a tractable theoretical framework for characterizing \emph{end-to-end} (E2E) inference performance. The metric is highly complicated as it needs to account for both channel distortion and artificial intelligence (AI) model architecture and computational complexity. In this work, we address this challenge by developing a tractable analytical model for E2E inference accuracy and leveraging it to design a \emph{channel-adaptive AI} algorithm that maximizes inference throughput, referred to as the edge processing rate (EPR), under latency and accuracy constraints. Specifically, we consider an edge inference system in which a server deploys a backbone model with early exit, which enables flexible computational complexity, to perform inference on data features transmitted by a mobile device. The proposed accuracy model characterizes high-dimensional feature distributions in the angular domain using a Mixture of von Mises (MvM) distribution. This leads to a desired closed-form expression for inference accuracy as a function of quantization bit-width and model traversal depth, which represents channel distortion and computational complexity, respectively. Building upon this accuracy model, we formulate and solve the EPR maximization problem under joint latency and accuracy constraints, leading to a channel-adaptive AI algorithm that achieves full IC$^2$ integration. The proposed algorithm jointly adapts transmit-side feature compression and receive-side model complexity according to channel conditions to maximize overall efficiency and inference throughput. Experimental results demonstrate its superior performance as compared with fixed-complexity counterparts.

