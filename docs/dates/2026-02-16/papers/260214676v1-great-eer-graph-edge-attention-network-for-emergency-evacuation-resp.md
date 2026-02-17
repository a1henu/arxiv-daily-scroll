---
layout: default
title: GREAT-EER: Graph Edge Attention Network for Emergency Evacuation Responses
---

# GREAT-EER: Graph Edge Attention Network for Emergency Evacuation Responses
**arXiv**：[2602.14676v1](https://arxiv.org/abs/2602.14676) · [PDF](https://arxiv.org/pdf/2602.14676.pdf)  
**作者**：Attila Lischka, Balázs Kulcsár  

**一句话要点**：提出基于图边注意网络的深度强化学习方法以解决公交疏散导向问题

**关键词**：公交疏散, 图边注意网络, 深度强化学习, 组合优化, 应急响应, 城市疏散

## 3 点简述
- 核心问题：定义公交疏散导向问题，旨在短时间内用公交车从受影响区域疏散最多人员
- 方法要点：利用图学习和深度强化学习，训练后能快速生成疏散路线
- 实验或效果：在旧金山真实路网场景中验证，实现近最优解并分析所需车辆数

## 摘要（原文）

> Emergency situations that require the evacuation of urban areas can arise from man-made causes (e.g., terrorist attacks or industrial accidents) or natural disasters, the latter becoming more frequent due to climate change. As a result, effective and fast methods to develop evacuation plans are of great importance. In this work, we identify and propose the Bus Evacuation Orienteering Problem (BEOP), an NP-hard combinatorial optimization problem with the goal of evacuating as many people from an affected area by bus in a short, predefined amount of time. The purpose of bus-based evacuation is to reduce congestion and disorder that arises in purely car-focused evacuation scenarios. To solve the BEOP, we propose a deep reinforcement learning-based method utilizing graph learning, which, once trained, achieves fast inference speed and is able to create evacuation routes in fractions of seconds. We can bound the gap of our evacuation plans using an MILP formulation. To validate our method, we create evacuation scenarios for San Francisco using real-world road networks and travel times. We show that we achieve near-optimal solution quality and are further able to investigate how many evacuation vehicles are necessary to achieve certain bus-based evacuation quotas given a predefined evacuation time while keeping run time adequate.

