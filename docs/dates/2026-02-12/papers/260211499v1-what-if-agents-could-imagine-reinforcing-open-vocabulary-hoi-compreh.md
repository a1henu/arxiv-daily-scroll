---
layout: default
title: What if Agents Could Imagine? Reinforcing Open-Vocabulary HOI Comprehension through Generation
---

# What if Agents Could Imagine? Reinforcing Open-Vocabulary HOI Comprehension through Generation
**arXiv**：[2602.11499v1](https://arxiv.org/abs/2602.11499) · [PDF](https://arxiv.org/pdf/2602.11499.pdf)  
**作者**：Zhenlong Yuan, Xiangyan Qu, Jing Tang, Rui Chen, Lei Sun, Ruidong Chen, Hongwei Yu, Chengxuan Qian, Xiangxiang Chu, Shuo Li, Yuyin Zhou  

**一句话要点**：提出ImagineAgent框架，通过生成式想象增强开放词汇人-物交互理解

**关键词**：开放词汇人-物交互, 多模态大语言模型, 认知图, 工具调用, 扩散模型, 检索增强

## 3 点简述
- 核心问题：多模态大语言模型在开放词汇人-物交互中存在跨模态幻觉和遮挡模糊问题
- 方法要点：构建认知图建模实体关系，动态调用检索、裁剪、扩散等工具获取证据
- 实验或效果：在SWIG-HOI和HICO-DET上实现SOTA，仅需约20%训练数据

## 摘要（原文）

> Multimodal Large Language Models have shown promising capabilities in bridging visual and textual reasoning, yet their reasoning capabilities in Open-Vocabulary Human-Object Interaction (OV-HOI) are limited by cross-modal hallucinations and occlusion-induced ambiguity. To address this, we propose \textbf{ImagineAgent}, an agentic framework that harmonizes cognitive reasoning with generative imagination for robust visual understanding. Specifically, our method innovatively constructs cognitive maps that explicitly model plausible relationships between detected entities and candidate actions. Subsequently, it dynamically invokes tools including retrieval augmentation, image cropping, and diffusion models to gather domain-specific knowledge and enriched visual evidence, thereby achieving cross-modal alignment in ambiguous scenarios. Moreover, we propose a composite reward that balances prediction accuracy and tool efficiency. Evaluations on SWIG-HOI and HICO-DET datasets demonstrate our SOTA performance, requiring approximately 20\% of training data compared to existing methods, validating our robustness and efficiency.

