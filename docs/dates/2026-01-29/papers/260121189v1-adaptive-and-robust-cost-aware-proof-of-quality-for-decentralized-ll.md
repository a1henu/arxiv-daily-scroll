---
layout: default
title: Adaptive and Robust Cost-Aware Proof of Quality for Decentralized LLM Inference Networks
---

# Adaptive and Robust Cost-Aware Proof of Quality for Decentralized LLM Inference Networks
**arXiv**：[2601.21189v1](https://arxiv.org/abs/2601.21189) · [PDF](https://arxiv.org/pdf/2601.21189.pdf)  
**作者**：Arther Tian, Alex Ding, Frank Chen, Simon Wu, Aaron Chan  

**一句话要点**：提出自适应鲁棒成本感知质量证明机制，以增强去中心化LLM推理网络中的激励对齐

**关键词**：去中心化推理网络, 质量证明机制, 鲁棒共识聚合, 评估者可靠性, 对抗性攻击, 成本感知激励

## 3 点简述
- 核心问题：去中心化LLM推理网络中，评估者异质性和恶意评分操纵会扭曲共识，削弱激励对齐。
- 方法要点：扩展成本感知质量证明，引入鲁棒聚合规则（如中位数、修剪均值）和自适应信任加权共识，以抵御攻击。
- 实验或效果：在问答和摘要任务中，鲁棒聚合提高了共识与真实代理的对齐度，降低了对噪声和策略攻击的敏感性。

## 摘要（原文）

> Decentralized large language model inference networks require lightweight mechanisms to reward high quality outputs under heterogeneous latency and cost. Proof of Quality provides scalable verification by sampling evaluator nodes that score candidate outputs, then aggregating their scores into a consensus signal that determines rewards. However, evaluator heterogeneity and malicious score manipulation can distort consensus and inflate payouts, which weakens incentive alignment in open participation settings.
>   This paper extends a cost-aware Proof of Quality mechanism by adding adversary-resilient consensus formation. We study robust aggregation rules, including median and trimmed mean, and an adaptive trust-weighted consensus that updates evaluator weights from deviation signals. Using question answering and summarization workloads with a ground truth proxy for offline analysis, we quantify evaluator reliability and show strong variance across evaluators, including task-dependent misalignment that can invert correlations. We then evaluate robustness under four adversarial strategies, including noise injection, boosting, sabotage, and intermittent manipulation, across a sweep of malicious ratios and evaluator sample sizes. Our results show that robust aggregation improves consensus alignment with the ground truth proxy and reduces sensitivity to noisy and strategic attacks compared with simple averaging. We further characterize the operational trade-off introduced by evaluator sampling, where larger evaluator sets reduce evaluator rewards and increase payoff variance while inference rewards remain relatively stable in our configuration. These findings motivate robust consensus as a default component for cost-aware Proof of Quality and provide practical guidance for selecting evaluator sampling parameters under adversarial risk and resource constraints.

