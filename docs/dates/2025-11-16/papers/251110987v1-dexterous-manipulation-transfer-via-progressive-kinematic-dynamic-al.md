---
layout: default
title: Dexterous Manipulation Transfer via Progressive Kinematic-Dynamic Alignment
---

# Dexterous Manipulation Transfer via Progressive Kinematic-Dynamic Alignment
**arXiv**：[2511.10987v1](https://arxiv.org/abs/2511.10987) · [PDF](https://arxiv.org/pdf/2511.10987.pdf)  
**作者**：Wenbin Bai, Qiyu Chen, Xiangbo Lin, Jianwen Li, Quancheng Li, Hejiang Pan, Yi Sun  

**一句话要点**：提出手无关操作转移系统以解决灵巧操作数据稀缺问题

**关键词**：灵巧操作转移, 运动学动态对齐, 手无关系统, 渐进式框架, 数据稀缺解决

## 3 点简述
- 核心问题：多指机器人手数据稀缺阻碍数据驱动策略学习
- 方法要点：渐进式转移框架，结合运动学匹配与动态优化
- 实验或效果：平均转移成功率73%，生成流畅且语义正确的操作轨迹

## 摘要（原文）

> The inherent difficulty and limited scalability of collecting manipulation data using multi-fingered robot hand hardware platforms have resulted in severe data scarcity, impeding research on data-driven dexterous manipulation policy learning. To address this challenge, we present a hand-agnostic manipulation transfer system. It efficiently converts human hand manipulation sequences from demonstration videos into high-quality dexterous manipulation trajectories without requirements of massive training data. To tackle the multi-dimensional disparities between human hands and dexterous hands, as well as the challenges posed by high-degree-of-freedom coordinated control of dexterous hands, we design a progressive transfer framework: first, we establish primary control signals for dexterous hands based on kinematic matching; subsequently, we train residual policies with action space rescaling and thumb-guided initialization to dynamically optimize contact interactions under unified rewards; finally, we compute wrist control trajectories with the objective of preserving operational semantics. Using only human hand manipulation videos, our system automatically configures system parameters for different tasks, balancing kinematic matching and dynamic optimization across dexterous hands, object categories, and tasks. Extensive experimental results demonstrate that our framework can automatically generate smooth and semantically correct dexterous hand manipulation that faithfully reproduces human intentions, achieving high efficiency and strong generalizability with an average transfer success rate of 73%, providing an easily implementable and scalable method for collecting robot dexterous manipulation data.

