---
layout: default
title: IntroSVG: Learning from Rendering Feedback for Text-to-SVG Generation via an Introspective Generator-Critic Framework
---

# IntroSVG: Learning from Rendering Feedback for Text-to-SVG Generation via an Introspective Generator-Critic Framework
**arXiv**：[2603.09312v1](https://arxiv.org/abs/2603.09312) · [PDF](https://arxiv.org/pdf/2603.09312.pdf)  
**作者**：Feiyu Wang, Jiayuan Yang, Zhiyuan Zhao, Da Zhang, Bingyu Li, Peng Liu, Junyu Gao  

**一句话要点**：提出IntroSVG框架，通过自省生成-批评循环解决文本到SVG生成中缺乏视觉反馈的问题。

**关键词**：文本到SVG生成, 视觉语言模型, 自省生成-批评框架, 直接偏好优化, 迭代优化

## 3 点简述
- 核心问题：现有文本到SVG生成方法因自回归训练未融入最终渲染图像的视觉感知，限制生成质量。
- 方法要点：采用统一视觉语言模型，通过监督微调和直接偏好优化，实现生成与批评的双重角色，并利用迭代循环自主改进输出。
- 实验或效果：在多项关键评估指标上达到最先进性能，生成具有更复杂结构、更强语义对齐和更高可编辑性的SVG。

## 摘要（原文）

> Scalable Vector Graphics (SVG) are central to digital design due to their inherent scalability and editability. Despite significant advancements in content generation enabled by Visual Language Models (VLMs), existing text-to-SVG generation methods are limited by a core challenge: the autoregressive training process does not incorporate visual perception of the final rendered image, which fundamentally constrains generation quality. To address this limitation, we propose an Introspective SVG Generation Framework (IntroSVG). At its core, the framework instantiates a unified VLM that operates in a closed loop, assuming dual roles of both generator and critic. Specifically, through Supervised Fine-Tuning (SFT), the model learns to draft SVGs and to provide feedback on their rendered outputs; moreover, we systematically convert early-stage failures into high-quality error-correction training data, thereby enhancing model robustness. Subsequently, we leverage a high-capacity teacher VLM to construct a preference dataset and further align the generator's policy through Direct Preference Optimization (DPO). During inference, the optimized generator and critic operate collaboratively in an iterative "generate-review-refine" cycle, starting from imperfect intermediate drafts to autonomously improve output quality. Experimental results demonstrate that our method achieves state-of-the-art performance across several key evaluation metrics, generating SVGs with more complex structures, stronger semantic alignment, and greater editability. These results corroborate the effectiveness of incorporating explicit visual feedback into the generation loop.

