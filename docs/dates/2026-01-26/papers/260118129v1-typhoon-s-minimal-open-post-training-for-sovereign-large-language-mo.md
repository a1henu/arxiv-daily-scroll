---
layout: default
title: Typhoon-S: Minimal Open Post-Training for Sovereign Large Language Models
---

# Typhoon-S: Minimal Open Post-Training for Sovereign Large Language Models
**arXiv**：[2601.18129v1](https://arxiv.org/abs/2601.18129) · [PDF](https://arxiv.org/pdf/2601.18129.pdf)  
**作者**：Kunat Pipatanakul, Pittawat Taveekitworachai  

**一句话要点**：提出Typhoon-S后训练方法，以最小化资源实现主权大语言模型的高质量适配与特定任务能力。

**关键词**：主权大语言模型, 后训练方法, 强化微调, 泰语自然语言处理, 最小化资源训练

## 3 点简述
- 核心问题：主权环境下，资源有限且需控制模型权重与数据，现有大语言模型训练方法依赖大规模指令数据和复杂调优。
- 方法要点：结合监督微调、策略蒸馏和小规模强化微调，使用InK-GRPO扩展GRPO损失以提升特定任务性能。
- 实验或效果：以泰语为例，该方法将基础模型转化为指令调优模型，在泰语法律推理和文化知识任务中表现优异，同时保持通用能力。

## 摘要（原文）

> Large language models (LLMs) have progressed rapidly; however, most state-of-the-art models are trained and evaluated primarily in high-resource languages such as English and Chinese, and are often developed by a small number of organizations with access to large-scale compute and data. This gatekeeping creates a practical barrier for sovereign settings in which a regional- or national-scale institution or domain owner must retain control and understanding of model weights, training data, and deployment while operating under limited resources and strict transparency constraints. To this end, we identify two core requirements: (1) adoptability, the ability to transform a base model into a general-purpose assistant, and (2) sovereign capability, the ability to perform high-stakes, region-specific tasks (e.g., legal reasoning in local languages and cultural knowledge). We investigate whether these requirements can be achieved without scaling massive instruction corpora or relying on complex preference tuning pipelines and large-scale reinforcement fine-tuning (RFT). We present Typhoon S, a minimal and open post-training recipe that combines supervised fine-tuning, on-policy distillation, and small-scale RFT. Using Thai as a representative case study, we demonstrate that our approach transforms both sovereign-adapted and general-purpose base models into instruction-tuned models with strong general performance. We further show that small-scale RFT with InK-GRPO -- an extension of GRPO that augments the GRPO loss with a next-word prediction loss -- improves Thai legal reasoning and Thai-specific knowledge while preserving general capabilities. Our results suggest that a carefully designed post-training strategy can reduce the required scale of instruction data and computation, providing a practical path toward high-quality sovereign LLMs under academic-scale resources.

