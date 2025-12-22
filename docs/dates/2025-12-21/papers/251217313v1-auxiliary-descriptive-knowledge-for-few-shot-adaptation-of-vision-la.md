---
layout: default
title: Auxiliary Descriptive Knowledge for Few-Shot Adaptation of Vision-Language Model
---

# Auxiliary Descriptive Knowledge for Few-Shot Adaptation of Vision-Language Model
**arXiv**：[2512.17313v1](https://arxiv.org/abs/2512.17313) · [PDF](https://arxiv.org/pdf/2512.17313.pdf)  
**作者**：SuBeen Lee, GilHan Park, WonJun Moon, Hyun Seok Seong, Jae-Pil Heo  

**一句话要点**：提出辅助描述知识框架以增强视觉语言模型在少样本适应中的文本表示

**关键词**：少样本适应, 视觉语言模型, 参数高效微调, 文本表示增强, 描述性提示

## 3 点简述
- 核心问题：视觉语言模型在分布偏移下游任务中表现不佳，现有参数高效微调方法依赖固定提示，语义理解有限
- 方法要点：利用大语言模型离线生成描述性提示，通过组合知识和实例特定知识动态丰富文本表示，无需额外参数
- 实验或效果：在多个参数高效微调基线上一致提升性能，在各种场景中达到新最优水平

## 摘要（原文）

> Despite the impressive zero-shot capabilities of Vision-Language Models (VLMs), they often struggle in downstream tasks with distribution shifts from the pre-training data. Few-Shot Adaptation (FSA-VLM) has emerged as a key solution, typically using Parameter-Efficient Fine-Tuning (PEFT) to adapt models with minimal data. However, these PEFT methods are constrained by their reliance on fixed, handcrafted prompts, which are often insufficient to understand the semantics of classes. While some studies have proposed leveraging image-induced prompts to provide additional clues for classification, they introduce prohibitive computational overhead at inference. Therefore, we introduce Auxiliary Descriptive Knowledge (ADK), a novel framework that efficiently enriches text representations without compromising efficiency. ADK first leverages a Large Language Model to generate a rich set of descriptive prompts for each class offline. These pre-computed features are then deployed in two ways: (1) as Compositional Knowledge, an averaged representation that provides rich semantics, especially beneficial when class names are ambiguous or unfamiliar to the VLM; and (2) as Instance-Specific Knowledge, where a lightweight, non-parametric attention mechanism dynamically selects the most relevant descriptions for a given image. This approach provides two additional types of knowledge alongside the handcrafted prompt, thereby facilitating category distinction across various domains. Also, ADK acts as a parameter-free, plug-and-play component that enhances existing PEFT methods. Extensive experiments demonstrate that ADK consistently boosts the performance of multiple PEFT baselines, setting a new state-of-the-art across various scenarios.

