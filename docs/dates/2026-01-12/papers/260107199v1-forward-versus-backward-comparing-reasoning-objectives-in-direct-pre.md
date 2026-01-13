---
layout: default
title: Forward versus Backward: Comparing Reasoning Objectives in Direct Preference Optimization
---

# Forward versus Backward: Comparing Reasoning Objectives in Direct Preference Optimization
**arXiv**：[2601.07199v1](https://arxiv.org/abs/2601.07199) · [PDF](https://arxiv.org/pdf/2601.07199.pdf)  
**作者**：Murtaza Nikzad, Raghuram Ramanujan  

**一句话要点**：比较前向与后向推理目标在直接偏好优化中对大语言模型可靠性的影响

**关键词**：直接偏好优化, 推理可靠性, 思维链生成, 后向验证, 大语言模型, 幻觉减少

## 3 点简述
- 核心问题：大语言模型在推理中常产生看似合理但错误的幻觉，影响可靠性。
- 方法要点：通过直接偏好优化，对比前向思维链生成和后向验证两种训练信号。
- 实验或效果：前向训练提升准确率，后向训练降低误报率，两者互补但存在权衡。

## 摘要（原文）

> Large language models exhibit impressive reasoning capabilities yet frequently generate plausible but incorrect solutions, a phenomenon commonly termed hallucination. This paper investigates the effect of training objective composition on reasoning reliability through Direct Preference Optimization. Two complementary training signals are examined: forward chain-of-thought generation, which trains the model to produce correct reasoning traces, and backward verification, which trains the model to verify and acknowledge errors in candidate solutions. Experiments on GSM8K reveal a fundamental trade-off between these objectives. Forward-only DPO training achieves the highest accuracy improvement, increasing from 83.1% to 86.6% (+3.5 percentage points), while backward-only training yields minimal accuracy gains but substantially reduces the false positive rate from 13.4% to 4.3%. Notably, both training variants reduce acknowledgement rate compared to the baseline, suggesting that preference optimization increases model confidence in its outputs. These findings indicate that forward and backward reasoning objectives provide distinct and complementary learning signals: forward training improves problem-solving capability, while backward training improves verification calibration. The complete training and evaluation pipeline, implemented efficiently through Low-Rank Adaptation, is released to facilitate further research.

