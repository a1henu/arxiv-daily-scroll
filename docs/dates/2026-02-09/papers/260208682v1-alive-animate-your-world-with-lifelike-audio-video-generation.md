---
layout: default
title: ALIVE: Animate Your World with Lifelike Audio-Video Generation
---

# ALIVE: Animate Your World with Lifelike Audio-Video Generation
**arXiv**：[2602.08682v1](https://arxiv.org/abs/2602.08682) · [PDF](https://arxiv.org/pdf/2602.08682.pdf)  
**作者**：Ying Guo, Qijun Gan, Yifu Zhang, Jinlai Liu, Yifei Hu, Pan Xie, Dongjun Qian, Yu Zhang, Ruiqi Li, Yuqi Zhang, Ruibiao Lu, Xiaofeng Mei, Bo Han, Xiang Yin, Bingyue Peng, Zehuan Yuan  

**一句话要点**：提出ALIVE模型，通过联合音频-视频分支实现Sora风格的音视频生成与动画

**关键词**：音视频生成, 动画生成, 跨模态融合, 数据管道, 基准测试, 微调训练

## 3 点简述
- 核心问题：将预训练文本到视频模型扩展为音视频生成与动画，解决音视频同步和参考动画的挑战
- 方法要点：在MMDiT架构中引入TA-CrossAttn和UniTemp-RoPE，设计高质量数据管道进行微调
- 实验或效果：在百万级数据上训练后，性能优于开源模型，匹配或超越商业解决方案

## 摘要（原文）

> Video generation is rapidly evolving towards unified audio-video generation. In this paper, we present ALIVE, a generation model that adapts a pretrained Text-to-Video (T2V) model to Sora-style audio-video generation and animation. In particular, the model unlocks the Text-to-Video&Audio (T2VA) and Reference-to-Video&Audio (animation) capabilities compared to the T2V foundation models. To support the audio-visual synchronization and reference animation, we augment the popular MMDiT architecture with a joint audio-video branch which includes TA-CrossAttn for temporally-aligned cross-modal fusion and UniTemp-RoPE for precise audio-visual alignment. Meanwhile, a comprehensive data pipeline consisting of audio-video captioning, quality control, etc., is carefully designed to collect high-quality finetuning data. Additionally, we introduce a new benchmark to perform a comprehensive model test and comparison. After continue pretraining and finetuning on million-level high-quality data, ALIVE demonstrates outstanding performance, consistently outperforming open-source models and matching or surpassing state-of-the-art commercial solutions. With detailed recipes and benchmarks, we hope ALIVE helps the community develop audio-video generation models more efficiently. Official page: https://github.com/FoundationVision/Alive.

