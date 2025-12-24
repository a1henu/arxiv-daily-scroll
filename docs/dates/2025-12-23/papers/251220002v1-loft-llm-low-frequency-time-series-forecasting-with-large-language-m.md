---
layout: default
title: LoFT-LLM: Low-Frequency Time-Series Forecasting with Large Language Models
---

# LoFT-LLM: Low-Frequency Time-Series Forecasting with Large Language Models
**arXiv**：[2512.20002v1](https://arxiv.org/abs/2512.20002) · [PDF](https://arxiv.org/pdf/2512.20002.pdf)  
**作者**：Jiacheng You, Jingcheng Yang, Yuhang Xie, Zhongxuan Wu, Xiucheng Li, Feng Li, Pengjie Wang, Jian Xu, Bo Zheng, Xinyang Chen  

**一句话要点**：提出LoFT-LLM，通过低频学习和LLM语义校准，解决金融和能源时间序列预测中数据有限和噪声复杂的问题。

**关键词**：时间序列预测, 低频学习, 大语言模型, 少样本学习, 金融预测, 能源预测

## 3 点简述
- 核心问题：时间序列预测面临训练数据有限、噪声复杂和辅助变量利用不足的挑战。
- 方法要点：结合低频趋势提取、高频残差建模和LLM语义校准，提升预测精度和鲁棒性。
- 实验或效果：在金融和能源数据集上，LoFT-LLM在全数据和少样本场景下均优于基线，提供高准确性和可解释性。

## 摘要（原文）

> Time-series forecasting in real-world applications such as finance and energy often faces challenges due to limited training data and complex, noisy temporal dynamics. Existing deep forecasting models typically supervise predictions using full-length temporal windows, which include substantial high-frequency noise and obscure long-term trends. Moreover, auxiliary variables containing rich domain-specific information are often underutilized, especially in few-shot settings. To address these challenges, we propose LoFT-LLM, a frequency-aware forecasting pipeline that integrates low-frequency learning with semantic calibration via a large language model (LLM). Firstly, a Patch Low-Frequency forecasting Module (PLFM) extracts stable low-frequency trends from localized spectral patches. Secondly, a residual learner then models high-frequency variations. Finally, a fine-tuned LLM refines the predictions by incorporating auxiliary context and domain knowledge through structured natural language prompts. Extensive experiments on financial and energy datasets demonstrate that LoFT-LLM significantly outperforms strong baselines under both full-data and few-shot regimes, delivering superior accuracy, robustness, and interpretability.

