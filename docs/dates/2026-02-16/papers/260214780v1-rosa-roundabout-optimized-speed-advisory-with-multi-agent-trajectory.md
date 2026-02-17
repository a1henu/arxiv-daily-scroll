---
layout: default
title: ROSA: Roundabout Optimized Speed Advisory with Multi-Agent Trajectory Prediction in Multimodal Traffic
---

# ROSA: Roundabout Optimized Speed Advisory with Multi-Agent Trajectory Prediction in Multimodal Traffic
**arXiv**：[2602.14780v1](https://arxiv.org/abs/2602.14780) · [PDF](https://arxiv.org/pdf/2602.14780.pdf)  
**作者**：Anna-Lena Schlamp, Jeremias Gerner, Klaus Bogenberger, Werner Huber, Stefanie Schmidtner  

**一句话要点**：提出ROSA系统，结合多智能体轨迹预测与协调速度引导，优化环形交叉口多模态交通效率与安全。

**关键词**：多智能体轨迹预测, 环形交叉口优化, Transformer模型, 速度引导系统, 多模态交通, 弱势道路用户安全

## 3 点简述
- 核心问题：环形交叉口多模态混合交通中，车辆与弱势道路用户（VRU）的轨迹冲突预测与协调速度引导。
- 方法要点：基于Transformer模型，联合预测车辆与VRU的未来轨迹，并部署自回归生成确定性输出，以提供实时速度建议。
- 实验或效果：模型在5秒预测范围内达到高精度（ADE: 1.29m, FDE: 2.99m），结合路线意图后性能提升（ADE: 1.10m, FDE: 2.36m），显著提高车辆效率和安全性。

## 摘要（原文）

> We present ROSA -- Roundabout Optimized Speed Advisory -- a system that combines multi-agent trajectory prediction with coordinated speed guidance for multimodal, mixed traffic at roundabouts. Using a Transformer-based model, ROSA jointly predicts the future trajectories of vehicles and Vulnerable Road Users (VRUs) at roundabouts. Trained for single-step prediction and deployed autoregressively, it generates deterministic outputs, enabling actionable speed advisories. Incorporating motion dynamics, the model achieves high accuracy (ADE: 1.29m, FDE: 2.99m at a five-second prediction horizon), surpassing prior work. Adding route intention further improves performance (ADE: 1.10m, FDE: 2.36m), demonstrating the value of connected vehicle data. Based on predicted conflicts with VRUs and circulating vehicles, ROSA provides real-time, proactive speed advisories for approaching and entering the roundabout. Despite prediction uncertainty, ROSA significantly improves vehicle efficiency and safety, with positive effects even on perceived safety from a VRU perspective. The source code of this work is available under: github.com/urbanAIthi/ROSA.

