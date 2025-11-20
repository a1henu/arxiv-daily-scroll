---
layout: default
title: PCARNN-DCBF: Minimal-Intervention Geofence Enforcement for Ground Vehicles
---

# PCARNN-DCBF: Minimal-Intervention Geofence Enforcement for Ground Vehicles
**arXiv**：[2511.15522v1](https://arxiv.org/abs/2511.15522) · [PDF](https://arxiv.org/pdf/2511.15522.pdf)  
**作者**：Yinan Yu, Samuel Scheidegger  

**一句话要点**：提出PCARNN-DCBF以最小干预方式强制执行地面车辆地理围栏

**关键词**：地理围栏强制执行, 控制仿射神经网络, 离散控制屏障函数, 实时二次规划, 车辆动力学, 最小干预控制

## 3 点简述
- 现有地理围栏方案难以平衡高保真学习与可验证控制的结构要求
- 集成物理编码控制仿射残差神经网络与预览离散控制屏障函数
- 在CARLA实验中显著优于分析和非结构化神经网络基线

## 摘要（原文）

> Runtime geofencing for ground vehicles is rapidly emerging as a critical technology for enforcing Operational Design Domains (ODDs). However, existing solutions struggle to reconcile high-fidelity learning with the structural requirements of verifiable control. We address this by introducing PCARNN-DCBF, a novel pipeline integrating a Physics-encoded Control-Affine Residual Neural Network with a preview-based Discrete Control Barrier Function. Unlike generic learned models, PCARNN explicitly preserves the control-affine structure of vehicle dynamics, ensuring the linearity required for reliable optimization. This enables the DCBF to enforce polygonal keep-in constraints via a real-time Quadratic Program (QP) that handles high relative degree and mitigates actuator saturation. Experiments in CARLA across electric and combustion platforms demonstrate that this structure-preserving approach significantly outperforms analytical and unstructured neural baselines.

