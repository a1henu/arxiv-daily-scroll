---
layout: default
title: BEAR: Towards Beam-Search-Aware Optimization for Recommendation with Large Language Models
---

# BEAR: Towards Beam-Search-Aware Optimization for Recommendation with Large Language Models
**arXiv**：[2601.22925v1](https://arxiv.org/abs/2601.22925) · [PDF](https://arxiv.org/pdf/2601.22925.pdf)  
**作者**：Weiqin Yang, Bohao Wang, Zhenxiang Xu, Jiawei Chen, Shengjia Zhang, Jingbang Chen, Canghong Jin, Can Wang  

**一句话要点**：提出BEAR正则化方法以解决大语言模型推荐中训练与推理不一致问题

**关键词**：大语言模型推荐, 束搜索优化, 训练推理一致性, 正则化方法, 监督微调

## 3 点简述
- 核心问题：监督微调优化整体概率，但束搜索可能因前缀概率不足而提前丢弃正项
- 方法要点：通过强制正项每个解码步的令牌排名在前B内，实现束搜索感知的优化
- 实验或效果：在四个真实数据集上显著超越基线，计算开销可忽略

## 摘要（原文）

> Recent years have witnessed a rapid surge in research leveraging Large Language Models (LLMs) for recommendation. These methods typically employ supervised fine-tuning (SFT) to adapt LLMs to recommendation scenarios, and utilize beam search during inference to efficiently retrieve $B$ top-ranked recommended items. However, we identify a critical training-inference inconsistency: while SFT optimizes the overall probability of positive items, it does not guarantee that such items will be retrieved by beam search even if they possess high overall probabilities. Due to the greedy pruning mechanism, beam search can prematurely discard a positive item once its prefix probability is insufficient.
>   To address this inconsistency, we propose BEAR (Beam-SEarch-Aware Regularization), a novel fine-tuning objective that explicitly accounts for beam search behavior during training. Rather than directly simulating beam search for each instance during training, which is computationally prohibitive, BEAR enforces a relaxed necessary condition: each token in a positive item must rank within the top-$B$ candidate tokens at each decoding step. This objective effectively mitigates the risk of incorrect pruning while incurring negligible computational overhead compared to standard SFT. Extensive experiments across four real-world datasets demonstrate that BEAR significantly outperforms strong baselines. Code will be released upon acceptance.

