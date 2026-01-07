---
layout: default
title: Decentralized Autoregressive Generation
---

# Decentralized Autoregressive Generation
**arXiv**：[2601.03184v1](https://arxiv.org/abs/2601.03184) · [PDF](https://arxiv.org/pdf/2601.03184.pdf)  
**作者**：Stepan Maschan, Haoxuan Qu, Jun Liu  

**一句话要点**：提出去中心化自回归生成理论，通过专家流组合定义目标，验证多模态模型训练等效性。

**关键词**：自回归生成, 去中心化训练, 离散流匹配, 多模态语言模型, 理论分析

## 3 点简述
- 核心问题：分析自回归生成过程的去中心化理论框架。
- 方法要点：定义去中心化离散流匹配目标，将概率生成速度表达为专家流的线性组合。
- 实验或效果：在多样化基准上，验证去中心化与中心化训练在多模态语言模型中的等效性。

## 摘要（原文）

> We present a theoretical analysis of decentralization of autoregressive generation. We define the Decentralized Discrete Flow Matching objective, by expressing probability generating velocity as a linear combination of expert flows. We also conduct experiments demonstrat- ing the equivalence between decentralized and centralized training settings for multimodal language models across diverse set of benchmarks. Specifically, we compare two distinct paradigms: LLaVA and InternVL 2.5-1B, which uses a fixed CLIP vision encoder and per- forms full-parameter fine-tuning (ViT+MLP+LLM) during the instruction tuning stage.

