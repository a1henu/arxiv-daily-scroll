---
layout: default
title: LAP: A Language-Aware Planning Model For Procedure Planning In Instructional Videos
---

# LAP: A Language-Aware Planning Model For Procedure Planning In Instructional Videos
**arXiv**：[2603.09743v1](https://arxiv.org/abs/2603.09743) · [PDF](https://arxiv.org/pdf/2603.09743.pdf)  
**作者**：Lei Shi, Victor Aregbede, Andreas Persson, Martin Längkvist, Amy Loutfi, Stephanie Lowry  

**一句话要点**：提出语言感知规划模型LAP，利用语言描述解决教学视频中程序规划的视觉模糊性问题。

**关键词**：程序规划, 教学视频, 视觉语言模型, 扩散模型, 文本嵌入, 动作序列预测

## 3 点简述
- 核心问题：现有方法依赖视觉观察，难以区分视觉相似的不同动作，导致规划模糊。
- 方法要点：使用微调视觉语言模型将视觉观察转为文本描述，提取文本嵌入，结合扩散模型规划动作序列。
- 实验或效果：在CrossTask、Coin和NIV基准上取得显著领先性能，验证语言感知规划的优势。

## 摘要（原文）

> Procedure planning requires a model to predict a sequence of actions that transform a start visual observation into a goal in instructional videos. While most existing methods rely primarily on visual observations as input, they often struggle with the inherent ambiguity where different actions can appear visually similar. In this work, we argue that language descriptions offer a more distinctive representation in the latent space for procedure planning. We introduce Language-Aware Planning (LAP), a novel method that leverages the expressiveness of language to bridge visual observation and planning. LAP uses a finetuned Vision Language Model (VLM) to translate visual observations into text descriptions and to predict actions and extract text embeddings. These text embeddings are more distinctive than visual embeddings and are used in a diffusion model for planning action sequences. We evaluate LAP on three procedure planning benchmarks: CrossTask, Coin, and NIV. LAP achieves new state-of-the-art performance across multiple metrics and time horizons by large margin, demonstrating the significant advantage of language-aware planning.

