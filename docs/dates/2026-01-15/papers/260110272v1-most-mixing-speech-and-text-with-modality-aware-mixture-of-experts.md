---
layout: default
title: MoST: Mixing Speech and Text with Modality-Aware Mixture of Experts
---

# MoST: Mixing Speech and Text with Modality-Aware Mixture of Experts
**arXiv**：[2601.10272v1](https://arxiv.org/abs/2601.10272) · [PDF](https://arxiv.org/pdf/2601.10272.pdf)  
**作者**：Yuxuan Lou, Kai Yang, Yang You  

**一句话要点**：提出MoST模型，通过模态感知专家混合架构无缝集成语音与文本处理。

**关键词**：语音文本集成, 模态感知专家混合, 多模态大语言模型, 开源数据集, ASR与TTS, 跨模态理解

## 3 点简述
- 核心问题：现有多模态模型用相同参数处理不同模态，忽略其表示差异。
- 方法要点：引入模态感知专家混合架构，包含模态特定专家组和共享专家，增强模态特定学习与跨模态理解。
- 实验或效果：在ASR、TTS、音频语言建模和口语问答基准上，性能优于参数规模相近的现有模型。

## 摘要（原文）

> We present MoST (Mixture of Speech and Text), a novel multimodal large language model that seamlessly integrates speech and text processing through our proposed Modality-Aware Mixture of Experts (MAMoE) architecture. While current multimodal models typically process diverse modality representations with identical parameters, disregarding their inherent representational differences, we introduce specialized routing pathways that direct tokens to modality-appropriate experts based on input type. MAMoE simultaneously enhances modality-specific learning and cross-modal understanding through two complementary components: modality-specific expert groups that capture domain-specific patterns and shared experts that facilitate information transfer between modalities. Building on this architecture, we develop an efficient transformation pipeline that adapts the pretrained MoE language model through strategic post-training on ASR and TTS datasets, followed by fine-tuning with a carefully curated speech-text instruction dataset. A key feature of this pipeline is that it relies exclusively on fully accessible, open-source datasets to achieve strong performance and data efficiency. Comprehensive evaluations across ASR, TTS, audio language modeling, and spoken question answering benchmarks show that MoST consistently outperforms existing models of comparable parameter counts. Our ablation studies confirm that the modality-specific routing mechanism and shared experts design significantly contribute to performance gains across all tested domains. To our knowledge, MoST represents the first fully open-source speech-text LLM built on a Mixture of Experts architecture. \footnote{We release MoST model, training code, inference code, and training data at https://github.com/NUS-HPC-AI-Lab/MoST

