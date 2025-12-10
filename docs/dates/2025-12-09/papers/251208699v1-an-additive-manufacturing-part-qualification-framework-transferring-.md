---
layout: default
title: An Additive Manufacturing Part Qualification Framework: Transferring Knowledge of Stress-strain Behaviors from Additively Manufactured Polymers to Metals
---

# An Additive Manufacturing Part Qualification Framework: Transferring Knowledge of Stress-strain Behaviors from Additively Manufactured Polymers to Metals
**arXiv**：[2512.08699v1](https://arxiv.org/abs/2512.08699) · [PDF](https://arxiv.org/pdf/2512.08699.pdf)  
**作者**：Chenglong Duan, Dazhong Wu  

**一句话要点**：提出动态时间规整-迁移学习框架，通过聚合物知识迁移实现增材制造金属部件应力应变行为预测

**关键词**：增材制造, 迁移学习, 动态时间规整, 长短期记忆网络, 应力应变预测, 部件认证

## 3 点简述
- 核心问题：增材制造部件认证需准确预测复杂应力应变行为，但金属数据稀缺。
- 方法要点：使用DTW选择最相关聚合物源域，结合LSTM模型进行知识迁移。
- 实验效果：在三种金属上，DTW-TL模型误差最低12.41%，决定系数最高0.96，优于基准模型。

## 摘要（原文）

> Part qualification is crucial in additive manufacturing (AM) because it ensures that additively manufactured parts can be consistently produced and reliably used in critical applications. Part qualification aims at verifying that an additively manufactured part meets performance requirements; therefore, predicting the complex stress-strain behaviors of additively manufactured parts is critical. We develop a dynamic time warping (DTW)-transfer learning (TL) framework for additive manufacturing part qualification by transferring knowledge of the stress-strain behaviors of additively manufactured low-cost polymers to metals. Specifically, the framework employs DTW to select a polymer dataset as the source domain that is the most relevant to the target metal dataset. Using a long short-term memory (LSTM) model, four source polymers (i.e., Nylon, PLA, CF-ABS, and Resin) and three target metals (i.e., AlSi10Mg, Ti6Al4V, and carbon steel) that are fabricated by different AM techniques are utilized to demonstrate the effectiveness of the DTW-TL framework. Experimental results show that the DTW-TL framework identifies the closest match between polymers and metals to select one single polymer dataset as the source domain. The DTW-TL model achieves the lowest mean absolute percentage error of 12.41% and highest coefficient of determination of 0.96 when three metals are used as the target domain, respectively, outperforming the vanilla LSTM model without TL as well as the TL model pre-trained on four polymer datasets as the source domain.

