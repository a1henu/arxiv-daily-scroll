---
layout: default
title: Spot-Wise Smart Parking: An Edge-Enabled Architecture with YOLOv11 and Digital Twin Integration
---

# Spot-Wise Smart Parking: An Edge-Enabled Architecture with YOLOv11 and Digital Twin Integration
**arXiv**：[2602.01754v1](https://arxiv.org/abs/2602.01754) · [PDF](https://arxiv.org/pdf/2602.01754.pdf)  
**作者**：Gustavo P. C. P. da Luz, Alvaro M. Aspilcueta Narvaez, Tiago Godoi Bannwart, Gabriel Massuyoshi Sato, Luis Fernando Gomez Gonzalez, Juliana Freitag Borin  

**一句话要点**：提出基于YOLOv11和数字孪生的边缘智能停车系统，实现车位级监控以提升城市交通效率。

**关键词**：智能停车系统, YOLOv11, 边缘计算, 数字孪生, 车位级监控, 自适应边界框分割

## 3 点简述
- 核心问题：现有停车系统仅能估计区域空闲车位数量，无法提供车位级洞察，限制了高级应用支持。
- 方法要点：采用距离感知匹配与空间容差策略，结合自适应边界框分割方法，增强车位识别准确性。
- 实验或效果：在资源受限边缘设备上实现98.80%的平衡准确率和8秒推理时间，并引入数字影子和应用服务器组件。

## 摘要（原文）

> Smart parking systems help reduce congestion and minimize users' search time, thereby contributing to smart city adoption and enhancing urban mobility. In previous works, we presented a system developed on a university campus to monitor parking availability by estimating the number of free spaces from vehicle counts within a region of interest. Although this approach achieved good accuracy, it restricted the system's ability to provide spot-level insights and support more advanced applications. To overcome this limitation, we extend the system with a spot-wise monitoring strategy based on a distance-aware matching method with spatial tolerance, enhanced through an Adaptive Bounding Box Partitioning method for challenging spaces. The proposed approach achieves a balanced accuracy of 98.80% while maintaining an inference time of 8 seconds on a resource-constrained edge device, enhancing the capabilities of YOLOv11m, a model that has a size of 40.5 MB. In addition, two new components were introduced: (i) a Digital Shadow that visually represents parking lot entities as a base to evolve to a full Digital Twin, and (ii) an application support server based on a repurposed TV box. The latter not only enables scalable communication among cloud services, the parking totem, and a bot that provides detailed spot occupancy statistics, but also promotes hardware reuse as a step towards greater sustainability.

