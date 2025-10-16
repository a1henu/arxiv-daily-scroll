---
layout: default
title: Risk-adaptive Activation Steering for Safe Multimodal Large Language Models
---

# Risk-adaptive Activation Steering for Safe Multimodal Large Language Models
**arXiv**：[2510.13698v1](https://arxiv.org/abs/2510.13698) · [PDF](https://arxiv.org/pdf/2510.13698.pdf)  
**作者**：Jonghyun Park, Minhyuk Seo, Jonghyun Choi  

**一句话要点**：提出风险自适应激活引导以解决多模态大模型的安全对齐问题

**关键词**：多模态大模型, 安全对齐, 激活引导, 风险自适应, 推理优化

## 3 点简述
- 核心问题：多模态查询中图像嵌入恶意意图，模型易受攻击且训练成本高
- 方法要点：重构查询增强跨模态注意力，评估风险并自适应引导激活
- 实验或效果：显著降低攻击成功率，保持任务性能并提升推理速度

## 摘要（原文）

> One of the key challenges of modern AI models is ensuring that they provide
> helpful responses to benign queries while refusing malicious ones. But often,
> the models are vulnerable to multimodal queries with harmful intent embedded in
> images. One approach for safety alignment is training with extensive safety
> datasets at the significant costs in both dataset curation and training.
> Inference-time alignment mitigates these costs, but introduces two drawbacks:
> excessive refusals from misclassified benign queries and slower inference speed
> due to iterative output adjustments. To overcome these limitations, we propose
> to reformulate queries to strengthen cross-modal attention to safety-critical
> image regions, enabling accurate risk assessment at the query level. Using the
> assessed risk, it adaptively steers activations to generate responses that are
> safe and helpful without overhead from iterative output adjustments. We call
> this Risk-adaptive Activation Steering (RAS). Extensive experiments across
> multiple benchmarks on multimodal safety and utility demonstrate that the RAS
> significantly reduces attack success rates, preserves general task performance,
> and improves inference speed over prior inference-time defenses.

