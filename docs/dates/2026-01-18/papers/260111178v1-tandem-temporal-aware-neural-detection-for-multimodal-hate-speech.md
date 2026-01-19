---
layout: default
title: TANDEM: Temporal-Aware Neural Detection for Multimodal Hate Speech
---

# TANDEM: Temporal-Aware Neural Detection for Multimodal Hate Speech
**arXiv**：[2601.11178v1](https://arxiv.org/abs/2601.11178) · [PDF](https://arxiv.org/pdf/2601.11178.pdf)  
**作者**：Girish A. Koushik, Helen Treharne, Diptesh Kanojia  

**一句话要点**：提出TANDEM框架，将视听仇恨检测转化为结构化推理问题，以提升长视频内容中仇恨言论检测的可解释性。

**关键词**：多模态仇恨检测, 时序推理, 可解释人工智能, 强化学习, 视听语言对齐

## 3 点简述
- 核心问题：现有自动化仇恨检测系统缺乏可解释性，无法提供精确时间戳和目标身份等细粒度证据。
- 方法要点：采用串联强化学习策略，通过视觉-语言和音频-语言模型的自约束跨模态上下文优化，稳定长时序推理。
- 实验或效果：在三个基准数据集上显著优于零样本和上下文增强基线，HateMM数据集目标识别F1达0.73，提升30%。

## 摘要（原文）

> Social media platforms are increasingly dominated by long-form multimodal content, where harmful narratives are constructed through a complex interplay of audio, visual, and textual cues. While automated systems can flag hate speech with high accuracy, they often function as "black boxes" that fail to provide the granular, interpretable evidence, such as precise timestamps and target identities, required for effective human-in-the-loop moderation. In this work, we introduce TANDEM, a unified framework that transforms audio-visual hate detection from a binary classification task into a structured reasoning problem. Our approach employs a novel tandem reinforcement learning strategy where vision-language and audio-language models optimize each other through self-constrained cross-modal context, stabilizing reasoning over extended temporal sequences without requiring dense frame-level supervision. Experiments across three benchmark datasets demonstrate that TANDEM significantly outperforms zero-shot and context-augmented baselines, achieving 0.73 F1 in target identification on HateMM (a 30% improvement over state-of-the-art) while maintaining precise temporal grounding. We further observe that while binary detection is robust, differentiating between offensive and hateful content remains challenging in multi-class settings due to inherent label ambiguity and dataset imbalance. More broadly, our findings suggest that structured, interpretable alignment is achievable even in complex multimodal settings, offering a blueprint for the next generation of transparent and actionable online safety moderation tools.

