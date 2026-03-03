---
layout: default
title: Nano-EmoX: Unifying Multimodal Emotional Intelligence from Perception to Empathy
---

# Nano-EmoX: Unifying Multimodal Emotional Intelligence from Perception to Empathy
**arXiv**：[2603.02123v1](https://arxiv.org/abs/2603.02123) · [PDF](https://arxiv.org/pdf/2603.02123.pdf)  
**作者**：Jiahao Huang, Fengyan Lin, Xuechao Yang, Chen Feng, Kexin Zhu, Xu Yang, Zhide Chen  

**一句话要点**：提出Nano-EmoX多模态情感模型和P2E训练框架，以统一情感智能从感知到共情的任务。

**关键词**：情感多模态模型, 认知层次架构, 全模态编码器, 课程学习训练, 轻量语言模型, 情感任务统一

## 3 点简述
- 核心问题：情感多模态模型存在感知与交互间的鸿沟，导致能力碎片化和泛化受限。
- 方法要点：基于认知层次设计三阶段架构，集成全模态编码器和异质适配器，通过课程学习框架P2E训练。
- 实验或效果：在2.2B参数下统一六项核心情感任务，在多个基准上达到先进或竞争性能，展示高效泛化。

## 摘要（原文）

> The development of affective multimodal language models (MLMs) has long been constrained by a gap between low-level perception and high-level interaction, leading to fragmented affective capabilities and limited generalization. To bridge this gap, we propose a cognitively inspired three-level hierarchy that organizes affective tasks according to their cognitive depth-perception, understanding, and interaction-and provides a unified conceptual foundation for advancing affective modeling. Guided by this hierarchy, we introduce Nano-EmoX, a small-scale multitask MLM, and P2E (Perception-to-Empathy), a curriculum-based training framework. Nano-EmoX integrates a suite of omni-modal encoders, including an enhanced facial encoder and a fusion encoder, to capture key multimodal affective cues and improve cross-task transferability. The outputs are projected into a unified language space via heterogeneous adapters, empowering a lightweight language model to tackle diverse affective tasks. Concurrently, P2E progressively cultivates emotional intelligence by aligning rapid perception with chain-of-thought-driven empathy. To the best of our knowledge, Nano-EmoX is the first compact MLM (2.2B) to unify six core affective tasks across all three hierarchy levels, achieving state-of-the-art or highly competitive performance across multiple benchmarks, demonstrating excellent efficiency and generalization.

