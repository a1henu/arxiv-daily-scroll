---
layout: default
title: GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation
---

# GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation
**arXiv**：[2512.01801v1](https://arxiv.org/abs/2512.01801) · [PDF](https://arxiv.org/pdf/2512.01801.pdf)  
**作者**：Yunfei Li, Xiao Ma, Jiafeng Xu, Yu Cui, Zhongren Cui, Zhigang Han, Liqun Huang, Tao Kong, Yuxiao Liu, Hao Niu, Wanli Peng, Jingchao Qiao, Zeyu Ren, Haixin Shi, Zhi Su, Jiawen Tian, Yuyang Xiao, Shenyu Zhang, Liwei Zheng, Hang Li, Yonghui Wu  

**一句话要点**：提出GR-RL框架，通过多阶段训练将通用VLA策略转化为长时程灵巧操控专家。

**关键词**：机器人学习, 长时程操控, 灵巧操作, 强化学习, 视觉语言动作策略, 轨迹过滤

## 3 点简述
- 核心问题：现有VLA策略依赖人类演示，但在灵巧精确任务中演示存在噪声和次优性。
- 方法要点：采用多阶段训练，包括基于离线RL的轨迹过滤、形态对称增强和在线RL的潜在空间噪声预测。
- 实验或效果：首次实现基于学习的策略自主系鞋带，成功率83.3%，需毫米级精度和软体交互。

## 摘要（原文）

> We present GR-RL, a robotic learning framework that turns a generalist vision-language-action (VLA) policy into a highly capable specialist for long-horizon dexterous manipulation. Assuming the optimality of human demonstrations is core to existing VLA policies. However, we claim that in highly dexterous and precise manipulation tasks, human demonstrations are noisy and suboptimal. GR-RL proposes a multi-stage training pipeline that filters, augments, and reinforces the demonstrations by reinforcement learning. First, GR-RL learns a vision-language-conditioned task progress, filters the demonstration trajectories, and only keeps the transitions that contribute positively to the progress. Specifically, we show that by directly applying offline RL with sparse reward, the resulting $Q$-values can be treated as a robust progress function. Next, we introduce morphological symmetry augmentation that greatly improves the generalization and performance of GR-RL. Lastly, to better align the VLA policy with its deployment behaviors for high-precision control, we perform online RL by learning a latent space noise predictor. With this pipeline, GR-RL is, to our knowledge, the first learning-based policy that can autonomously lace up a shoe by threading shoelaces through multiple eyelets with an 83.3% success rate, a task requiring long-horizon reasoning, millimeter-level precision, and compliant soft-body interaction. We hope GR-RL provides a step toward enabling generalist robot foundations models to specialize into reliable real-world experts.

