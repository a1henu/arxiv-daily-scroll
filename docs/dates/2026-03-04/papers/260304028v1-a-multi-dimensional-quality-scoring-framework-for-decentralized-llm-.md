---
layout: default
title: A Multi-Dimensional Quality Scoring Framework for Decentralized LLM Inference with Proof of Quality
---

# A Multi-Dimensional Quality Scoring Framework for Decentralized LLM Inference with Proof of Quality
**arXiv**：[2603.04028v1](https://arxiv.org/abs/2603.04028) · [PDF](https://arxiv.org/pdf/2603.04028.pdf)  
**作者**：Arther Tian, Alex Ding, Frank Chen, Simon Wu, Aaron Chan  

**一句话要点**：提出多维度质量评分框架以增强去中心化LLM推理中的质量证明机制

**关键词**：去中心化LLM推理, 质量证明, 多维度评分, 语义评估, 对抗性评估, 校准框架

## 3 点简述
- 核心问题：去中心化LLM推理网络需轻量级激励兼容机制评估输出质量，现有质量信号可能不可靠
- 方法要点：将输出质量分解为模型与成本先验、结构质量、语义质量、查询-输出对齐及一致性/不确定性等模块化维度
- 实验或效果：通过校准去除不可靠维度并重新归一化权重，校准后复合评分匹配或超越最佳单评估器和共识基线，并在对抗性评估攻击下与鲁棒聚合和自适应信任加权互补

## 摘要（原文）

> Decentralized large language model (LLM) inference networks can pool heterogeneous compute to scale serving, but they require lightweight and incentive-compatible mechanisms to assess output quality. Prior work introduced cost-aware Proof of Quality (PoQ) and adaptive robust PoQ to allocate rewards under evaluator heterogeneity and adversarial behavior. In this paper, we focus on the quality signal itself and propose a multi-dimensional quality scoring framework that decomposes output quality into modular dimensions, including model and cost priors, structure quality, semantic quality, query-output alignment, and agreement/uncertainty. Using logged outputs from QA and summarization tasks, we systematically audit dimension reliability and show that seemingly reasonable dimensions can be task-dependent and even negatively correlated with reference quality without calibration. While the default composite underperforms a strong single semantic evaluator, ablations reveal that removing unreliable dimensions and re-normalizing weights yields a calibrated composite that matches or exceeds the best single- evaluator and consensus baselines. Finally, we integrate the composite score as a drop-in quality signal in PoQ and demonstrate complementary benefits with robust aggregation and adaptive trust weighting under adversarial evaluator attacks.

