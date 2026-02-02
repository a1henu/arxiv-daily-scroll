---
layout: default
title: Guided by Trajectories: Repairing and Rewarding Tool-Use Trajectories for Tool-Integrated Reasoning
---

# Guided by Trajectories: Repairing and Rewarding Tool-Use Trajectories for Tool-Integrated Reasoning
**arXiv**：[2601.23032v1](https://arxiv.org/abs/2601.23032) · [PDF](https://arxiv.org/pdf/2601.23032.pdf)  
**作者**：Siyu Gong, Linan Yue, Weibo Gao, Fangzhou Yao, Shimin Di, Lei Feng, Min-Ling Zhang  

**一句话要点**：提出AutoTraj框架，通过修复和奖励工具使用轨迹以解决工具集成推理中的监督不足问题

**关键词**：工具集成推理, 轨迹修复, 奖励模型, 强化学习, 监督微调

## 3 点简述
- 核心问题：现有工具集成推理方法依赖高质量合成轨迹和稀疏奖励，导致监督有限且偏差大
- 方法要点：采用两阶段框架，包括监督微调阶段修复低质量轨迹和强化学习阶段训练轨迹级奖励模型
- 实验或效果：在真实世界基准测试中验证了AutoTraj在工具集成推理中的有效性

## 摘要（原文）

> Tool-Integrated Reasoning (TIR) enables large language models (LLMs) to solve complex tasks by interacting with external tools, yet existing approaches depend on high-quality synthesized trajectories selected by scoring functions and sparse outcome-based rewards, providing limited and biased supervision for learning TIR. To address these challenges, in this paper, we propose AutoTraj, a two-stage framework that automatically learns TIR by repairing and rewarding tool-use trajectories. Specifically, in the supervised fine-tuning (SFT) stage, AutoTraj generates multiple candidate tool-use trajectories for each query and evaluates them along multiple dimensions. High-quality trajectories are directly retained, while low-quality ones are repaired using a LLM (i.e., LLM-as-Repairer). The resulting repaired and high-quality trajectories form a synthetic SFT dataset, while each repaired trajectory paired with its original low-quality counterpart constitutes a dataset for trajectory preference modeling. In the reinforcement learning (RL) stage, based on the preference dataset, we train a trajectory-level reward model to assess the quality of reasoning paths and combine it with outcome and format rewards, thereby explicitly guiding the optimization toward reliable TIR behaviors. Experiments on real-world benchmarks demonstrate the effectiveness of AutoTraj in TIR.

