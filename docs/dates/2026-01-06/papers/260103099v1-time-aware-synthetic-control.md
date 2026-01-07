---
layout: default
title: Time-Aware Synthetic Control
---

# Time-Aware Synthetic Control
**arXiv**：[2601.03099v1](https://arxiv.org/abs/2601.03099) · [PDF](https://arxiv.org/pdf/2601.03099.pdf)  
**作者**：Saeyoung Rho, Cyrus Illick, Samhitha Narasipura, Alberto Abadie, Daniel Hsu, Vishal Misra  

**一句话要点**：提出时间感知合成控制方法，以处理时间序列面板数据中的强趋势和噪声问题。

**关键词**：合成控制, 时间序列分析, 因果推断, 状态空间模型, 卡尔曼滤波

## 3 点简述
- 核心问题：现有合成控制方法忽略时间顺序，无法充分利用时间结构处理强趋势。
- 方法要点：采用状态空间模型结合卡尔曼滤波和平滑器，保持低秩信号结构并拟合生成模型。
- 实验或效果：在模拟和真实数据集上验证，在强趋势和高噪声场景中表现更优。

## 摘要（原文）

> The synthetic control (SC) framework is widely used for observational causal inference with time-series panel data. SC has been successful in diverse applications, but existing methods typically treat the ordering of pre-intervention time indices interchangeable. This invariance means they may not fully take advantage of temporal structure when strong trends are present. We propose Time-Aware Synthetic Control (TASC), which employs a state-space model with a constant trend while preserving a low-rank structure of the signal. TASC uses the Kalman filter and Rauch-Tung-Striebel smoother: it first fits a generative time-series model with expectation-maximization and then performs counterfactual inference. We evaluate TASC on both simulated and real-world datasets, including policy evaluation and sports prediction. Our results suggest that TASC offers advantages in settings with strong temporal trends and high levels of observation noise.

