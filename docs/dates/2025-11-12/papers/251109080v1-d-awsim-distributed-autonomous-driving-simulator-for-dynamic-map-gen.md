---
layout: default
title: D-AWSIM: Distributed Autonomous Driving Simulator for Dynamic Map Generation Framework
---

# D-AWSIM: Distributed Autonomous Driving Simulator for Dynamic Map Generation Framework
**arXiv**：[2511.09080v1](https://arxiv.org/abs/2511.09080) · [PDF](https://arxiv.org/pdf/2511.09080.pdf)  
**作者**：Shunsuke Ito, Chaoran Zhao, Ryo Okamura, Takuya Azumi  

**一句话要点**：提出分布式模拟器D-AWSIM以支持大规模自动驾驶动态地图生成

**关键词**：自动驾驶模拟, 分布式系统, 动态地图生成, 传感器数据处理, 大规模交通仿真

## 3 点简述
- 核心问题：单机模拟器无法处理大规模城市交通和传感器部署，真实实验成本高。
- 方法要点：采用分布式架构，在多台机器上分配工作负载，支持动态地图生成框架。
- 实验或效果：相比单机设置，显著提升车辆数量和LiDAR传感器处理的吞吐量。

## 摘要（原文）

> Autonomous driving systems have achieved significant advances, and full autonomy within defined operational design domains near practical deployment. Expanding these domains requires addressing safety assurance under diverse conditions. Information sharing through vehicle-to-vehicle and vehicle-to-infrastructure communication, enabled by a Dynamic Map platform built from vehicle and roadside sensor data, offers a promising solution. Real-world experiments with numerous infrastructure sensors incur high costs and regulatory challenges. Conventional single-host simulators lack the capacity for large-scale urban traffic scenarios. This paper proposes D-AWSIM, a distributed simulator that partitions its workload across multiple machines to support the simulation of extensive sensor deployment and dense traffic environments. A Dynamic Map generation framework on D-AWSIM enables researchers to explore information-sharing strategies without relying on physical testbeds. The evaluation shows that D-AWSIM increases throughput for vehicle count and LiDAR sensor processing substantially compared to a single-machine setup. Integration with Autoware demonstrates applicability for autonomous driving research.

