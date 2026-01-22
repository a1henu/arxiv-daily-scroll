---
layout: default
title: UniCon: A Unified System for Efficient Robot Learning Transfers
---

# UniCon: A Unified System for Efficient Robot Learning Transfers
**arXiv**：[2601.14617v1](https://arxiv.org/abs/2601.14617) · [PDF](https://arxiv.org/pdf/2601.14617.pdf)  
**作者**：Yunfeng Lin, Li Xu, Yong Yu, Jiangmiao Pang, Weinan Zhang  

**一句话要点**：提出UniCon框架以解决异构机器人间学习控制器部署的挑战

**关键词**：机器人学习, 异构系统, 中间件优化, 即插即用部署, 推理效率

## 3 点简述
- 核心问题：异构机器人平台差异、接口不一致和中间件低效阻碍学习控制器部署
- 方法要点：通过标准化状态和控制流，分解工作流为可重用组件，实现即插即用部署
- 实验或效果：在12个机器人模型上验证，减少代码冗余，提升推理效率优于ROS系统

## 摘要（原文）

> Deploying learning-based controllers across heterogeneous robots is challenging due to platform differences, inconsistent interfaces, and inefficient middleware. To address these issues, we present UniCon, a lightweight framework that standardizes states, control flow, and instrumentation across platforms. It decomposes workflows into execution graphs with reusable components, separating system states from control logic to enable plug-and-play deployment across various robot morphologies. Unlike traditional middleware, it prioritizes efficiency through batched, vectorized data flow, minimizing communication overhead and improving inference latency. This modular, data-oriented approach enables seamless sim-to-real transfer with minimal re-engineering. We demonstrate that UniCon reduces code redundancy when transferring workflows and achieves higher inference efficiency compared to ROS-based systems. Deployed on over 12 robot models from 7 manufacturers, it has been successfully integrated into ongoing research projects, proving its effectiveness in real-world scenarios.

