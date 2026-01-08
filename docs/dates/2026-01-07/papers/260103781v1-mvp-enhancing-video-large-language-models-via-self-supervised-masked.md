---
layout: default
title: MVP: Enhancing Video Large Language Models via Self-supervised Masked Video Prediction
---

# MVP: Enhancing Video Large Language Models via Self-supervised Masked Video Prediction
**arXiv**：[2601.03781v1](https://arxiv.org/abs/2601.03781) · [PDF](https://arxiv.org/pdf/2601.03781.pdf)  
**作者**：Xiaokun Sun, Zezhong Wu, Zewen Ding, Linli Xu  

**一句话要点**：提出掩码视频预测以增强视频大语言模型的时序推理能力

**关键词**：视频大语言模型, 掩码视频预测, 时序推理, 自监督学习, 强化学习后训练

## 3 点简述
- 问题：现有视频大语言模型缺乏对时序连贯性和帧间相关性的显式监督，限制动态和因果理解
- 方法：引入掩码视频预测目标，通过重构掩码连续片段强制模型关注序列逻辑和时序上下文
- 效果：综合评估显示MVP直接强化时序推理和因果理解，提升视频推理能力

## 摘要（原文）

> Reinforcement learning based post-training paradigms for Video Large Language Models (VideoLLMs) have achieved significant success by optimizing for visual-semantic tasks such as captioning or VideoQA. However, while these approaches effectively enhance perception abilities, they primarily target holistic content understanding, often lacking explicit supervision for intrinsic temporal coherence and inter-frame correlations. This tendency limits the models' ability to capture intricate dynamics and fine-grained visual causality. To explicitly bridge this gap, we propose a novel post-training objective: Masked Video Prediction (MVP). By requiring the model to reconstruct a masked continuous segment from a set of challenging distractors, MVP forces the model to attend to the sequential logic and temporal context of events. To support scalable training, we introduce a scalable data synthesis pipeline capable of transforming arbitrary video corpora into MVP training samples, and further employ Group Relative Policy Optimization (GRPO) with a fine-grained reward function to enhance the model's understanding of video context and temporal properties. Comprehensive evaluations demonstrate that MVP enhances video reasoning capabilities by directly reinforcing temporal reasoning and causal understanding.

