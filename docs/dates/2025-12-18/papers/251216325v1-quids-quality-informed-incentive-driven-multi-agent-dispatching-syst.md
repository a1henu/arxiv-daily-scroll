---
layout: default
title: QUIDS: Quality-informed Incentive-driven Multi-agent Dispatching System for Mobile Crowdsensing
---

# QUIDS: Quality-informed Incentive-driven Multi-agent Dispatching System for Mobile Crowdsensing
**arXiv**：[2512.16325v1](https://arxiv.org/abs/2512.16325) · [PDF](https://arxiv.org/pdf/2512.16325.pdf)  
**作者**：Nan Zhou, Zuxin Li, Fanhang Man, Xuecheng Chen, Susu Xu, Fan Dang, Chaopeng Hong, Yunhao Liu, Xiao-Ping Zhang, Xinlei Chen  

**一句话要点**：提出QUIDS系统以解决非专用车载移动群智感知中的信息质量优化问题

**关键词**：移动群智感知, 信息质量优化, 激励机制, 多智能体调度, 感知覆盖, 感知可靠性

## 3 点简述
- 核心问题：非专用车载移动群智感知中，感知覆盖、可靠性和车辆动态参与相互关联，影响信息质量
- 方法要点：引入聚合感知质量指标，结合覆盖和可靠性，设计质量感知激励机制和多智能体调度算法
- 实验或效果：基于真实数据评估，QUIDS提升聚合感知质量38%，优于现有方法10%，并显著降低重建地图误差

## 摘要（原文）

> This paper addresses the challenge of achieving optimal Quality of Information (QoI) in non-dedicated vehicular mobile crowdsensing (NVMCS) systems. The key obstacles are the interrelated issues of sensing coverage, sensing reliability, and the dynamic participation of vehicles. To tackle these, we propose QUIDS, a QUality-informed Incentive-driven multi-agent Dispatching System, which ensures high sensing coverage and reliability under budget constraints. QUIDS introduces a novel metric, Aggregated Sensing Quality (ASQ), to quantitatively capture QoI by integrating both coverage and reliability. We also develop a Mutually Assisted Belief-aware Vehicle Dispatching algorithm that estimates sensing reliability and allocates incentives under uncertainty, further improving ASQ. Evaluation using real-world data from a metropolitan NVMCS deployment shows QUIDS improves ASQ by 38% over non-dispatching scenarios and by 10% over state-of-the-art methods. It also reduces reconstruction map errors by 39-74% across algorithms. By jointly optimizing coverage and reliability via a quality-informed incentive mechanism, QUIDS enables low-cost, high-quality urban monitoring without dedicated infrastructure, applicable to smart-city scenarios like traffic and environmental sensing.

