---
layout: default
title: LLEXICORP: End-user Explainability of Convolutional Neural Networks
---

# LLEXICORP: End-user Explainability of Convolutional Neural Networks
**arXiv**：[2511.02720v1](https://arxiv.org/abs/2511.02720) · [PDF](https://arxiv.org/pdf/2511.02720.pdf)  
**作者**：Vojtěch Kůr, Adam Bajger, Adam Kukučka, Marek Hradil, Vít Musil, Tomáš Brázdil  

**一句话要点**：提出LLEXICORP以自动生成CNN概念解释，提升可解释性可访问性。

**关键词**：卷积神经网络, 可解释人工智能, 概念相关性传播, 大语言模型, 自然语言解释, 图像分类

## 3 点简述
- 核心问题：CNN概念相关性传播方法依赖专家手动命名和解释，限制可扩展性。
- 方法要点：结合概念相关性传播与多模态大语言模型，自动命名概念并生成自然语言解释。
- 实验或效果：在ImageNet图像上定性评估，显示能降低解释深度神经网络的障碍。

## 摘要（原文）

> Convolutional neural networks (CNNs) underpin many modern computer vision
> systems. With applications ranging from common to critical areas, a need to
> explain and understand the model and its decisions (XAI) emerged. Prior works
> suggest that in the top layers of CNNs, the individual channels can be
> attributed to classifying human-understandable concepts. Concept relevance
> propagation (CRP) methods can backtrack predictions to these channels and find
> images that most activate these channels. However, current CRP workflows are
> largely manual: experts must inspect activation images to name the discovered
> concepts and must synthesize verbose explanations from relevance maps, limiting
> the accessibility of the explanations and their scalability.
>   To address these issues, we introduce Large Language model EXplaIns COncept
> Relevance Propagation (LLEXICORP), a modular pipeline that couples CRP with a
> multimodal large language model. Our approach automatically assigns descriptive
> names to concept prototypes and generates natural-language explanations that
> translate quantitative relevance distributions into intuitive narratives. To
> ensure faithfulness, we craft prompts that teach the language model the
> semantics of CRP through examples and enforce a separation between naming and
> explanation tasks. The resulting text can be tailored to different audiences,
> offering low-level technical descriptions for experts and high-level summaries
> for non-technical stakeholders.
>   We qualitatively evaluate our method on various images from ImageNet on a
> VGG16 model. Our findings suggest that integrating concept-based attribution
> methods with large language models can significantly lower the barrier to
> interpreting deep neural networks, paving the way for more transparent AI
> systems.

