---
layout: default
title: Bridging Your Imagination with Audio-Video Generation via a Unified Director
---

# Bridging Your Imagination with Audio-Video Generation via a Unified Director
**arXiv**：[2512.23222v1](https://arxiv.org/abs/2512.23222) · [PDF](https://arxiv.org/pdf/2512.23222.pdf)  
**作者**：Jiaxu Zhang, Tianshu Hu, Yuan Zhang, Zenan Li, Linjie Luo, Guosheng Lin, Xin Chen  

**一句话要点**：提出UniMAGE统一导演模型，通过统一脚本与关键帧生成，赋能非专家创作长上下文多镜头影片。

**关键词**：统一导演模型, 音频视频生成, 交错解耦训练, 长上下文影片, 多镜头生成, 脚本关键帧统一

## 3 点简述
- 现有AI视频创作系统将脚本起草与关键镜头设计分离，导致逻辑与想象脱节。
- 采用Mixture-of-Transformers架构，结合“先交错后解耦”训练范式，统一文本与图像生成。
- 实验显示UniMAGE在开源模型中性能领先，生成逻辑连贯脚本与视觉一致关键帧。

## 摘要（原文）

> Existing AI-driven video creation systems typically treat script drafting and key-shot design as two disjoint tasks: the former relies on large language models, while the latter depends on image generation models. We argue that these two tasks should be unified within a single framework, as logical reasoning and imaginative thinking are both fundamental qualities of a film director. In this work, we propose UniMAGE, a unified director model that bridges user prompts with well-structured scripts, thereby empowering non-experts to produce long-context, multi-shot films by leveraging existing audio-video generation models. To achieve this, we employ the Mixture-of-Transformers architecture that unifies text and image generation. To further enhance narrative logic and keyframe consistency, we introduce a ``first interleaving, then disentangling'' training paradigm. Specifically, we first perform Interleaved Concept Learning, which utilizes interleaved text-image data to foster the model's deeper understanding and imaginative interpretation of scripts. We then conduct Disentangled Expert Learning, which decouples script writing from keyframe generation, enabling greater flexibility and creativity in storytelling. Extensive experiments demonstrate that UniMAGE achieves state-of-the-art performance among open-source models, generating logically coherent video scripts and visually consistent keyframe images.

