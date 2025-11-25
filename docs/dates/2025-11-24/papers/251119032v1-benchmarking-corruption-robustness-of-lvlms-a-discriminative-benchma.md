---
layout: default
title: Benchmarking Corruption Robustness of LVLMs: A Discriminative Benchmark and Robustness Alignment Metric
---

# Benchmarking Corruption Robustness of LVLMs: A Discriminative Benchmark and Robustness Alignment Metric
**arXiv**：[2511.19032v1](https://arxiv.org/abs/2511.19032) · [PDF](https://arxiv.org/pdf/2511.19032.pdf)  
**作者**：Xiangjie Sui, Songyang Li, Hanwei Zhu, Baoliang Chen, Yuming Fang, Xin Sun  

**一句话要点**：提出Bench-C基准和RAS指标以评估LVLM在视觉损坏下的鲁棒性

**关键词**：视觉语言模型, 鲁棒性评估, 基准构建, 预测结构分析, 视觉损坏, 不确定性度量

## 3 点简述
- 现有评估范式存在样本低区分度和指标不全面问题，掩盖模型鲁棒性差距
- 引入Bench-C基准强调区分性样本，并设计RAS指标量化预测结构退化
- 实验揭示模型在损坏下行为模式，如错误置信和预测结构整体退化

## 摘要（原文）

> Despite the remarkable reasoning abilities of large vision-language models (LVLMs), their robustness under visual corruptions remains insufficiently studied. Existing evaluation paradigms exhibit two major limitations: 1) the dominance of low-discriminative samples in current datasets masks the real robustness gap between models; and 2) conventional accuracy-based metric fail to capture the degradation of the underlying prediction structure. To bridge these gaps, we introduce Bench-C, a comprehensive benchmark emphasizing discriminative samples for assessing corruption robustness, where a selection strategy is proposed to jointly consider the prediction inconsistency under corruption and the semantic diversity. Furthermore, we propose the Robustness Alignment Score (RAS), a unified metric that measures degradation in logit-level prediction structure by considering the shifts in prediction uncertainty and calibration alignment. Comprehensive experiments and analysis reveal several interesting findings: 1) model behaviors exhibit distinguish patterns under corruptions, such as erroneous confidence and hesitation; 2) despite subtle corruption may lead to a slight accuracy gain, the overall prediction structure still degrades; 3) by decomposing corruption robustness into destructive and corrective components, the distinct failure and recovery patterns across models can be revealed.

