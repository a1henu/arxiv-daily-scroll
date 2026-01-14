---
layout: default
title: Decoding Order Matters in Autoregressive Speech Synthesis
---

# Decoding Order Matters in Autoregressive Speech Synthesis
**arXiv**：[2601.08450v1](https://arxiv.org/abs/2601.08450) · [PDF](https://arxiv.org/pdf/2601.08450.pdf)  
**作者**：Minghui Zhao, Anton Ragni  

**一句话要点**：提出基于掩码扩散的自回归语音合成解码顺序优化方法，提升语音质量。

**关键词**：自回归语音合成, 解码顺序优化, 掩码扩散框架, 自适应解码, 声学表示量化

## 3 点简述
- 核心问题：自回归语音合成中解码顺序影响语音质量，传统左到右顺序非最优。
- 方法要点：采用掩码扩散框架，支持任意解码顺序训练和推理，比较固定与自适应策略。
- 实验或效果：自适应解码优于固定顺序，1比特量化声学表示仍能保持高质量语音。

## 摘要（原文）

> Autoregressive speech synthesis often adopts a left-to-right order, yet generation order is a modelling choice. We investigate decoding order through masked diffusion framework, which progressively unmasks positions and allows arbitrary decoding orders during training and inference. By interpolating between identity and random permutations, we show that randomness in decoding order affects speech quality. We further compare fixed strategies, such as \texttt{l2r} and \texttt{r2l} with adaptive ones, such as Top-$K$, finding that fixed-order decoding, including the dominating left-to-right approach, is suboptimal, while adaptive decoding yields better performance. Finally, since masked diffusion requires discrete inputs, we quantise acoustic representations and find that even 1-bit quantisation can support reasonably high-quality speech.

