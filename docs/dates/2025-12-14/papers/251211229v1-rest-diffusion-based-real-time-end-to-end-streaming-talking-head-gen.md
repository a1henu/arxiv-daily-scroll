---
layout: default
title: REST: Diffusion-based Real-time End-to-end Streaming Talking Head Generation via ID-Context Caching and Asynchronous Streaming Distillation
---

# REST: Diffusion-based Real-time End-to-end Streaming Talking Head Generation via ID-Context Caching and Asynchronous Streaming Distillation
**arXiv**：[2512.11229v1](https://arxiv.org/abs/2512.11229) · [PDF](https://arxiv.org/pdf/2512.11229.pdf)  
**作者**：Haotian Wang, Yuzhe Weng, Xinyi Yu, Jun Du, Haoran Xu, Xiaoyan Wu, Shan He, Bing Yin, Cong Liu, Qingfeng Liu  

**一句话要点**：提出REST框架，通过ID-Context缓存和异步流蒸馏实现基于扩散模型的实时端到端流式说话头生成。

**关键词**：说话头生成, 扩散模型, 实时流式生成, ID-Context缓存, 异步蒸馏训练, 视频潜在空间压缩

## 3 点简述
- 扩散模型在说话头生成中推理慢且非自回归，限制实时应用。
- 引入ID-Context缓存机制和异步流蒸馏训练策略，提升时序一致性和身份连贯性。
- 实验显示REST在生成速度和整体性能上优于现有方法，支持实时流式生成。

## 摘要（原文）

> Diffusion models have significantly advanced the field of talking head generation. However, the slow inference speeds and non-autoregressive paradigms severely constrain the application of diffusion-based THG models. In this study, we propose REST, the first diffusion-based, real-time, end-to-end streaming audio-driven talking head generation framework. To support real-time end-to-end generation, a compact video latent space is first learned through high spatiotemporal VAE compression. Additionally, to enable autoregressive streaming within the compact video latent space, we introduce an ID-Context Cache mechanism, which integrates ID-Sink and Context-Cache principles to key-value caching for maintaining temporal consistency and identity coherence during long-time streaming generation. Furthermore, an Asynchronous Streaming Distillation (ASD) training strategy is proposed to mitigate error accumulation in autoregressive generation and enhance temporal consistency, which leverages a non-streaming teacher with an asynchronous noise schedule to supervise the training of the streaming student model. REST bridges the gap between autoregressive and diffusion-based approaches, demonstrating substantial value for applications requiring real-time talking head generation. Experimental results demonstrate that REST outperforms state-of-the-art methods in both generation speed and overall performance.

