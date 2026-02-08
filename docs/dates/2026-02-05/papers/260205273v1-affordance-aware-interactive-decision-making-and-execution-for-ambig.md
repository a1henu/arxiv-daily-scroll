---
layout: default
title: Affordance-Aware Interactive Decision-Making and Execution for Ambiguous Instructions
---

# Affordance-Aware Interactive Decision-Making and Execution for Ambiguous Instructions
**arXiv**：[2602.05273v1](https://arxiv.org/abs/2602.05273) · [PDF](https://arxiv.org/pdf/2602.05273.pdf)  
**作者**：Hengxuan Xu, Fengbo Lan, Zhixin Zhao, Shengjie Wang, Mengqiao Liu, Jieqian Sun, Yu Cheng, Tao Zhang  

**一句话要点**：提出AIDE框架以解决机器人执行模糊指令时交互决策与执行的挑战

**关键词**：机器人决策, 视觉语言模型, 交互探索, 模糊指令理解, 可供性分析, 实时执行

## 3 点简述
- 核心问题：现有VLM方法在模糊指令下识别任务相关对象时，推理效率低且缺乏环境交互，阻碍实时任务执行
- 方法要点：AIDE采用双流框架，集成交互探索与视觉语言推理，实现零样本可供性分析和模糊指令解释
- 实验或效果：在仿真和真实环境中，AIDE任务规划成功率超80%，闭环执行准确率超95%，优于现有VLM方法

## 摘要（原文）

> Enabling robots to explore and act in unfamiliar environments under ambiguous human instructions by interactively identifying task-relevant objects (e.g., identifying cups or beverages for "I'm thirsty") remains challenging for existing vision-language model (VLM)-based methods. This challenge stems from inefficient reasoning and the lack of environmental interaction, which hinder real-time task planning and execution. To address this, We propose Affordance-Aware Interactive Decision-Making and Execution for Ambiguous Instructions (AIDE), a dual-stream framework that integrates interactive exploration with vision-language reasoning, where Multi-Stage Inference (MSI) serves as the decision-making stream and Accelerated Decision-Making (ADM) as the execution stream, enabling zero-shot affordance analysis and interpretation of ambiguous instructions. Extensive experiments in simulation and real-world environments show that AIDE achieves the task planning success rate of over 80\% and more than 95\% accuracy in closed-loop continuous execution at 10 Hz, outperforming existing VLM-based methods in diverse open-world scenarios.

