---
layout: default
title: Round Outcome Prediction in VALORANT Using Tactical Features from Video Analysis
---

# Round Outcome Prediction in VALORANT Using Tactical Features from Video Analysis
**arXiv**：[2510.17199v1](https://arxiv.org/abs/2510.17199) · [PDF](https://arxiv.org/pdf/2510.17199.pdf)  
**作者**：Nirai Hayakawa, Kazumasa Shimari, Kazuma Yamasaki, Hirotatsu Hoshikawa, Rikuto Tsuchida, Kenichi Matsumoto  

**一句话要点**：提出基于视频战术特征的模型以预测VALORANT回合结果

**关键词**：回合结果预测, 视频分析, 战术特征提取, TimeSformer模型, 电竞数据分析

## 3 点简述
- 核心问题：现有电竞预测多依赖日志数据，缺乏复杂策略分析。
- 方法要点：使用TimeSformer从小地图提取位置和事件特征，增强预测模型。
- 实验效果：模型在回合中后期预测准确率达81%，优于仅用小地图信息。

## 摘要（原文）

> Recently, research on predicting match outcomes in esports has been actively
> conducted, but much of it is based on match log data and statistical
> information. This research targets the FPS game VALORANT, which requires
> complex strategies, and aims to build a round outcome prediction model by
> analyzing minimap information in match footage. Specifically, based on the
> video recognition model TimeSformer, we attempt to improve prediction accuracy
> by incorporating detailed tactical features extracted from minimap information,
> such as character position information and other in-game events. This paper
> reports preliminary results showing that a model trained on a dataset augmented
> with such tactical event labels achieved approximately 81% prediction accuracy,
> especially from the middle phases of a round onward, significantly
> outperforming a model trained on a dataset with the minimap information itself.
> This suggests that leveraging tactical features from match footage is highly
> effective for predicting round outcomes in VALORANT.

