---
layout: default
title: M$^2$-Miner: Multi-Agent Enhanced MCTS for Mobile GUI Agent Data Mining
---

# M$^2$-Miner: Multi-Agent Enhanced MCTS for Mobile GUI Agent Data Mining
**arXiv**：[2602.05429v1](https://arxiv.org/abs/2602.05429) · [PDF](https://arxiv.org/pdf/2602.05429.pdf)  
**作者**：Rui Lv, Juncheng Mo, Tianyi Chu, Chen Rao, Hongyi Jing, Jiajie Teng, Jiafu Chen, Shiqi Zhang, Liangzi Ding, Shuo Fang, Huaizhong Lin, Ziqiang Dang, Chenguang Ma, Lei Zhao  

**一句话要点**：提出M$^2$-Miner框架，基于MCTS和多智能体协作，低成本自动化挖掘移动GUI智能体数据。

**关键词**：移动GUI智能体, 数据挖掘, 蒙特卡洛树搜索, 多智能体系统, 意图轨迹对

## 3 点简述
- 核心问题：移动GUI智能体数据挖掘面临高成本、低质量和低丰富度挑战。
- 方法要点：采用多智能体框架（InferAgent、OrchestraAgent、JudgeAgent）和意图回收策略提升效率与多样性。
- 实验或效果：在多个移动GUI基准测试中，基于挖掘数据微调的智能体达到最先进性能。

## 摘要（原文）

> Graphical User Interface (GUI) agent is pivotal to advancing intelligent human-computer interaction paradigms. Constructing powerful GUI agents necessitates the large-scale annotation of high-quality user-behavior trajectory data (i.e., intent-trajectory pairs) for training. However, manual annotation methods and current GUI agent data mining approaches typically face three critical challenges: high construction cost, poor data quality, and low data richness. To address these issues, we propose M$^2$-Miner, the first low-cost and automated mobile GUI agent data-mining framework based on Monte Carlo Tree Search (MCTS). For better data mining efficiency and quality, we present a collaborative multi-agent framework, comprising InferAgent, OrchestraAgent, and JudgeAgent for guidance, acceleration, and evaluation. To further enhance the efficiency of mining and enrich intent diversity, we design an intent recycling strategy to extract extra valuable interaction trajectories. Additionally, a progressive model-in-the-loop training strategy is introduced to improve the success rate of data mining. Extensive experiments have demonstrated that the GUI agent fine-tuned using our mined data achieves state-of-the-art performance on several commonly used mobile GUI benchmarks. Our work will be released to facilitate the community research.

