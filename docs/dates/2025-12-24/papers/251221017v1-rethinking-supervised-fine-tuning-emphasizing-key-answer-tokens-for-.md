---
layout: default
title: Rethinking Supervised Fine-Tuning: Emphasizing Key Answer Tokens for Improved LLM Accuracy
---

# Rethinking Supervised Fine-Tuning: Emphasizing Key Answer Tokens for Improved LLM Accuracy
**arXiv**：[2512.21017v1](https://arxiv.org/abs/2512.21017) · [PDF](https://arxiv.org/pdf/2512.21017.pdf)  
**作者**：Xiaofeng Shi, Qian Kou, Yuduo Li, Hua Zhou  

**一句话要点**：提出SFTKey两阶段训练方案，通过强调关键答案令牌以提升大语言模型在复杂推理任务中的准确性。

**关键词**：监督微调, 大语言模型, 链式思维, 关键答案优化, 两阶段训练

## 3 点简述
- 核心问题：传统监督微调中，模型可能过度关注长链思维序列，忽视短但关键答案部分，影响任务准确性。
- 方法要点：采用两阶段训练，第一阶段确保输出格式正确，第二阶段仅微调关键答案部分以优化准确性。
- 实验或效果：在多个基准和模型家族上，SFTKey相比传统监督微调平均准确率提升超过5%，同时保持格式生成能力。

## 摘要（原文）

> With the rapid advancement of Large Language Models (LLMs), the Chain-of-Thought (CoT) component has become significant for complex reasoning tasks. However, in conventional Supervised Fine-Tuning (SFT), the model could allocate disproportionately more attention to CoT sequences with excessive length. This reduces focus on the much shorter but essential Key portion-the final answer, whose correctness directly determines task success and evaluation quality. To address this limitation, we propose SFTKey, a two-stage training scheme. In the first stage, conventional SFT is applied to ensure proper output format, while in the second stage, only the Key portion is fine-tuned to improve accuracy. Extensive experiments across multiple benchmarks and model families demonstrate that SFTKey achieves an average accuracy improvement exceeding 5\% over conventional SFT, while preserving the ability to generate correct formats. Overall, this study advances LLM fine-tuning by explicitly balancing CoT learning with additional optimization on answer-relevant tokens.

