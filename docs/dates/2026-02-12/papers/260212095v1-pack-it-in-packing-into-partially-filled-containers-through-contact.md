---
layout: default
title: Pack it in: Packing into Partially Filled Containers Through Contact
---

# Pack it in: Packing into Partially Filled Containers Through Contact
**arXiv**：[2602.12095v1](https://arxiv.org/abs/2602.12095) · [PDF](https://arxiv.org/pdf/2602.12095.pdf)  
**作者**：David Russell, Zisong Xu, Maximo A. Roa, Mehmet Dogar  

**一句话要点**：提出接触感知装箱方法，利用与已有物品的交互在部分填充容器中创造空间以实现新物品放置。

**关键词**：接触感知装箱, 多物体轨迹优化, 模型预测控制, 物理感知感知, 部分填充容器, 仓库自动化

## 3 点简述
- 核心问题：现有装箱研究多针对空容器且采用无碰撞策略，但实际仓库中容器常部分填充且物品排列不佳，导致新物品难以放置。
- 方法要点：采用基于接触的多物体轨迹优化器，结合模型预测控制器、物理感知感知系统及物理可行位置建议方法，实现接触感知装箱。
- 实验或效果：未知，但方法旨在通过接触交互创造自由空间，提升装箱成功率。

## 摘要（原文）

> The automation of warehouse operations is crucial for improving productivity and reducing human exposure to hazardous environments. One operation frequently performed in warehouses is bin-packing where items need to be placed into containers, either for delivery to a customer, or for temporary storage in the warehouse. Whilst prior bin-packing works have largely been focused on packing items into empty containers and have adopted collision-free strategies, it is often the case that containers will already be partially filled with items, often in suboptimal arrangements due to transportation about a warehouse. This paper presents a contact-aware packing approach that exploits purposeful interactions with previously placed objects to create free space and enable successful placement of new items. This is achieved by using a contact-based multi-object trajectory optimizer within a model predictive controller, integrated with a physics-aware perception system that estimates object poses even during inevitable occlusions, and a method that suggests physically-feasible locations to place the object inside the container.

