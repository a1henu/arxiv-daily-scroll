---
layout: default
title: Adaptive Information Routing for Multimodal Time Series Forecasting
---

# Adaptive Information Routing for Multimodal Time Series Forecasting
**arXiv**：[2512.10229v1](https://arxiv.org/abs/2512.10229) · [PDF](https://arxiv.org/pdf/2512.10229.pdf)  
**作者**：Jun Seo, Hyeokjun Choe, Seohui Bae, Soyeon Park, Wonbin Ahn, Taeyoon Lim, Junhyuk Kang, Sangjun Han, Jaehoon Lee, Dongwan Kang, Minjae Kim, Sungdong Yoo, Soonyoung Lee  

**一句话要点**：提出自适应信息路由框架，利用文本动态引导时间序列模型以提升多模态预测精度

**关键词**：多模态时间序列预测, 自适应信息路由, 文本引导模型, 时间序列建模, 市场数据预测

## 3 点简述
- 核心问题：传统时间序列预测依赖历史数据，信息有限导致准确性不足，需结合文本等多模态数据。
- 方法要点：引入自适应信息路由框架，通过文本控制多变量时间序列信息的组合方式和程度，而非简单作为辅助特征。
- 实验或效果：基于原油价格和汇率等真实市场数据实验，证明该框架能有效利用文本输入调制模型行为，显著提高预测准确性。

## 摘要（原文）

> Time series forecasting is a critical task for artificial intelligence with numerous real-world applications. Traditional approaches primarily rely on historical time series data to predict the future values. However, in practical scenarios, this is often insufficient for accurate predictions due to the limited information available. To address this challenge, multimodal time series forecasting methods which incorporate additional data modalities, mainly text data, alongside time series data have been explored. In this work, we introduce the Adaptive Information Routing (AIR) framework, a novel approach for multimodal time series forecasting. Unlike existing methods that treat text data on par with time series data as interchangeable auxiliary features for forecasting, AIR leverages text information to dynamically guide the time series model by controlling how and to what extent multivariate time series information should be combined. We also present a text-refinement pipeline that employs a large language model to convert raw text data into a form suitable for multimodal forecasting, and we introduce a benchmark that facilitates multimodal forecasting experiments based on this pipeline. Experiment results with the real world market data such as crude oil price and exchange rates demonstrate that AIR effectively modulates the behavior of the time series model using textual inputs, significantly enhancing forecasting accuracy in various time series forecasting tasks.

