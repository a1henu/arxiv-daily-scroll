---
layout: default
title: Bridging Forecast Accuracy and Inventory KPIs: A Simulation-Based Software Framework
---

# Bridging Forecast Accuracy and Inventory KPIs: A Simulation-Based Software Framework
**arXiv**：[2601.21844v1](https://arxiv.org/abs/2601.21844) · [PDF](https://arxiv.org/pdf/2601.21844.pdf)  
**作者**：So Fukuhara, Abdallah Alabdallah, Nuwan Gunasekara, Slawomir Nowaczyk  

**一句话要点**：提出基于仿真的软件框架，以评估预测模型对汽车售后库存绩效的影响。

**关键词**：库存管理, 需求预测, 仿真框架, 运营绩效评估, 汽车售后市场

## 3 点简述
- 核心问题：传统预测模型评估依赖统计精度，但未明确其与库存关键绩效指标（如成本和服务水平）的关系。
- 方法要点：开发闭环仿真框架，包括需求生成器、预测模块和库存控制模拟器，实现模型在真实库存环境中的系统评估。
- 实验或效果：通过多场景仿真，发现统计精度提升不一定改善运营绩效，不同模型在成本-服务权衡上差异显著。

## 摘要（原文）

> Efficient management of spare parts inventory is crucial in the automotive aftermarket, where demand is highly intermittent and uncertainty drives substantial cost and service risks. Forecasting is therefore central, but the quality of a forecasting model should be judged not by statistical accuracy (e.g., MAE, RMSE, IAE) but rather by its impact on key operational performance indicators (KPIs), such as total cost and service level. Yet most existing work evaluates models exclusively using accuracy metrics, and the relationship between these metrics and operational KPIs remains poorly understood. To address this gap, we propose a decision-centric simulation software framework that enables systematic evaluation of forecasting model in realistic inventory management setting. The framework comprises: (i) a synthetic demand generator tailored to spare-parts demand characteristics, (ii) a flexible forecasting module that can host arbitrary predictive models, and (iii) an inventory control simulator that consumes the forecasts and computes operational KPIs. This closed-loop setup enables researchers to evaluate models not only in terms of statistical error but also in terms of their downstream implications for inventory decisions. Using a wide range of simulation scenarios, we show that improvements in conventional accuracy metrics do not necessarily translate into better operational performance, and that models with similar statistical error profiles can induce markedly different cost-service trade-offs. We analyze these discrepancies to characterize how specific aspects of forecast performance affect inventory outcomes and derive guidance for model selection. Overall, the framework operationalizes the link between demand forecasting and inventory management, shifting evaluation from purely predictive accuracy toward operational relevance in the automotive aftermarket and related domains.

