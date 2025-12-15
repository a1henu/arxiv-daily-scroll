---
layout: default
title: Exploring MLLM-Diffusion Information Transfer with MetaCanvas
---

# Exploring MLLM-Diffusion Information Transfer with MetaCanvas
**arXiv**：[2512.11464v1](https://arxiv.org/abs/2512.11464) · [PDF](https://arxiv.org/pdf/2512.11464.pdf)  
**作者**：Han Lin, Xichen Pan, Ziqi Huang, Ji Hou, Jialiang Wang, Weifeng Chen, Zecheng He, Felix Juefei-Xu, Junzhe Sun, Zhipeng Fan, Ali Thabet, Mohit Bansal, Chu Wang  

**一句话要点**：提出MetaCanvas框架，让多模态大语言模型在潜在空间中规划，以提升扩散模型生成图像的精确控制能力。

**关键词**：多模态大语言模型, 扩散模型, 潜在空间规划, 图像生成, 视频生成, 精确控制

## 3 点简述
- 当前多模态大语言模型在视觉理解中能解析复杂布局，但在生成图像时仅用作全局文本编码器，未充分利用其推理能力。
- MetaCanvas是一个轻量级框架，使多模态大语言模型能在空间和时空潜在空间中直接进行推理和规划，并与扩散生成器紧密接口。
- 在三种扩散骨干网络上实现，并在六项任务中评估，包括文本到图像生成和视频编辑，均优于全局条件基线。

## 摘要（原文）

> Multimodal learning has rapidly advanced visual understanding, largely via multimodal large language models (MLLMs) that use powerful LLMs as cognitive cores. In visual generation, however, these powerful core models are typically reduced to global text encoders for diffusion models, leaving most of their reasoning and planning ability unused. This creates a gap: current multimodal LLMs can parse complex layouts, attributes, and knowledge-intensive scenes, yet struggle to generate images or videos with equally precise and structured control. We propose MetaCanvas, a lightweight framework that lets MLLMs reason and plan directly in spatial and spatiotemporal latent spaces and interface tightly with diffusion generators. We empirically implement MetaCanvas on three different diffusion backbones and evaluate it across six tasks, including text-to-image generation, text/image-to-video generation, image/video editing, and in-context video generation, each requiring precise layouts, robust attribute binding, and reasoning-intensive control. MetaCanvas consistently outperforms global-conditioning baselines, suggesting that treating MLLMs as latent-space planners is a promising direction for narrowing the gap between multimodal understanding and generation.

