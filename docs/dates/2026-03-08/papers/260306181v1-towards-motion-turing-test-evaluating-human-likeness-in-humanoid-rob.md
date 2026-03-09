---
layout: default
title: Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots
---

# Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots
**arXiv**：[2603.06181v1](https://arxiv.org/abs/2603.06181) · [PDF](https://arxiv.org/pdf/2603.06181.pdf)  
**作者**：Mingzhe Li, Mengyin Liu, Zekai Wu, Xincheng Lin, Junsheng Zhang, Ming Yan, Zengye Xie, Changwang Zhang, Chenglu Wen, Lan Xu, Siqi Shen, Cheng Wang  

**一句话要点**：提出运动图灵测试框架，评估人形机器人运动的人性化程度

**关键词**：运动图灵测试, 人形机器人, 运动相似性评估, HHMotion数据集, SMPL-X表示, 人性化评分预测

## 3 点简述
- 核心问题：如何客观评估人形机器人运动与人类运动的相似性，消除外观影响。
- 方法要点：构建HHMotion数据集，包含人类和人形机器人的SMPL-X运动序列，并收集人工评分。
- 实验或效果：分析显示机器人运动在动态动作中偏差明显，提出基线模型优于现有LLM方法。

## 摘要（原文）

> Humanoid robots have achieved significant progress in motion generation and control, exhibiting movements that appear increasingly natural and human-like. Inspired by the Turing Test, we propose the Motion Turing Test, a framework that evaluates whether human observers can discriminate between humanoid robot and human poses using only kinematic information. To facilitate this evaluation, we present the Human-Humanoid Motion (HHMotion) dataset, which consists of 1,000 motion sequences spanning 15 action categories, performed by 11 humanoid models and 10 human subjects. All motion sequences are converted into SMPL-X representations to eliminate the influence of visual appearance. We recruited 30 annotators to rate the human-likeness of each pose on a 0-5 scale, resulting in over 500 hours of annotation. Analysis of the collected data reveals that humanoid motions still exhibit noticeable deviations from human movements, particularly in dynamic actions such as jumping, boxing, and running. Building on HHMotion, we formulate a human-likeness evaluation task that aims to automatically predict human-likeness scores from motion data. Despite recent progress in multimodal large language models, we find that they remain inadequate for assessing motion human-likeness. To address this, we propose a simple baseline model and demonstrate that it outperforms several contemporary LLM-based methods. The dataset, code, and benchmark will be publicly released to support future research in the community.

