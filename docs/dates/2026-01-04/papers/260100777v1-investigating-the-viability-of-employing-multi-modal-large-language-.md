---
layout: default
title: Investigating the Viability of Employing Multi-modal Large Language Models in the Context of Audio Deepfake Detection
---

# Investigating the Viability of Employing Multi-modal Large Language Models in the Context of Audio Deepfake Detection
**arXiv**：[2601.00777v1](https://arxiv.org/abs/2601.00777) · [PDF](https://arxiv.org/pdf/2601.00777.pdf)  
**作者**：Akanksha Chuchra, Shukesh Reddy, Sudeepta Mishra, Abhijit Das, Abhinav Dhall  

**一句话要点**：探索多模态大语言模型在音频深度伪造检测中的可行性

**关键词**：音频深度伪造检测, 多模态大语言模型, 提示工程, 零样本学习, 微调训练

## 3 点简述
- 核心问题：音频深度伪造检测中多模态大语言模型的应用潜力尚未充分探索
- 方法要点：结合音频输入与多样化文本提示，通过问答式引导进行特征学习
- 实验或效果：模型在零样本下表现不佳，但经微调后在域内数据上展现出良好性能

## 摘要（原文）

> While Vision-Language Models (VLMs) and Multimodal Large Language Models (MLLMs) have shown strong generalisation in detecting image and video deepfakes, their use for audio deepfake detection remains largely unexplored. In this work, we aim to explore the potential of MLLMs for audio deepfake detection. Combining audio inputs with a range of text prompts as queries to find out the viability of MLLMs to learn robust representations across modalities for audio deepfake detection. Therefore, we attempt to explore text-aware and context-rich, question-answer based prompts with binary decisions. We hypothesise that such a feature-guided reasoning will help in facilitating deeper multimodal understanding and enable robust feature learning for audio deepfake detection. We evaluate the performance of two MLLMs, Qwen2-Audio-7B-Instruct and SALMONN, in two evaluation modes: (a) zero-shot and (b) fine-tuned. Our experiments demonstrate that combining audio with a multi-prompt approach could be a viable way forward for audio deepfake detection. Our experiments show that the models perform poorly without task-specific training and struggle to generalise to out-of-domain data. However, they achieve good performance on in-domain data with minimal supervision, indicating promising potential for audio deepfake detection.

