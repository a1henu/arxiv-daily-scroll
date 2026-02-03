---
layout: default
title: Mitigating Safety Tax via Distribution-Grounded Refinement in Large Reasoning Models
---

# Mitigating Safety Tax via Distribution-Grounded Refinement in Large Reasoning Models
**arXiv**：[2602.02136v1](https://arxiv.org/abs/2602.02136) · [PDF](https://arxiv.org/pdf/2602.02136.pdf)  
**作者**：Yingsha Xie, Tiansheng Huang, Enneng Yang, Rui Min, Wenjie Lu, Xiaochun Cao, Naiqiang Tan, Li Shen  

**一句话要点**：提出分布对齐精炼方法DGR以缓解大型推理模型安全对齐中的能力退化问题

**关键词**：安全对齐, 分布对齐, 大型推理模型, 数据集精炼, 能力退化缓解

## 3 点简述
- 核心问题：安全对齐导致大型推理模型通用推理能力下降，源于外部数据集与目标模型分布不匹配
- 方法要点：DGR通过精炼外部安全推理数据集，使其与目标模型内部分布对齐，减少分布差距
- 实验或效果：DGR在保持安全性能的同时，平均推理准确率提升超20%，且分布偏移程度与能力退化相关

## 摘要（原文）

> Safety alignment incurs safety tax that perturbs a large reasoning model's (LRM) general reasoning ability. Existing datasets used for safety alignment for an LRM are usually constructed by distilling safety reasoning traces and answers from an external LRM or human labeler. However, such reasoning traces and answers exhibit a distributional gap with the target LRM that needs alignment, and we conjecture such distributional gap is the culprit leading to significant degradation of reasoning ability of the target LRM. Driven by this hypothesis, we propose a safety alignment dataset construction method, dubbed DGR. DGR transforms and refines an existing out-of-distributional safety reasoning dataset to be aligned with the target's LLM inner distribution. Experimental results demonstrate that i) DGR effectively mitigates the safety tax while maintaining safety performance across all baselines, i.e., achieving \textbf{+30.2\%} on DirectRefusal and \textbf{+21.2\%} on R1-ACT improvement in average reasoning accuracy compared to Vanilla SFT; ii) the degree of reasoning degradation correlates with the extent of distribution shift, suggesting that bridging this gap is central to preserving capabilities. Furthermore, we find that safety alignment in LRMs may primarily function as a mechanism to activate latent knowledge, as a mere \textbf{10} samples are sufficient for activating effective refusal behaviors. These findings not only emphasize the importance of distributional consistency but also provide insights into the activation mechanism of safety in reasoning models.

