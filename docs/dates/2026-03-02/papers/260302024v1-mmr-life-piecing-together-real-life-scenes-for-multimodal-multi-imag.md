---
layout: default
title: MMR-Life: Piecing Together Real-life Scenes for Multimodal Multi-image Reasoning
---

# MMR-Life: Piecing Together Real-life Scenes for Multimodal Multi-image Reasoning
**arXiv**：[2603.02024v1](https://arxiv.org/abs/2603.02024) · [PDF](https://arxiv.org/pdf/2603.02024.pdf)  
**作者**：Jiachun Li, Shaoping Huang, Zhuoran Jin, Chenlong Zhang, Pengfei Cao, Yubo Chen, Kang Liu, Jun Zhao  

**一句话要点**：提出MMR-Life基准以评估多模态大语言模型在真实场景中的多图像推理能力

**关键词**：多模态推理, 多图像理解, 真实场景基准, 推理类型评估, 模型性能分析

## 3 点简述
- 核心问题：现有MLLMs在真实生活场景中的多图像推理能力缺乏标准化评估基准
- 方法要点：构建包含2,646个选择题和19,108张真实图像的基准，覆盖七种推理类型
- 实验或效果：评估37个先进模型，最高准确率仅58%，显示推理能力存在显著挑战

## 摘要（原文）

> Recent progress in the reasoning capabilities of multimodal large language models (MLLMs) has empowered them to address more complex tasks such as scientific analysis and mathematical reasoning. Despite their promise, MLLMs' reasoning abilities across different scenarios in real life remain largely unexplored and lack standardized benchmarks for evaluation. To address this gap, we introduce MMR-Life, a comprehensive benchmark designed to evaluate the diverse multimodal multi-image reasoning capabilities of MLLMs across real-life scenarios. MMR-Life consists of 2,646 multiple-choice questions based on 19,108 images primarily sourced from real-world contexts, comprehensively covering seven reasoning types: abductive, analogical, causal, deductive, inductive, spatial, and temporal. Unlike existing reasoning benchmarks, MMR-Life does not rely on domain-specific expertise but instead requires models to integrate information across multiple images and apply diverse reasoning abilities. The evaluation of 37 advanced models highlights the substantial challenge posed by MMR-Life. Even top models like GPT-5 achieve only 58% accuracy and display considerable variance in performance across reasoning types. Moreover, we analyze the reasoning paradigms of existing MLLMs, exploring how factors such as thinking length, reasoning method, and reasoning type affect their performance. In summary, MMR-Life establishes a comprehensive foundation for evaluating, analyzing, and improving the next generation of multimodal reasoning systems.

