---
layout: default
title: Expertise need not monopolize: Action-Specialized Mixture of Experts for Vision-Language-Action Learning
---

# Expertise need not monopolize: Action-Specialized Mixture of Experts for Vision-Language-Action Learning
**arXiv**：[2510.14300v1](https://arxiv.org/abs/2510.14300) · [PDF](https://arxiv.org/pdf/2510.14300.pdf)  
**作者**：Weijie Shen, Yitian Liu, Yuhao Wu, Zhixuan Liang, Sijia Gu, Dehui Wang, Tian Nian, Lei Xu, Yusen Qin, Jiangmiao Pang, Xinping Guan, Xiaokang Yang, Yao Mu  

**一句话要点**：提出AdaMoE以解决视觉-语言-动作模型扩展中的计算效率与性能平衡问题

**关键词**：视觉-语言-动作模型, 专家混合架构, 机器人操作, 稀疏激活, 实时控制, 模型扩展

## 3 点简述
- 核心问题：VLA模型扩展需高计算资源与稀缺机器人数据，实时控制需平衡模型容量与效率
- 方法要点：采用MoE架构继承预训练权重，通过解耦专家选择与权重实现协作专家利用
- 实验或效果：在LIBERO和RoboTwin基准上性能提升1.8%和9.3%，真实世界实验提升21.5%

## 摘要（原文）

> Vision-Language-Action (VLA) models are experiencing rapid development and
> demonstrating promising capabilities in robotic manipulation tasks. However,
> scaling up VLA models presents several critical challenges: (1) Training new
> VLA models from scratch demands substantial computational resources and
> extensive datasets. Given the current scarcity of robot data, it becomes
> particularly valuable to fully leverage well-pretrained VLA model weights
> during the scaling process. (2) Real-time control requires carefully balancing
> model capacity with computational efficiency. To address these challenges, We
> propose AdaMoE, a Mixture-of-Experts (MoE) architecture that inherits
> pretrained weights from dense VLA models, and scales up the action expert by
> substituting the feedforward layers into sparsely activated MoE layers. AdaMoE
> employs a decoupling technique that decouples expert selection from expert
> weighting through an independent scale adapter working alongside the
> traditional router. This enables experts to be selected based on task relevance
> while contributing with independently controlled weights, allowing
> collaborative expert utilization rather than winner-takes-all dynamics. Our
> approach demonstrates that expertise need not monopolize. Instead, through
> collaborative expert utilization, we can achieve superior performance while
> maintaining computational efficiency. AdaMoE consistently outperforms the
> baseline model across key benchmarks, delivering performance gains of 1.8% on
> LIBERO and 9.3% on RoboTwin. Most importantly, a substantial 21.5% improvement
> in real-world experiments validates its practical effectiveness for robotic
> manipulation tasks.

