---
layout: default
title: FLAME: Flow Enhanced Legendre Memory Models for General Time Series Forecasting
---

# FLAME: Flow Enhanced Legendre Memory Models for General Time Series Forecasting
**arXiv**：[2512.14253v1](https://arxiv.org/abs/2512.14253) · [PDF](https://arxiv.org/pdf/2512.14253.pdf)  
**作者**：Xingjian Wu, Hanyin Cheng, Xiangfei Qiu, Zhengyu Li, Jilin Hu, Chenjuan Guo, Bin Yang  

**一句话要点**：提出FLAME模型，结合Legendre Memory和归一化流，实现高效稳健的时间序列确定性及概率预测。

**关键词**：时间序列预测, Legendre Memory, 归一化流, 零样本学习, 概率建模

## 3 点简述
- 核心问题：时间序列预测需兼顾确定性、概率性、高效性和长程推理能力。
- 方法要点：采用Legendre Memory变体（LegT和LegS）编码解码，增强泛化；归一化流预测头建模复杂分布。
- 实验或效果：在TSFM-Bench和ProbTS基准上，零样本性能达到先进水平。

## 摘要（原文）

> In this work, we introduce FLAME, a family of extremely lightweight and capable Time Series Foundation Models, which support both deterministic and probabilistic forecasting via generative probabilistic modeling, thus ensuring both efficiency and robustness. FLAME utilizes the Legendre Memory for strong generalization capabilities. Through adapting variants of Legendre Memory, i.e., translated Legendre (LegT) and scaled Legendre (LegS), in the Encoding and Decoding phases, FLAME can effectively capture the inherent inductive bias within data and make efficient long-range inferences. To enhance the accuracy of probabilistic forecasting while keeping efficient, FLAME adopts a Normalization Flow based forecasting head, which can model the arbitrarily intricate distributions over the forecasting horizon in a generative manner. Comprehensive experiments on well-recognized benchmarks, including TSFM-Bench and ProbTS, demonstrate the consistent state-of-the-art zero-shot performance of FLAME on both deterministic and probabilistic forecasting tasks.

