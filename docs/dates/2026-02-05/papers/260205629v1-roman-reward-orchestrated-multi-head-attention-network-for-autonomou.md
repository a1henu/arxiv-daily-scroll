---
layout: default
title: ROMAN: Reward-Orchestrated Multi-Head Attention Network for Autonomous Driving System Testing
---

# ROMAN: Reward-Orchestrated Multi-Head Attention Network for Autonomous Driving System Testing
**arXiv**：[2602.05629v1](https://arxiv.org/abs/2602.05629) · [PDF](https://arxiv.org/pdf/2602.05629.pdf)  
**作者**：Jianlei Chi, Yuzhen Wu, Jiaxuan Hou, Xiaodong Zhang, Ming Fan, Suhui Sun, Weijun Dai, Bo Li, Jianguo Sun, Jun Sun  

**一句话要点**：提出ROMAN方法，结合多头注意力与交通法规加权机制，生成高风险违规场景以测试自动驾驶系统。

**关键词**：自动驾驶系统测试, 场景生成, 多头注意力网络, 交通法规加权, 高风险违规, 模拟平台

## 3 点简述
- 核心问题：现有测试方法难以生成复杂高风险违规场景，且忽略多车交互与关键情况。
- 方法要点：使用多头注意力建模车辆、信号等交互，并基于LLM的风险加权模块评估违规严重性与发生频率。
- 实验或效果：在CARLA平台测试百度Apollo，ROMAN在违规数量和场景多样性上优于ABEL和LawBreaker，能覆盖所有输入法规条款。

## 摘要（原文）

> Automated Driving System (ADS) acts as the brain of autonomous vehicles, responsible for their safety and efficiency. Safe deployment requires thorough testing in diverse real-world scenarios and compliance with traffic laws like speed limits, signal obedience, and right-of-way rules. Violations like running red lights or speeding pose severe safety risks. However, current testing approaches face significant challenges: limited ability to generate complex and high-risk law-breaking scenarios, and failing to account for complex interactions involving multiple vehicles and critical situations. To address these challenges, we propose ROMAN, a novel scenario generation approach for ADS testing that combines a multi-head attention network with a traffic law weighting mechanism. ROMAN is designed to generate high-risk violation scenarios to enable more thorough and targeted ADS evaluation. The multi-head attention mechanism models interactions among vehicles, traffic signals, and other factors. The traffic law weighting mechanism implements a workflow that leverages an LLM-based risk weighting module to evaluate violations based on the two dimensions of severity and occurrence. We have evaluated ROMAN by testing the Baidu Apollo ADS within the CARLA simulation platform and conducting extensive experiments to measure its performance. Experimental results demonstrate that ROMAN surpassed state-of-the-art tools ABLE and LawBreaker by achieving 7.91% higher average violation count than ABLE and 55.96% higher than LawBreaker, while also maintaining greater scenario diversity. In addition, only ROMAN successfully generated violation scenarios for every clause of the input traffic laws, enabling it to identify more high-risk violations than existing approaches.

