---
layout: default
title: SynthCharge: An Electric Vehicle Routing Instance Generator with Feasibility Screening to Enable Learning-Based Optimization and Benchmarking
---

# SynthCharge: An Electric Vehicle Routing Instance Generator with Feasibility Screening to Enable Learning-Based Optimization and Benchmarking
**arXiv**：[2603.03230v1](https://arxiv.org/abs/2603.03230) · [PDF](https://arxiv.org/pdf/2603.03230.pdf)  
**作者**：Mertcan Daysalilar, Fuat Uyguroglu, Gabriel Nicolosi, Adam Meyers  

**一句话要点**：提出SynthCharge生成器以解决电动汽车路径问题中基准数据集静态且缺乏可验证可行性的问题。

**关键词**：电动汽车路径问题, 基准生成器, 可行性筛选, 学习型优化, 动态基准, 参数化实例

## 3 点简述
- 核心问题：现有电动汽车路径问题基准数据集静态且缺乏可验证可行性，限制学习型模型的评估。
- 方法要点：SynthCharge通过参数化生成器产生多样、可行性筛选的实例，集成几何、能量缩放和充电站布局。
- 实验或效果：实验聚焦5至100客户规模，提供动态基准设施以系统评估神经路由和数据驱动方法的鲁棒性。

## 摘要（原文）

> The electric vehicle routing problem with time windows (EVRPTW) extends the classical VRPTW by introducing battery capacity constraints and charging station decisions. Existing benchmark datasets are often static and lack verifiable feasibility, which restricts reproducible evaluation of learning-based routing models. We introduce SynthCharge, a parametric generator that produces diverse, feasibility-screened EVRPTW instances across varying spatiotemporal configurations and scalable customer counts. While SynthCharge can currently generate large-scale instances of up to 500 customers, we focus our experiments on sizes ranging from 5 to 100 customers. Unlike static benchmark suites, SynthCharge integrates instance geometry with adaptive energy capacity scaling and range-aware charging station placement. To guarantee structural validity, the generator systematically filters out unsolvable instances through a fast feasibility screening process. Ultimately, SynthCharge provides the dynamic benchmarking infrastructure needed to systematically evaluate the robustness of emerging neural routing and data-driven approaches.

