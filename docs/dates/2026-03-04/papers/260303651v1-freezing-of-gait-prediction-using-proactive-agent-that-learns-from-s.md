---
layout: default
title: Freezing of Gait Prediction using Proactive Agent that Learns from Selected Experience and DDQN Algorithm
---

# Freezing of Gait Prediction using Proactive Agent that Learns from Selected Experience and DDQN Algorithm
**arXiv**：[2603.03651v1](https://arxiv.org/abs/2603.03651) · [PDF](https://arxiv.org/pdf/2603.03651.pdf)  
**作者**：Septian Enggar Sukmana, Sang Won Bae, Tomohiro Shibata  

**一句话要点**：提出基于DDQN与优先经验回放的强化学习框架，用于预测帕金森病步态冻结，以支持主动干预。

**关键词**：步态冻结预测, 强化学习, 双深度Q网络, 优先经验回放, 帕金森病干预, 可穿戴设备

## 3 点简述
- 核心问题：帕金森病步态冻结的及时准确预测，以降低跌倒风险并提升移动能力。
- 方法要点：采用双深度Q网络结合优先经验回放，通过奖励塑形策略优化决策，实现步态冻结前兆点识别。
- 实验或效果：在独立和依赖受试者评估中，预测时间分别达8.72秒和7.89秒，展示模型在可穿戴设备中的集成潜力。

## 摘要（原文）

> Freezing of Gait (FOG) is a debilitating motor symptom commonly experienced by individuals with Parkinson's Disease (PD) which often leads to falls and reduced mobility. Timely and accurate prediction of FOG episodes is essential for enabling proactive interventions through assistive technologies. This study presents a reinforcement learning-based framework designed to identify optimal pre-FOG onset points, thereby extending the prediction horizon for anticipatory cueing systems. The model implements a Double Deep Q-Network (DDQN) architecture enhanced with Prioritized Experience Replay (PER) allowing the agent to focus learning on high-impact experiences and refine its policy. Trained over 9000 episodes with a reward shaping strategy that promotes cautious decision-making, the agent demonstrated robust performance in both subject-dependent and subject-independent evaluations. The model achieved a prediction horizon of up to 8.72 seconds prior to FOG onset in subject-independent scenarios and 7.89 seconds in subject-dependent settings. These results highlight the model's potential for integration into wearable assistive devices, offering timely and personalized interventions to mitigate FOG in PD patients.

