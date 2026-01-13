---
layout: default
title: IFDNS: An Iterative Feedback-Driven Neuro-Symbolic Method for Faithful Logical Reasoning
---

# IFDNS: An Iterative Feedback-Driven Neuro-Symbolic Method for Faithful Logical Reasoning
**arXiv**：[2601.07464v1](https://arxiv.org/abs/2601.07464) · [PDF](https://arxiv.org/pdf/2601.07464.pdf)  
**作者**：Xiaoheng Wang, Tongxuan Liu, Zi Gong, Xianzhe Dong, Yuting Zeng, Minhan Hu, Weizhe Huang, Jing Li  

**一句话要点**：提出IFDNS方法，通过迭代反馈机制解决大语言模型在复杂逻辑推理中的忠实性问题。

**关键词**：神经符号推理, 大语言模型, 逻辑推理, 迭代反馈, 忠实性提升, 提示方法集成

## 3 点简述
- 核心问题：现有神经符号方法在逻辑提取过程中存在信息丢失，导致推理不忠实。
- 方法要点：采用多轮反馈机制，准确提取因果语句并转换为逻辑表达式，减少信息损失。
- 实验或效果：在六个数据集上验证，显著提升CoT和CoT-SC性能，如LogiQA上CoT准确率提升9.40%。

## 摘要（原文）

> Large language models (LLMs) have demonstrated impressive capabilities across a wide range of reasoning tasks, including logical and mathematical problem-solving. While prompt-based methods like Chain-of-Thought (CoT) can enhance LLM reasoning abilities to some extent, they often suffer from a lack of faithfulness, where the derived conclusions may not align with the generated reasoning chain. To address this issue, researchers have explored neuro-symbolic approaches to bolster LLM logical reasoning capabilities. However, existing neuro-symbolic methods still face challenges with information loss during the process. To overcome these limitations, we introduce Iterative Feedback-Driven Neuro-Symbolic (IFDNS), a novel prompt-based method that employs a multi-round feedback mechanism to address LLM limitations in handling complex logical relationships. IFDNS utilizes iterative feedback during the logic extraction phase to accurately extract causal relationship statements and translate them into propositional and logical implication expressions, effectively mitigating information loss issues. Furthermore, IFDNS is orthogonal to existing prompt methods, allowing for seamless integration with various prompting approaches. Empirical evaluations across six datasets demonstrate the effectiveness of IFDNS in significantly improving the performance of CoT and Chain-of-Thought with Self-Consistency (CoT-SC). Specifically, IFDNS achieves a +9.40% accuracy boost for CoT on the LogiQA dataset and a +11.70% improvement for CoT-SC on the PrOntoQA dataset.

