---
layout: default
title: Spatial Audio Question Answering and Reasoning on Dynamic Source Movements
---

# Spatial Audio Question Answering and Reasoning on Dynamic Source Movements
**arXiv**：[2602.16334v1](https://arxiv.org/abs/2602.16334) · [PDF](https://arxiv.org/pdf/2602.16334.pdf)  
**作者**：Arvind Krishna Sridhar, Yinyi Guo, Erik Visser  

**一句话要点**：提出空间音频问答与运动推理方法，通过增强框架和思维模式提升动态声源理解。

**关键词**：空间音频问答, 运动推理, 音频增强, 多模态学习, 源分离

## 3 点简述
- 研究空间音频问答，聚焦从立体音频推断声源运动、位置和方向变化。
- 引入运动中心的空间音频增强框架，合成多样运动模式以生成可控训练数据。
- 提出端到端多模态微调方法，结合思维模式提升推理，实验显示分离与推理协同增效。

## 摘要（原文）

> Spatial audio understanding aims to enable machines to interpret complex auditory scenes, particularly when sound sources move over time. In this work, we study Spatial Audio Question Answering (Spatial AQA) with a focus on movement reasoning, where a model must infer object motion, position, and directional changes directly from stereo audio. First, we introduce a movement-centric spatial audio augmentation framework that synthesizes diverse motion patterns from isolated mono audio events, enabling controlled and scalable training data generation. Second, we propose an end-to-end multimodal finetuning approach with a thinking mode, which allows audio-language models to produce explicit intermediate reasoning steps before predicting an answer. Third, we investigate the impact of query-conditioned source separation as a preprocessing stage and compare three inference regimes: no masking, an audio grounding model (AGM), and ground-truth masks. Our results show that reasoning amplifies the benefits of source separation, with thinking mode showing significant improvement of +5.1% when a single event is present in the question. These findings highlight the interplay between movement modeling, reasoning, and separation quality, offering new insights for advancing spatial audio understanding.

