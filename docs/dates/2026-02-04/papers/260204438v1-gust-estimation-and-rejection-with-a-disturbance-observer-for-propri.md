---
layout: default
title: Gust Estimation and Rejection with a Disturbance Observer for Proprioceptive Underwater Soft Morphing Wings
---

# Gust Estimation and Rejection with a Disturbance Observer for Proprioceptive Underwater Soft Morphing Wings
**arXiv**：[2602.04438v1](https://arxiv.org/abs/2602.04438) · [PDF](https://arxiv.org/pdf/2602.04438.pdf)  
**作者**：Tobias Cook, Leo Micklem, Huazhi Dong, Yunjie Yang, Michael Mistry, Francesco Giorgio Serchi  

**一句话要点**：提出基于本体感知与扰动观测器的软变形翼，以提升水下无人载具在湍流环境中的稳定性。

**关键词**：水下无人载具, 软变形翼, 本体感知, 扰动观测器, 流体动力学, 稳定性控制

## 3 点简述
- 核心问题：浅水区湍流等扰动影响水下无人载具的稳定性和机动性。
- 方法要点：利用软变形翼的本体感知信号，通过扰动观测器实时估计流动参数。
- 实验或效果：实验验证了模型和控制器能准确估计攻角扰动并抑制升力响应中的干扰。

## 摘要（原文）

> Unmanned underwater vehicles are increasingly employed for maintenance and surveying tasks at sea, but their operation in shallow waters is often hindered by hydrodynamic disturbances such as waves, currents, and turbulence. These unsteady flows can induce rapid changes in direction and speed, compromising vehicle stability and manoeuvrability. Marine organisms contend with such conditions by combining proprioceptive feedback with flexible fins and tails to reject disturbances. Inspired by this strategy, we propose soft morphing wings endowed with proprioceptive sensing to mitigate environmental perturbations. The wing's continuous deformation provides a natural means to infer dynamic disturbances: sudden changes in camber directly reflect variations in the oncoming flow. By interpreting this proprioceptive signal, a disturbance observer can reconstruct flow parameters in real time. To enable this, we develop and experimentally validate a dynamic model of a hydraulically actuated soft wing with controllable camber. We then show that curvature-based sensing allows accurate estimation of disturbances in the angle of attack. Finally, we demonstrate that a controller leveraging these proprioceptive estimates can reject disturbances in the lift response of the soft wing. By combining proprioceptive sensing with a disturbance observer, this technique mirrors biological strategies and provides a pathway for soft underwater vehicles to maintain stability in hazardous environments.

