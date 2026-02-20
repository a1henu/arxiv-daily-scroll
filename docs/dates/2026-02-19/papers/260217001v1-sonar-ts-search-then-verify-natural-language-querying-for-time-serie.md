---
layout: default
title: Sonar-TS: Search-Then-Verify Natural Language Querying for Time Series Databases
---

# Sonar-TS: Search-Then-Verify Natural Language Querying for Time Series Databases
**arXiv**：[2602.17001v1](https://arxiv.org/abs/2602.17001) · [PDF](https://arxiv.org/pdf/2602.17001.pdf)  
**作者**：Zhao Tan, Yiji Zhao, Shiyu Wang, Chang Xu, Yuxuan Liang, Xiping Liu, Shirui Pan, Ming Jin  

**一句话要点**：提出Sonar-TS框架以解决时间序列数据库的自然语言查询问题

**关键词**：时间序列数据库, 自然语言查询, 神经符号框架, 搜索-验证管道, 基准测试

## 3 点简述
- 核心问题：现有方法难以处理连续形态意图和超长历史时间序列查询
- 方法要点：采用神经符号框架，通过搜索-验证管道结合SQL和Python程序
- 实验或效果：引入NLQTSBench基准，实验显示Sonar-TS能有效处理复杂查询

## 摘要（原文）

> Natural Language Querying for Time Series Databases (NLQ4TSDB) aims to assist non-expert users retrieve meaningful events, intervals, and summaries from massive temporal records. However, existing Text-to-SQL methods are not designed for continuous morphological intents such as shapes or anomalies, while time series models struggle to handle ultra-long histories. To address these challenges, we propose Sonar-TS, a neuro-symbolic framework that tackles NLQ4TSDB via a Search-Then-Verify pipeline. Analogous to active sonar, it utilizes a feature index to ping candidate windows via SQL, followed by generated Python programs to lock on and verify candidates against raw signals. To enable effective evaluation, we introduce NLQTSBench, the first large-scale benchmark designed for NLQ over TSDB-scale histories. Our experiments highlight the unique challenges within this domain and demonstrate that Sonar-TS effectively navigates complex temporal queries where traditional methods fail. This work presents the first systematic study of NLQ4TSDB, offering a general framework and evaluation standard to facilitate future research.

