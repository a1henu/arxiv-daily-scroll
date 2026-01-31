---
layout: default
title: Knowledge Vector Weakening: Efficient Training-free Unlearning for Large Vision-Language Models
---

# Knowledge Vector Weakening: Efficient Training-free Unlearning for Large Vision-Language Models
**arXiv**：[2601.21794v1](https://arxiv.org/abs/2601.21794) · [PDF](https://arxiv.org/pdf/2601.21794.pdf)  
**作者**：Yejin Kim, Dongjun Hwang, Sungmin Cha, Junsuk Choe  

**一句话要点**：提出知识向量弱化方法，以高效无训练方式实现大型视觉语言模型的知识遗忘。

**关键词**：大型视觉语言模型, 知识遗忘, 无训练方法, 计算效率, 隐私保护, 模型干预

## 3 点简述
- 核心问题：大型视觉语言模型存在隐私泄露和有害内容生成风险，现有遗忘方法依赖梯度优化，计算成本高。
- 方法要点：KVW通过识别并弱化遗忘集上激活的知识向量，直接干预模型，无需梯度计算。
- 实验或效果：在MLLMU和CLEAR基准上，KVW实现稳定遗忘-保留权衡，显著提升计算效率。

## 摘要（原文）

> Large Vision-Language Models (LVLMs) are widely adopted for their strong multimodal capabilities, yet they raise serious concerns such as privacy leakage and harmful content generation. Machine unlearning has emerged as a promising solution for removing the influence of specific data from trained models. However, existing approaches largely rely on gradient-based optimization, incurring substantial computational costs for large-scale LVLMs. To address this limitation, we propose Knowledge Vector Weakening (KVW), a training-free unlearning method that directly intervenes in the full model without gradient computation. KVW identifies knowledge vectors that are activated during the model's output generation on the forget set and progressively weakens their contributions, thereby preventing the model from exploiting undesirable knowledge. Experiments on the MLLMU and CLEAR benchmarks demonstrate that KVW achieves a stable forget-retain trade-off while significantly improving computational efficiency over gradient-based and LoRA-based unlearning methods.

