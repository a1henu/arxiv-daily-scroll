---
layout: default
title: Mull-Tokens: Modality-Agnostic Latent Thinking
---

# Mull-Tokens: Modality-Agnostic Latent Thinking
**arXiv**：[2512.10941v1](https://arxiv.org/abs/2512.10941) · [PDF](https://arxiv.org/pdf/2512.10941.pdf)  
**作者**：Arijit Ray, Ahmed Abdelkader, Chengzhi Mao, Bryan A. Plummer, Kate Saenko, Ranjay Krishna, Leonidas Guibas, Wen-Sheng Chu  

**一句话要点**：提出Mull-Tokens模态无关潜在令牌，以支持多模态自由推理，提升空间推理任务性能。

**关键词**：多模态推理, 潜在令牌, 空间推理, 模态无关表示, 无监督微调

## 3 点简述
- 核心问题：现有多模态模型依赖工具或图像生成，推理脆弱且难以扩展。
- 方法要点：预训练模态无关潜在令牌，通过监督和非监督微调实现跨模态中间信息表示。
- 实验或效果：在四个空间推理基准上平均提升3%，推理密集型任务最高提升16%。

## 摘要（原文）

> Reasoning goes beyond language; the real world requires reasoning about space, time, affordances, and much more that words alone cannot convey. Existing multimodal models exploring the potential of reasoning with images are brittle and do not scale. They rely on calling specialist tools, costly generation of images, or handcrafted reasoning data to switch between text and image thoughts. Instead, we offer a simpler alternative -- Mull-Tokens -- modality-agnostic latent tokens pre-trained to hold intermediate information in either image or text modalities to let the model think free-form towards the correct answer. We investigate best practices to train Mull-Tokens inspired by latent reasoning frameworks. We first train Mull-Tokens using supervision from interleaved text-image traces, and then fine-tune without any supervision by only using the final answers. Across four challenging spatial reasoning benchmarks involving tasks such as solving puzzles and taking different perspectives, we demonstrate that Mull-Tokens improve upon several baselines utilizing text-only reasoning or interleaved image-text reasoning, achieving a +3% average improvement and up to +16% on a puzzle solving reasoning-heavy split compared to our strongest baseline. Adding to conversations around challenges in grounding textual and visual reasoning, Mull-Tokens offers a simple solution to abstractly think in multiple modalities.

