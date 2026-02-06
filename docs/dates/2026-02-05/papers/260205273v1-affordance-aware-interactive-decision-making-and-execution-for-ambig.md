---
layout: default
title: Affordance-Aware Interactive Decision-Making and Execution for Ambiguous Instructions
---

# Affordance-Aware Interactive Decision-Making and Execution for Ambiguous Instructions
**arXiv**：[2602.05273v1](https://arxiv.org/abs/2602.05273) · [PDF](https://arxiv.org/pdf/2602.05273.pdf)  
**作者**：Hengxuan Xu, Fengbo Lan, Zhixin Zhao, Shengjie Wang, Mengqiao Liu, Jieqian Sun, Yu Cheng, Tao Zhang  

**一句话要点**：提出AIDE框架，通过双流交互决策与执行解决机器人模糊指令下的环境探索与任务执行问题。

**关键词**：机器人决策, 视觉语言模型, 模糊指令理解, 交互探索, 可供性分析, 实时执行

## 3 点简述
- 核心问题：现有VLM方法在模糊指令下难以实时规划任务，因推理效率低且缺乏环境交互。
- 方法要点：AIDE集成交互探索与视觉语言推理，采用多阶段推理决策流和加速决策执行流，实现零样本可供性分析。
- 实验或效果：在仿真与真实环境中，任务规划成功率超80%，闭环连续执行准确率超95%于10Hz，优于现有方法。

## 摘要（原文）

> Enabling robots to explore and act in unfamiliar environments under ambiguous human instructions by interactively identifying task-relevant objects (e.g., identifying cups or beverages for "I'm thirsty") remains challenging for existing vision-language model (VLM)-based methods. This challenge stems from inefficient reasoning and the lack of environmental interaction, which hinder real-time task planning and execution. To address this, We propose Affordance-Aware Interactive Decision-Making and Execution for Ambiguous Instructions (AIDE), a dual-stream framework that integrates interactive exploration with vision-language reasoning, where Multi-Stage Inference (MSI) serves as the decision-making stream and Accelerated Decision-Making (ADM) as the execution stream, enabling zero-shot affordance analysis and interpretation of ambiguous instructions. Extensive experiments in simulation and real-world environments show that AIDE achieves the task planning success rate of over 80\% and more than 95\% accuracy in closed-loop continuous execution at 10 Hz, outperforming existing VLM-based methods in diverse open-world scenarios.

