---
layout: default
title: NSR-Boost: A Neuro-Symbolic Residual Boosting Framework for Industrial Legacy Models
---

# NSR-Boost: A Neuro-Symbolic Residual Boosting Framework for Industrial Legacy Models
**arXiv**：[2601.10457v1](https://arxiv.org/abs/2601.10457) · [PDF](https://arxiv.org/pdf/2601.10457.pdf)  
**作者**：Ziming Dai, Dabiao Ma, Jinle Tong, Mengyuan Han, Jian Yang, Haojun Fei  

**一句话要点**：提出NSR-Boost神经符号残差提升框架，以非侵入方式修复工业遗留模型在硬区域的预测失败。

**关键词**：神经符号学习, 残差提升, 工业遗留模型, 非侵入式修复, 长尾风险, 贝叶斯优化

## 3 点简述
- 核心问题：工业高并发环境中升级遗留模型面临重训练成本高和系统风险大的挑战。
- 方法要点：通过残差识别硬区域，利用LLM生成符号代码结构并贝叶斯优化微调，轻量聚合器动态集成专家与遗留模型输出。
- 实验或效果：在公开和私有数据集上超越SOTA基线，实际在线数据表现优异，有效捕获传统模型遗漏的长尾风险。

## 摘要（原文）

> Although the Gradient Boosted Decision Trees (GBDTs) dominate industrial tabular applications, upgrading legacy models in high-concurrency production environments still faces prohibitive retraining costs and systemic risks. To address this problem, we present NSR-Boost, a neuro-symbolic residual boosting framework designed specifically for industrial scenarios. Its core advantage lies in being "non-intrusive". It treats the legacy model as a frozen model and performs targeted repairs on "hard regions" where predictions fail. The framework comprises three key stages: first, finding hard regions through residuals, then generating interpretable experts by generating symbolic code structures using Large Language Model (LLM) and fine-tuning parameters using Bayesian optimization, and finally dynamically integrating experts with legacy model output through a lightweight aggregator. We report on the successful deployment of NSR-Boost within the core financial risk control system at Qfin Holdings. This framework not only significantly outperforms state-of-the-art (SOTA) baselines across six public datasets and one private dataset, more importantly, shows excellent performance gains on real-world online data. In conclusion, it effectively captures long-tail risks missed by traditional models and offers a safe, low-cost evolutionary paradigm for industry.

