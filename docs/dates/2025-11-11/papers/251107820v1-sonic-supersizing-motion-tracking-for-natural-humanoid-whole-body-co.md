---
layout: default
title: SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control
---

# SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control
**arXiv**：[2511.07820v1](https://arxiv.org/abs/2511.07820) · [PDF](https://arxiv.org/pdf/2511.07820.pdf)  
**作者**：Zhengyi Luo, Ye Yuan, Tingwu Wang, Chenran Li, Sirui Chen, Fernando Castañeda, Zi-Ang Cao, Jiefeng Li, David Minor, Qingwei Ben, Xingye Da, Runyu Ding, Cyrus Hogg, Lina Song, Edy Lim, Eugene Jeong, Tairan He, Haoru Xue, Wenli Xiao, Zi Wang, Simon Yuen, Jan Kautz, Yan Chang, Umar Iqbal, Linxi "Jim" Fan, Yuke Zhu  

**一句话要点**：提出大规模运动跟踪模型以解决人形机器人全身控制问题

**关键词**：人形机器人控制, 运动跟踪, 基础模型, 大规模训练, 全身运动, 多模态输入

## 3 点简述
- 当前人形机器人控制器规模小、行为有限，训练资源不足
- 通过扩展模型参数、数据集和计算量，构建通用运动跟踪基础模型
- 模型支持实时运动规划和多输入接口，提升控制自然性和鲁棒性

## 摘要（原文）

> Despite the rise of billion-parameter foundation models trained across thousands of GPUs, similar scaling gains have not been shown for humanoid control. Current neural controllers for humanoids remain modest in size, target a limited behavior set, and are trained on a handful of GPUs over several days. We show that scaling up model capacity, data, and compute yields a generalist humanoid controller capable of creating natural and robust whole-body movements. Specifically, we posit motion tracking as a natural and scalable task for humanoid control, leverageing dense supervision from diverse motion-capture data to acquire human motion priors without manual reward engineering. We build a foundation model for motion tracking by scaling along three axes: network size (from 1.2M to 42M parameters), dataset volume (over 100M frames, 700 hours of high-quality motion data), and compute (9k GPU hours). Beyond demonstrating the benefits of scale, we show the practical utility of our model through two mechanisms: (1) a real-time universal kinematic planner that bridges motion tracking to downstream task execution, enabling natural and interactive control, and (2) a unified token space that supports various motion input interfaces, such as VR teleoperation devices, human videos, and vision-language-action (VLA) models, all using the same policy. Scaling motion tracking exhibits favorable properties: performance improves steadily with increased compute and data diversity, and learned representations generalize to unseen motions, establishing motion tracking at scale as a practical foundation for humanoid control.

