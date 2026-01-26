---
layout: default
title: Cite-While-You-Generate: Training-Free Evidence Attribution for Multimodal Clinical Summarization
---

# Cite-While-You-Generate: Training-Free Evidence Attribution for Multimodal Clinical Summarization
**arXiv**：[2601.16397v1](https://arxiv.org/abs/2601.16397) · [PDF](https://arxiv.org/pdf/2601.16397.pdf)  
**作者**：Qianqi Yan, Huy Nguyen, Sumana Srivatsa, Hari Bandi, Xin Eric Wang, Krishnaram Kenthapadi  

**一句话要点**：提出训练免费的多模态临床摘要证据归属框架，利用解码器注意力直接引用源文本或图像。

**关键词**：临床摘要, 证据归属, 多模态注意力, 训练免费方法, 解码器注意力, 医疗AI可解释性

## 3 点简述
- 核心问题：临床摘要需透明展示生成陈述的来源，现有方法依赖后处理或重训练。
- 方法要点：基于解码器注意力实现生成时归属，支持原始图像和字幕替换两种多模态策略。
- 实验或效果：在对话和放射报告数据集上优于嵌入和自归属基线，提升文本和多模态归属准确性。

## 摘要（原文）

> Trustworthy clinical summarization requires not only fluent generation but also transparency about where each statement comes from. We propose a training-free framework for generation-time source attribution that leverages decoder attentions to directly cite supporting text spans or images, overcoming the limitations of post-hoc or retraining-based methods. We introduce two strategies for multimodal attribution: a raw image mode, which directly uses image patch attentions, and a caption-as-span mode, which substitutes images with generated captions to enable purely text-based alignment. Evaluations on two representative domains: clinician-patient dialogues (CliConSummation) and radiology reports (MIMIC-CXR), show that our approach consistently outperforms embedding-based and self-attribution baselines, improving both text-level and multimodal attribution accuracy (e.g., +15% F1 over embedding baselines). Caption-based attribution achieves competitive performance with raw-image attention while being more lightweight and practical. These findings highlight attention-guided attribution as a promising step toward interpretable and deployable clinical summarization systems.

