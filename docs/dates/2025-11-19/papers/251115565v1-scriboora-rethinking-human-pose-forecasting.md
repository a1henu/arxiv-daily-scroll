---
layout: default
title: Scriboora: Rethinking Human Pose Forecasting
---

# Scriboora: Rethinking Human Pose Forecasting
**arXiv**：[2511.15565v1](https://arxiv.org/abs/2511.15565) · [PDF](https://arxiv.org/pdf/2511.15565.pdf)  
**作者**：Daniel Bermuth, Alexander Poeppel, Wolfgang Reif  

**一句话要点**：提出统一训练评估流程并适配语音模型，提升人体姿态预测性能与鲁棒性

**关键词**：人体姿态预测, 语音模型适配, 统一评估流程, 噪声鲁棒性, 无监督微调

## 3 点简述
- 核心问题：人体姿态预测存在可复现性问题，且真实噪声导致性能下降
- 方法要点：借鉴语音理解，高效适配语音模型以改进姿态预测
- 实验或效果：引入新数据集变体，无监督微调可部分恢复噪声下的性能

## 摘要（原文）

> Human pose forecasting predicts future poses based on past observations, and has many significant applications in areas such as action recognition, autonomous driving or human-robot interaction. This paper evaluates a wide range of pose forecasting algorithms in the task of absolute pose forecasting, revealing many reproducibility issues, and provides a unified training and evaluation pipeline. After drawing a high-level analogy to the task of speech understanding, it is shown that recent speech models can be efficiently adapted to the task of pose forecasting, and improve current state-of-the-art performance. At last the robustness of the models is evaluated, using noisy joint coordinates obtained from a pose estimator model, to reflect a realistic type of noise, which is more close to real-world applications. For this a new dataset variation is introduced, and it is shown that estimated poses result in a substantial performance degradation, and how much of it can be recovered again by unsupervised finetuning.

