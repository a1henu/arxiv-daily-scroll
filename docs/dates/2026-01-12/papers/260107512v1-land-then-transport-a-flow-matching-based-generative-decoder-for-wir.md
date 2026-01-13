---
layout: default
title: Land-then-transport: A Flow Matching-Based Generative Decoder for Wireless Image Transmission
---

# Land-then-transport: A Flow Matching-Based Generative Decoder for Wireless Image Transmission
**arXiv**：[2601.07512v1](https://arxiv.org/abs/2601.07512) · [PDF](https://arxiv.org/pdf/2601.07512.pdf)  
**作者**：Jingwen Fu, Ming Xiao, Mikael Skoglund, Dong In Kim  

**一句话要点**：提出基于流匹配的确定性生成解码器，以解决无线图像传输中的低延迟解码问题。

**关键词**：无线图像传输, 流匹配, 生成解码器, 低延迟解码, 信道感知, ODE解码

## 3 点简述
- 无线图像传输在低延迟下难以平衡速率、可靠性和感知质量。
- 采用流匹配方法构建确定性ODE解码器，复杂度线性于步数，无需迭代去噪。
- 实验在多种信道下优于传统和深度方法，仅需几步即可获得良好感知质量。

## 摘要（原文）

> Due to strict rate and reliability demands, wireless image transmission remains difficult for both classical layered designs and joint source-channel coding (JSCC), especially under low latency. Diffusion-based generative decoders can deliver strong perceptual quality by leveraging learned image priors, but iterative stochastic denoising leads to high decoding delay. To enable low-latency decoding, we propose a flow-matching (FM) generative decoder under a new land-then-transport (LTT) paradigm that tightly integrates the physical wireless channel into a continuous-time probability flow. For AWGN channels, we build a Gaussian smoothing path whose noise schedule indexes effective noise levels, and derive a closed-form teacher velocity field along this path. A neural-network student vector field is trained by conditional flow matching, yielding a deterministic, channel-aware ODE decoder with complexity linear in the number of ODE steps. At inference, it only needs an estimate of the effective noise variance to set the ODE starting time. We further show that Rayleigh fading and MIMO channels can be mapped, via linear MMSE equalization and singular-value-domain processing, to AWGN-equivalent channels with calibrated starting times. Therefore, the same probability path and trained velocity field can be reused for Rayleigh and MIMO without retraining. Experiments on MNIST, Fashion-MNIST, and DIV2K over AWGN, Rayleigh, and MIMO demonstrate consistent gains over JPEG2000+LDPC, DeepJSCC, and diffusion-based baselines, while achieving good perceptual quality with only a few ODE steps. Overall, LTT provides a deterministic, physically interpretable, and computation-efficient framework for generative wireless image decoding across diverse channels.

