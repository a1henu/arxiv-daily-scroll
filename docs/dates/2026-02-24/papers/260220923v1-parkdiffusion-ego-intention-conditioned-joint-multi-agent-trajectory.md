---
layout: default
title: ParkDiffusion++: Ego Intention Conditioned Joint Multi-Agent Trajectory Prediction for Automated Parking using Diffusion Models
---

# ParkDiffusion++: Ego Intention Conditioned Joint Multi-Agent Trajectory Prediction for Automated Parking using Diffusion Models
**arXiv**：[2602.20923v1](https://arxiv.org/abs/2602.20923) · [PDF](https://arxiv.org/pdf/2602.20923.pdf)  
**作者**：Jiarong Wei, Anna Rehr, Christian Feist, Abhinav Valada  

**一句话要点**：提出ParkDiffusion++，通过扩散模型联合预测自动泊车中的多模态自车意图与多智能体轨迹。

**关键词**：自动泊车, 轨迹预测, 扩散模型, 多智能体交互, 意图预测, 安全引导去噪

## 3 点简述
- 核心问题：自动泊车需预测自车意图及周围智能体的联合响应，现有方法常孤立处理。
- 方法要点：引入自车意图分词器、意图条件联合预测、安全引导去噪器及反事实知识蒸馏。
- 实验或效果：在DLP和inD数据集上达到先进性能，可视化显示智能体对不同意图反应合理。

## 摘要（原文）

> Automated parking is a challenging operational domain for advanced driver assistance systems, requiring robust scene understanding and interaction reasoning. The key challenge is twofold: (i) predict multiple plausible ego intentions according to context and (ii) for each intention, predict the joint responses of surrounding agents, enabling effective what-if decision-making. However, existing methods often fall short, typically treating these interdependent problems in isolation. We propose ParkDiffusion++, which jointly learns a multi-modal ego intention predictor and an ego-conditioned multi-agent joint trajectory predictor for automated parking. Our approach makes several key contributions. First, we introduce an ego intention tokenizer that predicts a small set of discrete endpoint intentions from agent histories and vectorized map polylines. Second, we perform ego-intention-conditioned joint prediction, yielding socially consistent predictions of the surrounding agents for each possible ego intention. Third, we employ a lightweight safety-guided denoiser with different constraints to refine joint scenes during training, thus improving accuracy and safety. Fourth, we propose counterfactual knowledge distillation, where an EMA teacher refined by a frozen safety-guided denoiser provides pseudo-targets that capture how agents react to alternative ego intentions. Extensive evaluations demonstrate that ParkDiffusion++ achieves state-of-the-art performance on the Dragon Lake Parking (DLP) dataset and the Intersections Drone (inD) dataset. Importantly, qualitative what-if visualizations show that other agents react appropriately to different ego intentions.

