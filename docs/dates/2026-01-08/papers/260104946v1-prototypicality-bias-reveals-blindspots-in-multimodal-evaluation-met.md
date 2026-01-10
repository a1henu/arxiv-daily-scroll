---
layout: default
title: Prototypicality Bias Reveals Blindspots in Multimodal Evaluation Metrics
---

# Prototypicality Bias Reveals Blindspots in Multimodal Evaluation Metrics
**arXiv**：[2601.04946v1](https://arxiv.org/abs/2601.04946) · [PDF](https://arxiv.org/pdf/2601.04946.pdf)  
**作者**：Subhadeep Roy, Gagan Bhatia, Steffen Eger  

**一句话要点**：提出ProtoBias基准和ProtoScore度量以解决多模态评估中的原型性偏差问题

**关键词**：多模态评估, 原型性偏差, 基准测试, 语义正确性, 度量鲁棒性, 文本到图像模型

## 3 点简述
- 核心问题：自动评估度量可能偏向视觉和社会原型而非语义正确性，导致系统偏差
- 方法要点：构建ProtoBias基准，配对语义正确但非原型图像与错误但原型图像进行对比评估
- 实验或效果：广泛度量如CLIPScore常误排，ProtoScore显著降低失败率并提升鲁棒性

## 摘要（原文）

> Automatic metrics are now central to evaluating text-to-image models, often substituting for human judgment in benchmarking and large-scale filtering. However, it remains unclear whether these metrics truly prioritize semantic correctness or instead favor visually and socially prototypical images learned from biased data distributions. We identify and study \emph{prototypicality bias} as a systematic failure mode in multimodal evaluation. We introduce a controlled contrastive benchmark \textsc{\textbf{ProtoBias}} (\textit{\textbf{Proto}typical \textbf{Bias}}), spanning Animals, Objects, and Demography images, where semantically correct but non-prototypical images are paired with subtly incorrect yet prototypical adversarial counterparts. This setup enables a directional evaluation of whether metrics follow textual semantics or default to prototypes. Our results show that widely used metrics, including CLIPScore, PickScore, and VQA-based scores, frequently misrank these pairs, while even LLM-as-Judge systems exhibit uneven robustness in socially grounded cases. Human evaluations consistently favour semantic correctness with larger decision margins. Motivated by these findings, we propose \textbf{\textsc{ProtoScore}}, a robust 7B-parameter metric that substantially reduces failure rates and suppresses misranking, while running at orders of magnitude faster than the inference time of GPT-5, approaching the robustness of much larger closed-source judges.

