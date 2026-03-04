---
layout: default
title: FlashEvaluator: Expanding Search Space with Parallel Evaluation
---

# FlashEvaluator: Expanding Search Space with Parallel Evaluation
**arXiv**：[2603.02565v1](https://arxiv.org/abs/2603.02565) · [PDF](https://arxiv.org/pdf/2603.02565.pdf)  
**作者**：Chao Feng, Yuanhao Pu, Chenghao Zhang, Shanqi Liu, Shuchang Liu, Xiang Li, Yongqi Liu, Lantao Hu, Kaiqiao Zhan, Han Li, Kun Gai  

**一句话要点**：提出FlashEvaluator以解决生成器-评估器框架中评估器效率低和准确性不足的问题

**关键词**：生成器-评估器框架, 并行评估, 跨序列比较, 推荐系统, 自然语言处理, 计算效率

## 3 点简述
- 传统评估器独立处理序列，缺乏跨序列比较且并行化差，导致准确性和效率低下
- FlashEvaluator通过跨序列令牌信息共享和单次前向传递处理所有序列，实现亚线性计算复杂度
- 在推荐和NLP任务中实验验证其优势，并已在快手在线推荐系统部署带来显著收益

## 摘要（原文）

> The Generator-Evaluator (G-E) framework, i.e., evaluating K sequences from a generator and selecting the top-ranked one according to evaluator scores, is a foundational paradigm in tasks such as Recommender Systems (RecSys) and Natural Language Processing (NLP). Traditional evaluators process sequences independently, suffering from two major limitations: (1) lack of explicit cross-sequence comparison, leading to suboptimal accuracy; (2) poor parallelization with linear complexity of O(K), resulting in inefficient resource utilization and negative impact on both throughput and latency. To address these challenges, we propose FlashEvaluator, which enables cross-sequence token information sharing and processes all sequences in a single forward pass. This yields sublinear computational complexity that improves the system's efficiency and supports direct inter-sequence comparisons that improve selection accuracy. The paper also provides theoretical proofs and extensive experiments on recommendation and NLP tasks, demonstrating clear advantages over conventional methods. Notably, FlashEvaluator has been deployed in online recommender system of Kuaishou, delivering substantial and sustained revenue gains in practice.

