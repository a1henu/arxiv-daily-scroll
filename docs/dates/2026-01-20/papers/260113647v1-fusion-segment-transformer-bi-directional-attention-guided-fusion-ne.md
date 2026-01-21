---
layout: default
title: Fusion Segment Transformer: Bi-Directional Attention Guided Fusion Network for AI-Generated Music Detection
---

# Fusion Segment Transformer: Bi-Directional Attention Guided Fusion Network for AI-Generated Music Detection
**arXiv**：[2601.13647v1](https://arxiv.org/abs/2601.13647) · [PDF](https://arxiv.org/pdf/2601.13647.pdf)  
**作者**：Yumin Kim, Seonghyeon Go  

**一句话要点**：提出融合段变换器以解决全音频AI生成音乐检测中的长期上下文建模问题

**关键词**：AI生成音乐检测, 段变换器, 门控融合层, 全音频分析, 长期上下文建模

## 3 点简述
- 核心问题：现有方法主要针对短音频，全音频检测需建模长期结构和上下文，挑战未充分探索。
- 方法要点：改进段变换器，引入门控融合层，有效整合内容和结构信息，捕捉长期上下文。
- 实验或效果：在SONICS和AIME数据集上超越先前模型和基线，实现最先进的检测性能。

## 摘要（原文）

> With the rise of generative AI technology, anyone can now easily create and deploy AI-generated music, which has heightened the need for technical solutions to address copyright and ownership issues. While existing works mainly focused on short-audio, the challenge of full-audio detection, which requires modeling long-term structure and context, remains insufficiently explored. To address this, we propose an improved version of the Segment Transformer, termed the Fusion Segment Transformer. As in our previous work, we extract content embeddings from short music segments using diverse feature extractors. Furthermore, we enhance the architecture for full-audio AI-generated music detection by introducing a Gated Fusion Layer that effectively integrates content and structural information, enabling the capture of long-term context. Experiments on the SONICS and AIME datasets show that our approach outperforms the previous model and recent baselines, achieving state-of-the-art results in AI-generated music detection.

