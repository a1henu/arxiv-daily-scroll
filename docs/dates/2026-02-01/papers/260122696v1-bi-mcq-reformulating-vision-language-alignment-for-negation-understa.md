---
layout: default
title: Bi-MCQ: Reformulating Vision-Language Alignment for Negation Understanding
---

# Bi-MCQ: Reformulating Vision-Language Alignment for Negation Understanding
**arXiv**：[2601.22696v1](https://arxiv.org/abs/2601.22696) · [PDF](https://arxiv.org/pdf/2601.22696.pdf)  
**作者**：Tae Hun Kim, Hyun Gyu Lee  

**一句话要点**：提出Bi-MCQ框架，通过条件语义比较增强医学视觉语言模型对否定陈述的理解能力。

**关键词**：视觉语言模型, 否定理解, 医学图像分析, 条件语义比较, 双向学习

## 3 点简述
- 现有视觉语言模型在医学图像分析中难以理解否定陈述，因对比对齐目标将否定视为次要语言变化。
- Bi-MCQ将视觉语言对齐重构为条件语义比较问题，通过双向多项选择学习框架联合训练图像到文本和文本到图像任务。
- 在多个医学数据集上，Bi-MCQ显著提升否定理解性能，减少肯定与否定之间的性能差距。

## 摘要（原文）

> Recent vision-language models (VLMs) achieve strong zero-shot performance via large-scale image-text pretraining and have been widely adopted in medical image analysis. However, existing VLMs remain notably weak at understanding negated clinical statements, largely due to contrastive alignment objectives that treat negation as a minor linguistic variation rather than a meaning-inverting operator. In multi-label settings, prompt-based InfoNCE fine-tuning further reinforces easy-positive image-prompt alignments, limiting effective learning of disease absence. To overcome these limitations, we reformulate vision-language alignment as a conditional semantic comparison problem, which is instantiated through a bi-directional multiple-choice learning framework(Bi-MCQ). By jointly training Image-to-Text and Text-to-Image MCQ tasks with affirmative, negative, and mixed prompts, our method implements fine-tuning as conditional semantic comparison instead of global similarity maximization. We further introduce direction-specific Cross-Attention fusion modules to address asymmetric cues required by bi-directional reasoning and reduce alignment interference. Experiments on ChestXray14, Open-I, CheXpert, and PadChest show that Bi-MCQ improves negation understanding by up to 0.47 AUC over the zero-shot performance of the state-of-the-art CARZero model, while achieving up to a 0.08 absolute gain on positive-negative combined (PNC) evaluation. Additionally, Bi-MCQ reduces the affirmative-negative AUC gap by an average of 0.12 compared to InfoNCE-based fine-tuning, demonstrating that objective reformulation can substantially enhance negation understanding in medical VLMs.

