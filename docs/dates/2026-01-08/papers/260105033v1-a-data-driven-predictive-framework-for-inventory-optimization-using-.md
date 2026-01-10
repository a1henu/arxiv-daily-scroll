---
layout: default
title: A Data-Driven Predictive Framework for Inventory Optimization Using Context-Augmented Machine Learning Models
---

# A Data-Driven Predictive Framework for Inventory Optimization Using Context-Augmented Machine Learning Models
**arXiv**：[2601.05033v1](https://arxiv.org/abs/2601.05033) · [PDF](https://arxiv.org/pdf/2601.05033.pdf)  
**作者**：Anees Fatima, Mohammad Abdus Salam  

**一句话要点**：提出基于上下文增强机器学习模型的库存优化预测框架，应用于零售和自动售货机系统。

**关键词**：需求预测, 库存优化, 机器学习, 供应链管理, 外部变量集成

## 3 点简述
- 核心问题：传统需求预测方法忽略天气、节假日等外部因素，导致供应链管理效率低下。
- 方法要点：集成XGBoost、ARIMA、Fb Prophet和SVR算法，并系统纳入星期、节假日等外部变量以提升预测精度。
- 实验或效果：XGBoost在加入外部变量后表现最佳，MAE最低为22.7，外部因素显著改善模型性能。

## 摘要（原文）

> Demand forecasting in supply chain management (SCM) is critical for optimizing inventory, reducing waste, and improving customer satisfaction. Conventional approaches frequently neglect external influences like weather, festivities, and equipment breakdowns, resulting in inefficiencies. This research investigates the use of machine learning (ML) algorithms to improve demand prediction in retail and vending machine sectors. Four machine learning algorithms. Extreme Gradient Boosting (XGBoost), Autoregressive Integrated Moving Average (ARIMA), Facebook Prophet (Fb Prophet), and Support Vector Regression (SVR) were used to forecast inventory requirements. Ex-ternal factors like weekdays, holidays, and sales deviation indicators were methodically incorporated to enhance precision. XGBoost surpassed other models, reaching the lowest Mean Absolute Error (MAE) of 22.7 with the inclusion of external variables. ARIMAX and Fb Prophet demonstrated noteworthy enhancements, whereas SVR fell short in performance. Incorporating external factors greatly improves the precision of demand forecasting models, and XGBoost is identified as the most efficient algorithm. This study offers a strong framework for enhancing inventory management in retail and vending machine systems.

