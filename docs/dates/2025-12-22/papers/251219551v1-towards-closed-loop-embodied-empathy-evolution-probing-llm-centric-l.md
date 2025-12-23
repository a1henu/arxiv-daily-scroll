---
layout: default
title: Towards Closed-Loop Embodied Empathy Evolution: Probing LLM-Centric Lifelong Empathic Motion Generation in Unseen Scenarios
---

# Towards Closed-Loop Embodied Empathy Evolution: Probing LLM-Centric Lifelong Empathic Motion Generation in Unseen Scenarios
**arXiv**：[2512.19551v1](https://arxiv.org/abs/2512.19551) · [PDF](https://arxiv.org/pdf/2512.19551.pdf)  
**作者**：Jiawen Wang, Jingjing Wang Tianyang Chen, Min Zhang, Guodong Zhou  

**一句话要点**：提出ES-MoE方法以解决LLM在未见场景中持续学习情感运动生成的问题

**关键词**：情感运动生成, 终身学习, 大语言模型, 未见场景适应, 专家混合模型, 因果引导

## 3 点简述
- 现有方法局限于固定数据集，忽视灵活多变的运动场景，导致泛化能力不足
- 提出ES-MoE方法，通过因果引导情感解耦和场景适应专家构建块应对情感解耦与场景适应挑战
- 构建多个L^2-EMG数据集验证，实验显示ES-MoE优于先进基线

## 摘要（原文）

> In the literature, existing human-centric emotional motion generation methods primarily focus on boosting performance within a single scale-fixed dataset, largely neglecting the flexible and scale-increasing motion scenarios (e.g., sports, dance), whereas effectively learning these newly emerging scenarios can significantly enhance the model's real-world generalization ability. Inspired by this, this paper proposes a new LLM-Centric Lifelong Empathic Motion Generation (L^2-EMG) task, which aims to equip LLMs with the capability to continually acquire emotional motion generation knowledge across different unseen scenarios, potentially contributing to building a closed-loop and self-evolving embodied agent equipped with both empathy and intelligence. Further, this paper poses two key challenges in the L^2-EMG task, i.e., the emotion decoupling challenge and the scenario adapting challenge. To this end, this paper proposes an Emotion-Transferable and Scenario-Adapted Mixture of Experts (ES-MoE) approach which designs a causal-guided emotion decoupling block and a scenario-adapted expert constructing block to address the two challenges, respectively. Especially, this paper constructs multiple L^2-EMG datasets to validate the effectiveness of the ES-MoE approach. Extensive evaluations show that ES-MoE outperforms advanced baselines.

