---
layout: default
title: CORE: Collaborative Reasoning via Cross Teaching
---

# CORE: Collaborative Reasoning via Cross Teaching
**arXiv**：[2601.21600v1](https://arxiv.org/abs/2601.21600) · [PDF](https://arxiv.org/pdf/2601.21600.pdf)  
**作者**：Kshitij Mishra, Mirat Aubakirov, Martin Takac, Nils Lukas, Salem Lahlou  

**一句话要点**：提出CORE框架，通过跨模型教学实现训练时协作推理，提升小模型在数学推理任务上的性能。

**关键词**：协作推理, 跨模型教学, 训练时协作, 数学推理, 模型互补性, 小模型优化

## 3 点简述
- 核心问题：大语言模型在推理任务中存在互补性错误，单个模型可能在不同实例上失败。
- 方法要点：采用两阶段协作框架，包括独立采样和基于成功同伴提示的救援轮次，结合正确性、多样性和救援奖励优化。
- 实验效果：在GSM8K和MATH等数据集上，小模型对（3B+4B）仅用少量训练样本实现Pass@2显著提升，如GSM8K达99.54%。

## 摘要（原文）

> Large language models exhibit complementary reasoning errors: on the same instance, one model may succeed with a particular decomposition while another fails. We propose Collaborative Reasoning (CORE), a training-time collaboration framework that converts peer success into a learning signal via a cross-teaching protocol. Each problem is solved in two stages: a cold round of independent sampling, followed by a contexted rescue round in which models that failed receive hint extracted from a successful peer. CORE optimizes a combined reward that balances (i) correctness, (ii) a lightweight DPP-inspired diversity term to reduce error overlap, and (iii) an explicit rescue bonus for successful recovery. We evaluate CORE across four standard reasoning datasets GSM8K, MATH, AIME, and GPQA. With only 1,000 training examples, a pair of small open source models (3B+4B) reaches Pass@2 of 99.54% on GSM8K and 92.08% on MATH, compared to 82.50% and 74.82% for single-model training. On harder datasets, the 3B+4B pair reaches Pass@2 of 77.34% on GPQA (trained on 348 examples) and 79.65% on AIME (trained on 792 examples), using a training-time budget of at most 1536 context tokens and 3072 generated tokens. Overall, these results show that training-time collaboration can reliably convert model complementarity into large gains without scaling model size.

