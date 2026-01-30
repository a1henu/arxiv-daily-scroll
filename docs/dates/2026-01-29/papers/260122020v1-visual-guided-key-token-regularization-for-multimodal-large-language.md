---
layout: default
title: Visual-Guided Key-Token Regularization for Multimodal Large Language Model Unlearning
---

# Visual-Guided Key-Token Regularization for Multimodal Large Language Model Unlearning
**arXiv**：[2601.22020v1](https://arxiv.org/abs/2601.22020) · [PDF](https://arxiv.org/pdf/2601.22020.pdf)  
**作者**：Chengyi Cai, Zesheng Ye, Peike Li, Bo Han, Jianzhong Qi, Feng Liu  

**一句话要点**：提出视觉引导关键令牌正则化方法，以解决多模态大语言模型遗忘中令牌重要性不均和视觉线索忽略的问题。

**关键词**：多模态大语言模型, 模型遗忘, 视觉引导正则化, 令牌级优化, 信息熵, 梯度重加权

## 3 点简述
- 核心问题：现有多模态大语言模型遗忘方法忽视答案令牌重要性差异和视觉模态线索，导致遗忘效果不佳。
- 方法要点：利用无关视觉输入预测理想令牌分布，通过信息熵定义关键令牌，并采用梯度重加权优先更新关键令牌。
- 实验或效果：在MLLMU和CLEAR基准测试中，有效执行遗忘，减轻遗忘并保持响应连贯性。

## 摘要（原文）

> Unlearning in Multimodal Large Language Models (MLLMs) prevents the model from revealing private information when queried about target images. Existing MLLM unlearning methods largely adopt approaches developed for LLMs. They treat all answer tokens uniformly, disregarding their varying importance in the unlearning process. Moreover, these methods focus exclusively on the language modality, disregarding visual cues that indicate key tokens in answers. In this paper, after formulating the problem of unlearning in multimodal question answering for MLLMs, we propose Visual-Guided Key-Token Regularization (ViKeR). We leverage irrelevant visual inputs to predict ideal post-unlearning token-level distributions and use these distributions to regularize the unlearning process, thereby prioritizing key tokens. Further, we define key tokens in unlearning via information entropy and discuss ViKeR's effectiveness through token-level gradient reweighting, which amplifies updates on key tokens. Experiments on MLLMU and CLEAR benchmarks demonstrate that our method effectively performs unlearning while mitigating forgetting and maintaining response coherence.

