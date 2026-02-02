---
layout: default
title: FNF: Functional Network Fingerprint for Large Language Models
---

# FNF: Functional Network Fingerprint for Large Language Models
**arXiv**：[2601.22692v1](https://arxiv.org/abs/2601.22692) · [PDF](https://arxiv.org/pdf/2601.22692.pdf)  
**作者**：Yiheng Liu, Junhao Ning, Sichen Xia, Haiyang Sun, Yang Yang, Hanyang Chi, Xiaohui Gao, Ning Qiang, Bao Ge, Junwei Han, Xintao Hu  

**一句话要点**：提出功能性网络指纹以检测大语言模型的知识产权归属

**关键词**：大语言模型, 知识产权保护, 功能性网络, 模型指纹, 样本高效, 鲁棒性验证

## 3 点简述
- 核心问题：保护开源大语言模型的知识产权，防止未经授权的模型盗用
- 方法要点：基于功能性网络活动一致性，无需训练，样本高效，验证模型来源
- 实验或效果：对微调、剪枝等修改鲁棒，跨架构和维度有效，代码已开源

## 摘要（原文）

> The development of large language models (LLMs) is costly and has significant commercial value. Consequently, preventing unauthorized appropriation of open-source LLMs and protecting developers' intellectual property rights have become critical challenges. In this work, we propose the Functional Network Fingerprint (FNF), a training-free, sample-efficient method for detecting whether a suspect LLM is derived from a victim model, based on the consistency between their functional network activity. We demonstrate that models that share a common origin, even with differences in scale or architecture, exhibit highly consistent patterns of neuronal activity within their functional networks across diverse input samples. In contrast, models trained independently on distinct data or with different objectives fail to preserve such activity alignment. Unlike conventional approaches, our method requires only a few samples for verification, preserves model utility, and remains robust to common model modifications (such as fine-tuning, pruning, and parameter permutation), as well as to comparisons across diverse architectures and dimensionalities. FNF thus provides model owners and third parties with a simple, non-invasive, and effective tool for protecting LLM intellectual property. The code is available at https://github.com/WhatAboutMyStar/LLM_ACTIVATION.

