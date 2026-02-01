---
layout: default
title: Scaling Reasoning Hop Exposes Weaknesses: Demystifying and Improving Hop Generalization in Large Language Models
---

# Scaling Reasoning Hop Exposes Weaknesses: Demystifying and Improving Hop Generalization in Large Language Models
**arXiv**：[2601.21214v1](https://arxiv.org/abs/2601.21214) · [PDF](https://arxiv.org/pdf/2601.21214.pdf)  
**作者**：Zhaoyi Li, Jiatong Li, Gangwei Jiang, Linqi Song, Defu Lian, Ying Wei  

**一句话要点**：提出推理时校正方法以提升大语言模型在推理步数泛化中的性能

**关键词**：推理步数泛化, 注意力头校正, 链式思维推理, 大语言模型, 测试时干预

## 3 点简述
- 核心问题：大语言模型在推理步数超出训练分布时性能骤降，错误集中于少数关键类型
- 方法要点：通过动态识别并停用错误处理注意力头，校正推理过程中的内部竞争机制
- 实验或效果：跨任务和模型实验显示该方法能一致改善推理步数泛化，验证其有效性和潜力

## 摘要（原文）

> Chain-of-thought (CoT) reasoning has become the standard paradigm for enabling Large Language Models (LLMs) to solve complex problems. However, recent studies reveal a sharp performance drop in reasoning hop generalization scenarios, where the required number of reasoning steps exceeds training distributions while the underlying algorithm remains unchanged. The internal mechanisms driving this failure remain poorly understood. In this work, we conduct a systematic study on tasks from multiple domains, and find that errors concentrate at token positions of a few critical error types, rather than being uniformly distributed. Closer inspection reveals that these token-level erroneous predictions stem from internal competition mechanisms: certain attention heads, termed erroneous processing heads (ep heads), tip the balance by amplifying incorrect reasoning trajectories while suppressing correct ones. Notably, removing individual ep heads during inference can often restore the correct predictions. Motivated by these insights, we propose test-time correction of reasoning, a lightweight intervention method that dynamically identifies and deactivates ep heads in the reasoning process. Extensive experiments across different tasks and LLMs show that it consistently improves reasoning hop generalization, highlighting both its effectiveness and potential.

