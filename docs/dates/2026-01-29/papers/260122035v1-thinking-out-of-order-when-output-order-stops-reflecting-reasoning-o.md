---
layout: default
title: Thinking Out of Order: When Output Order Stops Reflecting Reasoning Order in Diffusion Language Models
---

# Thinking Out of Order: When Output Order Stops Reflecting Reasoning Order in Diffusion Language Models
**arXiv**：[2601.22035v1](https://arxiv.org/abs/2601.22035) · [PDF](https://arxiv.org/pdf/2601.22035.pdf)  
**作者**：Longxuan Yu, Yu Fu, Shaorong Zhang, Hui Liu, Mukund Varma T, Greg Ver Steeg, Yue Dong  

**一句话要点**：提出掩码扩散语言模型以解决自回归模型在输出顺序与推理顺序冲突时的性能下降问题

**关键词**：掩码扩散语言模型, 自回归语言模型, 顺序鲁棒性, 推理顺序, 并行生成, 基准评估

## 3 点简述
- 核心问题：自回归语言模型固定左到右生成顺序，当输出结构要求答案先于推理时，导致过早承诺和准确性下降
- 方法要点：掩码扩散语言模型通过并行迭代精炼所有词元，解耦计算顺序与输出结构，实现顺序鲁棒性
- 实验或效果：在GSM8K、Math500和ReasonOrderQA基准上，掩码扩散模型在非标准顺序下性能稳定，相对下降≤14%，而自回归模型下降高达67%

## 摘要（原文）

> Autoregressive (AR) language models enforce a fixed left-to-right generation order, creating a fundamental limitation when the required output structure conflicts with natural reasoning (e.g., producing answers before explanations due to presentation or schema constraints). In such cases, AR models must commit to answers before generating intermediate reasoning, and this rigid constraint forces premature commitment. Masked diffusion language models (MDLMs), which iteratively refine all tokens in parallel, offer a way to decouple computation order from output structure. We validate this capability on GSM8K, Math500, and ReasonOrderQA, a benchmark we introduce with controlled difficulty and order-level evaluation. When prompts request answers before reasoning, AR models exhibit large accuracy gaps compared to standard chain-of-thought ordering (up to 67% relative drop), while MDLMs remain stable ($\leq$14% relative drop), a property we term "order robustness". Using ReasonOrderQA, we present evidence that MDLMs achieve order robustness by stabilizing simpler tokens (e.g., reasoning steps) earlier in the diffusion process than complex ones (e.g., final answers), enabling reasoning tokens to stabilize before answer commitment. Finally, we identify failure conditions where this advantage weakens, outlining the limits required for order robustness.

