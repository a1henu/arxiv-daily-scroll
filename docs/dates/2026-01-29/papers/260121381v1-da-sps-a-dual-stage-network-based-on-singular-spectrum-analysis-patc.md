---
layout: default
title: DA-SPS: A Dual-stage Network based on Singular Spectrum Analysis, Patching-strategy and Spearman-correlation for Multivariate Time-series Prediction
---

# DA-SPS: A Dual-stage Network based on Singular Spectrum Analysis, Patching-strategy and Spearman-correlation for Multivariate Time-series Prediction
**arXiv**：[2601.21381v1](https://arxiv.org/abs/2601.21381) · [PDF](https://arxiv.org/pdf/2601.21381.pdf)  
**作者**：Tianhao Zhang, Shusen Ma, Yu Kang, Yun-Bo Zhao  

**一句话要点**：提出DA-SPS模型，通过双阶段网络处理多元时间序列预测，提升目标变量预测精度。

**关键词**：多元时间序列预测, 奇异谱分析, Spearman相关性, 双阶段网络, 注意力机制, 长短期记忆网络

## 3 点简述
- 核心问题：现有方法未有效考虑外生变量对目标变量的影响，且未充分提取序列的复杂时间模式信息。
- 方法要点：采用双阶段结构，TVPS阶段用SSA和LSTM处理目标变量，EVPS阶段用Spearman相关性和L-Attention筛选分析外生变量。
- 实验或效果：在四个公共数据集上优于现有方法，并在私有笔记本电脑主板测试数据集上验证了实际应用效果。

## 摘要（原文）

> Multivariate time-series forecasting, as a typical problem in the field of time series prediction, has a wide range of applications in weather forecasting, traffic flow prediction, and other scenarios. However, existing works do not effectively consider the impact of extraneous variables on the prediction of the target variable. On the other hand, they fail to fully extract complex sequence information based on various time patterns of the sequences. To address these drawbacks, we propose a DA-SPS model, which adopts different modules for feature extraction based on the information characteristics of different variables. DA-SPS mainly consists of two stages: the target variable processing stage (TVPS) and the extraneous variables processing stage (EVPS). In TVPS, the model first uses Singular Spectrum Analysis (SSA) to process the target variable sequence and then uses Long Short-Term Memory (LSTM) and P-Conv-LSTM which deploys a patching strategy to extract features from trend and seasonality components, respectively. In EVPS, the model filters extraneous variables that have a strong correlation with the target variate by using Spearman correlation analysis and further analyses them using the L-Attention module which consists of LSTM and attention mechanism. Finally, the results obtained by TVPS and EVPS are combined through weighted summation and linear mapping to produce the final prediction. The results on four public datasets demonstrate that the DA-SPS model outperforms existing state-of-the-art methods. Additionally, its performance in real-world scenarios is further validated using a private dataset collected by ourselves, which contains the test items' information on laptop motherboards.

