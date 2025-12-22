---
layout: default
title: Confidence-Credibility Aware Weighted Ensembles of Small LLMs Outperform Large LLMs in Emotion Detection
---

# Confidence-Credibility Aware Weighted Ensembles of Small LLMs Outperform Large LLMs in Emotion Detection
**arXiv**：[2512.17630v1](https://arxiv.org/abs/2512.17630) · [PDF](https://arxiv.org/pdf/2512.17630.pdf)  
**作者**：Menna Elgabry, Ali Hamdi  

**一句话要点**：提出置信度-可信度加权集成框架，在情感检测任务中超越大型语言模型。

**关键词**：情感检测, 模型集成, 置信度加权, 可信度评估, 参数效率, Transformer模型

## 3 点简述
- 核心问题：传统集成方法依赖同质架构，可能缺乏错误多样性，影响情感检测性能。
- 方法要点：结合架构多样的小型Transformer模型，采用双权重投票机制，动态加权模型贡献。
- 实验效果：在DAIR-AI数据集上实现93.5%宏F1分数，优于大型模型，参数效率更高。

## 摘要（原文）

> This paper introduces a confidence-weighted, credibility-aware ensemble framework for text-based emotion detection, inspired by Condorcet's Jury Theorem (CJT). Unlike conventional ensembles that often rely on homogeneous architectures, our approach combines architecturally diverse small transformer-based large language models (sLLMs) - BERT, RoBERTa, DistilBERT, DeBERTa, and ELECTRA, each fully fine-tuned for emotion classification. To preserve error diversity, we minimize parameter convergence while taking advantage of the unique biases of each model. A dual-weighted voting mechanism integrates both global credibility (validation F1 score) and local confidence (instance-level probability) to dynamically weight model contributions. Experiments on the DAIR-AI dataset demonstrate that our credibility-confidence ensemble achieves a macro F1 score of 93.5 percent, surpassing state-of-the-art benchmarks and significantly outperforming large-scale LLMs, including Falcon, Mistral, Qwen, and Phi, even after task-specific Low-Rank Adaptation (LoRA). With only 595M parameters in total, our small LLMs ensemble proves more parameter-efficient and robust than models up to 7B parameters, establishing that carefully designed ensembles of small, fine-tuned models can outperform much larger LLMs in specialized natural language processing (NLP) tasks such as emotion detection.

