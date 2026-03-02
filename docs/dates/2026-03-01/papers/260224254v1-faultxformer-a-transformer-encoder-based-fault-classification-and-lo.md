---
layout: default
title: FaultXformer: A Transformer-Encoder Based Fault Classification and Location Identification model in PMU-Integrated Active Electrical Distribution System
---

# FaultXformer: A Transformer-Encoder Based Fault Classification and Location Identification model in PMU-Integrated Active Electrical Distribution System
**arXiv**：[2602.24254v1](https://arxiv.org/abs/2602.24254) · [PDF](https://arxiv.org/pdf/2602.24254.pdf)  
**作者**：Kriti Thakur, Alivelu Manga Parimi, Mayukha Pal  

**一句话要点**：提出FaultXformer，基于Transformer编码器，用于PMU集成的主动配电系统中故障分类与定位。

**关键词**：故障分类, 故障定位, Transformer编码器, 相量测量单元, 配电系统, 分布式能源

## 3 点简述
- 核心问题：分布式能源集成增加电网复杂性，需准确故障检测与定位。
- 方法要点：采用双阶段Transformer编码器，从PMU电流数据提取时序特征进行分类与定位。
- 实验或效果：在IEEE 13节点测试馈线数据集上验证，故障分类和定位平均准确率分别达98.76%和98.92%。

## 摘要（原文）

> Accurate fault detection and localization in electrical distribution systems is crucial, especially with the increasing integration of distributed energy resources (DERs), which inject greater variability and complexity into grid operations. In this study, FaultXformer is proposed, a Transformer encoder-based architecture developed for automatic fault analysis using real-time current data obtained from phasor measurement unit (PMU). The approach utilizes time-series current data to initially extract rich temporal information in stage 1, which is crucial for identifying the fault type and precisely determining its location across multiple nodes. In Stage 2, these extracted features are processed to differentiate among distinct fault types and identify the respective fault location within the distribution system. Thus, this dual-stage transformer encoder pipeline enables high-fidelity representation learning, considerably boosting the performance of the work. The model was validated on a dataset generated from the IEEE 13-node test feeder, simulated with 20 separate fault locations and several DER integration scenarios, utilizing current measurements from four strategically located PMUs. To demonstrate robust performance evaluation, stratified 10-fold cross-validation is performed. FaultXformer achieved average accuracies of 98.76% in fault type classification and 98.92% in fault location identification across cross-validation, consistently surpassing conventional deep learning baselines convolutional neural network (CNN), recurrent neural network (RNN). long short-term memory (LSTM) by 1.70%, 34.95%, and 2.04% in classification accuracy and by 10.82%, 40.89%, and 6.27% in location accuracy, respectively. These results demonstrate the efficacy of the proposed model with significant DER penetration.

