---
layout: default
title: InstMeter: An Instruction-Level Method to Predict Energy and Latency of DL Model Inference on MCUs
---

# InstMeter: An Instruction-Level Method to Predict Energy and Latency of DL Model Inference on MCUs
**arXiv**：[2603.04134v1](https://arxiv.org/abs/2603.04134) · [PDF](https://arxiv.org/pdf/2603.04134.pdf)  
**作者**：Hao Liu, Qing Wang, Marco Zuniga  

**一句话要点**：提出InstMeter方法，基于时钟周期预测MCU上深度学习模型推理的能耗与延迟。

**关键词**：微控制器推理, 能耗预测, 延迟预测, 时钟周期分析, 神经网络架构搜索, 线性预测器

## 3 点简述
- 核心问题：现有方法依赖MACs等粗粒度代理，预测能耗和延迟不准确或需大量数据。
- 方法要点：利用MCU时钟周期作为基础指标，构建线性预测器，简单且准确。
- 实验或效果：在多种MCU和设置下评估，预测误差显著降低，训练数据需求减少，提升NAS效率。

## 摘要（原文）

> Deep learning (DL) models can now run on microcontrollers (MCUs). Through neural architecture search (NAS), we can search DL models that meet the constraints of MCUs. Among various constraints, energy and latency costs of the model inference are critical metrics. To predict them, existing research relies on coarse proxies such as multiply-accumulations (MACs) and model's input parameters, often resulting in inaccurate predictions or requiring extensive data collection. In this paper, we propose InstMeter, a predictor leveraging MCUs' clock cycles to accurately estimate the energy and latency of DL models. Clock cycles are fundamental metrics reflecting MCU operations, directly determining energy and latency costs. Furthermore, a unique property of our predictor is its strong linearity, allowing it to be simple and accurate. We thoroughly evaluate InstMeter under different scenarios, MCUs, and software settings. Compared with state-of-the-art studies, InstMeter can reduce the energy and latency prediction errors by $3\times$ and $6.5\times$, respectively, while requiring $100\times$ and $10\times$ less training data. In the NAS scenario, InstMeter can fully exploit the energy budget, identifying optimal DL models with higher inference accuracy. We also evaluate InstMeter's generalization performance through various experiments on three ARM MCUs (Cortex-M4, M7, M33) and one RISC-V-based MCU (ESP32-C3), different compilation options (-Os, -O2), GCC versions (v7.3, v10.3), application scenarios (keyword spotting, image recognition), dynamic voltage and frequency scaling, temperatures (21°C, 43°C), and software settings (TFLMv2.4, TFLMvCI). We will open our source codes and the MCU-specific benchmark datasets.

