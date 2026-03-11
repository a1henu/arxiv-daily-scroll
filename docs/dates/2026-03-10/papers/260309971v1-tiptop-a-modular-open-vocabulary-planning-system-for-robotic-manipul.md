---
layout: default
title: TiPToP: A Modular Open-Vocabulary Planning System for Robotic Manipulation
---

# TiPToP: A Modular Open-Vocabulary Planning System for Robotic Manipulation
**arXiv**：[2603.09971v1](https://arxiv.org/abs/2603.09971) · [PDF](https://arxiv.org/pdf/2603.09971.pdf)  
**作者**：William Shen, Nishanth Kumar, Sahit Chintalapudi, Jie Wang, Christopher Watson, Edward Hu, Jing Cao, Dinesh Jayaraman, Leslie Pack Kaelbling, Tomás Lozano-Pérez  

**一句话要点**：提出TiPToP模块化系统，结合预训练视觉基础模型与任务运动规划器，从RGB图像和自然语言指令解决机器人多步操作任务。

**关键词**：机器人操作, 模块化系统, 任务运动规划, 视觉语言模型, 零机器人数据, 开源发布

## 3 点简述
- 核心问题：如何从RGB图像和自然语言指令直接解决机器人多步操作任务，无需机器人数据。
- 方法要点：模块化架构集成预训练视觉基础模型与现有任务运动规划器，易于安装和适配新机器人。
- 实验或效果：在28个桌面操作任务中评估，匹配或优于基于350小时演示微调的视觉语言动作模型，并分析失败模式。

## 摘要（原文）

> We present TiPToP, an extensible modular system that combines pretrained vision foundation models with an existing Task and Motion Planner (TAMP) to solve multi-step manipulation tasks directly from input RGB images and natural-language instructions. Our system aims to be simple and easy-to-use: it can be installed and run on a standard DROID setup in under one hour and adapted to new embodiments with minimal effort. We evaluate TiPToP -- which requires zero robot data -- over 28 tabletop manipulation tasks in simulation and the real world and find it matches or outperforms $π_{0.5}\text{-DROID}$, a vision-language-action (VLA) model fine-tuned on 350 hours of embodiment-specific demonstrations. TiPToP's modular architecture enables us to analyze the system's failure modes at the component level. We analyze results from an evaluation of 173 trials and identify directions for improvement. We release TiPToP open-source to further research on modular manipulation systems and tighter integration between learning and planning. Project website and code: https://tiptop-robot.github.io

