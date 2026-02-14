---
layout: default
title: TADA! Tuning Audio Diffusion Models through Activation Steering
---

# TADA! Tuning Audio Diffusion Models through Activation Steering
**arXiv**：[2602.11910v1](https://arxiv.org/abs/2602.11910) · [PDF](https://arxiv.org/pdf/2602.11910.pdf)  
**作者**：Łukasz Staniszewski, Katarzyna Zaleska, Mateusz Modrzejewski, Kamil Deja  

**一句话要点**：提出通过激活引导调优音频扩散模型，以精确控制生成音乐中的语义概念。

**关键词**：音频扩散模型, 激活引导, 语义控制, 注意力层, 音乐生成, 对比学习

## 3 点简述
- 音频扩散模型内部机制不透明，难以理解其如何表示高层次音乐概念。
- 使用激活修补识别出共享的注意力层控制特定语义概念，如乐器或风格。
- 应用对比激活加法和稀疏自编码器，实现高精度调控如节奏或情绪。

## 摘要（原文）

> Audio diffusion models can synthesize high-fidelity music from text, yet their internal mechanisms for representing high-level concepts remain poorly understood. In this work, we use activation patching to demonstrate that distinct semantic musical concepts, such as the presence of specific instruments, vocals, or genre characteristics, are controlled by a small, shared subset of attention layers in state-of-the-art audio diffusion architectures. Next, we demonstrate that applying Contrastive Activation Addition and Sparse Autoencoders in these layers enables more precise control over the generated audio, indicating a direct benefit of the specialization phenomenon. By steering activations of the identified layers, we can alter specific musical elements with high precision, such as modulating tempo or changing a track's mood.

