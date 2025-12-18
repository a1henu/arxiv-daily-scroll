---
layout: default
title: See It Before You Grab It: Deep Learning-based Action Anticipation in Basketball
---

# See It Before You Grab It: Deep Learning-based Action Anticipation in Basketball
**arXiv**：[2512.15386v1](https://arxiv.org/abs/2512.15386) · [PDF](https://arxiv.org/pdf/2512.15386.pdf)  
**作者**：Arnau Barrera Roy, Albert Clapés Sintes  

**一句话要点**：提出基于深度学习的篮球动作预测方法，以解决投篮后篮板球归属的实时预测问题。

**关键词**：动作预测, 篮球视频分析, 深度学习, 篮板预测, 视频理解, 多智能体场景

## 3 点简述
- 核心问题：篮球视频中动作预测任务，特别是投篮后篮板球归属的预测，现有研究较少。
- 方法要点：构建包含10万视频片段的自定义数据集，应用先进动作预测方法进行基准测试。
- 实验或效果：实验验证了篮板预测的可行性与挑战，支持实时广播和赛后分析应用。

## 摘要（原文）

> Computer vision and video understanding have transformed sports analytics by enabling large-scale, automated analysis of game dynamics from broadcast footage. Despite significant advances in player and ball tracking, pose estimation, action localization, and automatic foul recognition, anticipating actions before they occur in sports videos has received comparatively little attention. This work introduces the task of action anticipation in basketball broadcast videos, focusing on predicting which team will gain possession of the ball following a shot attempt. To benchmark this task, a new self-curated dataset comprising 100,000 basketball video clips, over 300 hours of footage, and more than 2,000 manually annotated rebound events is presented. Comprehensive baseline results are reported using state-of-the-art action anticipation methods, representing the first application of deep learning techniques to basketball rebound prediction. Additionally, two complementary tasks, rebound classification and rebound spotting, are explored, demonstrating that this dataset supports a wide range of video understanding applications in basketball, for which no comparable datasets currently exist. Experimental results highlight both the feasibility and inherent challenges of anticipating rebounds, providing valuable insights into predictive modeling for dynamic multi-agent sports scenarios. By forecasting team possession before rebounds occur, this work enables applications in real-time automated broadcasting and post-game analysis tools to support decision-making.

