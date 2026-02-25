---
layout: default
title: Echoes Over Time: Unlocking Length Generalization in Video-to-Audio Generation Models
---

# Echoes Over Time: Unlocking Length Generalization in Video-to-Audio Generation Models
**arXiv**：[2602.20981v1](https://arxiv.org/abs/2602.20981) · [PDF](https://arxiv.org/pdf/2602.20981.pdf)  
**作者**：Christian Simon, MAsato Ishii, Wei-Yao Wang, Koichi Saito, Akio Hayakawa, Dongseok Shim, Zhi Zhong, Shuyang Cui, Shusuke Takahashi, Takashi Shibuya, Yuki Mitsufuji  

**一句话要点**：提出MMHNet以解决视频到音频生成模型在长视频上的泛化问题

**关键词**：视频到音频生成, 长度泛化, 分层网络, 非因果Mamba, 长视频处理

## 3 点简述
- 核心问题：视频到音频生成中数据有限且文本描述与视频帧信息不匹配，导致模型难以泛化到长视频。
- 方法要点：集成分层方法和非因果Mamba，支持长音频生成，无需在长视频上训练。
- 实验或效果：在长视频基准测试中超越先前工作，能生成超过5分钟的音频。

## 摘要（原文）

> Scaling multimodal alignment between video and audio is challenging, particularly due to limited data and the mismatch between text descriptions and frame-level video information. In this work, we tackle the scaling challenge in multimodal-to-audio generation, examining whether models trained on short instances can generalize to longer ones during testing. To tackle this challenge, we present multimodal hierarchical networks so-called MMHNet, an enhanced extension of state-of-the-art video-to-audio models. Our approach integrates a hierarchical method and non-causal Mamba to support long-form audio generation. Our proposed method significantly improves long audio generation up to more than 5 minutes. We also prove that training short and testing long is possible in the video-to-audio generation tasks without training on the longer durations. We show in our experiments that our proposed method could achieve remarkable results on long-video to audio benchmarks, beating prior works in video-to-audio tasks. Moreover, we showcase our model capability in generating more than 5 minutes, while prior video-to-audio methods fall short in generating with long durations.

