---
layout: default
title: Multi-Modal Scene Graph with Kolmogorov-Arnold Experts for Audio-Visual Question Answering
---

# Multi-Modal Scene Graph with Kolmogorov-Arnold Experts for Audio-Visual Question Answering
**arXiv**：[2511.23304v1](https://arxiv.org/abs/2511.23304) · [PDF](https://arxiv.org/pdf/2511.23304.pdf)  
**作者**：Zijian Fu, Changsheng Lv, Mengshi Qi, Huadong Ma  

**一句话要点**：提出多模态场景图与Kolmogorov-Arnold专家网络以解决音频-视觉问答中的结构建模不足问题。

**关键词**：音频-视觉问答, 多模态场景图, Kolmogorov-Arnold网络, 专家混合, 跨模态交互, 时间推理

## 3 点简述
- 核心问题：现有方法难以从复杂音频-视觉内容中提取问题相关线索，缺乏视频结构信息建模和细粒度多模态特征融合。
- 方法要点：首次引入多模态场景图显式建模对象关系，并设计基于KAN的专家混合网络增强跨模态交互的细粒度建模。
- 实验或效果：在MUSIC-AVQA和MUSIC-AVQA v2基准上实现最先进性能，代码和模型将公开。

## 摘要（原文）

> In this paper, we propose a novel Multi-Modal Scene Graph with Kolmogorov-Arnold Expert Network for Audio-Visual Question Answering (SHRIKE). The task aims to mimic human reasoning by extracting and fusing information from audio-visual scenes, with the main challenge being the identification of question-relevant cues from the complex audio-visual content. Existing methods fail to capture the structural information within video, and suffer from insufficient fine-grained modeling of multi-modal features. To address these issues, we are the first to introduce a new multi-modal scene graph that explicitly models the objects and their relationship as a visually grounded, structured representation of the audio-visual scene. Furthermore, we design a Kolmogorov-Arnold Network~(KAN)-based Mixture of Experts (MoE) to enhance the expressive power of the temporal integration stage. This enables more fine-grained modeling of cross-modal interactions within the question-aware fused audio-visual representation, leading to capture richer and more nuanced patterns and then improve temporal reasoning performance. We evaluate the model on the established MUSIC-AVQA and MUSIC-AVQA v2 benchmarks, where it achieves state-of-the-art performance. Code and model checkpoints will be publicly released.

