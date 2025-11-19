---
layout: default
title: StreamingTalker: Audio-driven 3D Facial Animation with Autoregressive Diffusion Model
---

# StreamingTalker: Audio-driven 3D Facial Animation with Autoregressive Diffusion Model
**arXiv**：[2511.14223v1](https://arxiv.org/abs/2511.14223) · [PDF](https://arxiv.org/pdf/2511.14223.pdf)  
**作者**：Yifan Yang, Zhi Cen, Sida Peng, Xiangwei Chen, Yifu Deng, Xinyu Zhu, Fan Jia, Xiaowei Zhou, Hujun Bao  

**一句话要点**：提出自回归扩散模型以解决语音驱动3D面部动画的长序列处理延迟问题

**关键词**：语音驱动动画, 自回归扩散模型, 3D面部动画, 流式处理, 实时合成

## 3 点简述
- 核心问题：现有方法处理长音频序列时性能下降且延迟高
- 方法要点：采用流式处理结合历史运动上下文，迭代生成面部运动帧
- 实验或效果：实现低延迟实时合成，并发布交互演示验证有效性

## 摘要（原文）

> This paper focuses on the task of speech-driven 3D facial animation, which aims to generate realistic and synchronized facial motions driven by speech inputs.Recent methods have employed audio-conditioned diffusion models for 3D facial animation, achieving impressive results in generating expressive and natural animations.However, these methods process the whole audio sequences in a single pass, which poses two major challenges: they tend to perform poorly when handling audio sequences that exceed the training horizon and will suffer from significant latency when processing long audio inputs. To address these limitations, we propose a novel autoregressive diffusion model that processes input audio in a streaming manner. This design ensures flexibility with varying audio lengths and achieves low latency independent of audio duration. Specifically, we select a limited number of past frames as historical motion context and combine them with the audio input to create a dynamic condition. This condition guides the diffusion process to iteratively generate facial motion frames, enabling real-time synthesis with high-quality results. Additionally, we implemented a real-time interactive demo, highlighting the effectiveness and efficiency of our approach. We will release the code at https://zju3dv.github.io/StreamingTalker/.

