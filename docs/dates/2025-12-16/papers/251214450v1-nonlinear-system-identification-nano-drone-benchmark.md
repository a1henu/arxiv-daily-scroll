---
layout: default
title: Nonlinear System Identification Nano-drone Benchmark
---

# Nonlinear System Identification Nano-drone Benchmark
**arXiv**：[2512.14450v1](https://arxiv.org/abs/2512.14450) · [PDF](https://arxiv.org/pdf/2512.14450.pdf)  
**作者**：Riccardo Busetto, Elia Cereda, Marco Forgione, Gabriele Maroni, Dario Piga, Daniele Palossi  

**一句话要点**：提出基于Crazyflie 2.1纳米四旋翼的真实世界系统辨识基准，以评估非线性动态下的预测方法。

**关键词**：系统辨识, 纳米无人机, 非线性动态, 多步预测, 开源基准, 机器人研究

## 3 点简述
- 核心问题：纳米无人机在敏捷机动下的多输入多输出、开环不稳定和非线性动态辨识挑战。
- 方法要点：提供包含7.5万样本的数据集，含同步电机输入和输出测量，支持多步预测误差评估。
- 实验或效果：开源数据与脚本，提供基线模型，促进算法透明比较和微型空中机器人研究。

## 摘要（原文）

> We introduce a benchmark for system identification based on 75k real-world samples from the Crazyflie 2.1 Brushless nano-quadrotor, a sub-50g aerial vehicle widely adopted in robotics research. The platform presents a challenging testbed due to its multi-input, multi-output nature, open-loop instability, and nonlinear dynamics under agile maneuvers. The dataset comprises four aggressive trajectories with synchronized 4-dimensional motor inputs and 13-dimensional output measurements. To enable fair comparison of identification methods, the benchmark includes a suite of multi-horizon prediction metrics for evaluating both one-step and multi-step error propagation. In addition to the data, we provide a detailed description of the platform and experimental setup, as well as baseline models highlighting the challenge of accurate prediction under real-world noise and actuation nonlinearities. All data, scripts, and reference implementations are released as open-source at https://github.com/idsia-robotics/nanodrone-sysid-benchmark to facilitate transparent comparison of algorithms and support research on agile, miniaturized aerial robotics.

