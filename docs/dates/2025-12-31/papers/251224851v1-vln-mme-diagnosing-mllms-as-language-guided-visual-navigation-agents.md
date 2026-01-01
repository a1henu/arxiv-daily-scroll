---
layout: default
title: VLN-MME: Diagnosing MLLMs as Language-guided Visual Navigation agents
---

# VLN-MME: Diagnosing MLLMs as Language-guided Visual Navigation agents
**arXiv**：[2512.24851v1](https://arxiv.org/abs/2512.24851) · [PDF](https://arxiv.org/pdf/2512.24851.pdf)  
**作者**：Xunyi Zhao, Gengze Zhou, Qi Wu  

**一句话要点**：提出VLN-MME框架以评估多模态大语言模型在视觉语言导航中的零样本代理能力

**关键词**：多模态大语言模型, 视觉语言导航, 零样本评估, 具身代理, 空间推理, 顺序决策

## 3 点简述
- 核心问题：探索MLLMs在需要多轮对话空间推理和顺序动作预测的具身代理任务中的性能
- 方法要点：通过统一可扩展的评估框架，将传统导航数据集标准化为VLN-MME基准
- 实验或效果：发现增强思维链推理和自反思导致性能下降，揭示MLLMs在3D空间推理中的局限性

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have demonstrated remarkable capabilities across a wide range of vision-language tasks. However, their performance as embodied agents, which requires multi-round dialogue spatial reasoning and sequential action prediction, needs further exploration. Our work investigates this potential in the context of Vision-and-Language Navigation (VLN) by introducing a unified and extensible evaluation framework to probe MLLMs as zero-shot agents by bridging traditional navigation datasets into a standardized benchmark, named VLN-MME. We simplify the evaluation with a highly modular and accessible design. This flexibility streamlines experiments, enabling structured comparisons and component-level ablations across diverse MLLM architectures, agent designs, and navigation tasks. Crucially, enabled by our framework, we observe that enhancing our baseline agent with Chain-of-Thought (CoT) reasoning and self-reflection leads to an unexpected performance decrease. This suggests MLLMs exhibit poor context awareness in embodied navigation tasks; although they can follow instructions and structure their output, their 3D spatial reasoning fidelity is low. VLN-MME lays the groundwork for systematic evaluation of general-purpose MLLMs in embodied navigation settings and reveals limitations in their sequential decision-making capabilities. We believe these findings offer crucial guidance for MLLM post-training as embodied agents.

