---
layout: default
title: Unbiased Gradient Estimation for Event Binning via Functional Backpropagation
---

# Unbiased Gradient Estimation for Event Binning via Functional Backpropagation
**arXiv**：[2602.12590v1](https://arxiv.org/abs/2602.12590) · [PDF](https://arxiv.org/pdf/2602.12590.pdf)  
**作者**：Jinze Chen, Wei Zhai, Han Han, Tiankai Ma, Yang Cao, Bin Li, Zheng-Jun Zha  

**一句话要点**：提出基于函数反向传播的无偏梯度估计框架，以解决事件分箱操作中的梯度截断与偏差问题。

**关键词**：事件相机, 梯度估计, 反向传播, 弱导数, 视觉感知, 自监督学习

## 3 点简述
- 事件分箱操作不连续，导致梯度截断或偏差，限制事件数据学习效率。
- 通过分部积分和余切函数重构，在反向传播中合成弱导数，保持前向输出不变。
- 实验表明，在自监督光流和SLAM等任务中，显著降低误差并加速收敛。

## 摘要（原文）

> Event-based vision encodes dynamic scenes as asynchronous spatio-temporal spikes called events. To leverage conventional image processing pipelines, events are typically binned into frames. However, binning functions are discontinuous, which truncates gradients at the frame level and forces most event-based algorithms to rely solely on frame-based features. Attempts to directly learn from raw events avoid this restriction but instead suffer from biased gradient estimation due to the discontinuities of the binning operation, ultimately limiting their learning efficiency. To address this challenge, we propose a novel framework for unbiased gradient estimation of arbitrary binning functions by synthesizing weak derivatives during backpropagation while keeping the forward output unchanged. The key idea is to exploit integration by parts: lifting the target functions to functionals yields an integral form of the derivative of the binning function during backpropagation, where the cotangent function naturally arises. By reconstructing this cotangent function from the sampled cotangent vector, we compute weak derivatives that provably match long-range finite differences of both smooth and non-smooth targets. Experimentally, our method improves simple optimization-based egomotion estimation with 3.2\% lower RMS error and 1.57$\times$ faster convergence. On complex downstream tasks, we achieve 9.4\% lower EPE in self-supervised optical flow, and 5.1\% lower RMS error in SLAM, demonstrating broad benefits for event-based visual perception. Source code can be found at https://github.com/chjz1024/EventFBP.

