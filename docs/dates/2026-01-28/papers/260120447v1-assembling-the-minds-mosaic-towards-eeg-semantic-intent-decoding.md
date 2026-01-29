---
layout: default
title: Assembling the Mind's Mosaic: Towards EEG Semantic Intent Decoding
---

# Assembling the Mind's Mosaic: Towards EEG Semantic Intent Decoding
**arXiv**：[2601.20447v1](https://arxiv.org/abs/2601.20447) · [PDF](https://arxiv.org/pdf/2601.20447.pdf)  
**作者**：Jiahe Li, Junru Chen, Fanqi Shen, Jialan Yang, Jada Li, Zhizhang Yuan, Baowen Cheng, Meng Li, Yang Yang  

**一句话要点**：提出语义意图解码框架以解决脑机接口中语义表示简化与可解释性不足的问题

**关键词**：脑机接口, 语义解码, 脑电图分析, 深度学习架构, 神经信号处理

## 3 点简述
- 核心问题：现有脑机接口框架语义表示过于简化且缺乏可解释性，阻碍自然通信
- 方法要点：引入语义意图解码，将神经活动建模为组合语义单元，通过BrainMosaic架构实现解码与重建
- 实验或效果：在多语言EEG和临床SEEG数据集上验证，相比现有框架具有显著优势

## 摘要（原文）

> Enabling natural communication through brain-computer interfaces (BCIs) remains one of the most profound challenges in neuroscience and neurotechnology. While existing frameworks offer partial solutions, they are constrained by oversimplified semantic representations and a lack of interpretability. To overcome these limitations, we introduce Semantic Intent Decoding (SID), a novel framework that translates neural activity into natural language by modeling meaning as a flexible set of compositional semantic units. SID is built on three core principles: semantic compositionality, continuity and expandability of semantic space, and fidelity in reconstruction. We present BrainMosaic, a deep learning architecture implementing SID. BrainMosaic decodes multiple semantic units from EEG/SEEG signals using set matching and then reconstructs coherent sentences through semantic-guided reconstruction. This approach moves beyond traditional pipelines that rely on fixed-class classification or unconstrained generation, enabling a more interpretable and expressive communication paradigm. Extensive experiments on multilingual EEG and clinical SEEG datasets demonstrate that SID and BrainMosaic offer substantial advantages over existing frameworks, paving the way for natural and effective BCI-mediated communication.

