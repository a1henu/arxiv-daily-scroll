---
layout: default
title: A General One-Shot Multimodal Active Perception Framework for Robotic Manipulation: Learning to Predict Optimal Viewpoint
---

# A General One-Shot Multimodal Active Perception Framework for Robotic Manipulation: Learning to Predict Optimal Viewpoint
**arXiv**：[2601.13639v1](https://arxiv.org/abs/2601.13639) · [PDF](https://arxiv.org/pdf/2601.13639.pdf)  
**作者**：Deyun Qin, Zezhi Liu, Hanqian Luo, Xiao Liang, Yongchun Fang  

**一句话要点**：提出一次性多模态主动感知框架，通过预测最优视点提升机器人抓取成功率

**关键词**：主动感知, 机器人抓取, 多模态融合, 视点预测, 仿真到现实迁移

## 3 点简述
- 核心问题：现有主动感知方法依赖迭代优化，成本高且任务耦合，限制可迁移性
- 方法要点：框架解耦视点质量评估，通过跨注意力融合多模态特征直接预测相机位姿调整
- 实验或效果：在视点受限环境中显著提高抓取成功率，实现无额外微调的仿真到现实迁移

## 摘要（原文）

> Active perception in vision-based robotic manipulation aims to move the camera toward more informative observation viewpoints, thereby providing high-quality perceptual inputs for downstream tasks. Most existing active perception methods rely on iterative optimization, leading to high time and motion costs, and are tightly coupled with task-specific objectives, which limits their transferability. In this paper, we propose a general one-shot multimodal active perception framework for robotic manipulation. The framework enables direct inference of optimal viewpoints and comprises a data collection pipeline and an optimal viewpoint prediction network. Specifically, the framework decouples viewpoint quality evaluation from the overall architecture, supporting heterogeneous task requirements. Optimal viewpoints are defined through systematic sampling and evaluation of candidate viewpoints, after which large-scale training datasets are constructed via domain randomization. Moreover, a multimodal optimal viewpoint prediction network is developed, leveraging cross-attention to align and fuse multimodal features and directly predict camera pose adjustments. The proposed framework is instantiated in robotic grasping under viewpoint-constrained environments. Experimental results demonstrate that active perception guided by the framework significantly improves grasp success rates. Notably, real-world evaluations achieve nearly double the grasp success rate and enable seamless sim-to-real transfer without additional fine-tuning, demonstrating the effectiveness of the proposed framework.

