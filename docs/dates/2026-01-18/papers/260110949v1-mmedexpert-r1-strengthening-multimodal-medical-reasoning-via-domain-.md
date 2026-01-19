---
layout: default
title: MMedExpert-R1: Strengthening Multimodal Medical Reasoning via Domain-Specific Adaptation and Clinical Guideline Reinforcement
---

# MMedExpert-R1: Strengthening Multimodal Medical Reasoning via Domain-Specific Adaptation and Clinical Guideline Reinforcement
**arXiv**：[2601.10949v1](https://arxiv.org/abs/2601.10949) · [PDF](https://arxiv.org/pdf/2601.10949.pdf)  
**作者**：Meidan Ding, Jipeng Zhang, Wenxuan Wang, Haiqin Zhong, Xiaoling Luo, Wenting Chen, Linlin Shen  

**一句话要点**：提出MMedExpert-R1，通过领域特定适应和临床指南强化，增强多模态医疗推理能力。

**关键词**：多模态医疗推理, 领域特定适应, 临床指南强化, LoRA模块, 专科对齐, 数据集构建

## 3 点简述
- 核心问题：现有医疗视觉语言模型在复杂临床推理中表现不足，面临数据稀缺、多专科对齐困难和推理多样性建模失败。
- 方法要点：构建高质量数据集MMedExpert，采用领域特定适应创建专科LoRA模块，并基于指南优势建模不同临床推理视角。
- 实验或效果：在MedXpert-MM和OmniMedVQA上实现先进性能，7B模型分别达到27.50和83.03分，验证了方法的有效性。

## 摘要（原文）

> Medical Vision-Language Models (MedVLMs) excel at perception tasks but struggle with complex clinical reasoning required in real-world scenarios. While reinforcement learning (RL) has been explored to enhance reasoning capabilities, existing approaches face critical mismatches: the scarcity of deep reasoning data, cold-start limits multi-specialty alignment, and standard RL algorithms fail to model clinical reasoning diversity. We propose MMedExpert-R1, a novel reasoning MedVLM that addresses these challenges through domain-specific adaptation and clinical guideline reinforcement. We construct MMedExpert, a high-quality dataset of 10K samples across four specialties with step-by-step reasoning traces. Our Domain-Specific Adaptation (DSA) creates specialty-specific LoRA modules to provide diverse initialization, while Guideline-Based Advantages (GBA) explicitly models different clinical reasoning perspectives to align with real-world diagnostic strategies. Conflict-Aware Capability Integration then merges these specialized experts into a unified agent, ensuring robust multi-specialty alignment. Comprehensive experiments demonstrate state-of-the-art performance, with our 7B model achieving 27.50 on MedXpert-MM and 83.03 on OmniMedVQA, establishing a robust foundation for reliable multimodal medical reasoning systems.

