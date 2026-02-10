---
layout: default
title: Next Concept Prediction in Discrete Latent Space Leads to Stronger Language Models
---

# Next Concept Prediction in Discrete Latent Space Leads to Stronger Language Models
**arXiv**：[2602.08984v1](https://arxiv.org/abs/2602.08984) · [PDF](https://arxiv.org/pdf/2602.08984.pdf)  
**作者**：Yuliang Liu, Yunchong Song, Yixuan Wang, Kewen Ge, Alex Lamb, Qipeng Guo, Kai Chen, Bowen Zhou, Zhouhan Lin  

**一句话要点**：提出Next Concept Prediction以增强语言模型，通过预测多令牌概念提升预训练效果。

**关键词**：Next Concept Prediction, 语言模型预训练, Vector Quantization, 概念词汇表, 性能提升

## 3 点简述
- 核心问题：传统Next Token Prediction可能限制语言模型性能，需更挑战性预训练目标。
- 方法要点：基于Vector Quantization构建概念词汇表，结合NCP和NTP更新参数，用概念指导后续令牌生成。
- 实验或效果：在13个基准测试中，NCP带来一致性能提升，并在Llama模型上通过持续预训练进一步改进。

## 摘要（原文）

> We propose Next Concept Prediction (NCP), a generative pretraining paradigm built on top of Next Token Prediction (NTP). NCP predicts discrete concepts that span multiple tokens, thereby forming a more challenging pretraining objective. Our model, ConceptLM, quantizes hidden states using Vector Quantization and constructs a concept vocabulary. It leverages both NCP and NTP to drive parameter updates and generates a concept to guide the generation of the following tokens. We train ConceptLM from scratch at scales ranging from 70M to 1.5B parameters with up to 300B training data, including Pythia and GPT-2 backbones. Results on 13 benchmarks show that NCP yields consistent performance gains over traditional token-level models. Furthermore, continual pretraining experiments on an 8B-parameter Llama model indicate that NCP can further improve an NTP-trained model. Our analysis suggests that NCP leads to more powerful language models by introducing a harder pretraining task, providing a promising path toward better language modeling.

