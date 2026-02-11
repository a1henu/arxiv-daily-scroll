---
layout: default
title: AUHead: Realistic Emotional Talking Head Generation via Action Units Control
---

# AUHead: Realistic Emotional Talking Head Generation via Action Units Control
**arXiv**：[2602.09534v1](https://arxiv.org/abs/2602.09534) · [PDF](https://arxiv.org/pdf/2602.09534.pdf)  
**作者**：Jiayi Lyu, Leigang Qu, Wenjing Zhang, Hanyu Jiang, Kai Liu, Zhenglin Zhou, Xiaobo Xia, Jian Xue, Tat-Seng Chua  

**一句话要点**：提出AUHead方法，通过动作单元控制实现逼真的情感说话头生成，解决现有方法情感控制不足的问题。

**关键词**：说话头生成, 动作单元控制, 音频语言模型, 扩散模型, 情感表达, 视频合成

## 3 点简述
- 核心问题：现有说话头生成方法缺乏细粒度情感控制，难以捕捉微妙情绪表达。
- 方法要点：采用两阶段方法，先利用音频语言模型从音频解耦动作单元，再通过扩散模型基于动作单元序列合成视频。
- 实验或效果：在基准数据集上，AUHead在情感逼真度、唇部同步和视觉一致性方面超越现有技术。

## 摘要（原文）

> Realistic talking-head video generation is critical for virtual avatars, film production, and interactive systems. Current methods struggle with nuanced emotional expressions due to the lack of fine-grained emotion control. To address this issue, we introduce a novel two-stage method (AUHead) to disentangle fine-grained emotion control, i.e. , Action Units (AUs), from audio and achieve controllable generation. In the first stage, we explore the AU generation abilities of large audio-language models (ALMs), by spatial-temporal AU tokenization and an "emotion-then-AU" chain-of-thought mechanism. It aims to disentangle AUs from raw speech, effectively capturing subtle emotional cues. In the second stage, we propose an AU-driven controllable diffusion model that synthesizes realistic talking-head videos conditioned on AU sequences. Specifically, we first map the AU sequences into the structured 2D facial representation to enhance spatial fidelity, and then model the AU-vision interaction within cross-attention modules. To achieve flexible AU-quality trade-off control, we introduce an AU disentanglement guidance strategy during inference, further refining the emotional expressiveness and identity consistency of the generated videos. Results on benchmark datasets demonstrate that our approach achieves competitive performance in emotional realism, accurate lip synchronization, and visual coherence, significantly surpassing existing techniques. Our implementation is available at https://github.com/laura990501/AUHead_ICLR

