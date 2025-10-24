---
layout: default
title: Dual Control Reference Generation for Optimal Pick-and-Place Execution under Payload Uncertainty
---

# Dual Control Reference Generation for Optimal Pick-and-Place Execution under Payload Uncertainty
**arXiv**：[2510.20483v1](https://arxiv.org/abs/2510.20483) · [PDF](https://arxiv.org/pdf/2510.20483.pdf)  
**作者**：Victor Vantilborgh, Hrishikesh Sathyanarayan, Guillaume Crevecoeur, Ian Abraham, Tom Lefebvre  

**一句话要点**：提出双控制参考轨迹生成方法以解决负载不确定下的机器人抓取任务优化问题

**关键词**：机器人控制, 双控制, 参数不确定性, 参考轨迹生成, 最优控制, 系统辨识

## 3 点简述
- 核心问题：机器人抓取任务在未知负载动态下，需在线参数适应以实现精确模型控制。
- 方法要点：简化双控制问题，预定义反馈策略结构，嵌入参数不确定性或最小化最优性损失。
- 实验或效果：在抓取任务中实现更快、更准确的任务执行和系统辨识，确保稳定控制。

## 摘要（原文）

> This work addresses the problem of robot manipulation tasks under unknown
> dynamics, such as pick-and-place tasks under payload uncertainty, where active
> exploration and(/for) online parameter adaptation during task execution are
> essential to enable accurate model-based control. The problem is framed as dual
> control seeking a closed-loop optimal control problem that accounts for
> parameter uncertainty. We simplify the dual control problem by pre-defining the
> structure of the feedback policy to include an explicit adaptation mechanism.
> Then we propose two methods for reference trajectory generation. The first
> directly embeds parameter uncertainty in robust optimal control methods that
> minimize the expected task cost. The second method considers minimizing the
> so-called optimality loss, which measures the sensitivity of parameter-relevant
> information with respect to task performance. We observe that both approaches
> reason over the Fisher information as a natural side effect of their
> formulations, simultaneously pursuing optimal task execution. We demonstrate
> the effectiveness of our approaches for a pick-and-place manipulation task. We
> show that designing the reference trajectories whilst taking into account the
> control enables faster and more accurate task performance and system
> identification while ensuring stable and efficient control.

