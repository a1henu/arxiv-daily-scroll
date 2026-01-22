---
layout: default
title: Iterative Refinement Improves Compositional Image Generation
---

# Iterative Refinement Improves Compositional Image Generation
**arXiv**：[2601.15286v1](https://arxiv.org/abs/2601.15286) · [PDF](https://arxiv.org/pdf/2601.15286.pdf)  
**作者**：Shantanu Jaiswal, Mihir Prabhudesai, Nikash Bhardwaj, Zheyang Qin, Amir Zadeh, Chuan Li, Katerina Fragkiadaki, Deepak Pathak  

**一句话要点**：提出迭代细化方法以提升文本到图像模型在复杂组合场景下的生成质量

**关键词**：文本到图像生成, 迭代细化, 视觉语言模型, 组合场景, 测试时策略, 图像生成基准

## 3 点简述
- 核心问题：文本到图像模型在处理多对象、关系和属性的复杂提示时仍存在对齐不足。
- 方法要点：采用迭代测试时策略，利用视觉语言模型作为批评者提供反馈，逐步细化图像生成。
- 实验或效果：在多个基准测试中实现显著提升，如ConceptMix全正确率提高16.9%，人类评估偏好率达58.7%。

## 摘要（原文）

> Text-to-image (T2I) models have achieved remarkable progress, yet they continue to struggle with complex prompts that require simultaneously handling multiple objects, relations, and attributes. Existing inference-time strategies, such as parallel sampling with verifiers or simply increasing denoising steps, can improve prompt alignment but remain inadequate for richly compositional settings where many constraints must be satisfied. Inspired by the success of chain-of-thought reasoning in large language models, we propose an iterative test-time strategy in which a T2I model progressively refines its generations across multiple steps, guided by feedback from a vision-language model as the critic in the loop. Our approach is simple, requires no external tools or priors, and can be flexibly applied to a wide range of image generators and vision-language models. Empirically, we demonstrate consistent gains on image generation across benchmarks: a 16.9% improvement in all-correct rate on ConceptMix (k=7), a 13.8% improvement on T2I-CompBench (3D-Spatial category) and a 12.5% improvement on Visual Jenga scene decomposition compared to compute-matched parallel sampling. Beyond quantitative gains, iterative refinement produces more faithful generations by decomposing complex prompts into sequential corrections, with human evaluators preferring our method 58.7% of the time over 41.3% for the parallel baseline. Together, these findings highlight iterative self-correction as a broadly applicable principle for compositional image generation. Results and visualizations are available at https://iterative-img-gen.github.io/

