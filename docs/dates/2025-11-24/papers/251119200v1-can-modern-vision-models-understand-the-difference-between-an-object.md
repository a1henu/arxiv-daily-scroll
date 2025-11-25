---
layout: default
title: Can Modern Vision Models Understand the Difference Between an Object and a Look-alike?
---

# Can Modern Vision Models Understand the Difference Between an Object and a Look-alike?
**arXiv**：[2511.19200v1](https://arxiv.org/abs/2511.19200) · [PDF](https://arxiv.org/pdf/2511.19200.pdf)  
**作者**：Itay Cohen, Ethan Fetaya, Amir Rosenfeld  

**一句话要点**：提出RoLA数据集和嵌入方向方法，以评估视觉语言模型区分真实物体与相似物的能力。

**关键词**：视觉语言模型, 相似物识别, CLIP嵌入, 跨模态检索, 图像描述增强

## 3 点简述
- 核心问题：视觉语言模型能否区分真实物体与相似物（如玩具、雕像），弥补与人类感知的差距。
- 方法要点：构建RoLA数据集，估计CLIP嵌入空间中真实与相似物的方向，并应用于跨模态检索和图像描述。
- 实验或效果：该方法在Conceptual12M上提升检索性能，并改进CLIP前缀描述器的描述质量。

## 摘要（原文）

> Recent advances in computer vision have yielded models with strong performance on recognition benchmarks; however, significant gaps remain in comparison to human perception. One subtle ability is to judge whether an image looks like a given object without being an instance of that object. We study whether vision-language models such as CLIP capture this distinction. We curated a dataset named RoLA (Real or Lookalike) of real and lookalike exemplars (e.g., toys, statues, drawings, pareidolia) across multiple categories, and first evaluate a prompt-based baseline with paired "real"/"lookalike" prompts. We then estimate a direction in CLIP's embedding space that moves representations between real and lookalike. Applying this direction to image and text embeddings improves discrimination in cross-modal retrieval on Conceptual12M, and also enhances captions produced by a CLIP prefix captioner.

