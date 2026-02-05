---
layout: default
title: Audio ControlNet for Fine-Grained Audio Generation and Editing
---

# Audio ControlNet for Fine-Grained Audio Generation and Editing
**arXiv**：[2602.04680v1](https://arxiv.org/abs/2602.04680) · [PDF](https://arxiv.org/pdf/2602.04680.pdf)  
**作者**：Haina Zhu, Yao Xiao, Xiquan Li, Ziyang Ma, Jianwei Yu, Bowen Zhang, Mingqi Yang, Xie Chen  

**一句话要点**：提出T2A-Adapter以解决细粒度文本到音频生成中精确控制属性如响度、音高和声音事件的问题。

**关键词**：细粒度音频生成, 可控音频生成, 音频编辑, ControlNet, T2A-Adapter, 文本到音频

## 3 点简述
- 核心问题：现有文本到音频模型缺乏对响度、音高和声音事件等属性的精确控制。
- 方法要点：在预训练T2A骨干上训练ControlNet模型，引入T2A-Adapter实现高效结构，仅需38M额外参数。
- 实验或效果：在AudioSet-Strong上达到事件级和段级F1分数的先进性能，并扩展至音频编辑任务。

## 摘要（原文）

> We study the fine-grained text-to-audio (T2A) generation task. While recent models can synthesize high-quality audio from text descriptions, they often lack precise control over attributes such as loudness, pitch, and sound events. Unlike prior approaches that retrain models for specific control types, we propose to train ControlNet models on top of pre-trained T2A backbones to achieve controllable generation over loudness, pitch, and event roll. We introduce two designs, T2A-ControlNet and T2A-Adapter, and show that the T2A-Adapter model offers a more efficient structure with strong control ability. With only 38M additional parameters, T2A-Adapter achieves state-of-the-art performance on the AudioSet-Strong in both event-level and segment-level F1 scores. We further extend this framework to audio editing, proposing T2A-Editor for removing and inserting audio events at time locations specified by instructions. Models, code, dataset pipelines, and benchmarks will be released to support future research on controllable audio generation and editing.

