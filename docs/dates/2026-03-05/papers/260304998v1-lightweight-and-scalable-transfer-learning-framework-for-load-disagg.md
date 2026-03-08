---
layout: default
title: Lightweight and Scalable Transfer Learning Framework for Load Disaggregation
---

# Lightweight and Scalable Transfer Learning Framework for Load Disaggregation
**arXiv**：[2603.04998v1](https://arxiv.org/abs/2603.04998) · [PDF](https://arxiv.org/pdf/2603.04998.pdf)  
**作者**：L. E. Garcia-Marrero, G. Petrone, E. Monmasson  

**一句话要点**：提出RefQuery框架以解决非侵入式负载监测中跨域泛化与实时部署的挑战

**关键词**：非侵入式负载监测, 迁移学习, 边缘计算, 多任务学习, 设备指纹, 实时系统

## 3 点简述
- 核心问题：非侵入式负载监测面临跨家庭设备特性、使用模式和背景负载差异导致的泛化难题
- 方法要点：基于紧凑设备指纹的多设备多任务框架，冻结预训练网络，仅学习设备嵌入实现轻量适应
- 实验或效果：在三个公开数据集上验证，相比基线方法在精度与效率间取得良好平衡，支持资源受限边缘设备实时操作

## 摘要（原文）

> Non-Intrusive Load Monitoring (NILM) aims to estimate appliance-level consumption from aggregate electrical signals recorded at a single measurement point. In recent years, the field has increasingly adopted deep learning approaches; however, cross-domain generalization remains a persistent challenge due to variations in appliance characteristics, usage patterns, and background loads across homes. Transfer learning provides a practical paradigm to adapt models with limited target data. However, existing methods often assume a fixed appliance set, lack flexibility for evolving real-world deployments, remain unsuitable for edge devices, or scale poorly for real-time operation. This paper proposes RefQuery, a scalable multi-appliance, multi-task NILM framework that conditions disaggregation on compact appliance fingerprints, allowing one shared model to serve many appliances without a fixed output set. RefQuery keeps a pretrained disaggregation network fully frozen and adapts to a target home by learning only a per-appliance embedding during a lightweight backpropagation stage. Experiments on three public datasets demonstrate that RefQuery delivers a strong accuracy-efficiency trade-off against single-appliance and multi-appliance baselines, including modern Transformer-based methods. These results support RefQuery as a practical path toward scalable, real-time NILM on resource-constrained edge devices.

