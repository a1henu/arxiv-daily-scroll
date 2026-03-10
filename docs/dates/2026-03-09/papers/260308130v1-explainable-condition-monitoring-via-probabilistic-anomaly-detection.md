---
layout: default
title: Explainable Condition Monitoring via Probabilistic Anomaly Detection Applied to Helicopter Transmissions
---

# Explainable Condition Monitoring via Probabilistic Anomaly Detection Applied to Helicopter Transmissions
**arXiv**：[2603.08130v1](https://arxiv.org/abs/2603.08130) · [PDF](https://arxiv.org/pdf/2603.08130.pdf)  
**作者**：Aurelio Raffa Ugolini, Jessica Leoni, Valentina Breschi, Damiano Paniccia, Francesco Aldo Tucci, Luigi Capone, Mara Tanelli  

**一句话要点**：提出基于健康数据概率分布的可解释状态监测方法，应用于直升机传动系统异常检测。

**关键词**：可解释状态监测, 概率异常检测, 贝叶斯方法, 直升机传动系统, 健康数据学习, 不确定性量化

## 3 点简述
- 核心问题：故障罕见，需仅依赖健康数据进行状态监测与异常检测。
- 方法要点：采用贝叶斯视角，定义概率偏差度量，实现不确定性量化与结果可解释性。
- 实验或效果：在预测性维护基准和真实直升机传动数据集上验证，检测性能与先进方法竞争。

## 摘要（原文）

> We present a novel Explainable methodology for Condition Monitoring, relying on healthy data only. Since faults are rare events, we propose to focus on learning the probability distribution of healthy observations only, and detect Anomalies at runtime. This objective is achieved via the definition of probabilistic measures of deviation from nominality, which allow to detect and anticipate faults. The Bayesian perspective underpinning our approach allows us to perform Uncertainty Quantification to inform decisions. At the same time, we provide descriptive tools to enhance the interpretability of the results, supporting the deployment of the proposed strategy also in safety-critical applications. The methodology is validated experimentally on two use cases: a publicly available benchmark for Predictive Maintenance, and a real-world Helicopter Transmission dataset collected over multiple years. In both applications, the method achieves competitive detection performance with respect to state-of-the-art anomaly detection methods.

