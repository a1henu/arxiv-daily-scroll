---
layout: default
title: SJD++: Improved Speculative Jacobi Decoding for Training-free Acceleration of Discrete Auto-regressive Text-to-Image Generation
---

# SJD++: Improved Speculative Jacobi Decoding for Training-free Acceleration of Discrete Auto-regressive Text-to-Image Generation
**arXiv**：[2512.07503v1](https://arxiv.org/abs/2512.07503) · [PDF](https://arxiv.org/pdf/2512.07503.pdf)  
**作者**：Yao Teng, Zhihuan Jiang, Han Shi, Xian Liu, Xuefei Ning, Guohao Dai, Yu Wang, Zhenguo Li, Xihui Liu  

**一句话要点**：提出SJD++以加速自回归文本到图像生成，无需训练即可减少推理延迟和步骤。

**关键词**：自回归模型, 文本到图像生成, 并行解码, 推测采样, Jacobi解码, 推理加速

## 3 点简述
- 自回归模型生成图像慢，需大量顺序前向传递预测下一个标记。
- SJD++结合Jacobi解码的多标记预测和推测采样的草稿验证机制，实现并行解码。
- 实验显示SJD++在多个模型上实现2-3倍延迟降低和2-7倍步骤压缩，视觉质量无下降。

## 摘要（原文）

> Large autoregressive models can generate high-quality, high-resolution images but suffer from slow generation speed, because these models require hundreds to thousands of sequential forward passes for next-token prediction during inference. To accelerate autoregressive text-to-image generation, we propose Speculative Jacobi Decoding++ (SJD++), a training-free probabilistic parallel decoding algorithm. Unlike traditional next-token prediction, SJD++ performs multi-token prediction in each forward pass, drastically reducing generation steps. Specifically, it integrates the iterative multi-token prediction mechanism from Jacobi decoding, with the probabilistic drafting-and-verification mechanism from speculative sampling. More importantly, for further acceleration, SJD++ reuses high-confidence draft tokens after each verification phase instead of resampling them all. We conduct extensive experiments on several representative autoregressive text-to-image generation models and demonstrate that SJD++ achieves $2\times$ to $3\times$ inference latency reduction and $2\times$ to $7\times$ step compression, while preserving visual quality with no observable degradation.

