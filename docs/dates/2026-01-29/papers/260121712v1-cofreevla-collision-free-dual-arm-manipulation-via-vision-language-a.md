---
layout: default
title: CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation
---

# CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation
**arXiv**：[2601.21712v1](https://arxiv.org/abs/2601.21712) · [PDF](https://arxiv.org/pdf/2601.21712.pdf)  
**作者**：Xuanran Zhai, Binkai Ou, Yemin Wang, Hui Yi Leong, Qiaojun Yu, Ce Hao, Yaohua Liu  

**一句话要点**：提出CoFreeVLA，通过视觉-语言-动作模型和风险估计解决双机械臂操作中的自碰撞问题

**关键词**：双机械臂操作, 视觉-语言-动作模型, 自碰撞风险估计, 机器人安全控制, 端到端学习

## 3 点简述
- 核心问题：双机械臂操作中，视觉-语言-动作模型因未充分建模臂间和抓取物体自碰撞而存在安全隐患
- 方法要点：引入短时域自碰撞风险估计器，基于本体感知、视觉嵌入和计划动作预测碰撞概率，并用于门控风险命令和策略优化
- 实验或效果：在PiPER机器人上测试五个双任务，相比RDT和APEX，减少自碰撞并提高成功率

## 摘要（原文）

> Vision Language Action (VLA) models enable instruction following manipulation, yet dualarm deployment remains unsafe due to under modeled selfcollisions between arms and grasped objects. We introduce CoFreeVLA, which augments an endtoend VLA with a short horizon selfcollision risk estimator that predicts collision likelihood from proprioception, visual embeddings, and planned actions. The estimator gates risky commands, recovers to safe states via risk-guided adjustments, and shapes policy refinement for safer rollouts. It is pre-trained with model-based collision labels and posttrained on real robot rollouts for calibration. On five bimanual tasks with the PiPER robot arm, CoFreeVLA reduces selfcollisions and improves success rates versus RDT and APEX.

