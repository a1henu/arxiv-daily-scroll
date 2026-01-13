---
layout: default
title: A High-Recall Cost-Sensitive Machine Learning Framework for Real-Time Online Banking Transaction Fraud Detection
---

# A High-Recall Cost-Sensitive Machine Learning Framework for Real-Time Online Banking Transaction Fraud Detection
**arXiv**：[2601.07276v1](https://arxiv.org/abs/2601.07276) · [PDF](https://arxiv.org/pdf/2601.07276.pdf)  
**作者**：Karthikeyan V. R., Premnath S., Kavinraaj S., J. Sangeetha  

**一句话要点**：提出基于成本敏感机器学习的实时在线银行交易欺诈检测框架，以高召回率减少漏检

**关键词**：在线银行欺诈检测, 成本敏感机器学习, 高召回率, 实时交易监控, 不平衡数据分类

## 3 点简述
- 核心问题：数字银行欺诈日益复杂，传统规则和精度导向方法难以应对新骗局和行为变化，漏检导致高损失。
- 方法要点：采用集成学习方法，通过智能阈值调整实现成本敏感决策，优化高召回率。
- 实验或效果：在真实世界不平衡交易数据上测试，检测约91%欺诈，优于标准规则系统，并集成实时交易流和浏览器插件。

## 摘要（原文）

> Fraudulent activities on digital banking services are becoming more intricate by the day, challenging existing defenses. While older rule driven methods struggle to keep pace, even precision focused algorithms fall short when new scams are introduced. These tools typically overlook subtle shifts in criminal behavior, missing crucial signals. Because silent breaches cost institutions far more than flagged but legitimate actions, catching every possible case is crucial. High sensitivity to actual threats becomes essential when oversight leads to heavy losses. One key aim here involves reducing missed fraud cases without spiking incorrect alerts too much. This study builds a system using group learning methods adjusted through smart threshold choices. Using real world transaction records shared openly, where cheating acts rarely appear among normal activities, tests are run under practical skewed distributions. The outcomes reveal that approximately 91 percent of actual fraud is detected, outperforming standard setups that rely on unchanging rules when dealing with uneven examples across classes. When tested in live settings, the fraud detection system connects directly to an online banking transaction flow, stopping questionable activities before they are completed. Alongside this setup, a browser add on built for Chrome is designed to flag deceptive web links and reduce threats from harmful sites. These results show that adjusting decisions by cost impact and validating across entire systems makes deployment more stable and realistic for today's digital banking platforms.

