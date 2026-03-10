---
layout: default
title: Disentangling Reasoning in Large Audio-Language Models for Ambiguous Emotion Prediction
---

# Disentangling Reasoning in Large Audio-Language Models for Ambiguous Emotion Prediction
**arXiv**：[2603.08230v1](https://arxiv.org/abs/2603.08230) · [PDF](https://arxiv.org/pdf/2603.08230.pdf)  
**作者**：Xiaofeng Yu, Jiaheng Dong, Jean Honorio, Abhirup Ghosh, Hong Jia, Ting Dang  

**一句话要点**：提出分布推理框架以解决大音频语言模型在模糊情感预测中的推理能力不足问题

**关键词**：语音情感识别, 模糊情感预测, 大音频语言模型, 分布推理, 链式思维监督, 训练策略优化

## 3 点简述
- 核心问题：现有语音情感识别方法常预测单一标签，忽略了人类情感表达的模糊性，大音频语言模型在此方面的推理能力有限。
- 方法要点：将模糊情感识别重构为分布推理问题，引入模糊感知目标和结构化链式思维监督，以对齐人类感知分布并引导情感线索推理。
- 实验或效果：在IEMOCAP和CREMA-D数据集上，通过SFT、DPO和GRPO训练策略验证了方法的持续改进效果。

## 摘要（原文）

> Speech emotion recognition plays an important role in various applications. However, most existing approaches predict a single emotion label, oversimplifying the inherently ambiguous nature of human emotional expression. Recent large audio-language models show promise in generating richer outputs, but their reasoning ability for ambiguous emotional understanding remains limited. In this work, we reformulate ambiguous emotion recognition as a distributional reasoning problem and present the first systematic study of ambiguity-aware reasoning in LALMs. Our framework comprises two complementary components: an ambiguity-aware objective that aligns predictions with human perceptual distributions, and a structured ambiguity-aware chain-of-thought supervision that guides reasoning over emotional cues. Experiments on IEMOCAP and CREMA-D demonstrate consistent improvements across SFT, DPO, and GRPO training strategies.

