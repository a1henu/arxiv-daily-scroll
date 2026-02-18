---
layout: default
title: Proactive Conversational Assistant for a Procedural Manual Task based on Audio and IMU
---

# Proactive Conversational Assistant for a Procedural Manual Task based on Audio and IMU
**arXiv**：[2602.15707v1](https://arxiv.org/abs/2602.15707) · [PDF](https://arxiv.org/pdf/2602.15707.pdf)  
**作者**：Rehana Mahfuz, Yinyi Guo, Erik Visser, Phanidhar Chinchili  

**一句话要点**：提出基于音频和IMU的实时对话助手，用于家具组装任务，以轻量隐私保护模态替代视频输入。

**关键词**：实时对话助手, 隐私保护模态, UWA LoRA微调, 家具组装任务, 边缘计算

## 3 点简述
- 核心问题：实时对话助手依赖视频输入，计算成本高且侵犯隐私，需轻量隐私保护方案。
- 方法要点：使用音频和IMU输入理解上下文，设计UWA LoRA微调方法抑制非信息对话，提升指令传达效率。
- 实验或效果：微调后F-score提升>30%，速度提升16倍，并实现边缘设备部署，无需云端依赖。

## 摘要（原文）

> Real-time conversational assistants for procedural tasks often depend on video input, which can be computationally expensive and compromise user privacy. For the first time, we propose a real-time conversational assistant that provides comprehensive guidance for a procedural task using only lightweight privacy-preserving modalities such as audio and IMU inputs from a user's wearable device to understand the context. This assistant proactively communicates step-by-step instructions to a user performing a furniture assembly task, and answers user questions. We construct a dataset containing conversations where the assistant guides the user in performing the task. On observing that an off-the-shelf language model is a very talkative assistant, we design a novel User Whim Agnostic (UWA) LoRA finetuning method which improves the model's ability to suppress less informative dialogues, while maintaining its tendency to communicate important instructions. This leads to >30% improvement in the F-score. Finetuning the model also results in a 16x speedup by eliminating the need to provide in-context examples in the prompt. We further describe how such an assistant is implemented on edge devices with no dependence on the cloud.

