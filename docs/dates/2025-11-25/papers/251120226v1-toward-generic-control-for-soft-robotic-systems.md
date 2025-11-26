---
layout: default
title: Toward generic control for soft robotic systems
---

# Toward generic control for soft robotic systems
**arXiv**：[2511.20226v1](https://arxiv.org/abs/2511.20226) · [PDF](https://arxiv.org/pdf/2511.20226.pdf)  
**作者**：Yu Sun, Yaosheng Deng, Wenjie Mei, Xiaogang Xiong, Yang Bai, Masaki Ogura, Zeyu Zhou, Mir Feroskhan, Michael Yu Wang, Qiyang Zuo, Yao Li, Yunjiang Lou  

**一句话要点**：提出基于控制柔性的通用软体机器人控制框架，以解决任务特定控制器问题。

**关键词**：软体机器人, 通用控制框架, 控制柔性, 机器人运动控制, 跨平台可转移

## 3 点简述
- 核心问题：软体机器人控制方法碎片化，依赖精确模型和低层执行，缺乏通用性。
- 方法要点：借鉴人类运动控制，利用高层意图表达和局部自主机制，显式利用控制柔性。
- 实验或效果：在多种形态和驱动机制的机器人上验证，实现稳定、安全和跨平台可转移行为。

## 摘要（原文）

> Soft robotics has advanced rapidly, yet its control methods remain fragmented: different morphologies and actuation schemes still require task-specific controllers, hindering theoretical integration and large-scale deployment. A generic control framework is therefore essential, and a key obstacle lies in the persistent use of rigid-body control logic, which relies on precise models and strict low-level execution. Such a paradigm is effective for rigid robots but fails for soft robots, where the ability to tolerate and exploit approximate action representations, i.e., control compliance, is the basis of robustness and adaptability rather than a disturbance to be eliminated. Control should thus shift from suppressing compliance to explicitly exploiting it. Human motor control exemplifies this principle: instead of computing exact dynamics or issuing detailed muscle-level commands, it expresses intention through high-level movement tendencies, while reflexes and biomechanical mechanisms autonomously resolve local details. This architecture enables robustness, flexibility, and cross-task generalization. Motivated by this insight, we propose a generic soft-robot control framework grounded in control compliance and validate it across robots with diverse morphologies and actuation mechanisms. The results demonstrate stable, safe, and cross-platform transferable behavior, indicating that embracing control compliance, rather than resisting it, may provide a widely applicable foundation for unified soft-robot control.

