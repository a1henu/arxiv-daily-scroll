---
layout: default
title: OCR-Agent: Agentic OCR with Capability and Memory Reflection
---

# OCR-Agent: Agentic OCR with Capability and Memory Reflection
**arXiv**：[2602.21053v1](https://arxiv.org/abs/2602.21053) · [PDF](https://arxiv.org/pdf/2602.21053.pdf)  
**作者**：Shimin Wen, Zeyu Zhang, Xingdou Bian, Hongjie Zhu, Lulu He, Layi Shama, Daji Ergu, Ying Cai  

**一句话要点**：提出OCR-Agent框架，通过能力与记忆反思增强视觉语言模型的自校正能力，以解决迭代优化中的认知偏差问题。

**关键词**：视觉语言模型, 自校正机制, 迭代优化, 能力反思, 记忆反思, OCR基准测试

## 3 点简述
- 核心问题：视觉语言模型在迭代优化中缺乏有效自校正机制，易陷入重复无效尝试，难以稳定提升答案质量。
- 方法要点：引入能力反思诊断错误并制定校正计划，结合记忆反思回顾过去尝试以避免重复，通过严格再推理优化答案。
- 实验或效果：在OCRBench v2基准测试中，OCR-Agent超越开源SOTA模型，在视觉理解和推理任务上达到最优结果，无需额外训练。

## 摘要（原文）

> Large Vision-Language Models (VLMs) have demonstrated significant potential on complex visual understanding tasks through iterative optimization methods.However, these models generally lack effective self-correction mechanisms, making it difficult for them to independently rectify cognitive biases. Consequently, during multi-turn revisions, they often fall into repetitive and ineffective attempts, failing to achieve stable improvements in answer quality.To address this issue, we propose a novel iterative self-correction framework that endows models with two key capabilities: Capability Reflection and Memory Reflection. This framework guides the model to first diagnose errors and generate a correction plan via Capability Reflection, then leverage Memory Reflection to review past attempts to avoid repetition and explore new solutions, and finally, optimize the answer through rigorous re-reasoning. Experiments on the challenging OCRBench v2 benchmark show that OCR-Agent outperforms the current open-source SOTA model InternVL3-8B by +2.0 on English and +1.2 on Chinese subsets, while achieving state-of-the-art results in Visual Understanding (79.9) and Reasoning (66.5) - surpassing even larger fine-tuned models. Our method demonstrates that structured, self-aware reflection can significantly enhance VLMs' reasoning robustness without additional training. Code: https://github.com/AIGeeksGroup/OCR-Agent.

