---
layout: default
title: Aura: Universal Multi-dimensional Exogenous Integration for Aviation Time Series
---

# Aura: Universal Multi-dimensional Exogenous Integration for Aviation Time Series
**arXiv**：[2603.05092v1](https://arxiv.org/abs/2603.05092) · [PDF](https://arxiv.org/pdf/2603.05092.pdf)  
**作者**：Jiafeng Lin, Mengren Zheng, Simeng Ye, Yuxuan Wang, Huan Zhang, Yuhui Liu, Zhongyi Pei, Jianmin Wang  

**一句话要点**：提出Aura框架以解决航空时间序列中多维外生因素集成问题

**关键词**：时间序列预测, 外生因素集成, 航空维护, 异质编码, 工业应用

## 3 点简述
- 核心问题：航空时间序列预测需集成多维外生因素，但现有模型难以捕捉异质交互。
- 方法要点：Aura通过三方编码机制，根据交互模式组织并编码异质外部信息。
- 实验或效果：在南方航空大规模数据集上，Aura实现最优性能，提升航空安全与可靠性。

## 摘要（原文）

> Time series forecasting has witnessed an increasing demand across diverse industrial applications, where accurate predictions are pivotal for informed decision-making. Beyond numerical time series data, reliable forecasting in practical scenarios requires integrating diverse exogenous factors. Such exogenous information is often multi-dimensional or even multimodal, introducing heterogeneous interactions that unimodal time series models struggle to capture. In this paper, we delve into an aviation maintenance scenario and identify three distinct types of exogenous factors that influence temporal dynamics through distinct interaction modes. Based on this empirical insight, we propose Aura, a universal framework that explicitly organizes and encodes heterogeneous external information according to its interaction mode with the target time series. Specifically, Aura utilizes a tailored tripartite encoding mechanism to embed heterogeneous features into well-established time series models, ensuring seamless integration of non-sequential context. Extensive experiments on a large-scale, three-year industrial dataset from China Southern Airlines, covering the Boeing 777 and Airbus A320 fleets, demonstrate that Aura consistently achieves state-of-the-art performance across all baselines and exhibits superior adaptability. Our findings highlight Aura's potential as a general-purpose enhancement for aviation safety and reliability.

