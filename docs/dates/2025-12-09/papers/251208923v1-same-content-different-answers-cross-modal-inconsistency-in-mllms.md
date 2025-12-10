---
layout: default
title: Same Content, Different Answers: Cross-Modal Inconsistency in MLLMs
---

# Same Content, Different Answers: Cross-Modal Inconsistency in MLLMs
**arXiv**：[2512.08923v1](https://arxiv.org/abs/2512.08923) · [PDF](https://arxiv.org/pdf/2512.08923.pdf)  
**作者**：Angela van Sprang, Laurens Samson, Ana Lucic, Erman Acar, Sennay Ghebreab, Yuki M. Asano  

**一句话要点**：提出REST和REST+基准以评估多模态大语言模型的跨模态不一致性

**关键词**：多模态大语言模型, 跨模态一致性, 基准评估, 模态间隙, 视觉特征影响, 文本识别

## 3 点简述
- 核心问题：MLLMs在图像、文本和混合模态中处理相同语义信息时存在推理不一致
- 方法要点：构建包含三种模态的基准，评估15个MLLMs的跨模态一致性
- 实验或效果：发现模态不一致程度差异大，视觉特征和视觉令牌数影响性能

## 摘要（原文）

> We introduce two new benchmarks REST and REST+(Render-Equivalence Stress Tests) to enable systematic evaluation of cross-modal inconsistency in multimodal large language models (MLLMs). MLLMs are trained to represent vision and language in the same embedding space, yet they cannot perform the same tasks in both modalities. Our benchmarks contain samples with the same semantic information in three modalities (image, text, mixed) and we show that state-of-the-art MLLMs cannot consistently reason over these different modalities. We evaluate 15 MLLMs and find that the degree of modality inconsistency varies substantially, even when accounting for problems with text recognition (OCR). Neither rendering text as image nor rendering an image as text solves the inconsistency. Even if OCR is correct, we find that visual characteristics (text colour and resolution, but not font) and the number of vision tokens have an impact on model performance. Finally, we find that our consistency score correlates with the modality gap between text and images, highlighting a mechanistic interpretation of cross-modal inconsistent MLLMs.

