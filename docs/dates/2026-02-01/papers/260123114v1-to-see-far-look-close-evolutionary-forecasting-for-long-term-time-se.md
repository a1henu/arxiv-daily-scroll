---
layout: default
title: To See Far, Look Close: Evolutionary Forecasting for Long-term Time Series
---

# To See Far, Look Close: Evolutionary Forecasting for Long-term Time Series
**arXiv**：[2601.23114v1](https://arxiv.org/abs/2601.23114) · [PDF](https://arxiv.org/pdf/2601.23114.pdf)  
**作者**：Jiaming Ma, Siyuan Mu, Ruilin Tang, Haofeng Ma, Qihe Huang, Zhengyang Zhou, Pengkun Wang, Binwu Wang, Yang Wang  

**一句话要点**：提出进化预测范式以解决长时序预测中直接预测的优化病理问题

**关键词**：长时序预测, 进化预测, 优化病理, 梯度冲突, 生成框架, 外推稳定性

## 3 点简述
- 揭示直接预测范式在长时序预测中存在梯度冲突的优化病理
- 提出进化预测作为统一生成框架，证明直接预测是其退化特例
- 实验表明单一进化预测模型超越任务特定直接预测集成，展现稳定外推能力

## 摘要（原文）

> The prevailing Direct Forecasting (DF) paradigm dominates Long-term Time Series Forecasting (LTSF) by forcing models to predict the entire future horizon in a single forward pass. While efficient, this rigid coupling of output and evaluation horizons necessitates computationally prohibitive re-training for every target horizon. In this work, we uncover a counter-intuitive optimization anomaly: models trained on short horizons-when coupled with our proposed Evolutionary Forecasting (EF) paradigm-significantly outperform those trained directly on long horizons. We attribute this success to the mitigation of a fundamental optimization pathology inherent in DF, where conflicting gradients from distant futures cripple the learning of local dynamics. We establish EF as a unified generative framework, proving that DF is merely a degenerate special case of EF. Extensive experiments demonstrate that a singular EF model surpasses task-specific DF ensembles across standard benchmarks and exhibits robust asymptotic stability in extreme extrapolation. This work propels a paradigm shift in LTSF: moving from passive Static Mapping to autonomous Evolutionary Reasoning.

