---
layout: default
title: Diverging Flows: Detecting Extrapolations in Conditional Generation
---

# Diverging Flows: Detecting Extrapolations in Conditional Generation
**arXiv**：[2602.13061v1](https://arxiv.org/abs/2602.13061) · [PDF](https://arxiv.org/pdf/2602.13061.pdf)  
**作者**：Constantinos Tsakonas, Serena Ivaldi, Jean-Baptiste Mouret  

**一句话要点**：提出Diverging Flows方法，通过结构设计实现条件生成与离群检测，以解决流匹配模型在安全关键场景中的外推风险。

**关键词**：流匹配, 条件生成, 外推检测, 安全关键系统, 离群输入, 高效传输

## 3 点简述
- 核心问题：流匹配模型因平滑性偏差，对离群条件产生看似合理但错误的输出，导致安全关键部署中的静默失败。
- 方法要点：通过强制离群输入的低效传输，使单个模型同时执行条件生成和原生外推检测，无需额外模块。
- 实验或效果：在合成流形、跨域风格迁移和天气温度预测上验证，有效检测外推，不损害预测精度或推理延迟。

## 摘要（原文）

> The ability of Flow Matching (FM) to model complex conditional distributions has established it as the state-of-the-art for prediction tasks (e.g., robotics, weather forecasting). However, deployment in safety-critical settings is hindered by a critical extrapolation hazard: driven by smoothness biases, flow models yield plausible outputs even for off-manifold conditions, resulting in silent failures indistinguishable from valid predictions. In this work, we introduce Diverging Flows, a novel approach that enables a single model to simultaneously perform conditional generation and native extrapolation detection by structurally enforcing inefficient transport for off-manifold inputs. We evaluate our method on synthetic manifolds, cross-domain style transfer, and weather temperature forecasting, demonstrating that it achieves effective detection of extrapolations without compromising predictive fidelity or inference latency. These results establish Diverging Flows as a robust solution for trustworthy flow models, paving the way for reliable deployment in domains such as medicine, robotics, and climate science.

