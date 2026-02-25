---
layout: default
title: Inner Speech as Behavior Guides: Steerable Imitation of Diverse Behaviors for Human-AI coordination
---

# Inner Speech as Behavior Guides: Steerable Imitation of Diverse Behaviors for Human-AI coordination
**arXiv**：[2602.20517v1](https://arxiv.org/abs/2602.20517) · [PDF](https://arxiv.org/pdf/2602.20517.pdf)  
**作者**：Rakshit Trivedi, Kartik Sharma, David C Parkes  

**一句话要点**：提出MIMIC框架，利用语言作为行为意图内部表示，以增强人机协调中行为多样性与可引导性。

**关键词**：模仿学习, 人机协调, 内部语音, 视觉语言模型, 行为引导, 扩散策略

## 3 点简述
- 核心问题：现有模仿学习方法难以捕捉人类行为多样性和非马尔可夫性，且推理时缺乏行为引导能力。
- 方法要点：基于人类认知理论，使用视觉语言模型训练条件变分自编码器生成内部语音，结合扩散策略实现行为克隆。
- 实验或效果：在机器人操作和人机协作任务中，显著提升行为多样性和保真度，无需额外演示即可实现精细行为引导。

## 摘要（原文）

> Effective human-AI coordination requires artificial agents capable of exhibiting and responding to human-like behaviors while adapting to changing contexts. Imitation learning has emerged as one of the prominent approaches to build such agents by training them to mimic human-demonstrated behaviors. However, current methods struggle to capture the inherent diversity and non-Markovian nature of human behavior and lack the ability to steer behavior at inference time. Drawing inspiration from the theory of human cognitive processes, where inner speech guides action selection before execution, we propose MIMIC (Modeling Inner Motivations for Imitation and Control), a framework that uses language as an internal representation of behavioral intent. MIMIC employs the novel use of vision-language models as linguistic scaffolding to train a conditional variational autoencoder capable of generating inner speech from observations. A diffusion-based behavior cloning policy then selects actions conditioned on current observations and the generated inner speech. MIMIC enables fine-grained steering of behavior at inference time by conditioning the agent on behavior-specific speech. Experiments across robotic manipulation tasks and human-AI collaboration games demonstrate that MIMIC significantly enhances both behavior diversity and fidelity to human demonstrations while enabling nuanced behavioral steering without training on additional demonstrations. We open source our code and provide pre-trained MIMIC agents and qualitative demos at: https://mimic-research.github.io.

