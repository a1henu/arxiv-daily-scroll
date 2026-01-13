---
layout: default
title: A Unified Framework for Emotion Recognition and Sentiment Analysis via Expert-Guided Multimodal Fusion with Large Language Models
---

# A Unified Framework for Emotion Recognition and Sentiment Analysis via Expert-Guided Multimodal Fusion with Large Language Models
**arXiv**：[2601.07565v1](https://arxiv.org/abs/2601.07565) · [PDF](https://arxiv.org/pdf/2601.07565.pdf)  
**作者**：Jiaqi Qiao, Xiujuan Xu, Xinran Li, Yu Liu  

**一句话要点**：提出专家引导多模态融合框架EGMF，结合大语言模型统一处理情感识别与情感分析。

**关键词**：多模态情感理解, 专家引导融合, 大语言模型集成, 分层动态门控, 跨语言鲁棒性, LoRA微调

## 3 点简述
- 核心问题：多模态情感理解需有效整合文本、音频和视觉信息，处理离散情感识别和连续情感分析。
- 方法要点：通过三个专家网络（细粒度局部、语义关联、全局上下文）和分层动态门控，自适应融合特征，并利用大语言模型生成自然语言处理分类与回归任务。
- 实验或效果：在双语基准测试中优于现有方法，展示跨语言鲁棒性，揭示中英文多模态情感表达的通用模式。

## 摘要（原文）

> Multimodal emotion understanding requires effective integration of text, audio, and visual modalities for both discrete emotion recognition and continuous sentiment analysis. We present EGMF, a unified framework combining expert-guided multimodal fusion with large language models. Our approach features three specialized expert networks--a fine-grained local expert for subtle emotional nuances, a semantic correlation expert for cross-modal relationships, and a global context expert for long-range dependencies--adaptively integrated through hierarchical dynamic gating for context-aware feature selection. Enhanced multimodal representations are integrated with LLMs via pseudo token injection and prompt-based conditioning, enabling a single generative framework to handle both classification and regression through natural language generation. We employ LoRA fine-tuning for computational efficiency. Experiments on bilingual benchmarks (MELD, CHERMA, MOSEI, SIMS-V2) demonstrate consistent improvements over state-of-the-art methods, with superior cross-lingual robustness revealing universal patterns in multimodal emotional expressions across English and Chinese. We will release the source code publicly.

