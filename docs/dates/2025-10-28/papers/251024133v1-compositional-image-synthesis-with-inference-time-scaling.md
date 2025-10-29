---
layout: default
title: Compositional Image Synthesis with Inference-Time Scaling
---

# Compositional Image Synthesis with Inference-Time Scaling
**arXiv**：[2510.24133v1](https://arxiv.org/abs/2510.24133) · [PDF](https://arxiv.org/pdf/2510.24133.pdf)  
**作者**：Minsuk Ji, Sanghyeok Lee, Namhyuk Ahn  

**一句话要点**：提出训练免费框架，结合对象中心方法与自精炼，提升文本到图像合成的布局忠实度。

**关键词**：文本到图像合成, 布局忠实度, 对象中心方法, 自精炼, 推理时缩放, 视觉语言模型

## 3 点简述
- 现代文本到图像模型在组合性上表现不佳，常无法准确渲染对象数量、属性和空间关系。
- 利用大语言模型合成显式布局，并通过对象中心视觉语言模型迭代重排候选图像以对齐提示。
- 框架在推理时缩放，实现更强的场景对齐，同时保持美学质量，代码已开源。

## 摘要（原文）

> Despite their impressive realism, modern text-to-image models still struggle
> with compositionality, often failing to render accurate object counts,
> attributes, and spatial relations. To address this challenge, we present a
> training-free framework that combines an object-centric approach with
> self-refinement to improve layout faithfulness while preserving aesthetic
> quality. Specifically, we leverage large language models (LLMs) to synthesize
> explicit layouts from input prompts, and we inject these layouts into the image
> generation process, where a object-centric vision-language model (VLM) judge
> reranks multiple candidates to select the most prompt-aligned outcome
> iteratively. By unifying explicit layout-grounding with self-refine-based
> inference-time scaling, our framework achieves stronger scene alignment with
> prompts compared to recent text-to-image models. The code are available at
> https://github.com/gcl-inha/ReFocus.

