---
layout: default
title: Can MLLMs Read the Room? A Multimodal Benchmark for Assessing Deception in Multi-Party Social Interactions
---

# Can MLLMs Read the Room? A Multimodal Benchmark for Assessing Deception in Multi-Party Social Interactions
**arXiv**：[2511.16221v1](https://arxiv.org/abs/2511.16221) · [PDF](https://arxiv.org/pdf/2511.16221.pdf)  
**作者**：Caixin Kang, Yifei Huang, Liangyang Ouyang, Mingfang Zhang, Ruicong Liu, Yoichi Sato  

**一句话要点**：提出多模态交互欺骗评估任务与数据集，以解决MLLMs在复杂社交中识别欺骗的不足。

**关键词**：多模态大语言模型, 社交欺骗评估, 多模态数据集, 社交推理, 基准测试

## 3 点简述
- 核心问题：MLLMs缺乏在多人社交互动中识别欺骗的能力，无法有效解读多模态社交线索。
- 方法要点：引入MIDA任务和数据集，设计SoCoT推理管道和DSEM模块以提升社交推理。
- 实验或效果：评估12个MLLMs显示性能差距大，新框架带来改进，但模型仍不可靠。

## 摘要（原文）

> Despite their advanced reasoning capabilities, state-of-the-art Multimodal Large Language Models (MLLMs) demonstrably lack a core component of human intelligence: the ability to `read the room' and assess deception in complex social interactions. To rigorously quantify this failure, we introduce a new task, Multimodal Interactive Deception Assessment (MIDA), and present a novel multimodal dataset providing synchronized video and text with verifiable ground-truth labels for every statement. We establish a comprehensive benchmark evaluating 12 state-of-the-art open- and closed-source MLLMs, revealing a significant performance gap: even powerful models like GPT-4o struggle to distinguish truth from falsehood reliably. Our analysis of failure modes indicates that these models fail to effectively ground language in multimodal social cues and lack the ability to model what others know, believe, or intend, highlighting the urgent need for novel approaches to building more perceptive and trustworthy AI systems. To take a step forward, we design a Social Chain-of-Thought (SoCoT) reasoning pipeline and a Dynamic Social Epistemic Memory (DSEM) module. Our framework yields performance improvement on this challenging task, demonstrating a promising new path toward building MLLMs capable of genuine human-like social reasoning.

