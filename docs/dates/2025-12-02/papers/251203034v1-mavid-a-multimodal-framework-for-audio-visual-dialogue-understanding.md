---
layout: default
title: MAViD: A Multimodal Framework for Audio-Visual Dialogue Understanding and Generation
---

# MAViD: A Multimodal Framework for Audio-Visual Dialogue Understanding and Generation
**arXiv**：[2512.03034v1](https://arxiv.org/abs/2512.03034) · [PDF](https://arxiv.org/pdf/2512.03034.pdf)  
**作者**：Youxin Pang, Jiajun Liu, Lingfeng Tan, Yong Zhang, Feng Gao, Xiang Deng, Zhuoliang Kang, Xiaoming Wei, Yebin Liu  

**一句话要点**：提出MAViD框架以解决音频-视觉对话理解与生成中的多模态融合和长视频一致性挑战。

**关键词**：多模态对话系统, 音频-视觉融合, 长视频生成, 自回归模型, 扩散模型, 对话理解

## 3 点简述
- 核心问题：现有方法难以生成自然长视频对话，需整合理解与生成能力及音频-视频融合。
- 方法要点：采用Conductor-Creator架构，结合自回归和扩散模型，并引入新融合模块增强多模态同步。
- 实验或效果：实验表明框架能生成生动、上下文连贯的长对话交互，准确理解用户多模态查询。

## 摘要（原文）

> We propose MAViD, a novel Multimodal framework for Audio-Visual Dialogue understanding and generation. Existing approaches primarily focus on non-interactive systems and are limited to producing constrained and unnatural human speech.The primary challenge of this task lies in effectively integrating understanding and generation capabilities, as well as achieving seamless multimodal audio-video fusion. To solve these problems, we propose a Conductor-Creator architecture that divides the dialogue system into two primary components.The Conductor is tasked with understanding, reasoning, and generating instructions by breaking them down into motion and speech components, thereby enabling fine-grained control over interactions. The Creator then delivers interactive responses based on these instructions.Furthermore, to address the difficulty of generating long videos with consistent identity, timbre, and tone using dual DiT structures, the Creator adopts a structure that combines autoregressive (AR) and diffusion models. The AR model is responsible for audio generation, while the diffusion model ensures high-quality video generation.Additionally, we propose a novel fusion module to enhance connections between contextually consecutive clips and modalities, enabling synchronized long-duration audio-visual content generation.Extensive experiments demonstrate that our framework can generate vivid and contextually coherent long-duration dialogue interactions and accurately interpret users' multimodal queries.

