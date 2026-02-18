---
layout: default
title: Benchmarking IoT Time-Series AD with Event-Level Augmentations
---

# Benchmarking IoT Time-Series AD with Event-Level Augmentations
**arXiv**：[2602.15457v1](https://arxiv.org/abs/2602.15457) · [PDF](https://arxiv.org/pdf/2602.15457.pdf)  
**作者**：Dmitry Zhevnenko, Ilya Makarov, Aleksandr Kovalenko, Fedor Meshchaninov, Anton Kozhukhov, Vladislav Travnikov, Makar Ippolitov, Kirill Yashunin, Iurii Katser  

**一句话要点**：提出事件级增强的评估协议，以提升物联网时序异常检测在现实扰动下的可靠性评估。

**关键词**：物联网时序异常检测, 事件级评估, 数据增强, 传感器级分析, 模型比较, 现实扰动模拟

## 3 点简述
- 核心问题：现有研究多关注点级结果，缺乏对安全关键物联网时序异常检测事件级可靠性和早期性的评估。
- 方法要点：引入统一事件级增强，模拟传感器丢失、漂移、噪声和窗口偏移等现实问题，并支持传感器级根因分析。
- 实验或效果：评估14个模型在多个数据集上，发现无通用最优模型，不同模型在不同扰动下表现各异，协议可指导设计选择。

## 摘要（原文）

> Anomaly detection (AD) for safety-critical IoT time series should be judged at the event level: reliability and earliness under realistic perturbations. Yet many studies still emphasize point-level results on curated base datasets, limiting value for model selection in practice. We introduce an evaluation protocol with unified event-level augmentations that simulate real-world issues: calibrated sensor dropout, linear and log drift, additive noise, and window shifts. We also perform sensor-level probing via mask-as-missing zeroing with per-channel influence estimation to support root-cause analysis. We evaluate 14 representative models on five public anomaly datasets (SWaT, WADI, SMD, SKAB, TEP) and two industrial datasets (steam turbine, nuclear turbogenerator) using unified splits and event aggregation. There is no universal winner: graph-structured models transfer best under dropout and long events (e.g., on SWaT under additive noise F1 drops 0.804->0.677 for a graph autoencoder, 0.759->0.680 for a graph-attention variant, and 0.762->0.756 for a hybrid graph attention model); density/flow models work well on clean stationary plants but can be fragile to monotone drift; spectral CNNs lead when periodicity is strong; reconstruction autoencoders become competitive after basic sensor vetting; predictive/hybrid dynamics help when faults break temporal dependencies but remain window-sensitive. The protocol also informs design choices: on SWaT under log drift, replacing normalizing flows with Gaussian density reduces high-stress F1 from ~0.75 to ~0.57, and fixing a learned DAG gives a small clean-set gain (~0.5-1.0 points) but increases drift sensitivity by ~8x.

