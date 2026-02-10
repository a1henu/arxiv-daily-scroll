---
layout: default
title: Omni-Video 2: Scaling MLLM-Conditioned Diffusion for Unified Video Generation and Editing
---

# Omni-Video 2: Scaling MLLM-Conditioned Diffusion for Unified Video Generation and Editing
**arXiv**：[2602.08820v1](https://arxiv.org/abs/2602.08820) · [PDF](https://arxiv.org/pdf/2602.08820.pdf)  
**作者**：Hao Yang, Zhiyu Tan, Jia Gong, Luozheng Qin, Hesen Chen, Xiaomeng Yang, Yuqing Sun, Yuetan Lin, Mengping Yang, Hao Li  

**一句话要点**：提出Omni-Video 2，通过连接MLLM与视频扩散模型实现统一视频生成与编辑。

**关键词**：视频生成, 视频编辑, 多模态大语言模型, 扩散模型, 参数高效适配

## 3 点简述
- 核心问题：如何利用MLLM的理解能力提升视频编辑的复杂指令遵循性能。
- 方法要点：开发轻量适配器注入多模态条件，重用预训练视频扩散模型先验。
- 实验或效果：在FiVE和VBench基准测试中展示优越的编辑和生成能力。

## 摘要（原文）

> We present Omni-Video 2, a scalable and computationally efficient model that connects pretrained multimodal large-language models (MLLMs) with video diffusion models for unified video generation and editing. Our key idea is to exploit the understanding and reasoning capabilities of MLLMs to produce explicit target captions to interpret user instructions. In this way, the rich contextual representations from the understanding model are directly used to guide the generative process, thereby improving performance on complex and compositional editing. Moreover, a lightweight adapter is developed to inject multimodal conditional tokens into pretrained text-to-video diffusion models, allowing maximum reuse of their powerful generative priors in a parameter-efficient manner. Benefiting from these designs, we scale up Omni-Video 2 to a 14B video diffusion model on meticulously curated training data with quality, supporting high quality text-to-video generation and various video editing tasks such as object removal, addition, background change, complex motion editing, \emph{etc.} We evaluate the performance of Omni-Video 2 on the FiVE benchmark for fine-grained video editing and the VBench benchmark for text-to-video generation. The results demonstrate its superior ability to follow complex compositional instructions in video editing, while also achieving competitive or superior quality in video generation tasks.

