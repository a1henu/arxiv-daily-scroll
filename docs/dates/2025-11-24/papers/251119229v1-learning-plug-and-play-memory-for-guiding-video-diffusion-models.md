---
layout: default
title: Learning Plug-and-play Memory for Guiding Video Diffusion Models
---

# Learning Plug-and-play Memory for Guiding Video Diffusion Models
**arXiv**：[2511.19229v1](https://arxiv.org/abs/2511.19229) · [PDF](https://arxiv.org/pdf/2511.19229.pdf)  
**作者**：Selena Song, Ziming Xu, Zijun Zhang, Kun Zhou, Jiaxian Guo, Lianhui Qin, Biwei Huang  

**一句话要点**：提出可插拔记忆模块以提升视频扩散模型的世界知识注入能力

**关键词**：视频扩散模型, 可插拔记忆, 世界知识注入, Transformer干预, 高效训练, 物理规则遵循

## 3 点简述
- 核心问题：视频扩散模型常违反物理规律和常识动态，缺乏显式世界知识
- 方法要点：设计可学习记忆编码器，通过干预隐藏状态注入参考视频知识
- 实验或效果：在少量数据和参数下高效训练，提升视频物理规则遵循和保真度

## 摘要（原文）

> Diffusion Transformer(DiT) based video generation models have recently achieved impressive visual quality and temporal coherence, but they still frequently violate basic physical laws and commonsense dynamics, revealing a lack of explicit world knowledge. In this work, we explore how to equip them with a plug-and-play memory that injects useful world knowledge. Motivated by in-context memory in Transformer-based LLMs, we conduct empirical studies to show that DiT can be steered via interventions on its hidden states, and simple low-pass and high-pass filters in the embedding space naturally disentangle low-level appearance and high-level physical/semantic cues, enabling targeted guidance. Building on these observations, we propose a learnable memory encoder DiT-Mem, composed of stacked 3D CNNs, low-/high-pass filters, and self-attention layers. The encoder maps reference videos into a compact set of memory tokens, which are concatenated as the memory within the DiT self-attention layers. During training, we keep the diffusion backbone frozen, and only optimize the memory encoder. It yields a rather efficient training process on few training parameters (150M) and 10K data samples, and enables plug-and-play usage at inference time. Extensive experiments on state-of-the-art models demonstrate the effectiveness of our method in improving physical rule following and video fidelity. Our code and data are publicly released here: https://thrcle421.github.io/DiT-Mem-Web/.

