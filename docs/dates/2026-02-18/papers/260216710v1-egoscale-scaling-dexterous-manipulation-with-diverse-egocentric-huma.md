---
layout: default
title: EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data
---

# EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data
**arXiv**：[2602.16710v1](https://arxiv.org/abs/2602.16710) · [PDF](https://arxiv.org/pdf/2602.16710.pdf)  
**作者**：Ruijie Zheng, Dantong Niu, Yuqi Xie, Jing Wang, Mengda Xu, Yunfan Jiang, Fernando Castañeda, Fengyuan Hu, You Liang Tan, Letian Fu, Trevor Darrell, Furong Huang, Yuke Zhu, Danfei Xu, Linxi Fan  

**一句话要点**：提出EgoScale框架，利用大规模人类数据提升灵巧操作性能

**关键词**：灵巧操作, 人类数据迁移, 视觉语言动作模型, 两阶段训练, 机器人学习

## 3 点简述
- 核心问题：大规模人类数据能否有效支持高自由度灵巧操作
- 方法要点：基于20,854小时人类视频训练VLA模型，采用两阶段迁移策略
- 实验或效果：在22自由度机械手上成功率提升54%，可迁移至低自由度手

## 摘要（原文）

> Human behavior is among the most scalable sources of data for learning physical intelligence, yet how to effectively leverage it for dexterous manipulation remains unclear. While prior work demonstrates human to robot transfer in constrained settings, it is unclear whether large scale human data can support fine grained, high degree of freedom dexterous manipulation. We present EgoScale, a human to dexterous manipulation transfer framework built on large scale egocentric human data. We train a Vision Language Action (VLA) model on over 20,854 hours of action labeled egocentric human video, more than 20 times larger than prior efforts, and uncover a log linear scaling law between human data scale and validation loss. This validation loss strongly correlates with downstream real robot performance, establishing large scale human data as a predictable supervision source. Beyond scale, we introduce a simple two stage transfer recipe: large scale human pretraining followed by lightweight aligned human robot mid training. This enables strong long horizon dexterous manipulation and one shot task adaptation with minimal robot supervision. Our final policy improves average success rate by 54% over a no pretraining baseline using a 22 DoF dexterous robotic hand, and transfers effectively to robots with lower DoF hands, indicating that large scale human motion provides a reusable, embodiment agnostic motor prior.

