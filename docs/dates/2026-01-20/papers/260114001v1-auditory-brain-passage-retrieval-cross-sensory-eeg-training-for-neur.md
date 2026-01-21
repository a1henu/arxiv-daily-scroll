---
layout: default
title: Auditory Brain Passage Retrieval: Cross-Sensory EEG Training for Neural Information Retrieval
---

# Auditory Brain Passage Retrieval: Cross-Sensory EEG Training for Neural Information Retrieval
**arXiv**：[2601.14001v1](https://arxiv.org/abs/2601.14001) · [PDF](https://arxiv.org/pdf/2601.14001.pdf)  
**作者**：Niall McGuire, Yashar Moshfeghi  

**一句话要点**：提出听觉脑电通道检索方法，通过跨感官训练解决数据稀缺问题并提升神经信息检索性能。

**关键词**：脑电通道检索, 跨感官训练, 听觉脑电, 神经信息检索, 双编码器架构, 池化策略

## 3 点简述
- 核心问题：现有脑电通道检索仅依赖视觉刺激，无法支持语音界面和视障用户，且数据稀缺限制性能。
- 方法要点：使用双编码器架构和四种池化策略，比较听觉、视觉及跨感官训练在听觉和视觉脑电数据集上的效果。
- 实验或效果：听觉脑电优于视觉脑电，跨感官训练显著提升检索指标，并超越传统文本检索基线。

## 摘要（原文）

> Query formulation from internal information needs remains fundamentally challenging across all Information Retrieval paradigms due to cognitive complexity and physical impairments. Brain Passage Retrieval (BPR) addresses this by directly mapping EEG signals to passage representations without intermediate text translation. However, existing BPR research exclusively uses visual stimuli, leaving critical questions unanswered: Can auditory EEG enable effective retrieval for voice-based interfaces and visually impaired users? Can training on combined EEG datasets from different sensory modalities improve performance despite severe data scarcity? We present the first systematic investigation of auditory EEG for BPR and evaluate cross-sensory training benefits. Using dual encoder architectures with four pooling strategies (CLS, mean, max, multi-vector), we conduct controlled experiments comparing auditory-only, visual-only, and combined training on the Alice (auditory) and Nieuwland (visual) datasets. Results demonstrate that auditory EEG consistently outperforms visual EEG, and cross-sensory training with CLS pooling achieves substantial improvements over individual training: 31% in MRR (0.474), 43% in Hit@1 (0.314), and 28% in Hit@10 (0.858). Critically, combined auditory EEG models surpass BM25 text baselines (MRR: 0.474 vs 0.428), establishing neural queries as competitive with traditional retrieval whilst enabling accessible interfaces. These findings validate auditory neural interfaces for IR tasks and demonstrate that cross-sensory training addresses data scarcity whilst outperforming single-modality approaches Code: https://github.com/NiallMcguire/Audio_BPR

