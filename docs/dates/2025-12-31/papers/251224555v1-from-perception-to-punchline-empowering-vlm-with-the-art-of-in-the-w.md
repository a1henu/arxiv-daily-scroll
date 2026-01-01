---
layout: default
title: From Perception to Punchline: Empowering VLM with the Art of In-the-wild Meme
---

# From Perception to Punchline: Empowering VLM with the Art of In-the-wild Meme
**arXiv**：[2512.24555v1](https://arxiv.org/abs/2512.24555) · [PDF](https://arxiv.org/pdf/2512.24555.pdf)  
**作者**：Xueyan Li, Yingyi Xue, Mengjie Jiang, Qingzi Zhu, Yazhe Niu  

**一句话要点**：提出HUMOR框架，通过分层推理与群体偏好对齐，提升视觉语言模型在开放域幽默表情包生成中的性能。

**关键词**：幽默表情包生成, 视觉语言模型, 分层推理, 群体偏好对齐, 开放域多模态生成

## 3 点简述
- 核心问题：幽默表情包生成需超越直接监督，融合视觉感知、上下文线索和主观幽默推理。
- 方法要点：采用分层多路径思维链增强推理多样性，并基于模板内群体训练成对奖励模型以对齐人类偏好。
- 实验或效果：实验表明HUMOR能提升多种视觉语言模型的推理多样性、偏好对齐可靠性和整体生成质量。

## 摘要（原文）

> Generating humorous memes is a challenging multimodal task that moves beyond direct image-to-caption supervision. It requires a nuanced reasoning over visual content, contextual cues, and subjective humor. To bridge this gap between visual perception and humorous punchline creation, we propose HUMOR}, a novel framework that guides VLMs through hierarchical reasoning and aligns them with group-wise human preferences. First, HUMOR employs a hierarchical, multi-path Chain-of-Thought (CoT): the model begins by identifying a template-level intent, then explores diverse reasoning paths under different contexts, and finally anchors onto a high-quality, context-specific path. This CoT supervision, which traces back from ground-truth captions, enhances reasoning diversity. We further analyze that this multi-path exploration with anchoring maintains a high expected humor quality, under the practical condition that high-quality paths retain significant probability mass. Second, to capture subjective humor, we train a pairwise reward model that operates within groups of memes sharing the same template. Following established theory, this approach ensures a consistent and robust proxy for human preference, even with subjective and noisy labels. The reward model then enables a group-wise reinforcement learning optimization, guaranteeing providing a theoretical guarantee for monotonic improvement within the trust region. Extensive experiments show that HUMOR empowers various VLMs with superior reasoning diversity, more reliable preference alignment, and higher overall meme quality. Beyond memes, our work presents a general training paradigm for open-ended, human-aligned multimodal generation, where success is guided by comparative judgment within coherent output group.

