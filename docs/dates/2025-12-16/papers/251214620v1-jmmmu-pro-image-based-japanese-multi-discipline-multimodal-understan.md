---
layout: default
title: JMMMU-Pro: Image-based Japanese Multi-discipline Multimodal Understanding Benchmark via Vibe Benchmark Construction
---

# JMMMU-Pro: Image-based Japanese Multi-discipline Multimodal Understanding Benchmark via Vibe Benchmark Construction
**arXiv**：[2512.14620v1](https://arxiv.org/abs/2512.14620) · [PDF](https://arxiv.org/pdf/2512.14620.pdf)  
**作者**：Atsuyuki Miyai, Shota Onohara, Jeonghun Baek, Kiyoharu Aizawa  

**一句话要点**：提出JMMMU-Pro基准和Vibe Benchmark Construction方法，以低成本构建高质量日语多学科视觉问答基准。

**关键词**：日语多模态理解, 视觉问答基准, 图像生成模型, 基准构建方法, 开源语言模型评估

## 3 点简述
- 核心问题：现有日语多模态理解基准需改进，以更严格评估语言模型在视觉-文本整合理解上的能力。
- 方法要点：使用图像生成模型（如Nano Banana Pro）生成候选视觉问题，人工验证和调整提示以确保质量。
- 实验或效果：所有开源语言模型在JMMMU-Pro上表现显著困难，突显其作为未来开源社区发展的重要基准价值。

## 摘要（原文）

> This paper introduces JMMMU-Pro, an image-based Japanese Multi-discipline Multimodal Understanding Benchmark, and Vibe Benchmark Construction, a scalable construction method. Following the evolution from MMMU to MMMU-Pro, JMMMU-Pro extends JMMMU by composing the question image and question text into a single image, thereby creating a benchmark that requires integrated visual-textual understanding through visual perception. To build JMMMU-Pro, we propose Vibe Benchmark Construction, a methodology in which an image generative model (e.g., Nano Banana Pro) produces candidate visual questions, and humans verify the outputs and, when necessary, regenerate with adjusted prompts to ensure quality. By leveraging Nano Banana Pro's highly realistic image generation capabilities and its ability to embed clean Japanese text, we construct a high-quality benchmark at low cost, covering a wide range of background and layout designs. Experimental results show that all open-source LMMs struggle substantially with JMMMU-Pro, underscoring JMMMU-Pro as an important benchmark for guiding future efforts in the open-source community. We believe that JMMMU-Pro provides a more rigorous evaluation tool for assessing the Japanese capabilities of LMMs and that our Vibe Benchmark Construction also offers an efficient guideline for future development of image-based VQA benchmarks.

