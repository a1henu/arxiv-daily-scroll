---
layout: default
title: StyleStream: Real-Time Zero-Shot Voice Style Conversion
---

# StyleStream: Real-Time Zero-Shot Voice Style Conversion
**arXiv**：[2602.20113v1](https://arxiv.org/abs/2602.20113) · [PDF](https://arxiv.org/pdf/2602.20113.pdf)  
**作者**：Yisi Liu, Nicholas Lee, Gopala Anumanchipalli  

**一句话要点**：提出StyleStream实现实时零样本语音风格转换，通过解耦内容和风格并采用扩散变换器。

**关键词**：语音风格转换, 零样本学习, 扩散变换器, 实时处理, 内容风格解耦

## 3 点简述
- 核心问题：语音风格转换需解耦语言内容和风格，现有方法质量有限且未实现实时处理。
- 方法要点：使用Destylizer去除风格保留内容，Stylizer基于扩散变换器引入目标风格，通过文本监督和信息瓶颈增强解耦。
- 实验或效果：实现端到端延迟1秒的实时转换，性能达到最先进水平，提供在线演示。

## 摘要（原文）

> Voice style conversion aims to transform an input utterance to match a target speaker's timbre, accent, and emotion, with a central challenge being the disentanglement of linguistic content from style. While prior work has explored this problem, conversion quality remains limited, and real-time voice style conversion has not been addressed. We propose StyleStream, the first streamable zero-shot voice style conversion system that achieves state-of-the-art performance. StyleStream consists of two components: a Destylizer, which removes style attributes while preserving linguistic content, and a Stylizer, a diffusion transformer (DiT) that reintroduces target style conditioned on reference speech. Robust content-style disentanglement is enforced through text supervision and a highly constrained information bottleneck. This design enables a fully non-autoregressive architecture, achieving real-time voice style conversion with an end-to-end latency of 1 second. Samples and real-time demo: https://berkeley-speech-group.github.io/StyleStream/.

