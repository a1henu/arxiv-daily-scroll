---
layout: default
title: MMAudioSep: Taming Video-to-Audio Generative Model Towards Video/Text-Queried Sound Separation
---

# MMAudioSep: Taming Video-to-Audio Generative Model Towards Video/Text-Queried Sound Separation
**arXiv**：[2510.09065v1](https://arxiv.org/abs/2510.09065) · [PDF](https://arxiv.org/pdf/2510.09065.pdf)  
**作者**：Akira Takahashi, Shusuke Takahashi, Yuki Mitsufuji  
**一句话要点**：提出MMAudioSep，基于预训练视频到音频模型实现视频/文本查询的声音分离。
**关键词**：声音分离, 视频到音频生成, 预训练模型微调, 多模态查询, 生成模型

## 3 点简述
- 核心问题：视频或文本查询下的声音分离任务，需高效训练模型。
- 方法要点：利用预训练视频到音频生成模型的知识，通过微调实现分离功能。
- 实验或效果：在分离性能上优于基线模型，并保留原始视频到音频生成能力。

## 摘要（原文）

> We introduce MMAudioSep, a generative model for video/text-queried sound
> separation that is founded on a pretrained video-to-audio model. By leveraging
> knowledge about the relationship between video/text and audio learned through a
> pretrained audio generative model, we can train the model more efficiently,
> i.e., the model does not need to be trained from scratch. We evaluate the
> performance of MMAudioSep by comparing it to existing separation models,
> including models based on both deterministic and generative approaches, and
> find it is superior to the baseline models. Furthermore, we demonstrate that
> even after acquiring functionality for sound separation via fine-tuning, the
> model retains the ability for original video-to-audio generation. This
> highlights the potential of foundational sound generation models to be adopted
> for sound-related downstream tasks. Our code is available at
> https://github.com/sony/mmaudiosep.

