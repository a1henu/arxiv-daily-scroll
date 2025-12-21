---
layout: default
title: Differences That Matter: Auditing Models for Capability Gap Discovery and Rectification
---

# Differences That Matter: Auditing Models for Capability Gap Discovery and Rectification
**arXiv**：[2512.16921v1](https://arxiv.org/abs/2512.16921) · [PDF](https://arxiv.org/pdf/2512.16921.pdf)  
**作者**：Qihao Liu, Chengzhi Mao, Yaojie Liu, Alan Yuille, Wen-Sheng Chu  

**一句话要点**：提出AuditDM框架以自动发现和修正多模态大语言模型的能力差距

**关键词**：多模态大语言模型, 模型审计, 能力差距发现, 强化学习微调, 反事实图像生成, 模型诊断

## 3 点简述
- 传统多模态大语言模型评估方法缺乏可解释性，难以全面揭示模型间显著能力差距
- 通过强化学习微调模型作为审计器，生成最大化目标模型分歧的挑战性问题和反事实图像
- 在Gemma-3和PaliGemma-2等模型上发现20多种失败类型，微调后提升16个基准性能，使3B模型超越28B模型

## 摘要（原文）

> Conventional evaluation methods for multimodal LLMs (MLLMs) lack interpretability and are often insufficient to fully disclose significant capability gaps across models. To address this, we introduce AuditDM, an automated framework that actively discovers and rectifies MLLM failure modes by auditing their divergence. AuditDM fine-tunes an MLLM as an auditor via reinforcement learning to generate challenging questions and counterfactual images that maximize disagreement among target models. Once trained, the auditor uncovers diverse, interpretable exemplars that reveal model weaknesses and serve as annotation-free data for rectification. When applied to SoTA models like Gemma-3 and PaliGemma-2, AuditDM discovers more than 20 distinct failure types. Fine-tuning on these discoveries consistently improves all models across 16 benchmarks, and enables a 3B model to surpass its 28B counterpart. Our results suggest that as data scaling hits diminishing returns, targeted model auditing offers an effective path to model diagnosis and improvement.

