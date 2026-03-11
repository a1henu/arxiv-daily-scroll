---
layout: default
title: OOD-MMSafe: Advancing MLLM Safety from Harmful Intent to Hidden Consequences
---

# OOD-MMSafe: Advancing MLLM Safety from Harmful Intent to Hidden Consequences
**arXiv**：[2603.09706v1](https://arxiv.org/abs/2603.09706) · [PDF](https://arxiv.org/pdf/2603.09706.pdf)  
**作者**：Ming Wen, Kun Yang, Jingyu Zhang, Yuxuan Liu, shiwen cui, Shouling Ji, Xingjun Ma  

**一句话要点**：提出OOD-MMSafe基准和CASPO框架以增强多模态大语言模型在后果驱动安全中的风险识别能力

**关键词**：多模态大语言模型, 安全对齐, 后果驱动安全, 因果推理, 自蒸馏训练, 基准评估

## 3 点简述
- 核心问题：现有MLLM安全对齐主要针对恶意意图，忽视上下文依赖因果链中的潜在危害。
- 方法要点：引入OOD-MMSafe基准评估模型因果盲区，开发CASPO框架通过自蒸馏奖励优化安全推理。
- 实验或效果：CASPO显著降低风险识别失败率，如Qwen2.5-VL-7B降至7.3%，同时保持整体有效性。

## 摘要（原文）

> While safety alignment for Multimodal Large Language Models (MLLMs) has gained significant attention, current paradigms primarily target malicious intent or situational violations. We propose shifting the safety frontier toward consequence-driven safety, a paradigm essential for the robust deployment of autonomous and embodied agents. To formalize this shift, we introduce OOD-MMSafe, a benchmark comprising 455 curated query-image pairs designed to evaluate a model's ability to identify latent hazards within context-dependent causal chains. Our analysis reveals a pervasive causal blindness among frontier models, with the highest 67.5% failure rate in high-capacity closed-source models, and identifies a preference ceiling where static alignment yields format-centric failures rather than improved safety reasoning as model capacity grows. To address these bottlenecks, we develop the Consequence-Aware Safety Policy Optimization (CASPO) framework, which integrates the model's intrinsic reasoning as a dynamic reference for token-level self-distillation rewards. Experimental results demonstrate that CASPO significantly enhances consequence projection, reducing the failure ratio of risk identification to 7.3% for Qwen2.5-VL-7B and 5.7% for Qwen3-VL-4B while maintaining overall effectiveness.

