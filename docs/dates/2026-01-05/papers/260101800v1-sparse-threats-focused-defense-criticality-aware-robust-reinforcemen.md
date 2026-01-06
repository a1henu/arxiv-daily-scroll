---
layout: default
title: Sparse Threats, Focused Defense: Criticality-Aware Robust Reinforcement Learning for Safe Autonomous Driving
---

# Sparse Threats, Focused Defense: Criticality-Aware Robust Reinforcement Learning for Safe Autonomous Driving
**arXiv**：[2601.01800v1](https://arxiv.org/abs/2601.01800) · [PDF](https://arxiv.org/pdf/2601.01800.pdf)  
**作者**：Qi Wei, Junchao Fan, Zhao Yang, Jianhua Wang, Jingkai Mao, Xiaolin Chang  

**一句话要点**：提出CARRL方法以解决自动驾驶中稀疏安全风险的鲁棒强化学习问题

**关键词**：自动驾驶, 鲁棒强化学习, 对抗训练, 稀疏风险, 一般和博弈, 安全关键场景

## 3 点简述
- 现有对抗训练方法忽视风险稀疏性和不对称性，导致鲁棒性不足
- CARRL包含风险暴露对手和风险目标鲁棒代理，建模为一般和博弈
- 实验显示碰撞率降低至少22.66%，优于基线方法

## 摘要（原文）

> Reinforcement learning (RL) has shown considerable potential in autonomous driving (AD), yet its vulnerability to perturbations remains a critical barrier to real-world deployment. As a primary countermeasure, adversarial training improves policy robustness by training the AD agent in the presence of an adversary that deliberately introduces perturbations. Existing approaches typically model the interaction as a zero-sum game with continuous attacks. However, such designs overlook the inherent asymmetry between the agent and the adversary and then fail to reflect the sparsity of safety-critical risks, rendering the achieved robustness inadequate for practical AD scenarios. To address these limitations, we introduce criticality-aware robust RL (CARRL), a novel adversarial training approach for handling sparse, safety-critical risks in autonomous driving. CARRL consists of two interacting components: a risk exposure adversary (REA) and a risk-targeted robust agent (RTRA). We model the interaction between the REA and RTRA as a general-sum game, allowing the REA to focus on exposing safety-critical failures (e.g., collisions) while the RTRA learns to balance safety with driving efficiency. The REA employs a decoupled optimization mechanism to better identify and exploit sparse safety-critical moments under a constrained budget. However, such focused attacks inevitably result in a scarcity of adversarial data. The RTRA copes with this scarcity by jointly leveraging benign and adversarial experiences via a dual replay buffer and enforces policy consistency under perturbations to stabilize behavior. Experimental results demonstrate that our approach reduces the collision rate by at least 22.66\% across all cases compared to state-of-the-art baseline methods.

