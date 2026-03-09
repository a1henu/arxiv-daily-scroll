---
layout: default
title: Fly360: Omnidirectional Obstacle Avoidance within Drone View
---

# Fly360: Omnidirectional Obstacle Avoidance within Drone View
**arXiv**：[2603.06573v1](https://arxiv.org/abs/2603.06573) · [PDF](https://arxiv.org/pdf/2603.06573.pdf)  
**作者**：Xiangkai Zhang, Dizhe Zhang, WenZhuo Cao, Zhaoliang Wan, Yingjie Niu, Lu Qi, Xu Yang, Zhiyong Liu  

**一句话要点**：提出Fly360以解决全景无人机全向避障问题

**关键词**：无人机避障, 全景感知, 深度图表示, 轻量策略网络, 全向运动规划

## 3 点简述
- 研究无人机在任意方向障碍物环境中的全向避障问题，构建包含三个飞行任务的基准
- 采用两阶段感知-决策流程，包括全景RGB转深度图表示和轻量策略网络输出速度命令
- 通过仿真和真实实验验证Fly360在全向避障任务中优于前向视角基线方法

## 摘要（原文）

> Obstacle avoidance in unmanned aerial vehicles (UAVs), as a fundamental capability, has gained increasing attention with the growing focus on spatial intelligence. However, current obstacle-avoidance methods mainly depend on limited field-of-view sensors and are ill-suited for UAV scenarios which require full-spatial awareness when the movement direction differs from the UAV's heading. This limitation motivates us to explore omnidirectional obstacle avoidance for panoramic drones with full-view perception. We first study an under explored problem setting in which a UAV must generate collision-free motion in environments with obstacles from arbitrary directions, and then construct a benchmark that consists of three representative flight tasks. Based on such settings, we propose Fly360, a two-stage perception-decision pipeline with a fixed random-yaw training strategy. At the perception stage, panoramic RGB observations are input and converted into depth maps as a robust intermediate representation. For the policy network, it is lightweight and used to output body-frame velocity commands from depth inputs. Extensive simulation and real-world experiments demonstrate that Fly360 achieves stable omnidirectional obstacle avoidance and outperforms forward-view baselines across all tasks. Our model is available at https://zxkai.github.io/fly360/

