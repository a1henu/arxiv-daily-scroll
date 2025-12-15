---
layout: default
title: Elevation Aware 2D/3D Co-simulation Framework for Large-scale Traffic Flow and High-fidelity Vehicle Dynamics
---

# Elevation Aware 2D/3D Co-simulation Framework for Large-scale Traffic Flow and High-fidelity Vehicle Dynamics
**arXiv**：[2512.11249v1](https://arxiv.org/abs/2512.11249) · [PDF](https://arxiv.org/pdf/2512.11249.pdf)  
**作者**：Chandra Raskoti, Weizi Li  

**一句话要点**：提出自动化高程感知协同仿真框架，以支持复杂地形下自动驾驶系统的高保真测试。

**关键词**：自动驾驶仿真, 高程感知, 协同仿真, SUMO-CARLA集成, 地形建模, 高保真测试

## 3 点简述
- 核心问题：现有仿真工具常忽略真实高程，限制在复杂地形城市中的自动驾驶测试可靠性。
- 方法要点：集成SUMO与CARLA，融合OpenStreetMap路网和USGS高程数据，生成物理一致的3D环境。
- 实验或效果：在旧金山多个区域演示，验证了框架的可扩展性和再现陡峭不规则地形的能力。

## 摘要（原文）

> Reliable testing of autonomous driving systems requires simulation environments that combine large-scale traffic modeling with realistic 3D perception and terrain. Existing tools rarely capture real-world elevation, limiting their usefulness in cities with complex topography. This paper presents an automated, elevation-aware co-simulation framework that integrates SUMO with CARLA using a pipeline that fuses OpenStreetMap road networks and USGS elevation data into physically consistent 3D environments. The system generates smooth elevation profiles, validates geometric accuracy, and enables synchronized 2D-3D simulation across platforms. Demonstrations on multiple regions of San Francisco show the framework's scalability and ability to reproduce steep and irregular terrain. The result is a practical foundation for high-fidelity autonomous vehicle testing in realistic, elevation-rich urban settings.

