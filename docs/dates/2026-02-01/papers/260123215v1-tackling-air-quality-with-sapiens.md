---
layout: default
title: Tackling air quality with SAPIENS
---

# Tackling air quality with SAPIENS
**arXiv**：[2601.23215v1](https://arxiv.org/abs/2601.23215) · [PDF](https://arxiv.org/pdf/2601.23215.pdf)  
**作者**：Marcella Bona, Nathan Heatley, Jia-Chen Hua, Adriana Lara, Valeria Legaria-Santiago, Alberto Luviano Juarez, Fernando Moreno-Gomez, Jocelyn Richardson, Natan Vilchis, Xiwen Shirley Zheng  

**一句话要点**：提出基于交通数据的环状描述方法，以预测墨西哥城超局部动态空气质量。

**关键词**：空气质量预测, 交通数据分析, 偏最小二乘回归, 超局部建模, 城市环境监测

## 3 点简述
- 核心问题：城市空气质量监测粗粒度，交通数据细粒度但关系未充分利用。
- 方法要点：将彩色交通图转换为同心环描述，使用偏最小二乘回归预测污染水平。
- 实验或效果：优化训练样本提升预测性能，工作流程可适配其他城市场景。

## 摘要（原文）

> Air pollution is a chronic problem in large cities worldwide and awareness is rising as the long-term health implications become clearer. Vehicular traffic has been identified as a major contributor to poor air quality. In a lot of cities the publicly available air quality measurements and forecasts are coarse-grained both in space and time. However, in general, real-time traffic intensity data is openly available in various forms and is fine-grained. In this paper, we present an in-depth study of pollution sensor measurements combined with traffic data from Mexico City. We analyse and model the relationship between traffic intensity and air quality with the aim to provide hyper-local, dynamic air quality forecasts. We developed an innovative method to represent traffic intensities by transforming simple colour-coded traffic maps into concentric ring-based descriptions, enabling improved characterisation of traffic conditions. Using Partial Least Squares Regression, we predict pollution levels based on these newly defined traffic intensities. The model was optimised with various training samples to achieve the best predictive performance and gain insights into the relationship between pollutants and traffic. The workflow we have designed is straightforward and adaptable to other contexts, like other cities beyond the specifics of our dataset.

