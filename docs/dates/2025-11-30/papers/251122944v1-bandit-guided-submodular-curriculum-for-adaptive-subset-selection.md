---
layout: default
title: Bandit Guided Submodular Curriculum for Adaptive Subset Selection
---

# Bandit Guided Submodular Curriculum for Adaptive Subset Selection
**arXiv**：[2511.22944v1](https://arxiv.org/abs/2511.22944) · [PDF](https://arxiv.org/pdf/2511.22944.pdf)  
**作者**：Prateek Chanda, Prayas Agrawal, Saral Sureka, Lokesh Reddy Polu, Atharv Kshirsagar, Ganesh Ramakrishnan  

**一句话要点**：提出ONLINESUBMOD，将自适应子集选择建模为多臂老虎机问题以优化课程学习。

**关键词**：课程学习, 自适应子集选择, 多臂老虎机, 子模函数, 在线优化, 验证驱动奖励

## 3 点简述
- 传统课程学习依赖难以定义的难度概念，限制了自适应样本选择。
- 将子集选择重新解释为多臂老虎机，每臂对应子模函数，提出在线贪婪策略ONLINESUBMOD实现无遗憾性能。
- 在视觉和语言数据集上，ONLINESUBMOD超越传统课程学习和双层优化方法，展示更优的准确率-效率权衡。

## 摘要（原文）

> Traditional curriculum learning proceeds from easy to hard samples, yet defining a reliable notion of difficulty remains elusive. Prior work has used submodular functions to induce difficulty scores in curriculum learning. We reinterpret adaptive subset selection and formulate it as a multi-armed bandit problem, where each arm corresponds to a submodular function guiding sample selection. We introduce ONLINESUBMOD, a novel online greedy policy that optimizes a utility-driven reward and provably achieves no-regret performance under various sampling regimes. Empirically, ONLINESUBMOD outperforms both traditional curriculum learning and bi-level optimization approaches across vision and language datasets, showing superior accuracy-efficiency tradeoffs. More broadly, we show that validationdriven reward metrics offer a principled way to guide the curriculum schedule.

