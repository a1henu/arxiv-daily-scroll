---
layout: default
title: Vision-Language Models on the Edge for Real-Time Robotic Perception
---

# Vision-Language Models on the Edge for Real-Time Robotic Perception
**arXiv**：[2601.14921v1](https://arxiv.org/abs/2601.14921) · [PDF](https://arxiv.org/pdf/2601.14921.pdf)  
**作者**：Sarat Ahmad, Maryam Hafeez, Syed Ali Raza Zaidi  

**一句话要点**：在6G边缘部署视觉语言模型以提升机器人实时感知性能

**关键词**：视觉语言模型, 边缘计算, 机器人感知, 实时系统, 6G网络, 延迟优化

## 3 点简述
- 核心问题：视觉语言模型在机器人部署中面临延迟、资源限制和云卸载隐私风险。
- 方法要点：基于ORAN/MEC基础设施和WebRTC管道，在边缘节点部署VLMs进行实时处理。
- 实验或效果：边缘部署保持近云精度，降低端到端延迟5%；紧凑模型实现亚秒响应，但精度下降。

## 摘要（原文）

> Vision-Language Models (VLMs) enable multimodal reasoning for robotic perception and interaction, but their deployment in real-world systems remains constrained by latency, limited onboard resources, and privacy risks of cloud offloading. Edge intelligence within 6G, particularly Open RAN and Multi-access Edge Computing (MEC), offers a pathway to address these challenges by bringing computation closer to the data source. This work investigates the deployment of VLMs on ORAN/MEC infrastructure using the Unitree G1 humanoid robot as an embodied testbed. We design a WebRTC-based pipeline that streams multimodal data to an edge node and evaluate LLaMA-3.2-11B-Vision-Instruct deployed at the edge versus in the cloud under real-time conditions. Our results show that edge deployment preserves near-cloud accuracy while reducing end-to-end latency by 5\%. We further evaluate Qwen2-VL-2B-Instruct, a compact model optimized for resource-constrained environments, which achieves sub-second responsiveness, cutting latency by more than half but at the cost of accuracy.

