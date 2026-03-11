---
layout: default
title: Reading, Not Thinking: Understanding and Bridging the Modality Gap When Text Becomes Pixels in Multimodal LLMs
---

# Reading, Not Thinking: Understanding and Bridging the Modality Gap When Text Becomes Pixels in Multimodal LLMs
**arXiv**：[2603.09095v1](https://arxiv.org/abs/2603.09095) · [PDF](https://arxiv.org/pdf/2603.09095.pdf)  
**作者**：Kaiser Sun, Xiaochuang Yuan, Hongjun Liu, Chen Zhao, Cheng Zhang, Mark Dredze, Fan Bai  

**一句话要点**：提出自蒸馏方法以解决多模态大语言模型中文本图像模态差距问题

**关键词**：多模态大语言模型, 模态差距, 文本图像处理, 自蒸馏训练, 视觉文本理解, 性能诊断

## 3 点简述
- 核心问题：多模态大语言模型处理图像文本时性能下降，任务和数据依赖性显著
- 方法要点：通过自蒸馏训练，将纯文本推理轨迹与图像输入配对，提升视觉文本理解
- 实验或效果：在GSM8K上图像模式准确率从30.71%提升至92.72%，并迁移至未见基准

## 摘要（原文）

> Multimodal large language models (MLLMs) can process text presented as images, yet they often perform worse than when the same content is provided as textual tokens. We systematically diagnose this "modality gap" by evaluating seven MLLMs across seven benchmarks in five input modes, spanning both synthetically rendered text and realistic document images from arXiv PDFs to Wikipedia pages. We find that the modality gap is task- and data-dependent. For example, math tasks degrade by over 60 points on synthetic renderings, while natural document images often match or exceed text-mode performance. Rendering choices such as font and resolution are strong confounds, with font alone swinging accuracy by up to 47 percentage points. To understand this, we conduct a grounded-theory error analysis of over 4,000 examples, revealing that image mode selectively amplifies reading errors (calculation and formatting failures) while leaving knowledge and reasoning errors largely unchanged, and that some models exhibit a chain-of-thought reasoning collapse under visual input. Motivated by these findings, we propose a self-distillation method that trains the model on its own pure text reasoning traces paired with image inputs, raising image-mode accuracy on GSM8K from 30.71% to 92.72% and transferring to unseen benchmarks without catastrophic forgetting. Overall, our study provides a systematic understanding of the modality gap and suggests a practical path toward improving visual text understanding in multimodal language models.

