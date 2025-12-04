---
layout: default
title: Prediction-Driven Motion Planning: Route Integration Strategies in Attention-Based Prediction Models
---

# Prediction-Driven Motion Planning: Route Integration Strategies in Attention-Based Prediction Models
**arXiv**：[2512.03756v1](https://arxiv.org/abs/2512.03756) · [PDF](https://arxiv.org/pdf/2512.03756.pdf)  
**作者**：Marlon Steiner, Royden Wagner, Ömer Sahin Tas, Christoph Stiller  

**一句话要点**：提出基于注意力的预测模型集成导航信息策略，以增强自动驾驶车辆交互与规划。

**关键词**：运动预测, 运动规划, 注意力模型, 导航集成, 自动驾驶交互, nuPlan数据集

## 3 点简述
- 核心问题：结合运动预测与规划时，如何基于导航目标进行预测并确保轨迹稳定可行。
- 方法要点：通过将自车意图路线和目标姿态集成到模型架构中，提出多种导航集成策略。
- 实验或效果：在nuPlan数据集上评估，展示导航信息能提升预测和规划任务性能。

## 摘要（原文）

> Combining motion prediction and motion planning offers a promising framework for enhancing interactions between automated vehicles and other traffic participants. However, this introduces challenges in conditioning predictions on navigation goals and ensuring stable, kinematically feasible trajectories. Addressing the former challenge, this paper investigates the extension of attention-based motion prediction models with navigation information. By integrating the ego vehicle's intended route and goal pose into the model architecture, we bridge the gap between multi-agent motion prediction and goal-based motion planning. We propose and evaluate several architectural navigation integration strategies to our model on the nuPlan dataset. Our results demonstrate the potential of prediction-driven motion planning, highlighting how navigation information can enhance both prediction and planning tasks. Our implementation is at: https://github.com/KIT-MRT/future-motion.

