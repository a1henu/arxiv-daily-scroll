---
layout: default
title: Simple Models, Rich Representations: Visual Decoding from Primate Intracortical Neural Signals
---

# Simple Models, Rich Representations: Visual Decoding from Primate Intracortical Neural Signals
**arXiv**：[2601.11108v1](https://arxiv.org/abs/2601.11108) · [PDF](https://arxiv.org/pdf/2601.11108.pdf)  
**作者**：Matteo Ciferri, Matteo Ferrante, Nicola Toschi  

**一句话要点**：提出基于简单模型与丰富表示的视觉解码方法，从灵长类颅内神经信号中重建图像。

**关键词**：视觉解码, 神经信号处理, 时间注意力, 生成模型, 脑机接口, 语义重建

## 3 点简述
- 核心问题：如何从高密度颅内记录解码视觉信息，以理解神经活动与感知的关系。
- 方法要点：使用简单模型结合时间注意力与浅层MLP，强调建模神经信号的时间动态而非架构复杂性。
- 实验或效果：在THINGS数据集上达到70% top-1图像检索准确率，并设计生成式解码管道从200 ms脑活动生成图像。

## 摘要（原文）

> Understanding how neural activity gives rise to perception is a central challenge in neuroscience. We address the problem of decoding visual information from high-density intracortical recordings in primates, using the THINGS Ventral Stream Spiking Dataset. We systematically evaluate the effects of model architecture, training objectives, and data scaling on decoding performance. Results show that decoding accuracy is mainly driven by modeling temporal dynamics in neural signals, rather than architectural complexity. A simple model combining temporal attention with a shallow MLP achieves up to 70% top-1 image retrieval accuracy, outperforming linear baselines as well as recurrent and convolutional approaches. Scaling analyses reveal predictable diminishing returns with increasing input dimensionality and dataset size. Building on these findings, we design a modular generative decoding pipeline that combines low-resolution latent reconstruction with semantically conditioned diffusion, generating plausible images from 200 ms of brain activity. This framework provides principles for brain-computer interfaces and semantic neural decoding.

