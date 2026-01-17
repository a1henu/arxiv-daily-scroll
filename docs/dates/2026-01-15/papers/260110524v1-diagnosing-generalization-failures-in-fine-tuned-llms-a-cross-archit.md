---
layout: default
title: Diagnosing Generalization Failures in Fine-Tuned LLMs: A Cross-Architectural Study on Phishing Detection
---

# Diagnosing Generalization Failures in Fine-Tuned LLMs: A Cross-Architectural Study on Phishing Detection
**arXiv**：[2601.10524v1](https://arxiv.org/abs/2601.10524) · [PDF](https://arxiv.org/pdf/2601.10524.pdf)  
**作者**：Frank Bobe, Gregory D. Vetaw, Chase Pavlick, Darshan Bryner, Matthew Cook, Jose Salas-Vernis  

**一句话要点**：提出多层级诊断框架以解决微调大语言模型在钓鱼检测中的泛化失败问题

**关键词**：大语言模型微调, 泛化失败诊断, 钓鱼检测, 跨架构研究, SHAP分析, 机制可解释性

## 3 点简述
- 核心问题：微调大语言模型在专业任务中性能脆弱且泛化失败的原因诊断是开放问题
- 方法要点：应用SHAP分析和机制可解释性进行跨架构研究，揭示泛化失败的根源
- 实验或效果：发现泛化依赖于架构与数据多样性协同，Gemma 2 9B在多样化数据集上性能最佳

## 摘要（原文）

> The practice of fine-tuning Large Language Models (LLMs) has achieved state-of-the-art performance on specialized tasks, yet diagnosing why these models become brittle and fail to generalize remains a critical open problem. To address this, we introduce and apply a multi-layered diagnostic framework to a cross-architectural study. We fine-tune Llama 3.1 8B, Gemma 2 9B, and Mistral models on a high-stakes phishing detection task and use SHAP analysis and mechanistic interpretability to uncover the root causes of their generalization failures. Our investigation reveals three critical findings: (1) Generalization is driven by a powerful synergy between architecture and data diversity. The Gemma 2 9B model achieves state-of-the-art performance (>91\% F1), but only when trained on a stylistically diverse ``generalist'' dataset. (2) Generalization is highly architecture-dependent. We diagnose a specific failure mode in Llama 3.1 8B, which performs well on a narrow domain but cannot integrate diverse data, leading to a significant performance drop. (3) Some architectures are inherently more generalizable. The Mistral model proves to be a consistent and resilient performer across multiple training paradigms. By pinpointing the flawed heuristics responsible for these failures, our work provides a concrete methodology for diagnosing and understanding generalization failures, underscoring that reliable AI requires deep validation of the interplay between architecture, data, and training strategy.

