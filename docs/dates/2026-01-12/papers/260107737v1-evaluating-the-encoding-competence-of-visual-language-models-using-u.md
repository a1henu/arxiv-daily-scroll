---
layout: default
title: Evaluating the encoding competence of visual language models using uncommon actions
---

# Evaluating the encoding competence of visual language models using uncommon actions
**arXiv**：[2601.07737v1](https://arxiv.org/abs/2601.07737) · [PDF](https://arxiv.org/pdf/2601.07737.pdf)  
**作者**：Chen Ling, Nai Ding  

**一句话要点**：提出UAIT数据集以评估视觉语言模型在非常识动作场景中的语义理解能力

**关键词**：视觉语言模型, 语义理解评估, 非常识动作, 图像-文本对, 微调优化, 诊断工具

## 3 点简述
- 核心问题：现有视觉语言模型在非常识动作场景中语义理解能力不足，难以区分语法正确性与语义合理性。
- 方法要点：通过半自动化流程合成高质量非常识图像-文本对，结合大语言模型和文本到图像生成技术构建UAIT数据集。
- 实验或效果：实验显示所有模型在语义判断上显著差于人类，但轻量模型微调后准确率提升，表明定向适应潜力。

## 摘要（原文）

> We propose UAIT (Uncommon-sense Action Image-Text) dataset, a new evaluation benchmark designed to test the semantic understanding ability of visual language models (VLMs) in uncommon-sense action scenes. Unlike previous datasets that focus on common visual scenes with statistical frequency advantages, UAIT challenges models with grammatically reasonable but semantically counter-common sense image-text pairs. Such tasks require models to go beyond superficial pattern recognition and demonstrate a deep understanding of agent-patient relationships and physical feasibility. To build UAIT, we designed a semi-automated process to synthesize high-quality uncommon-sense image-text samples using large language models, few-shot prompt engineering, and text-to-image generation. Each sample is accompanied by a carefully designed multiple-choice question to test the model's competence in fine-grained reasoning. We evaluate multiple state-of-the-art visual language models and compare them with models based on contrastive learning. Experiments show that all models perform significantly worse than humans in semantic judgment, especially in distinguishing grammatical correctness from semantic rationality. Further experiments show that even the lightweight model can improve its accuracy after fine-tuning, demonstrating the great potential of directional adaptation. This study not only reveals the key weaknesses of VLMs, but also provides diagnostic tools and research directions for the development of robust models with real visual semantic reasoning capabilities.

