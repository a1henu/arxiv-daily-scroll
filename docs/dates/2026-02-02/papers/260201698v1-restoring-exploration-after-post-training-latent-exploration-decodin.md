---
layout: default
title: Restoring Exploration after Post-Training: Latent Exploration Decoding for Large Reasoning Models
---

# Restoring Exploration after Post-Training: Latent Exploration Decoding for Large Reasoning Models
**arXiv**：[2602.01698v1](https://arxiv.org/abs/2602.01698) · [PDF](https://arxiv.org/pdf/2602.01698.pdf)  
**作者**：Wenhui Tan, Fiorenzo Parascandolo, Enver Sangineto, Jianzhong Ju, Zhenbo Luo, Qian Cao, Rita Cucchiara, Ruihua Song, Jian Luan  

**一句话要点**：提出潜在探索解码以解决大型推理模型后训练中的探索崩溃问题

**关键词**：大型推理模型, 后训练探索, 熵不对称, 深度条件解码, 推理性能提升

## 3 点简述
- 核心问题：后训练导致探索崩溃，温度采样无法提升推理准确性
- 方法要点：基于熵不对称性，通过深度条件解码聚合中间层后验
- 实验或效果：无需额外训练，在多个基准上提升pass@1和pass@16准确率

## 摘要（原文）

> Large Reasoning Models (LRMs) have recently achieved strong mathematical and code reasoning performance through Reinforcement Learning (RL) post-training. However, we show that modern reasoning post-training induces an unintended exploration collapse: temperature-based sampling no longer increases pass@$n$ accuracy. Empirically, the final-layer posterior of post-trained LRMs exhibit sharply reduced entropy, while the entropy of intermediate layers remains relatively high. Motivated by this entropy asymmetry, we propose Latent Exploration Decoding (LED), a depth-conditioned decoding strategy. LED aggregates intermediate posteriors via cumulative sum and selects depth configurations with maximal entropy as exploration candidates. Without additional training or parameters, LED consistently improves pass@1 and pass@16 accuracy by 0.61 and 1.03 percentage points across multiple reasoning benchmarks and models. Project page: https://GitHub.com/Xiaomi-Research/LED.

