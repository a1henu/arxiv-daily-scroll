---
layout: default
title: Distilling the Essence: Efficient Reasoning Distillation via Sequence Truncation
---

# Distilling the Essence: Efficient Reasoning Distillation via Sequence Truncation
**arXiv**：[2512.21002v1](https://arxiv.org/abs/2512.21002) · [PDF](https://arxiv.org/pdf/2512.21002.pdf)  
**作者**：Wei-Rui Chen, Vignesh Kothapalli, Ata Fatahibaarzi, Hejian Sang, Shao Tang, Qingquan Song, Zhipeng Wang, Muhammad Abdul-Mageed  

**一句话要点**：提出序列截断方法以优化大语言模型推理蒸馏的计算效率

**关键词**：推理蒸馏, 序列截断, 计算效率, 知识蒸馏, 大语言模型, 链式思维

## 3 点简述
- 核心问题：推理蒸馏中长序列训练导致计算成本高昂
- 方法要点：仅监督链式思维令牌，建立截断协议权衡计算与质量
- 实验或效果：截断50%令牌可保留约94%性能，减少50%训练资源

## 摘要（原文）

> Distilling the reasoning capabilities from a large language model (LLM) to a smaller student model often involves training on substantial amounts of reasoning data. However, distillation over lengthy sequences with prompt (P), chain-of-thought (CoT), and answer (A) segments makes the process computationally expensive. In this work, we investigate how the allocation of supervision across different segments (P, CoT, A) affects student performance. Our analysis shows that selective knowledge distillation over only the CoT tokens can be effective when the prompt and answer information is encompassed by it. Building on this insight, we establish a truncation protocol to quantify computation-quality tradeoffs as a function of sequence length. We observe that training on only the first $50\%$ of tokens of every training sequence can retain, on average, $\approx94\%$ of full-sequence performance on math benchmarks while reducing training time, memory usage, and FLOPs by about $50\%$ each. These findings suggest that reasoning distillation benefits from prioritizing early reasoning tokens and provides a simple lever for computation-quality tradeoffs. Codes are available at https://github.com/weiruichen01/distilling-the-essence.

