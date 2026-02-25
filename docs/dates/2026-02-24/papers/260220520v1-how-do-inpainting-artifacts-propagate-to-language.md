---
layout: default
title: How Do Inpainting Artifacts Propagate to Language?
---

# How Do Inpainting Artifacts Propagate to Language?
**arXiv**：[2602.20520v1](https://arxiv.org/abs/2602.20520) · [PDF](https://arxiv.org/pdf/2602.20520.pdf)  
**作者**：Pratham Yashwante, Davit Abrahamyan, Shresth Grover, Sukruth Rao  

**一句话要点**：研究扩散修复视觉伪影如何影响视觉语言模型的语言生成

**关键词**：视觉修复伪影, 视觉语言模型, 语言生成诊断, 扩散模型, 图像描述生成

## 3 点简述
- 核心问题：扩散修复引入的视觉伪影如何传播到语言生成中
- 方法要点：采用两阶段诊断设置，比较原始与修复图像的描述生成
- 实验或效果：分析重建保真度与描述质量的关系，发现伪影导致模型行为系统性变化

## 摘要（原文）

> We study how visual artifacts introduced by diffusion-based inpainting affect language generation in vision-language models. We use a two-stage diagnostic setup in which masked image regions are reconstructed and then provided to captioning models, enabling controlled comparisons between captions generated from original and reconstructed inputs. Across multiple datasets, we analyze the relationship between reconstruction fidelity and downstream caption quality. We observe consistent associations between pixel-level and perceptual reconstruction metrics and both lexical and semantic captioning performance. Additional analysis of intermediate visual representations and attention patterns shows that inpainting artifacts lead to systematic, layer-dependent changes in model behavior. Together, these results provide a practical diagnostic framework for examining how visual reconstruction quality influences language generation in multimodal systems.

