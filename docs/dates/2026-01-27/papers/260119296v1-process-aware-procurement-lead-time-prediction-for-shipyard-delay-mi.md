---
layout: default
title: Process-Aware Procurement Lead Time Prediction for Shipyard Delay Mitigation
---

# Process-Aware Procurement Lead Time Prediction for Shipyard Delay Mitigation
**arXiv**：[2601.19296v1](https://arxiv.org/abs/2601.19296) · [PDF](https://arxiv.org/pdf/2601.19296.pdf)  
**作者**：Yongjae Lee, Eunhee Park, Daesan Park, Dongho Kim, Jongho Choi, Hyerim Bae  

**一句话要点**：提出结合事件日志与静态属性的框架，以提升造船业采购提前期预测准确性

**关键词**：采购提前期预测, 事件日志, 深度序列神经网络, 造船业, 过程感知

## 3 点简述
- 核心问题：传统方法忽略采购过程的动态性和多利益相关者事件，导致预测不准确
- 方法要点：提取事件日志的时间属性，使用深度序列神经网络整合静态与动态特征
- 实验或效果：在真实数据上，预测性能比现有最佳方法提升22.6%至50.4%

## 摘要（原文）

> Accurately predicting procurement lead time (PLT) remains a challenge in engineered-to-order industries such as shipbuilding and plant construction, where delays in a single key component can disrupt project timelines. In shipyards, pipe spools are critical components; installed deep within hull blocks soon after steel erection, any delay in their procurement can halt all downstream tasks. Recognizing their importance, existing studies predict PLT using the static physical attributes of pipe spools. However, procurement is inherently a dynamic, multi-stakeholder business process involving a continuous sequence of internal and external events at the shipyard, factors often overlooked in traditional approaches. To address this issue, this paper proposes a novel framework that combines event logs, dataset records of the procurement events, with static attributes to predict PLT. The temporal attributes of each event are extracted to reflect the continuity and temporal context of the process. Subsequently, a deep sequential neural network combined with a multi-layered perceptron is employed to integrate these static and dynamic features, enabling the model to capture both structural and contextual information in procurement. Comparative experiments are conducted using real-world pipe spool procurement data from a globally renowned South Korean shipbuilding corporation. Three tasks are evaluated, which are production, post-processing, and procurement lead time prediction. The results show a 22.6% to 50.4% improvement in prediction performance in terms of mean absolute error over the best-performing existing approaches across the three tasks. These findings indicate the value of considering procurement process information for more accurate PLT prediction.

